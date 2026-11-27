---
name: ca-capital-gains
description: "Canadian resident individuals: calculate capital gains and losses, reconstruct adjusted cost base, test principal residence and flipping rules, calculate eligible LCGE deductions and reserves, and prepare Schedule 3. Ordinary inclusion is one-half under enacted law. For non-residents use ca-nonresident-cgt."
version: 1.2
jurisdiction: CA
tax_year: 2026
last_updated: 2026-11-27
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: filing-howto
depends_on:
  - income-tax-workflow-base
---

# Canada: capital gains for individuals

## Scope

Federal capital gains and losses for individuals resident in Canada, **tax year 2026**, with a separately dated **2025** filing map. Covers shares/funds, homes and cottages, personal-use/listed personal property, qualifying business/farm/fishing gains, losses and reserves. Amounts are Canadian dollars. Obtain provincial/territorial and Quebec calculations separately. Use ca-tax-residency for residence/departure questions, ca-nonresident-cgt for non-resident dispositions and ca-return-assembly for the wider T1. Corporations, trusts and partnerships need their own treatment.

## Ask the client first

Obtain residence/ownership history; acquisition, disposition and expense dates/currencies; all broker confirmations, T5008/T3 slips, purchase costs, improvements and selling costs; family homes and designated years; rental/CCA/election history; any housing sale within the flipping window and its reason; related or registered-plan repurchases; QSBC/QFFP eligibility evidence, prior deductions, ABIL and CNIL records; loss balances and origin years; and deferred consideration. Establish taxpayer/spouse business status for deadlines. Missing basis, dates, ownership or eligibility means **no usable filing conclusion**.

## The method, step by step

1. Establish capital rather than business character, including the flipping test below; classify each asset before calculating.
2. Rebuild the transaction and remaining ACB pool from source records in CAD. Calculate the full gain/loss, then the applicable exemption, loss restriction or reserve.
3. Apply ordinary half inclusion once, net ordinary allowable losses against taxable gains, and keep LPP separate. Apply prior-year losses and the capital gains deduction only through their own limits.
4. Reconcile the actual annual forms, obtain specialist work for the holds below, then pass working papers to the return preparer. Preparation, review, submission, CRA processing and payment are separate events.

### Rates, limits and the ordinary gain

| Item and conditions | 2026 | 2025 | Official source |
|---|---|---|---|
| Ordinary taxable capital gain / allowable capital loss; specified gifts separately | One-half | One-half | [ITA38(a),(b)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-38.html) |
| LCGE for eligible QSBC/QFFP gains, before personal history and eligibility limits | $1,275,000 gains; $637,500 deduction | $1,250,000 gains; $625,000 deduction | [CRA indexation table](https://www.canada.ca/en/revenue-agency/services/tax/individuals/frequently-asked-questions-individuals/adjustment-personal-income-tax-benefit-amounts.html), [ITA110.6](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-110.6.html) |
| Ordinary whole personal-use item: minimum cost and proceeds; partial interests, sets and excluded gifting arrangements require separate treatment | $1,000 each | Same | [ITA46](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-46.html) |
| Late PRE designation accepted under the discretionary election provisions | Lesser of $8,000 and $100 × complete months late | Same | [ITA220(3.2),(3.21),(3.5)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-220.html) |

**Ordinary gain = proceeds − ACB − selling outlays;** reverse the difference for a loss, then apply the loss restrictions. ITA40(1). ACB normally includes purchase commissions/legal costs and capital improvements, not maintenance/repairs. Convert proceeds at the sale-date rate, cost at acquisition-date rate and each expense at its incurred-date rate. [G02][G19]

**Identical-property pool:** new average = (remaining pre-purchase ACB + new acquisition cost) / total units now held. Remove sold units at their average cost; never restore costs already disposed of. Employee-option securities, debt instruments and other statutory exceptions need their own treatment. Stock splits/consolidations change per-share cost, not aggregate cost. [G09][G19]

**T3 box42:** positive reduces ACB; negative increases it by its magnitude. When an adjustment would take ACB below zero, recognize that excess as a capital gain and reset ACB to zero. Trace each adjustment to the correct trust-unit pool. [G19]

**T5008 reconciliation:** box20 book value may differ from tax ACB. The actual2026 slip is available; its fields include currency13, transaction date14, security15–18, cost20 and proceeds21. The issuer guide uses settlement date and permits1231 for aggregated transactions; neither proves acquisition date. Box21 is gross proceeds: reconcile commissions to the confirmations and avoid deducting costs twice or importing the same sale twice. [G41][G42][G43]

### Principal residence exemption (PRE)

First establish capital property. An owned housing unit, qualifying leasehold or co-operative housing share must satisfy ordinary habitation by the taxpayer, spouse/common-law partner, former spouse/common-law partner or child and designation for the year. House/cottage/condo/apartment/duplex/trailer/mobile-home/houseboat forms can qualify. Normally surrounding land is limited to **half a hectare**; excess needs proof it was necessary for use and enjoyment. [G03][G20¶2.7–2.14,2.32–2.35]

For1982onward, only one property per family unit can be designated for a year. For the current family definition include the throughout-year spouse/common-law partner unless separated throughout under a court order/written agreement, and children except those married, partnered or aged18or more during the year; for an unmarried/unpartnered taxpayer under18throughout, include parents and unmarried/unpartnered siblings under18. Historical family definitions require the actual historical-year test. [G20¶2.13–2.14]

Under ITA40(2)(b), remaining gain = **max(0, A − A×B/C − D)**: A is otherwise determined gain; B is eligible designated years ending after acquisition during Canadian residence, plus one **only if resident during the acquisition year**; C is all ownership tax years ending after acquisition; D is the specified1994-election adjustment, otherwise zero. ITA257 floors a negative algebraic result at nil. Do not grant the extra year to someone non-resident throughout acquisition year or manufacture a loss from a fraction exceeding one. A relevant1994 election requires its actual calculation. [G02][G39]

Report the sale/designation even where fully sheltered. **Actual2025** Schedule3 Part2 line17900 box1 (all years/all but one) uses T2091(IND) Section1 on **page2**; boxes2/3 also require applicable Section2 beginning **page3**. Complete a separate form for each property and use only the taxpayer's share/residence portion. Pre1982 ownership,1994 elections, mixed use, changes of use and missed elections remain held below. [G26][G30]

Late designation requires a discretionary CRA request, subject to ITA220's ten-calendar-year application rule; acceptance is not automatic. The penalty in the table runs to a satisfactory application:12complete months gives1,200;100months is capped at8,000. [G16]

### Flipped housing

ITA12(12)–(14) applies to Canadian housing units or rights held **less than365consecutive days**, excluding property already inventory. An otherwise arising gain is business income, no half inclusion or PRE; the business loss is deemed nil. The rule applies to dispositions after2022. Report business results through T2125. [G13][G20¶2.6–2.6.4][G26]

The exception requires the disposition reasonably to occur **due to, or in anticipation of**, death of taxpayer/related person; related household addition/joining; marriage/partnership breakdown after at least90days living apart; safety threat; serious illness/disability; eligible relocation of taxpayer/spouse/partner; involuntary employment termination of taxpayer/spouse/partner; taxpayer insolvency; or destruction/expropriation. The relocation exception uses the statutory definition with the Canadian new-location/residence requirements removed; a40km comparison alone is insufficient. [G13][G48]

A life event or holding for365days does **not** establish capital character. General trading/business facts must still be decided before PRE. [G20¶2.6]

### LCGE: qualification before deduction

The table gives gains and deduction in different units. ITA117.1 indexes the625,000 deduction base for years after2025. Deduction entitlement needs Canadian residence throughout the claim year;110.6(5) deems that condition met where resident at some time that year and throughout the immediately preceding or following year. [G04][G06][G18]

For QSBC shares: at sale the shares must be of a small business corporation. For a direct operating CCPC, the at-sale standard is **all or substantially all** qualifying asset FMV; CRA's90%description is not an enacted percentage safe harbour. Throughout the preceding24months no owner may be outside the permitted individual/related person-or-partnership chain, and throughout the part of that period owned by that chain, the CCPC must have **more than50%** qualifying asset FMV. New issues, substituted shares and connected-company asset tracing need the actual110.6(1),(14) tests; exactly50%fails the history threshold. QFFP has separate tests. [G04][G48]

Complete **T657** and claim permitted deduction at **25400**: the current eligible gain, annual gains limit, cumulative gains limit and remaining lifetime limit all constrain it; prior QSBC/QFFP deductions share the lifetime room. CNIL is cumulative investment expense over investment income after1987, if positive, and reduces the cumulative limit. T936 supplies that history. For the annual limit, subtract old loss deductions only after their offset by net non-eligible taxable gains; adjusted ABIL also reduces the limit. Use complete forms, not headline-cap subtraction. AMT remains a separate held calculation. [G04][G28][G29]

### Losses

Net ordinary allowable losses against current taxable gains first. Excess forms the net capital loss, generally available against taxable gains **three years back or indefinitely forward**. For2026 the carryback years are2023–2025; for2025 they are2022–2024. Use **T1A**, not an amended prior-year return merely for the carryback. Carryforward claims go to **25300**, oldest losses first, retaining balances by origin year. [G05][G21][G22][G27]

Adjust historical allowable-loss balances to the claim-year inclusion rate:1988–1989 used two-thirds;1990–1999 three-quarters;2000 uses the taxpayer's actual Schedule3 rate;2001–2025 one-half. Never subtract current-rate use from an unadjusted origin-year balance. Prior-year net capital losses reduce **taxable income rather than net income**; a carryback can nevertheless require a linked LCGE recomputation. Pre1986 other-income relief, death-year exceptions and ABIL are held below. [G05][G21][G22]

**Superficial loss:** both tests are required: taxpayer/affiliated person acquires identical/substituted property (including qualifying rights) in the30days-before through30days-after window, and taxpayer/affiliate still owns or has the right to acquire it at the end. The loss is denied under40(2)(g)(i). For the same taxpayer's full taxable-account repurchase, the denied loss generally increases substituted-property ACB. A later day31purchase cannot cure another in-window affiliated acquisition/right. Complex affiliations, partial quantities, deemed-disposition exceptions and registered plans remain held below. [G02][G03][G21]

For ordinary personal-use property, apply the table's floors; when cost and proceeds are both1,000or less, there is no reportable gain. PUP losses are generally denied; LPP and the statutory debt exception require their separate rules. **LPP** means the statutory personal-use art, jewellery, rare folios/manuscripts/books, stamps and coins (including interests/rights), not any asset expected to appreciate. LPP losses offset LPP gains only, oldest eligible first, three years back/seven forward; a2026loss potentially reaches2023–2025 or2027–2033, subject to actual gains/prior use. Partial interests/sets/excluded gifting arrangements do not receive automatic separate1,000floors. [G02(2)(g)][G03][G10][G11]

### Ordinary reserve and specified gifts

Calculate the full gain first. Ordinary reserve is the lesser of a reasonable gain portion of proceeds **payable after year-end** (normally gain×deferred proceeds/proceeds) and remaining caps **80%,60%,40%,20%,0%** in sale year and the following four years. In a later year also cap at the preceding claimed reserve and recognize **prior reserve − new reserve**, not original gain afresh or a compulsory fixed20%increment. Claim through **T2017**. [G02(1)(a)][G44]

No ordinary reserve where non-resident/exempt at year-end or any time in the following year, or sale to an immediately controlled corporation or partnership in which immediately a majority-interest partner; test the complete40(2)(a) conditions. Ten-year/special transfer routes and older sale/gift categories remain held below. [G02]

Eligible listed securities/fund gifts to a qualified donee can have zero inclusion under38(a.1); with an advantage,38.2 limits that treatment to gain×eligible gift amount/proceeds and applies ordinary half inclusion to the remainder. Use **T1170**. This is not a blanket exemption for all gifts: ecological-land, exchangeable-security, partnership and flow-through exceptions require their own conditions, and AMT/credit work remains separate. [G01][G45][G47]

### Actual2025 forms: ordered filing map

This map is for **2025 only**, not final2026 annual field numbers. [G26–G30][G44][G45]

1. Schedule3 Part1 asks the flipping facts at17905/17906; Part2 handles PRE at17900 as above.
2. Part3 records acquisition year, proceeds, ACB, outlays and gain/loss by property type: QSBC1(10699/10700), QFFP2(10999/11000), QFFP foreclosures3(12399/12400), public/other shares4(13199/13200), real/depreciable/other property5(13599/13800), debt6(15199/15300), capital crypto7(15200/15301), other foreclosures8(15499/15500), PUP9(15800 gain only), LPP10(15900 net gain only). Character and the special PRE directions control; a business sale never becomes capital by choosing a row.
3. Part4 reconciles directed slips, including T317600 and T2017reserve19200, to19700. Part5 applies50%then separately adds special partnership amount19890at100%, giving19900. Positive goes to12700; negative goes to loss records/T1A. Do not halve an already-taxable amount twice or interpret19890as a general two-thirds threshold.
4. Complete T936 Parts1–3/ChartA and T657 annual/cumulative/remaining-limit steps before claiming25400. On T6572025 Step1,14–16 subtract T936ChartA14 net non-eligible taxable gains from25300losses, floored at zero;17–19 adjust ABIL;21 is the annual limit. Reconstruct actual prior-edition opening balances; the2025T936line20 references **2024** T936line19.
5. For2025carryback, T1A Part5 uses2022/2023/2024 fields66360/66370/66380; LPP Part6 separately uses66420/66430/66440. Preserve certification/signature/date and actual submission/reassessment. T2017net adjustment67060feeds Schedule319200. T1170's ordinary taxable portion follows its directed share13200/debt15300/ecological-land13800 destination.
6. Attach the required schedules/signed designations to a paper return, or follow the actual form/software electronic instructions and retain signed records. Reconcile imported slips and allocations against underlying transactions to prevent duplicate reporting. Historical reserve/trust/partnership charts and final2026field maps are held below.

## Boundary and exception table

| Trigger | Usable boundary or hold |
|---|---|
| Less-than365day Canadian housing disposal with no listed event | Flipping business treatment above; C5 |
| Exactly365days or listed event | Reassess business versus capital; no automatic PRE |
| Family city home and cottage / acquisition-year non-residence | One designation/year and conditional plus-one; C3 |
| Loss plus in-window replacement / day31alternative | Both superficial tests, then all other loss restrictions; C2 |
| QSBC exactly50% historical qualifying value | Fails more-than50%test; entitlement not established |
| PUP loss / low-cost boat / LPP | PUP floors/denial and separate LPP channel; C6 |
| Prior losses, eligible and non-eligible gains | Adjust units and annual limit separately; C7,Checks7–8 |
| Deferred proceeds / gift advantage | Conditional reserve and prorated gift rules; Checks6,9 |

## Worked cases

All cases: individual resident in Canada throughout 2026, amounts in Canadian dollars, federal treatment only. The amounts are illustrations, not official figures.

**C1. Shares bought twice, part sold (average cost).**
Bought 100 shares of one public company at $20 each plus $10 commission (cost $2,010), later 100 more at $30 each plus $10 commission (cost $3,010). Total cost $5,020 for 200 shares, so the average cost is $25.10 a share. In June 2026 sold 150 shares at $40 each: proceeds $6,000, commission $10.
- ACB of the shares sold: 150 × $25.10 = $3,765.
- Capital gain: $6,000 − $3,765 − $10 = $2,225.
- Taxable capital gain (one-half): $1,112.50, reported through Schedule 3 to line 12700 (actual2025 public-share row4; verify2026edition).
- The 50 shares left keep the average cost: ACB $1,255.

**C2. Loss sale and buy-back (superficial loss).**
100 shares with an ACB of $5,000 sold on 10 March 2026 for $3,000 (a $2,000 loss). On 25 March 2026 the client buys 100 identical shares for $3,100 and still holds them on 9 April 2026 (30 days after the sale).
- Both tests are met, so the $2,000 loss is a superficial loss and is denied for 2026.
- The client bought the substituted shares, so the new ACB is $3,100 + $2,000 = $5,100.
- If instead the client bought back on15April2026,36days after sale, with no taxpayer/affiliated acquisition or right in the window8February–9April, the superficial-loss rule would not deny the loss. Assuming no other restriction, allowable capital loss is1,000.

**C3. Cottage and city home in one family (principal residence formula).**
A couple owns a city home (bought 2008) and a cottage the husband bought in 2017 for $300,000. The cottage is sold in 2026 for $700,000 with $20,000 of selling costs. Both were ordinarily inhabited by the family every year; both spouses were resident in Canada throughout. They decide to designate the cottage for4years(2023–2026) and keep the other years for the city home. Assume capital property, no change-of-use/CCA issue, all designated years eligible, D=0 and no1994 election adjustment.
- Gain: $700,000 − $300,000 − $20,000 = $380,000.
- Years owned ending after acquisition: 2017 to 2026 = 10. Years designated = 4, plus 1 = 5.
- Exempt part: $380,000 × 5 ÷ 10 = $190,000. Remaining gain: $190,000.
- Taxable capital gain: $95,000.
- Report on Schedule 3 and the full Form T2091(IND) (the cottage was not the principal residence for all years or all years but one). The city home cannot be designated for 2023 to 2026 when it is sold later. Compare gain per year on each property before choosing the years.

**C4. Selling qualified small business shares (LCGE 2026).**
A founder sells all her shares of a CCPC in August 2026 for a capital gain of $1,500,000. She and related persons held the shares for more than 24 months, the more-than-50% asset test was met throughout, and at the time of sale 90% or more of the assets were used in an active business carried on primarily in Canada. Assume the actual all-or-substantially-all statutory at-sale test and all other QSBC conditions are established; 90% alone is not a statutory safe harbour. No LCGE used before, no CNIL, no ABIL, no net capital losses claimed.
- Taxable capital gain: $750,000 (line 12700).
- Capital gains deduction (2026 limit): $637,500 on line 25400, supported by Form T657 and Form T936.
- Taxable capital gain left in taxable income: $112,500.
- This leaves112,500 of this gain in ordinary taxable income before any other taxpayer items. It is not112,500 of tax payable. Obtain the correct-year T691 AMT calculation before finalising; no AMT dollar amount is established here.

**C5. Condo sold after nine months (flipping rule).**
Bought 1 February 2026 for $500,000, sold 1 November 2026 for $560,000, selling costs $10,000. No listed life event.
- Owned less than 365 consecutive days, so it is a flipped property.
- Profit $50,000 is **business income** (Form T2125), fully included; no inclusion rate, no principal residence exemption.
- If the move satisfies the complete eligible-relocation exception, including the40km comparison and causal link, the statutory flipping deeming does not apply. Reassess business versus capital on general principles, then PRE separately if capital. A job move or273-day holding period alone does not establish an exemption.

**C6. Personal-use property floor.**
A boat bought for $800 is sold for $1,500.
- ACB is under $1,000, so ACB is treated as $1,000. Gain: $1,500 − $1,000 = $500; taxable capital gain $250, reported on Schedule 3 (actual2025 PUProw9; verify2026edition).
- Had it sold for $900, both ACB and proceeds would be $1,000 or less: no gain, nothing to report. Had it sold at a loss, the loss would not be deductible.

**C7. Net capital loss carried back.**
In 2026 the client has capital losses of $10,000 and capital gains of $4,000.
- Allowable capital loss $5,000; taxable capital gain $2,000. Net: $3,000 of unapplied allowable loss, which is the 2026 net capital loss.
- Nothing goes on line 12700 for 2026, and the loss cannot reduce 2026 employment income.
- Carry it back against taxable capital gains of 2023, 2024 or 2025 on Part 5 of Form T1A filed with the 2026 return, or keep it for line 25300 in a later year.

### Check1: original average-cost partial sale and a later purchase

C1's remaining50shares have1,255ACB. If another50shares are acquired for2,000all-in, the new100-share pool has3,255ACB and32.55average, not the original5,020plus2,000. [G09][G19]

```oa-check
name: Canadian capital shares partial sale preserves remaining pool
inputs:
  first_cost: 2010
  second_cost: 3010
  initial_units: 200
  sold_units: 150
  proceeds: 6000
  sale_cost: 10
  later_cost: 2000
  later_units: 50
steps:
  initial_pool: first_cost + second_cost
  average: initial_pool / initial_units
  sold_acb: average * sold_units
  gain: proceeds - sold_acb - sale_cost
  taxable_gain: gain * 0.5
  remaining_pool: initial_pool - sold_acb
  remaining_units: initial_units - sold_units
  new_pool: remaining_pool + later_cost
  new_average: new_pool / (remaining_units + later_units)
expected:
  initial_pool: 5020
  average: 25.1
  sold_acb: 3765
  gain: 2225
  taxable_gain: 1112.5
  remaining_pool: 1255
  new_pool: 3255
  new_average: 32.55
```

### Check2: original loss repurchase and original annual net loss

For C2 the full100-share self-repurchase is within8February–9April2026 and still held at the end; all2,000 is denied and substituted ACB becomes5,100. The15April alternative is36days after sale, with no other in-window acquisition/right and no other restriction. For C7 assume ordinary losses, no LPP/ABIL/stop-loss complications. [G02][G03][G21][G21]

```oa-check
name: Canadian ordinary and superficial losses use distinct balances
inputs:
  old_acb: 5000
  sale_proceeds: 3000
  repurchase_cost: 3100
  year_gross_losses: 10000
  year_gross_gains: 4000
steps:
  denied_loss: old_acb - sale_proceeds
  substituted_acb: repurchase_cost + denied_loss
  alternative_allowable_loss: denied_loss * 0.5
  year_allowable_losses: year_gross_losses * 0.5
  year_taxable_gains: year_gross_gains * 0.5
  net_capital_loss: max(0, year_allowable_losses - year_taxable_gains)
  positive_12700: max(0, year_taxable_gains - year_allowable_losses)
expected:
  denied_loss: 2000
  substituted_acb: 5100
  alternative_allowable_loss: 1000
  year_allowable_losses: 5000
  year_taxable_gains: 2000
  net_capital_loss: 3000
  positive_12700: 0
```

### Check3: cottage formula, full designation and no manufactured PRE loss

C3 assumes acquisition-year residence, all four eligible designations, capital character and D=0. The second subcase uses10designated years and10owned years with plus-one: the negative algebraic result is nil under257. D must be calculated separately in a relevant1994-election case. [G02][G30][G39]

```oa-check
name: Canadian principal residence formula preserves D and floors at nil
inputs:
  proceeds: 700000
  acb: 300000
  costs: 20000
  designated_years: 4
  owned_years: 10
  d_adjustment: 0
steps:
  gain: proceeds - acb - costs
  exempt_ratio_amount: gain * (designated_years + 1) / owned_years
  remaining_gain: max(0, gain - exempt_ratio_amount - d_adjustment)
  taxable_gain: remaining_gain * 0.5
  all_designated_result: max(0, gain - gain * (owned_years + 1) / owned_years - d_adjustment)
expected:
  gain: 380000
  exempt_ratio_amount: 190000
  remaining_gain: 190000
  taxable_gain: 95000
  all_designated_result: 0
```

### Check4: eligible QSBC headline limit is not a tax bill

C4 assumes all actual QSBC tests, residence and unused limits proved, no CNIL/ABIL/loss/prior-deduction reduction. The indexed2026 result637,500 remains conditional; taxable amount112,500 is not tax payable. [G04][G06][G18]

```oa-check
name: Canadian eligible 2026 gain and indexed deduction are different units
inputs:
  gross_gain: 1500000
  eligible_gain_limit: 1275000
steps:
  taxable_gain: gross_gain * 0.5
  deduction_cap: eligible_gain_limit * 0.5
  deduction: min(taxable_gain, deduction_cap)
  remaining_taxable_amount: taxable_gain - deduction
expected:
  taxable_gain: 750000
  deduction_cap: 637500
  deduction: 637500
  remaining_taxable_amount: 112500
```

### Check5: flipping and personal-use floors

C5 is273days from1February to1November2026, no qualifying life event and already-established Canadian housing facts. Its50,000profit is business income, with no half inclusion/PRE. C6 is an ordinary whole boat, not a partial-interest/set/gifting-arrangement case. [G10][G13]

```oa-check
name: Canadian flipped profit and personal use floor are separate treatments
inputs:
  condo_proceeds: 560000
  condo_cost: 500000
  condo_sale_cost: 10000
  boat_acb: 800
  boat_proceeds: 1500
  alternative_proceeds: 900
steps:
  business_profit: condo_proceeds - condo_cost - condo_sale_cost
  pup_acb: max(1000, boat_acb)
  pup_gain: max(1000, boat_proceeds) - pup_acb
  pup_taxable: pup_gain * 0.5
  alternative_gain: max(1000, alternative_proceeds) - pup_acb
expected:
  business_profit: 50000
  pup_acb: 1000
  pup_gain: 500
  pup_taxable: 250
  alternative_gain: 0
```

### Check6: reserve can produce no additional gain in a later year

Original gain100,000/proceeds200,000/deferred60,000. Choose the maximum ordinary permissible reserve30,000 in year1, recognizing70,000. If60,000remains payable after year2, the still-permitted30,000reserve leaves **zero** further reserve-related gain that year, not a compulsory20,000. Full gain remains recognized by the final deadline. This assumes no prohibition and no other sale-year amounts. [G02][G44]

```oa-check
name: Canadian reserve uses remaining reserve and prior year reconciliation
inputs:
  original_gain: 100000
  proceeds: 200000
  deferred_year1: 60000
  deferred_year2: 60000
steps:
  reasonable_year1: original_gain * deferred_year1 / proceeds
  cap_year1: original_gain * 0.8
  reserve_year1: min(reasonable_year1, cap_year1)
  recognized_year1: original_gain - reserve_year1
  reasonable_year2: original_gain * deferred_year2 / proceeds
  cap_year2: original_gain * 0.6
  reserve_year2: min(reasonable_year2, cap_year2, reserve_year1)
  recognized_year2: reserve_year1 - reserve_year2
  reserve_final_year: original_gain * 0
expected:
  reserve_year1: 30000
  recognized_year1: 70000
  reserve_year2: 30000
  recognized_year2: 0
  reserve_final_year: 0
```

### Check7: non-eligible gains absorb old losses before the LCGE adjustment

Synthetic all-capital case with no T2048/trust adjustments, current loss or ABIL: eligible taxable gains30,000, non-eligible taxable gains20,000. An old-loss deduction15,000is fully absorbed by non-eligible gains for this limit;35,000leaves15,000adjusted loss reducing the eligible annual limit to15,000. CNIL/cumulative/lifetime constraints still require their own steps. [G04][G28][G29]

```oa-check
name: Canadian annual gains limit adjusts old losses for non eligible gains
inputs:
  eligible_taxable_gain: 30000
  other_taxable_gain: 20000
  old_loss_a: 15000
  old_loss_b: 35000
steps:
  total_taxable_gains: eligible_taxable_gain + other_taxable_gain
  a_limit: min(total_taxable_gains, eligible_taxable_gain)
  non_eligible_excess: max(0, total_taxable_gains - a_limit)
  adjusted_loss_a: max(0, old_loss_a - non_eligible_excess)
  annual_limit_a: max(0, a_limit - adjusted_loss_a)
  adjusted_loss_b: max(0, old_loss_b - non_eligible_excess)
  annual_limit_b: max(0, a_limit - adjusted_loss_b)
expected:
  total_taxable_gains: 50000
  non_eligible_excess: 20000
  adjusted_loss_a: 0
  annual_limit_a: 30000
  adjusted_loss_b: 15000
  annual_limit_b: 15000
```

### Check8: historical allowable-loss balance is not a current-rate balance

Origin1995rate75%, remaining allowable balance7,500; current ordinary rate50%. Current deduction3,000consumes4,500origin-year allowable-loss units and leaves3,000origin units, equivalent to2,000current-rate deduction. Keep rates and units on both sides of the ledger. [G05][G21][G22]

```oa-check
name: Canadian capital loss rate conversion preserves origin balance units
inputs:
  origin_allowable_balance: 7500
  origin_rate: 0.75
  current_rate: 0.5
  current_deduction: 3000
steps:
  current_equivalent: origin_allowable_balance * current_rate / origin_rate
  origin_consumed: current_deduction * origin_rate / current_rate
  origin_remaining: origin_allowable_balance - origin_consumed
  current_remaining_equivalent: origin_remaining * current_rate / origin_rate
expected:
  current_equivalent: 5000
  origin_consumed: 4500
  origin_remaining: 3000
  current_remaining_equivalent: 2000
```

### Check9: gift advantage and T3 capital adjustment

Gift example assumes qualifying listed securities, eligible donee/receipt and no flow-through/partnership special gain. Ordinary taxable400does not settle AMT or the charitable credit. The separate T3example proves below-zero reset and the negative-box magnitude. [G02][G21][G19][G45][G47]

```oa-check
name: Canadian gift advantage and trust unit adjustments avoid blanket zero rates
inputs:
  gift_proceeds: 10000
  gift_acb: 6000
  eligible_gift: 8000
  pool_acb: 100
  positive_box42: 150
  negative_box42_magnitude: 50
steps:
  gift_gain: gift_proceeds - gift_acb
  zero_inclusion_gain: gift_gain * eligible_gift / gift_proceeds
  ordinary_gain: gift_gain - zero_inclusion_gain
  ordinary_taxable: ordinary_gain * 0.5
  deemed_gain: max(0, positive_box42 - pool_acb)
  reset_acb: max(0, pool_acb - positive_box42)
  increased_acb: pool_acb + negative_box42_magnitude
expected:
  gift_gain: 4000
  zero_inclusion_gain: 3200
  ordinary_gain: 800
  ordinary_taxable: 400
  deemed_gain: 50
  reset_acb: 0
  increased_acb: 150
```

**Decision checks:** exactly365days is outside the statutory window but can still be business;89days separation fails the90dayevent; exactly50%fails the QSBC history test; day31repurchase does not cure an in-window affiliated acquisition/right; disposing of replacement before window end can change that test but does not establish deductibility. Missing basis/ownership/designation/eligibility holds the result. The45(3)/CCA, child-residence and partnership-majority reserve cases remain non-usable specialist holds above.


## When to refuse or refer

Each following outcome is **held, non-usable** until the missing operative conditions/evidence are resolved:

- Residence changes, non-resident ownership, departure tax, trusts/estates/partnerships/corporations, gifts/inheritances and express spouse/farm rollovers, depreciable property/CCA/recapture, provincial/Quebec tax: Check this point with one of our partner accountants.
- Mixed/ancillary income use, structural changes,45(2)/45(3)elections (including partial changes), post1984CCA, employer-relocation54.1relief, pre1982ownership and1994election/T2091-WS adjustments: Check this point with one of our partner accountants.
- QFFP ownership/use tests; new/substituted/connected-company QSBC shares and purification; EOT/qualifying business transfers, cooperative/intergenerational transfers and small-business investment deferral; ten-year reserves including child residence immediately before transfer; old pre13November1981reserves and non-qualifying-security gifts: Check this point with one of our partner accountants.
- ABIL reductions/eligibility, death-year111(2), pre23May1985losses and later pre-date-agreement dispositions, restricted farm losses; affiliated/registered-plan/partial-repurchase stop losses and superficial-loss statutory exceptions; partial interests/sets/excluded PUP gifting arrangements: Check this point with one of our partner accountants.
- Ecological gifts, security exchanges, partnership/flow-through additional gains, charitable credit and T691AMT (including death/special-return exceptions): Check this point with one of our partner accountants.
- Historical T657reserve/trust/partnership charts, pre1992CNIL exceptions, missing prior-year forms and final2026annual Schedule3/T657/T936/T2091/T1A/T2017/T1170/T691fields: Check this point with one of our partner accountants.
- Late designations/amendments, death/special returns or evidence of trading (including options, short sales or frequent trading): Check this point with one of our partner accountants.

## Filing and payment

Report taxable/reportable capital dispositions in the sale/deemed-sale calendar year through Schedule3 and T1; retain the specific PUP no-report exception and the fully designated home directions. **2026:** ordinary filing30April2027; qualifying business filer/cohabiting spouse or common-law partner15June2027, unless tax-shelter-investment expenditures are primary, in which case30April2027. Balance payment30April2027. [G17][G19][G38]

**Dated2025bridge:** ordinary filing30April2026; qualifying self-employed filer/spouse15June2026, subject to the same statutory tax-shelter exception; balance30April2026. Ordinary half inclusion and the2025LCGE in the table apply. Carryback years2022–2024. The2024LCGE split and old reserve/allocations require their original-date charts, not a substituted2026ceiling. [G17][G21][G33]

## Completion checklist

Return a transaction/remaining-pool schedule with ownership, dates, currency, evidence, proceeds/ACB/outlays, special-rule decisions, reserve and form destinations; loss balances in original-year and current-rate units; family designations/elections; LCGE/CNIL history; exact annual form editions; dates and remaining holds. Do not infer accountant approval from a directory or a different method. No calculation here signs, submits, elects, designates or pays for a client. Keep unresolved outcomes explicitly non-usable.

## Sources

- [G01] [Official source](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-38.html). Read for ITA38(a),(a.1)–(a.3),(b): ordinary inclusion, specified gifts and loss fraction. Read 2026-11-27.
- [G02] [Official source](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-40.html). Read for ITA40(1)(a),(b),40(2)(a),(b),(g): gain/loss, ordinary reserve, residence/control prohibitions, full PRE formula/D and loss denials; special transfers remain held. Read 2026-11-27.
- [G03] [Official source](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-54.html). Read for individual PRE, personal-use/listed-property and complete superficial-loss definitions, including family and acquisition/right conditions. Read 2026-11-27.
- [G04] [Official source](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-110.6.html). Read for 110.6(1) annual/cumulative/CNIL and QSBC definition,110.6(2),(2.1),(5), eligible deduction limits, residence and relevant special-condition boundaries; full QFFP/transfer eligibility held. Read 2026-11-27.
- [G05] [Official source](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-111.html). Read for 111(1)(b),(1.1),(2),(3): carryover, rate conversion and special-death/pre1986 boundaries; special outcomes held. Read 2026-11-27.
- [G06] [Official source](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-117.1.html). Read for 117.1(2)(c) post2025indexation and adjacent rounding provisions; reconcile to published2026LCGE table. Read 2026-11-27.
- [G09] [Official source](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-47.html). Read for 47(1)–(3): remaining-pool averaging and debt/employee-security exceptions. Read 2026-11-27.
- [G10] [Official source](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-46.html). Read for 46(1)–(5):1,000floors, partial interests, sets and excluded-gift conditions. Read 2026-11-27.
- [G11] [Official source](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-41.html). Read for 41(1)–(3): separate LPP gain/loss,3/7year windows, oldest-first and prior-use limits. Read 2026-11-27.
- [G13] [Official source](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-12.html). Read for 12(12)–(14): housing/right definition, inventory exclusion, all nine causal events and loss denial. Read 2026-11-27.
- [G16] [Official source](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-220.html). Read for 220(3.2),(3.21),(3.5): discretionary late PRE application window/election status/penalty. Read 2026-11-27.
- [G17] [Official source](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-150.html). Read for 150(1)(d): ordinary and business/cohabiting-spouse deadlines, tax-shelter exception and special-death boundary. Read 2026-11-27.
- [G18] [Official source](https://www.canada.ca/en/revenue-agency/services/tax/individuals/frequently-asked-questions-individuals/adjustment-personal-income-tax-benefit-amounts.html). Read for 2026/2025LCGE gain/deduction rows, year-column headings and footnotes; historical2024figures only for held chart context. Read 2026-11-27.
- [G19] [Official source](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4037/capital-gains.html). Read for 2025T4037 ACB/costs/CAD FX, identical pools, T3box42/reset, stock splits, PUP floors/no-report and specialist boundaries; not the entire guide. Read 2026-11-27.
- [G20] [Official source](https://www.canada.ca/en/revenue-agency/services/tax/technical-information/income-tax/income-tax-folios-index/series-1-individuals/folio-3-family-unit-issues/income-tax-folio-s1-f3-c2-principal-residence.html). Read for PRE folio2.6–2.14 business/flipping/property/ordinary habitation/family and2.32–2.35land; change-of-use and estate outcomes remain held. Read 2026-11-27.
- [G21] [Official source](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/personal-income/line-12700-capital-gains/capital-losses-deductions.html). Read for ordinary netting/carryback/carryforward, historical rates, taxable-versus-net income, LCGE interaction and superficial-loss/basis passages; special losses held. Read 2026-11-27.
- [G22] [Official source](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-25300-net-capital-losses-other-years.html). Read for line25300 origin-year balances, oldest-first, different-rate adjustment and pre1986 referral boundary. Read 2026-11-27.
- [G26] [Official source](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5000-s3/5000-s3-25e.pdf). Read actual2025Schedule3 pages1–4: flipping/PRE, complete property/field rows, slips/reserve and ordinary/special partnership inclusion. Read 2026-11-27.
- [G27] [Official source](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t1a/t1a-25e.pdf). Read actual2025T1A Parts5–7: ordinary/LPP2022–2024carryback fields, remaining balances and certification. Read 2026-11-27.
- [G28] [Official source](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t936/t936-25e.pdf). Read actual2025T936 Parts1–3 and ChartA: CNIL components, prior-edition opening totals and T657 linkage. Read 2026-11-27.
- [G29] [Official source](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t657/t657-25e.pdf). Read actual2025T657 opening limits, annual Step1/cumulative Step2 and relevant original-year chart boundaries; historical chart application held. Read 2026-11-27.
- [G30] [Official source](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t2091ind/t2091ind-25e.pdf). Read actual2025T2091(IND) pages1–4: electronic/paper instructions, page2Section1/box1shortcut, page3Section2 and1994worksheet boundary. Read 2026-11-27.
- [G33] [Official source](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/important-dates-individuals.html). Read actual2025 ordinary/self-employed filing and payment dates and death-return qualification. Read 2026-11-27.
- [G38] [Official source](https://www.canada.ca/en/services/taxes/resources-for-small-and-medium-businesses/2026-tax-deadlines-canadian-businesses-self-employed-individuals.html). Read published2027 ordinary/self-employed filing/payment dates and primary-tax-shelter exception; not unrelated business deadlines. Read 2026-11-27.
- [G39] [Official source](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-257.html). Read full operative257 negative algebraic amount/number rule. Read 2026-11-27.
- [G41] [Official source](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t5008/t5008-26b.pdf). Read actual2026T5008first-page edition and field labels13–21; not a claim final2026annual return forms exist. Read 2026-11-27.
- [G42] [Official source](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4091/t5008-guide-return-securities-transactions.html). Read T4091boxes13–21: currency, settlement/aggregate1231, quantity/security/cost and gross proceeds; not the whole dealer-filing guide. Read 2026-11-27.
- [G43] [Official source](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/tax-slips/understand-your-tax-slips/t5-slips/t5008-statement-securities-transactions-slip-information-individuals.html). Read individualT5008book-value-versus-tax-ACB warning and business/capital route. Read 2026-11-27.
- [G44] [Official source](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t2017/t2017-25e.pdf). Read actual2025T2017 ordinary reserve/prior-ceiling and net67060→Schedule319200; special old/child/QBT/QCC/gift category outcomes held. Read 2026-11-27.
- [G45] [Official source](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t1170/t1170-25e.pdf). Read actual2025T1170eligible securities, gift-advantage proration and directed ordinary taxable-gain destinations; special exchange/flowthrough/AMT held. Read 2026-11-27.
- [G47] [Official source](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-38.2.html). Read full operative38.2 gift-advantage allocation. Read 2026-11-27.

- [G48] [Official source](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-248.html). Read248(1)complete small-business-corporation and eligible-relocation definitions, including connected assets/Canada/location/distance predicates; other definitions not certified. Read 2026-11-27.

Not yet confirmed: the specialist outcomes listed under When to refuse or refer; final2026annual form fields and historical chart applicability for any actual client. They are not usable filing conclusions. Original2026case inputs and the separate2025bridge are preserved. Historical proposal/cancellation commentary is not a source for the operative rate.
