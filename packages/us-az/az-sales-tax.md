---
name: az-sales-tax
description: Arizona transaction privilege tax (TPT), the state's sales tax, and use tax for 2026. TPT is a tax on the seller for the privilege of doing business, not a tax on the buyer. Covers the classifications and state rates (5.6% for retail, restaurants, prime contracting and most others, 5.5% transient lodging, 3.125% mining), county and city layers from the ADOR rate tables (for example 9.10% combined for retail in Phoenix), prime contracting on 65% of gross receipts against maintenance, repair, replacement or alteration work, the $100,000 remote seller and marketplace facilitator thresholds, licensing at $12 per location, the TPT-2 return due on the 20th, annual, quarterly and monthly filing bands, the June estimated payment, the 1% or 1.2% accounting credit and use tax. Trigger on "Arizona sales tax", "AZ TPT", "transaction privilege tax", "TPT-2", "Arizona use tax", "Arizona prime contracting", "MRRA", "Arizona economic nexus". Load us-sales-tax for the federal-level framework.
version: "3.0"
jurisdiction: US-AZ
tax_year: 2026
last_updated: 2026-11-13
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: vat-gst
type: computation
---

# Arizona transaction privilege tax (sales tax) and use tax, 2026

> **Source-cited draft.** Built from A.R.S. 42-5008, 42-5010, 42-5010.01, 42-5014, 42-5017, 42-5044 and 42-5075 on azleg.gov, the ADOR Transaction Privilege and Other Tax Rate Tables effective 1 October 2026 and the ADOR Transaction Privilege Tax page, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** Arizona's "sales tax" is the **transaction privilege tax (TPT)**, a tax on the seller's gross receipts for the privilege of doing business. The seller owes it whether or not it is charged to the customer. The state rate is **5.6%** for retail and most classifications (5% under A.R.S. 42-5010 plus 0.6% under 42-5010.01), **5.5%** for transient lodging and **3.125%** for mining. Counties and cities add their own rates, all collected by ADOR on one TPT-2 return: retail in Phoenix is **9.10%** (6.30% state and Maricopa County plus 2.80% Phoenix). Prime contractors pay on **65%** of gross receipts. Remote sellers must license once direct Arizona retail sales pass **$100,000** in the current or prior year. Returns are due on the **20th** of the month after the period.

## Scope and who this is for

In scope: any business with Arizona TPT activity in 2026, in-state or remote; retail, restaurant, rental, lodging and prime contracting classifications; county and city TPT collected by ADOR; use tax on purchases where no TPT was paid; licensing, filing and payment.

Out of scope, and where it goes:

| Topic | Skill |
| --- | --- |
| The US-wide sales tax framework | `us-sales-tax` |
| Which states a remote seller has nexus in | `us-sales-tax-nexus-50-state-matrix` |
| Arizona income tax on the owner | `az-income-tax` |
| Arizona corporate income tax | `az-corporate-tax` |
| Property tax, vehicle use tax (ADOT), mining severance detail, 911 and telecom excise, marijuana excise | Not covered |

## Ask the client first

1. What does the business sell, and which TPT classifications does that fall in (retail, restaurant, rental of tangible personal property, transient lodging, prime contracting, others)?
2. Where is each business location, which cities and counties do sales arise in, and is any activity on a reservation?
3. In-state business, or a remote seller? Direct Arizona retail sales in 2025 and to date in 2026, separately from sales through a marketplace facilitator.
4. TPT license number, licensed locations and the filing frequency ADOR assigned.
5. For contractors: new construction or modification (prime contracting), or maintenance, repair, replacement or alteration (MRRA)? Is there a written contract, and who is the prime?
6. Purchases from out-of-state vendors with no Arizona tax charged (use tax).
7. Resale or exemption certificates received and given (Form 5000, 5000A, 5005).

## The method, step by step

### Rates, bands and thresholds

| Item | 2026 figure | Source |
| --- | --- | --- |
| State rate, retail, restaurant and bar, amusement, personal property rental, prime contracting, utilities, telecommunications, transporting, pipeline, private car line, publication, job printing | 5% | [A.R.S. 42-5010(A)(1)](https://www.azleg.gov/ars/42/05010.htm) |
| Additional state increment on the same classifications (1 July 2021 to 30 June 2041) | 0.6% (state total 5.6%) | [A.R.S. 42-5010.01(A)](https://www.azleg.gov/ars/42/05010-01.htm) |
| State rate, transient lodging and registered online lodging marketplaces | 5.5% | [A.R.S. 42-5010(A)(2)](https://www.azleg.gov/ars/42/05010.htm) |
| State rate, mining | 3.125% (three and one-eighth percent) | [A.R.S. 42-5010(A)(3)](https://www.azleg.gov/ars/42/05010.htm) |
| State rate, commercial lease | 0% (cities may still tax it) | [A.R.S. 42-5010(A)(4)](https://www.azleg.gov/ars/42/05010.htm) |
| Combined state and county, retail (code 017): Maricopa | 6.30% | [ADOR rate tables, 1 Oct 2026, Table 1](https://azdor.gov/sites/default/files/document/TPT_RATETABLE_10012026.pdf) |
| Combined state and county, retail: Pima | 6.10% | [ADOR rate tables, Table 1](https://azdor.gov/sites/default/files/document/TPT_RATETABLE_10012026.pdf) |
| Combined state and county, retail: Mohave | 5.60% (no county rate) | [ADOR rate tables, Table 1](https://azdor.gov/sites/default/files/document/TPT_RATETABLE_10012026.pdf) |
| Combined state and county, retail: Coconino | 6.90% | [ADOR rate tables, Table 1](https://azdor.gov/sites/default/files/document/TPT_RATETABLE_10012026.pdf) |
| Combined state and county, retail: Pinal | 6.70% | [ADOR rate tables, Table 1](https://azdor.gov/sites/default/files/document/TPT_RATETABLE_10012026.pdf) |
| Combined state and county, retail: Yavapai / Yuma | 6.35% / 6.712% | [ADOR rate tables, Table 1](https://azdor.gov/sites/default/files/document/TPT_RATETABLE_10012026.pdf) |
| Combined state and county, retail: Cochise, Gila, Graham, La Paz, Santa Cruz | 6.60% | [ADOR rate tables, Table 1](https://azdor.gov/sites/default/files/document/TPT_RATETABLE_10012026.pdf) |
| Combined state and county, retail: Navajo / Apache and Greenlee | 6.43% / 6.10% | [ADOR rate tables, Table 1](https://azdor.gov/sites/default/files/document/TPT_RATETABLE_10012026.pdf) |
| Combined state and county, transient lodging (code 025): Maricopa | 7.27% | [ADOR rate tables, Table 1](https://azdor.gov/sites/default/files/document/TPT_RATETABLE_10012026.pdf) |
| Use tax on purchases (code 029), state | 5.60% in every county | [ADOR rate tables, Table 1](https://azdor.gov/sites/default/files/document/TPT_RATETABLE_10012026.pdf) |
| City rate, Phoenix (region PX): retail, restaurants, prime contracting, rental of tangible personal property, hotels, use tax | 2.80% (retail single-item portion over $14,338: 2.00%; hotel additional tax 3.00%) | [ADOR rate tables, Table 2](https://azdor.gov/sites/default/files/document/TPT_RATETABLE_10012026.pdf) |
| City rate, Tucson (region TU): retail, restaurants, prime contracting | 2.60% (hotels 9.00%) | [ADOR rate tables, Table 2](https://azdor.gov/sites/default/files/document/TPT_RATETABLE_10012026.pdf) |
| Prime contracting tax base | 65% of gross proceeds or gross income, after the listed deductions | [A.R.S. 42-5075(B)](https://www.azleg.gov/ars/42/05075.htm) |
| Remote seller threshold | Direct Arizona retail sales (not through a marketplace facilitator) over $100,000 in the previous or current calendar year | [A.R.S. 42-5044(A)(1)(c)](https://www.azleg.gov/ars/42/05044.htm) |
| Marketplace facilitator threshold | Arizona retail sales, own and facilitated, over $100,000 | [A.R.S. 42-5044(A)(2)](https://www.azleg.gov/ars/42/05044.htm) |
| Licence fee | $12 per location | [ADOR TPT page](https://azdor.gov/business/transaction-privilege-tax) |
| Filing frequency | Annual: estimated annual liability under $2,000; quarterly: $2,000 to $8,000; monthly otherwise | [A.R.S. 42-5014(A), (B)](https://www.azleg.gov/ars/42/05014.htm) |
| Due date | The 20th of the month after the period | [A.R.S. 42-5014(A)(1)](https://www.azleg.gov/ars/42/05014.htm) |
| June estimated payment | Required if prior-year total TPT liability was $4,100,000 or more (2023 on); due 20 June | [A.R.S. 42-5014(D)](https://www.azleg.gov/ars/42/05014.htm) |
| Electronic filing required | Prior-year total liability of $500 or more | [A.R.S. 42-5014(P)](https://www.azleg.gov/ars/42/05014.htm) |
| Accounting credit (state tax only, timely paid) | Paper: 1% of tax, up to $10,000 a year; electronic: 1.2%, up to $12,000 a year | [A.R.S. 42-5017(A)](https://www.azleg.gov/ars/42/05017.htm) |

### Step 1: is the activity taxable, and in which classification?

TPT is levied on the seller under [A.R.S. 42-5008](https://www.azleg.gov/ars/42/05008.htm) by classification. Sales of tangible personal property are retail; meals are restaurant; renting equipment is personal property rental; hotels are transient lodging; building is prime contracting. Professional and personal services are generally not a classification and not taxed. Food for home consumption is exempt from the state retail tax, but some cities tax it (the ADOR tables list it as code 062 where a city does). Software and digital products are fact-specific: refer (R-AZ-TPT-4).

### Step 2: is the seller required to be licensed?

An Arizona location, employees or inventory in Arizona require a licence. A remote seller with no physical presence licenses once direct Arizona retail sales (excluding sales through a marketplace facilitator) pass $100,000 in the current or previous year, with affiliates aggregated (42-5044(B)). If the threshold is first crossed during the year, the seller licenses then and begins remitting on the first day of the month starting at least 30 days later (42-5044(C)). Marketplace facilitators report facilitated sales under their own licence.

### Step 3: the tax base

Gross receipts of the classification, less deductions (resale on a valid Form 5000A, exempt sales, out-of-state sales). TPT the seller passes on to the customer may be excluded from the base only when separately stated; otherwise use ADOR's factored rate to back the tax out. For prime contracting, the base is 65% of gross receipts (A.R.S. 42-5075(B)).

### Step 4: rate by location

Apply the combined state and county rate (Table 1) and the city rate (Table 2) for the region code where the sale is sourced. In-state sellers source most retail sales to their business location; remote sellers use the separate Remote Seller and Marketplace Facilitator rate tables, sourced to the customer's location. Rates change during the year: use the table in force for the period filed.

### Step 5: credit and return

Total the tax by classification and region on the TPT-2 (or TPT-EZ for simple single-location filers), deduct the accounting credit on the state tax only if filing and paying on time, and pay by the 20th.

### Prime contracting against MRRA

Prime contracting covers new construction and modification of real property. Maintenance, repair, replacement or alteration (MRRA) of existing property is not prime contracting: the contractor pays TPT (or use tax) to its supplier on materials and does not charge prime contracting TPT on the job. Where a city taxes MRRA, the ADOR table shows it as code 315 (Phoenix and Tucson both list it). A subcontractor working under a prime who is liable for the tax is not taxed on that job (42-5075(D)); the prime gives the subcontractor Form 5005.

### Use tax

Use tax at 5.6% (state; cities may add their own) applies to tangible personal property stored, used or consumed in Arizona where the seller charged no Arizona TPT, where goods bought for resale are used, or where another state's tax was lower than Arizona's (ADOR TPT page). A licensed business reports it on the TPT-2 under code 029.

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Customer refuses to pay the TPT line on an invoice | The seller still owes the tax; TPT is the seller's own tax |
| Remote seller, $90,000 direct and $40,000 marketplace sales to Arizona in 2026, under $100,000 direct in 2025 | No licence needed: only direct sales count toward the remote seller threshold |
| Remote seller crosses $100,000 of direct sales in August 2026 | License then; begin collecting on the first day of the month starting at least 30 days later; keep collecting for the rest of 2026 and all of 2027 |
| Seller absorbs the tax and charges a tax-inclusive price | Back out TPT with the factored rate; base excludes the tax only if separately stated |
| New house built under contract | Prime contracting: tax on 65% of the contract |
| Bathroom remodel, roof replacement, repainting | MRRA: no prime contracting TPT; tax paid on materials at purchase |
| Contract mixes an addition (prime) and a remodel (MRRA) | Split the contract; refer if the split is not documented (R-AZ-TPT-1) |
| Subcontractor under a liable prime | Not taxed on that job with Form 5005 from the prime |
| Groceries sold in Arizona | State retail exempt; check the city table for code 062 |
| Several locations | Licence and report each location ($12 each) or take a consolidated licence |
| Seller under 19 with gross income up to $10,000 a year | No TPT licence needed from 14 September 2024 (A.R.S. 42-5045, ADOR TPT page) |
| Business inside the Maricopa County Stadium District | Report under county region MCZ and city region PZ (ADOR TPT page) |
| Paying late | The accounting credit is lost for that period (42-5017(C)) |

### Defaults when a fact is missing

| Missing fact | Default |
| --- | --- |
| City of the sale | Do not compute the city layer; ask |
| Filing frequency | Use ADOR's assigned frequency; if none, apply the 42-5014 bands to expected annual liability |
| Whether a contract is prime or MRRA | Do not compute; ask for the scope of work |
| Rate table date | Use the table in force for the period filed |

### Red flags to raise with the client

| Flag | Why |
| --- | --- |
| Out-of-state seller counting marketplace sales toward the $100,000 threshold | Only direct sales count for a remote seller |
| Contractor charging prime contracting TPT on repair work | MRRA is not prime contracting |
| Prime contractor taxing 100% of the contract | Base is 65% |
| Filing on the 25th or later | Due on the 20th |
| TPT netted out of gross receipts on the federal return | TPT is the seller's own tax; gross receipts include amounts collected, and TPT paid is a business tax expense |
| Old rates (Phoenix 2.30%) in the point-of-sale system | Phoenix retail is 2.80% in the October 2026 tables |
| Activity on a reservation | Tribal region codes apply and federal preemption may; refer |

## Worked cases

**Case 1, a Phoenix retailer's monthly return.** A shop in Phoenix sells $10,000 of taxable goods in October 2026 and files electronically on time. Combined rate: 6.30% (state and Maricopa) plus 2.80% (Phoenix) = 9.10%. Tax: $910.00. Accounting credit on the state tax only: $10,000 x 5.6% = $560 of state tax, x 1.2% = $6.72 (the ADOR table shows this as an electronic-filer credit rate of .0672% of the base). Net payable: $903.28.

```oa-check
name: AZ 2026 Phoenix retail TPT with electronic accounting credit
inputs:
  sales: 10000
  state_county_rate: 0.063
  city_rate: 0.028
  state_rate: 0.056
  credit_rate: 0.012
steps:
  - tax: sales * (state_county_rate + city_rate)
  - credit: sales * state_rate * credit_rate
  - net: tax - credit
expected:
  tax: 910.00
  credit: 6.72
  net: 903.28
```

**Case 2, a decision: prime contracting or MRRA?** A Phoenix contractor has two jobs of $200,000 each: a new house built under a contract with the owner, and a full remodel of an existing house with no change to its footprint. The new house is prime contracting: base $200,000 x 65% = $130,000; tax at 9.10% = $11,830.00, less an electronic accounting credit on the state part of $130,000 x 5.6% x 1.2% = $87.36. The remodel is MRRA: no prime contracting TPT on the $200,000; the contractor pays TPT to suppliers on its materials. Decision: report the new house under code 015 on the TPT-2 and do not report the remodel as prime contracting; keep the scope of work on file to support the MRRA treatment.

```oa-check
name: AZ 2026 Phoenix prime contracting on a new house against an MRRA remodel
inputs:
  new_build: 200000
  remodel: 200000
  base_share: 0.65
  combined_rate: 0.091
  state_rate: 0.056
  credit_rate: 0.012
steps:
  - base: new_build * base_share
  - tax_new_build: base * combined_rate
  - credit: base * state_rate * credit_rate
  - tax_remodel: remodel * 0
expected:
  base: 130000.00
  tax_new_build: 11830.00
  credit: 87.36
  tax_remodel: 0.00
```

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-AZ-TPT-1 | A contract mixing prime contracting and MRRA work with no documented split | Refer; fact-intensive |
| R-AZ-TPT-2 | Activity on tribal land or sales to enrolled members on a reservation | Refer; federal preemption analysis |
| R-AZ-TPT-3 | Mining severance or metalliferous mining computation | Refer |
| R-AZ-TPT-4 | Whether software, a digital product or a remotely accessed service is taxable (state or city) | Refer; ask for a private taxpayer ruling if material |
| R-AZ-TPT-5 | Marketplace facilitator against seller responsibility when the facts are unclear | Refer |
| R-AZ-TPT-6 | Speculative builder, owner-builder or other city-only taxes | Refer to the city tax rules |
| R-AZ-TPT-7 | Audit, voluntary disclosure or protest | Refer to an Arizona-licensed practitioner |

## Filing and payment

1. **Licence.** Apply on the Joint Tax Application (JT-1) through AZTaxes.gov, which also opens withholding and unemployment accounts ($12 per location; some cities add their own fee).
2. **Return.** TPT-2 (or TPT-EZ) through AZTaxes.gov, one return covering state, county and city tax, each line with a business (class) code and a region code. Electronic filing is required at $500 or more of prior-year liability.
3. **When.** By the 20th of the month after the month, quarter (20 April, 20 July, 20 October, 20 January) or year (20 January). A business with $4,100,000 or more of prior-year liability also pays a June estimate by 20 June.
4. **Credit.** Take the accounting credit (1.2% electronic, 1% paper, on the state tax) only when paying on time.
5. **After filing.** ADOR distributes the city and county share; a city may still audit. Amend by filing a corrected TPT-2 for the period.

## Completion checklist

- Every activity placed in a classification, with its business code.
- Every sale coded to the right region (city and county).
- Rate table in force for the period used.
- Remote seller threshold tested on direct sales only.
- Prime contracting on 65%; MRRA left out; Form 5005 on file for subcontracts.
- Use tax on untaxed purchases reported under code 029.
- Accounting credit on the state portion only, and only when timely.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| ADOR, Transaction Privilege and Other Tax Rate Tables, effective 1 October 2026. Read for Table 1 (combined state and county rates by class and county: retail 017 Maricopa 6.30%, Pima 6.10%; transient lodging 025 Maricopa 7.27%; use tax 029 5.60%; accounting credit rates .056% / .0672%) and Table 2 (Phoenix PX 2.80%, single-item over $14,338 2.00%; Tucson TU 2.60%, hotels 9.00%). | https://azdor.gov/sites/default/files/document/TPT_RATETABLE_10012026.pdf | 2026-11-13 |
| ADOR, Transaction Privilege Tax. Read for "a tax on a vendor for the privilege of doing business", the $12 licence per location, use tax cases, the under-19 rule and the Stadium District codes. | https://azdor.gov/business/transaction-privilege-tax | 2026-11-13 |
| A.R.S. 42-5010. Read for the 5%, 5.5%, 3.125% and 0% rates by classification. | https://www.azleg.gov/ars/42/05010.htm | 2026-11-13 |
| A.R.S. 42-5010.01. Read for the additional 0.6% from 1 July 2021 to 30 June 2041. | https://www.azleg.gov/ars/42/05010-01.htm | 2026-11-13 |
| A.R.S. 42-5008. Read for the levy on persons by business classification. | https://www.azleg.gov/ars/42/05008.htm | 2026-11-13 |
| A.R.S. 42-5014. Read for the 20th, the $2,000 / $8,000 bands, the $4,100,000 June estimate and the $500 electronic filing line. | https://www.azleg.gov/ars/42/05014.htm | 2026-11-13 |
| A.R.S. 42-5017. Read for the 1% / $10,000 and 1.2% / $12,000 accounting credit. | https://www.azleg.gov/ars/42/05017.htm | 2026-11-13 |
| A.R.S. 42-5044. Read for the $100,000 remote seller and marketplace facilitator thresholds, aggregation and the start date. | https://www.azleg.gov/ars/42/05044.htm | 2026-11-13 |
| A.R.S. 42-5075. Read for the 65% base, the subcontractor rule in (D) and the modification definition. | https://www.azleg.gov/ars/42/05075.htm | 2026-11-13 |

Not yet confirmed: rate changes after 1 October 2026 (check the latest ADOR table for each period); the remote seller and marketplace facilitator rate tables for 2026 were not opened; the exact line layout of the 2026 TPT-2; the A.R.S. 42-5040 sourcing text and the A.R.S. 42-5061 retail exemptions list were not re-read for this version.
