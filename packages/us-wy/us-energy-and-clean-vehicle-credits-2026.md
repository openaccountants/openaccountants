---
name: us-energy-and-clean-vehicle-credits-2026
description: What the One Big Beautiful Bill Act (Public Law 119-21) ended for individual US taxpayers, and when, and what is still claimable on a 2026 Form 1040. Covers the new clean vehicle credit (section 30D) and the previously-owned clean vehicle credit (section 25E), both ended for vehicles acquired after 30 September 2025, with the IRS meaning of "acquired" (a written binding contract plus a payment); the energy efficient home improvement credit (section 25C), ended for property placed in service after 31 December 2025; the residential clean energy credit (section 25D), ended for expenditures made after 31 December 2025, with its carryforward of unused credit into 2026; and the alternative fuel vehicle refueling property credit (section 30C), ended for property placed in service after 30 June 2026. Business-side credits (45W, 45L, 179D, 45Y, 48E) are pointers only. Trigger on "EV credit 2026", "clean vehicle credit", "solar credit 2026", "Form 5695 2026", "Form 8936", "home charger credit", "Form 8911", "energy credit carryforward", "did the OBBBA end the energy credits". Federal only.
version: "1.0"
jurisdiction: US
tax_year: 2026
last_updated: 2026-11-13
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: situation-rules
---

# US energy and clean vehicle credits after the One Big Beautiful Bill Act, tax year 2026

> **Source-cited draft.** Built from Public Law 119-21 sections 70501 to 70509, IRS Fact Sheet FS-2025-05, the IRS clean vehicle credits page, the 2025 Instructions for Form 5695, the Instructions for Form 8936 (2025) and Form 8911 (Rev. December 2025), and 26 U.S.C. 25C, 25D, 25E, 30C and 30D, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** For a 2026 Form 1040, the household energy and EV credits are mostly gone. No new or used clean vehicle credit for a vehicle **acquired after 30 September 2025** (acquired means a written binding contract was signed and a payment made). A vehicle acquired by that date but delivered in 2026 still qualifies, in 2026. No energy efficient home improvement credit for anything **placed in service after 31 December 2025**. No residential clean energy credit (solar, batteries, geothermal) for any expenditure **made after 31 December 2025**, and an expenditure is made when installation is completed, so a 2025 payment for a 2026 installation gets nothing. Unused residential clean energy credit from 2025 still **carries forward** into 2026. A home EV charger still earns the alternative fuel vehicle refueling property credit if **placed in service by 30 June 2026** in an eligible census tract.

## Scope and who this is for

In scope: an individual's 2026 Form 1040 claim (or non-claim) for sections 30D, 25E, 25C, 25D and 30C, the end dates, the carryforward of 25D credit, and what to tell a client who bought or installed something in late 2025 or in 2026.

Out of scope, and where it goes:

| Topic | Skill or pointer |
| --- | --- |
| The whole 2026 return, the standard deduction, credits order | `us-federal-income-tax-return-1040` |
| Summary of every 2026 change | `us-2026-federal-tax-changes` |
| Qualified commercial clean vehicle credit (45W), ended for vehicles acquired after 30 September 2025 | Pointer only: a business credit on Form 8936 and Form 3800 |
| New energy efficient home credit for builders (45L), ended for homes acquired after 30 June 2026 | Pointer only: builder's general business credit |
| Energy efficient commercial buildings deduction (179D), ended for construction beginning after 30 June 2026 | Pointer only: Schedule C line 27a via Form 7205, see `us-schedule-c-and-se-computation` |
| Clean electricity production and investment credits (45Y, 48E) for wind and solar facilities | Pointer only: business and utility-scale; Public Law 119-21 section 70512 and following |
| Depreciation of business energy property | `us-section-179-and-bonus-depreciation` |
| The car loan interest deduction (new for 2025 to 2028) | `us-new-deductions-tips-overtime-senior-car-loan` |

## Ask the client first

1. **Vehicle:** the date the purchase contract was signed, the date and amount of the first payment (a nominal deposit or a trade-in counts), and the date the client took possession. Did the dealer transfer the credit at the time of sale (a price cut or cash), and did the dealer give a time-of-sale report?
2. **Vehicle type and price:** new or used, the manufacturer's suggested retail price (new) or sale price (used), and whether used for business.
3. **Modified adjusted gross income** for 2025 and for 2026, and filing status (the clean vehicle credits use the lower of the two years).
4. **Home improvements and solar:** what was installed, at which home, and the date installation was **completed** (not the date paid). For a new build, the date the client first lived in it.
5. **2025 Form 5695:** any unused residential clean energy credit on line 16 to carry to 2026.
6. **EV charger:** date placed in service, cost, whether at the main home, and the 11-digit census tract of the address.
7. **Expected 2026 income tax** before these credits: all of these personal credits are nonrefundable.

## The method, step by step

### Rates, bands and thresholds

| Item | Amount or date | Source |
| --- | --- | --- |
| New clean vehicle credit (30D): no credit for a vehicle acquired after | 30 September 2025 | [Public Law 119-21, section 70502](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| Previously-owned clean vehicle credit (25E): no credit for a vehicle acquired after | 30 September 2025 | [Public Law 119-21, section 70501](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| Meaning of "acquired" for 25E, 30D and 45W | written binding contract entered into and a payment made (a nominal down payment or a trade-in counts) | [IRS FS-2025-05, question 2](https://www.irs.gov/newsroom/faqs-for-modification-of-sections-25c-25d-25e-30c-30d-45l-45w-and-179d-under-public-law-119-21-139-stat-72-july-4-2025-commonly-known-as-the-one-big-beautiful-bill-obbb) |
| New clean vehicle credit, critical minerals part and battery components part | USD 3,750 each (USD 7,500 together) | [26 U.S.C. 30D(b)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partIV-subpartB-sec30D.htm) |
| New clean vehicle MSRP limit, vans, SUVs, pickups | USD 80,000 | [26 U.S.C. 30D(f)(11)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partIV-subpartB-sec30D.htm) |
| New clean vehicle MSRP limit, other vehicles | USD 55,000 | [26 U.S.C. 30D(f)(11)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partIV-subpartB-sec30D.htm) |
| New clean vehicle MAGI limit, joint or surviving spouse | USD 300,000 | [26 U.S.C. 30D(f)(10)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partIV-subpartB-sec30D.htm) |
| New clean vehicle MAGI limit, head of household | USD 225,000 | [26 U.S.C. 30D(f)(10)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partIV-subpartB-sec30D.htm) |
| New clean vehicle MAGI limit, other filers | USD 150,000 | [26 U.S.C. 30D(f)(10)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partIV-subpartB-sec30D.htm) |
| Previously-owned clean vehicle credit | lesser of USD 4,000 or 30 percent of the sale price | [26 U.S.C. 25E(a)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partIV-subpartA-sec25E.htm) |
| Previously-owned clean vehicle MAGI limit, joint or surviving spouse / head of household / other | USD 150,000 / USD 112,500 / USD 75,000 | [26 U.S.C. 25E(b)(2)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partIV-subpartA-sec25E.htm) |
| Energy efficient home improvement credit (25C): no credit for property placed in service after | 31 December 2025 | [Public Law 119-21, section 70505](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| Residential clean energy credit (25D): no credit for expenditures made after | 31 December 2025 | [Public Law 119-21, section 70506](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| Residential clean energy credit rate, last year it applies (2025) | 30% | [2025 Instructions for Form 5695](https://www.irs.gov/pub/irs-pdf/i5695.pdf) |
| Alternative fuel vehicle refueling property credit (30C): no credit for property placed in service after | 30 June 2026 | [Public Law 119-21, section 70504](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| 30C credit rate, non-depreciable (home) property | 30 percent | [26 U.S.C. 30C(a)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partIV-subpartB-sec30C.htm) |
| 30C limit per item, non-depreciable (home) property | USD 1,000 | [26 U.S.C. 30C(b)(2)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partIV-subpartB-sec30C.htm) |

None of the dollar amounts above is indexed. Public Law 119-21 changed only the end dates (and 25D's rate schedule after 2025), so the 2024 edition of the Code still states the amounts correctly.

### Step 1: vehicles (30D new, 25E used)

1. **Was the vehicle acquired on or before 30 September 2025?** Acquired = written binding contract plus a payment. If not, stop: no credit, whenever delivered. Source: [IRS clean vehicle tax credits](https://www.irs.gov/clean-vehicle-tax-credits).
2. **Which year?** The credit is claimed for the year the vehicle is **placed in service**, which is when the buyer takes possession. A vehicle acquired by 30 September 2025 and delivered in 2026 is a 2026 credit. Source: [IRS clean vehicle tax credits](https://www.irs.gov/clean-vehicle-tax-credits).
3. **Seller report.** The seller must give the buyer the time-of-sale information and file the report through Energy Credits Online; without it the vehicle is not eligible. New registrations on that portal closed on 30 September 2025, but previously registered dealers can still submit reports. Source: [IRS FS-2025-05, question 5](https://www.irs.gov/newsroom/faqs-for-modification-of-sections-25c-25d-25e-30c-30d-45l-45w-and-179d-under-public-law-119-21-139-stat-72-july-4-2025-commonly-known-as-the-one-big-beautiful-bill-obbb).
4. **Limits.** New: MSRP limit and MAGI limit from the table; MAGI is the **lesser** of the current or preceding year's (2026 or 2025 for a 2026 delivery). Used: MAGI limit from the table, also the lesser of the two years. Source: [26 U.S.C. 30D(f)(10)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partIV-subpartB-sec30D.htm), [26 U.S.C. 25E(b)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partIV-subpartA-sec25E.htm).
5. **Personal or business.** The business-use part is a general business credit (Form 3800, carries back and forward). The personal part is a nonrefundable personal credit with no carryforward: what tax cannot absorb is lost. Source: [26 U.S.C. 30D(c)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partIV-subpartB-sec30D.htm).
6. **Transfer to the dealer.** The buyer may elect at the time of sale (when taking possession) to transfer the credit to a registered dealer for an immediate price cut or payment. The election is made at the time of sale, not at contract. If the buyer's MAGI turns out over the limit, the amount received is added back to the buyer's tax. File Form 8936 and Schedule A (Form 8936) either way. Sources: [IRS FS-2025-05, question 4](https://www.irs.gov/newsroom/faqs-for-modification-of-sections-25c-25d-25e-30c-30d-45l-45w-and-179d-under-public-law-119-21-139-stat-72-july-4-2025-commonly-known-as-the-one-big-beautiful-bill-obbb), [26 U.S.C. 30D(g)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partIV-subpartB-sec30D.htm), [Instructions for Form 8936 (2025)](https://www.irs.gov/pub/irs-pdf/i8936.pdf).

### Step 2: home improvements (25C)

7. **Nothing placed in service in 2026 qualifies.** Windows, doors, insulation, heat pumps, water heaters, panel upgrades and home energy audits: if installation was completed after 31 December 2025, no credit. Source: [IRS FS-2025-05, question 1](https://www.irs.gov/newsroom/faqs-for-modification-of-sections-25c-25d-25e-30c-30d-45l-45w-and-179d-under-public-law-119-21-139-stat-72-july-4-2025-commonly-known-as-the-one-big-beautiful-bill-obbb).
8. **No carryforward.** 25C has no carryforward provision, so any 2025 25C credit not used against 2025 tax is lost; nothing reaches 2026. Source: [26 U.S.C. 25C](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partIV-subpartA-sec25C.htm) (no carryforward subsection, unlike 25D(c)).

### Step 3: solar, batteries, geothermal, small wind, fuel cells (25D)

9. **No new 2026 credit.** An expenditure is treated as made when the original installation is completed (for a new build, when the taxpayer's original use of the home begins). Paying in 2025 does not help if installation finished in 2026. Source: [IRS FS-2025-05, question 7](https://www.irs.gov/newsroom/faqs-for-modification-of-sections-25c-25d-25e-30c-30d-45l-45w-and-179d-under-public-law-119-21-139-stat-72-july-4-2025-commonly-known-as-the-one-big-beautiful-bill-obbb).
10. **The carryforward survives.** Any 25D credit that exceeded the 2025 tax liability limit (2025 Form 5695, line 16) carries to 2026 and is added to the 2026 credit. Public Law 119-21 did not repeal 25D(c). Sources: [26 U.S.C. 25D(c)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partIV-subpartA-sec25D.htm), [2025 Instructions for Form 5695, line 16](https://www.irs.gov/pub/irs-pdf/i5695.pdf).
11. **Use in 2026** = the smaller of the carryforward and the 2026 tax after the credits ordered ahead of it. Anything still unused carries on to 2027.

### Step 4: home EV charger (30C)

12. **Placed in service by 30 June 2026**, at the main home, in an eligible census tract (a low-income community tract or one that is not an urban area; check the 11-digit census tract GEOID). Source: [Instructions for Form 8911 (Rev. December 2025)](https://www.irs.gov/pub/irs-pdf/i8911.pdf), [26 U.S.C. 30C(c)(3)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partIV-subpartB-sec30C.htm).
13. **Credit** = 30 percent of cost, up to USD 1,000 per item, on Form 8911. Placed in service on or after 1 July 2026: nothing.

### Business-side credits (pointers only)

45W commercial clean vehicles ended for vehicles acquired after 30 September 2025 (section 70503); 45L new energy efficient homes ends for homes acquired after 30 June 2026 (section 70508); 179D ends for property whose construction begins after 30 June 2026 (section 70507); 45Y and 48E wind and solar facilities have their own placed-in-service and construction-start rules (sections 70512 and 70513). Refer these.

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| EV contract and deposit on 25 September 2025, delivery January 2026 | Qualifies, as a 2026 credit (if seller report and limits are met) |
| EV contract signed 25 September 2025, no payment until October 2025 | Not acquired by 30 September 2025: no credit |
| EV ordered online, refundable reservation fee only, no binding contract | Not acquired: no credit (ask for the contract) |
| Leased EV | No 30D credit for the lessee; the lessor may have claimed 45W if acquired by 30 September 2025 |
| Solar paid in full December 2025, installation completed February 2026 | No 25D credit (expenditure made in 2026) |
| Solar installed 2025, credit larger than 2025 tax | Carry the excess to 2026 (and onward) |
| Heat pump installed December 2025 | 2025 25C credit only; nothing in 2026; no carryforward |
| Heat pump installed January 2026 | No credit |
| Home EV charger placed in service 15 June 2026, eligible tract | 30C credit, 30% up to USD 1,000 |
| Home EV charger placed in service 2 July 2026 | No credit |
| Credit transferred to the dealer, MAGI later over the limit | Repay: the transferred amount is added to the 2026 tax |

### Defaults when a fact is missing

| Missing fact | Default, and flag it |
| --- | --- |
| Date of the first payment on a vehicle | No credit until the contract and payment record are seen |
| Installation completion date | Use the final invoice or permit sign-off date; no credit if it is in 2026 |
| 2025 Form 5695 | Carryforward zero until the 2025 Form 5695 line 16 is seen |
| Census tract of the charger address | No 30C credit until the tract is checked |
| Seller time-of-sale report | No vehicle credit without it |

### Red flags to raise with the client

| Flag | Why it matters |
| --- | --- |
| Vehicle delivered after 30 September 2025 | Prove acquisition date with the contract and payment |
| Solar or battery contracts signed late 2025 | Installation date decides; many finished in 2026 |
| Software suggests a 2026 Form 5695 credit for 2026 work | Wrong: only the 2025 carryforward is allowed |
| MAGI near the vehicle limit in both 2025 and 2026 | A transferred credit may have to be repaid |

## Worked cases

**Case 1, the 25D carryforward.** A single filer had solar panels installed and completed in October 2025 for USD 40,000. The 2025 credit was 30% = USD 12,000, but the 2025 tax liability limit (Form 5695 line 14) was USD 7,000, so USD 5,000 carried to 2026 on line 16. In February 2026 she added a home battery for USD 15,000: installation completed in 2026, so no credit. Her 2026 tax after the credits ordered ahead of 25D is USD 9,000. She uses the full USD 5,000 carryforward; tax falls to USD 4,000 and nothing carries to 2027.

```oa-check
name: 25D carryforward used in 2026
inputs:
  solar_cost_2025: 40000
  limit_2025: 7000
  new_25d_credit_2026: 0
  tax_2026_before_25d: 9000
steps:
  - credit_2025: solar_cost_2025 * 0.30
  - carry_to_2026: max(credit_2025 - limit_2025, 0)
  - used_2026: min(carry_to_2026 + new_25d_credit_2026, tax_2026_before_25d)
  - tax_after: tax_2026_before_25d - used_2026
  - carry_to_2027: carry_to_2026 + new_25d_credit_2026 - used_2026
expected:
  credit_2025: 12000.00
  carry_to_2026: 5000.00
  used_2026: 5000.00
  tax_after: 4000.00
  carry_to_2027: 0.00
```

**Case 2, a decision: transfer the EV credit to the dealer or claim it on the return?** A single buyer signed a binding contract and paid a USD 1,000 deposit on 20 September 2025 for a new EV car with an MSRP of USD 45,000 (under the USD 55,000 limit) that meets both requirements (USD 3,750 + USD 3,750). Delivery is 10 January 2026. MAGI was USD 160,000 in 2025 and is expected to be USD 140,000 in 2026: the lesser, USD 140,000, is under USD 150,000, so he qualifies. His expected 2026 income tax is USD 6,000. Claimed on the return, the personal credit is nonrefundable with no carryforward, so only USD 6,000 is used and USD 1,500 is lost. Transferred to a registered dealer at delivery, he gets the full USD 7,500 off the price. Transfer wins by USD 1,500, provided the dealer is registered and files the time-of-sale report, and he accepts that if 2026 MAGI (and 2025 MAGI) both end up over USD 150,000 he repays the USD 7,500. If his 2026 tax were USD 7,500 or more, the two routes would give the same credit and only timing would differ.

```oa-check
name: EV credit, transfer at sale against claim on the return (2026)
inputs:
  minerals_part: 3750
  battery_part: 3750
  msrp: 45000
  msrp_limit: 55000
  magi_2025: 160000
  magi_2026: 140000
  magi_limit: 150000
  tax_2026: 6000
steps:
  - credit: minerals_part + battery_part
  - magi_tested: min(magi_2025, magi_2026)
  - magi_headroom: magi_limit - magi_tested
  - msrp_headroom: msrp_limit - msrp
  - claimed_on_return: min(credit, tax_2026)
  - transferred: credit
  - transfer_advantage: transferred - claimed_on_return
expected:
  credit: 7500.00
  magi_tested: 140000.00
  magi_headroom: 10000.00
  msrp_headroom: 10000.00
  claimed_on_return: 6000.00
  transferred: 7500.00
  transfer_advantage: 1500.00
```

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-EN-BIZ | 45W, 45L, 179D, 45Y, 48E or any business energy credit | Refer: business credits, Form 3800 |
| R-EN-ACQ | Acquisition date cannot be documented | Do not claim; ask for the contract and payment proof |
| R-EN-LEASE | Lessee asks for the vehicle credit | No 30D for the lessee; refer the lessor question |
| R-EN-RECAPTURE | Dealer transfer and MAGI over the limit in both years | Compute the add-back; refer if disputed |
| R-EN-NEWBUILD | 25D on a new home where original use began around year end | Refer: date of original use decides |

## Filing and payment

Form 8936 with Schedule A (Form 8936) for a 2026 vehicle credit (required even if transferred to the dealer); Form 5695 for the 25D carryforward; Form 8911 for a home charger. All attach to the 2026 Form 1040, due 15 April 2027. The full return order is in `us-federal-income-tax-return-1040`.

## Completion checklist

- Vehicle: contract date, payment date and possession date on file; seller report seen; MSRP and MAGI limits checked with the lower of 2025 and 2026 MAGI.
- No 25C or new 25D credit claimed for anything completed in 2026.
- 2025 Form 5695 line 16 carried to 2026; any remaining excess recorded for 2027.
- Charger: placed-in-service date on or before 30 June 2026, census tract checked.
- Business energy credits referred.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Public Law 119-21 (One Big Beautiful Bill Act). Read for sections 70501 (25E, 30 September 2025), 70502 (30D, acquired after 30 September 2025), 70503 (45W), 70504 (30C, 30 June 2026), 70505 (25C, placed in service after 31 December 2025), 70506 (25D, expenditures made after 31 December 2025), 70507 (179D), 70508 (45L). | https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm | 2026-11-13 |
| IRS FS-2025-05, FAQs on sections 25C, 25D, 25E, 30C, 30D, 45L, 45W and 179D under Public Law 119-21. Read for the termination table (Q1), the meaning of "acquired" (Q2), transfer election at sale (Q4), Energy Credits Online (Q5) and 25D installation timing (Q7). | https://www.irs.gov/newsroom/faqs-for-modification-of-sections-25c-25d-25e-30c-30d-45l-45w-and-179d-under-public-law-119-21-139-stat-72-july-4-2025-commonly-known-as-the-one-big-beautiful-bill-obbb | 2026-11-13 |
| IRS clean vehicle tax credits page. Read for placed in service after 30 September 2025 requires acquisition by that date, and possession as placed in service. | https://www.irs.gov/clean-vehicle-tax-credits | 2026-11-13 |
| 2025 Instructions for Form 5695. Read for What's New (termination), the 30% rate for 2022 to 2025, and line 16 carry to 2026. | https://www.irs.gov/pub/irs-pdf/i5695.pdf | 2026-11-13 |
| Instructions for Form 8936 (2025). Read for "acquired" and filing Schedule A when the credit is transferred. | https://www.irs.gov/pub/irs-pdf/i8936.pdf | 2026-11-13 |
| Instructions for Form 8911 (Rev. December 2025). Read for the 30 June 2026 termination and the census tract check. | https://www.irs.gov/pub/irs-pdf/i8911.pdf | 2026-11-13 |
| 26 U.S.C. 30D (govinfo). Read for (b) USD 3,750 parts, (c) personal and business credit, (f)(10) MAGI limits, (f)(11) MSRP limits, (g) transfer and add-back. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partIV-subpartB-sec30D.htm | 2026-11-13 |
| 26 U.S.C. 25E (govinfo). Read for (a) USD 4,000 or 30 percent and (b) MAGI limits. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partIV-subpartA-sec25E.htm | 2026-11-13 |
| 26 U.S.C. 25C (govinfo). Read for the absence of a carryforward. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partIV-subpartA-sec25C.htm | 2026-11-13 |
| 26 U.S.C. 25D (govinfo). Read for (c) carryforward of unused credit. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partIV-subpartA-sec25D.htm | 2026-11-13 |
| 26 U.S.C. 30C (govinfo). Read for (a) 30 percent, (b)(2) USD 1,000 and (c)(3) eligible census tracts. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partIV-subpartB-sec30C.htm | 2026-11-13 |

Not yet confirmed: the 2026 Form 5695, Form 8936 and Form 8911 and their instructions were not published when read, so 2026 line numbers are not quoted; whether the IRS keeps a 2026 Form 5695 only for the 25D carryforward is assumed from 25D(c) and the 2025 instructions' "carry the unused portion of the residential clean energy credit to 2026".
