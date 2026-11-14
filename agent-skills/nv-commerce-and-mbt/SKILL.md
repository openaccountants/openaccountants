---
name: nv-commerce-and-mbt
description: "Nevada 2026 Commerce Tax and Modified Business Tax: fiscal revenue, current category rates, employer wages/health, four-quarter credit, returns and recomputed cases."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/nv-commerce-and-mbt"
  jurisdiction: "US-NV"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Nevada Commerce Tax and Modified Business Tax, 2026

## Scope

Nevada 2026 Commerce Tax and Modified Business Tax (MBT), including ordinary business, financial institutions/mining and the Commerce-to-MBT credit. Commerce Tax here uses July 1, 2025-June 30, 2026, due August 14, 2026; calendar 2026 MBT is computed quarterly. For the next Commerce year ending June 30, 2027, use the same currently published rules unless changed. Nevada has no individual or conventional corporate net-income tax; that does not remove either business tax. The current Commerce return is V2026.1. [Official source](https://tax.nv.gov/faqs/commerce-tax-faqs/); [Official source](https://tax.nv.gov/wp-content/uploads/2025/07/EXC-F025-COM-Tax-Return.pdf).

This is the single owner for Commerce Tax and MBT. It incorporates the retired `nv-commerce-tax` skill, including its professional-firm example, full rate table, source inputs, line mapping and refusals. `nv-payroll` owns UI and the absence of state income-tax withholding; `nv-sales-tax` owns sales/use tax. Formation/business licences, gaming, net proceeds of minerals, gold/silver excise, insurance premium, live entertainment and property taxes remain separate jobs. No uniform business-licence fee or specialist excise rate is prescribed here.

**Circular 230 §10.37 disclosure:** This skill supplies general state-tax working papers from the sources below. It is not a professional approval. A qualified tax professional must review the facts, assumptions and outputs before filing.

## Ask the client first

1. Legal entity, exemptions, actual Nevada business connection, account IDs and any merger/conversion/closure?
2. July-June receipts by type and source, federal/book revenue reconciliation, excluded income and statutory deductions?
3. Principal activity, current NAICS evidence, revenue share by category, prior election and permission to change?
4. Calendar-quarter gross Nevada wages, employer-paid qualifying health benefits, employee reimbursements and prior health offset?
5. Financial/mining licensing/status, affiliates, common payroll provider and Department approval?
6. Commerce Tax paid by year/date, credit used in each eligible MBT quarter, prior filings, estimates, notices and approved credits?

## The method, step by step

### 1. Determine each entity's Commerce filing requirement

Business entities include corporations, S corporations, disregarded LLCs, partnerships, sole proprietors and business trusts; federal pass-through status does not itself exempt them. The FAQ includes Schedule C/E/F business activity, including Nevada rentals; rent is not automatically passive income. Specific exempt entities include governments, qualifying nonprofits, credit unions, certain trusts/estates, certain REIT/REMIC arrangements and passive/intangible-investment entities. Confirm the exact exemption, rather than treating an ordinary commercial landlord as passive. Current NRS 363C.020 also excludes persons extracting gold/silver; such operators need specialist coordination. [Official source](https://tax.nv.gov/faqs/commerce-tax-faqs/); [Official source](https://www.leg.state.nv.us/Division/Legal/Lawlibrary/NRS/NRS-363C.html).

After allowed adjustments, Nevada gross revenue **over $4,000,000** creates a filing requirement for an entity engaged in Nevada business. At or below that amount, there is no annual Commerce return requirement from 2018-2019 onward. No annual waiver/Nexus Questionnaire is needed solely to obtain that threshold exemption. A closing account may require a final return. An out-of-state entity needs both a minimum Nevada connection and the revenue threshold; $4 million is not itself proof of nexus. Use the Department's Nexus Questionnaire and regulations for disputed facts. [Official source](https://tax.nv.gov/faqs/commerce-tax-faqs/).

Each entity determines its own filing and files separately. There is no ordinary affiliated/consolidated Commerce return election, no five-year combined election and no group-wide single threshold. The return instructions allow a surviving/resulting entity in a qualifying NRS 92A merger/conversion to file one combined return for that event; that limited rule is not a standing group election. Affiliation matters for excluded intercompany receipts and the approved payroll-provider credit route below. [Official source](https://tax.nv.gov/faqs/commerce-tax-faqs/); [Official source](https://tax.nv.gov/wp-content/uploads/2025/07/EXC-F025-COM-Tax-Return.pdf).

### 2. Reconcile July-June revenue and situs it

Commerce uses July 1-June 30, independently of the federal/calendar year; keep a separate bridge from the books. Ordinary expenses, cost of goods sold, wages and profit are not substituted for gross revenue. Maintain actual source evidence; do not estimate Nevada receipts solely from the billing address if user/property data contradicts it. [Official source](https://tax.nv.gov/wp-content/uploads/2025/07/EXC-F025-COM-Tax-Return.pdf).

| Revenue type | Rule | Official source |
| --- | --- | --- |
| Inventory, tangible goods | Delivery/shipment to Nevada, regardless of FOB | [Line 1](https://tax.nv.gov/wp-content/uploads/2025/07/EXC-F025-COM-Tax-Return.pdf) |
| Sale/rents/royalties of real property | Nevada property location | [Lines 1/3](https://tax.nv.gov/wp-content/uploads/2025/07/EXC-F025-COM-Tax-Return.pdf) |
| Tangible-property rents/leases | Property located/used in Nevada | [Line 3](https://tax.nv.gov/wp-content/uploads/2025/07/EXC-F025-COM-Tax-Return.pdf) |
| Ordinary services | Generally purchaser use/benefit location; specialized regulations may differ | [Line 2](https://tax.nv.gov/wp-content/uploads/2025/07/EXC-F025-COM-Tax-Return.pdf) |
| Transportation | Both trip origin and destination in Nevada; destination alone is insufficient | [Line 2](https://tax.nv.gov/wp-content/uploads/2025/07/EXC-F025-COM-Tax-Return.pdf) |
| Credit-sales/loan interest | Use the return's specific credit/loan situs rule | [Line 4](https://tax.nv.gov/wp-content/uploads/2025/07/EXC-F025-COM-Tax-Return.pdf) |
| Litigation/insurance for lost business revenue | Included when replacing Nevada business income | [Lines 5/6](https://tax.nv.gov/wp-content/uploads/2025/07/EXC-F025-COM-Tax-Return.pdf) |
| Other receipts | Classify under the form/regulations; no universal place-of-performance rule | [Line 8](https://tax.nv.gov/wp-content/uploads/2025/07/EXC-F025-COM-Tax-Return.pdf) |

For SaaS, hosting, APIs, downloadable products, advertising and multi-location business customers, document purchaser use/benefit and allocation data; billing address alone is not an established universal safe harbour. The old claims that Nevada issued a particular 2017 transition/informal 2018-2020 digital policy were not substantiated by a fetched official document and are not usable authority. Refer material unresolved allocations or use a supported reasonable, consistent alternative situsing method with the form checkbox. [Official source](https://tax.nv.gov/wp-content/uploads/2025/07/EXC-F025-COM-Tax-Return.pdf).

### 3. Separate excluded revenue from deductions

V2026.1 page 3 excludes cash discounts taken; complimentary goods/services; specified nonprofit donations in kind; indirect expense reductions; interest/dividends except customer credit-sales/loan interest; corporate/pass-through distributions and distributive shares; qualifying hedging receipts without title transfer; affiliate receipts with at least 50% common control; loan/principal redemptions and repo principal; own equity/options/treasury proceeds; qualifying capital contributions; specified liquidation/acquisition/reorganization/exchange amounts; receivable sales; specified intellectual-property dispositions; nonordinary capital/business-asset dispositions; involuntary conversions; insurance proceeds other than lost business revenue; damages other than lost business income; constitutionally protected receipts; and amounts not GAAP revenue. Keep the exact statutory transaction conditions: a vendor reimbursement, gift or barter is not universally excluded merely by its label. [Official source](https://tax.nv.gov/wp-content/uploads/2025/07/EXC-F025-COM-Tax-Return.pdf).

Deductions apply only to amounts included in revenue: customer returns/refunds; qualifying previously included bad debt; legally/fiduciarily required distributions; specified written-contract distributions and client advances/reimbursements; purchaser taxes collected/remitted; other specifically allowed deductions; and industry deductions for employee leasing, gaming, health care, insurance, liquor, mining and Armed Forces housing. Healthcare institutional reductions and specialist netting require the line instructions. A tax imposed on the business itself is not a purchaser-tax deduction. Never deduct the same item as excluded revenue and again on lines 12-25. [Official source](https://tax.nv.gov/wp-content/uploads/2025/07/EXC-F025-COM-Tax-Return.pdf).

The old list's intercompany, stock, distributions, bad debts and taxed gaming/insurance/mining receipts thus survives with corrected legal conditions. Blanket “all gifts”, “barter outside Nevada” and “all interest” exclusions are not established. Equity/debt principal and capital-asset proceeds must be classified, not treated as ordinary inventory revenue. Maintain a ledger matching every adjustment to the form page/line and underlying evidence. [Official source](https://tax.nv.gov/wp-content/uploads/2025/07/EXC-F025-COM-Tax-Return.pdf).

### 4. Apply one category and compute Commerce Tax

Select the category generating the highest share of Nevada gross revenue; do not split taxable revenue among rates. Obtain Department permission to change a prior category. NRS 363C.091 now references the most recent NAICS edition with a Department review mechanism. The V2026.1 instructions still mention 2012 in narrative but their chart reflects the revised publishing codes. Use the current chart and obtain classification confirmation if the edition mismatch changes the answer. The old separate broadcasting/motion-picture categories and combined accommodation/food row are superseded by the current chart; food remains 0.194%, accommodation 0.200%. [Official source](https://tax.nv.gov/wp-content/uploads/2025/07/EXC-F025-COM-Tax-Return.pdf); [Official source](https://www.leg.state.nv.us/Division/Legal/Lawlibrary/NRS/NRS-363C.html).

Compute max(0, Nevada revenue less allowed adjustments less $4,000,000) x category rate. In the form sequence, total revenue is line 9, threshold 10, adjusted 11, deductions 26, floored taxable revenue 27, decimal rate 28 and tax 29. One exclusion is applied once per entity, not once per activity. A high-revenue sole proprietor still uses this computation despite having no Nevada individual return. Federal treatment is in `us-schedule-c-and-se-computation`, `us-form-1065-partnership`, `us-form-1120-c-corp` and `us-form-1120-s-s-corporation-return`; do not promise a deduction in the payment year without the federal accounting method. [Official source](https://tax.nv.gov/wp-content/uploads/2025/07/EXC-F025-COM-Tax-Return.pdf).

### Rates, categories and thresholds

| Item | Amount or rule | Official source |
| --- | --- | --- |
| agriculture, forestry, fishing, hunting (NAICS 11) | 0.063% | [V2026.1 chart](https://tax.nv.gov/wp-content/uploads/2025/07/EXC-F025-COM-Tax-Return.pdf) |
| mining, quarrying, oil and gas extraction (NAICS 21) | 0.051% | [V2026.1 chart](https://tax.nv.gov/wp-content/uploads/2025/07/EXC-F025-COM-Tax-Return.pdf) |
| utilities and telecommunications (NAICS 22) | 0.136% | [V2026.1 chart](https://tax.nv.gov/wp-content/uploads/2025/07/EXC-F025-COM-Tax-Return.pdf) |
| construction (NAICS 23) | 0.083% | [V2026.1 chart](https://tax.nv.gov/wp-content/uploads/2025/07/EXC-F025-COM-Tax-Return.pdf) |
| manufacturing (NAICS 31, 32, 33) | 0.091% | [V2026.1 chart](https://tax.nv.gov/wp-content/uploads/2025/07/EXC-F025-COM-Tax-Return.pdf) |
| wholesale trade (NAICS 42) | 0.101% | [V2026.1 chart](https://tax.nv.gov/wp-content/uploads/2025/07/EXC-F025-COM-Tax-Return.pdf) |
| retail trade (NAICS 44, 45) | 0.111% | [V2026.1 chart](https://tax.nv.gov/wp-content/uploads/2025/07/EXC-F025-COM-Tax-Return.pdf) |
| air transportation (NAICS 481) | 0.058% | [V2026.1 chart](https://tax.nv.gov/wp-content/uploads/2025/07/EXC-F025-COM-Tax-Return.pdf) |
| truck transportation (NAICS 484) | 0.202% | [V2026.1 chart](https://tax.nv.gov/wp-content/uploads/2025/07/EXC-F025-COM-Tax-Return.pdf) |
| rail transportation (NAICS 482) | 0.331% | [V2026.1 chart](https://tax.nv.gov/wp-content/uploads/2025/07/EXC-F025-COM-Tax-Return.pdf) |
| other transportation (NAICS 483, 485, 486, 487, 488, 491, 492) | 0.129% | [V2026.1 chart](https://tax.nv.gov/wp-content/uploads/2025/07/EXC-F025-COM-Tax-Return.pdf) |
| warehousing and storage (NAICS 493) | 0.128% | [V2026.1 chart](https://tax.nv.gov/wp-content/uploads/2025/07/EXC-F025-COM-Tax-Return.pdf) |
| publishing, software and data processing (NAICS 512, 513, 516, 518) | 0.253% | [V2026.1 chart](https://tax.nv.gov/wp-content/uploads/2025/07/EXC-F025-COM-Tax-Return.pdf) |
| utilities and telecommunications (NAICS 517) | 0.136% | [V2026.1 chart](https://tax.nv.gov/wp-content/uploads/2025/07/EXC-F025-COM-Tax-Return.pdf) |
| finance and insurance (NAICS 52) | 0.111% | [V2026.1 chart](https://tax.nv.gov/wp-content/uploads/2025/07/EXC-F025-COM-Tax-Return.pdf) |
| real estate and rental and leasing (NAICS 53) | 0.250% | [V2026.1 chart](https://tax.nv.gov/wp-content/uploads/2025/07/EXC-F025-COM-Tax-Return.pdf) |
| professional, scientific and technical services (NAICS 54) | 0.181% | [V2026.1 chart](https://tax.nv.gov/wp-content/uploads/2025/07/EXC-F025-COM-Tax-Return.pdf) |
| management of companies and enterprises (NAICS 55) | 0.137% | [V2026.1 chart](https://tax.nv.gov/wp-content/uploads/2025/07/EXC-F025-COM-Tax-Return.pdf) |
| administrative and support services (NAICS 561) | 0.154% | [V2026.1 chart](https://tax.nv.gov/wp-content/uploads/2025/07/EXC-F025-COM-Tax-Return.pdf) |
| waste management and remediation services (NAICS 562) | 0.261% | [V2026.1 chart](https://tax.nv.gov/wp-content/uploads/2025/07/EXC-F025-COM-Tax-Return.pdf) |
| educational services (NAICS 61) | 0.281% | [V2026.1 chart](https://tax.nv.gov/wp-content/uploads/2025/07/EXC-F025-COM-Tax-Return.pdf) |
| health care and social assistance (NAICS 62) | 0.190% | [V2026.1 chart](https://tax.nv.gov/wp-content/uploads/2025/07/EXC-F025-COM-Tax-Return.pdf) |
| arts, entertainment and recreation (NAICS 71) | 0.240% | [V2026.1 chart](https://tax.nv.gov/wp-content/uploads/2025/07/EXC-F025-COM-Tax-Return.pdf) |
| accommodation (NAICS 721) | 0.200% | [V2026.1 chart](https://tax.nv.gov/wp-content/uploads/2025/07/EXC-F025-COM-Tax-Return.pdf) |
| food services and drinking places (NAICS 722) | 0.194% | [V2026.1 chart](https://tax.nv.gov/wp-content/uploads/2025/07/EXC-F025-COM-Tax-Return.pdf) |
| other services (NAICS 81) | 0.142% | [V2026.1 chart](https://tax.nv.gov/wp-content/uploads/2025/07/EXC-F025-COM-Tax-Return.pdf) |
| unclassified (NAICS 519, 92) | 0.128% | [V2026.1 chart](https://tax.nv.gov/wp-content/uploads/2025/07/EXC-F025-COM-Tax-Return.pdf) |

| Item | Amount or rule | Official source |
| --- | --- | --- |
| Commerce filing/base threshold | $4,000,000 Nevada gross revenue; strictly over for annual filing | [Official source](https://tax.nv.gov/faqs/commerce-tax-faqs/) |
| Commerce year/due | July 1-June 30; 45 days after year-end, normallyAugust 14 | [Official source](https://tax.nv.gov/faqs/commerce-tax-faqs/) |
| General MBT | 1.17% after health offset and $50,000 quarterly floor | [Official source](https://tax.nv.gov/wp-content/uploads/2025/12/TAX-F003-MBT-Return-General-Business.pdf); [DOR MBT page](https://tax.nv.gov/tax-types/modified-business-tax/) |
| Financial/mining MBT | 1.554%; no $50,000 floor (the floor is a line on the general-business return only) | [Official source](https://tax.nv.gov/wp-content/uploads/2025/12/TAX-F002-MBT-Return-Financial-Institution.pdf); [Official source](https://tax.nv.gov/wp-content/uploads/2025/12/TAX-F004-MBT-Return-Mining.pdf); [general-business return](https://tax.nv.gov/wp-content/uploads/2025/12/TAX-F003-MBT-Return-General-Business.pdf); [DOR MBT page](https://tax.nv.gov/tax-types/modified-business-tax/) |
| Employer health deduction | Full qualifying employer-paid amount, not 50%; excess offset carries forward | [Official source](https://tax.nv.gov/faqs/modified-business-tax-faqs/) |
| Commerce-to-MBT credit | 50% of Commerce Tax actually paid; four quarters after June 30 | [Official source](https://tax.nv.gov/faqs/commerce-tax-faqs/) |
| Commerce extension interest | 0.75% per month despite the extension | [Official source](https://tax.nv.gov/faqs/commerce-tax-faqs/) |
| Commerce late payment | 2% days 1-10; 4%11-15; 6%16-20; 8%21-30; 10%31+ | [Official source](https://tax.nv.gov/wp-content/uploads/2025/07/EXC-F025-COM-Tax-Return.pdf) |

### 5. Compute MBT from gross wages, not UI-capped wages

ESD UI registration automatically creates the Department MBT account; account IDs remain different from the federal EIN. General-business MBT begins with total Nevada wages including tips, matching ESD **gross** wages, not UI taxable wages or an assumed federal 941 line. There is no per-person MBT wage cap. Sole proprietor/partner draws and genuine independent-contractor payments are not employee wages; corporate officer/status disputes require the state rules. Distinguish worker coverage before selecting the base. [Official source](https://tax.nv.gov/faqs/modified-business-tax-faqs/); [Official source](https://tax.nv.gov/wp-content/uploads/2025/12/TAX-F003-MBT-Return-General-Business.pdf).

Deduct the **full** qualifying employer-paid health insurance/benefit amount, excluding amounts repaid by workers. Employee/dependent medical, dental and vision qualify; qualified self-insured claims/direct administration and Taft-Hartley welfare payments can qualify. HSA contributions and industrial-injury/occupational-disease cover do not. Unsubstantiated FSA/wellness arrangements need specific confirmation. If qualifying health exceeds wages, carry the excess health offset forward under the return; an unused $50,000 general wage floor never carries and wage floors cannot be averaged across quarters. General tax=max(0, gross wages-health-current prior offset-$50,000)x 0.0117. Financial/mining tax uses adjusted wages x 0.01554 without that floor. [Official source](https://tax.nv.gov/faqs/modified-business-tax-faqs/); [Official source](https://tax.nv.gov/wp-content/uploads/2025/12/TAX-F003-MBT-Return-General-Business.pdf); [Official source](https://tax.nv.gov/wp-content/uploads/2025/12/TAX-F002-MBT-Return-Financial-Institution.pdf); [Official source](https://tax.nv.gov/wp-content/uploads/2025/12/TAX-F004-MBT-Return-Mining.pdf).

Classify financial institutions from NRS 363A.050 licensing/registration and affiliation criteria, not a software customer's industry. A SaaS vendor to banks is not automatically a financial institution. Mortgage, lending, fintech, money-transmission, pawn, insurance-sales and holding-company cases need actual licences and statutory exceptions; do not copy the old blanket “all fintech” or “all credit unions” statement. Mining uses its own current return. Classification disputes use a supported petition. Employer MBT cannot be withheld from workers. [Official source](https://tax.nv.gov/faqs/modified-business-tax-faqs/).

The old 1.378%/1.853% rates were historical, replaced fromJuly 1, 2023. The old litigation/AB 495 narrative was not substantiated and must not be used to restore an obsolete rate. The old assertion that the health deduction was 50% was incorrect. For $100,000 wages and $20,000 qualifying employer health, general 2026 MBT is($100,000-$20,000-$50,000)x 1.17%=$351. The rate-only general-versus-financial difference on $1 million adjusted wages is $3,840, before the general-business floor; the old $4,750 illustration used superseded rates. [Official source](https://tax.nv.gov/faqs/modified-business-tax-faqs/); [Official source](https://tax.nv.gov/wp-content/uploads/2025/12/TAX-F003-MBT-Return-General-Business.pdf).

### 6. Apply the linked credit in its actual four-quarter window

Available credit is 50% of Commerce Tax **paid**, limited to MBT otherwise due. It is nonrefundable. The eligible quarters are the four calendar quarters immediately after the Commerce Tax year ends June 30, regardless of the payment/filing date. For Commerce year ending June 30, 2026, they endSeptember 30, 2026, December 31, 2026, March 31, 2027, June 30, 2027. Late payment can support amended eligible returns; it does not restart the clock. Partial payment creates only half the paid amount. Unused credit after quarter 4 expires. Both MBT regimes can use it. [Official source](https://tax.nv.gov/faqs/commerce-tax-faqs/).

For example, $10,000 paid Commerce Tax generates $5,000 credit; MBT for a quarter of $3,000 can absorb $3,000, leaving $2,000 for remaining eligible quarters. If only $200 of a $1,000 Commerce liability is paid, credit is $100. A late May payment can still be used by amending eligible earlier quarters or in the last eligible June quarter. The FAQ permits MBT amendment within three years after the last day of the month following the affected quarter; preserve dates and the assessment/credit history. [Official source](https://tax.nv.gov/faqs/commerce-tax-faqs/).

An approved affiliated-group central payroll provider may use eligible affiliates' credit under the application conditions. Common control alone does not transfer the credit. An affiliate with no employees generating MBT cannot supply credit under that route merely because it paid Commerce Tax. An unrelated payroll agent simply files the business's own return and needs no affiliate-provider designation. [Official source](https://tax.nv.gov/faqs/commerce-tax-faqs/).

## Worked cases

All facts are hypothetical; old examples are recomputed using current forms rather than silently removed.

**Case 1, Sierra Cloud LLC:** For the year ended June 30, 2026, total receipts $7.2 m include $5 m Nevada-sitused receipts. Assume documented excluded affiliate receipts $50,000 and ordinary interest $20,000 were included in that $5 m; adjusted $4.93 m, excess $930,000, rate 0.253%, Commerce $2,352.90. Quarterly wages $250,000 and full health $40,000 give $160,000 MBT base, MBT $1,872. Credit $1,176.45 leaves $695.55 for September 2026 quarter; with same wages next 3 quarters, total MBT after credit $6,311.55. Classify actual SaaS use/benefit and NAICS; neither follows from billing alone. No instruction to round the Commerce payment to $2,353 is assumed.

```oa-check
name: NV Sierra Cloud Commerce and MBT
inputs:
  nv_including_excluded: 5000000
  affiliate: 50000
  interest: 20000
  wages: 250000
  health: 40000
steps:
- adjusted: nv_including_excluded - affiliate - interest
- commerce: (adjusted - 4000000) * 0.00253
- mbt_base: max(wages - health - 50000, 0)
- mbt: mbt_base * 0.0117
- credit: commerce * 0.5
- first_mbt: mbt - credit
- four_quarter_mbt: mbt * 4 - credit
expected:
  adjusted: 4930000
  commerce: 2352.9
  mbt_base: 160000
  mbt: 1872
  credit: 1176.45
  first_mbt: 695.55
  four_quarter_mbt: 6311.55
```

**Case 2, Vegas Custom Builds LLC:** $2.5 m Nevada Commerce revenue requires no ordinary annual Commerce filing. General 2026 quarterly wages $40 k/$80 k/$90 k/$35 k; full health $4 k/$6 k/$6 k/$4 k. MBT bases 0/$24 k/$34 k/0, tax 0/$280.80/$397.80/0, total $678.60. No unused quarterly wage-floor transfer. File MBT even at zero; no Commerce credit when none paid.

```oa-check
name: NV Vegas Custom Builds quarters
inputs:
  q1: 40000
  q2: 80000
  q3: 90000
  q4: 35000
steps:
- tax1: max(q1 - 4000 - 50000, 0) * 0.0117
- tax2: max(q2 - 6000 - 50000, 0) * 0.0117
- tax3: max(q3 - 6000 - 50000, 0) * 0.0117
- tax4: max(q4 - 4000 - 50000, 0) * 0.0117
- total: tax1 + tax2 + tax3 + tax4
expected:
  tax1: 0
  tax2: 280.8
  tax3: 397.8
  tax4: 0
  total: 678.6
```

**Case 3, Silver State Mortgage Co. LLC:** Assume its actual licence establishes financial-institution status. Nevada revenue $3.2 m gives no annual Commerce filing. Quarterly wages $400,000 less full qualifying health $60,000=$340,000; no wage floor, tax $5,283.60, annual $21,134.40. If a later eligible Commerce payment is $5,000, the $2,500 credit can reduce four eligible quarters with those wages to $18,634.40. Do not import the old half-health deduction or 1.853% rate.

```oa-check
name: NV Silver State Mortgage financial
inputs:
  wages: 400000
  health: 60000
  future_commerce: 5000
steps:
- base: wages - health
- quarter: base * 0.01554
- annual: quarter * 4
- future_credit: future_commerce * 0.5
- after_future_credit: annual - future_credit
expected:
  base: 340000
  quarter: 5283.6
  annual: 21134.4
  future_credit: 2500
  after_future_credit: 18634.4
```

**Case 4, retained professional-firm example:** $6 m adjusted Nevada revenue, NAICS 54 rate 0.181%:tax $3,620. On $1 m excess, documented professional services cost $1,810 versus publishing/data $2,530, difference $720. Classification follows principal revenue activity; it is not a taxpayer election to pick the lower amount. If facts change to publishing/data, the higher rate applies.

```oa-check
name: NV professional firm and category decision
inputs:
  revenue: 6000000
  excess_compare: 1000000
steps:
- firm_tax: (revenue - 4000000) * 0.00181
- professional: excess_compare * 0.00181
- data: excess_compare * 0.00253
- difference: data - professional
expected:
  firm_tax: 3620
  professional: 1810
  data: 2530
  difference: 720
```

## When to refuse or refer

Refer disputed nexus, passive/investment/REIT/gold-silver exclusions, uncertain NAICS transitions, multistate digital situsing, unproven pass-through deductions, mergers and affiliate payroll-provider claims. Refer financial/mining status and health arrangements without documentation. Do not file from the old assertions of combined returns, 100% credit, 50% health, automatic zero-return waiver or a payment-date credit clock. Revenue below the threshold does not remove MBT or UI duties.

Gaming, mining/net-proceeds, insurance premiums, live entertainment, county property taxes and licence fees need their own official rules. The old indicative rates for those out-of-scope taxes are retained as unconfirmed historical claims in the source-gap line, not issued as 2026 tax instructions. No state-income return is created to compute a Commerce/MBT business expense; federal computations stay with their owners.

## Filing and payment

Commerce: register/file/pay via My Nevada Tax; the year ended June 30, 2026 was due August 14, 2026. No estimates. Good cause can support a 30-day **file-and-pay** extension requested before the due date; interest still accrues 0.75% per month from the unextended date. The next-day business rule applies to weekends/holidays. Current form penalty table is graduated 2%-10%, not automatic 10%; its interest worksheet prints “.075%(.0075)”, an inconsistent label. The FAQ clearly states 0.75% monthly, which matches multiplier 0.0075. Record the arithmetic and state payoff instead of using prime+2%. [Official source](https://tax.nv.gov/faqs/commerce-tax-faqs/); [Official source](https://tax.nv.gov/wp-content/uploads/2025/07/EXC-F025-COM-Tax-Return.pdf).

Commerce line mapping corrects the retired file: NAICS is in the header; lines 1-8 source receipts; 9 total; 10 threshold; 11 adjusted; 12-25 deductions; 26 deduction total; 27 base; 28 rate; 29 tax; 30 penalty; 31 interest; 32 prior liability; 33 approved credit; 34 total due; 35 paid. Registering in a portal does not itself establish a filing duty. Amend with supporting records when estimates become actual; mark alternative situsing if used. [Official source](https://tax.nv.gov/wp-content/uploads/2025/07/EXC-F025-COM-Tax-Return.pdf).

MBT: file general, financial or mining return quarterly, including zero wages/zero tax until account closure; no automatic no-employee waiver. Due last day of following month, with state weekend/holiday handling. The 2026 quarter ends March 31, June 30, September 30, December 31 give ordinary deadlines April 30, July 31, November 2, 2026 and February 1, 2027. Use My Nevada Tax and the actual return/account. General current form health is line 2, prior offset 4, threshold 7, tax 9, Commerce credit 10; obsolete line 6 credit references are not used. Do not guess a generic $50 late-file charge; use actual form penalty/interest instructions. [Official source](https://tax.nv.gov/faqs/modified-business-tax-faqs/); [Official source](https://tax.nv.gov/wp-content/uploads/2025/12/TAX-F003-MBT-Return-General-Business.pdf).

Keep source invoices/contracts, use/delivery evidence, July-June bridge, NAICS revenue analysis, affiliate ownership, health invoices and employee reimbursements, gross-wage reconciliation, paid-tax credit schedule and state confirmations. Reconcile supplier/bank labels to account/type/period; neither a Commerce nor MBT payment proves its deduction. To close payroll, notify ESD of last payroll and complete all returns; the Department then closes MBT. [Official source](https://tax.nv.gov/faqs/modified-business-tax-faqs/).

## Completion checklist

- Entity/exemption and Nevada connection established, including a final return if closing.
- Fiscal receipts reconciled and source/exclusion/deduction conditions documented without double deduction.
- One approved category/rate applied, threshold once, correct current form used.
- MBT gross wages matched to ESD, full eligible health and prior health offset separated from quarterly wage floor.
- Financial/mining status documented; UI cap does not limit MBT.
- Credit limited to 50% paid and eligible four-quarter window, with affiliate approval if needed.
- Zero MBT returns, filing/payment dates and separate federal/excise jobs resolved.

## Sources

| Source and reading scope | URL | Read on |
| --- | --- | --- |
| Commerce V2026.1 return/instructions. Read for current 26 category chart, revenue exclusions, deductions, situsing, line mapping and penalty worksheet. | https://tax.nv.gov/wp-content/uploads/2025/07/EXC-F025-COM-Tax-Return.pdf | 2026-11-13 |
| DOR Commerce FAQ. Read for threshold waiver, entity/nexus, separate returns, extension, 50% credit window and affiliate-provider conditions. | https://tax.nv.gov/faqs/commerce-tax-faqs/ | 2026-11-13 |
| Current NRS 363C. Read for NAICS edition rule, entity definitions and gold/silver exception; read through web because direct fetch 403. | https://www.leg.state.nv.us/Division/Legal/Lawlibrary/NRS/NRS-363C.html | 2026-11-13 |
| DOR MBT FAQ. Read for current rates, full health deduction, no wage cap, registration, zero filing and closure. | https://tax.nv.gov/faqs/modified-business-tax-faqs/ | 2026-11-13 |
| Current general MBT return. Read for 1.17%, health offset, $50,000 floor and credit lines. | https://tax.nv.gov/wp-content/uploads/2025/12/TAX-F003-MBT-Return-General-Business.pdf | 2026-11-13 |
| Current financial MBT return. Read for 1.554%, full health and no general floor. | https://tax.nv.gov/wp-content/uploads/2025/12/TAX-F002-MBT-Return-Financial-Institution.pdf | 2026-11-13 |
| Current mining MBT return. Read for distinct mining return and 1.554% rate. | https://tax.nv.gov/wp-content/uploads/2025/12/TAX-F004-MBT-Return-Mining.pdf | 2026-11-13 |

Not yet confirmed: specialist source/nexus and industry deduction cases; NAICS narrative-edition mismatch; out-of-scope excise/licence rates. The old live-entertainment 9%, gaming 3.5%-6.75%, insurance 3.5%, uniform $500 licence, unverified court/AB 495 history, blanket digital billing-address practice, gift/barter exclusions, FSA/wellness treatment and generic $50 late-file fee were not established as current rules. Historical rates 1.378%/1.853% and half-health computations are superseded, not 2026 filing inputs.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `nv-commerce-and-mbt` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/nv-commerce-and-mbt. If neither is available, confirm every figure against the official source pages cited above before relying on it.
