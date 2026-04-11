---
name: tx-sales-use-tax
description: >
  Texas Sales and Use Tax return (Form 01-114) for self-employed individuals and small businesses. Covers the 6.25% state rate, local tax add-ons (up to 2%), combined maximum of 8.25%, use tax, data processing services exemption under Section 151.351, and filing frequencies. Primary source: Texas Tax Code Chapter 151.
version: 1.0
jurisdiction: US-TX
tax_year: 2025
category: state
depends_on:
  - us-tax-workflow-base
validated: April 2026
---

# Texas Sales and Use Tax (Form 01-114) v1.0

## What this file is

**Obligation category:** CT (Consumption Tax)
**Functional role:** Return preparation
**Status:** Complete

This is a Tier 2 content skill for preparing the Texas sales and use tax return (Form 01-114) for sole proprietors and small businesses selling taxable goods or services in Texas.

---

## Section 1 -- Scope statement

**In scope:**

- Form 01-114 (Texas Sales and Use Tax Return)
- State sales tax at 6.25%
- Local sales tax (city, county, transit, special purpose districts)
- Use tax on out-of-state purchases
- Data processing services 20% exemption (§151.351)
- Taxable services enumeration
- Timely filing discount
- Filing frequency determination

**Out of scope (refused):**

- Motor vehicle sales tax (Form 14-117)
- Franchise tax (separate skill)
- Mixed beverage taxes
- Hotel occupancy tax
- Marketplace provider obligations
- Multi-state nexus analysis
- Tax refund/credit claims

---

## Section 2 -- Filing requirements

### Who must register

Any person who sells, leases, or rents taxable tangible personal property or taxable services in Texas must obtain a Texas sales tax permit. There is no fee for the permit. **Source:** Texas Tax Code §151.201.

### Filing frequency

| Quarterly tax liability | Filing frequency | Source |
|------------------------|------------------|--------|
| $0 -- $500/quarter | Annually (due January 20) | Texas Comptroller Rule 3.286 |
| $500 -- $1,500/quarter | Quarterly (due 20th after quarter) | Texas Comptroller Rule 3.286 |
| Over $1,500/quarter | Monthly (due 20th of following month) | Texas Comptroller Rule 3.286 |
| $500,000+/quarter | Monthly with prepayment option | Texas Tax Code §151.424 |

**Due date:** The 20th of the month following the reporting period. If the 20th falls on a weekend or holiday, the next business day.

---

## Section 3 -- Rates and thresholds

| Item | Rate | Source |
|------|------|--------|
| State sales tax | 6.25% | Texas Tax Code §151.051 |
| Maximum local tax | 2.00% | Texas Tax Code §321.101, §322.103 |
| Maximum combined rate | 8.25% | Texas Tax Code §151.051 + local caps |
| Use tax | Same as sales tax (6.25% state + local) | Texas Tax Code §151.101 |

### Local tax components

The local 2% maximum is composed of:

| Component | Maximum rate | Source |
|-----------|-------------|--------|
| City sales tax | 2.00% (within the 2% cap) | Texas Tax Code §321.101 |
| County sales tax | 0.50% | Texas Tax Code §323.101 |
| Transit authority tax | 1.00% | Texas Tax Code §322.103 |
| Special purpose district tax | varies | Various statutes |

Total local taxes cannot exceed 2.00% for any location.

### Timely filing discount (prepayment discount)

| Item | Amount | Source |
|------|--------|--------|
| Timely filing discount | 0.5% of tax due (max $500/reporting period for monthly/quarterly filers) | Texas Tax Code §151.423 |

The discount is forfeited if the return is filed or paid late.

---

## Section 4 -- Computation rules (Step format)

### Step 1: Classify all sales

For each transaction, determine:
1. **Tangible personal property or taxable service?** If yes, taxable unless an exemption applies.
2. **Exempt?** (See Section 5.)
3. **Location of sale.** Texas is destination-based for intrastate sales. The rate is determined by the delivery location.

### Step 2: Compute total sales (01-114 Item 1)

Sum of all gross sales, rentals, and leases of taxable items.

### Step 3: Compute taxable sales (01-114 Item 2)

Total sales minus exempt sales (sales for resale, exempt items, out-of-state sales).

### Step 4: Compute state tax (01-114 Item 3)

Taxable sales x 6.25% = state sales tax.

### Step 5: Compute local tax (01-114 Item 4)

For each delivery location:
- Look up the combined local rate (city + county + transit + special).
- Taxable sales to that location x local rate.
- Sum all local tax amounts.

### Step 6: Compute use tax (01-114 Item 5)

For purchases on which no Texas tax was collected:
- Purchase price x (6.25% state + applicable local rate) = use tax.
- Credit allowed for sales tax paid to another state (limited to the Texas rate).

### Step 7: Compute total tax (01-114 Item 6)

State tax + local tax + use tax = total tax.

### Step 8: Apply timely filing discount (01-114 Item 7)

If filing on time: total tax x 0.5%, capped at $500 per period.

### Step 9: Compute net tax due (01-114 Item 8)

Total tax - timely filing discount = net tax due.

---

## Section 5 -- Edge cases and special rules

### E-1: Data processing services -- 20% exemption

The sale of data processing services is taxable, BUT 20% of the charge is exempt. Only 80% of the data processing service charge is subject to sales tax. **Source:** Texas Tax Code §151.351.

Data processing services include word processing, data entry, data retrieval, data search, information compilation, payroll processing, and similar computer-based services. **Source:** Texas Tax Code §151.0035.

Example: $10,000 data processing invoice. Taxable amount: $10,000 x 80% = $8,000. Tax: $8,000 x 8.25% = $660.

### E-2: Internet access and web hosting

Internet access services are exempt from Texas sales tax (per the federal Internet Tax Freedom Act). Web hosting is classified as a data processing service and is taxable (at the 80% rate). **Source:** Texas Comptroller Rule 3.330.

### E-3: Software

- Canned software (sold off-the-shelf or downloaded): taxable as tangible personal property.
- Custom software (written to specific customer specs): exempt.
- SaaS (Software as a Service): the Comptroller's position treats SaaS as a data processing service (taxable at 80%). Some taxpayers dispute this classification.

### E-4: Manufacturing exemptions

Tangible personal property directly used in manufacturing is exempt. This includes machinery, equipment, and materials that become an ingredient or component of a manufactured product for sale. **Source:** Texas Tax Code §151.318.

### E-5: Agricultural exemptions

Farm machinery, feed, seed, and fertilizer are exempt when used exclusively in agricultural production. Requires a valid agricultural exemption certificate (Ag/Timber Number). **Source:** Texas Tax Code §151.316.

### E-6: Occasional sales

A person who does not regularly sell tangible personal property is not required to collect sales tax on an occasional sale, provided they do not make more than two sales of taxable items in a 12-month period. **Source:** Texas Tax Code §151.304(a).

### E-7: Destination-based sourcing

Texas is destination-based: the local tax rate is determined by the location where the item is received by the purchaser. For shipped goods, this is the ship-to address. For pickup, this is the seller's location. **Source:** Texas Tax Code §321.203.

---

## Section 6 -- Test suite

### Test 1: Basic monthly return

- **Input:** Retailer in Houston (combined rate 8.25%). Taxable sales: $50,000.
- **Expected:** State tax: $50,000 x 6.25% = $3,125. Local tax: $50,000 x 2.0% = $1,000. Total: $4,125. Discount: $4,125 x 0.5% = $20.63. Net: $4,104.37.

### Test 2: Data processing service

- **Input:** IT consultant in Dallas (combined rate 8.25%). Data processing services: $20,000.
- **Expected:** Taxable amount: $20,000 x 80% = $16,000. Tax: $16,000 x 8.25% = $1,320. Discount: $1,320 x 0.5% = $6.60. Net: $1,313.40.

### Test 3: Mixed sales with exemptions

- **Input:** Retailer selling $30,000 general merchandise + $5,000 sold for resale (with valid resale certificate).
- **Expected:** Taxable: $30,000. Exempt: $5,000. Tax on $30,000 at applicable combined rate.

### Test 4: Use tax

- **Input:** Business purchases $3,000 of office supplies from out-of-state vendor, no tax collected. Located in Austin (8.25%).
- **Expected:** Use tax: $3,000 x 8.25% = $247.50.

### Test 5: Late filing

- **Input:** Same as Test 1 but filed 5 days late.
- **Expected:** No timely filing discount. Penalty: 5% of tax due ($206.25). Interest applies.

---

## Section 7 -- Prohibitions

- **P-1:** Do NOT apply origin-based sourcing. Texas is destination-based for local tax.
- **P-2:** Do NOT tax the full amount of data processing services. Only 80% is taxable.
- **P-3:** Do NOT classify all software as taxable. Custom software is exempt.
- **P-4:** Do NOT claim the timely filing discount on a late return.
- **P-5:** Do NOT apply local tax rates exceeding the 2% cap.
- **P-6:** Do NOT accept a resale certificate without verifying the purchaser's sales tax permit number.

---

## Section 8 -- Self-checks

Before delivering output, verify:

- [ ] All transactions classified as taxable, exempt, or for resale
- [ ] State rate of 6.25% applied correctly
- [ ] Local rate verified for each delivery destination (destination-based)
- [ ] Combined rate does not exceed 8.25%
- [ ] Data processing services taxed at 80% only
- [ ] Use tax reported for out-of-state purchases
- [ ] Timely filing discount applied (or forfeited if late)
- [ ] Filing frequency matches liability thresholds
- [ ] Resale certificates on file for exempt sales

---

## Section 9 -- Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
