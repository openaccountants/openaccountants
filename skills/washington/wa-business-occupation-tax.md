---
name: wa-business-occupation-tax
description: >
  Washington State Business and Occupation (B&O) Tax for self-employed individuals. Covers gross receipts tax classifications (service/other, retailing, wholesaling, manufacturing), B&O tax rates, small business credit (SBC), city B&O taxes, and filing frequencies on the Combined Excise Tax Return. Primary source: RCW 82.04.
version: 1.0
jurisdiction: US-WA
tax_year: 2025
category: state
depends_on:
  - us-tax-workflow-base
validated: April 2026
---

# Washington B&O Tax v1.0

## What this file is

**Obligation category:** IT (Income Tax equivalent -- gross receipts)
**Functional role:** Computation + Return
**Status:** Complete

This is a Tier 2 content skill for computing Washington's Business and Occupation Tax. Washington has no personal income tax; instead, it imposes a gross receipts tax (B&O) on almost all business activity. The B&O tax is levied on gross income -- there is no deduction for costs of doing business, labor, materials, or overhead.

---

## Section 1 -- Scope statement

**In scope:**

- Combined Excise Tax Return (B&O section)
- All major B&O classifications: service/other, retailing, wholesaling, manufacturing
- Small business credit (SBC)
- Filing frequency determination
- City B&O tax overview (Seattle, Tacoma, Bellevue, etc.)

**Out of scope (refused):**

- Retail sales tax (separate skill: wa-sales-tax)
- Use tax computation
- Insurance premiums tax
- Real estate excise tax
- City B&O tax return preparation (each city has its own return)
- Multi-activity tax credit (MATC) beyond basic explanation
- International fuel tax agreement
- Timber tax

---

## Section 2 -- Filing requirements

### Who must file

Any person, business, or organization engaging in business activity in Washington is subject to B&O tax, regardless of whether the activity is profitable. There is no minimum filing threshold -- if you do business in Washington, you must register and file. **Source:** RCW 82.04.220.

### Registration

All businesses must register with the Washington Department of Revenue (DOR) before conducting business. Registration is free via the Business Licensing Service (BLS). **Source:** RCW 82.32.030.

### Filing frequency

| Gross income | Filing frequency | Source |
|-------------|------------------|--------|
| Less than $28,000/year and less than $4,200/month tax liability | Annual (due April 15) | WAC 458-20-22801 |
| $28,000 -- $420,000/year | Quarterly (due last day of month following quarter) | WAC 458-20-22801 |
| Over $420,000/year | Monthly (due 25th of following month) | WAC 458-20-22801 |

---

## Section 3 -- Rates and thresholds

### B&O tax rate schedule (2025)

| Classification | Rate | RCW |
|---------------|------|-----|
| Retailing | 0.471% | RCW 82.04.250 |
| Wholesaling | 0.484% | RCW 82.04.270 |
| Manufacturing | 0.484% | RCW 82.04.240 |
| Service and Other Activities | 1.50% | RCW 82.04.290(2) |
| Printing/publishing | 0.484% | RCW 82.04.260 |
| Travel agents, insurance agents | 0.275% | RCW 82.04.260 |
| Real estate brokers | 1.50% | RCW 82.04.290(2) |
| Royalty income | 1.50% | RCW 82.04.290(2) |
| International services (qualifying) | 0.275% | RCW 82.04.261 |

### Small Business Credit (SBC)

| Item | Amount | Source |
|------|--------|--------|
| Maximum credit (service/other at 1.5%) | $70 per month / $210 per quarter / $840 per year | RCW 82.04.4451 |
| Phase-in range (service/other) | Gross income $0 -- $250,000/year | RCW 82.04.4451 |
| Phase-out complete | Gross income > $250,000/year | RCW 82.04.4451 |

The SBC is designed to reduce the tax burden on small businesses. It is computed separately for each B&O classification. The credit phases out as gross income approaches $250,000 per year.

**SBC formula (service/other, annual):**
- If gross income <= $125,000: full credit ($840/year)
- If gross income > $125,000 and <= $250,000: credit = $840 x (1 - (gross income - $125,000) / $125,000)
- If gross income > $250,000: no credit

---

## Section 4 -- Computation rules (Step format)

### Step 1: Classify all income

Every dollar of gross income must be classified into a B&O category:

| Activity | Classification |
|----------|---------------|
| Selling tangible goods to end consumers | Retailing |
| Selling tangible goods to other businesses for resale | Wholesaling |
| Making/fabricating goods | Manufacturing |
| Providing professional services (consulting, legal, IT, design) | Service/Other |
| Software development services | Service/Other |
| Selling prewritten (canned) software | Retailing |

### Step 2: Compute gross income by classification

For each classification, total the gross income earned during the reporting period. **Gross income means the TOTAL amount received -- no deductions for expenses, COGS, or labor.**

### Step 3: Compute B&O tax by classification

For each classification:
- Gross income x applicable rate = B&O tax.

### Step 4: Apply Small Business Credit

Compute the SBC for each classification based on annualized gross income in that classification. Apply as a reduction to the tax.

### Step 5: Apply any other credits

- Multiple Activities Tax Credit (MATC): prevents pyramiding when the same product is subject to B&O tax at multiple stages (e.g., manufacturing AND selling). The MATC allows a credit for the lower-rate classification's tax.
- Other specialized credits (high-technology R&D, etc.).

### Step 6: Compute total B&O tax due

Sum of all classifications' tax minus credits = total B&O tax due.

### Step 7: Report on Combined Excise Tax Return

B&O tax is reported on the B&O section of the Combined Excise Tax Return alongside retail sales tax and use tax.

---

## Section 5 -- Edge cases and special rules

### E-1: No deductions for expenses

The B&O tax is on GROSS income, not net income. There is no deduction for wages, rent, materials, COGS, or any other business expense. This is the fundamental difference from an income tax. **Source:** RCW 82.04.080.

### E-2: Multiple classifications

A business may have income in multiple B&O classifications. Each must be reported separately at its respective rate. For example, a software company that sells canned software (retailing at 0.471%) and provides custom development services (service/other at 1.50%) must separate these revenue streams.

### E-3: Service vs. retailing for digital goods

- Selling prewritten software (even digitally delivered): retailing (0.471%).
- Custom software development: service/other (1.50%).
- SaaS: generally service/other (1.50%), though classification continues to evolve.

### E-4: Interstate sales deductions

Gross income from sales delivered outside Washington may be deductible for B&O purposes if the taxpayer does not have nexus in the destination state. This is the Interstate and Foreign Sales deduction under RCW 82.04.4286. Verify nexus carefully.

### E-5: City B&O taxes

Several Washington cities impose their own B&O taxes in addition to the state B&O tax. Major examples:

| City | Rate (service/other) | Filing |
|------|---------------------|--------|
| Seattle | 0.415% (most services) | FileLocal or city portal |
| Tacoma | 0.200% | FileLocal |
| Bellevue | 0.150% | FileLocal |
| Everett | 0.100% | FileLocal |

City B&O taxes are NOT reported on the state Combined Excise Tax Return. They are filed separately, often through the FileLocal portal.

### E-6: Occasional sales exemption

The occasional sale of tangible personal property is generally not subject to B&O tax if the seller does not engage in the business of selling such property. This does not apply to service income.

### E-7: Nexus for out-of-state businesses

Physical presence or economic nexus (> $100,000 in receipts from Washington sources) triggers B&O tax filing obligations. **Source:** RCW 82.04.067.

---

## Section 6 -- Test suite

### Test 1: Freelance consultant

- **Input:** Software consultant, all service income in WA. Gross income: $100,000/year.
- **Expected:** B&O tax: $100,000 x 1.50% = $1,500. SBC: $840 x (1 - ($100,000 - $125,000)/$125,000) -- since $100,000 < $125,000, full credit = $840. Net tax: $660.

### Test 2: Above SBC phase-out

- **Input:** Consultant with $300,000 gross income, all service/other.
- **Expected:** B&O tax: $300,000 x 1.50% = $4,500. SBC: $0 (above $250,000). Net tax: $4,500.

### Test 3: Retailer

- **Input:** Online retailer. Gross receipts from WA sales: $200,000.
- **Expected:** B&O tax: $200,000 x 0.471% = $942. SBC for retailing computed separately.

### Test 4: Mixed classification

- **Input:** Software company. Canned software sales: $150,000 (retailing). Custom development: $100,000 (service/other).
- **Expected:** Retailing B&O: $150,000 x 0.471% = $706.50. Service B&O: $100,000 x 1.50% = $1,500. SBC computed per classification. Total before SBC: $2,206.50.

### Test 5: Gross vs. net trap

- **Input:** Consultant with $200,000 gross income and $80,000 in expenses.
- **Expected:** B&O tax on FULL $200,000, NOT $120,000. Tax: $200,000 x 1.50% = $3,000.

---

## Section 7 -- Prohibitions

- **P-1:** Do NOT deduct business expenses from gross income for B&O computation. The tax is on gross receipts.
- **P-2:** Do NOT apply a single B&O rate to all income. Each classification has its own rate.
- **P-3:** Do NOT claim the SBC for classifications where annual gross income exceeds $250,000.
- **P-4:** Do NOT report city B&O taxes on the state Combined Excise Tax Return. They are separate filings.
- **P-5:** Do NOT confuse B&O tax with retail sales tax. They are separate obligations; a business may owe both.
- **P-6:** Do NOT assume SaaS classification is settled. Flag for reviewer if SaaS revenue is material.

---

## Section 8 -- Self-checks

Before delivering output, verify:

- [ ] All income classified into correct B&O categories
- [ ] Gross income used (no expense deductions)
- [ ] Correct rate applied per classification
- [ ] SBC computed per classification, not aggregated
- [ ] SBC phase-out applied for income between $125K and $250K
- [ ] Multi-activity tax credit considered if applicable
- [ ] Filing frequency matches gross income thresholds
- [ ] City B&O obligations identified (not computed here but flagged)
- [ ] Interstate sales deduction evaluated

---

## Section 9 -- Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
