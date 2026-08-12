---
name: de-gross-receipts-tax
description: "Delaware Gross Receipts Tax for sole proprietors and self-employed individuals. Covers tax rates by business activity category, monthly/quarterly exclusions, filing frequency, and compliance requirements. Delaware has no sales tax but imposes this tax on gross business revenues. Trigger: any person or entity conducting business in Delaware."
version: "0.1"
jurisdiction: US-DE
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# DE Gross Receipts Tax

## Delaware Gross Receipts Tax Skill — Self-Employed / Sole Proprietor

> **Scope.** This skill covers the Delaware Gross Receipts Tax (GRT) for self-employed individuals and sole proprietors doing business in Delaware. Delaware has no general sales tax; the GRT serves as the state's primary transaction-level tax, levied on the seller rather than the buyer.
> **Quality tier.** Q3 — AI-drafted with citations. Must be reviewed by a qualified professional before use.

## Section 1: Metadata

**Metadata table**

| Field | Value |
| --- | --- |
| Jurisdiction | US-DE (Delaware) |
| Tax authority | Delaware Division of Revenue — Gross Receipts Tax Section |
| Filing portal | [Delaware One Stop](https://onestop.delaware.gov/) |
| Legislation citation | 30 Del. C. Chapter 23 (Occupational and Business License Tax) |
| Primary form | Gross Receipts Tax coupon (issued by Division of Revenue based on business type) |
| Filing frequency | Monthly, quarterly, or annually depending on liability |
| Contact | (302) 577-8780 or grt@delaware.gov |
| Version | 0.1 |
| Generated date | May 22, 2026 |
| Validation status | AI-drafted — Q3 |

### Sources consulted

- Delaware Division of Revenue — Gross Receipts Tax FAQ: https://revenue.delaware.gov/gross-receipts-tax/
- Delaware Division of Revenue — Step 4: Learn About Gross Receipts Taxes: https://revenue.delaware.gov/business-tax-forms/doing-business-in-delaware/step-4-gross-receipts-taxes/
- Delaware Finance Department — Business and Occupational License and Gross Receipts Tax: https://financefiles.delaware.gov/docs/bus_occup_lic.pdf
- HandsOff Sales Tax — Delaware Gross Receipts Tax Guide: https://handsoffsalestax.com/de-gross-receipts-tax/

## Section 2: Quick reference — rates and exclusions by business category

**Placeholder for parent heading — content in subsection**

### Common GRT rates (effective for periods beginning after 12/31/2013)

**Common GRT rates**  _(Source: Delaware Division of Revenue official Tax Tips; 30 Del. C. Chapter 23.)_

| Business category | Tax rate | Monthly exclusion |
| --- | --- | --- |
| Retailers (tangible goods) | 0.7543% | $100,000 |
| Wholesalers | 0.3983% | $100,000 |
| Manufacturers | 0.1260% | $1,250,000 |
| General services (professional, occupational) | 0.3983% | $100,000 |
| Contractors | 0.6472% | $100,000 |
| Food processors | 0.2291% | $100,000 |
| Commercial feed dealers | 0.0945% | $100,000 |
| Lessors of real property | 0.3983% | $100,000 |
| Motor vehicle lessors | 1.9914% | $100,000 |
| Restaurants | 0.7543% | $100,000 |
| Petroleum products | Variable (up to 2.4218%) | Varies |

**Important:** Rates and exclusions vary by specific business activity. The above are the most common categories. Sole proprietors must identify their primary business activity and register for the correct category. If a business conducts multiple activities, separate licenses and filings are required for each.

### How the exclusion works

- The monthly exclusion reduces the taxable base before applying the rate
- Example: A general services sole proprietor with $150,000 gross receipts in a month pays tax on $50,000 ($150,000 − $100,000 exclusion) × 0.3983% = $199.15
- Quarterly filers get 3× the monthly exclusion ($300,000 for most categories)

## Section 3: Who must register and file

### Registration requirement

- **Registration requirement** — Any person or entity engaged in business in Delaware must obtain a business license from the Delaware Division of Revenue before commencing operations. This includes: Sole proprietors, Corporations, Partnerships, LLCs, Independent contractors providing services in Delaware

### What constitutes "gross receipts"

- **Gross receipts definition** — Total receipts from goods sold and services rendered in Delaware. No deductions allowed for: Cost of goods sold, Labor costs, Interest expense, Discounts paid, Delivery costs, State or federal taxes paid, Any other business expenses

### Exemptions

- **GRT exemptions** — The following are NOT subject to GRT: Casual sales (isolated transactions not in the ordinary course of business), Sales to the U.S. government, Sales to the State of Delaware, Insurance premiums (taxed separately), Certain agricultural products sold by the producer

## Section 4: Filing frequency and due dates

**Filing frequency and due dates**

| Filing frequency | Threshold | Due date |
| --- | --- | --- |
| Monthly | Tax liability > $5,000/month | 20th of the following month |
| Quarterly | Tax liability $1,500–$5,000/quarter | Last day of month following quarter end |
| Annually | Tax liability < $1,500/quarter | January 31 of following year |

New businesses typically start on a quarterly filing schedule. The Division of Revenue uses a "look-back period" to determine frequency changes.

### Quarterly due dates (calendar year)

**Quarterly due dates (calendar year)**

| Quarter | Period | Due date |
| --- | --- | --- |
| Q1 | January – March | April 30 |
| Q2 | April – June | July 31 |
| Q3 | July – September | October 31 |
| Q4 | October – December | January 31 |

## Section 5: Self-employed specific considerations

### Multiple business activities

- **Multiple business activities** — If a sole proprietor performs both retail sales and professional services, separate GRT licenses and filings are required for each activity at the respective rate.

### Online/remote sellers

- **Online/remote sellers** — If you sell tangible goods to Delaware customers from outside Delaware, you may be subject to GRT based on nexus rules. Physical presence in Delaware triggers GRT; economic nexus rules may also apply.

### Interaction with income tax

- **Interaction with income tax** — GRT paid is a deductible business expense on federal Schedule C (and therefore reduces Delaware taxable income). It is NOT a pass-through tax to the customer (unlike sales tax), though some businesses choose to include it in pricing.

### Record-keeping

- **Record-keeping** — Maintain monthly gross receipts records by business activity category. The Division of Revenue may audit and reclassify business activity if the registered category does not match actual operations.

## Section 6: Tier 1 rules — deterministic

- **DE-GRT-1.01** — GRT is levied on the seller/provider, not the buyer/customer
- **DE-GRT-1.02** — Tax base = total gross receipts minus monthly/quarterly exclusion
- **DE-GRT-1.03** — No deductions from gross receipts for COGS, expenses, or other costs
- **DE-GRT-1.04** — If gross receipts for the period ≤ exclusion amount, no tax is due but return must still be filed
- **DE-GRT-1.05** — Separate licenses required for each distinct business activity
- **DE-GRT-1.06** — GRT paid is deductible as a business expense on federal Schedule C
- **DE-GRT-1.07** — New businesses must register before commencing operations
- **DE-GRT-1.08** — Late filing penalty: 5% per month on unpaid tax (up to 50%) plus 1% per month interest

## Section 7: Tier 2 rules — requires judgment

- **DE-GRT-2.01** — Correct business category classification  _(Some businesses straddle categories; reviewer must determine primary activity)_
- **DE-GRT-2.02** — Nexus determination for remote sellers  _(Whether out-of-state activity creates sufficient nexus for GRT)_
- **DE-GRT-2.03** — Mixed-use transactions  _(How to allocate receipts between taxable and exempt activities)_
- **DE-GRT-2.04** — Pass-through vs. absorption of GRT  _(Whether to add GRT to customer pricing or absorb as business cost)_

## Section 8: Supplier pattern library

**Supplier pattern library**

| Pattern on bank statement | Likely meaning |
| --- | --- |
| DE DIV REVENUE GRT | Delaware Gross Receipts Tax payment |
| STATE OF DE BUS TAX | Delaware business tax payment |
| DELAWARE GRT PMT | Gross Receipts Tax quarterly/monthly payment |

## Section 9: Refusal catalogue

**Refusal catalogue**

| Refusal ID | Topic | Reason |
| --- | --- | --- |
| R-DE-GRT-01 | Petroleum products variable rate | Complex formula; requires Division of Revenue lookup |
| R-DE-GRT-02 | Insurance premium tax | Separate tax regime |
| R-DE-GRT-03 | Nexus analysis for complex multi-state operations | Requires legal analysis |
| R-DE-GRT-04 | Audit defense / reclassification disputes | Requires professional representation |
| R-DE-GRT-05 | Wilmington city net profits tax | Separate municipal tax |

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your jurisdiction — **no liability on either side until you and the accountant sign a formal engagement letter** — book a free 30-minute call:

**→ [Book a call](https://calendly.com/openaccountants-info/30min)**

We'll route you to the named verifier covering your country or state. You can also see the full list of verified accountants at [openaccountants.com/network](https://openaccountants.com/network).

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
