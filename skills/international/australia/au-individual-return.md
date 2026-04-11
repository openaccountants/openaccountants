---
name: au-individual-return
description: Use this skill whenever asked about Australian individual income tax for sole traders. Trigger on phrases like "how much tax do I pay in Australia", "Australian tax return", "sole trader tax", "ABN tax", "Medicare levy", "LITO", "PAYG", "tax brackets Australia", "BAS", "instant asset write-off", "home office deduction", "HELP repayment", "HECS debt", "small business income tax offset", or any question about filing or computing income tax for an Australian sole trader. This skill covers 2024-25 Stage 3 tax rates, Medicare levy and surcharge, LITO, business income computation, allowable deductions, depreciation, instant asset write-off, small business income tax offset, private health insurance rebate, HELP/HECS repayments, TFN obligations, and final tax computation. ALWAYS read this skill before touching any Australian income tax work.
---

# Australia Individual Income Tax -- Sole Trader Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Australia |
| Jurisdiction Code | AU |
| Primary Legislation | Income Tax Assessment Act 1997 (ITAA 1997); Income Tax Assessment Act 1936 (ITAA 1936) |
| Supporting Legislation | A New Tax System (Medicare Levy Surcharge -- Fringe Benefits) Act 1999; Medicare Levy Act 1986; Tax Administration Act 1953; Higher Education Support Act 2003 |
| Tax Authority | Australian Taxation Office (ATO) |
| Filing Portal | myTax (via myGov) or registered tax agent |
| Contributor | Open Accountants |
| Validated By | Pending -- Australian CPA/CA sign-off required |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Tax Year | 2024-25 (1 July 2024 -- 30 June 2025) |
| Confidence Coverage | Tier 1: rate table application, tax-free threshold, Medicare levy, LITO computation, SBITO computation, HELP repayment thresholds, instant asset write-off eligibility, motor vehicle cents-per-km, home office fixed rate. Tier 2: mixed-use expense apportionment, private health insurance rebate tier selection, motor vehicle logbook method, depreciation effective life estimates, Medicare levy exemption eligibility. Tier 3: CGT events, foreign income, complex trust distributions, non-resident tax, amended assessments, prior year losses with integrity rules. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags and presents options. Qualified accountant must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate and document.

---

## Step 0: Client Onboarding Questions

Before computing any income tax figure, you MUST know:

1. **Residency status** [T1] -- Australian resident for tax purposes, foreign resident, or temporary resident. Determines which rate table and thresholds apply. **This skill covers Australian residents only.**
2. **ABN and TFN status** [T1] -- does the client have an active ABN and TFN?
3. **Gross business income** [T1] -- total business income received or invoiced in the financial year
4. **Business expenses** [T1/T2] -- nature and amount of each expense (T2 for mixed-use items)
5. **Depreciating assets acquired in the year** [T1] -- type, cost, date first used or installed ready for use
6. **Aggregated turnover** [T1] -- required to determine small business entity eligibility (under $10 million)
7. **Other income** [T1] -- employment income (per payment summary/income statement), interest, dividends, rental, capital gains
8. **Private health insurance status** [T2] -- held for full year? Level of cover? Excess amount?
9. **HELP/HECS-HELP debt** [T1] -- does the client have an outstanding study or training loan?
10. **Medicare levy exemption eligibility** [T2] -- any exempt categories (e.g., blind pensioner, foreign aid worker)?
11. **Prior year losses** [T1] -- carried forward tax losses from prior years
12. **PAYG instalments paid** [T1] -- amounts paid during the year via PAYG instalment system
13. **Spouse details** [T2] -- required for Medicare levy surcharge family threshold and PHI rebate

**If residency status is unknown, STOP. Do not apply a rate table. Residency status is mandatory.**

---

## Step 1: Determine Applicable Tax Rates [T1]

**Legislation:** ITAA 1997, Division 4-10; Stage 3 tax cuts effective 1 July 2024

### Australian Resident Tax Rates -- 2024-25

| Taxable Income (AUD) | Rate | Cumulative Tax at Top of Band |
|----------------------|------|-------------------------------|
| $0 -- $18,200 | 0% (tax-free threshold) | $0 |
| $18,201 -- $45,000 | 16% | $4,288 |
| $45,001 -- $135,000 | 30% | $31,288 |
| $135,001 -- $190,000 | 37% | $51,638 |
| $190,001+ | 45% | -- |

**These are the Stage 3 rates effective from 1 July 2024.** The previous 19% rate was reduced to 16%, the 32.5% rate was reduced to 30%, the 37% threshold was raised from $120,000 to $135,000, and the 45% threshold was raised from $180,000 to $190,000.

**The tax-free threshold of $18,200 is NOT a separate personal allowance -- it is built into the rate table as the 0% band.**

---

## Step 2: Medicare Levy [T1]

**Legislation:** Medicare Levy Act 1986

### Standard Rate [T1]

The Medicare levy is **2%** of taxable income, applied on top of income tax.

### Low-Income Reduction [T1]

| Circumstance | No Levy Below | Reduced Levy Phase-In |
|-------------|---------------|----------------------|
| Single (no dependants) | $27,222 | $27,222 -- $34,027 |
| Single (entitled to SAPTO) | $43,846 | $43,846 -- $54,807 |
| Family | $45,907 (+ $4,216 per dependent child after first) | Phase-in to $57,383 |

For individuals in the phase-in range, the Medicare levy = 10% x (taxable income minus lower threshold).

### Medicare Levy Exemption [T2]

Certain categories are exempt (e.g., blind pensioners, foreign aid workers with specific conditions). Flag for reviewer if client claims exemption.

---

## Step 3: Medicare Levy Surcharge (MLS) [T1/T2]

**Legislation:** A New Tax System (Medicare Levy Surcharge -- Fringe Benefits) Act 1999

The MLS applies if the taxpayer does NOT hold an appropriate level of private patient hospital cover and their income for MLS purposes exceeds the threshold.

### MLS Rates -- 2024-25 [T1]

| Income for MLS Purposes (Single) | Income for MLS Purposes (Family) | MLS Rate |
|----------------------------------|----------------------------------|----------|
| $0 -- $93,000 | $0 -- $186,000 | 0% |
| $93,001 -- $108,000 | $186,001 -- $216,000 | 1.0% |
| $108,001 -- $144,000 | $216,001 -- $288,000 | 1.25% |
| $144,001+ | $288,001+ | 1.5% |

Family thresholds increase by $1,500 for each MLS dependent child after the first.

**To avoid the MLS:** hold private patient hospital cover with an excess of $750 or less (singles) or $1,500 or less (couples/families) for the full financial year.

**[T2] Flag:** Confirm whether the client held appropriate cover for the full year. Partial-year cover results in pro-rata MLS.

---

## Step 4: Tax Offsets [T1]

### 4A: Low Income Tax Offset (LITO) [T1]

**Legislation:** ITAA 1997, s 61-520

| Taxable Income (AUD) | LITO Amount |
|----------------------|-------------|
| $0 -- $37,500 | $700 (maximum) |
| $37,501 -- $45,000 | $700 minus 5 cents for every $1 above $37,500 |
| $45,001 -- $66,667 | $325 minus 1.5 cents for every $1 above $45,000 |
| $66,668+ | $0 |

**LITO combined with the tax-free threshold means an individual earning up to approximately $22,575 pays zero income tax (after LITO reduces tax payable to nil).**

LITO is a non-refundable offset -- it can reduce tax payable to zero but cannot create a refund.

The ATO calculates LITO automatically upon lodgment. Do not apply LITO manually in the return -- include it only in the working paper computation.

### 4B: Low and Middle Income Tax Offset (LMITO) [T1]

**LMITO HAS EXPIRED.** The last year LMITO was available was 2021-22. It does NOT apply to the 2024-25 year or any year from 2022-23 onwards. Do not include LMITO in any computation for 2024-25.

### 4C: Small Business Income Tax Offset (SBITO) [T1]

**Legislation:** ITAA 1997, s 61-527

| Condition | Requirement |
|-----------|-------------|
| Entity type | Individual sole trader (or partner/trust beneficiary receiving small business income) |
| Aggregated turnover | Less than $5 million |
| Offset rate | 16% of tax payable on net small business income |
| Maximum offset | $1,000 |

The SBITO is a non-refundable offset. The ATO calculates it automatically based on the net small business income reported in the return.

**Formula:** SBITO = min($1,000, 16% x (basic income tax liability x net small business income / taxable income))

---

## Step 5: Business Income Computation for Sole Traders [T1/T2]

**Legislation:** ITAA 1997, Division 6-5 (ordinary income), Division 8-1 (deductions)

### 5A: Assessable Income [T1]

All amounts derived from carrying on a business are assessable income. This includes:

- Fees for services rendered
- Sales of trading stock
- Government grants and subsidies (including JobKeeper historical, if applicable)
- Insurance recoveries for lost income
- Interest on business bank accounts

**GST:** If registered for GST, report income exclusive of GST. GST collected is not income -- it is remitted to the ATO via the BAS. If not registered for GST, the gross amount received is the income figure.

### 5B: Allowable Deductions -- General Deduction Provision [T1/T2]

**Legislation:** ITAA 1997, s 8-1

A loss or outgoing is deductible if it is incurred in gaining or producing assessable income, or necessarily incurred in carrying on a business for the purpose of gaining or producing assessable income -- provided it is not capital, private, or domestic in nature.

### Deductible Business Expenses

| Expense | Tier | Treatment |
|---------|------|-----------|
| Office rent (dedicated business premises) | T1 | Fully deductible |
| Professional indemnity insurance | T1 | Fully deductible |
| Accounting and tax agent fees | T1 | Fully deductible |
| Legal fees (business-related) | T1 | Fully deductible |
| Office supplies and stationery | T1 | Fully deductible |
| Software subscriptions (business use) | T1 | Fully deductible |
| Marketing and advertising | T1 | Fully deductible |
| Bank fees (business account) | T1 | Fully deductible |
| Training and professional development (maintaining existing skills) | T1 | Fully deductible |
| Industry memberships and subscriptions | T1 | Fully deductible |
| Superannuation contributions (within caps) | T2 | Deductible for self-employed -- flag for reviewer to confirm cap compliance |
| Bad debts (genuinely written off, previously included in income) | T2 | Flag for reviewer -- confirm write-off criteria met |
| Telephone and internet | T2 | Business-use portion only -- client to confirm percentage |
| Travel (domestic, business purpose) | T1 | Fully deductible if wholly for business |
| Meals while travelling overnight for business | T1 | Reasonable amount deductible |
| Contractor payments | T1 | Fully deductible -- check TPAR reporting obligations |

### NOT Deductible [T1]

| Expense | Reason |
|---------|--------|
| Entertainment (client meals not while travelling, social events) | Blocked under Div 32 ITAA 1997 |
| Private or domestic expenses | Not incurred in producing assessable income |
| Fines and penalties | Public policy -- s 26-5 ITAA 1997 |
| Income tax itself | Cannot deduct tax on income |
| Capital expenditure (unless eligible for instant write-off or depreciation) | Capital in nature -- goes through Div 40 |
| Drawings / personal withdrawals | Not an expense |
| Initial cost of obtaining a licence to operate (capital) | Capital in nature |
| Clothing (conventional) | Private -- only occupation-specific or protective clothing qualifies |

---

## Step 6: Home Office Deductions [T1/T2]

**Legislation:** ITAA 1997, s 8-1; ATO Practical Compliance Guideline PCG 2023/1

### Fixed Rate Method [T1]

From 1 July 2024, the fixed rate is **$0.70 per hour** worked from home.

**What the fixed rate covers:**
- Energy expenses (electricity and gas for heating, cooling, lighting)
- Internet and phone expenses (home internet, mobile data, mobile phone, home phone)
- Stationery and computer consumables (printer ink, paper)

**What you can claim separately (on top of the fixed rate):**
- Decline in value (depreciation) of home office equipment (desk, chair, computer, monitor)
- Repairs and maintenance of home office equipment
- Cleaning of a dedicated home office

**Record-keeping requirement:** You must keep a record of the total number of hours worked from home during the year. A timesheet, roster, diary, or similar document is acceptable. You no longer need to keep a log for a representative 4-week period -- you need the actual hours for the full year.

### Actual Cost Method [T2]

Calculate the actual costs incurred for each running expense. Apportion between business and private use. [T2] Flag for reviewer: requires detailed records and reasonable apportionment basis. More complex but may yield a higher deduction.

**A dedicated home office is NOT required for either method.** You can claim under the fixed rate method even if you work from a shared or multi-use space (e.g., kitchen table). This differs from some other jurisdictions.

---

## Step 7: Motor Vehicle Deductions [T1/T2]

**Legislation:** ITAA 1997, Div 28 and Div 40; ATO Determination TD 2024/3

### Cents Per Kilometre Method [T1]

- Rate for 2024-25: **$0.88 per kilometre** (increased from $0.85 in 2023-24)
- Maximum claimable: **5,000 business kilometres per year** (cap = $4,400)
- No written evidence of kilometres required, but must be able to demonstrate how the estimate was reasonable
- Covers ALL car expenses (fuel, insurance, registration, depreciation, maintenance) -- cannot claim separately

### Logbook Method [T2]

- Must maintain a logbook for a continuous 12-week period (valid for 5 years if circumstances unchanged)
- Business-use percentage from logbook applied to actual running costs
- No kilometre cap
- [T2] Flag for reviewer: confirm logbook is valid and business percentage is reasonable

**The two methods are mutually exclusive for the same vehicle in the same year.**

---

## Step 8: Depreciation and Instant Asset Write-Off [T1]

**Legislation:** ITAA 1997, Div 40 (capital allowances); Subdiv 328-D (simplified depreciation for SBE)

### 8A: Instant Asset Write-Off -- Small Business Entities [T1]

| Period | Threshold (per asset, exclusive of GST if registered) | Eligibility |
|--------|-------------------------------------------------------|-------------|
| 1 July 2024 -- 30 June 2025 | **$20,000** | Small business entity with aggregated turnover < $10 million |
| 1 July 2025 -- 30 June 2026 | **$20,000** (extended) | Same |
| From 1 July 2026 | Reverts to $1,000 (unless further extended) | Same |

- The $20,000 threshold applies **per asset**, so multiple assets can each be written off immediately
- Asset must be **first used or installed ready for use** during the income year
- If the asset costs $20,000 or more, it goes into the small business pool (see below)

### 8B: Small Business Simplified Depreciation Pool [T1]

| Pool | Rate |
|------|------|
| General small business pool | 15% in first year, 30% in subsequent years (diminishing value) |
| Assets $20,000+ | Added to the general pool |

### 8C: Standard Depreciation (Non-SBE or Election Not to Use Simplified) [T1]

| Method | Formula |
|--------|---------|
| Diminishing value | Base value x (days held / 365) x (200% / effective life in years) |
| Prime cost (straight-line) | Cost x (days held / 365) x (100% / effective life in years) |

Effective life is determined by the ATO's Table of Effective Life (TR 2024/3) or the taxpayer's own reasonable estimate.

### Common Effective Lives [T1]

| Asset | ATO Effective Life | Prime Cost Rate |
|-------|-------------------|-----------------|
| Laptop / desktop computer | 4 years | 25% |
| Computer software (in-house) | 4 years | 25% |
| Mobile phone | 3 years | 33.3% |
| Office furniture (desk, chair) | 10 years | 10% |
| Motor vehicle | 8 years | 12.5% |
| Printer / scanner | 5 years | 20% |

---

## Step 9: HELP / HECS-HELP Repayment [T1]

**Legislation:** Higher Education Support Act 2003; ATO repayment thresholds

### 2024-25 Compulsory Repayment Thresholds and Rates [T1]

| Repayment Income (AUD) | Repayment Rate |
|------------------------|----------------|
| Below $54,435 | 0% |
| $54,435 -- $59,518 | 1.0% |
| $59,519 -- $63,089 | 2.0% |
| $63,090 -- $66,875 | 2.5% |
| $66,876 -- $70,888 | 3.0% |
| $70,889 -- $75,144 | 3.5% |
| $75,145 -- $79,659 | 4.0% |
| $79,660 -- $84,432 | 4.5% |
| $84,433 -- $89,494 | 5.0% |
| $89,495 -- $94,865 | 5.5% |
| $94,866 -- $100,557 | 6.0% |
| $100,558 -- $106,590 | 6.5% |
| $106,591 -- $112,985 | 7.0% |
| $112,986 -- $119,764 | 7.5% |
| $119,765 -- $126,950 | 8.0% |
| $126,951 -- $134,568 | 8.5% |
| $134,569 -- $142,642 | 9.0% |
| $142,643 -- $151,200 | 9.5% |
| $151,201+ | 10.0% |

**Repayment income** = taxable income + net investment losses + reportable fringe benefits + reportable super contributions.

**Note:** The repayment rate applies to the **entire** repayment income for 2024-25 (not marginal). This changes to a marginal system from 2025-26.

**Note:** HELP repayment is NOT a tax -- it is a compulsory loan repayment collected through the tax system. It does not reduce taxable income.

---

## Step 10: Private Health Insurance Rebate [T2]

**Legislation:** Private Health Insurance Act 2007, Part 6-2; ITAA 1997, Div 61

### Income Thresholds -- 2024-25 [T1]

| Tier | Single | Family | Rebate (Under 65) | Rebate (65-69) | Rebate (70+) |
|------|--------|--------|-------------------|----------------|--------------|
| Base | $0 -- $93,000 | $0 -- $186,000 | 24.608% | 28.710% | 32.812% |
| Tier 1 | $93,001 -- $108,000 | $186,001 -- $216,000 | 16.405% | 20.507% | 24.608% |
| Tier 2 | $108,001 -- $144,000 | $216,001 -- $288,000 | 8.202% | 12.303% | 16.405% |
| Tier 3 | $144,001+ | $288,001+ | 0% | 0% | 0% |

Family thresholds increase by $1,500 for each dependent child after the first.

The rebate can be received as a premium reduction (through the insurer) or claimed as a tax offset at lodgment.

**[T2] Flag:** Confirm income tier, age bracket, and whether rebate was already received as a premium reduction. If received as a reduction, the tax offset claim must be adjusted to avoid double-counting.

---

## Step 11: Tax File Number (TFN) Declaration [T1]

**Legislation:** Tax Administration Act 1953, s 202A

- Every individual must have a TFN to lodge a return
- Sole traders must quote their individual TFN (not a separate business TFN)
- Failure to quote TFN on investment income (e.g., bank interest) results in withholding at the top marginal rate (45% + 2% Medicare = 47%)
- ABN is separate from TFN and required for carrying on a business

---

## Step 12: Filing Deadlines and PAYG [T1]

**Legislation:** Tax Administration Act 1953

### Key Deadlines -- 2024-25 Income Year [T1]

| Filing / Payment | Deadline |
|-----------------|----------|
| Individual return (self-lodging) | 31 October 2025 |
| Individual return (via registered tax agent, if prior years up to date) | Up to 15 May 2026 |
| PAYG instalment -- Quarter 1 (Jul-Sep) | 28 October 2024 |
| PAYG instalment -- Quarter 2 (Oct-Dec) | 28 February 2025 |
| PAYG instalment -- Quarter 3 (Jan-Mar) | 28 April 2025 |
| PAYG instalment -- Quarter 4 (Apr-Jun) | 28 July 2025 |

### PAYG Instalment System [T1]

Sole traders who had a tax liability in the prior year may enter the PAYG instalment system. The ATO issues an instalment rate or amount. PAYG instalments paid during the year are credited against the final tax liability.

---

## Step 13: Penalties [T1]

**Legislation:** Tax Administration Act 1953, Div 284, Div 286, Sch 1

| Offence | Penalty |
|---------|---------|
| Failure to lodge on time (FTL) | 1 penalty unit ($330 for 2024-25) per 28-day period, up to 5 penalty units ($1,650 maximum) |
| Shortfall -- lack of reasonable care | 25% of the shortfall amount |
| Shortfall -- recklessness | 50% of the shortfall amount |
| Shortfall -- intentional disregard | 75% of the shortfall amount |
| General interest charge (GIC) on unpaid tax | Updated quarterly by ATO -- approximately 11-12% p.a. (2024-25) |
| Failure to keep records | Up to $1,100 per offence |

**Note:** The ATO generally does not apply FTL penalties for a first isolated late lodgment. Penalties may be remitted on application.

---

## Step 14: Record Keeping [T1]

**Legislation:** ITAA 1997, Div 900; Tax Administration Act 1953

| Requirement | Detail |
|-------------|--------|
| Minimum retention period | 5 years from the date of lodgment (or the due date, whichever is later) |
| What to keep | All invoices, receipts, bank statements, contracts, asset purchase records, motor vehicle logbook (if applicable), home office hours log |
| Format | Paper or digital (ATO accepts digital records including photos of receipts) |
| BAS records | All GST transaction records, BAS lodgments, and supporting documents |

---

## Step 15: Final Tax Computation -- Step-by-Step [T1]

**This is the mechanical computation sequence. All intermediate results should appear in working papers.**

```
1.  Gross business income (assessable income from sole trader activity)
2.  Less: Allowable deductions (including home office, motor vehicle, depreciation / instant asset write-off)
3.  = Net business income (or loss)
4.  Add: Other assessable income (employment, interest, dividends, rent, capital gains)
5.  Less: Prior year tax losses (if any)
6.  = TOTAL TAXABLE INCOME

7.  Apply tax rates from Step 1 to taxable income
8.  = BASIC INCOME TAX LIABILITY (gross tax)

9.  Less: LITO (Step 4A)
10. Less: SBITO (Step 4C -- up to $1,000)
11. Less: Private health insurance rebate offset (Step 10, if claiming as offset)
12. Less: Other non-refundable offsets
13. = NET TAX PAYABLE (cannot be less than zero after non-refundable offsets)

14. Add: Medicare levy (Step 2 -- 2% of taxable income, subject to low-income reduction)
15. Add: Medicare levy surcharge (Step 3 -- if applicable)
16. Add: HELP / HECS compulsory repayment (Step 9 -- if applicable)
17. = TOTAL TAX AND CHARGES

18. Less: PAYG instalments paid during the year
19. Less: Tax withheld (from employment income statements, interest, dividends)
20. Less: Refundable tax offsets (if any)
21. = TAX PAYABLE / REFUND
```

**NEVER compute Step 7 (tax from rate table) using Claude directly in a live return -- pass taxable income to the deterministic engine to apply the rate table.**

---

## Step 16: Edge Case Registry

### EC1 -- GST registered sole trader income [T1]
**Situation:** GST-registered sole trader reports $110,000 gross receipts (including 10% GST).
**Resolution:** Assessable income = $100,000. The $10,000 GST collected is a liability to the ATO, not income. Always report income exclusive of GST if registered for GST.

### EC2 -- Non-GST-registered sole trader [T1]
**Situation:** Sole trader with turnover under $75,000 is not registered for GST. Charges $50,000 to clients.
**Resolution:** Assessable income = $50,000 (full amount charged). No GST component to exclude. Input credits on purchases cannot be claimed either.

### EC3 -- Instant asset write-off, asset costs exactly $20,000 [T1]
**Situation:** Sole trader buys equipment for exactly $20,000 (excl. GST).
**Resolution:** NOT eligible for instant write-off. The threshold is **less than** $20,000. Asset costing exactly $20,000 must be added to the small business depreciation pool.

### EC4 -- Motor vehicle, both methods claimed [T1]
**Situation:** Client claims cents-per-km for one car and also claims fuel receipts for the same car.
**Resolution:** INCORRECT. The cents-per-km rate covers ALL car running costs. Cannot claim any car expenses separately when using this method. Choose one method per vehicle.

### EC5 -- Home office, no records of hours [T2]
**Situation:** Client worked from home but kept no record of hours worked.
**Resolution:** Cannot use the fixed rate method without records of actual hours. [T2] Flag for reviewer: explore whether the actual cost method could apply with available records, or whether a reasonable estimate can be reconstructed from other evidence (e.g., calendar entries, timesheets). Conservative approach: no claim.

### EC6 -- HELP repayment calculated on total income [T1]
**Situation:** Client earns $80,000 taxable income plus $5,000 net investment loss. Repayment income = $85,000?
**Resolution:** Repayment income = taxable income + net investment losses (added back) + reportable fringe benefits + reportable super contributions. Net investment loss of $5,000 is ADDED to taxable income: repayment income = $80,000 + $5,000 = $85,000. Apply 4.5% rate: repayment = $3,825.

### EC7 -- Medicare levy surcharge, partial year cover [T2]
**Situation:** Client earned $100,000 and held private hospital cover for only 8 months.
**Resolution:** MLS applies for the 4 months without cover. Pro-rata: 1.0% x $100,000 x 4/12 = $333. [T2] Flag for reviewer: confirm exact dates of cover from the private health insurer statement.

### EC8 -- LITO phases out mid-bracket [T1]
**Situation:** Client has taxable income of $50,000. What is the LITO?
**Resolution:** Income is in the $45,001-$66,667 band. LITO = $325 - (1.5% x ($50,000 - $45,000)) = $325 - $75 = $250.

### EC9 -- Private use of business asset [T2]
**Situation:** Client buys a $15,000 camera. Uses it 60% for business, 40% personal.
**Resolution:** Instant asset write-off applies to the business-use portion only. Deduction = $15,000 x 60% = $9,000. Or if using the small business pool, only 60% of cost enters the pool. [T2] Flag for reviewer: confirm business-use percentage is reasonable and documented.

### EC10 -- Sole trader with PAYG employment income [T1]
**Situation:** Client is employed (PAYG withholding from employer) and also runs a sole trader business on the side.
**Resolution:** Both income streams are declared on the same individual tax return. Employment income goes to Item 1, business income to Item P (Business and professional items schedule). Tax is calculated on total taxable income. PAYG withheld from employment is credited at Step 19 of the computation. SBITO only applies to the sole trader income portion.

### EC11 -- Instant asset write-off for non-SBE [T1]
**Situation:** Sole trader has aggregated turnover of $12 million. Wants to claim instant asset write-off for a $15,000 asset.
**Resolution:** NOT eligible. The $20,000 instant asset write-off only applies to small business entities with aggregated turnover under $10 million. Must use standard depreciation under Div 40.

### EC12 -- Entertainment expense [T1]
**Situation:** Sole trader takes clients to dinner and wants to claim $2,000 as a deduction.
**Resolution:** NOT deductible. Entertainment is blocked under Div 32 ITAA 1997. Includes food, drink, and recreation provided to clients. No partial deduction. No apportionment. Full block.

---

## Step 17: Reviewer Escalation Protocol

When Claude identifies a [T2] situation:

```
REVIEWER FLAG
Tier: T2
Client: [name]
Situation: [description]
Issue: [what is ambiguous]
Options: [possible treatments]
Recommended: [most likely correct treatment and why]
Action Required: Qualified accountant (CPA/CA) must confirm before lodgment.
```

When Claude identifies a [T3] situation:

```
ESCALATION REQUIRED
Tier: T3
Client: [name]
Situation: [description]
Issue: [outside skill scope]
Action Required: Do not advise. Refer to qualified accountant. Document gap.
```

---

## Step 18: Test Suite

### Test 1 -- Standard sole trader, mid-range income
**Input:** Australian resident, sole trader, gross business income $120,000, allowable deductions $30,000, no other income, no HELP debt, no PHI, no PAYG instalments paid, aggregated turnover $120,000.
**Expected computation:**
- Taxable income = $120,000 - $30,000 = $90,000
- Tax = $4,288 + 30% x ($90,000 - $45,000) = $4,288 + $13,500 = $17,788
- LITO = $0 (income above $66,667)
- SBITO = min($1,000, 16% x $17,788 x $90,000 / $90,000) = min($1,000, $2,846) = $1,000
- Net tax = $17,788 - $1,000 = $16,788
- Medicare levy = 2% x $90,000 = $1,800
- MLS = 1.0% x $90,000 = $900 (no PHI, income $90,000 < $93,000 threshold -- actually $90,000 is below the $93,000 threshold, so MLS = $0)
- HELP = $0 (no debt)
- **Total payable = $16,788 + $1,800 = $18,588**

### Test 2 -- Low-income sole trader with LITO
**Input:** Australian resident, sole trader, gross business income $40,000, allowable deductions $5,000, no other income, no HELP, no PHI.
**Expected computation:**
- Taxable income = $35,000
- Tax = 16% x ($35,000 - $18,200) = 16% x $16,800 = $2,688
- LITO = $700 (income $35,000 < $37,500)
- SBITO = min($1,000, 16% x $2,688) = min($1,000, $430) = $430
- Net tax = $2,688 - $700 - $430 = $1,558
- Medicare levy = 2% x $35,000 = $700
- **Total payable = $1,558 + $700 = $2,258**

### Test 3 -- High-income sole trader, top bracket, with HELP
**Input:** Australian resident, sole trader, taxable income $250,000, HELP debt $30,000, no PHI, no PAYG paid.
**Expected computation:**
- Tax = $51,638 + 45% x ($250,000 - $190,000) = $51,638 + $27,000 = $78,638
- LITO = $0
- SBITO = $1,000 (cap)
- Net tax = $78,638 - $1,000 = $77,638
- Medicare levy = 2% x $250,000 = $5,000
- MLS = 1.5% x $250,000 = $3,750 (no PHI, income above $144,000)
- HELP = 10% x $250,000 = $25,000 (but capped at remaining HELP debt of $30,000, so $25,000)
- **Total payable = $77,638 + $5,000 + $3,750 + $25,000 = $111,388**

### Test 4 -- Sole trader plus employment income
**Input:** Australian resident, employment income $60,000 (PAYG withheld $12,000), sole trader net business income $25,000, no HELP, holds PHI (Base tier), aggregated turnover $50,000.
**Expected computation:**
- Taxable income = $60,000 + $25,000 = $85,000
- Tax = $4,288 + 30% x ($85,000 - $45,000) = $4,288 + $12,000 = $16,288
- LITO = $0 (income above $66,667)
- SBITO = min($1,000, 16% x $16,288 x $25,000 / $85,000) = min($1,000, $766) = $766
- Net tax = $16,288 - $766 = $15,522
- Medicare levy = 2% x $85,000 = $1,700
- MLS = $0 (holds PHI)
- Total charges = $15,522 + $1,700 = $17,222
- Less PAYG withheld = $12,000
- **Total payable = $17,222 - $12,000 = $5,222**

### Test 5 -- Instant asset write-off and home office
**Input:** Australian resident, sole trader (SBE, turnover $80,000), gross income $80,000, bought laptop $1,800 and desk $900 (both first used in year), worked from home 1,200 hours, other deductions $10,000.
**Expected computation:**
- Instant write-off: laptop $1,800 (< $20,000) + desk $900 (< $20,000) = $2,700
- Home office: 1,200 x $0.70 = $840
- Total deductions: $10,000 + $2,700 + $840 = $13,540
- Taxable income = $80,000 - $13,540 = $66,460
- Tax = $4,288 + 30% x ($66,460 - $45,000) = $4,288 + $6,438 = $10,726
- LITO = $325 - 1.5% x ($66,460 - $45,000) = $325 - $321.90 = $3.10 (rounded to $3)
- SBITO = min($1,000, 16% x $10,726) = min($1,000, $1,716) = $1,000
- Net tax = $10,726 - $3 - $1,000 = $9,723
- Medicare levy = 2% x $66,460 = $1,329
- **Total payable = $9,723 + $1,329 = $11,052**

### Test 6 -- Tax-free threshold not exceeded
**Input:** Australian resident, sole trader, gross income $20,000, deductions $5,000.
**Expected computation:**
- Taxable income = $15,000
- Tax = $0 (below $18,200 threshold)
- LITO = $700 (not needed, tax already $0)
- Medicare levy: $15,000 is below $27,222 single threshold -- levy = $0
- **Total payable = $0**

### Test 7 -- LITO phase-out in first band
**Input:** Australian resident, taxable income $42,000.
**Expected computation:**
- Tax = 16% x ($42,000 - $18,200) = $3,808
- LITO = $700 - 5% x ($42,000 - $37,500) = $700 - $225 = $475
- Net tax before SBITO = $3,808 - $475 = $3,333
- (SBITO and Medicare as applicable)

---

## PROHIBITIONS

- NEVER apply a rate table without confirming Australian residency status
- NEVER compute tax from the rate table directly in a live return -- pass taxable income to the deterministic engine
- NEVER include GST collected as assessable income for GST-registered sole traders
- NEVER allow entertainment expenses as a deduction
- NEVER allow fines, penalties, or income tax as a deduction
- NEVER apply LMITO for any year from 2022-23 onwards -- it has expired
- NEVER allow an asset costing $20,000 or more to be instantly written off (threshold is LESS THAN $20,000)
- NEVER claim both cents-per-km and actual costs for the same vehicle in the same year
- NEVER apply the instant asset write-off for entities with aggregated turnover of $10 million or more
- NEVER treat HELP/HECS repayment as a tax deduction -- it is a loan repayment
- NEVER present tax calculations as definitive -- always label as estimated and direct client to their accountant for confirmation
- NEVER allow the home office fixed rate claim without records of actual hours worked from home
- NEVER allow SBITO to exceed $1,000
- NEVER allow LITO to make tax payable negative (it is non-refundable)

---

## Contribution Notes (For Non-Australian Jurisdictions)

If adapting this skill for another country:

1. Replace ITAA 1997 references with your jurisdiction's equivalent income tax legislation.
2. Replace the rate table with your jurisdiction's equivalent bands and rates.
3. Replace the individual tax return structure with your jurisdiction's equivalent self-assessment form.
4. Replace the general deduction provision (s 8-1) with your jurisdiction's equivalent deductibility test.
5. Replace depreciation rules (Div 40) with your jurisdiction's equivalent capital allowance schedule.
6. Replace the instant asset write-off with your jurisdiction's equivalent accelerated depreciation concession.
7. Replace Medicare levy with your jurisdiction's equivalent social health insurance contribution.
8. Replace HELP/HECS with your jurisdiction's equivalent student loan repayment mechanism.
9. Replace the PAYG instalment system with your jurisdiction's equivalent provisional/estimated tax mechanism.
10. Replace filing deadlines and penalty rates with your jurisdiction's current figures.
11. Have a licensed practitioner in your jurisdiction validate every T1 rule before publishing.

**A skill may not be published without sign-off from a qualified practitioner in the relevant jurisdiction.**

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, CA, registered tax agent, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
