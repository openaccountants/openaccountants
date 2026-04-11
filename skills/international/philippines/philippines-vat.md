---
name: philippines-vat
description: Use this skill whenever asked to prepare, review, or classify transactions for Philippines VAT purposes. Trigger on phrases like "Philippines VAT", "BIR VAT", "2550Q", "2550M", "Philippine VAT return", "NIRC VAT", "VAT 12%", or any request involving Philippine VAT filing, classification, or compliance. This skill contains the complete Philippines VAT classification rules, BIR form mappings, deductibility rules, reverse charge treatment, registration thresholds, and filing deadlines required to produce a correct return. ALWAYS read this skill before touching any Philippines VAT-related work.
---

# Philippines VAT Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Philippines |
| Jurisdiction Code | PH |
| Primary Legislation | National Internal Revenue Code of 1997 (NIRC), as amended by Republic Act No. 10963 (TRAIN Law, 2017), Republic Act No. 12066 (CREATE MORE Act, 2024), and Republic Act No. 12023 (VAT on Digital Services Act, 2024) -- Title IV, Sections 105-115 |
| Supporting Legislation | Revenue Regulations (RR) No. 16-2005 (Consolidated VAT Regulations); RR No. 9-2021 (invoicing); RR No. 13-2018 (TRAIN implementation); RR No. 3-2025 and RR No. 14-2025 (VAT on Digital Services implementing rules); Revenue Memorandum Circular (RMC) No. 5-2024 (e-invoicing/CAS) |
| Tax Authority | Bureau of Internal Revenue (BIR) |
| Filing Portal | https://efps.bir.gov.ph (eFPS) and https://ebirforms.bir.gov.ph |
| Contributor | [Jurisdiction practitioner to be confirmed] |
| Validated By | Deep research verification, April 2026 |
| Validation Date | April 2026 |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: transaction classification, rate determination, BIR form box assignment, blocked input tax, zero-rating conditions, derived calculations. Tier 2: partial input VAT allocation for mixed taxpayers, transitional input VAT, CAS compliance. Tier 3: BOI/PEZA interactions, treaty-based exemptions, complex financial instruments. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required. Claude executes, engine computes.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags the issue and presents options. A licensed tax practitioner must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to licensed tax practitioner and document the gap.

---

## Step 0: Client Onboarding Questions

Before classifying ANY transaction, you MUST know these facts about the client. Ask if not already known:

1. **Entity name and TIN (Taxpayer Identification Number)** [T1] -- 9-digit TIN plus branch code (if applicable)
2. **VAT registration status** [T1] -- VAT-registered, Non-VAT (percentage tax under Section 116), or VAT-exempt
3. **Filing type** [T1] -- eFPS (Electronic Filing and Payment System) or eBIRForms
4. **Taxable quarter** [T1] -- fiscal quarter (January-March, April-June, July-September, October-December for calendar year taxpayers)
5. **Business type** [T1] -- corporation, sole proprietor, partnership, professional
6. **Industry/sector** [T2] -- impacts exempt/zero-rated classification and input VAT allocation
7. **Does the business make both taxable and exempt supplies?** [T2] -- if yes, input VAT allocation required (Section 110(A)(3)); reviewer must confirm allocation method
8. **Does the business have PEZA/BOI registration?** [T3] -- fiscal incentive zones have VAT zero-rating or exemptions; escalate
9. **Does the business use a CAS (Computerized Accounting System)?** [T1] -- CAS permit from BIR required if using computerized books/invoices
10. **Excess input VAT carried forward** [T1] -- from prior quarter's BIR Form 2550Q

**If any of items 1-2 are unknown, STOP. Do not classify any transactions until registration status is confirmed.**

---

## Step 1: Transaction Classification Rules

### 1a. Determine Transaction Type [T1]
- Sale/revenue (output VAT) or Purchase/expense (input VAT)
- Salaries, withholding taxes (EWT/FWT), SSS/PhilHealth/Pag-IBIG contributions, loan repayments, dividends = OUT OF SCOPE (never on VAT return)
- **Legislation:** NIRC Section 105 -- persons liable for VAT; Section 106 (sale of goods); Section 108 (sale of services)

### 1b. Determine Counterparty Location [T1]
- Domestic (Philippines): supplier/customer located in the Philippines
- Overseas: supplier/customer located outside the Philippines
- **Note:** Services rendered to non-resident foreign clients (B2B) may qualify for zero-rating (Section 108(B))
- **Note:** Goods imported into the Philippines = subject to import VAT (collected by Bureau of Customs)

### 1c. Determine VAT Rate [T1]
- **Standard rate: 12%** (NIRC Section 106(A), Section 108(A))
- **Zero rate: 0%** -- exports, services to non-residents, specific activities (Sections 106(A)(2), 108(B))
- **Exempt: no VAT** -- listed in Section 109
- **Legislation:** NIRC Sections 106, 108, 109

### 1d. Rate Calculation from Invoice [T1]
- Calculate from amounts: `rate = vat_amount / (gross_amount - vat_amount) * 100`
- Philippine invoices typically show VAT as: `gross_amount / 1.12 = net_amount; VAT = net_amount * 0.12`
- Normalize to 0% or 12%
- If calculated rate does not match 0% or 12%, [T2] flag for reviewer

### 1e. Determine Expense Category [T1]
- Capital goods: tangible depreciable assets with aggregate acquisition cost > PHP 1,000,000 within a 12-month period (amortization of input VAT applies -- Section 110(A)(2))
- Goods for resale: inventory purchased for resale
- Goods other than for resale: raw materials, supplies, operating inputs
- Services: professional fees, utilities, rent, etc.
- **Legislation:** NIRC Section 110(A)(2) (capital goods input VAT amortization)

---

## Step 2: VAT Rates and Classification Matrix

### Taxable Sales at 12% (Standard Rate) [T1]
**Legislation:** NIRC Section 106(A) (goods), Section 108(A) (services)

All sales of goods, properties, and services by VAT-registered persons are subject to 12% VAT unless specifically zero-rated or exempt. Includes:
- Sale of goods/merchandise in the ordinary course of trade
- Sale of real property in the ordinary course of trade (not residential under PHP 3.199M threshold)
- Lease of commercial property
- Services rendered domestically (professional, consulting, etc.)
- Importation of goods (collected by Bureau of Customs)
- Deemed sale transactions (Section 106(B)): distribution of inventory to shareholders, change from VAT to non-VAT, retirement/dissolution

### Zero-Rated Sales (0%) [T1]
**Legislation:** NIRC Section 106(A)(2) (goods), Section 108(B) (services)

| Category | Section | Conditions |
|----------|---------|------------|
| Export sales | 106(A)(2)(a)(1) | Goods shipped from Philippines to foreign country; must have export documentation |
| Foreign currency denominated sales | 106(A)(2)(a)(2) | Sale to non-resident, paid in foreign currency, goods shipped abroad |
| Sales to PEZA/Freeport enterprises | 106(A)(2)(a)(5) | Sales to registered enterprises in ecozones (cross-border doctrine) |
| Services rendered to non-residents | 108(B)(1) | Service performed for a person engaged in business outside Philippines; paid in foreign currency or equivalent |
| Services rendered to PEZA/Freeport enterprises | 108(B)(5) | Services to registered enterprises in ecozones |
| Transport of passengers/cargo by domestic carrier from Philippines to foreign country | 108(B)(4) | International carriers |
| Sale of power/fuel generated through renewable energy | 106(A)(2)(a)(6) | Renewable energy developers registered under RE Act |

### Zero-Rating Requirements (Critical) [T1]
For zero-rating to apply, ALL of the following must be present:
1. The seller must be VAT-registered
2. The transaction must fall within the enumerated zero-rated categories
3. Proper documentation must exist (export permits, proof of foreign currency payment, BOC export declarations)
4. BIR invoices/receipts must indicate zero-rated sale

**If documentation is incomplete, zero-rating is disallowed and 12% applies.** [T2] flag for reviewer if documentation is uncertain.

### Exempt Transactions (Section 109) [T1]
**Legislation:** NIRC Section 109 (as amended by TRAIN Law)

| Category | Section 109 Reference | Notes |
|----------|----------------------|-------|
| Sale/importation of agricultural products in original state | 109(A) | Unprocessed: rice, corn, vegetables, fruits, meat, fish, poultry, eggs, milk |
| Sale/importation of fertilizers, seeds, seedlings, fingerlings, feeds, ingredients for animal feeds | 109(B) | Agricultural inputs |
| Importation of personal/household effects (returning residents) | 109(C) | Subject to conditions |
| Importation of professional instruments/tools (returning OFWs) | 109(D) | Conditions apply |
| Services of agricultural contract growers/milling for others | 109(E) | Processing for agricultural producers |
| Medical/dental/hospital/veterinary services (except those by professionals) | 109(G) | Hospital services exempt; professional fees of doctors subject to 12% if > PHP 3M or VAT-registered |
| Educational services | 109(H) | By government or proprietary educational institutions and non-stock non-profit |
| Services rendered by individuals under employer-employee relationship | 109(I) | Salary/wages are not subject to VAT |
| Services by regional/area headquarters of multinationals | 109(K) | Non-income generating RHQs |
| Sale/lease of residential dwelling not exceeding PHP 3,199,200 | 109(P) | Threshold per TRAIN Law (updated annually) |
| Lease of residential unit with monthly rent not exceeding PHP 15,000 | 109(Q) | Per unit per month |
| Sale of books, newspapers, magazines | 109(R) | Mass media publications |
| Transport of passengers by international carriers | 109(S) | Subject to special tax |
| Sale/importation of drugs and medicines for diabetes, high cholesterol, hypertension | 109(AA) | TRAIN Law addition |
| Sale of gold to BSP | 109(T) | Small-scale mining |
| Sale of real property not primarily for sale (occasional sale) | 109(P) | Not in the ordinary course of trade |
| Cooperatives (limited conditions) | 109(L), 109(M), 109(N) | Duly registered cooperatives |
| Financial services (lending, guarantees) | 109(U), 109(V), 109(W) | Banks subject to GRT instead of VAT on certain services |

---

## Step 3: BIR Forms Structure and Box Assignment [T1]

### BIR Form 2550M -- Monthly VAT Declaration

**Filed monthly for the first two months of each quarter (e.g., January, February for Q1).**

| Section | Description |
|---------|-------------|
| Part I | Background information (TIN, name, period) |
| Part II | Tax Credits/Payments |
| Part III | Details of transactions |

| Item | Description | Amount |
|------|-------------|--------|
| 12A | Taxable sales (12%) | Net sales |
| 12B | Sales to government (12%, subject to withholding) | Net sales |
| 12C | Zero-rated sales | Net sales |
| 12D | Exempt sales | Net sales |
| 13 | Total sales (12A + 12B + 12C + 12D) | Sum |
| 14A | Output VAT on 12A (12%) | VAT amount |
| 14B | Output VAT on 12B (12%) | VAT amount |
| 14C | Less: Allowable input VAT | Input VAT |
| 15 | Net VAT payable (14A + 14B - 14C) | Net |
| 16-20 | Tax credits (prior excess, withholding, etc.) | Credits |
| 21 | Tax still due | After credits |
| 22 | Surcharges/interest/penalties | If late |
| 23 | Total amount payable | Final |

### BIR Form 2550Q -- Quarterly VAT Return

**Filed quarterly for the entire quarter (cumulative of all 3 months).**

| Section | Description |
|---------|-------------|
| Part I | Background information |
| Part IV-A | Summary of Sales |
| Part IV-B | Summary of Purchases/Input VAT |
| Part IV-C | VAT Computation |

#### Part IV-A: Sales/Receipts

| Item | Description |
|------|-------------|
| 16A | Taxable sales -- private (12%) |
| 16B | Taxable sales -- government (12%, subject to 5% FWT) |
| 16C | Zero-rated sales |
| 16D | Exempt sales |
| 17 | Total sales |
| 18A | Output VAT on 16A |
| 18B | Output VAT on 16B |
| 19 | Total output VAT |

#### Part IV-B: Purchases/Input VAT

| Item | Description |
|------|-------------|
| 20A | Purchases of capital goods exceeding PHP 1M (amortized) |
| 20B | Purchases of capital goods not exceeding PHP 1M |
| 20C | Purchases of goods other than capital goods |
| 20D | Purchases of services |
| 20E | Purchases not qualifying for input VAT (blocked) |
| 20F | Others (importations) |
| 21 | Total purchases |
| 22A | Input VAT on 20A (amortized portion for the quarter) |
| 22B | Input VAT on 20B |
| 22C | Input VAT on 20C |
| 22D | Input VAT on 20D |
| 22E | Input VAT on 20E (always zero -- blocked) |
| 22F | Input VAT on 20F (imports) |
| 23 | Total allowable input VAT |

#### Part IV-C: VAT Computation

| Item | Description | Calculation |
|------|-------------|-------------|
| 24 | Total output VAT | From Item 19 |
| 25 | Less: Total allowable input VAT | From Item 23 |
| 26A | VAT payable (if 24 > 25) | 24 - 25 |
| 26B | Excess input VAT (if 25 > 24) | 25 - 24 |
| 27 | Less: Tax credits (excess from prior quarter, FWT) | Credits |
| 28 | Net VAT payable | 26A - 27 |
| 29 | Surcharges/interest/penalties | If late |
| 30 | Total amount payable | 28 + 29 |

### Derived Calculations [T1]

```
Item 17  = 16A + 16B + 16C + 16D
Item 19  = 18A + 18B
Item 21  = 20A + 20B + 20C + 20D + 20E + 20F
Item 23  = 22A + 22B + 22C + 22D + 22E (always 0) + 22F
IF Item 19 > Item 23 THEN
  Item 26A = Item 19 - Item 23  -- VAT payable
  Item 26B = 0
ELSE
  Item 26A = 0
  Item 26B = Item 23 - Item 19  -- Excess input VAT
END
Item 28  = max(0, Item 26A - Item 27)
Item 30  = Item 28 + Item 29
```

---

## Step 4: Input VAT Rules [T1]

### Creditable Input VAT (Section 110) [T1]
**Legislation:** NIRC Section 110(A)

| Source of Input VAT | Creditable? | Conditions |
|-------------------|-------------|------------|
| Domestic purchases of goods with VAT invoice | Yes | Must have valid VAT invoice/receipt |
| Domestic purchases of services with VAT receipt | Yes | Must have valid VAT official receipt |
| Import VAT paid to Bureau of Customs | Yes | With import entry and proof of payment |
| Transitional input VAT (Section 111(A)) | Yes | Inventory on hand at time of VAT registration |
| Presumptive input VAT (Section 111(B)) | Yes | For processors of sardines, mackerel, milk, refined sugar, cooking oil, flour |

### Capital Goods Input VAT Amortization (Section 110(A)(2)) [T1]
**Legislation:** NIRC Section 110(A)(2)

- If aggregate acquisition cost of capital goods > PHP 1,000,000 in a 12-month period:
  - Input VAT must be AMORTIZED over the useful life or 60 months, whichever is shorter
  - Monthly amortization = Total input VAT / (useful life in months or 60, whichever is shorter)
  - Only the quarterly amortized portion is claimed on the 2550Q
- If aggregate acquisition cost <= PHP 1,000,000:
  - Full input VAT claimed in the period of purchase

### Blocked / Non-Creditable Input VAT [T1]
**Legislation:** NIRC Section 110(A); RR 16-2005

| Blocked Category | Notes |
|-----------------|-------|
| Purchases from non-VAT registered suppliers | No valid VAT invoice = no input VAT |
| Purchases without valid VAT invoice/receipt | Documentation requirement absolute |
| Input VAT attributable to exempt sales (if mixed, allocated portion) | Must allocate if mixed taxpayer |
| Input VAT on purchases for personal use | Not related to business |
| Input VAT on entertainment, amusement, recreation expenses | Not creditable (RR 16-2005) |
| Input VAT on passenger vehicles and components (non-transport business) | Unless transport or dealer |
| Purchases supported only by acknowledgment receipts or non-VAT invoices | Must be official VAT receipt/invoice |

### Input VAT Allocation for Mixed Taxpayers [T2]
**Legislation:** NIRC Section 110(A)(3)

If taxpayer makes both taxable and exempt sales:
- Input VAT directly attributable to taxable sales = fully creditable
- Input VAT directly attributable to exempt sales = NOT creditable
- Input VAT on common expenses = allocated proportionally:

```
Creditable % = (Taxable Sales / Total Sales) * 100
```

- Allocation calculated quarterly on the 2550Q
- **Flag for reviewer:** Classification of expenses as direct vs. common must be confirmed

---

## Step 5: Reverse Charge / Withholding VAT Mechanics [T1]

### VAT on Services from Non-Residents (Section 108(A)) [T1]
**Legislation:** NIRC Section 108(A); RR 16-2005, Section 4.108-1

When a VAT-registered person pays for services rendered by a non-resident (no Philippine branch/establishment):
1. The VAT-registered payor acts as withholding agent
2. Withhold VAT at 12% on the gross payment
3. Remit using BIR Form 1600 (monthly) -- filed by the 10th of the following month
4. The withheld VAT is the supplier's output VAT (remitted on their behalf)
5. The payor claims the withheld amount as input VAT on their 2550Q (Item 22D or 22F)

### VAT on Digital Services (Effective 2 June 2025) [T1]
**Legislation:** Republic Act No. 12023 (VAT on Digital Services Act); RR No. 3-2025; RR No. 14-2025

Effective 2 June 2025, 12% VAT applies to all digital services consumed in the Philippines, whether provided by resident or non-resident providers.

| Rule | Detail |
|------|--------|
| Scope | Digital services consumed in the Philippines, including online advertising, digital content, SaaS, cloud services, online marketplaces, and electronic data management |
| Registration threshold (non-resident DSPs) | PHP 3,000,000 gross sales in any 12-month period |
| Registration deadline | On or before 1 July 2025 via VDS Portal or ORUS |
| B2C sales by non-resident DSP | Non-resident DSP directly reports and remits 12% VAT |
| B2B sales by non-resident DSP to VAT-registered buyer | VAT-registered buyer withholds 12% VAT and remits under the reverse-charge mechanism |
| Non-compliance | Suspension of business operations including blocking of digital services in the Philippines |

### VAT Withholding on Government Payments (Section 114(C)) [T1]
**Legislation:** NIRC Section 114(C); RR 16-2005

Government agencies/instrumentalities must:
1. Withhold 5% Final Withholding VAT (FWT) on payments to VAT-registered suppliers
2. Supplier reports total output VAT (12%) but credits the 5% FWT
3. Supplier's remaining 7% liability = self-remitted with the return
4. FWT withheld by government = creditable against supplier's VAT liability

---

## Step 6: Invoicing and CAS Requirements [T1]

### VAT Invoice Requirements (Section 113) [T1]
**Legislation:** NIRC Section 113; RR 9-2021

#### VAT Sales Invoice (for goods)
1. Name, TIN, and address of seller (VAT-registered)
2. Name, TIN, and address of buyer
3. Sequential invoice number
4. Date of transaction
5. Description of goods, quantity, unit cost, total price
6. VAT amount shown separately
7. The words "VAT-Registered" and TIN prominently displayed
8. BIR Authority to Print (ATP) number or CAS Permit number (if computerized)
9. Imprinted on invoice: TIN-VAT

#### VAT Official Receipt (for services)
Same requirements as invoice but issued for services rendered.

### CAS (Computerized Accounting System) Requirements [T1]
**Legislation:** RR 9-2021; RMC 5-2024

- All taxpayers using computerized books of accounts and/or computerized invoicing must obtain a CAS Permit (Permit to Use) from BIR
- CAS must be capable of generating VAT invoices/receipts that meet all BIR requirements
- CAS systems subject to BIR audit -- system documentation must be maintained
- Loose-leaf books of accounts: separate permit required
- Non-compliance: potential revocation of permit and assessment of penalties

---

## Step 7: Registration Rules [T1]

**Legislation:** NIRC Section 236; RR 16-2005; TRAIN Law amendments

| Registration Rule | Threshold / Condition |
|-------------------|----------------------|
| Mandatory VAT registration | Gross sales/receipts exceed PHP 3,000,000 in any 12-month period |
| Voluntary registration | Any person below PHP 3M may voluntarily register for VAT |
| Non-VAT alternative (below threshold) | Subject to 3% Percentage Tax under Section 116 (reduced to 1% during COVID, reverted per TRAIN sunset) |
| Registration deadline | Within 30 days of exceeding PHP 3M threshold |
| VAT-exempt persons | Listed in Section 109 -- registration as VAT is not required |
| PEZA/Freeport registered entities | May be zero-rated or exempt depending on registration type [T3] |
| Professionals | If gross receipts exceed PHP 3M, must register for VAT |

### Change of Registration Status [T1]
- Non-VAT to VAT: file BIR Form 1905; transitional input VAT may be claimed on inventory
- VAT to Non-VAT: file BIR Form 1905; deemed sale provisions apply (Section 106(B))

---

## Step 8: Filing Deadlines and Penalties [T1]

**Legislation:** NIRC Sections 248-252 (penalties); Section 114 (filing)

### Filing Deadlines

| Form | Purpose | Deadline | Frequency |
|------|---------|----------|-----------|
| BIR Form 2550M | Monthly VAT Declaration | 20th of the following month | Monthly (Months 1 and 2 of each quarter) |
| BIR Form 2550Q | Quarterly VAT Return | 25th of the month following the close of the quarter | Quarterly (cumulative for the full quarter) |
| BIR Form 1600 | Monthly remittance of VAT withheld on non-resident services | 10th of the following month | Monthly |
| Summary List of Sales (SLSP) | Quarterly list of sales with VAT | Same as 2550Q | Quarterly |
| Summary List of Purchases (SLP) | Quarterly list of purchases with input VAT | Same as 2550Q | Quarterly |

### Penalties [T1]

| Violation | Penalty | Legal Reference |
|-----------|---------|-----------------|
| Late filing | 25% surcharge on tax due | Section 248(A)(1) |
| Willful neglect to file | 50% surcharge on tax due | Section 248(A)(2) |
| Late payment | 12% interest per annum (previously 20%, reduced by TRAIN) | Section 249 |
| Failure to register for VAT | Fine PHP 5,000 -- 20,000 + criminal penalty | Section 236, Section 275 |
| Failure to issue VAT invoice/receipt | Fine PHP 5,000 -- 50,000 + criminal penalty | Section 264 |
| Issuance of false/fraudulent invoice | Fine + imprisonment (2-4 years) | Section 254 |
| Failure to file quarterly returns | Penalty + potential assessment by BIR | Sections 248-249 |
| Under-declaration of income | 50% surcharge + 12% interest | Section 248(B) |

### Compromise Penalty [T1]
BIR publishes a schedule of compromise penalties (in lieu of criminal prosecution for minor violations). Amount depends on the violation type and applicable taxes.

---

## Step 9: Refund and Excess Input VAT [T1]

**Legislation:** NIRC Section 112 (refund of input VAT on zero-rated sales)

### Excess Input VAT Treatment

| Situation | Treatment | Reference |
|-----------|-----------|-----------|
| Excess from domestic sales | Carry forward to next quarter (NO refund) | Section 110(B) |
| Excess attributable to zero-rated sales | May apply for refund OR carry forward | Section 112(A) |
| Excess attributable to zero-rated sales to PEZA | May apply for refund | Section 112(A) |

### Refund Rules (Section 112) [T1]
- Refund application must be filed within 2 years from the close of the quarter when the zero-rated sale was made
- BIR has 90 days to process (per CREATE Act amendments -- previously 120 days)
- If BIR does not act within 90 days, taxpayer may appeal to the Court of Tax Appeals (CTA) within 30 days
- Refund ONLY available for excess input VAT attributable to zero-rated sales (Section 112(A))
- Excess input VAT from domestic sales: carry forward only, NO refund

---

## Step 10: Edge Case Registry

These are known ambiguous situations and their confirmed resolutions. Each is tagged with its confidence tier.

### EC1 -- Services rendered to non-resident foreign company, paid in PHP [T2]
**Situation:** VAT-registered company provides consulting to a Singapore firm but receives payment in Philippine Pesos.
**Resolution:** Zero-rating under Section 108(B)(1) requires payment in acceptable foreign currency or its equivalent in accordance with BSP rules. Payment in PHP may disqualify zero-rating. [T2] Flag for reviewer: confirm currency of payment and whether it meets BSP requirements for foreign currency equivalent.
**Legislation:** NIRC Section 108(B)(1); RR 16-2005

### EC2 -- Sale of passenger vehicle by non-transport company [T1]
**Situation:** Company (not in transport business) sells a used company car.
**Resolution:** Sale of capital asset by a VAT-registered person is subject to 12% output VAT (Section 106(A)). Even if input VAT was blocked on purchase, output VAT is still due on sale. If the company is non-VAT, the sale is subject to percentage tax or exempt depending on registration.
**Legislation:** NIRC Section 106(A)

### EC3 -- Import of goods: VAT paid at Customs [T1]
**Situation:** VAT-registered company imports raw materials. Bureau of Customs collects 12% VAT on import value (CIF + duty).
**Resolution:** Import VAT is creditable as input VAT. Report on BIR Form 2550Q, Item 20F (importations) and Item 22F (input VAT). Supporting document: Import Entry and Internal Revenue Declaration (IEIRD) or Single Administrative Document.
**Legislation:** NIRC Section 110(A)(1)(B)

### EC4 -- Government payment with 5% FWT [T1]
**Situation:** VAT-registered company supplies goods to a government agency for PHP 112,000 (inclusive of 12% VAT). Government withholds 5% FWT.
**Resolution:** Output VAT = PHP 12,000 (12% of PHP 100,000 net). Government withholds 5% FWT = PHP 5,000 (5% of net PHP 100,000). Supplier self-remits 7% = PHP 7,000. On 2550Q: Item 16B = PHP 100,000, Item 18B = PHP 12,000. FWT credit of PHP 5,000 applied in Part IV-C.
**Legislation:** NIRC Section 114(C)

### EC5 -- Lease of residential unit at PHP 14,000/month [T1]
**Situation:** Taxpayer leases a residential apartment at PHP 14,000 per month.
**Resolution:** Exempt from VAT under Section 109(Q) -- lease of residential unit with monthly rent not exceeding PHP 15,000. No output VAT. If rent exceeds PHP 15,000, the ENTIRE rent (not just the excess) becomes subject to 12% VAT.
**Legislation:** NIRC Section 109(Q)

### EC6 -- Professional earning PHP 2.5M gross receipts [T1]
**Situation:** Self-employed CPA with gross receipts of PHP 2.5M per year. Not VAT-registered.
**Resolution:** Below the PHP 3M threshold. Subject to 3% Percentage Tax under Section 116 (or 8% income tax option under TRAIN). Not required to register for VAT. Cannot issue VAT receipts. Cannot charge output VAT.
**Legislation:** NIRC Section 116; Section 24(A)(2)(b)

### EC7 -- Mixed taxpayer: allocation of input VAT [T2]
**Situation:** Hospital (VAT-registered) provides both exempt medical services and taxable pharmacy/canteen sales.
**Resolution:** Input VAT on purchases directly for taxable sales = fully creditable. Input VAT on purchases directly for exempt services = blocked. Common expenses: allocate proportionally using the formula (Taxable Sales / Total Sales). [T2] Flag for reviewer: direct vs. common expense classification requires professional judgement.
**Legislation:** NIRC Section 110(A)(3)

### EC8 -- Credit note / sales return [T1]
**Situation:** Customer returns goods worth PHP 56,000 (inclusive of PHP 6,000 VAT).
**Resolution:** Issue a credit memo / adjustment note referencing the original VAT invoice. Reduce output VAT by PHP 6,000 and net sales by PHP 50,000 in the quarter the credit is issued. Must maintain supporting documentation (return slip, credit memo, adjusted invoice).
**Legislation:** RR 16-2005, Section 4.113

### EC9 -- Withholding VAT on non-resident digital service [T1]
**Situation:** Company pays USD 5,000 to a US-based cloud provider for SaaS services. No Philippine presence.
**Resolution:** Company must withhold 12% VAT on the gross payment (converting to PHP at exchange rate on payment date). File BIR Form 1600 by the 10th. Claim the withheld amount as input VAT on the 2550Q.
**Legislation:** NIRC Section 108(A); RR 16-2005, Section 4.108-1

### EC10 -- Sale of real property in ordinary course of trade, price PHP 2.5M [T1]
**Situation:** Real estate developer (VAT-registered) sells a residential unit for PHP 2,500,000.
**Resolution:** Below the PHP 3,199,200 threshold. Exempt from VAT under Section 109(P). No output VAT. However, if the same developer sells a commercial unit or a residential unit above the threshold, 12% VAT applies.
**Legislation:** NIRC Section 109(P); TRAIN Law threshold

---

## Step 11: Key Thresholds Summary

| Threshold | Value | Legal Reference |
|-----------|-------|-----------------|
| Mandatory VAT registration | PHP 3,000,000 gross sales/receipts | Section 236(G) NIRC |
| VAT rate | 12% | Section 106(A), 108(A) |
| Percentage tax for non-VAT | 3% | Section 116 |
| Capital goods amortization trigger | PHP 1,000,000 aggregate in 12 months | Section 110(A)(2) |
| Capital goods amortization period | Useful life or 60 months (shorter) | Section 110(A)(2) |
| Residential dwelling exempt threshold | PHP 3,199,200 | Section 109(P) |
| Residential lease exempt threshold | PHP 15,000/month per unit | Section 109(Q) |
| Government FWT rate | 5% of net | Section 114(C) |
| Refund filing deadline | 2 years from close of quarter of zero-rated sale | Section 112(A) |
| BIR refund processing | 90 days | Section 112(C) |
| CTA appeal after BIR inaction | 30 days after 90-day period | Section 112(C) |
| Late filing surcharge | 25% (basic) or 50% (willful) | Section 248 |
| Interest on late payment | 12% per annum | Section 249 |
| 2550M filing deadline | 20th of following month | Section 114 |
| 2550Q filing deadline | 25th of month following quarter | Section 114 |

---

## Step 12: Reviewer Escalation Protocol

When Claude identifies a [T2] situation, output the following structured flag before proceeding:

```
REVIEWER FLAG
Tier: T2
Transaction: [description]
Issue: [what is ambiguous]
Options: [list the possible treatments]
Recommended: [which treatment Claude considers most likely correct and why]
Action Required: Licensed tax practitioner must confirm before filing.
```

When Claude identifies a [T3] situation, output:

```
ESCALATION REQUIRED
Tier: T3
Transaction: [description]
Issue: [what is outside skill scope]
Action Required: Do not classify. Refer to licensed tax practitioner. Document gap.
```

---

## Step 13: Test Suite

These reference transactions have known correct outputs. Use to validate skill execution.

### Test 1 -- Standard domestic sale, 12% VAT
**Input:** VAT-registered company sells goods to private buyer, gross PHP 112,000 (net PHP 100,000, VAT PHP 12,000).
**Expected output:** 2550Q Item 16A = PHP 100,000, Item 18A = PHP 12,000 (output VAT).

### Test 2 -- Domestic purchase with valid VAT invoice
**Input:** VAT-registered company purchases office supplies, net PHP 50,000, VAT PHP 6,000, valid VAT invoice received.
**Expected output:** 2550Q Item 20C = PHP 50,000, Item 22C = PHP 6,000 (creditable input VAT).

### Test 3 -- Export sale (zero-rated)
**Input:** VAT-registered exporter ships goods to Japan, FOB PHP 500,000. Export documentation complete.
**Expected output:** 2550Q Item 16C = PHP 500,000 (zero-rated sales). Output VAT = PHP 0. Input VAT on related purchases fully creditable.

### Test 4 -- Services to non-resident, paid in USD (zero-rated)
**Input:** VAT-registered company provides consulting to Singapore client. Fee USD 10,000 (= PHP 560,000). Paid in USD. Service performed in Philippines.
**Expected output:** 2550Q Item 16C = PHP 560,000 (zero-rated service). No output VAT. Input VAT on related expenses fully creditable.

### Test 5 -- Government sale with 5% FWT
**Input:** VAT-registered company supplies IT equipment to government agency, net PHP 200,000, VAT PHP 24,000, gross PHP 224,000. Government withholds 5% = PHP 10,000.
**Expected output:** 2550Q Item 16B = PHP 200,000, Item 18B = PHP 24,000. FWT credit PHP 10,000 in Part IV-C Item 27. Net VAT self-remitted = PHP 14,000.

### Test 6 -- Capital goods > PHP 1M (amortized)
**Input:** VAT-registered company purchases machinery for PHP 2,400,000 (net) + PHP 288,000 (VAT). Useful life = 10 years.
**Expected output:** Input VAT PHP 288,000 amortized over 60 months (shorter of 10 years or 60 months). Quarterly claim = PHP 288,000 / 60 * 3 = PHP 14,400 per quarter. 2550Q Item 20A = PHP 2,400,000, Item 22A = PHP 14,400.

### Test 7 -- Exempt sale: unprocessed agricultural products
**Input:** Farmer (VAT-registered for other activities) sells fresh vegetables for PHP 200,000.
**Expected output:** 2550Q Item 16D = PHP 200,000 (exempt sales). No output VAT. Input VAT on expenses exclusively for vegetable farming = NOT creditable.

### Test 8 -- Residential lease below PHP 15,000/month
**Input:** Taxpayer leases a residential apartment at PHP 12,000/month (3 months in the quarter = PHP 36,000).
**Expected output:** Exempt from VAT under Section 109(Q). Report as exempt in Item 16D = PHP 36,000. No output VAT.

### Test 9 -- Withholding VAT on foreign service provider
**Input:** Company pays GBP 3,000 to UK consultant (no PH presence) = PHP 210,000. Withholds 12% VAT.
**Expected output:** VAT withheld = PHP 22,500 (12% of PHP 187,500 net -- or 12% of gross if payment terms are VAT-exclusive). File BIR Form 1600. Claim PHP 22,500 as input VAT on 2550Q Item 22D.

### Test 10 -- Import VAT at Customs
**Input:** Company imports electronics, CIF + duty value PHP 1,000,000. Customs collects 12% VAT = PHP 120,000.
**Expected output:** 2550Q Item 20F = PHP 1,000,000, Item 22F = PHP 120,000 (creditable input VAT). Supporting document: IEIRD.

---

## PROHIBITIONS [T1]

- NEVER let AI guess VAT classification -- it is deterministic from the facts and legislation
- NEVER claim input VAT without a valid BIR-registered VAT invoice or official receipt
- NEVER claim full input VAT on capital goods exceeding PHP 1,000,000 aggregate -- amortization is mandatory
- NEVER apply zero-rate without confirming ALL documentation requirements are met (export docs, foreign currency proof)
- NEVER confuse zero-rated sales (input VAT fully recoverable) with exempt sales (input VAT NOT recoverable)
- NEVER refund excess input VAT from purely domestic sales -- carry forward only (Section 110(B))
- NEVER ignore the 5% FWT on government payments -- it reduces the supplier's VAT liability
- NEVER apply VAT to transactions specifically listed under Section 109 exemptions
- NEVER allow a non-VAT registered person to issue VAT invoices or charge output VAT
- NEVER claim input VAT on entertainment, amusement, or recreation expenses
- NEVER confuse BIR Form 2550M (monthly) with BIR Form 2550Q (quarterly) -- different forms, different deadlines
- NEVER file 2550M for the third month of a quarter -- the full quarter is covered by 2550Q
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not Claude

---

## Contribution Notes

If you are adapting this skill for another ASEAN jurisdiction, you must:

1. Replace all legislation references with the equivalent national legislation.
2. Replace BIR form items with the equivalent form structure for your jurisdiction.
3. Replace VAT rates with your jurisdiction's rates.
4. Replace the registration threshold (PHP 3M) with your jurisdiction's equivalent.
5. Replace the blocked categories with your jurisdiction's equivalent non-creditable categories.
6. Have a licensed tax practitioner in your jurisdiction validate every T1 rule before publishing.
7. Add your own edge cases to the Edge Case Registry.
8. Run all test suite cases against your jurisdiction's rules and replace expected outputs accordingly.

**A skill may not be published without sign-off from a licensed practitioner in the relevant jurisdiction.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
