---
name: fl-sales-use-tax
description: >
  Florida Sales and Use Tax return (Form DR-15) for self-employed individuals and small businesses. Covers the 6% state sales tax rate, county discretionary sales surtax, use tax on out-of-state purchases, exempt transactions, filing frequencies, and dealer collection allowance. Primary source: Florida Statutes Chapter 212.
version: 1.0
jurisdiction: US-FL
tax_year: 2025
category: state
depends_on:
  - us-tax-workflow-base
validated: April 2026
---

# Florida Sales and Use Tax (DR-15) v1.0

## What this file is

**Obligation category:** CT (Consumption Tax)
**Functional role:** Return preparation
**Status:** Complete

This is a Tier 2 content skill that loads on top of `us-tax-workflow-base`. It covers the preparation of Form DR-15 (Sales and Use Tax Return) for Florida-registered dealers who are sole proprietors or single-member LLCs.

**Tax year coverage.** This skill targets **tax year 2025** (returns filed monthly, quarterly, semiannually, or annually depending on tax liability).

---

## Section 1 -- Scope statement

**In scope:**

- Form DR-15 (Sales and Use Tax Return)
- Form DR-15EZ (simplified return for dealers with no surtax obligation)
- Sole proprietors and single-member LLCs registered as Florida dealers
- Taxable sales of tangible personal property
- Taxable services (commercial pest control, detective/security, nonresidential cleaning, commercial interior design)
- Use tax on purchases where sales tax was not collected
- Discretionary sales surtax by county
- Collection allowance (vendor discount)
- Filing frequency determination

**Out of scope (refused):**

- Form DR-1 (Application for Sales Tax Registration) -- separate process
- Communications services tax (Form DR-700016)
- Solid waste fees, lead-acid battery fees, tire fees
- Transient rental taxes (tourist development tax)
- Sales tax on commercial real property leases beyond basic classification
- Marketplace provider obligations (Amazon, Etsy platform responsibilities)
- Multi-state sales tax nexus analysis

---

## Section 2 -- Filing requirements

### Who must register

Any person who makes or intends to make taxable sales or charges admission in Florida must register as a dealer with the Florida Department of Revenue (FDOR). Registration is free. **Source:** §212.18, F.S.

### Filing frequency

| Annual taxable sales | Filing frequency | Source |
|---------------------|------------------|--------|
| $1,000 or less per year | Annual (due January 20) | FDOR Rule 12A-1.056, F.A.C. |
| $1,001 -- $2,500 per year | Semiannual (due January 20 and July 20) | FDOR Rule 12A-1.056, F.A.C. |
| $2,501 -- $12,000 per year | Quarterly (due 1st/20th after quarter end) | FDOR Rule 12A-1.056, F.A.C. |
| Over $12,000 per year | Monthly (due 1st/20th after month end) | FDOR Rule 12A-1.056, F.A.C. |

**Due date:** The 1st through the 20th of the month following the reporting period. If the 20th falls on a Saturday, Sunday, or state/federal holiday, the due date is the next business day.

**Electronic filing:** Required for all dealers remitting $20,000+ in tax during the prior state fiscal year (July 1 -- June 30). All other dealers may file electronically or by paper. **Source:** §213.755, F.S.

---

## Section 3 -- Rates and thresholds

### State sales tax rate

| Item | Rate | Source |
|------|------|--------|
| State sales tax | 6.0% | §212.05, F.S. |
| State use tax | 6.0% | §212.06, F.S. |

### Discretionary sales surtax (selected counties, 2025)

The surtax is levied by individual counties and applies to the first $5,000 of any single taxable transaction. **Source:** §212.055, F.S.

| County | Surtax rate | Combined rate | Source |
|--------|-------------|---------------|--------|
| Miami-Dade | 1.0% | 7.0% | FDOR Form DR-15DSS (2025) |
| Broward | 1.0% | 7.0% | FDOR Form DR-15DSS (2025) |
| Hillsborough (Tampa) | 1.5% | 7.5% | FDOR Form DR-15DSS (2025) |
| Orange (Orlando) | 0.5% | 6.5% | FDOR Form DR-15DSS (2025) |
| Duval (Jacksonville) | 1.5% | 7.5% | FDOR Form DR-15DSS (2025) |
| Palm Beach | 1.0% | 7.0% | FDOR Form DR-15DSS (2025) |
| Alachua (Gainesville) | 1.0% | 7.0% | FDOR Form DR-15DSS (2025) |

**Important:** The surtax rate is determined by the county where the goods are delivered or services performed. The dealer must look up the current rate on Form DR-15DSS for each county. Rates change periodically.

### Collection allowance (vendor discount)

| Item | Amount | Source |
|------|--------|--------|
| Collection allowance | 2.5% of first $1,200 in tax due (max $25/month or equivalent per period) | §212.12(1), F.S. |

The collection allowance is a compensation to the dealer for collecting and remitting sales tax. It is applied as a deduction on Line 9 of Form DR-15. The allowance is forfeited if the return is filed late.

### Bracket system for tax on partial dollars

Florida uses a bracket system rather than rounding. The bracket table must be used to compute tax on individual transactions. **Source:** §212.12(9), F.S.; FDOR bracket chart.

---

## Section 4 -- Computation rules (Step format)

### Step 1: Classify all transactions

For each sale during the reporting period, determine:

1. **Taxable or exempt?** See Section 5 for exemptions.
2. **Location of delivery.** Determines which county surtax applies.
3. **Single transaction amount.** Surtax applies only to the first $5,000 of each transaction.

### Step 2: Compute gross sales (DR-15 Line 1)

Sum of all sales (taxable and exempt) during the reporting period.

### Step 3: Compute exempt sales (DR-15 Line 2)

Sum of all exempt sales (see Section 5). Subtract from Line 1.

### Step 4: Compute taxable amount (DR-15 Line 3)

Line 1 minus Line 2 = taxable amount.

### Step 5: Compute state sales tax (DR-15 Line 4)

Taxable amount x 6.0% = state sales tax due.

### Step 6: Compute discretionary sales surtax (DR-15 Line 5)

For each county where sales were delivered:
- Identify the applicable surtax rate from DR-15DSS.
- Apply surtax to the first $5,000 of each individual taxable transaction in that county.
- Sum all surtax amounts.

### Step 7: Compute use tax (DR-15 Line 6)

For purchases where the seller did not collect Florida sales tax:
- Apply 6.0% state rate + applicable county surtax rate.
- Include purchases from out-of-state sellers, internet purchases, and items removed from exempt inventory for personal use.

### Step 8: Compute gross tax (DR-15 Line 7)

Line 4 + Line 5 + Line 6 = gross tax.

### Step 9: Apply lawful deductions (DR-15 Lines 8-9)

- Line 8: Credit memo adjustments for returned merchandise.
- Line 9: Collection allowance (2.5% of first $1,200 of tax due, max $25). Forfeited if late.

### Step 10: Compute net tax due (DR-15 Line 10)

Line 7 minus Line 8 minus Line 9 = net tax due.

### Step 11: Apply penalty and interest if late

| Item | Rate | Source |
|------|------|--------|
| Penalty (1-30 days late) | 10% of tax due | §213.235, F.S. |
| Penalty (over 30 days late) | 10% of tax due + additional penalties | §213.235, F.S. |
| Interest | Floating rate per §213.235, F.S. (updated annually) | §213.235, F.S. |
| Minimum penalty | None stated | §213.235, F.S. |

---

## Section 5 -- Edge cases and special rules

### E-1: Common exemptions

- Groceries (unprepared food for home consumption) -- exempt. **Source:** §212.08(1), F.S.
- Prescription drugs and medical supplies -- exempt. **Source:** §212.08(2), F.S.
- Items purchased for resale (with valid DR-13 resale certificate) -- exempt. **Source:** §212.07(1), F.S.
- Agricultural inputs (feed, seed, fertilizer with DR-14A certificate) -- exempt.
- Certain packaging materials used to package tangible personal property for sale.

### E-2: Services generally not taxable

Most services in Florida are NOT subject to sales tax. Only specifically enumerated services are taxable: nonresidential pest control, burglar protection/detective services, nonresidential building cleaning, and commercial interior design services. **Source:** §212.05(1), F.S.

### E-3: Software and digital goods

- Canned (prewritten) software delivered on tangible media: taxable.
- Canned software delivered electronically (SaaS, downloads): generally taxable per FDOR TAA 14A-032. However, custom software is exempt.
- Digital books, music, movies: Florida does NOT tax these as of 2025.

### E-4: Surtax cap on single transactions

The $5,000 surtax cap applies per single item. If a customer buys 10 items at $2,000 each in one transaction, the surtax applies to the first $5,000 of EACH item, not the transaction total. **Source:** §212.054, F.S.

### E-5: Commercial rent

Rental of commercial real property is subject to the 5.5% state rate (NOT 6%) plus applicable surtax. This is a separate line on DR-15 and uses a different rate. **Source:** §212.031, F.S.

### E-6: Zero returns

Dealers with no taxable activity during a reporting period must still file a return showing zero tax due. Failure to file zero returns results in delinquency notices and potential revocation of the dealer's registration.

---

## Section 6 -- Test suite

### Test 1: Basic monthly return

- **Input:** Sole proprietor, Broward County. Gross sales: $15,000. All taxable, all delivered in Broward. No exempt sales.
- **Expected:** State tax: $15,000 x 6% = $900. Surtax: $15,000 x 1% = $150 (all items under $5,000). Gross tax: $1,050. Collection allowance: $1,050 x 2.5% = $26.25, capped at $25. Net tax: $1,025.

### Test 2: Mixed county sales

- **Input:** Sales of $8,000 delivered in Orange County (0.5% surtax) and $4,000 delivered in Miami-Dade (1.0% surtax).
- **Expected:** State tax: $12,000 x 6% = $720. Surtax: ($8,000 x 0.5%) + ($4,000 x 1.0%) = $40 + $40 = $80. Gross tax: $800.

### Test 3: Transaction exceeding $5,000 surtax cap

- **Input:** Single sale of $10,000 in Hillsborough County (1.5% surtax).
- **Expected:** State tax: $10,000 x 6% = $600. Surtax: $5,000 x 1.5% = $75 (capped at first $5,000). Gross tax: $675.

### Test 4: Late filing

- **Input:** Monthly return, 15 days late. Tax due: $500.
- **Expected:** Penalty: $500 x 10% = $50. Collection allowance: forfeited. Total due: $550 plus interest.

### Test 5: Use tax on out-of-state purchase

- **Input:** Business purchased $2,000 of office equipment from an out-of-state vendor that did not collect FL tax. Business located in Palm Beach County (1.0% surtax).
- **Expected:** Use tax: $2,000 x 7% = $140.

---

## Section 7 -- Prohibitions

- **P-1:** Do NOT accept a resale certificate (DR-13) without verifying it is properly completed and the buyer is a registered dealer.
- **P-2:** Do NOT apply the surtax to amounts exceeding $5,000 per individual item in a transaction.
- **P-3:** Do NOT claim the collection allowance on a late-filed return.
- **P-4:** Do NOT charge the 6% rate on commercial real property rent; the rate is 5.5%.
- **P-5:** Do NOT classify all software as taxable -- custom software is exempt.
- **P-6:** Do NOT assume digital goods are taxable in Florida. As of 2025, they generally are not.

---

## Section 8 -- Self-checks

Before delivering output, verify:

- [ ] All transactions classified as taxable or exempt with statutory basis
- [ ] Correct surtax rate applied for each delivery county (verified against current DR-15DSS)
- [ ] Surtax cap of $5,000 per item applied correctly
- [ ] Collection allowance computed correctly and not claimed on late returns
- [ ] Use tax included for out-of-state purchases where no FL tax was collected
- [ ] Filing frequency matches annual tax liability threshold
- [ ] Zero return filed if no activity (not skipped)
- [ ] Commercial rent at 5.5% (not 6%)
- [ ] Reviewer brief includes any classification uncertainties

---

## Section 9 -- Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
