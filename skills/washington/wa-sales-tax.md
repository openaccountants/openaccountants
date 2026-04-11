---
name: wa-sales-tax
description: >
  Washington State Sales Tax for self-employed individuals selling taxable goods or services. Covers the 6.5% state rate, local tax add-ons, destination-based sourcing, use tax, and the Combined Excise Tax Return. Primary source: RCW 82.08 (sales tax), RCW 82.12 (use tax).
version: 1.0
jurisdiction: US-WA
tax_year: 2025
category: state
depends_on:
  - us-tax-workflow-base
validated: April 2026
---

# Washington Sales Tax v1.0

## What this file is

**Obligation category:** CT (Consumption Tax)
**Functional role:** Return preparation
**Status:** Complete

This is a Tier 2 content skill for the Washington state retail sales tax and use tax portion of the Combined Excise Tax Return. Washington has a 6.5% state rate plus local rates that vary by location, using destination-based sourcing.

---

## Section 1 -- Scope statement

**In scope:**

- Combined Excise Tax Return (retail sales tax and use tax sections)
- State retail sales tax at 6.5%
- Local sales tax (city, county, transit, regional transit)
- Destination-based sourcing rules
- Use tax on purchases where no WA sales tax was collected
- Reseller permits and exemptions

**Out of scope (refused):**

- B&O tax computation (separate skill: wa-business-occupation-tax)
- Motor vehicle excise tax
- Real estate excise tax
- Spirits/tobacco/cannabis taxes
- Marketplace facilitator obligations (platform responsibilities)
- Multi-state nexus analysis

---

## Section 2 -- Filing requirements

### Who must collect

Any person making retail sales of tangible personal property or certain services in Washington must collect and remit retail sales tax. The seller must register with the Washington DOR. **Source:** RCW 82.08.050.

### Filing frequency

Filing frequency aligns with the same thresholds used for B&O tax (the Combined Excise Tax Return reports both):

| Tax liability | Filing frequency | Due date |
|--------------|------------------|----------|
| Small (annual option) | Annual | April 15 |
| Medium | Quarterly | Last day of month following quarter |
| Large | Monthly | 25th of following month |

---

## Section 3 -- Rates and thresholds

### State rate

| Item | Rate | Source |
|------|------|--------|
| State retail sales tax | 6.5% | RCW 82.08.020 |
| State use tax | 6.5% | RCW 82.12.020 |

### Local rate examples (2025)

Local rates vary significantly. Washington has over 400 local tax jurisdictions. Selected examples:

| Location | Local rate | Combined rate | Source |
|----------|-----------|---------------|--------|
| Seattle | 3.60% | 10.10% | DOR tax rate lookup |
| Tacoma | 3.80% | 10.30% | DOR tax rate lookup |
| Bellevue | 3.60% | 10.10% | DOR tax rate lookup |
| Spokane | 2.40% | 8.90% | DOR tax rate lookup |
| Vancouver (Clark Co.) | 2.00% | 8.50% | DOR tax rate lookup |
| Unincorporated King Co. | 3.60% | 10.10% | DOR tax rate lookup |

**Critical:** Always use the DOR tax rate lookup tool (dor.wa.gov) to determine the exact rate for each delivery address. Rates change quarterly.

### Sourcing

Washington uses **destination-based sourcing** for all retail sales:
- Delivered goods: tax rate where the buyer receives the goods.
- Over-the-counter (pickup): tax rate of the seller's location.
- Services: tax rate where the service is received/performed.
- Digital goods/services: tax rate of the buyer's address.

**Source:** RCW 82.32.730 (Streamlined Sales and Use Tax Agreement conformity).

---

## Section 4 -- Computation rules (Step format)

### Step 1: Determine taxable vs. exempt sales

For each sale, determine:
1. Is the item tangible personal property or an enumerated taxable service? If yes, taxable unless exempt.
2. Does the buyer have a valid reseller permit? If yes, the sale is exempt (sale for resale).
3. Does another exemption apply? (See Section 5.)

### Step 2: Determine the tax rate by destination

For each taxable sale:
1. Identify the delivery address (ship-to or pickup location).
2. Look up the combined rate (state + local) for that address using the DOR tax rate lookup.
3. Identify the location code (4-digit code) for reporting.

### Step 3: Compute sales tax collected

For each rate/location combination:
- Taxable sales x combined rate = sales tax.

### Step 4: Report on Combined Excise Tax Return

Group sales by location code. Report:
- Gross sales
- Exempt/deductible sales
- Taxable sales
- Tax collected
- Location code

### Step 5: Compute use tax

For items purchased for use in Washington where no sales tax was collected:
- Purchase price x combined rate (for the location where the item will be used) = use tax.

### Step 6: Reconcile and remit

Total sales tax collected + use tax owed = total tax due.

If sales tax collected exceeds the amount due (rounding differences), the excess is still remitted.

---

## Section 5 -- Edge cases and special rules

### E-1: Services -- most are NOT taxable

Washington taxes retail sales of tangible personal property and certain specifically enumerated services. Most professional services (consulting, legal, accounting, marketing) are NOT subject to retail sales tax. **Taxable services include:**
- Construction/repair services (labor on real/personal property)
- Landscaping, janitorial services
- Physical fitness services
- Digital automated services
- Extended warranties/service contracts

**Source:** RCW 82.04.050 (definition of retail sale).

### E-2: Digital products and services

Washington taxes digital goods (e-books, music, movies, apps) and digital automated services (SaaS). This is a significant difference from many states. **Source:** RCW 82.04.192; RCW 82.04.050(6).

- Digital goods: taxed at the buyer's location rate.
- Digital automated services (SaaS): taxed at the buyer's location rate.
- Custom software: exempt from retail sales tax.

### E-3: Food

- Prepared food (restaurants, heated food, food with utensils): taxable.
- Grocery food (unprepared food for home consumption): exempt.
- Dietary supplements: taxable.
- Soft drinks: taxable.

**Source:** RCW 82.08.0293.

### E-4: Reseller permit

A buyer making purchases for resale must present a valid reseller permit (not the old resale certificate, which was retired in 2010). The seller must verify the permit using the DOR's online lookup tool. **Source:** RCW 82.04.060.

### E-5: Manufacturing machinery and equipment

Machinery and equipment used directly in a manufacturing operation is exempt from sales tax. This is a significant exemption for manufacturers. **Source:** RCW 82.08.02565.

### E-6: Interstate sales

Sales of goods shipped to buyers outside Washington are generally exempt from Washington retail sales tax if the seller ships via common carrier. The seller must retain documentation of out-of-state delivery. **Source:** RCW 82.08.0273.

### E-7: Marketplace facilitators

As of January 1, 2020, marketplace facilitators (Amazon, Etsy, etc.) must collect and remit Washington sales tax on behalf of marketplace sellers. If a marketplace facilitator collects the tax, the seller does NOT need to collect it again. **Source:** RCW 82.08.0531.

---

## Section 6 -- Test suite

### Test 1: In-store retail sale in Seattle

- **Input:** Sale of $500 of tangible goods, buyer picks up in Seattle. Combined rate: 10.10%.
- **Expected:** Tax: $500 x 10.10% = $50.50.

### Test 2: Shipped sale (destination-based)

- **Input:** Seller in Seattle ships $1,000 of goods to buyer in Spokane. Spokane combined rate: 8.90%.
- **Expected:** Tax: $1,000 x 8.90% = $89.00 (Spokane rate, not Seattle rate).

### Test 3: Digital product sale

- **Input:** Sale of $200 SaaS subscription to a Bellevue customer. Combined rate: 10.10%.
- **Expected:** Taxable as digital automated service. Tax: $200 x 10.10% = $20.20.

### Test 4: Professional service (not taxable)

- **Input:** $5,000 consulting engagement for a Seattle client.
- **Expected:** Professional consulting is NOT subject to retail sales tax. Tax: $0. (Note: B&O tax still applies.)

### Test 5: Use tax

- **Input:** Business in Tacoma purchases $2,000 of office furniture from Oregon vendor, no tax collected. Tacoma combined rate: 10.30%.
- **Expected:** Use tax: $2,000 x 10.30% = $206.00.

---

## Section 7 -- Prohibitions

- **P-1:** Do NOT use origin-based sourcing. Washington is destination-based.
- **P-2:** Do NOT assume all services are taxable. Most professional services are exempt from retail sales tax.
- **P-3:** Do NOT accept the old resale certificate form. Only valid reseller permits are accepted (since 2010).
- **P-4:** Do NOT tax grocery food. Only prepared food is taxable.
- **P-5:** Do NOT ignore digital goods and SaaS. Washington taxes them.
- **P-6:** Do NOT use a flat rate for all locations. Rates vary by destination address and change quarterly.

---

## Section 8 -- Self-checks

Before delivering output, verify:

- [ ] Destination-based sourcing applied (rate based on buyer's location)
- [ ] Correct combined rate looked up per delivery address via DOR tool
- [ ] Services correctly classified (most professional services exempt)
- [ ] Digital goods/SaaS taxed at buyer's location rate
- [ ] Grocery food exempt; prepared food taxable
- [ ] Reseller permits verified (not old resale certificates)
- [ ] Use tax reported for out-of-state purchases
- [ ] Location codes correctly assigned for each jurisdiction
- [ ] Sales shipped out of state properly excluded

---

## Section 9 -- Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
