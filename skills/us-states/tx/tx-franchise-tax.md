---
name: tx-franchise-tax
description: "Texas Franchise Tax for single-member LLCs and other taxable entities. Covers the 2026 report no-tax-due threshold ($2,650,000), discontinued Form 05-163 for report years 2024+, required PIR/OIR filing, E-Z computation rate (0.331%), standard computation, passive-entity filing path, and annual filing requirements. Primary source: Texas Comptroller and Texas Tax Code Chapter 171."
version: 1.0
jurisdiction: US-TX
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - us-tax-workflow-base
category: state
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# TX Franchise Tax

## What this file is

**Obligation category:** EF (Entity Fees) / IT (margin tax)
**Functional role:** Entity filing + Computation
**Status:** Complete

This is a Tier 2 content skill for computing and filing the Texas franchise tax for single-member LLCs. Texas has no personal income tax, but the franchise tax (also called the "margin tax") applies to most legal entities doing business in Texas, including SMLLCs. Sole proprietors without an LLC are NOT subject to franchise tax.

## Section 1 -- Scope statement

**In scope:**

- Form 05-102 (Public Information Report -- mandatory annual filing)
- No-tax-due threshold determination; the old Form 05-163 No Tax Due Report is discontinued for report years 2024 and later
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

- **Sole proprietors without an LLC** — Exempt from franchise tax  _(Texas Tax Code §171.001(a))_
- **General partnerships directly owned by natural persons** — Exempt  _(Texas Tax Code §171.001(a))_
- **Passive entities** — Out of scope  _(Texas Tax Code §171.0003)_
- **Combined group reporting** — Out of scope  _(Texas Tax Code §171.1014)_
- **Franchise tax credits (research, clean energy, etc.)** — Out of scope  _(unsure)_
- **Extensions beyond the automatic extension** — Out of scope  _(unsure)_
- **Franchise tax refund claims** — Out of scope  _(unsure)_

### Who must file

- **Who must file** — Every taxable entity formed in Texas or doing business in Texas must file a franchise tax report annually. This includes LLCs, corporations, limited partnerships, and professional associations.  _(Texas Tax Code §171.001)_
- **Key exemption** — Sole proprietors (natural persons operating without an entity) and general partnerships directly owned entirely by natural persons are exempt.  _(Texas Tax Code §171.001(a))_

### Due dates

**Due dates**  _(Texas Tax Code §171.202)_

| Item | Date | Source |
| --- | --- | --- |
| Annual report due date | May 15, 2025 (for accounting year ending in 2024) | Texas Tax Code §171.202 |
| Automatic extension | November 15, 2025 (with 90% of tax paid by May 15) | Texas Comptroller Rule 3.584 |
| Public Information Report (05-102) | Due with the franchise tax report | Texas Tax Code §171.203 |

### Initial filing

- **Initial filing** — A newly formed entity must file its first franchise tax report by May 15 of the year after its formation. The report covers the period from formation through December 31 of that year (or the entity's fiscal year end).  _(unsure)_

## Section 3 -- Rates and thresholds

**Rates and thresholds**  _([Texas Comptroller 2026 Franchise Tax Report Forms; No Tax Due Reporting for Report Year 2024 and Later](https://comptroller.texas.gov/taxes/franchise/forms/2026-franchise.php))_

| Item | Amount | Source |
| --- | --- | --- |
| No-tax-due threshold (2026 report) | $2,650,000 total revenue | Texas Comptroller 2026 franchise forms |
| No-tax-due threshold (2024-2025 reports) | $2,470,000 total revenue | Texas Comptroller / Tax Code §171.006 |
| EZ computation rate | 0.331% of total revenue (apportioned) | Texas Tax Code §171.1016 |
| EZ computation revenue limit | $20,000,000 | Texas Comptroller 2026 franchise forms |
| Standard rate -- retail/wholesale | 0.375% of taxable margin | Texas Tax Code §171.002(b) |
| Standard rate -- other entities | 0.75% of taxable margin | Texas Tax Code §171.002(a) |
| Minimum tax | $0 (no minimum) | Texas Tax Code §171.002 |
| Cost of goods sold alternative | Available per Tax Code §171.1012 | Texas Tax Code §171.1012 |
| Compensation deduction alternative | Available per Tax Code §171.1013; 2026-2027 per-person cap $480,000 | Texas Comptroller 2026 franchise forms |

### No-tax-due threshold

- **No-tax-due threshold filing requirement** — For the 2026 report, an entity with annualized total revenue at or below $2,650,000 owes no franchise tax and is not required to file a No Tax Due Report. Form 05-163 is discontinued for report years 2024 and later. The entity generally must still file Form 05-102 Public Information Report or Form 05-167 Ownership Information Report, unless a specific exception such as a qualifying new veteran-owned business applies.  _([Texas Comptroller No Tax Due Reporting for Report Year 2024 and Later; 2026 Franchise Tax Report Forms](https://comptroller.texas.gov/taxes/franchise/forms/2026-franchise.php))_

### Step 1: Determine if the entity is subject to franchise tax

0. **Step 1** — Is the entity an LLC, LP, LLP, corporation, or other legal entity? --> Subject. Is the entity a sole proprietorship (no LLC)? --> Exempt. STOP. Is the entity a general partnership owned entirely by natural persons? --> Exempt. STOP.

### Step 2: Determine total revenue

0. **Step 2** — Total revenue is computed from federal tax return data: For entities filing federal Form 1040 Schedule C (SMLLCs): total revenue = gross income from Schedule C plus all other revenue items attributable to the entity. Generally: total revenue = gross receipts minus returns and allowances, plus other income items per Texas Tax Code §171.1011.

### Step 3: Apply the no-tax-due threshold

0. **Step 3** — If annualized total revenue <= $2,650,000 for the 2026 report: do not file Form 05-163; it is discontinued. File the required PIR (Form 05-102) or OIR (Form 05-167), unless a specific exception applies. No franchise tax payment required. STOP computation here.  _([Texas Comptroller 2026 Franchise Tax Report Forms](https://comptroller.texas.gov/taxes/franchise/forms/2026-franchise.php))_

### Step 4: Choose computation method

0. **Step 4** — If total revenue > $2,650,000, choose ONE of: **Option A: EZ Computation (if total revenue <= $20,000,000)** - Tax = apportioned total revenue x 0.331% - No deductions for COGS, compensation, or margin. - Simplest method but may result in higher tax. **Option B: Standard computation -- COGS method** - Taxable margin = total revenue - cost of goods sold - Tax = taxable margin x rate (0.375% retail/wholesale or 0.75% other) **Option C: Standard computation -- Compensation method** - Taxable margin = total revenue - compensation - Tax = taxable margin x rate **Option D: 70% of total revenue** - Taxable margin cannot exceed 70% of total revenue. - This is an automatic cap, not an election.

### Step 5: Compute apportionment (if multi-state)

0. **Step 5** — If the entity has revenue from both Texas and other states: Texas apportionment factor = Texas gross receipts / total gross receipts everywhere. Apply factor to taxable margin. For entities operating entirely in Texas: apportionment factor = 100%.

### Step 6: Compute tax due

0. **Step 6** — EZ method: apportioned revenue x 0.331%. Standard method: apportioned taxable margin x applicable rate (0.375% or 0.75%)

### Step 7: Compare computation methods

0. **Step 7** — For standard computation, the tax is the LESSER of: Tax computed using COGS method; Tax computed using compensation method; Tax computed using 70% of total revenue method

### Step 8: File required forms

0. **Step 8** — Regardless of tax due, file the required information report or tax report path: below-threshold entities generally file Form 05-102 PIR or Form 05-167 OIR only; above-threshold entities file E-Z Computation (05-169) or Long Form (05-158-A/B) plus PIR/OIR as applicable. Form 05-163 is discontinued for report years 2024 and later.  _([Texas Comptroller 2026 Franchise Tax Report Forms](https://comptroller.texas.gov/taxes/franchise/forms/2026-franchise.php))_

### E-1: SMLLC is subject even though disregarded federally

- **SMLLC subject even though disregarded federally** — A single-member LLC that is disregarded for federal income tax purposes is treated as a separate taxable entity for Texas franchise tax purposes. The SMLLC must file its own franchise tax report using data from the owner's federal return (Schedule C).  _(Texas Tax Code §171.0002(a))_

### E-2: Passive entities

- **Passive entities** — A qualifying passive entity under Texas Tax Code §171.0003 does not file Form 05-163. For report years 2024 and later, it must file either the E-Z Computation Report or the Long Form, blacken the passive-entity circle, complete the accounting-year fields, sign the report, and generally need not file a PIR or OIR.  _([Texas Comptroller No Tax Due Reporting for Report Year 2024 and Later; 2026 Franchise Tax Report Forms](https://comptroller.texas.gov/taxes/franchise/ntd-rpt-updates-2024.php))_

### E-3: First-year reporting

- **First-year reporting** — A newly formed entity's first franchise tax report covers a short period (date of formation through the entity's first accounting year end). The no-tax-due threshold is NOT prorated for short periods.  _(unsure)_

### E-4: Retail vs. wholesale classification

- **Retail vs. wholesale classification** — Entities primarily engaged in retail or wholesale trade qualify for the reduced 0.375% rate. The entity must derive more than 50% of its total revenue from retail or wholesale activities. Misclassification is a common audit trigger.  _(Texas Tax Code §171.002(b))_

### E-5: COGS for service businesses

- **COGS for service businesses** — Service businesses generally cannot use the COGS method because they do not sell tangible personal property. However, Texas has a broad COGS definition that includes some service costs. Review Texas Tax Code §171.1012 carefully. When in doubt, use the compensation method.  _(Texas Tax Code §171.1012)_

### E-6: No tax due but must still file

- **No tax due but must still file** — Even if the entity owes $0 in franchise tax, the filing requirement remains. Failure to file results in forfeiture of the entity's right to transact business in Texas and potential involuntary termination.  _(unsure)_

### Test 1: Below no-tax-due threshold

**Input:** SMLLC with total revenue of $180,000.
**Expected:** Below $2,650,000 threshold. File Form 05-102 (or Form 05-167 if applicable); do not file Form 05-163. Tax: $0.

### Test 2: EZ computation

**Input:** SMLLC with total revenue of $3,000,000, 100% Texas.
**Expected:** EZ tax: $3,000,000 x 0.331% = $9,930. Compare with standard methods to choose optimal.

### Test 3: Standard computation -- compensation method

**Input:** Service SMLLC. Total revenue: $5,000,000. Compensation paid: $2,000,000. 100% Texas.
**Expected:** Margin: $5,000,000 - $2,000,000 = $3,000,000. Cap: 70% x $5,000,000 = $3,500,000. Use $3,000,000. Tax: $3,000,000 x 0.75% = $22,500.

### Test 4: Retail entity at reduced rate

**Input:** Retail SMLLC. Total revenue: $4,000,000. COGS: $2,500,000.
**Expected:** Margin: $1,500,000. Cap: $2,800,000. Use $1,500,000. Tax: $1,500,000 x 0.375% = $5,625.

### Test 5: Sole proprietor (no entity)

**Input:** Individual freelancer with no LLC.
**Expected:** NOT subject to TX franchise tax. No filing required.

## Section 7 -- Prohibitions

- **P-1** — Do NOT tell a sole proprietor (without an LLC) that they must file franchise tax. They are exempt.  _(unsure)_
- **P-2** — Do NOT prorate the no-tax-due threshold for short-period returns.  _(unsure)_
- **P-3** — Do NOT use the COGS method for a service business without verifying that the costs qualify under §171.1012.  _(Texas Tax Code §171.1012)_
- **P-4** — Do NOT skip the Public Information Report (05-102). It is always required.  _(unsure)_
- **P-5** — Do NOT classify an entity as retail/wholesale for the reduced rate unless >50% of revenue is from retail/wholesale activities.  _(unsure)_
- **P-6** — Do NOT advise on whether to form or dissolve an LLC based on franchise tax implications. That is legal advice.  _(unsure)_

## Section 8 -- Self-checks

Before delivering output, verify:

- [ ] Entity type correctly identified (SMLLC vs. sole proprietor)
- [ ] Total revenue computed from correct federal return data
- [ ] No-tax-due threshold of $2,650,000 applied
- [ ] Form 05-102 (Public Information Report) included in every filing
- [ ] EZ computation only used if revenue <= $20,000,000
- [ ] Correct rate applied (0.75% other vs. 0.375% retail/wholesale)
- [ ] 70% of total revenue cap applied as automatic limit
- [ ] All computation methods compared to select the lowest tax
- [ ] Short-period threshold NOT prorated

## Section 9 -- Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is
different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your
jurisdiction — **no liability on either side until you and the accountant sign
a formal engagement letter** — book a free 30-minute call:

**→ [Book a call](https://calendly.com/openaccountants-info/30min)**

We'll route you to the named verifier covering your country or state. You can
also see the full list of verified accountants at
[openaccountants.com/network](https://openaccountants.com/network).

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
