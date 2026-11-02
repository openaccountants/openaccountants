---
name: gr-living-expense-presumptions
description: "Greek deemed income from living-expense presumptions (τεκμήρια διαβίωσης) for tax year 2026 under the Income Tax Code, ν. 4172/2013 arts. 30 to 34, with the cuts made by ν. 5246/2025 from tax year 2025. Covers the annual deemed expense of the main and second homes, private cars, boats, aircraft, pools, private school fees and domestic staff; the minimum living expense (EUR 3,000 single, EUR 5,000 joint); asset purchases and loan repayments; how deemed income is compared with total income; the rebuttal and coverage grounds (savings of earlier years, loans, exempt income, gifts, asset sales); and how the difference is taxed on the scale. Trigger phrases: τεκμήρια, τεκμαρτό εισόδημα, διαφορά τεκμηρίων, deemed income Greece, Greek car presumption, living expenses tax Greece. Out of scope: the self-employed minimum income of art. 28A and the scale itself (gr-income-tax), non-residents and the 5A and 5C regimes (gr-cross-border), capital gains."
version: 0.2
jurisdiction: GR
tax_year: 2026
last_updated: 2026-11-01
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Greece: deemed income from living-expense presumptions, tax year 2026

Source-cited draft. Built by Michael Cutajar and the OpenAccountants team.

Greece taxes an individual on at least the income their lifestyle implies. The law calls it "alternative minimum taxation" (εναλλακτική ελάχιστη φορολογία). Homes, cars, boats, staff, school fees and asset purchases each carry a deemed annual expense. If the total is higher than declared income, the difference is added to taxable income and taxed (art. 30(1) ΚΦΕ). This skill computes that difference. It links to the pack's other skills instead of repeating them:

- The 2026 scale, the art. 16 tax reduction, the self-employed minimum income of art. 28A and the E1 return: `gr-income-tax`
- Non-residents, the 5A, 5B and 5C regimes: `gr-cross-border`
- EFKA contributions: `gr-efka`

The law is the Income Tax Code (Κώδικας Φορολογίας Εισοδήματος, ΚΦΕ, ν. 4172/2013), arts. 30 to 34, read in the Ministry of Finance codification up to ν. 5264/2025. ν. 5246/2025 art. 7 cut the home, car and boat amounts, ended the minimum expense for dependent children with their own income, and cut the deemed expense for zero-emission cars over EUR 50,000 from EUR 4,000 to EUR 2,000. These changes apply from tax year 2025 (ν. 5246/2025 art. 47(2)), so they apply to 2026. AADE circular Ο.3068/2025 gives notice of them. The tax year is the calendar year.

## Who this applies to

1. **Every individual subject to Greek income tax** whose deemed income is higher than total income (art. 30(1)). The deemed expense covers the taxpayer, the spouse and the dependent members (art. 31(1)).
2. **Total income** is the taxable income of all four categories (employment and pensions, business, capital, capital gains) of the taxpayer and dependants (art. 30(3)). Exempt income does not count here, but it can cover the difference later (art. 34(2)(a)).
3. **The self-employed.** The art. 28A minimum business income (computed in `gr-income-tax`) is a separate presumption. On our reading of arts. 7 and 30(3), where it applies, the art. 28A amount is the business income in total income for this comparison, not the lower profit (see "Not yet confirmed").
4. **Married couples on a joint return** are compared together. On separate returns each spouse carries their own deemed expenses and declares their own coverage amounts; minor children follow art. 11(5) (art. 34(2), last paragraph).

Out of scope of the presumptions altogether (art. 30(4)): foreign diplomats and consular staff who are nationals of the sending state with a diplomatic passport, and staff of EU institutions and international organisations based in Greece under a treaty.

## Rates, bands and thresholds

"Codification" is the Ministry of Finance codification of ν. 4172/2013 up to ν. 5264/2025, linked under the table and in Sources. All amounts apply from tax year 2025, so to 2026.

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Main home, first 80 m² of main space | EUR 28 per m² | 2026 | ΚΦΕ art. 31(1)(a), as amended by ν. 5246/2025 art. 7(1); Codification |
| Main home, 81 to 120 m² | EUR 45 per m² | 2026 | same |
| Main home, 121 to 200 m² | EUR 77 per m² | 2026 | same |
| Main home, 201 to 300 m² | EUR 140 per m² | 2026 | same |
| Main home, over 300 m² | EUR 280 per m² | 2026 | same |
| Auxiliary space of the main home | EUR 28 per m² | 2026 | same |
| Uplift for zone price EUR 2,800 to 4,999 per m² | 30% | 2026 | same |
| Uplift for zone price EUR 5,000 per m² or more | 58% | 2026 | same |
| Uplift for a detached house (μονοκατοικία) | 20% on all the above | 2026 | same |
| Second homes (owned or rented) | Half of the main-home amount | 2026 | ΚΦΕ art. 31(1)(b); Codification |
| Car first registered in Greece or the EU/EEA up to 31.10.2010, and any motorhome: up to 1,200 cc | EUR 2,000 | 2026 | ΚΦΕ art. 31(1)(γ)(αα); Codification |
| Same, 1,201 to 2,000 cc | Plus EUR 300 per 100 cc over 1,200 | 2026 | ΚΦΕ art. 31(1)(γ)(ββ); Codification |
| Same, 2,001 to 3,000 cc | Plus EUR 450 per 100 cc over 2,000 | 2026 | ΚΦΕ art. 31(1)(γ)(γγ); Codification |
| Same, over 3,000 cc | Plus EUR 600 per 100 cc over 3,000 | 2026 | ΚΦΕ art. 31(1)(γ)(δδ); Codification |
| Car first registered from 1.11.2010: up to 122 g CO2/km | EUR 2,000 | 2026 | ΚΦΕ art. 31(1)(γ)(εε)(i); Codification |
| Same, 123 to 139 g | Plus EUR 30 per gram over 122 | 2026 | ΚΦΕ art. 31(1)(γ)(εε)(ii); Codification |
| Same, 140 to 166 g | Plus EUR 45 per gram over 139 | 2026 | ΚΦΕ art. 31(1)(γ)(εε)(iii); Codification |
| Same, over 166 g | Plus EUR 60 per gram over 166 | 2026 | ΚΦΕ art. 31(1)(γ)(εε)(iv); Codification |
| Zero-emission car, L-category vehicle, moped or motorcycle, pre-tax retail price up to EUR 50,000 | EUR 0 deemed expense, and the purchase is not an art. 32 expense | 2026 | ΚΦΕ art. 33(θ), as amended by ν. 5246/2025 art. 7(2); Codification |
| Same, price over EUR 50,000 | EUR 2,000 a year | 2026 | same |
| Open motor boat up to 5 m | EUR 2,800, plus EUR 1,400 per metre over 5 | 2026 | ΚΦΕ art. 31(1)(στ)(αα); Codification |
| Boat with cabin up to 7 m | EUR 8,400; per extra metre plus EUR 2,100 (7 to 10 m), 5,250 (10 to 12 m), 10,500 (12 to 15 m), 15,750 (15 to 18 m), 21,000 (18 to 22 m), 35,000 (over 22 m) | 2026 | ΚΦΕ art. 31(1)(στ)(ββ); Codification |
| Sailing boats and traditional Greek wooden boats | Boat amounts cut by 50%; permanent crew pay added | 2026 | ΚΦΕ art. 31(1)(στ); Codification |
| Gliders; ultralight aircraft | EUR 8,000; EUR 20,000 | 2026 | ΚΦΕ art. 31(1)(ζ)(αα) and (δδ); Codification |
| Piston and turboprop aircraft, helicopters | EUR 65,000 for the first 150 hp, plus EUR 500 per hp over 150 | 2026 | ΚΦΕ art. 31(1)(ζ)(ββ); Codification |
| Jet aircraft | EUR 200 per pound of thrust | 2026 | ΚΦΕ art. 31(1)(ζ)(γγ); Codification |
| Outdoor pool | EUR 160 per m² up to 60 m², EUR 320 per m² above; doubled for an indoor pool | 2026 | ΚΦΕ art. 31(1)(η); Codification |
| Private primary and secondary school fees | The fees actually paid, per receipts (evening schools and special-needs schools excluded) | 2026 | ΚΦΕ art. 31(1)(δ); Codification |
| Domestic staff, drivers, tutors and other staff | The statutory minimum pay of each category; not applied for one domestic helper only, or for one carer of a person with 67% disability or aged over 65 | 2026 | ΚΦΕ art. 31(1)(ε); Codification |
| Minimum annual living expense | EUR 3,000 single; EUR 5,000 for spouses on a joint return; not applied to dependent children with their own income who must file | 2026 | ΚΦΕ art. 31(1)(θ), as amended by ν. 5246/2025 art. 7(1); Codification |
| Pensioners over 65 | Art. 31 amounts cut by 30% | 2026 | ΚΦΕ art. 33(ζ); Codification |
| Movable goods counted as an asset purchase | Items worth over EUR 10,000 each, or sets worth over EUR 10,000 together | 2026 | ΚΦΕ art. 32(a); Codification |
| Gifts and parental gifts made, counted as an expense | Over EUR 300 a year, except to the state, public bodies and listed charities | 2026 | ΚΦΕ art. 32(ε); Codification |
| Capital-only taxpayer taxed on the scale | Deemed income up to EUR 9,500 | 2026 | ΚΦΕ art. 34(1)(a); Codification |
| Low income, no business (art. 15(1A)) | Real income up to EUR 6,000 and deemed income up to EUR 9,500: taxed on the scale with the art. 16 reduction | 2026 | ΚΦΕ art. 15(1A), ν. 5246/2025; Codification |

Codification: [Income Tax Code, Ministry of Finance codification up to ν. 5264/2025](https://minfin.gov.gr/wp-content/uploads/2026/04/%CE%9A%CE%A9%CE%94%CE%99%CE%9A%CE%9F%CE%A0%CE%9F%CE%99%CE%97%CE%A3%CE%97-%CE%A4%CE%9F%CE%A5-%CE%9A%CE%A9%CE%94%CE%99%CE%9A%CE%91-%CE%A6%CE%9F%CE%A1%CE%9F%CE%9B%CE%9F%CE%93%CE%99%CE%91%CE%A3-%CE%95%CE%99%CE%A3%CE%9F%CE%94%CE%97%CE%9C%CE%91%CE%A4%CE%9F%CE%A3-%CE%9C%CE%95%CE%A7%CE%A1%CE%99-%CE%A4%CE%9F-%CE%9D-5264-2025.pdf)

## The taxable base

**Step 1: annual deemed expense (art. 31).** Add the amounts in the table for each home, car, boat, aircraft, pool, school and staff member of the taxpayer, spouse and dependants. The main home counts whether owned, rented or given free. The m² bands apply to main space (κύριοι χώροι); auxiliary space has its own rate. The total is never below the minimum living expense of EUR 3,000 (single) or EUR 5,000 (joint return) when real or deemed income is declared (art. 31(1)(θ)).

Car rules (art. 31(1)(γ)): a car owned for part of the year counts by twelfths, a part month over 15 days counting as a whole month; the same applies if the car is laid up or destroyed. Real co-owners split the amount by share; a sham transfer between close relatives counts in full for each party unless proved otherwise. A minor child's car counts for the parent with the higher income. A leased car counts for the lessee. Cars of partnerships and companies are attributed to the general partners, the LLC members or managers, or the managing directors of an SA, but no more than the company's highest-expense car per person. Vintage cars with a certificate of authenticity, cars adapted for a disabled driver, and a disabled person's car exempt from road tax do not count (arts. 31(1)(γ) and 33(a)). Mixed-use vehicles and jeeps follow the same scale.

**Step 2: asset purchases and repayments (art. 32).** Add the money actually paid in the year for: buying or financially leasing cars, motorcycles and three-wheelers, boats, aircraft and goods worth over EUR 10,000; buying a business, founding or adding capital to a company, buying shares and securities, and the investment part of unit-linked insurance; buying, timesharing or financially leasing property, building, or building a pool (at the full price in the deed, or a higher price found on audit); loans made to anyone; cash gifts over EUR 300 a year to non-exempt recipients; and repayments of loans and credit, including interest and default interest. Fixed business equipment bought by a business does not count (art. 33(ε)).

**Step 3: the difference (art. 30(1)).** Deemed income is step 1 plus step 2. If it exceeds total income, the difference is added to taxable income.

**Step 4: the person can reduce the art. 31 amount (art. 31(2)).** The art. 31 total (not the art. 32 purchases) can be challenged when actual living costs were lower, with evidence. The law names: military service; prison; hospital stay; registered unemployment with benefit; living with first-degree relatives who pay part of the costs from visible income; orphaned minors who inherited a car; and force majeure. AADE checks the evidence and cuts the amount. For military service and for living with relatives, the amount cut is added to the deemed expense of the parent or child who pays the costs; between two parents, to the one with the higher income.

**Step 5: coverage of the difference (art. 34(2)).** AADE must take into account amounts on the return that are backed by legal documents. The burden of proof is on the taxpayer. These amounts reduce the difference:

1. exempt income, or income taxed in a special way, of the taxpayer, spouse and dependants; foreign income counts if taxable or lawfully exempt in Greece;
2. sums that are not income under the law;
3. proceeds of selling assets;
4. foreign currency brought in, if its foreign origin is shown. No proof is needed for tax residents of another state, people who lived abroad 3 years and bring it within 2 years of moving, people who lived abroad 5 straight years and bring EU/EEA bank deposits within 1 year without sending them back out, and people on the 5A regime;
5. loans proved by documents with a certain date. For an art. 32 purchase the loan must be dated before the purchase;
6. cash gifts and parental gifts, if the gift tax return was filed by the end of the year of the expense. If it was filed later, AADE accepts the gift where the money was received before the expense and gift tax was paid or the gift was exempt (AADE circular Ε.2009/2025);
7. spending of capital (savings) taxed or lawfully exempt in earlier years. That capital is built year by year: taxed and exempt income, plus items 2 to 6 and any other proven receipts, minus that year's art. 31 and 32 expenses. Where art. 31 expenses were nil or under EUR 3,000 single or EUR 5,000 for spouses, AADE deducts a living cost based on the family's situation, never below those amounts (EUR 3,000 for each spouse on separate returns).

Any cost of getting these receipts reduces them. The list is not closed: art. 34(2) names the amounts "in particular" (ιδίως), and item 7 counts any other amount proven to have been received.

**Step 6: how the remaining difference is taxed (art. 34(1)).** The difference is added to taxable income in the same tax year and taxed:

1. on the art. 15(1) scale if the person has only employment or pension income, or most income is employment or pension, or there is no income at all, or the person has only capital income or capital gains and deemed income is EUR 9,500 or less;
2. under art. 29(1) (the business scale, without the art. 16 reduction) if the person has only business income or most income is not employment or pension;
3. under art. 29(3) (the art. 15(1) scale applied to farm profit separately, with the art. 16 reduction) if income is only or mostly from an individual farm;
4. on the art. 15(1) scale if the person is registered unemployed with the public employment service.

The 2026 scale is in `gr-income-tax`. The tax on the difference is the scale tax on total income plus the difference, minus the scale tax on total income alone. For business profit under this article, losses of the same or earlier years are not deducted and are not carried forward (art. 34(3)).

**Low incomes with no business (art. 15(1A)).** Where real income is EUR 6,000 or less, deemed income is EUR 9,500 or less, and the person runs no registered business or farm, the income (other than capital income and gains) and the added difference are taxed on the scale with the art. 16 reduction. Real income above EUR 6,000 is taxed under art. 29(1) without the reduction.

**Interaction with art. 28A.** The two presumptions are separate. Art. 28A sets a minimum business income for a sole trader; that figure is computed in `gr-income-tax`. On our reading of art. 30(3), where it applies it is the business income in the total income that this skill compares with deemed expenses, so a sole trader whose deemed living expenses exceed the art. 28A amount is taxed on the art. 30 difference above it. We have not read AADE guidance on this point.

## Deadlines and filing

| Event | Deadline | Source |
|---|---|---|
| Declare homes, cars, boats, staff, school fees, asset purchases and coverage amounts on form E1 for 2026 | With the 2026 return, 15 March to 15 July 2027 | ΚΦΕ art. 67(3); [AADE E1 instructions](https://www.aade.gr/sites/default/files/2026-03/Odigies_E1_2026_0.pdf) |
| Gift tax return for a cash gift used to cover the difference | By the end of the year of the expense (later filing accepted only on the Ε.2009/2025 conditions) | ΚΦΕ art. 34(2)(στ); AADE circular Ε.2009/2025 |
| Tax on the difference | Assessed with the return; paid in the same 8 monthly instalments from the last working day of July 2027 | ΚΦΕ arts. 34(1) and 67(6) |
| Challenge of the art. 31 amount (art. 31(2) grounds) | Evidence filed with AADE; AADE checks it and reduces the amount | ΚΦΕ art. 31(2) |

The E1 instructions linked are for 2025 income (filed in 2026). For staff, for example, they use E1 code 770. AADE publishes the 2026 form in early 2027.

## Penalties and interest

| Breach | Penalty | Source |
|---|---|---|
| Not declaring, or wrongly declaring, asset purchases (property bought or built) and living-expense items | Fines and penalties of the Tax Procedure Code | ΚΦΕ art. 34(4) |
| Inaccurate return: tax difference 5% to 20% of the tax declared | 10% of the difference | ΚΦΔ (ν. 5104/2024) art. 54(1)(a) |
| Difference over 20% and up to 50% | 25% of the difference | ΚΦΔ art. 54(1)(b) |
| Difference over 50% | 50% of the difference | ΚΦΔ art. 54(1)(c) |
| Late payment | Interest from the day after the payment deadline | ΚΦΔ art. 52(1) |

Late-filing fines are in `gr-income-tax`. The late-payment interest rate is set by ministerial decision; we did not read the percentage.

## Cross-border points

- **Non-residents.** The art. 31 presumptions (homes, cars, boats, minimum expense) do not apply to a person tax resident abroad. The art. 32 purchase rules apply to them only if they have Greek income (art. 33(η)).
- **Boats of permanent residents abroad** carry no deemed expense (art. 33(δ)).
- **5C regime (inbound workers).** The deemed expense for the home and the private car does not apply (art. 33(ι)). See `gr-cross-border`.
- **5A regime (lump-sum tax).** Foreign currency brought in needs no proof of origin to cover a difference (art. 34(2)(δ)(δδ)).
- **Foreign income** covers the difference only if it is taxable in Greece or lawfully exempt (art. 34(2)(a)).
- **Returnees.** Currency brought in within the art. 34(2)(δ) time limits after 3 or 5 years abroad needs no proof of origin.
- **Foreign staff of shipping companies** under α.ν. 89/1967, α.ν. 378/1968 and ν. 27/1975 art. 25 who do not live permanently in Greece carry no car or home presumption (art. 33(β)).

## Worked examples

### Example 1: employee whose home and car exceed the salary

Eleni is single, aged 40, no children, a Greek-resident employee. Her 2026 taxable salary is EUR 14,000. She rents a 200 m² flat (main space) in an area with a zone price of EUR 5,500 per m². She owns a petrol car first registered in 2015, rated 160 g CO2/km. She has no other income, no savings used and no loans.

Home: 80 m² at 28 (2,240) + 40 m² at 45 (1,800) + 80 m² at 77 (6,160) = 10,200, uplifted by 58% for the zone price: EUR 16,116. Car: 2,000 + 17 grams at 30 (510) + 21 grams at 45 (945) = EUR 3,455. Deemed income is EUR 19,571, above the EUR 3,000 minimum. The difference over her salary is EUR 5,571.

Her income is all salary, so the difference is taxed on the art. 15(1) scale. On EUR 19,571 it falls in the 20% band: 900 + 9,571 at 20% = EUR 2,814.20, against EUR 1,700 on the salary alone. The difference adds EUR 1,114.20 of tax. Her art. 16 reduction is EUR 777 minus EUR 40, so EUR 737: art. 16(2) phases it out by EUR 20 per EUR 1,000 of salary and pension income over EUR 12,000, so the added difference does not reduce it, and it is used in full against the salary tax either way.

```oa-check
name: GR employee, salary EUR 14,000, 200 m2 flat in EUR 5,000+ zone, 160 g car, 2026
inputs:
  salary: 14000
  m2: 200
  co2: 160
steps:
  - h1: min(m2, 80) * 28
  - h2: max(min(m2, 120) - 80, 0) * 45
  - h3: max(min(m2, 200) - 120, 0) * 77
  - h4: max(min(m2, 300) - 200, 0) * 140
  - h5: max(m2 - 300, 0) * 280
  - home: (h1 + h2 + h3 + h4 + h5) * 1.58
  - car: 2000 + max(min(co2, 139) - 122, 0) * 30 + max(min(co2, 166) - 139, 0) * 45 + max(co2 - 166, 0) * 60
  - deemed: max(home + car, 3000)
  - difference: max(deemed - salary, 0)
  - tax_salary: min(salary, 10000) * 0.09 + max(min(salary, 20000) - 10000, 0) * 0.20
  - total: salary + difference
  - tax_total: min(total, 10000) * 0.09 + max(min(total, 20000) - 10000, 0) * 0.20 + max(min(total, 30000) - 20000, 0) * 0.26
  - tax_on_difference: tax_total - tax_salary
expected:
  home: 16116.00
  car: 3455.00
  deemed: 19571.00
  difference: 5571.00
  tax_on_difference: 1114.20
```

### Example 2: freelancer who buys a car, covered by a loan and savings

Giorgos is single, a Greek-resident freelance engineer in his 8th year, with no staff. His 2026 taxable business profit is EUR 20,000, which is above his art. 28A minimum (see `gr-income-tax`), so EUR 20,000 is his total income. He owns a 90 m² flat (main space) in an area with a zone price under EUR 2,800 and an older car rated 120 g CO2/km. In 2026 he paid EUR 30,000 for a new petrol car and EUR 3,600 in repayments, with interest, on an older loan. He took a EUR 12,000 car loan, dated before the purchase. He proves EUR 4,000 of savings from income taxed in 2024.

Living expense: home 80 at 28 (2,240) + 10 at 45 (450) = EUR 2,690; old car EUR 2,000; total EUR 4,690. The new car counts by twelfths from the month he bought it (art. 31(1)(γ)); to keep the example simple, he bought it on 20 December, so its deemed annual expense adds nothing for 2026. Asset spending: EUR 30,000 + EUR 3,600. Deemed income is EUR 38,290, EUR 18,290 above total income. The loan (EUR 12,000) and earlier savings (EUR 4,000) cover EUR 16,000, leaving EUR 2,290.

Most of his income is business income, so the EUR 2,290 is taxed under art. 29(1), on the scale without the art. 16 reduction. It falls in the 26% band (EUR 20,000 to 30,000): EUR 595.40 more tax, on top of EUR 2,900 on his profit.

```oa-check
name: GR freelancer, profit EUR 20,000, car bought EUR 30,000, loan and savings cover, 2026
inputs:
  profit: 20000
  home_m2: 90
  old_car: 2000
  car_price: 30000
  loan_repaid: 3600
  new_loan: 12000
  savings: 4000
steps:
  - home: min(home_m2, 80) * 28 + max(min(home_m2, 120) - 80, 0) * 45
  - living: max(home + old_car, 3000)
  - deemed: living + car_price + loan_repaid
  - gross_difference: max(deemed - profit, 0)
  - difference: max(gross_difference - new_loan - savings, 0)
  - tax_profit: min(profit, 10000) * 0.09 + max(min(profit, 20000) - 10000, 0) * 0.20
  - total: profit + difference
  - tax_total: min(total, 10000) * 0.09 + max(min(total, 20000) - 10000, 0) * 0.20 + max(min(total, 30000) - 20000, 0) * 0.26
  - tax_on_difference: tax_total - tax_profit
expected:
  living: 4690.00
  deemed: 38290.00
  gross_difference: 18290.00
  difference: 2290.00
  tax_profit: 2900.00
  tax_on_difference: 595.40
```

## Ask the client first

1. Which homes do you and your family use (owned, rented or free), their main and auxiliary m², and whether each is a detached house? Do you know the zone price of the area? These set the largest presumption.
2. Which cars, motorcycles, boats or aircraft do you own or lease, with first registration date, CO2 or cc, and the months held in 2026? Each one adds a deemed amount.
3. What did you pay in 2026 for property, building, cars, shares, company capital, loans to others, gifts over EUR 300, and loan repayments? These are added in full.
4. What can cover a gap: exempt income, asset sales, loans with dated documents, gifts with a filed gift tax return, savings from income taxed in earlier years, money brought from abroad? Each needs documents.
5. Are you a pensioner over 65, registered unemployed, in military service, in hospital, living with relatives who pay costs, or on the 5A or 5C regime, or tax resident abroad? These cut or remove the presumption.
6. Are you married, and on a joint or separate return? This sets the EUR 5,000 or EUR 3,000 minimum and who carries each expense.

## Sources

| Source | URL | Read on |
|---|---|---|
| Income Tax Code (ν. 4172/2013), Ministry of Finance codification up to ν. 5264/2025: arts. 15(1A), 16(1), 29, 30, 31, 32, 33, 34, 67, with footnotes 228, 229 and 237 on ν. 5246/2025 art. 7 | https://minfin.gov.gr/wp-content/uploads/2026/04/%CE%9A%CE%A9%CE%94%CE%99%CE%9A%CE%9F%CE%A0%CE%9F%CE%99%CE%97%CE%A3%CE%97-%CE%A4%CE%9F%CE%A5-%CE%9A%CE%A9%CE%94%CE%99%CE%9A%CE%91-%CE%A6%CE%9F%CE%A1%CE%9F%CE%9B%CE%9F%CE%93%CE%99%CE%91%CE%A3-%CE%95%CE%99%CE%A3%CE%9F%CE%94%CE%97%CE%9C%CE%91%CE%A4%CE%9F%CE%A3-%CE%9C%CE%95%CE%A7%CE%A1%CE%99-%CE%A4%CE%9F-%CE%9D-5264-2025.pdf | 2026-10-23 |
| AADE circular Ο.3068/18-11-2025, notice of ν. 5246/2025 arts. 2 to 16, 43 and 47 (art. 7: cuts to home, car and boat amounts, end of the children's minimum expense; in force from tax year 2025) | https://www.aade.gr/egkyklioi-kai-apofaseis/o-3068-18-11-2025 | 2026-10-23 |
| AADE circular Ε.2009/14-02-2025, gifts filed late used to cover the difference | https://www.aade.gr/egkyklioi-kai-apofaseis/e-2009-14-02-2025 | 2026-10-23 |
| Tax Procedure Code (ν. 5104/2024), AADE codification Ε.2109/2025: arts. 52, 54 | https://www.aade.gr/sites/default/files/2025-12/e2109_2025.pdf | 2026-10-23 |
| AADE, E1 return instructions (2025 income, filed 2026) | https://www.aade.gr/sites/default/files/2026-03/Odigies_E1_2026_0.pdf | 2026-10-23 |

Not yet confirmed: the annual minimum-wage base AADE uses for the 2026 art. 28A minimum (12 or 14 monthly wages; not found in the E1 instructions, AADE decision Α.1062/2026 (the E1 form for 2025 income) or AADE circulars Ο.3071/2023 and Ε.2027/2024, which repeat the law's "annual amount of the gross minimum wage"); that the art. 28A amount, where it applies, is the business income in "total income" for art. 30(3) (our reading of arts. 7, 28A and 30; no AADE text read on it); whether the art. 16 reduction applies to the tax on a difference taxed on the art. 15(1) scale outside art. 15(1A) (the examples avoid the point); whether the 55% prepayment of art. 69 is charged on a difference taxed under art. 29(1); the 2026 E1 form and its codes; the late-payment interest percentage under ΚΦΔ art. 52; any amendment to arts. 30 to 34 made during 2026 after ν. 5264/2025.

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
