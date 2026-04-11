---
name: il-estimated-tax
description: >
  Illinois Estimated Income Tax (Form IL-1040-ES) for self-employed individuals. Covers quarterly payment requirements, 4.95% flat rate computation, safe harbour rules, underpayment penalty calculation, and payment schedule. Primary source: 35 ILCS 5/803; 86 Ill. Admin. Code 100.8010.
version: 1.0
jurisdiction: US-IL
tax_year: 2025
category: state
depends_on:
  - us-tax-workflow-base
validated: April 2026
---

# Illinois Estimated Tax (IL-1040-ES) v1.0

## What this file is

**Obligation category:** ET (Estimated Tax)
**Functional role:** Computation
**Status:** Complete

This is a Tier 2 content skill for computing quarterly estimated Illinois income tax payments for sole proprietors and single-member LLCs. Illinois imposes a flat 4.95% income tax rate with no brackets, which simplifies the estimated tax computation relative to graduated-rate states.

---

## Section 1 -- Scope statement

**In scope:**

- Form IL-1040-ES quarterly estimated tax payments
- Sole proprietors and single-member LLCs (disregarded entities)
- Safe harbour rules to avoid underpayment penalty
- Underpayment penalty computation (Form IL-2210)
- Interaction with federal estimated tax payments

**Out of scope (refused):**

- Partnerships, S-corps, C-corps
- Pass-through withholding (Form IL-1000)
- Composite returns
- Non-resident estimated tax
- Amended estimated payments after audit adjustments

---

## Section 2 -- Filing requirements

### Who must make estimated payments

An individual must make estimated payments if:

1. The taxpayer expects to owe $500 or more in Illinois income tax after subtracting Illinois withholding and credits, AND
2. The taxpayer expects Illinois withholding and credits to be less than the smaller of: (a) 90% of the current year tax liability, or (b) 100% of the prior year tax liability.

**Source:** 35 ILCS 5/803(a); 86 Ill. Admin. Code 100.8010.

### Payment schedule

| Installment | Period covered | Due date | Source |
|-------------|---------------|----------|--------|
| 1st quarter | Jan 1 -- Mar 31 | April 15, 2025 | 35 ILCS 5/803(b) |
| 2nd quarter | Apr 1 -- May 31 | June 15, 2025 | 35 ILCS 5/803(b) |
| 3rd quarter | Jun 1 -- Aug 31 | September 15, 2025 | 35 ILCS 5/803(b) |
| 4th quarter | Sep 1 -- Dec 31 | January 15, 2026 | 35 ILCS 5/803(b) |

Illinois follows the same quarterly schedule as the IRS.

---

## Section 3 -- Rates and thresholds

| Item | Amount | Source |
|------|--------|--------|
| Illinois flat income tax rate | 4.95% | 35 ILCS 5/201(b)(5.4) |
| Estimated tax threshold | $500 | 35 ILCS 5/803(a) |
| Personal exemption | $2,625 (single); $5,250 (MFJ) | 35 ILCS 5/204 (2025) |
| Safe harbour -- current year | 90% of current year tax | 35 ILCS 5/804 |
| Safe harbour -- prior year | 100% of prior year tax | 35 ILCS 5/804 |
| Underpayment penalty rate | Varies (set by IDOR quarterly, tied to federal short-term rate + 2%) | 35 ILCS 5/804(c) |

**Note:** Illinois does NOT have a 110% prior-year safe harbour for high-income taxpayers as the IRS does. The prior-year safe harbour is always 100%.

---

## Section 4 -- Computation rules (Step format)

### Step 1: Estimate current year Illinois taxable income

1. Start with expected federal adjusted gross income (AGI).
2. Add Illinois addition modifications (Schedule M, Line 3): e.g., interest from non-Illinois state/local bonds, any bonus depreciation add-back per Illinois decoupling from IRC §168(k).
3. Subtract Illinois subtraction modifications (Schedule M, Line 16): e.g., U.S. government bond interest, Illinois income tax refunds included in federal AGI, Illinois retirement income subtraction (if applicable).
4. Result = Illinois base income.

### Step 2: Subtract personal exemption

- Single/HoH: $2,625
- MFJ: $5,250
- MFS: $2,625
- Result = Illinois net income (equivalent to Illinois taxable income for individuals).

### Step 3: Compute estimated annual tax

Illinois net income x 4.95% = estimated annual Illinois income tax.

### Step 4: Subtract credits and withholding

- Subtract expected Illinois withholding (from W-2 jobs, if any).
- Subtract the Illinois Property Tax Credit (5% of property taxes paid on principal residence).
- Subtract the Illinois Earned Income Credit (20% of federal EIC for 2025).
- Subtract any other applicable credits.
- Result = net estimated tax liability.

### Step 5: Determine if estimated payments are required

If the result from Step 4 is $500 or more, estimated payments are required.

### Step 6: Determine safe harbour amount

The required annual payment is the lesser of:
- 90% of the current year estimated tax (from Step 4), OR
- 100% of the prior year Illinois tax liability (from the prior year IL-1040).

### Step 7: Compute quarterly payment

Divide the required annual payment by 4. Each quarterly installment is 25% of the annual amount.

### Step 8: Adjust for annualized income (if applicable)

If income is not earned evenly throughout the year, the taxpayer may use the annualized income installment method (Form IL-2210, Section B) to reduce early-quarter payments. This requires demonstrating that income was concentrated in later quarters.

---

## Section 5 -- Edge cases and special rules

### E-1: Part-year residents

Part-year residents must estimate tax only on income earned during the period of Illinois residency plus Illinois-source income earned while a non-resident. Use Schedule NR to allocate.

### E-2: Bonus depreciation add-back

Illinois does not conform to federal IRC §168(k) bonus depreciation. Illinois requires an add-back of the bonus depreciation amount and allows the standard MACRS depreciation instead. This affects the estimated tax base. **Source:** 35 ILCS 5/203(a)(2)(D-25).

### E-3: No estimated payment vouchers needed for e-pay

Illinois allows estimated payments via MyTax Illinois (mytax.illinois.gov) without submitting Form IL-1040-ES vouchers. If paying electronically, retain confirmation numbers.

### E-4: Prior year had no tax liability

If the taxpayer's prior year Illinois tax liability was zero (e.g., first year of self-employment with no IL-1040 filed), the prior-year safe harbour is $0. The taxpayer must pay 90% of the current year tax to avoid penalties.

### E-5: Fiscal year taxpayers

Fiscal year taxpayers follow the same quarterly pattern but shifted to match their fiscal year. Payments are due on the 15th day of the 4th, 6th, 9th, and 1st months of the following fiscal year.

### E-6: Overpayment from prior year applied

If an overpayment from the prior year IL-1040 was applied to estimated taxes, this amount reduces the first quarter estimated payment. Document the amount applied.

---

## Section 6 -- Test suite

### Test 1: Standard freelancer

- **Input:** Single filer, IL resident all year. Expected net income from Schedule C: $100,000. No withholding. No credits other than personal exemption.
- **Expected:** IL taxable income: $100,000 - $2,625 = $97,375. Tax: $97,375 x 4.95% = $4,820.06. Quarterly payment: $4,820.06 / 4 = $1,205.02 per quarter.

### Test 2: Below threshold

- **Input:** Part-year freelancer. Expected IL taxable income: $8,000. Tax: $8,000 x 4.95% = $396. With withholding of $0.
- **Expected:** $396 < $500 threshold. No estimated payments required.

### Test 3: Safe harbour using prior year

- **Input:** Current year estimated tax: $6,000. Prior year IL tax: $4,000.
- **Expected:** Safe harbour = lesser of ($6,000 x 90% = $5,400) or ($4,000 x 100% = $4,000). Required annual payment: $4,000. Quarterly: $1,000.

### Test 4: MFJ with W-2 withholding

- **Input:** MFJ. Combined income: $150,000. W-2 withholding (spouse): $3,200. Estimated tax: ($150,000 - $5,250) x 4.95% = $7,170.23. Net after withholding: $7,170.23 - $3,200 = $3,970.23.
- **Expected:** $3,970.23 > $500. Quarterly: $3,970.23 / 4 = $992.56.

### Test 5: Property tax credit

- **Input:** Single filer, IL taxable income $80,000. Property taxes paid: $6,000.
- **Expected:** Tax: ($80,000 - $2,625) x 4.95% = $3,830.06. Property tax credit: $6,000 x 5% = $300. Net: $3,530.06. Quarterly: $882.52.

---

## Section 7 -- Prohibitions

- **P-1:** Do NOT apply the federal 110% safe harbour for high-income taxpayers. Illinois uses 100% for all taxpayers.
- **P-2:** Do NOT include bonus depreciation in the Illinois income estimate without adding it back.
- **P-3:** Do NOT skip estimated payments because the taxpayer expects a large 4th quarter adjustment. Each quarter's payment is independently required.
- **P-4:** Do NOT advise on penalty abatement requests. That is a procedural matter outside this skill's scope.

---

## Section 8 -- Self-checks

Before delivering output, verify:

- [ ] Federal AGI correctly adjusted for Illinois modifications (Schedule M)
- [ ] Flat rate of 4.95% applied (not a graduated rate)
- [ ] Personal exemption of $2,625 (single) or $5,250 (MFJ) deducted
- [ ] $500 threshold applied to determine filing requirement
- [ ] Safe harbour computed using the lesser of 90% current / 100% prior
- [ ] 100% prior year rule used (not 110%)
- [ ] Bonus depreciation add-back included if applicable
- [ ] Property tax credit at 5% included if applicable
- [ ] Quarterly payments divided evenly (25% each)

---

## Section 9 -- Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
