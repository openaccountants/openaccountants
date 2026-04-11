---
name: tx-franchise-tax
description: >
  Texas Franchise Tax for single-member LLCs and other taxable entities. Covers the no-tax-due threshold ($2,470,000 for 2025), EZ computation rate (0.331%), standard computation, Public Information Report (Form 05-102), and annual filing requirements. Primary source: Texas Tax Code Chapter 171.
version: 1.0
jurisdiction: US-TX
tax_year: 2025
category: state
depends_on:
  - us-tax-workflow-base
validated: April 2026
---

# Texas Franchise Tax v1.0

## What this file is

**Obligation category:** EF (Entity Fees) / IT (margin tax)
**Functional role:** Entity filing + Computation
**Status:** Complete

This is a Tier 2 content skill for computing and filing the Texas franchise tax for single-member LLCs. Texas has no personal income tax, but the franchise tax (also called the "margin tax") applies to most legal entities doing business in Texas, including SMLLCs. Sole proprietors without an LLC are NOT subject to franchise tax.

---

## Section 1 -- Scope statement

**In scope:**

- Form 05-102 (Public Information Report -- mandatory annual filing)
- Form 05-163 (No Tax Due Information Report)
- Form 05-158-A (Franchise Tax Report -- Long Form)
- Form 05-169 (EZ Computation Report)
- Single-member LLCs (disregarded for federal tax but taxable for TX franchise tax)
- No-tax-due threshold determination
- EZ computation method
- Cost of goods sold (COGS) method
- Compensation method

**Out of scope (refused):**

- Sole proprietors without an LLC (exempt from franchise tax)
- General partnerships directly owned by natural persons (exempt)
- Passive entities (as defined by Tax Code §171.0003)
- Combined group reporting (Tax Code §171.1014)
- Franchise tax credits (research, clean energy, etc.)
- Extensions beyond the automatic extension
- Franchise tax refund claims

---

## Section 2 -- Filing requirements

### Who must file

Every taxable entity formed in Texas or doing business in Texas must file a franchise tax report annually. This includes LLCs, corporations, limited partnerships, and professional associations. **Source:** Texas Tax Code §171.001.

**Key exemption:** Sole proprietors (natural persons operating without an entity) and general partnerships directly owned entirely by natural persons are exempt. **Source:** Texas Tax Code §171.001(a).

### Due dates

| Item | Date | Source |
|------|------|--------|
| Annual report due date | May 15, 2025 (for accounting year ending in 2024) | Texas Tax Code §171.202 |
| Automatic extension | November 15, 2025 (with 90% of tax paid by May 15) | Texas Comptroller Rule 3.584 |
| Public Information Report (05-102) | Due with the franchise tax report | Texas Tax Code §171.203 |

### Initial filing

A newly formed entity must file its first franchise tax report by May 15 of the year after its formation. The report covers the period from formation through December 31 of that year (or the entity's fiscal year end).

---

## Section 3 -- Rates and thresholds

| Item | Amount | Source |
|------|--------|--------|
| No-tax-due threshold (2025 report) | $2,470,000 total revenue | Texas Tax Code §171.002(d)(2) |
| EZ computation rate | 0.331% of total revenue (apportioned) | Texas Tax Code §171.1016 |
| EZ computation revenue limit | $20,000,000 | Texas Tax Code §171.1016 |
| Standard rate -- retail/wholesale | 0.375% of taxable margin | Texas Tax Code §171.002(b) |
| Standard rate -- other entities | 0.75% of taxable margin | Texas Tax Code §171.002(a) |
| Minimum tax | $0 (no minimum) | Texas Tax Code §171.002 |
| Cost of goods sold alternative | Available per Tax Code §171.1012 | Texas Tax Code §171.1012 |
| Compensation deduction alternative | Available per Tax Code §171.1013 | Texas Tax Code §171.1013 |

### No-tax-due threshold

If total revenue is $2,470,000 or less, the entity owes no franchise tax but MUST still file:
- Form 05-102 (Public Information Report), AND
- Form 05-163 (No Tax Due Information Report).

---

## Section 4 -- Computation rules (Step format)

### Step 1: Determine if the entity is subject to franchise tax

- Is the entity an LLC, LP, LLP, corporation, or other legal entity? --> Subject.
- Is the entity a sole proprietorship (no LLC)? --> Exempt. STOP.
- Is the entity a general partnership owned entirely by natural persons? --> Exempt. STOP.

### Step 2: Determine total revenue

Total revenue is computed from federal tax return data:
- For entities filing federal Form 1040 Schedule C (SMLLCs): total revenue = gross income from Schedule C plus all other revenue items attributable to the entity.
- Generally: total revenue = gross receipts minus returns and allowances, plus other income items per Texas Tax Code §171.1011.

### Step 3: Apply the no-tax-due threshold

If total revenue <= $2,470,000:
- File Form 05-163 (No Tax Due) and Form 05-102 (Public Information Report).
- No tax payment required.
- STOP computation here.

### Step 4: Choose computation method

If total revenue > $2,470,000, choose ONE of:

**Option A: EZ Computation (if total revenue <= $20,000,000)**
- Tax = apportioned total revenue x 0.331%
- No deductions for COGS, compensation, or margin.
- Simplest method but may result in higher tax.

**Option B: Standard computation -- COGS method**
- Taxable margin = total revenue - cost of goods sold
- Tax = taxable margin x rate (0.375% retail/wholesale or 0.75% other)

**Option C: Standard computation -- Compensation method**
- Taxable margin = total revenue - compensation
- Tax = taxable margin x rate

**Option D: 70% of total revenue**
- Taxable margin cannot exceed 70% of total revenue.
- This is an automatic cap, not an election.

### Step 5: Compute apportionment (if multi-state)

If the entity has revenue from both Texas and other states:
- Texas apportionment factor = Texas gross receipts / total gross receipts everywhere.
- Apply factor to taxable margin.

For entities operating entirely in Texas: apportionment factor = 100%.

### Step 6: Compute tax due

- EZ method: apportioned revenue x 0.331%
- Standard method: apportioned taxable margin x applicable rate (0.375% or 0.75%)

### Step 7: Compare computation methods

For standard computation, the tax is the LESSER of:
- Tax computed using COGS method
- Tax computed using compensation method
- Tax computed using 70% of total revenue method

### Step 8: File required forms

Regardless of tax due:
- File Form 05-102 (Public Information Report) with current entity information.
- File the applicable tax report (05-163, 05-169, or 05-158-A).

---

## Section 5 -- Edge cases and special rules

### E-1: SMLLC is subject even though disregarded federally

A single-member LLC that is disregarded for federal income tax purposes is treated as a separate taxable entity for Texas franchise tax purposes. The SMLLC must file its own franchise tax report using data from the owner's federal return (Schedule C). **Source:** Texas Tax Code §171.0002(a).

### E-2: Passive entities

An entity may qualify as a passive entity if 90% or more of its federal gross income consists of passive income (dividends, interest, royalties, rents, capital gains). Passive entities are exempt from franchise tax but must still file Form 05-163. **Source:** Texas Tax Code §171.0003.

### E-3: First-year reporting

A newly formed entity's first franchise tax report covers a short period (date of formation through the entity's first accounting year end). The no-tax-due threshold is NOT prorated for short periods.

### E-4: Retail vs. wholesale classification

Entities primarily engaged in retail or wholesale trade qualify for the reduced 0.375% rate. The entity must derive more than 50% of its total revenue from retail or wholesale activities. Misclassification is a common audit trigger. **Source:** Texas Tax Code §171.002(b).

### E-5: COGS for service businesses

Service businesses generally cannot use the COGS method because they do not sell tangible personal property. However, Texas has a broad COGS definition that includes some service costs. Review Texas Tax Code §171.1012 carefully. When in doubt, use the compensation method.

### E-6: No tax due but must still file

Even if the entity owes $0 in franchise tax, the filing requirement remains. Failure to file results in forfeiture of the entity's right to transact business in Texas and potential involuntary termination.

---

## Section 6 -- Test suite

### Test 1: Below no-tax-due threshold

- **Input:** SMLLC with total revenue of $180,000.
- **Expected:** Below $2,470,000 threshold. File Form 05-163 + Form 05-102. Tax: $0.

### Test 2: EZ computation

- **Input:** SMLLC with total revenue of $3,000,000, 100% Texas.
- **Expected:** EZ tax: $3,000,000 x 0.331% = $9,930. Compare with standard methods to choose optimal.

### Test 3: Standard computation -- compensation method

- **Input:** Service SMLLC. Total revenue: $5,000,000. Compensation paid: $2,000,000. 100% Texas.
- **Expected:** Margin: $5,000,000 - $2,000,000 = $3,000,000. Cap: 70% x $5,000,000 = $3,500,000. Use $3,000,000. Tax: $3,000,000 x 0.75% = $22,500.

### Test 4: Retail entity at reduced rate

- **Input:** Retail SMLLC. Total revenue: $4,000,000. COGS: $2,500,000.
- **Expected:** Margin: $1,500,000. Cap: $2,800,000. Use $1,500,000. Tax: $1,500,000 x 0.375% = $5,625.

### Test 5: Sole proprietor (no entity)

- **Input:** Individual freelancer with no LLC.
- **Expected:** NOT subject to TX franchise tax. No filing required.

---

## Section 7 -- Prohibitions

- **P-1:** Do NOT tell a sole proprietor (without an LLC) that they must file franchise tax. They are exempt.
- **P-2:** Do NOT prorate the no-tax-due threshold for short-period returns.
- **P-3:** Do NOT use the COGS method for a service business without verifying that the costs qualify under §171.1012.
- **P-4:** Do NOT skip the Public Information Report (05-102). It is always required.
- **P-5:** Do NOT classify an entity as retail/wholesale for the reduced rate unless >50% of revenue is from retail/wholesale activities.
- **P-6:** Do NOT advise on whether to form or dissolve an LLC based on franchise tax implications. That is legal advice.

---

## Section 8 -- Self-checks

Before delivering output, verify:

- [ ] Entity type correctly identified (SMLLC vs. sole proprietor)
- [ ] Total revenue computed from correct federal return data
- [ ] No-tax-due threshold of $2,470,000 applied
- [ ] Form 05-102 (Public Information Report) included in every filing
- [ ] EZ computation only used if revenue <= $20,000,000
- [ ] Correct rate applied (0.75% other vs. 0.375% retail/wholesale)
- [ ] 70% of total revenue cap applied as automatic limit
- [ ] All computation methods compared to select the lowest tax
- [ ] Short-period threshold NOT prorated

---

## Section 9 -- Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
