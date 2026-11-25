---
name: fl-sales-use-tax
description: "Florida Sales and Use Tax return (Form DR-15) for self-employed individuals and small businesses. Covers the 6% state sales tax rate, county discretionary sales surtax, use tax on out-of-state purchases, exempt transactions, filing frequencies, and dealer collection allowance. Primary source: Florida Statutes Chapter 212."
jurisdiction: US-FL
tax_year: 2025
last_updated: 2026-11-25
version: "1.1"
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
reviewed_by: "Rob Hoffman"
reviewed_on: 2026-11-03
tier: 1
domain: income-tax
---

# FL Sales Use Tax

## Florida Sales and Use Tax (DR-15) v1.1

## What this file is

**Obligation category:** CT (Consumption Tax)
**Functional role:** Return preparation
**Status:** Correction draft for 2025; independent changed-line source review and accountant approval pending. Retained approval metadata does not certify this version. Explicit non-usable holds are not filing/tax positions.

This is a Tier 2 content skill that loads on top of `us-tax-workflow-base`. It covers the preparation of Form DR-15 (Sales and Use Tax Return) for Florida-registered dealers who are sole proprietors or single-member LLCs.

**Tax year coverage.** This skill targets **tax year 2025** (returns filed monthly, quarterly, semiannually, or annually depending on tax liability).

## Section 1 -- Scope statement

**In scope:**

- Form DR-15 (Sales and Use Tax Return)
- Form DR-15EZ (simplified return for dealers with no surtax obligation)
- Sole proprietors and single-member LLCs registered as Florida dealers
- Taxable sales of tangible personal property
- Taxable services (commercial pest control, detective/security, nonresidential cleaning; interior-design contracts require separate goods/fee classification)
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

## Section 2 -- Filing requirements

### Who must register

**Non-usable hold:** The ordinary application-fee assertion is unverified; the statutory failure-to-register charge is a different amount.

- **Dealer registration requirement** — Any person who makes or intends to make taxable sales or charges admission in Florida must register as a dealer with the Florida Department of Revenue (FDOR). Registration is free.  _(§212.18, F.S.)_

### Filing frequency

**Filing frequency**  _(FDOR Rule 12A-1.056, F.A.C.)_

| Tax remitted for preceding four calendar quarters | Ordinary assigned filing frequency | Source |
| --- | --- | --- |
| $100 or less | Annual | [DOR overview](https://floridarevenue.com/taxes/taxesfees/Pages/sales_tax.aspx); [212.11](https://www.flsenate.gov/Laws/Statutes/2025/212.11) |
| $101–$500 | Semiannual | [DOR overview](https://floridarevenue.com/taxes/taxesfees/Pages/sales_tax.aspx) |
| $501–$1,000 | Quarterly | [DOR overview](https://floridarevenue.com/taxes/taxesfees/Pages/sales_tax.aspx) |
| More than $1,000 | Monthly ordinarily; statute permits quarterly returns with monthly payment for more than $1,000–$12,000 and other assigned exceptions | [212.11](https://www.flsenate.gov/Laws/Statutes/2025/212.11) |

- **Due date** — The 1st through the 20th of the month following the reporting period. If the 20th falls on a Saturday, Sunday, or state/federal holiday, the due date is the next business day.  _(FDOR Rule 12A-1.056, F.A.C.)_
- **Electronic filing/payment requirement**: $5,000 or more paid during the preceding state fiscal year triggers the next calendar-year requirement, with location aggregation, consolidated filing and applicable waivers. [Source](https://www.flsenate.gov/Laws/Statutes/2025/213.755).

## Section 3 -- Rates and thresholds

**Electronic payment cutoff:** initiate payment and obtain confirmation by 5 p.m. Eastern on the business day preceding the due date; timely return filing alone does not establish timely payment. [Source](https://floridarevenue.com/Forms_library/current/dr15.pdf).

### State sales tax rate

**State sales tax rate**  _(§212.05, F.S.; §212.06, F.S.)_

| Item | Rate | Source |
| --- | --- | --- |
| State sales tax | 6.0% | §212.05, F.S. |
| State use tax | 6.0% | §212.06, F.S. |

### Discretionary sales surtax (selected counties, 2025)

- **Surtax base** — The first-$5,000 limitation applies to qualifying tangible property per item, with bulk/working-unit and boat-trailer aggregation and the prepaid-calling exception. It is not a universal transaction cap on services, admissions or rentals. [Source](https://www.flsenate.gov/Laws/Statutes/2025/212.054).  _(§212.055, F.S.)_

**Discretionary sales surtax (selected counties, 2025)**  _(FDOR Form DR-15DSS (2025))_

| County | Surtax rate | Combined rate | Source |
| --- | --- | --- | --- |
| Miami-Dade | 1.0% | 7.0% | FDOR Form DR-15DSS (2025) |
| Broward | 1.0% | 7.0% | FDOR Form DR-15DSS (2025) |
| Hillsborough (Tampa), January–May 2025 | 0.5% | 6.5% ordinary | [TIP 24A01-15](https://floridarevenue.com/taxes/tips/Documents/TIP_24A01-15.pdf) |
| Hillsborough (Tampa), June–December 2025 | 1.5% | 7.5% ordinary | [TIP 25A01-02](https://floridarevenue.com/taxes/tips/Documents/TIP_25A01-02.pdf) |
| Orange (Orlando) | 0.5% | 6.5% | FDOR Form DR-15DSS (2025) |
| Duval (Jacksonville) | 1.5% | 7.5% | FDOR Form DR-15DSS (2025) |
| Palm Beach | 1.0% | 7.0% | FDOR Form DR-15DSS (2025) |
| Alachua (Gainesville) | 1.5% | 7.5% | [2025 DR-15DSS](https://floridarevenue.com/Forms_library/current/dr15dss_25.pdf) |

- **Surtax rate lookup** — The surtax rate is determined by the county where the goods are delivered or services performed. The dealer must look up the current rate on Form DR-15DSS for each county. Rates change periodically.  _(FDOR Form DR-15DSS (2025))_

### Collection allowance (vendor discount)

**Collection allowance (vendor discount)**  _(§212.12(1), F.S.)_

| Item | Amount | Source |
| --- | --- | --- |
| Collection allowance | 2.5% of first $1,200 in tax due; maximum $30 per reporting location/period, subject to eligibility | [212.12(1)](https://www.flsenate.gov/Laws/Statutes/2025/212.12); [DR-15](https://floridarevenue.com/Forms_library/current/dr15.pdf); [DOR filing tips](https://floridarevenue.com/taxes/taxesfees/Pages/sales_tax.aspx) |

- **Collection allowance application** — The collection allowance is a compensation to the dealer for collecting and remitting sales tax. It is deducted on line 11. Return and payment must both be timely and electronic; incomplete returns can also lose allowance. Do not multiply the $30 maximum automatically by months in a reporting period. [Source](https://floridarevenue.com/Forms_library/current/dr15.pdf). [Source](https://www.flsenate.gov/Laws/Statutes/2025/212.12).  _(§212.12(1), F.S.)_

### Rounding tax on partial dollars

- **Rounding rule**: rounding replaced brackets from July 1, 2021. Compute through the third decimal; round the cent up when the third decimal exceeds four. [Section 212.12(10)](https://www.flsenate.gov/Laws/Statutes/2025/212.12).

## Section 4 -- Computation rules (Step format)

### Step 1: Classify all transactions

- **Transaction classification** — For each sale during the reporting period, determine: 1. **Taxable or exempt?** See Section 5 for exemptions. 2. **Location of delivery.** Determines which county surtax applies. 3. **Item/category facts.** Apply the qualifying tangible-property cap and aggregation/exception rules; do not cap every transaction. [Source](https://www.flsenate.gov/Laws/Statutes/2025/212.054).  _(Section 5)_

### Step 2: Compute gross sales (column 1)

Use column 1 within the applicable lettered category A–E; these are columns, not numbered lines 1–3. [2025 DR-15](https://floridarevenue.com/Forms_library/current/dr15.pdf).

### Step 3: Compute exempt sales (column 2)

Enter category exemptions in column 2 with operative support; do not infer the broad held exemptions below.

### Step 4: Compute taxable amount (column 3)

Column 1 minus column 2 within the relevant category gives column 3.

### Step 5: Compute tax (column 4)

Apply the relevant state rate and applicable surtax in column 4 for each category. Column 4 is not state-only numbered line 4; avoid adding surtax twice. [2025 DR-15](https://floridarevenue.com/Forms_library/current/dr15.pdf).

### Step 6: Summarize surtax and total tax

Apply category/item cap and county/date conditions. Surtax is already in column 4; report its summary at 15(d), not a separate tax add-on on line 5. Line 5 totals column 4. [2025 DR-15](https://floridarevenue.com/Forms_library/current/dr15.pdf).

### Step 7: Report taxable purchases (row B)

Taxable purchases on which the seller did not collect the relevant Florida tax belong in row B. Establish taxable use/base and applicable credits/exemptions first. Line 6 is lawful deductions, not use tax. [2025 DR-15](https://floridarevenue.com/Forms_library/current/dr15.pdf).

### Step 8: Compute net tax (line 7)

Line 5 totals tax; line 6 contains qualifying lawful deductions, including supported dealer refunds for returned merchandise. Line 7 is line 5 minus line 6. [2025 DR-15](https://floridarevenue.com/Forms_library/current/dr15.pdf); [bounded DR-15N passages](https://floridarevenue.com/Forms_library/current/dr15n.pdf).

### Step 9: Apply estimates/credit memos and allowance in their correct fields

Line 8 is estimated tax paid and DOR-issued credit memos; line 9 **adds** estimated tax due for the current month. Collection allowance is line 11, not line 9. Its cap is $30 per location/period with electronic/timely return and payment and complete-return conditions. Actual estimate gateway, liability history and credits remain held. [2025 DR-15](https://floridarevenue.com/Forms_library/current/dr15.pdf); [DR-15N](https://floridarevenue.com/Forms_library/current/dr15n.pdf); [212.12](https://www.flsenate.gov/Laws/Statutes/2025/212.12).

### Step 10: Compute amount due (lines 10–14)

Line 10 = line 7 − line 8 + line 9. Deduct eligible allowance on line 11 and add penalty/interest on lines 12–13 to obtain line 14. Do not subtract the current estimate. [2025 DR-15](https://floridarevenue.com/Forms_library/current/dr15.pdf).

### Step 11: Apply penalty and interest if late

**Penalty and interest table**: penalty authority is section 212.12; section 213.235 governs interest.

| Item | Rate | Source |
| --- | --- | --- |
| Ordinary late filing/payment | 10% of tax due, minimum $50, subject to exceptions/relief | [212.12(2)(a)](https://www.flsenate.gov/Laws/Statutes/2025/212.12); [DR-15](https://floridarevenue.com/Forms_library/current/dr15.pdf) |
| Undisclosed tax | Separate monthly escalation under 212.12(2)(b), up to 50%; do not apply automatically to properly disclosed late-paid tax | [212.12](https://www.flsenate.gov/Laws/Statutes/2025/212.12) |
| Interest | Floating January/July adjustment; actual 2025 daily factors and dates required | [213.235](https://www.flsenate.gov/Laws/Statutes/2025/213.235); [DOR rates](https://floridarevenue.com/taxes/taxesfees/Pages/tax_interest_rates.aspx) |
| Zero-tax late return | $50 minimum subject to applicable exceptions/relief | [DR-15](https://floridarevenue.com/Forms_library/current/dr15.pdf); [212.12](https://www.flsenate.gov/Laws/Statutes/2025/212.12) |

## Section 5 -- Edge cases and special rules

### E-1: Common exemptions

- **Groceries exemption** — Groceries (unprepared food for home consumption) -- exempt.  _(§212.08(1), F.S.)_
- **Prescription drugs and medical supplies exemption** — Apply the prescription, listed-product and defined-category branches of section 212.08(2). Not every medical supply is exempt. [Source](https://www.flsenate.gov/Laws/Statutes/2025/212.08).  _(§212.08(2), F.S.)_
- **Resale exemption** — Items purchased for resale (with valid DR-13 resale certificate) -- exempt.  _(§212.07(1), F.S.)_
**Non-usable hold:** Full eligibility/certificate authority is unverified.

- **Agricultural inputs exemption** — Agricultural inputs (feed, seed, fertilizer with DR-14A certificate) -- exempt.
**Non-usable hold:** Specific materials, use and operative exemption are unverified.

- **Packaging materials exemption** — Certain packaging materials used to package tangible personal property for sale.

### E-2: Services generally not taxable

**Non-usable hold:** The exhaustive current service classification and exceptions are not established; the design-specific correction does not clear all services.

- **Taxable services enumeration** — Most services in Florida are NOT subject to sales tax. Only specifically enumerated services are taxable: nonresidential pest control, burglar protection/detective services, nonresidential building cleaning, with interior-design consultation and goods-related fees classified separately. TAA 02A-031 distinguishes design-only consultation without goods sales from charges connected to taxable goods; actual contract and current-rule conditions remain necessary. [Source](https://floridarevenue.com/TaxLaw/Documents/TAA%2002A-031.pdf).  _(§212.05(1), F.S.)_

### E-3: Software and digital goods

- **Canned software on tangible media** — Canned (prewritten) software delivered on tangible media: taxable.
- **Electronic and custom software**: the fact-specific TAA 09A-001 and 10A-028 rulings contradict blanket taxability for standalone electronic-only software. Custom software bundled into taxable hardware/software sales may be taxable total consideration; customization alone is not universal exemption. Do not decide every SaaS product without its actual delivery/bundle facts. [TAA 09A-001](https://floridarevenue.com/TaxLaw/Documents/TAA%2009A-001.pdf); [TAA 10A-028](https://floridarevenue.com/TaxLaw/Documents/10A-028.pdf). TAA 14A-032 concerns residential fuel for an RV-park laundry, not software; it is the wrong authority.
**Non-usable hold:** Download/streaming/bundle and communications-tax classification has not been established.

- **Digital books, music, movies** — Digital books, music, movies: Florida does NOT tax these as of 2025.

### E-4: Surtax cap on single transactions

- **Surtax cap per item** — For qualifying tangible property the $5,000 cap applies per item, subject to bulk/working-unit, boat-trailer and prepaid-calling rules; it is not a cap for every category. [Source](https://www.flsenate.gov/Laws/Statutes/2025/212.054). If a customer buys 10 items at $2,000 each in one transaction, the surtax applies to the first $5,000 of EACH item, not the transaction total.  _(§212.054, F.S.)_

### E-5: Commercial rent

- **Commercial real property rent rate**: ordinary commercial rent had 2% state tax plus applicable surtax for occupancy periods through September 2025. Both were repealed for occupancy periods beginning October 1, 2025. Late payment for a taxable earlier period remains taxable. The surviving categories listed in the notice retain their separate treatment; do not infer all rentals are repealed. [TIP 25A01-04](https://floridarevenue.com/taxes/tips/Documents/TIP_25A01-04.pdf).

### E-6: Zero returns

- **Zero return filing requirement** — Dealers with no taxable activity during a reporting period must still file a return showing zero tax due. Failure to file zero returns results in delinquency notices and potential revocation of the dealer's registration.

## Section 6 -- Test suite

### Test 1: Basic monthly return

**Input:** Sole proprietor, Broward County. Gross sales: $15,000. All taxable, all delivered in Broward. No exempt sales.
**Expected:** State tax: $15,000 x 6% = $900. Surtax: $15,000 x 1% = $150 (all items under $5,000). Gross tax: $1,050. Eligible electronic/timely/complete return and payment: $1,050 × 2.5% = $26.25, below the $30 cap; net $1,023.75 before other adjustments. If allowance conditions fail, $1,050 is due before other adjustments, not $1,025.

### Test 2: Mixed county sales

**Input:** Sales of $8,000 delivered in Orange County (0.5% surtax) and $4,000 delivered in Miami-Dade (1.0% surtax).
**Expected:** State tax: $12,000 x 6% = $720. Surtax: ($8,000 x 0.5%) + ($4,000 x 1.0%) = $40 + $40 = $80. Gross tax: $800 if the $8,000 Orange aggregate is not one capped item. **Non-usable hold:** item sizes are absent; one qualifying $8,000 item would give $25 + $40 = $65 surtax, and $785 total. Preserve the original totals as conditional arithmetic, not a cleared return.

### Test 3: Transaction exceeding $5,000 surtax cap

**Input:** Single sale of $10,000 in Hillsborough County (1.5% surtax).
**Expected:** State tax: $10,000 x 6% = $600. Surtax: $5,000 x 1.5% = $75 (capped at first $5,000). Gross tax: $675 for a qualifying item from June 2025. For January–May the 0.5% Hillsborough surtax gives $25 and $625 total. **Non-usable hold:** sale date and qualifying-item nature are unstated.

### Test 4: Late filing

**Input:** Monthly return, 15 days late. Tax due: $500.
**Expected:** Penalty: $500 x 10% = $50. Collection allowance: forfeited. Total due: $550 plus interest.

### Test 5: Use tax on out-of-state purchase

**Input:** Business purchased $2,000 of office equipment from an out-of-state vendor that did not collect FL tax. Business located in Palm Beach County (1.0% surtax).
**Non-usable hold:** Taxable-use, credit and exemption facts are absent; this is stipulated arithmetic only.

**Expected:** Use tax: $2,000 x 7% = $140.

```oa-check
name: Original Broward return; allowance conditions assumed met
inputs:
  sales: 15000
steps:
  state_tax: sales * 0.06
  surtax: sales * 0.01
  gross_tax: state_tax + surtax
  eligible_allowance: min(gross_tax, 1200) * 0.025
  net: gross_tax - eligible_allowance
expected:
  gross_tax: 1050
  eligible_allowance: 26.25
  net: 1023.75
```

```oa-check
name: Original mixed-county sales; item sizes unresolved
inputs:
  orange_sales: 8000
  miami_sales: 4000
steps:
  state_tax: (orange_sales + miami_sales) * 0.06
  uncapped_surtax: orange_sales * 0.005 + miami_sales * 0.01
  conditional_uncapped_total: state_tax + uncapped_surtax
  one_orange_item_surtax: min(orange_sales, 5000) * 0.005 + miami_sales * 0.01
  conditional_capped_total: state_tax + one_orange_item_surtax
expected:
  conditional_uncapped_total: 800
  conditional_capped_total: 785
```

```oa-check
name: Original Hillsborough item; date and category unresolved
inputs:
  sale: 10000
steps:
  state_tax: sale * 0.06
  jan_may_surtax: min(sale, 5000) * 0.005
  june_onward_surtax: min(sale, 5000) * 0.015
  jan_may_total: state_tax + jan_may_surtax
  june_onward_total: state_tax + june_onward_surtax
expected:
  jan_may_total: 625
  june_onward_total: 675
```

```oa-check
name: Original 15-day-late return; interest unresolved
inputs:
  tax_due: 500
steps:
  penalty: max(tax_due * 0.10, 50)
  before_interest: tax_due + penalty
expected:
  penalty: 50
  before_interest: 550
```

```oa-check
name: Original Palm Beach stipulated use-tax base before credits
inputs:
  purchase: 2000
steps:
  ordinary_tax_before_credits: purchase * 0.07
expected:
  ordinary_tax_before_credits: 140
```

## Section 7 -- Prohibitions

- **P-1:** Do NOT accept a resale certificate (DR-13) without verifying it is properly completed and the buyer is a registered dealer.
- **P-2:** Apply the $5,000 cap only to the qualifying tangible-property/item categories and aggregation rules; never cap all services, rentals or admissions.
- **P-3:** Claim allowance only for an eligible complete return and timely electronic return/payment; cap $30 per location/period.
- **P-4:** Apply the occupancy-period commercial-rent rule: ordinary 2% plus surtax through September 2025, repeal from October subject to surviving categories and prior-period payments.
- **P-5:** Do not classify all electronic software as taxable or all custom software as exempt; determine tangible delivery, goods bundles and actual contract facts.
**Non-usable hold:** The categorical digital-goods no-tax proposition is unverified.

- **P-6:** Do NOT assume digital goods are taxable in Florida. As of 2025, they generally are not.

## Section 8 -- Self-checks

Before delivering output, verify:

- [ ] All transactions classified as taxable or exempt with statutory basis
- [ ] Correct surtax rate applied for each delivery county (verified against current DR-15DSS)
- [ ] Surtax item/category/aggregation conditions applied; no universal transaction cap
- [ ] Allowance on line 11 is eligible, complete and timely/electronic for return and payment, maximum $30 per location/period
- [ ] Use tax included for out-of-state purchases where no FL tax was collected
- [ ] Assigned filing frequency matches tax remitted for preceding four quarters and applicable statutory exceptions
- [ ] Zero return filed if no activity (not skipped)
- [ ] Commercial rent uses the actual 2025 occupancy period, repeal and surviving-category rules
- [ ] Reviewer brief includes any classification uncertainties

## Section 9 -- Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.


## Sources

Bounded primary-source reads completed 2026-11-22 and reused for these 2025 corrections. The DR-15N revision effective December 2025 is distinguished from the actual earlier 2025 DR-15 form. Fact-specific rulings are not universal product classifications.

| Authority | Actual read scope and short exact wording | Read on |
| --- | --- | --- |
| [2025 Form DR-15 (R.01/25, effective02/25)](https://floridarevenue.com/Forms_library/current/dr15.pdf) | Read in the linked authority (bounded scope): Both extracted pages read: form labels, reverse surtax schedule, allowance, deadlines and penalty. Uppercase/www variants failed; this lowercase URL succeeded. Short exact excerpt: “11. Less Collection Allowance”. | 2026-11-22 |
| [DOR sales/use tax overview](https://floridarevenue.com/taxes/taxesfees/Pages/sales_tax.aspx) | Read in the linked authority (bounded scope): General rate, use tax, registration, surtax, rounding, allowance and frequency passages read, including substantive indexed official text; not an exhaustive exemption/service review. Short exact excerpt: “More than $1,000”. | 2026-11-22 |
| [DOR sales/use tax overview, bounded follow-up](https://floridarevenue.com/taxes/taxesfees/Pages/sales_tax.aspx) | Actual operative Rounding and Tips for Filing paragraphs read; “not to exceed $30 for each reporting location” and “Effective July 1, 2021”. Both are present in the linked authority; no new consolidation method or whole-page clearance claimed. | 2026-11-25 |
| [DR-15N R.10/25, effective12/25](https://floridarevenue.com/Forms_library/current/dr15n.pdf) | Read in the linked authority (bounded scope): Cover/form and bounded passages on deadlines, electronic filing, lawful deductions and estimated tax read. Not all eight pages. Revision effective December 2025 distinguished from the earlier S1 form. Short exact excerpt: “Line 9. Plus Estimated Tax Due Current Month”. | 2026-11-22 |
| [2025 F.S.212.11](https://www.flsenate.gov/Laws/Statutes/2025/212.11) | Read in the linked authority (bounded scope): Subsection 1 filing/payment, frequency, nonrecurring activity and alternate-period permissions read; not the full section. Short exact excerpt: “preceding four calendar quarters”. | 2026-11-22 |
| [2025 F.S.212.054](https://www.flsenate.gov/Laws/Statutes/2025/212.054) | Read in the linked authority (bounded scope): Subsections 1–2 cap, bulk/working-unit aggregation and delivery passages read; not all special sourcing branches. Short exact excerpt: “any item of tangible personal property”. | 2026-11-22 |
| [2025 DR-15DSS](https://floridarevenue.com/Forms_library/current/dr15dss_25.pdf) | Read in the linked authority (bounded scope): Seven selected county rows and the Hillsborough suspension callout read; printed rate reconciled with S7/S8. Short exact excerpt: “Alachua 1.5%”. | 2026-11-22 |
| [TIP24A01-15](https://floridarevenue.com/taxes/tips/Documents/TIP_24A01-15.pdf) | Read in the linked authority (bounded scope): Suspension date, remaining school component and requirement for later resumption notice read. Short exact excerpt: “Beginning January 1, 2025”. | 2026-11-22 |
| [TIP25A01-02](https://floridarevenue.com/taxes/tips/Documents/TIP_25A01-02.pdf) | Read in the linked authority (bounded scope): Resumption date, component rates and suspension ending May 31 read. The notice's 213.031 reference is a typo; commercial rent authority is 212.031. Short exact excerpt: “Beginning June 1, 2025”. | 2026-11-22 |
| [2025 F.S.213.755](https://www.flsenate.gov/Laws/Statutes/2025/213.755) | Read in the linked authority (bounded scope): Threshold, location aggregation, consolidated filers and waiver passages read. Short exact excerpt: “greater than or equal to $5,000”. | 2026-11-22 |
| [2025 F.S.212.18](https://www.flsenate.gov/Laws/Statutes/2025/212.18) | Read in the linked authority (bounded scope): Registration, location, cancellation and failure-to-register fee passages read; ordinary fee not established. Short exact excerpt: “for each place of business”. | 2026-11-22 |
| [2025 F.S.212.06](https://www.flsenate.gov/Laws/Statutes/2025/212.06) | Read in the linked authority (bounded scope): Opening subsection 1 taxable-use/cost rules read; full valuation, credit and dealer rules not read. Short exact excerpt: “6 percent of the cost price”. | 2026-11-22 |
| [2025 F.S.212.12](https://www.flsenate.gov/Laws/Statutes/2025/212.12) | Read in the linked authority (bounded scope): Allowance subsection 1, ordinary late filing/payment versus nondisclosure in 2(a)/(b), and rounding in 10 read; no full penalty clearance. Short exact excerpt: “only by electronic means”. | 2026-11-22 |
| [2025 F.S.213.235](https://www.flsenate.gov/Laws/Statutes/2025/213.235) | Read in the linked authority (bounded scope): Operative subsections 1–5 interest adjustment read; this is interest authority, not ordinary late-filing penalty authority. Short exact excerpt: “On July 1 of the same calendar year”. | 2026-11-22 |
| [DOR tax/interest rates](https://floridarevenue.com/taxes/taxesfees/Pages/tax_interest_rates.aspx) | Read in the linked authority (bounded scope): Twice-yearly interest and current 2026 rate passages read; historical 2025 daily-factor notices not read. Short exact excerpt: “updated twice a year”. | 2026-11-22 |
| [2025 F.S.212.08](https://www.flsenate.gov/Laws/Statutes/2025/212.08) | Read in the linked authority (bounded scope): Groceries subsection 1 and medical subsection 2 passages read; not the entire large exemption section. Agriculture and packaging remain held. Short exact excerpt: “according to an individual prescription”. | 2026-11-22 |
| [2025 F.S.212.07](https://www.flsenate.gov/Laws/Statutes/2025/212.07) | Read in the linked authority (bounded scope): Subsection 1(b) resale documentation, authorization alternatives and recurring customers read. Short exact excerpt: “In lieu of maintaining a copy”. | 2026-11-22 |
| [TAA02A-031](https://floridarevenue.com/TaxLaw/Documents/TAA%2002A-031.pdf) | Read in the linked authority (bounded scope): Summary and initial contract facts read; not all twelve pages or the full current interior-design rule. Fact-specific ruling. Short exact excerpt: “when no sale of tangible personal property occurs”. | 2026-11-22 |
| [TAA09A-001](https://floridarevenue.com/TaxLaw/Documents/TAA%2009A-001.pdf) | Read in the linked authority (bounded scope): Substantive software discussion and conclusion on pages 4–6 read, including physical delivery, electronic-only sales, custom software and bundles. Fact-specific ruling. Short exact excerpt: “software, canned or customized, electronically downloaded”. | 2026-11-22 |
| [TAA10A-028](https://floridarevenue.com/TaxLaw/Documents/10A-028.pdf) | Read in the linked authority (bounded scope): Summary and initial facts read; corroborates electronic-only standalone software, without clearing every SaaS product. Short exact excerpt: “not part of the sale of tangible personal property”. | 2026-11-22 |
| [Named TAA14A-032](https://floridarevenue.com/TaxLaw/Documents/14A-032.pdf) | Read in the linked authority (bounded scope): Question, answer, facts and residential-fuel analysis read; wrong subject for software citation. Short exact excerpt: “Residential Exemption on Fuels”. | 2026-11-22 |
| [TIP25A01-04](https://floridarevenue.com/taxes/tips/Documents/TIP_25A01-04.pdf) | Read in the linked authority (bounded scope): Repeal, occupancy dates, old 2% rate, delayed payments, excluded categories and initial reporting Q&A read; not every refund procedure. Short exact excerpt: “rental or occupancy periods beginning on or after October 1, 2025”. | 2026-11-22 |

Not yet confirmed; non-usable holds: ordinary registration fee; actual assigned reporting dates, relief and electronic-payment calendar; taxable-use/base and other-state credit/exemption facts; special county sourcing; actual estimate gateway/liability history and credit records; exact historical interest periods/daily factors; agricultural certificate and packaging exemptions; exhaustive current service classifications/exceptions; digital download/streaming/bundle/communications-tax treatment; and item/date facts and complete tax outcomes in the original mixed-county, Hillsborough and Palm Beach examples. No actual return, remittance or client liability is cleared. Independent changed-line source review and accountant approval of this changed version remain pending.
