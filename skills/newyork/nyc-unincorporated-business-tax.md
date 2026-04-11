---
name: nyc-unincorporated-business-tax
description: >
  NYC Unincorporated Business Tax (UBT) for sole proprietors and SMLLCs operating in the five boroughs. Covers the 4% tax rate, $95,000 exemption with phase-out, Form NYC-202, Form NYC-202S (simplified), the IT-219 credit against NYC resident income tax, and estimated UBT payments. Primary source: NYC Admin Code Title 11, Chapter 5.
version: 1.0
jurisdiction: US-NY-NYC
tax_year: 2025
category: state
depends_on:
  - us-tax-workflow-base
validated: April 2026
---

# NYC Unincorporated Business Tax (UBT) v1.0

## What this file is

**Obligation category:** IT (Income Tax)
**Functional role:** Computation + Return
**Status:** Complete

This is a Tier 2 content skill for computing and preparing the NYC Unincorporated Business Tax return for sole proprietors and single-member LLCs doing business in New York City. The UBT is a city-level tax imposed on net income from unincorporated businesses operating in the five boroughs.

---

## Section 1 -- Scope statement

**In scope:**

- Form NYC-202 (Unincorporated Business Tax Return)
- Form NYC-202S (Simplified Unincorporated Business Tax Return for filers with gross income of $250,000 or less)
- Form NYC-202EIN (UBT estimated tax payments)
- Form IT-219 (Credit for NYC UBT against NYC resident income tax on Form IT-201)
- Sole proprietors operating in NYC
- Single-member LLCs operating in NYC
- The $95,000 exemption and its phase-out
- UBT estimated tax payments

**Out of scope (refused):**

- Partnerships (Form NYC-204)
- Corporations (General Corporation Tax / Business Corporation Tax)
- Employees who are NOT carrying on an unincorporated business
- Multi-jurisdictional allocation of UBT income (business allocation percentage)
- UBT credit for corporations (Form NYC-3L)
- Amended UBT returns

---

## Section 2 -- Filing requirements

### Who must file

Every individual or SMLLC carrying on or liquidating a trade, business, profession, or occupation wholly or partly in NYC must file a UBT return if gross income from the NYC business exceeds $95,000. **Source:** NYC Admin Code §11-503(a).

### Filing thresholds

| Item | Amount | Source |
|------|--------|--------|
| Filing requirement threshold | Gross income > $95,000 | NYC Admin Code §11-503(a) |
| Simplified return threshold | Gross income <= $250,000 (may use NYC-202S) | NYC-202S instructions |

### Due date

| Item | Date | Source |
|------|------|--------|
| Annual return due date | April 15, 2026 (for tax year 2025) | NYC Admin Code §11-514 |
| Extension | Automatic with federal extension (to October 15, 2026) | NYC DOF instructions |

### Estimated tax payments

Quarterly estimated payments are required if the expected UBT liability is $3,400 or more. Payment dates follow the same schedule as NY state estimated tax (April 15, June 15, September 15, January 15).

---

## Section 3 -- Rates and thresholds

| Item | Amount | Source |
|------|--------|--------|
| UBT rate | 4.0% of unincorporated business taxable income | NYC Admin Code §11-503(a) |
| Exemption | $95,000 deduction from unincorporated business taxable income | NYC Admin Code §11-510(a) |
| Exemption phase-out start | Taxable income > $95,000 | NYC Admin Code §11-510(a) |
| Exemption phase-out rate | Reduced by $1 for each $2 of income over $95,000 | NYC Admin Code §11-510(a) |
| Exemption fully phased out | Taxable income >= $190,000 | Computed: $95,000 + (2 x $95,000) |
| IT-219 credit | 100% of UBT paid, limited to NYC personal income tax liability | NY Tax Law §1310(e); Form IT-219 |
| Estimated tax threshold | $3,400 expected annual UBT liability | NYC-202EIN instructions |

### Exemption phase-out computation

The $95,000 exemption is reduced by $1 for every $2 of taxable income exceeding $95,000:

| Taxable income | Exemption | Tax |
|---------------|-----------|-----|
| $95,000 or less | $95,000 (full) | $0 |
| $120,000 | $95,000 - ($25,000 / 2) = $82,500 | ($120,000 - $82,500) x 4% = $1,500 |
| $150,000 | $95,000 - ($55,000 / 2) = $67,500 | ($150,000 - $67,500) x 4% = $3,300 |
| $190,000 or more | $0 (fully phased out) | Taxable income x 4% |

---

## Section 4 -- Computation rules (Step format)

### Step 1: Determine if UBT applies

The taxpayer must be carrying on a trade, business, profession, or occupation wholly or partly within NYC. Key tests:

1. Is there a profit motive? (Hobby income is not subject to UBT.)
2. Is the business conducted in NYC? (Physical presence, not just customers.)
3. Is the individual an employee or an independent contractor? (Employees are not subject to UBT for their employment income.)

### Step 2: Compute unincorporated business gross income (NYC-202, Line 1)

Start with gross income from the business:
- Schedule C gross income (for sole proprietors)
- Include all business income attributable to NYC operations
- Include gains from business property

### Step 3: Compute unincorporated business deductions (NYC-202, Lines 2-13)

Allowable deductions mirror federal Schedule C deductions with these exceptions:
- **No deduction for:** salaries paid to the owner, distributions to owner, federal/state/local income taxes (including UBT itself).
- **Add back:** owner's health insurance deduction, retirement plan contributions for the owner (these are personal deductions, not business deductions for UBT).

### Step 4: Compute unincorporated business taxable income (NYC-202, Line 14)

Gross income - allowable deductions = unincorporated business taxable income (before exemption).

### Step 5: Apply the $95,000 exemption (NYC-202, Line 15)

If taxable income <= $95,000: exemption = taxable income. Tax = $0.

If taxable income > $95,000:
- Excess = taxable income - $95,000
- Exemption reduction = excess / 2
- Allowable exemption = $95,000 - exemption reduction
- If allowable exemption < $0, set to $0.

### Step 6: Compute UBT (NYC-202, Line 16)

(Taxable income - allowable exemption) x 4% = UBT before credits.

### Step 7: Apply UBT credits (NYC-202, Lines 17-21)

- Credit for UBT paid to other jurisdictions (limited situations)
- Lower Manhattan relocation employment assistance program (LMREAP) credit
- Other business credits

### Step 8: Compute net UBT due (NYC-202, Line 22)

UBT before credits - credits = net UBT due.

### Step 9: Compute IT-219 credit (for NYC residents)

The full amount of UBT paid is available as a credit against NYC personal income tax via Form IT-219. This credit:
- Is limited to the NYC personal income tax liability (cannot create a refund)
- Flows to Form IT-201-ATT, Line 53 (NYC resident tax credit)
- Effectively prevents double taxation of NYC business income at both the UBT and personal income tax levels

### Step 10: File and pay

- File NYC-202 (or NYC-202S) with NYC Department of Finance.
- Pay any balance due.
- Retain confirmation for reviewer brief.

---

## Section 5 -- Edge cases and special rules

### E-1: Freelancers and independent contractors

A freelancer who provides services in NYC is subject to UBT if their NYC business gross income exceeds $95,000. Simply having clients in NYC may be sufficient nexus if the work is performed in NYC.

### E-2: Work-from-home in NYC

If a freelancer works from home in NYC, the home office IS in NYC, and all income earned from that home office is NYC-source business income for UBT purposes.

### E-3: Mixed NYC/non-NYC income

If the business operates both inside and outside NYC, the taxpayer must allocate income using the business allocation percentage. This is computed on Schedule C of Form NYC-202 using a formula based on property, payroll, and gross receipts in NYC vs. everywhere. **This skill handles only 100% NYC businesses; allocation is out of scope.**

### E-4: The IT-219 credit is critical

NYC residents who pay UBT and also owe NYC personal income tax receive a full credit for UBT paid via Form IT-219. This means the economic burden of UBT for NYC residents is reduced (often to zero additional tax) because the credit offsets NYC personal income tax. However, the credit cannot exceed the NYC personal income tax, so if UBT exceeds NYC personal income tax, the excess UBT is a net cost.

### E-5: Hobby vs. business

Activities not engaged in for profit (hobbies) are not subject to UBT. The IRS presumption (profit in 3 of 5 years) is a useful guideline but is not the UBT standard. NYC follows federal characterization of the activity.

### E-6: Multiple businesses

If a taxpayer operates multiple unincorporated businesses in NYC, all businesses are combined on a single NYC-202 return. Separate NYC-202 forms are not filed for each business.

### E-7: Simplified return (NYC-202S)

If gross income from the business is $250,000 or less AND the taxpayer has no employees, no motor vehicle expenses, and no depreciation deductions, Form NYC-202S (simplified) may be used instead of the full NYC-202.

---

## Section 6 -- Test suite

### Test 1: Income below exemption

- **Input:** Freelancer with $80,000 NYC business gross income.
- **Expected:** Below $95,000 threshold. No UBT due. No filing required (gross income <= $95,000).

### Test 2: Income in phase-out range

- **Input:** Freelancer with $130,000 taxable business income, all NYC.
- **Expected:** Excess: $130,000 - $95,000 = $35,000. Exemption reduction: $35,000 / 2 = $17,500. Allowable exemption: $95,000 - $17,500 = $77,500. Taxable after exemption: $130,000 - $77,500 = $52,500. UBT: $52,500 x 4% = $2,100.

### Test 3: Income above phase-out

- **Input:** Freelancer with $200,000 taxable business income, all NYC.
- **Expected:** Exemption fully phased out ($0). UBT: $200,000 x 4% = $8,000.

### Test 4: IT-219 credit

- **Input:** Same as Test 3. NYC personal income tax: $6,500. UBT paid: $8,000.
- **Expected:** IT-219 credit: limited to $6,500 (cannot exceed NYC personal income tax). Net UBT cost: $8,000 - $6,500 = $1,500.

### Test 5: Simplified return eligibility

- **Input:** Freelancer with $100,000 gross income. No employees, no vehicle, no depreciation.
- **Expected:** Eligible for NYC-202S. Must still compute exemption phase-out.

---

## Section 7 -- Prohibitions

- **P-1:** Do NOT deduct the owner's salary, draws, or distributions when computing UBT taxable income.
- **P-2:** Do NOT deduct federal, state, or local income taxes (including UBT itself) from UBT income.
- **P-3:** Do NOT claim the IT-219 credit in excess of the NYC personal income tax liability.
- **P-4:** Do NOT apply the UBT to employment income. Employees are not subject to UBT.
- **P-5:** Do NOT file separate NYC-202 returns for multiple businesses. Combine all businesses.
- **P-6:** Do NOT allocate income between NYC and non-NYC without using the business allocation percentage schedule. This skill covers only 100% NYC businesses.

---

## Section 8 -- Self-checks

Before delivering output, verify:

- [ ] Business activity is in NYC (not just clients in NYC)
- [ ] Gross income exceeds $95,000 filing threshold
- [ ] Exemption phase-out computed correctly using $1-for-$2 formula
- [ ] Owner's salary/draws NOT deducted from UBT income
- [ ] Income taxes NOT deducted from UBT income
- [ ] IT-219 credit correctly limited to NYC personal income tax liability
- [ ] Estimated tax required if UBT liability >= $3,400
- [ ] NYC-202S eligibility checked (gross income <= $250K, no employees, no vehicles, no depreciation)
- [ ] Reviewer brief notes the IT-219 credit flow to IT-201

---

## Section 9 -- Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
