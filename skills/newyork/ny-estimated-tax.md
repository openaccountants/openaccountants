---
name: ny-estimated-tax
description: >
  New York State estimated tax (Form IT-2105) for self-employed individuals. Covers quarterly instalment requirements, safe harbour rules, MCTMT estimated payments, underpayment penalty computation via Form IT-2105.9, and NYC estimated tax. Primary source: NY Tax Law Section 685.
version: 1.0
jurisdiction: US-NY
tax_year: 2025
category: state
depends_on:
  - us-tax-workflow-base
validated: April 2026
---

# NY Estimated Tax (IT-2105) v1.0

## What this file is

**Obligation category:** ET (Estimated Tax)
**Functional role:** Computation
**Status:** Complete

This is a Tier 2 content skill for computing quarterly estimated New York State (and NYC) income tax payments for sole proprietors and single-member LLCs. NY estimated tax covers state tax, NYC resident tax (if applicable), Yonkers tax, and MCTMT -- all on one voucher.

---

## Section 1 -- Scope statement

**In scope:**

- Form IT-2105 (Estimated Tax Payment Voucher)
- Form IT-2105.9 (Underpayment of Estimated Tax by Individuals)
- NY state income tax estimated payments
- NYC resident income tax estimated payments
- Yonkers resident/nonresident estimated payments
- MCTMT for self-employed individuals
- Safe harbour computation (90% current / 100% or 110% prior year)
- Annualized income installment method

**Out of scope (refused):**

- Corporation estimated tax (CT-400)
- Partnership estimated tax
- Fiduciary estimated tax (IT-2106)
- PTET estimated payments
- Estimated tax for non-resident filers

---

## Section 2 -- Filing requirements

### Who must make estimated payments

You must make estimated tax payments if:

1. Your estimated NY tax (state + city + MCTMT) after withholding and credits will be $300 or more, AND
2. Your withholding and credits will be less than the required annual payment (the lesser of 90% current year or the prior-year safe harbour).

**Source:** NY Tax Law §685(c).

### Payment schedule

| Installment | Due date | Source |
|-------------|----------|--------|
| 1st | April 15, 2025 | NY Tax Law §685(c) |
| 2nd | June 15, 2025 | NY Tax Law §685(c) |
| 3rd | September 15, 2025 | NY Tax Law §685(c) |
| 4th | January 15, 2026 | NY Tax Law §685(c) |

---

## Section 3 -- Rates and thresholds

| Item | Amount | Source |
|------|--------|--------|
| Estimated tax threshold | $300 | NY Tax Law §685(c) |
| Safe harbour -- current year | 90% of current year tax | NY Tax Law §685(d) |
| Safe harbour -- prior year (NYAGI <= $150K single / $150K MFJ) | 100% of prior year tax | NY Tax Law §685(d) |
| Safe harbour -- prior year (NYAGI > $150K single / $150K MFJ) | 110% of prior year tax | NY Tax Law §685(d)(2) |
| MCTMT Zone 1 rate (self-employed) | 0.60% of NESE > $50,000 | NY Tax Law §801(a) |
| MCTMT Zone 2 rate (self-employed) | 0.34% of NESE > $50,000 | NY Tax Law §801(a) |
| NYC top resident rate | 3.876% | NYC Admin Code §11-1701 |
| Yonkers resident surcharge | 16.75% of NY state tax | NY Tax Law Art. 30-A |
| Underpayment penalty rate | Varies quarterly (set by NYSDTF) | NY Tax Law §685(a) |

**Important:** NY has a 110% prior-year safe harbour for high-income taxpayers (NYAGI > $150,000), unlike Illinois which uses 100% for all. This mirrors the federal rule.

---

## Section 4 -- Computation rules (Step format)

### Step 1: Estimate current year NY state tax

Use the NY IT-201 computation:
1. Federal AGI + NY additions - NY subtractions = NYAGI.
2. NYAGI - standard deduction or itemized = NY taxable income.
3. Apply NY tax rate schedule (progressive 4% to 10.9%).
4. Subtract NY credits (household credit, EIC, etc.).
5. Result = estimated NY state tax.

### Step 2: Estimate NYC resident tax (if applicable)

If the taxpayer lives in the five NYC boroughs:
1. NYC taxable income (generally equals NY taxable income).
2. Apply NYC rate schedule (3.078% to 3.876%).
3. Subtract NYC household credit and NYC UBT credit (if applicable).
4. Result = estimated NYC tax.

### Step 3: Estimate Yonkers tax (if applicable)

- Yonkers resident: 16.75% of NY state tax.
- Yonkers nonresident working in Yonkers: 0.5% of Yonkers-source earnings.

### Step 4: Estimate MCTMT (if applicable)

If the taxpayer is self-employed in the MCTD (12 counties):
- Net self-employment earnings (NESE) in Zone 1 counties above $50,000 x 0.60%.
- NESE in Zone 2 counties above $50,000 x 0.34%.

### Step 5: Compute total estimated tax

NY state tax + NYC tax + Yonkers tax + MCTMT = total estimated tax.

### Step 6: Subtract expected withholding and credits

Total estimated tax - W-2 withholding - other credits = net estimated tax to be paid via vouchers.

### Step 7: Determine required annual payment

Required annual payment = lesser of:
- 90% of current year estimated tax, OR
- 100% of prior year tax (or 110% if prior year NYAGI > $150,000).

### Step 8: Compute quarterly installments

Divide required annual payment by 4. Each installment = 25%.

### Step 9: File vouchers or pay electronically

Pay via:
- Paper vouchers (Form IT-2105) mailed to NYSDTF
- Online at www.tax.ny.gov (no voucher needed)

---

## Section 5 -- Edge cases and special rules

### E-1: The 110% prior-year rule

Unlike Illinois, New York requires 110% of prior year tax for high-income taxpayers (NYAGI > $150,000). This matches the federal 110% rule. **Source:** NY Tax Law §685(d)(2).

### E-2: MCTMT is included in estimated tax

MCTMT for self-employed individuals is reported on Form IT-201 (Lines 54a/54b) and must be included in estimated tax calculations. It is NOT a separate filing.

### E-3: NYC UBT credit reduces estimated tax

If the taxpayer expects to pay NYC Unincorporated Business Tax, the IT-219 credit reduces NYC resident tax. Include this reduction when estimating NYC tax.

### E-4: First year of self-employment

If the taxpayer had no NY tax liability in the prior year, the prior-year safe harbour is $0. The 90% current-year method must be used.

### E-5: Annualized income installment method

If income is not earned evenly (e.g., seasonal freelancer), Form IT-2105.9 allows the annualized income installment method to reduce early-quarter payments. This requires computing income actually earned through each quarter-end date.

### E-6: Overpayment applied from prior year

Prior-year overpayment applied to estimated tax reduces the first quarter payment. Document the amount on the voucher.

---

## Section 6 -- Test suite

### Test 1: Standard NYC freelancer

- **Input:** Single NYC resident. NYAGI: $120,000. NY tax: $6,500. NYC tax: $3,800. MCTMT: ($120,000 - $50,000) x 0.60% = $420. No withholding.
- **Expected:** Total: $10,720. Required: $10,720 x 90% = $9,648 (or 100% prior if lower). Quarterly: $2,412.

### Test 2: High-income, 110% prior year

- **Input:** Single, NYAGI $200,000. Current year total tax: $18,000. Prior year tax: $14,000.
- **Expected:** 90% current = $16,200. 110% prior = $15,400. Required = $15,400 (lesser). Quarterly: $3,850.

### Test 3: Below threshold

- **Input:** NYC resident, estimated total tax: $250 after withholding.
- **Expected:** $250 < $300 threshold. No estimated payments required.

### Test 4: Yonkers resident

- **Input:** Yonkers resident. NY state tax: $5,000. Yonkers surcharge: $5,000 x 16.75% = $837.50.
- **Expected:** Include $837.50 in estimated tax total.

### Test 5: MCTMT Zone 2 only

- **Input:** Westchester resident (Zone 2). NESE: $80,000.
- **Expected:** MCTMT: ($80,000 - $50,000) x 0.34% = $102.

---

## Section 7 -- Prohibitions

- **P-1:** Do NOT omit MCTMT from estimated tax calculations. It is part of the IT-201, not a separate return.
- **P-2:** Do NOT use 100% prior-year safe harbour for taxpayers with NYAGI > $150,000. Use 110%.
- **P-3:** Do NOT estimate NYC tax for taxpayers who are not NYC residents.
- **P-4:** Do NOT ignore the NYC UBT credit when estimating NYC tax.
- **P-5:** Do NOT advise on penalty waiver requests. That is a procedural matter.

---

## Section 8 -- Self-checks

Before delivering output, verify:

- [ ] $300 threshold applied correctly
- [ ] All tax layers included (state + city + Yonkers + MCTMT as applicable)
- [ ] 110% prior-year rule applied for NYAGI > $150,000
- [ ] MCTMT computed with correct zone rate and $50,000 threshold
- [ ] NYC UBT credit offset included in NYC tax estimate (if applicable)
- [ ] Quarterly payments divided evenly (25% each)
- [ ] Withholding and prior-year overpayment credits subtracted before determining installments
- [ ] Reviewer brief notes which safe harbour method was used

---

## Section 9 -- Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
