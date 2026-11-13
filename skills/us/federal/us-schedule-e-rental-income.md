---
name: us-schedule-e-rental-income
description: >
  Compute 2026 Schedule E Part I for an individual's residential or commercial rental real estate: rents, repairs, the split of land and building, straight-line depreciation over 27.5 years (residential) or 39 years (nonresidential) with the mid-month convention, the section 280A vacation-home tests, and the section 469 passive loss limit including the USD 25,000 active-participation allowance and Form 8582. Trigger on "Schedule E", "rental income", "vacation home", "27.5 year depreciation", "39 year property", "Form 8582", "passive loss allowance". Real estate professional status and the seven-day rental rule are in us-real-estate-professional-and-short-term-rentals. A rental of fewer than 15 days is in us-augusta-rule-home-rental-to-your-business. Federal only.
version: "1.0"
jurisdiction: US
category: federal
tax_year: 2026
last_updated: 2026-11-13
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
---

# Schedule E rental real estate, tax year 2026

> **Source-cited draft.** Built from 26 U.S.C. 168 and 469 (U.S. Code, 2024 edition, on govinfo.gov), Publication 527 (2025), Publication 925 (2025) for the point where the special allowance reaches zero, and the early-release draft Instructions for Schedule E (Form 1040) (2026), read on 2026-11-13. The draft is marked not for filing. No accountant has reviewed this skill. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** Report rent on Schedule E (Form 1040), Part I, not on Schedule C, unless the owner provides substantial services. Depreciate the building, never the land, on the straight-line method: **27.5 years** if the building is residential rental property, **39 years** if it is nonresidential real property, using the mid-month convention. A dwelling used as a home (personal use more than the greater of 14 days or 10 percent of the fair-rental days) cannot throw a rental loss against other income. Otherwise a rental loss is passive. A natural person who actively participates may use up to **USD 25,000** of rental real estate loss against non-passive income. That allowance is reduced by 50 percent of modified AGI over **USD 100,000** and is gone at **USD 150,000**.

## Scope and who this is for

In scope: one individual's Schedule E, Part I, for U.S. rental real estate in calendar year 2026, including depreciation of the building, the vacation-home limits in section 280A, and the passive-loss computation through the special allowance. A single-member domestic LLC that is disregarded reports on the owner's Schedule E.

Out of scope, and where it goes:

| Topic | Skill |
| --- | --- |
| Real estate professional tests, material participation, and the seven-day average-stay rule | `us-real-estate-professional-and-short-term-rentals` |
| Renting a dwelling for fewer than 15 days | `us-augusta-rule-home-rental-to-your-business` |
| Section 179 and bonus depreciation on personal property inside the unit | `us-section-179-and-bonus-depreciation` |
| Qualified business income deduction on the rental | `us-qbi-deduction` |
| A nonresident owner's section 871(d) election | `us-form-1040-nr-nonresident-return` |
| Sale of the property | `us-nonresident-cgt` for a nonresident; Form 4797 for a resident is not computed here |

## Ask the client first

1. **Each property:** address, residential or nonresidential, date placed in service, cost split between land and building, and prior depreciation allowed or allowable.
2. **Days in 2026:** days rented at a fair price, days of personal use (including family use and days rented below a fair price), and days the unit was available but empty.
3. **Who participates.** Does the owner (or spouse) approve tenants, set terms, or approve repairs, and do they own at least 10 percent? Is anyone claiming real estate professional status? If yes, stop and use `us-real-estate-professional-and-short-term-rentals`.
4. **Modified AGI** for the section 469(i) test, before the passive loss, and filing status. Married filing separately and living with the spouse at any time gets no special allowance.
5. **Amounts not at risk** (nonrecourse debt that is not qualified nonrecourse financing, guarantees). At-risk limits apply before the passive loss.
6. **Services.** Heat and light only (Schedule E), or substantial services such as a hotel (Schedule C)?

## The method, step by step

### Rates, bands and thresholds

| Item | Amount, 2026 | Source |
| --- | --- | --- |
| Residential rental property, recovery period, straight line | 27.5 years | [26 U.S.C. 168(c) and 168(b)(3)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVI-sec168.htm) |
| Nonresidential real property, recovery period, straight line | 39 years | [26 U.S.C. 168(c) and 168(b)(3)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVI-sec168.htm) |
| Convention for both real-property classes | mid-month | [26 U.S.C. 168(d)(2) and (d)(4)(B)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVI-sec168.htm) |
| Residential rental property test | 80 percent of gross rental income from dwelling units | [26 U.S.C. 168(e)(2)(A)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVI-sec168.htm) |
| Dwelling used as a home if personal use exceeds the greater of | 14 days, or 10 percent of fair-rental days | [Publication 527 (2025), chapter 5](https://www.irs.gov/publications/p527) |
| Rent excluded, and no rental deductions, if used as a home and rented | less than 15 days | [Publication 527 (2025), chapter 5](https://www.irs.gov/publications/p527) |
| Special allowance, active participation, single or joint | USD 25,000 | [26 U.S.C. 469(i)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapE-partII-subpartC-sec469.htm) |
| Special allowance starts to fall at modified AGI above | USD 100,000 | [26 U.S.C. 469(i)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapE-partII-subpartC-sec469.htm) |
| Reduction of the allowance per dollar over that start | 50 percent | [26 U.S.C. 469(i)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapE-partII-subpartC-sec469.htm) |
| Allowance fully gone at modified AGI of | USD 150,000 | [Publication 925 (2025)](https://www.irs.gov/pub/irs-pdf/p925.pdf) |
| Married filing separately, lived apart all year, maximum allowance | USD 12,500 | [26 U.S.C. 469(i)(5)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapE-partII-subpartC-sec469.htm) |

None of the statutory amounts is indexed. The 27.5-year and 39-year periods and the USD 25,000 allowance are the same for 2026 as in the Code edition read. Publication 527 (2025) is the latest final publication on irs.gov when read. The 2026 instructions exist only as an early-release draft.

### Income and expenses

1. **Rents.** Report rent received for real estate, including a room, on Schedule E, Part I. The early-release 2026 draft puts that income on line 3, one column per property. Do not use Schedule E for an activity that is not for profit, or where the owner provides substantial services (hotel-type services): those go on Schedule C. Source: [Publication 527 (2025), chapter 3](https://www.irs.gov/publications/p527) and the [2026 draft Instructions for Schedule E](https://www.irs.gov/pub/irs-dft/i1040se--dft.pdf).
2. **Repairs versus improvements.** Repairs that keep the property in operating condition (a broken lock, painting a room) are deducted. Improvements (a new HVAC system, substantial insulation) are capitalized and depreciated. The draft puts repairs on line 14 and says improvements go to the depreciation line.
3. **Other operating expenses** that are ordinary and necessary (insurance, utilities, management fees) go on the listed lines or on line 19 of the draft for amounts not listed on lines 5 through 18.
4. **Land is not depreciated.** Divide the purchase price between land and building by the ratio of fair market values at purchase. If those values are not known, the draft allows the assessed-value ratio used for real estate tax. Depreciate only the building portion.

### Depreciation

Residential rental property and nonresidential real property use the straight-line method, salvage value zero, and the mid-month convention. Property placed in service in any month is treated as placed in service on the midpoint of that month. For a building placed in service in January and held all year, that is 11.5 months of a full year: half of January plus February through December.

A full year of straight-line depreciation is the building's basis divided by 27.5 (residential) or 39 (nonresidential). The first-year deduction is that full-year amount times the months in service under the mid-month convention, divided by 12. Publication 527's Table 2-2d builds the same convention into a percentage. Its February, year-1 residential percentage is 3.182 percent: a USD 160,000 building placed in service on 8 February is USD 160,000 times 3.182 percent, which Publication 527 prints as USD 5,091.

The building is residential rental property for the year only if 80 percent or more of the gross rental income from the building is rental income from dwelling units. A unit in a hotel, motel, or other establishment where more than half the units are used on a transient basis is not a dwelling unit. If the test fails, the building is nonresidential real property (39 years) if it is section 1250 property. Appliances and other personal property are not the building: their recovery period and any bonus depreciation are in `us-section-179-and-bonus-depreciation`.

Publication 527 puts the depreciation deduction on Schedule E, line 18, and says Form 4562 is attached when it is required. The 2026 draft still directs depreciation to line 18.

### Vacation home (section 280A)

Divide expenses between rental use and personal use by days. Publication 527 uses a fraction: fair-rental days divided by fair-rental days plus personal-use days.

The unit is used as a home if personal use is more than the greater of 14 days or 10 percent of the days rented at a fair price. Personal use includes use by the owner, by a family member who does not use it as a main home at a fair rent, use under a reciprocal arrangement, and days rented below a fair price. A day rented at a fair price on which the owner also uses the unit counts as personal use, not as a rental day, for this test.

- **Used as a home and rented fewer than 15 days.** Do not report the rent and do not deduct rental expenses on Schedule E. See `us-augusta-rule-home-rental-to-your-business`.
- **Used as a home and rented 15 days or more.** Report the rent. If expenses exceed the rent, the excess does not offset other income. Publication 527 says this rental is not a passive activity. Operating expenses and then depreciation are allowed only up to the rent left after the expenses that are deductible anyway, and the rest carries forward. Use Worksheet 5-1 in Publication 527.
- **Personal use, but not used as a home.** Divide expenses, report the rent, and a rental loss is possible. Then apply the passive-loss limits.

### Passive loss and the USD 25,000 allowance

Apply limits in this order. The 2026 draft says: at-risk rules (Form 6198) first, then passive activity rules, then the excess business loss on Form 461. Form 461 does not change the Schedule E line. It adds any disallowed excess business loss to income on Schedule 1.

A rental activity is passive even if the owner works in it, unless the owner is a real estate professional who materially participates. That status is not computed here.

A natural person who actively participated may deduct rental real estate loss against non-passive income up to the allowance. Active participation is approving tenants, setting rental terms, or approving repairs, and the owner and spouse must own at least 10 percent for the whole period. The allowance is USD 25,000, reduced (not below zero) by 50 percent of the amount by which modified AGI exceeds USD 100,000. Publication 925 prints the result: the allowance is gone at modified AGI of USD 150,000 (USD 75,000 if married filing separately). A married person who files separately and lived with the spouse at any time during the year gets no allowance. A married person who files separately and lived apart all year uses USD 12,500 in place of USD 25,000 and USD 50,000 in place of USD 100,000.

The loss allowed is the smaller of the rental loss and the allowance that remains. The rest is suspended and carried forward. Run Form 8582 unless the instructions' exception for a small active-participation loss applies. The real estate professional computation, if it is in play, is on Schedule E line 43 in Publication 527's discussion, and the tests are in `us-real-estate-professional-and-short-term-rentals`.

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Land | Never depreciated. Split cost before computing the building basis |
| Building, 80 percent or more of gross rents from dwelling units | 27.5-year straight line, mid-month |
| Building that fails that test | 39-year straight line, mid-month, if it is nonresidential real property |
| Personal use above the 14-day or 10 percent test, rented 15 days or more | No rental loss against other income. Excess expenses carry forward |
| Personal use above that test, rented fewer than 15 days | Rent not reported. No Schedule E deductions |
| Personal use at or under the test | Loss allowed, then at-risk, then passive limits |
| Active participation, modified AGI USD 100,000 or below | Allowance USD 25,000 |
| Active participation, modified AGI USD 150,000 or more | Allowance zero. Loss is suspended unless there is other passive income |
| Married filing separately and lived together at any time | Allowance zero |
| Not at risk | Form 6198 before Form 8582 |
| Real estate professional who materially participates | Not this computation. Use the linked skill |

## Worked cases

**Case 1, a decision: stay under the vacation-home line, or go over it.** An unmarried owner, not a real estate professional, actively participates and owns 100 percent. Modified AGI before the rental loss is USD 120,000. The cottage is rented at a fair price for 200 days. Gross rent is USD 24,000. Rental-portion expenses, including depreciation, are USD 32,000, so the tentative rental loss is USD 8,000.

The home threshold is the greater of 14 days and 10 percent of 200 days, which is 20 days. At 10 personal days the cottage is not used as a home. The loss is passive. The allowance is USD 25,000 minus 50 percent of (USD 120,000 minus USD 100,000), which is USD 15,000. The deductible loss against other income is the smaller of USD 8,000 and USD 15,000, so USD 8,000.

At 30 personal days the cottage is used as a home (30 is more than 20) and it was rented more than 14 days. Publication 527 says that rental is not a passive activity and the excess of expenses over rent does not offset other income. The deductible loss against wages is zero, and the unused expenses carry forward on Worksheet 5-1. The figure that decides the year is USD 8,000 of loss allowed, or none. Staying at or under 20 personal days is what makes the allowance available.

```oa-check
name: Vacation home personal-use decision against the passive allowance (2026)
inputs:
  gross_rent: 24000
  rental_expenses: 32000
  fair_rental_days: 200
  magi: 120000
steps:
  - tentative_loss: rental_expenses - gross_rent
  - ten_percent_days: fair_rental_days * 0.10
  - home_threshold: max(14, ten_percent_days)
  - allowance: max(25000 - 0.5 * max(magi - 100000, 0), 0)
  - loss_if_not_a_home: min(tentative_loss, allowance)
  - loss_if_used_as_a_home: 0
expected:
  tentative_loss: 8000.00
  ten_percent_days: 20.00
  home_threshold: 20.00
  allowance: 15000.00
  loss_if_not_a_home: 8000.00
  loss_if_used_as_a_home: 0.00
```

**Case 2, January placement, residential, no personal use.** The owner buys a rental house and places it in service in January 2026. The contract allocates USD 330,000 to the building and the rest to land. It is residential rental property, held all year, with no personal use. Gross rents are USD 36,000. Operating expenses other than depreciation are USD 18,000. The owner is not asking about a passive loss, because the result is profit.

A full straight-line year is USD 330,000 divided by 27.5, which is USD 12,000. Mid-month for a January placement is 11.5 months. Depreciation is USD 12,000 times 11.5 divided by 12, which is USD 11,500. Schedule E net income is USD 36,000 minus USD 18,000 minus USD 11,500, which is USD 6,500. Enter depreciation on line 18. Land is not in the USD 330,000.

```oa-check
name: Residential rental placed in service in January, straight line mid-month (2026)
inputs:
  building_basis: 330000
  recovery_years: 27.5
  months_in_service: 11.5
  gross_rents: 36000
  other_expenses: 18000
steps:
  - full_year: building_basis / recovery_years
  - depreciation: full_year * months_in_service / 12
  - schedule_e_net: gross_rents - other_expenses - depreciation
expected:
  full_year: 12000.00
  depreciation: 11500.00
  schedule_e_net: 6500.00
```

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-E-REP | The owner may be a real estate professional, or the average stay is seven days or less | `us-real-estate-professional-and-short-term-rentals` |
| R-E-14 | Rented fewer than 15 days and used as a home | `us-augusta-rule-home-rental-to-your-business` |
| R-E-ATR | Part of the investment is not at risk | Form 6198 before this loss |
| R-E-163J | Business interest may be over the section 163(j) limit | Form 8990. Do not deduct the limited interest in full |
| R-E-HOTEL | Substantial services for guests | Schedule C, not Schedule E |
| R-E-K1 | The rental is inside a partnership or S corporation | Page 2 of Schedule E from the Schedule K-1, after basis. Not Part I |

## Filing and payment

Schedule E is attached to the owner's 2026 Form 1040, 1040-SR, or 1040-NR. It is not a separate return. The early-release draft says to use as many Schedules E as there are properties, and to fill lines 23a through 26 (the combined totals) on only one of them. Form 4562 is attached for depreciation of property placed in service in 2026. Form 8582 is attached when the passive-loss computation is required. Form 6198 comes before Form 8582 when the owner is not fully at risk.

The failure-to-file addition on the income-tax return is 5 percent of the tax per month or fraction, not over 25 percent, and the failure-to-pay addition is 0.5 percent per month or fraction, not over 25 percent, unless the failure is due to reasonable cause and not willful neglect. Source: [26 U.S.C. 6651(a)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapA-partI-sec6651.htm).

## Completion checklist

- Land removed from depreciable basis before the 27.5-year or 39-year computation.
- Month placed in service recorded, and the mid-month fraction used (11.5 months for January, held all year).
- Personal-use days compared with the greater of 14 and 10 percent of fair-rental days.
- If the unit is a home and was rented 15 days or more, Worksheet 5-1 used, and no loss taken against wages.
- If it is not a home, at-risk first, then the allowance at the modified AGI actually computed, then Form 8582.
- Real estate professional status asked, and handed to the other skill if it is claimed.
- Depreciation on line 18 of the draft, rent on line 3, and improvements not deducted as repairs.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| 26 U.S.C. 168 (govinfo, U.S. Code 2024 edition). Read for (b)(3) straight line for residential rental property and nonresidential real property, (c) the 27.5-year and 39-year recovery periods, (d)(2) and (d)(4)(B) the mid-month convention, and (e)(2) the 80 percent dwelling-unit test. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVI-sec168.htm | 2026-11-13 |
| 26 U.S.C. 469 (govinfo, U.S. Code 2024 edition). Read for (i) the USD 25,000 allowance, the 50 percent reduction above USD 100,000, and the USD 12,500 and USD 50,000 figures for a married person filing separately who lived apart all year. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapE-partII-subpartC-sec469.htm | 2026-11-13 |
| 26 U.S.C. 6651 (govinfo, U.S. Code 2024 edition). Read for (a)(1) 5 percent a month capped at 25 percent and (a)(2) 0.5 percent a month capped at 25 percent. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapA-partI-sec6651.htm | 2026-11-13 |
| Publication 527 (2025), Residential Rental Property. Read for chapter 2 (straight line, mid-month, Table 2-2d February year-1 rate 3.182 percent on a USD 160,000 building), chapter 3 (Schedule E line 18 and Form 8582), and chapter 5 (14 days or 10 percent, the fewer-than-15-day rule, and Worksheet 5-1). | https://www.irs.gov/publications/p527 | 2026-11-13 |
| Publication 925 (2025). Read for the sentence that the special allowance is gone when modified AGI is USD 150,000 or more (USD 75,000 if married filing separately). | https://www.irs.gov/pub/irs-pdf/p925.pdf | 2026-11-13 |
| Instructions for Schedule E (Form 1040) (2026), early-release draft, catalog number 24332T, marked "DRAFT—NOT FOR FILING". Read for line 3 (rents), line 14 (repairs versus improvements), line 18 (depreciation), line 19 (other expenses), the land-and-building split, and the order of at-risk, passive, and Form 461 limits. | https://www.irs.gov/pub/irs-dft/i1040se--dft.pdf | 2026-11-13 |

Not yet confirmed: the final 2026 Instructions for Schedule E and the 2026 edition of Publication 527 were not posted. The early-release draft is not for filing and says drafts of instructions usually change before release, so a line number that appears only in that draft (including new line 13a for vehicle-loan interest) is not used as a final 2026 figure. The 2026 standard mileage rates for rental miles were left out for that reason. The modified-AGI definition's cross-references in section 469(i)(3)(F) were not re-read item by item. Net investment income tax thresholds were not read.
