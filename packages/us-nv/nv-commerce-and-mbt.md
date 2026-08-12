---
name: nv-commerce-and-mbt
description: "Source-cited tax guide for US-NV: nv commerce and mbt. Unverified draft, pending local-accountant review."
jurisdiction: US-NV
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# NV Commerce And Mbt

## Nevada Commerce Tax and Modified Business Tax

Nevada has no personal income tax (constitutional prohibition under Article 10, Section 1 of the Nevada Constitution). State-level business taxation runs through two parallel regimes: the Commerce Tax under NRS Chapter 363C, a gross-receipts tax imposed on businesses with Nevada gross revenue above $4,000,000 at rates that vary across 26 NAICS-derived industry categories from 0.051% (Mining) to 0.331% (Rail Transportation), and the Modified Business Tax under NRS Chapters 363A and 363B, a payroll-style tax on Nevada wages at 1.378% (general business, with a $50,000 per-quarter wage floor) or 1.853% (financial institutions and mining, no floor). A 50% Commerce-Tax-against-MBT credit links the two regimes with a four-quarter carryforward. The Commerce Tax fiscal year runs July 1 through June 30 and the return (Form TXR-030.01) is due August 14. Tax year 2025.

## 1. Scope and what this skill does NOT cover

### 1.1 In scope

- Nevada Commerce Tax (NRS Ch. 363C, regulations at NAC 363C)
- Nevada Modified Business Tax on general business (NRS Ch. 363B)
- Nevada Modified Business Tax on financial institutions (NRS Ch. 363A)
- Mining MBT treatment (NRS 363A.130 extends the 1.853% rate to mining operations)
- The 50% Commerce-Tax-against-MBT credit under NRS 363B.120 (the so-called "Commerce Tax credit")
- The federal interaction: Commerce Tax and MBT are deductible business expenses on Schedule C / Form 1120 / Form 1065 for federal purposes
- Worked examples for sole proprietors, single-member LLCs, and small corporations operating in Nevada

### 1.2 Out of scope — refer out

- **Nevada Sales and Use Tax** (NRS Ch. 372 retail sales; NRS Ch. 374 local school support tax). Combined statewide minimum is 6.85% (4.6% state + 2.25% Local School Support / Basic City-County Relief). Most counties add local option taxes; Clark County (Las Vegas) is currently 8.375% combined and Washoe County (Reno) is 8.265% combined. Filed on Form TXR-01.01 (combined sales/use return). Out of scope here — refer to the Nevada sales tax skill.
- **Live Entertainment Tax** (NRS Ch. 368A). 9% on admission charges and certain food/beverage/merchandise at venues with live entertainment over a capacity threshold. Industry-specific; refer out.
- **Gaming Tax** (NRS Ch. 463). Imposed on gross gaming revenue at graduated rates from 3.5% to 6.75% under NRS 463.370. Administered by the Nevada Gaming Control Board, not the Department of Taxation. Refer out.
- **Insurance Premium Tax** (NRS Ch. 680B). 3.5% on net direct premiums. Industry-specific; refer out.
- **Personal property tax** at the county level. Out of scope.
- **Real property tax** at the county assessor level. Out of scope.

### 1.3 Refusals (carry up to workflow base)

- **R-NV-1** — Do not compute Commerce Tax for taxpayers with Nevada gross revenue under $4,000,000 — they are exempt from the substantive tax but must still file the Commerce Tax Return (with zeros) unless they have filed Form TXR-030.81 (Commerce Tax Nexus Questionnaire) and confirmed they fall under the small-business filing exemption. The Department waived the mandatory zero-return for entities under $4M starting with the 2018-19 tax year — verify current filing waiver status before suppressing a return.  _(R-NV-1)_
- **R-NV-2** — Do not apply a Commerce Tax industry category without explicit NAICS evidence. The Department of Taxation requires the taxpayer to identify the single category that produces the largest share of Nevada gross revenue (NRS 363C.020), and miscategorization is a frequent audit issue.  _(R-NV-2, NRS 363C.020)_
- **R-NV-3** — Do not net wages across quarters for MBT. The $50,000 quarterly threshold applies on a strict calendar-quarter basis (NRS 363B.110). Q1 wages over $50,000 are taxable even if Q2 wages drop to $30,000.  _(R-NV-3, NRS 363B.110)_
- **R-NV-4** — Do not apply the 50% MBT credit to a quarter that ends before the Commerce Tax return is filed. The credit attaches to the first four quarters beginning immediately after the Commerce Tax return is filed, not the four quarters following the fiscal year-end (NRS 363B.120(2)).  _(R-NV-4, NRS 363B.120(2))_
- **R-NV-5** — Do not assume a foreign or out-of-state entity is exempt from Commerce Tax solely because it has no physical presence. Nevada applies economic nexus principles; any entity "engaging in business" in Nevada under NRS 363C.030 with Nevada gross revenue over $4M is liable. Post-Wayfair, the bright-line revenue threshold itself is sufficient.  _(R-NV-5, NRS 363C.030)_

## 2. Commerce Tax (NRS Ch. 363C)

### 2.1 Imposition and the $4,000,000 threshold

- **Imposition of Commerce Tax** — NRS 363C.200 imposes the Commerce Tax on each business entity engaged in business in Nevada whose Nevada gross revenue in a taxable year exceeds $4,000,000. The tax equals the entity's Nevada gross revenue (in excess of $4M) multiplied by the rate for the industry category in which the entity is primarily engaged. The $4M is a threshold, not an exemption amount. Once Nevada gross revenue crosses $4M, the entire excess is subject to tax (i.e., the first $4M is excluded but everything above is taxed in full). If Nevada gross revenue ≤ $4,000,000, the substantive tax is zero. The entity may still have a filing obligation depending on the Department's current zero-return waiver policy.  _(NRS 363C.200)_
- **Commerce Tax formula** — Commerce Tax = (Nevada gross revenue − $4,000,000) × Industry rate  _(NRS 363C.200)_

### 2.2 "Business entity" — who is liable

- **Business entity definition** — NRS 363C.030 defines a business entity broadly: C corporations; S corporations; Partnerships (general, limited, LLP, LLLP); Limited liability companies (single-member and multi-member, whether disregarded or not for federal tax); Sole proprietorships; Business trusts, REITs, RICs; Joint ventures; Any other entity engaged in business and required to file a federal income tax return. Sole proprietors and SMLLCs disregarded for federal tax are nevertheless separate "business entities" for Commerce Tax purposes — this is a critical departure from the federal disregarded-entity treatment. An SMLLC owned by an individual must file its own Commerce Tax Return if its Nevada gross revenue exceeds $4M, separately from any return the individual files for other sole-proprietor activity.  _(NRS 363C.030)_
- **Exclusions from business entity status** — Specifically excluded from "business entity" status under NRS 363C.030(2): Natural persons not engaged in business (i.e., wage earners); Governmental entities; Nonprofits exempt under IRC §501(c); Certain credit unions; Certain grantor trusts where the grantor is a natural person.  _(NRS 363C.030(2))_

### 2.3 Nevada gross revenue — sourcing and apportionment

"Nevada gross revenue" under NRS 363C.030 means the gross revenue of the business sitused to Nevada. Sourcing rules vary by revenue type:

**Nevada gross revenue sourcing table**  _(NRS 363C.220)_

| Revenue type | Sourcing rule | Authority |
| --- | --- | --- |
| Sale of tangible personal property | Destination — where the property is delivered to the purchaser | NRS 363C.220(1) |
| Sale of real property | Location of the real property | NRS 363C.220(2) |
| Rentals/leases of TPP | Location where the property is used | NRS 363C.220(3) |
| Rentals/leases of real property | Location of the real property | NRS 363C.220(3) |
| **Services** | **Market-based: where the benefit is received** | NRS 363C.220(4) (as amended 2017) |
| Transportation of persons | Where the person is delivered | NRS 363C.220(5) |
| Transportation of property | Where the property is delivered | NRS 363C.220(5) |
| Intangibles | Where the intangible is used | NRS 363C.220(6) |
| Interest | Domicile of the payor | NRS 363C.220(7) |
| Other receipts | Where the income-producing activity is performed | NRS 363C.220(8) |

- **Sourcing of services — market-based** — A common misconception is that Nevada uses cost-of-performance sourcing for services because it did so in early administrative guidance. In 2017 the Department issued revised regulations and guidance confirming that NRS 363C.220(4) operates on a market-based standard: services are sourced to Nevada to the extent the benefit of the service is received in Nevada. For a SaaS provider, the benefit is typically received at the customer's billing or use location. For consulting or professional services, the benefit is received where the client uses the work product. This aligns Nevada with the market-based sourcing trend (CA, NY, IL, MA, OH-CAT) and away from the older cost-of-performance approach.  _(NRS 363C.220(4))_

### 2.4 The 26 industry categories and rates (NRS 363C.300 – 363C.560)

Each business entity must elect one — and only one — industry category, based on the NAICS sector that generates the largest portion of its Nevada gross revenue (NRS 363C.020). The election is made on Form TXR-030.01 and can be changed only with Department approval.

**26 industry categories and rates table**  _(NRS 363C.300 – 363C.560)_

| # | Industry category | NAICS sector | Rate |
| --- | --- | --- | --- |
| 1 | Mining and Oil and Gas Extraction | 21 | **0.051%** |
| 2 | Agriculture, Forestry, Fishing and Hunting | 11 | 0.063% |
| 3 | Construction | 23 | 0.083% |
| 4 | Manufacturing | 31-33 | 0.091% |
| 5 | Wholesale Trade | 42 | 0.101% |
| 6 | Retail Trade | 44-45 | 0.111% |
| 7 | Air Transportation | 481 | 0.058% |
| 8 | Truck Transportation | 484 | 0.202% |
| 9 | Rail Transportation | 482 | **0.331%** |
| 10 | Other Transportation | 483, 485-488, 492 | 0.129% |
| 11 | Warehousing and Storage | 493 | 0.128% |
| 12 | Publishing, Software, Data Processing | 511, 518, 519 | 0.253% |
| 13 | Telecommunications | 517 | 0.136% |
| 14 | Broadcasting | 515 | 0.119% |
| 15 | Motion Picture and Sound Recording | 512 | 0.124% |
| 16 | Finance and Insurance (general) | 52 | 0.111% |
| 17 | Real Estate and Rental and Leasing | 53 | **0.250%** |
| 18 | Professional, Scientific and Technical Services | 54 | 0.181% |
| 19 | Management of Companies and Enterprises | 55 | 0.137% |
| 20 | Administrative and Support Services | 561 | 0.154% |
| 21 | Waste Management and Remediation | 562 | 0.261% |
| 22 | Educational Services | 61 | 0.281% |
| 23 | Health Care and Social Assistance | 62 | 0.190% |
| 24 | Arts, Entertainment and Recreation | 71 | 0.240% |
| 25 | Accommodation and Food Services | 72 | 0.200% |
| 26 | Other Services (catch-all) | 81, anything not above | 0.142% |
| 27 | Unclassified | none | 0.128% |

The two extremes are Mining at 0.051% (deliberately low to protect a politically important Nevada industry) and Rail Transportation at 0.331% (deliberately high — rails were estimated to bear a disproportionate share of historical state services). For freelance software developers and consultancies, the category will almost always be either: Category 12 (Publishing, Software, Data Processing) at 0.253% — for SaaS, packaged software, and data-processing service providers, or Category 18 (Professional, Scientific and Technical Services) at 0.181% — for custom development consulting and time-and-materials engagements. The category election matters: on $1M of Nevada gross revenue above the $4M threshold, the difference between 0.181% and 0.253% is $720 of additional tax. Document the NAICS evidence carefully.

### 2.5 Excluded revenue (NRS 363C.210)

The following are excluded from Nevada gross revenue (i.e., they reduce the gross revenue base before applying the $4M threshold and the rate):

- **Excluded revenue list** — 1. Returns and allowances — refunds, credits, or allowances issued to customers. 2. Bad debts — amounts that have become worthless and were previously included in gross revenue, deductible to the extent they would be under IRC §166. 3. Cash discounts allowed and taken at the time of sale. 4. Federal, state, and local taxes collected from purchasers and remitted to a taxing authority (e.g., sales tax collected, excise tax pass-through). 5. Pass-through receipts received by the entity that are required to be distributed to a third party (e.g., trust accounts, escrow, certain reimbursements). The Department applies a strict test: the entity must have no discretion over the disposition of the funds. 6. Receipts from intercompany transactions between members of an affiliated group (defined under NRS 363C.030 with a 50% common-ownership test). 7. Interest income (other than interest earned by a financial institution from its core business). Most ordinary entities exclude all interest. 8. Dividends received from any source. 9. Distributions from pass-through entities (avoids double taxation of receipts that already passed through a partnership or S-corp Commerce Tax filer). 10. Capital gains on the sale of investment assets (but not on the sale of inventory or operating assets used in the business). 11. Receipts from the sale, exchange, or other disposition of assets described in IRC §1221 or §1231 that are not held for sale in the ordinary course of business. 12. Proceeds from issuance of the entity's own equity or debt. 13. Insurance proceeds (other than business interruption proceeds, which are taxable). 14. Gifts, donations, contributions received. 15. Damages received in litigation other than for lost profits. 16. Hedging transactions — net of gains and losses. 17. Bartering — excluded if the parties are not engaged in business in Nevada.  _(NRS 363C.210)_

The excluded-revenue list is long, and Schedule B of Form TXR-030.01 walks the preparer through each exclusion. The most commonly missed exclusions are intercompany receipts (item 6) and pass-through receipts (item 5).

### 2.6 Filing and due date

- **Filing details** — Form: TXR-030.01 (Commerce Tax Return). Tax year: July 1 through June 30 (fiscal year, not the entity's federal tax year). Due date: 45 days after the end of the taxable year = August 14. Extension: 30-day extension available on request (Form TXR-030.E) — extends to September 13. The extension is of time to file, not to pay; interest accrues from August 14 if unpaid. Payment: Electronic via the Department's Nevada Tax Center portal, or by check with a payment voucher. Penalties: NRS 360.417 — 10% late-payment penalty plus interest at the prime rate + 2%, computed monthly. Estimated payments: None. Commerce Tax is an annual tax, paid in a single installment with the return.  _(NRS 360.417)_

Because the Commerce Tax tax year is fixed July 1 – June 30 regardless of the entity's federal fiscal year, an entity with a December year-end will need to recompute Nevada gross revenue on the state fiscal-year basis. Maintain a separate Nevada gross revenue worksheet keyed to July-June periods.

### 2.7 Affiliated groups and unitary combination

- **Combined filing rules** — NRS 363C.030 allows (does not require) affiliated entities under 50% common ownership to file a single combined Commerce Tax Return ("Consolidated Return" in the Department's terminology, though it is closer to a combined return than a federal consolidated return). The election is made on Form TXR-030.81 and once made is binding for five years. Combined filing matters because: Intercompany receipts between members of the combined group are excluded (NRS 363C.210(6)). The $4M threshold applies once to the combined group, not separately to each member. A single industry category is elected for the combined group based on the largest Nevada gross revenue component.  _(NRS 363C.030, NRS 363C.210(6))_

For most freelance software consultancies operating as a single LLC, combined filing is irrelevant. It becomes relevant when an owner controls multiple Nevada LLCs whose combined Nevada gross revenue exceeds $4M.

## 3. Modified Business Tax — General Business (NRS Ch. 363B)

### 3.1 Imposition

- **MBT General imposition** — NRS 363B.110 imposes the Modified Business Tax — General Business on every employer (other than financial institutions and mining operators, which are covered by NRS 363A) for the privilege of doing business in Nevada. The tax base is Nevada gross wages paid during the calendar quarter, less certain allowable deductions, and applies only to the excess of taxable wages over $50,000 per quarter.  _(NRS 363B.110)_
- **MBT-General formula** — MBT-General = max(0, Quarterly Nevada gross wages − Allowable deductions − $50,000) × 1.378%  _(NRS 363B.110)_

The $50,000 threshold is per quarter, not cumulative across the year. An employer with $40,000 of Nevada wages in Q1 owes zero MBT for Q1 (no carryover of the unused $10,000 of threshold). The same employer with $80,000 of Nevada wages in Q2 owes 1.378% × ($80,000 − $50,000) = $413.40 for Q2.

### 3.2 Rate — 1.378% and the rate history

- **Current general MBT rate** — 1.378%  _(NRS 363B.110 (as amended by 2021 AB 495))_

The rate history is important context because it occasionally surfaces in older guidance: Pre-2015: General MBT rate was 1.17%. 2015 (SB 483, 78th Legislature): Rate raised to 1.475% with an automatic-reduction trigger if biennial revenue collections exceeded a forecast — the so-called "sunset" mechanism intended to return some of the increase if state revenues outperformed. 2019 (Department of Taxation memorandum): Department announced an automatic reduction to 1.378% effective July 1, 2019, citing the sunset trigger. Nevada Supreme Court litigation (2020-21): The Court in Clark County School District v. Nevada Dept. of Taxation (137 Nev., Adv. Op. 6) held that the 2019 reduction was unconstitutional because the underlying revenue increase had been adopted by less than the two-thirds supermajority required for tax changes under Article 4, Section 18 of the Nevada Constitution — the Court reasoned that the reduction trigger was itself part of a tax change and could not effect a reduction without two-thirds approval. The Court ordered the higher rate (1.475%) restored retroactively. 2021 Legislature (AB 495): Following the Court decision, the Legislature enacted the current 1.378% rate by two-thirds vote, ratifying the post-litigation settlement and resolving the constitutional question. For tax year 2025 the rate is settled at 1.378% (general business) and 1.853% (financial institutions and mining). Treat older sources citing 1.17% or 1.475% as superseded.

### 3.3 Wages subject to tax

- **Wages definition** — "Wages" under NRS 363B.030 picks up the federal §3121 definition of wages for FICA purposes, but with Nevada-specific adjustments: Includes: salaries, hourly wages, commissions, bonuses, vacation pay, sick pay, tips reported to the employer, and the cash value of non-cash compensation. Excludes: wages paid to the sole proprietor or partner himself/herself (an SMLLC owner taking owner-draws is not paying themselves "wages"), independent-contractor payments (those go on 1099-NEC and are not subject to MBT), and employer FICA/Medicare contributions. The wage base tracks (but is not identical to) the Nevada Unemployment Insurance wage definition under NRS 612.190. UI has a wage cap (the 2025 Nevada UI taxable wage base is $41,800); MBT has no wage cap — it applies to total Nevada gross wages, not just to the UI-taxable portion.  _(NRS 363B.030, NRS 612.190)_

This is a frequent point of confusion: MBT taxable wages exceed UI taxable wages for any employee earning above the UI cap. Use the gross-wages-paid figure from federal Form 941 Box 5a/5c equivalents for Nevada employees, not the UI Form NUCS-4072 figure.

### 3.4 Health insurance deduction (NRS 363B.115)

- **Health insurance deduction** — An employer may deduct 50% of the cost of health insurance premiums paid for employees before computing the MBT. The deduction: Applies to premiums for medical, dental, and vision coverage. Applies only to premiums paid by the employer — employee-paid portions (whether pre-tax under a §125 cafeteria plan or after-tax) are not deductible by the employer for MBT purposes. Includes premiums for the employee, the employee's spouse, and the employee's dependents covered under the plan. Does not include HSA contributions, FSA contributions, or wellness program payments. Is taken at the quarter in which the premium is paid (cash basis), regardless of the coverage period.  _(NRS 363B.115)_

Worked illustration: An employer pays $20,000 of qualifying health insurance premiums for Nevada employees in Q3. Quarterly Nevada wages are $100,000. The deduction is $20,000 × 50% = $10,000. MBT taxable base = $100,000 − $10,000 − $50,000 = $40,000. MBT = $40,000 × 1.378% = $551.20.

### 3.5 Filing — Form TXR-020.04

- **Filing details** — Form: TXR-020.04 (Modified Business Tax — General Business). Frequency: Quarterly. Due dates: Q1 (Jan-Mar): April 30; Q2 (Apr-Jun): July 31; Q3 (Jul-Sep): October 31; Q4 (Oct-Dec): January 31. Filing: Electronic via Nevada Tax Center, or by paper with a check. Penalties: NRS 360.417 — 10% late-payment penalty plus interest. Plus a $50 per quarter late-file penalty for failure to file even when zero tax is due. Zero-return obligation: An employer with Nevada wages below the $50,000 threshold still must file the quarterly TXR-020.04 reporting zero tax unless the Department has issued a filing waiver. The waiver is automatic for employers with no Nevada employees in the quarter, but is not automatic merely because wages fell below $50,000.  _(NRS 360.417)_

## 4. Modified Business Tax — Financial Institutions and Mining (NRS Ch. 363A)

### 4.1 Imposition

- **MBT FI/Mining imposition** — NRS 363A.130 imposes a higher-rate MBT on: Financial institutions as defined in NRS 363A.050 — banks, savings and loan associations, credit unions (most), holding companies, mortgage banking companies, sales finance companies, money transmitters, and certain consumer-finance lenders. The definition is intentionally broad to capture both depository and non-depository financial-service providers. Mining operators — surface and underground mining of metal, mineral, and oil/gas extraction (added by 2015 legislation to extend the higher rate to the politically protected mining industry, balancing the low 0.051% Commerce Tax rate).  _(NRS 363A.130, NRS 363A.050)_

### 4.2 Rate — 1.853% with no threshold

- **MBT FI/Mining rate** — 1.853% on all Nevada wages paid — there is no $50,000 quarterly exclusion. Financial institutions and mining operators pay MBT from the first dollar of wages.  _(NRS 363A.130)_
- **MBT-FI/Mining formula** — MBT-FI/Mining = (Quarterly Nevada gross wages − Allowable health insurance deduction) × 1.853%  _(NRS 363A.130)_
- **Health insurance deduction mirror** — The 50% health insurance deduction under NRS 363A.140 mirrors the general-business deduction in NRS 363B.115.  _(NRS 363A.140)_

### 4.3 Filing — Form TXR-021.04

- **Filing details** — Form: TXR-021.04 (Modified Business Tax — Financial Institutions). Frequency: Quarterly. Due dates: Same as TXR-020.04 (last day of month following quarter-end). Filing: Electronic via Nevada Tax Center.  _(NRS 363A.130)_

### 4.4 What is a "financial institution" — common edge cases

- **Financial institution edge cases** — Fintech companies that engage in lending, payments, or money transmission are typically financial institutions. A SaaS platform that merely sells software to banks is not a financial institution. Mortgage brokers (originating but not funding loans) are financial institutions under NRS 363A.050. Pawn shops are financial institutions because they engage in secured consumer lending. Insurance companies are generally not subject to NRS 363A — they pay the Insurance Premium Tax (NRS 680B) in lieu. Holding companies for financial institutions are themselves financial institutions if they meet the more-than-50%-of-revenue test in NRS 363A.050(2).  _(NRS 363A.050)_

Misclassification matters: the difference between 1.378% (general) and 1.853% (financial) on $1M of wages is $4,750 per year.

## 5. The 50% Commerce-Tax-against-MBT credit (NRS 363B.120)

The Commerce Tax credit is the principal mechanism that ties the two taxes together and prevents pure double taxation of Nevada business activity.

### 5.1 The mechanic

- **Credit mechanic** — An employer that paid Commerce Tax for a Commerce Tax taxable year (July 1 – June 30) may claim a credit equal to 50% of the Commerce Tax paid against the Modified Business Tax owed in the four calendar quarters immediately following the end of the Commerce Tax year during which the return was filed.  _(NRS 363B.120)_
- **Credit formula** — MBT credit available = 50% × Commerce Tax paid Credit period = 4 quarters beginning with the quarter in which Commerce Tax was paid  _(NRS 363B.120)_

### 5.2 Timing

- **Timing rules** — The "four quarters following" language is operative. Two timing rules apply: 1. The credit attaches to the MBT quarter in which the Commerce Tax was paid, plus the next three quarters. 2. The credit must be claimed in each quarter on Form TXR-020.04 Line 6 (or TXR-021.04 Line 6) as it is used; any unused portion of the 50% allowance after four quarters expires and is not refundable.  _(NRS 363B.120)_

Example: A taxpayer files and pays Commerce Tax of $10,000 on August 14, 2025 (for the FY 2024-25 Commerce Tax year ended June 30, 2025). The available MBT credit is $5,000.
- Q3 2025 (Jul-Sep), MBT due October 31, 2025: claim credit up to $5,000.
- Q4 2025 (Oct-Dec), MBT due January 31, 2026: claim remaining credit.
- Q1 2026 (Jan-Mar), MBT due April 30, 2026: claim remaining credit.
- Q2 2026 (Apr-Jun), MBT due July 31, 2026: claim remaining credit.
- After Q2 2026: any unused credit expires.

### 5.3 Credit limitation

- **Credit limitation rule** — The credit in any single quarter is limited to the lesser of: The remaining unused credit balance, and The MBT liability for that quarter (before credit). The credit cannot reduce MBT below zero. It is not refundable.  _(NRS 363B.120)_

### 5.4 Why 50% and not 100%

The 50% cap is a legislative compromise from the 2015 enactment. The Commerce Tax was framed as a gross-receipts tax separate from the wage tax, and full credit was rejected to preserve some Commerce Tax revenue. The 4-quarter expiration further protects the General Fund from credit overhang.

### 5.5 Interaction with the financial-institution rate

- **Credit applies to both MBT regimes** — The credit is available against both NRS 363A (financial) and NRS 363B (general) MBT. A financial institution that pays Commerce Tax (e.g., a bank with Nevada gross revenue above $4M) can credit 50% of its Commerce Tax against its 1.853% MBT in the four following quarters, just like a general-business taxpayer.  _(NRS 363A, NRS 363B)_

## 6. Worked examples

### 6.1 Example 1 — SaaS company with $5,000,000 Nevada gross revenue

**Facts.** Sierra Cloud LLC is a Nevada single-member LLC owned by a Nevada-resident individual. It sells SaaS subscriptions to customers nationwide. For the Commerce Tax year July 1, 2024 – June 30, 2025:
- Total gross revenue: $7,200,000
- Sourcing analysis: customers located in Nevada generated $5,000,000 of subscription revenue (market-based sourcing under NRS 363C.220(4)).
- Excluded revenue: $50,000 of intercompany pass-through receipts from a sister LLC, $20,000 of interest income.
- Industry classification: Sierra Cloud's primary activity is SaaS hosting. NAICS 518 (Data Processing, Hosting, and Related Services) falls in Commerce Tax Category 12 (Publishing, Software, Data Processing) at **0.253%**.
- Sierra Cloud has 8 Nevada-resident employees, total quarterly Nevada gross wages of $250,000 per quarter, $40,000 quarterly health insurance premiums paid by employer.

**Commerce Tax computation.**
```
Nevada gross revenue                                $5,000,000
Less excluded receipts:
  Intercompany pass-through                            (50,000)
  Interest income                                      (20,000)
Adjusted Nevada gross revenue                       $4,930,000
Less $4M threshold                                 (4,000,000)
Taxable Nevada gross revenue                          $930,000
Rate (Category 12)                                     0.253%
Commerce Tax                                          $2,352.90
```
File Form TXR-030.01 by August 14, 2025. Pay $2,353 (rounded).

**MBT computation — Q3 2025 (Jul-Sep), due Oct 31, 2025.**
```
Quarterly Nevada wages                               $250,000
Health insurance deduction (50% × $40,000)            (20,000)
Less $50,000 quarterly threshold                      (50,000)
MBT taxable base                                     $180,000
Rate (general business)                                1.378%
MBT before credit                                     $2,480.40
Commerce Tax credit (50% × $2,353 = $1,176.50)        (1,176.50)
MBT after credit                                      $1,303.90
```

**Subsequent quarters Q4 2025, Q1 2026, Q2 2026.** Because the entire $1,176.50 credit was absorbed in Q3 2025, no Commerce Tax credit remains. Each of the next three quarters pays the full $2,480.40 (if wages remain flat). Annual MBT after credit ≈ $9,265.

**Federal interaction.** The $2,353 Commerce Tax and the ~$9,265 of MBT are both deductible business expenses on Schedule C / Form 1065 / Form 1120 in the year paid.

### 6.2 Example 2 — Small business with $40,000 Q1 wages and $80,000 Q2 wages

**Facts.** Vegas Custom Builds LLC (general contractor, NAICS 23) has Nevada gross revenue of $2,500,000 — below the $4M Commerce Tax threshold. Quarterly Nevada wages:
- Q1 2025: $40,000 (one full-time employee on hourly)
- Q2 2025: $80,000 (added two seasonal helpers)
- Q3 2025: $90,000
- Q4 2025: $35,000

Health insurance premiums paid quarterly: $4,000 (Q1 and Q4), $6,000 (Q2 and Q3).

**Commerce Tax.** Below $4M threshold → no substantive Commerce Tax. Must still file TXR-030.01 with zeros unless the Department's current filing-waiver applies (verify with the Department or the Nevada Tax Center portal each year — the waiver was extended in recent guidance but the entity should obtain explicit confirmation).

**MBT — General Business at 1.378%.**

Q1 2025 (due April 30, 2025):
```
Quarterly Nevada wages              $40,000
Health insurance deduction (50% × $4,000)  (2,000)
Adjusted wages                      $38,000
Less $50,000 threshold              (50,000) — capped at adjusted wages
MBT taxable base                    $0
MBT                                 $0
```
File TXR-020.04 with $0 due. The unused $12,000 of threshold does NOT carry to Q2 — R-NV-3 above.

Q2 2025 (due July 31, 2025):
```
Quarterly Nevada wages              $80,000
Health insurance deduction (50% × $6,000)  (3,000)
Adjusted wages                      $77,000
Less $50,000 threshold              (50,000)
MBT taxable base                    $27,000
Rate                                1.378%
MBT                                 $372.06
```

Q3 2025:
```
Adjusted wages = $90,000 − $3,000 = $87,000
Taxable base = $37,000
MBT = $37,000 × 1.378% = $509.86
```

Q4 2025:
```
Adjusted wages = $35,000 − $2,000 = $33,000
Below $50,000 threshold → MBT = $0
```

Annual MBT 2025 = $0 + $372.06 + $509.86 + $0 = **$881.92**.

No Commerce Tax credit is available because no Commerce Tax was paid.

### 6.3 Example 3 — Financial institution with no Commerce Tax but full MBT

**Facts.** Silver State Mortgage Co. LLC is a Nevada mortgage broker — a financial institution under NRS 363A.050. Nevada gross revenue for the Commerce Tax year July 1, 2024 – June 30, 2025: $3,200,000. Quarterly Nevada wages: $400,000 (steady across all four quarters), 12 W-2 employees. Health insurance premiums: $60,000 per quarter.

**Commerce Tax.** Nevada gross revenue $3.2M < $4M threshold → no Commerce Tax liability. File TXR-030.01 with zero tax (subject to current Department waiver). Note: a financial institution is not automatically a Commerce Tax filer — the $4M threshold applies to financial institutions identically to other businesses.

**MBT — Financial Institutions at 1.853%.** No $50,000 quarterly threshold applies under NRS 363A.130.

Q1 2025 (TXR-021.04 due April 30, 2025):
```
Quarterly Nevada wages              $400,000
Health insurance deduction (50% × $60,000)  (30,000)
MBT taxable base                    $370,000
Rate                                1.853%
MBT                                 $6,856.10
```

Each quarter pays $6,856.10 → annual MBT = **$27,424.40**.

No Commerce Tax credit (no Commerce Tax paid).

If in a later year Silver State's Nevada gross revenue exceeds $4M and it pays, say, $5,000 of Commerce Tax (Category 16 Finance and Insurance at 0.111%, applied to the excess), it would receive a $2,500 MBT credit usable across the four quarters following the Commerce Tax filing — reducing $27,424.40 of annual MBT to $24,924.40 in that year.

## 7. Practical guidance and common errors

### 7.1 Sourcing of cloud services and digital products

- **Cloud/digital sourcing guidance** — The market-based sourcing rule under NRS 363C.220(4) for services has limited published guidance for digital and cloud-delivered products. Department practice (per informal guidance issued 2018-2020) is: SaaS subscriptions: sourced to the customer's billing address or, if more reliably known, the location of the user. For a B2B SaaS customer with employees in multiple states, the practical approach is the customer's billing address. Downloadable software: sourced to the customer's billing address (treated as service rather than TPP). Hosting services: sourced to where the customer accesses the hosted resource (typically billing address). API/usage-based revenue: sourced to the customer's location. Advertising revenue: sourced to where the advertising is displayed (i.e., where the audience is located). For an ad network, an apportionment based on audience geography is generally accepted. Document the sourcing methodology in a contemporaneous memo. The Department has occasionally asked for sourcing documentation on audit.  _(NRS 363C.220(4))_

### 7.2 Federal income tax deductibility

- **Federal deductibility** — Both Commerce Tax and MBT are ordinary and necessary business expenses, deductible on: Schedule C Line 23 (Taxes and licenses) for sole proprietors and SMLLCs disregarded for federal tax. Form 1065 Line 14 (Taxes and licenses) for partnerships. Form 1120 Line 17 (Taxes and licenses) for C corporations. Form 1120-S Line 12 (Taxes and licenses) for S corporations. Because Nevada has no personal income tax, the federal SALT cap under IRC §164(b)(6) is largely irrelevant to Nevada residents at the individual level. However, the Commerce Tax and MBT are business taxes (not individual taxes) and are therefore deductible at the entity level without reference to the SALT cap.  _(IRC §164(b)(6))_

### 7.3 The "doing business in Nevada" question for out-of-state entities

- **Nexus rules** — NRS 363C.030 reaches any "business entity engaged in business in Nevada." Post-Wayfair (South Dakota v. Wayfair, 138 S.Ct. 2080 (2018)), a state may impose tax on entities lacking physical presence if economic nexus exists. Nevada applies the $4M gross revenue threshold itself as a de facto economic nexus threshold: an entity with over $4M of Nevada-sourced revenue is engaged in business in Nevada and owes Commerce Tax, regardless of physical presence. For MBT, by contrast, nexus is established only by paying Nevada wages. An out-of-state entity that sells into Nevada but has no Nevada employees has no MBT obligation.  _(NRS 363C.030; South Dakota v. Wayfair, Inc., 138 S.Ct. 2080 (2018))_

### 7.4 Common errors observed on audit

- **Common audit errors** — 1. Wrong industry category. Taxpayers default to Category 26 (Other Services) at 0.142% to avoid analyzing NAICS classification. The Department reclassifies on audit, often to higher-rate categories. 2. Treating intercompany receipts as taxable. Affiliated-group intercompany receipts are excluded under NRS 363C.210(6) but only with the 50% common-ownership documentation. Failure to document the affiliation defeats the exclusion. 3. Confusing the Commerce Tax fiscal year with the entity's federal year. The Commerce Tax year is always July 1 – June 30 regardless of the entity's fiscal year for federal purposes. 4. Netting MBT thresholds across quarters. R-NV-3 above. Each quarter is computed independently. 5. Missing the MBT credit window. The 4-quarter credit expires; taxpayers who forget to claim the credit on TXR-020.04 lose it. 6. Forgetting the zero-return for MBT. Even quarters below the $50,000 threshold require a filed return. 7. Misclassifying a fintech as general business. Mortgage brokers, money transmitters, and consumer lenders are financial institutions under NRS 363A.050 and pay the 1.853% rate. 8. Confusing MBT wages with UI wages. MBT has no wage cap. UI's $41,800 wage cap (2025) does not limit the MBT base.  _(NRS 363C.210(6); NRS 363A.050)_

## 8. Provenance and citations

### 8.1 Statutory authority

- NRS Ch. 363A — Modified Business Tax on Financial Institutions and Mining
- NRS Ch. 363B — Modified Business Tax on General Business
- NRS Ch. 363C — Commerce Tax
- NRS Ch. 360 — General provisions, including penalty and interest computation (NRS 360.417)
- Nev. Const. Article 4, Section 18 — Two-thirds supermajority requirement for tax changes
- Nev. Const. Article 10, Section 1 — Personal income tax prohibition

### 8.2 Regulations

- NAC 363C — Commerce Tax regulations, including industry-classification guidance and sourcing rules
- NAC 363B — Modified Business Tax regulations

### 8.3 Forms

- Form TXR-030.01 — Commerce Tax Return (annual)
- Form TXR-030.E — Commerce Tax Extension Request
- Form TXR-030.81 — Commerce Tax Nexus Questionnaire / Combined Return Election
- Form TXR-020.04 — Modified Business Tax — General Business (quarterly)
- Form TXR-021.04 — Modified Business Tax — Financial Institutions (quarterly)

### 8.4 Case law

- Clark County School District v. Nevada Department of Taxation, 137 Nev., Adv. Op. 6 (2021) — invalidated the 2019 automatic MBT rate reduction, leading to the 2021 legislative ratification of the 1.378% rate.
- South Dakota v. Wayfair, Inc., 138 S.Ct. 2080 (2018) — overruling Quill's physical-presence requirement; underpins Nevada's economic-nexus reach for Commerce Tax.

### 8.5 Department guidance

- Nevada Department of Taxation, "Commerce Tax FAQs" (revised periodically; consult current version on nv.gov before filing).
- Department of Taxation Information Notices on market-based sourcing (issued 2017 and supplemented thereafter).
- Department of Taxation, "Modified Business Tax FAQs" (revised periodically).

### 8.6 Verification checklist for tax year 2025

Before relying on this skill for a return that will be signed, verify:
- [ ] Commerce Tax industry-category rate table has not been amended by the 2025 legislative session (no scheduled changes as of skill date).
- [ ] $4M Commerce Tax threshold remains at $4M (not changed since 2015 enactment).
- [ ] MBT general rate at 1.378% confirmed (2021 AB 495).
- [ ] MBT financial/mining rate at 1.853% confirmed.
- [ ] Health insurance deduction remains at 50% (NRS 363B.115 unchanged).
- [ ] Commerce Tax credit remains at 50% with 4-quarter window (NRS 363B.120 unchanged).
- [ ] Filing portal: Nevada Tax Center (tax.nv.gov) — verify it is live and the entity is registered.

## 9. Decision flowchart

1. Is the entity engaged in business in Nevada?
   - Yes → proceed
   - No → no Nevada filing obligations

2. Does the entity have Nevada gross revenue > $4,000,000 in the July-June fiscal year?
   - Yes → file Commerce Tax (Form TXR-030.01) by August 14
   - No → still file zero-return TXR-030.01 unless Department waiver applies

3. Does the entity pay any Nevada wages?
   - Yes → file quarterly MBT
     - Is the entity a financial institution under NRS 363A.050 or a mining operator?
       - Yes → Form TXR-021.04, rate 1.853%, no quarterly threshold
       - No → Form TXR-020.04, rate 1.378%, $50,000 quarterly threshold
     - Apply 50% health insurance deduction
   - No → no MBT filing

4. Did the entity pay Commerce Tax in the most recent fiscal year?
   - Yes → claim 50% Commerce Tax credit on TXR-020.04 / TXR-021.04 in the four quarters beginning with the quarter in which Commerce Tax was paid

5. Reminder: Nevada has no personal income tax.
   The owner of a sole proprietorship or SMLLC has no Nevada personal income tax return to file
   on the federal Schedule C profit. The federal return (Form 1040 with Schedule C, SE, etc.) is
   the only income tax return.

## 10. Quick reference card

**Quick reference card**  _(NRS 363C, 363B, 363A)_

| Item | Value | Authority |
| --- | --- | --- |
| Personal income tax | None | Nev. Const. Art. 10 §1 |
| Commerce Tax threshold | $4,000,000 Nevada gross revenue per fiscal year | NRS 363C.200 |
| Commerce Tax year | July 1 – June 30 | NRS 363C.030 |
| Commerce Tax due date | August 14 (45 days after year-end) | NRS 363C.230 |
| Commerce Tax extension | 30 days, file-only | NRS 363C.235 |
| Commerce Tax — Mining | 0.051% | NRS 363C.300 |
| Commerce Tax — Construction | 0.083% | NRS 363C.330 |
| Commerce Tax — Wholesale Trade | 0.101% | NRS 363C.360 |
| Commerce Tax — Retail Trade | 0.111% | NRS 363C.370 |
| Commerce Tax — Finance/Insurance | 0.111% | NRS 363C.420 |
| Commerce Tax — Health Care | 0.190% | NRS 363C.490 |
| Commerce Tax — Prof./Sci./Tech. Services | 0.181% | NRS 363C.450 |
| Commerce Tax — Publishing/Software/Data | 0.253% | NRS 363C.380 |
| Commerce Tax — Information (Telecom) | 0.136% | NRS 363C.390 |
| Commerce Tax — Real Estate | 0.250% | NRS 363C.430 |
| Commerce Tax — Accommodation/Food | 0.200% | NRS 363C.500 |
| Commerce Tax — Other Services | 0.142% | NRS 363C.520 |
| Commerce Tax — Rail Transportation | 0.331% | NRS 363C.340 |
| MBT — General business rate | 1.378% on wages > $50,000 per quarter | NRS 363B.110 |
| MBT — Financial/Mining rate | 1.853% on all wages (no threshold) | NRS 363A.130 |
| MBT — Health insurance deduction | 50% of employer-paid premiums | NRS 363B.115, 363A.140 |
| MBT — Filing frequency | Quarterly | NRS 363B.110(4) |
| MBT — Due date | Last day of month following quarter | NRS 363B.110(4) |
| Commerce-Tax-against-MBT credit | 50% of Commerce Tax, 4-quarter window | NRS 363B.120 |
| Sales/Use tax (refer out) | 6.85% state min; 8.375% Clark County | NRS 372, 374 |
| Live Entertainment Tax (refer out) | 9% on admissions | NRS 368A |
| Gaming Tax (refer out) | 3.5%–6.75% on gross gaming revenue | NRS 463.370 |

## End of skill. Tax year 2025.

End of skill. Tax year 2025.

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is different, and the rules in the skill may not match your specific facts. To speak with one of the licensed accountants who verifies skills for your jurisdiction — no liability on either side until you and the accountant sign a formal engagement letter — book a free 30-minute call: → [Book a call](https://calendly.com/openaccountants-info/30min). We'll route you to the named verifier covering your country or state. You can also see the full list of verified accountants at [openaccountants.com/network](https://openaccountants.com/network).

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
