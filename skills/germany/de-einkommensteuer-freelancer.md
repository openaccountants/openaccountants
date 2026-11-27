---
name: de-einkommensteuer-freelancer
description: "Compute 2026 German income tax on one resident self-employed person’s profit: EÜR, business expenses, assets, investment deductions, taxable income, tariff, splitting, solidarity surcharge, trade-tax credit, filing and payments. Collect the missing facts before using a worked case. Covers Freiberufler, Gewerbetreibende, Einkommensteuer Selbständige, Anlage EÜR and Anlage S/G."
version: 1.9
jurisdiction: DE
tax_year: 2026
last_updated: 2026-11-27
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: situation-rules
---

# Income tax for the self-employed in Germany

## Who this applies to

Compute the ordinary **2026** income tax of one individual resident in Germany with freelance or trade income. Residence or habitual abode in Germany establishes full income-tax liability ([§ 1(1) EStG](https://www.gesetze-im-internet.de/estg/__1.html)). This method assumes residence for the full year. Calculate tax on taxable income after deductions, then apply the relevant credits and surcharge; turnover is not taxable income.

Before calculating, obtain the activity and qualifications, residence dates, VAT status, bank and cash records, profit method and any bookkeeping notice, asset register, withdrawals/deposits, expense evidence, home-work days, other income, spouse/partner assessment choice, children, church/state, insurer certificates, loss notices and payments. Read the records before asking for missing facts. An unconfirmed deduction or credit stays unresolved; do not invent a zero or produce a final return from incomplete inputs.

**Freiberufler:** § 18 includes independently exercised scientific, artistic, writing, teaching and educational activities, the listed professions and similar professions; other self-employed work includes executors, asset administrators and supervisory-board members. Qualified staff are compatible with freelance status only where the owner leads and takes responsibility using their own expertise; temporary representation is allowed ([§ 18 EStG](https://www.gesetze-im-internet.de/estg/__18.html)). **Trade:** independently and sustainably participating in general economic activity for profit, excluding farming, a liberal profession and other self-employed work ([§ 15(2) EStG](https://www.gesetze-im-internet.de/estg/__15.html)). A job title alone does not settle classification. Similar professions, mixed activities and partnership taint/separability: Check this point with one of our partner accountants.

Use `de-freelance-intake` for start-up registration and questionnaire, and `germany-bookkeeping` for statutory/voluntary books, size limits, notices, succession, balance sheets and records. Do not assume freelance status always permits EÜR despite voluntary books/accounts. Registration timing and the correct receiving authority: Check this point with one of our partner accountants.

## Rates, bands and thresholds

The ordinary tariff below applies from assessment year 2026, subject to the special provisions listed in § 32a. Let x be taxable income rounded down to a full euro, y = (x − 12,348)/10,000 and z = (x − 17,799)/10,000. Round the resulting tax down to a full euro.

| Zone of taxable income (single) | From | To | Formula | Source |
| --- | --- | --- | --- | --- |
| 1, basic allowance | 0 | EUR 12,348 | tax = 0 | https://www.gesetze-im-internet.de/estg/__32a.html |
| 2 | EUR 12,349 | EUR 17,799 | (914.51 * y + 1400) * y | https://www.gesetze-im-internet.de/estg/__32a.html |
| 3 | EUR 17,800 | EUR 69,878 | (173.10 * z + 2397) * z + 1034.87 | https://www.gesetze-im-internet.de/estg/__32a.html |
| 4 | EUR 69,879 | EUR 277,825 | 0.42 * x - 11135.63 | https://www.gesetze-im-internet.de/estg/__32a.html |
| 5 | EUR 277,826 | none | 0.45 * x - 19470.38 | https://www.gesetze-im-internet.de/estg/__32a.html |

**Splitting:** qualifying spouses may choose joint assessment if both are fully liable under § 1(1)/(2) or § 1a, not permanently separated, and those conditions existed at the start or arose during the year. Either spouse can elect individual assessment; both choose joint assessment; absent a valid choice, joint assessment applies. Registered civil partners receive the spouse rules ([§ 26](https://www.gesetze-im-internet.de/estg/__26.html), [§ 2(8)](https://www.gesetze-im-internet.de/estg/__2.html)). For joint assessment, tax is twice the ordinary tax on half the joint taxable income ([§ 32a(5)](https://www.gesetze-im-internet.de/estg/__32a.html)). Widowed/remarried special splitting: Check this point with one of our partner accountants.

**Solidarity surcharge:** for assessment, recompute income tax with all eligible § 32 child allowances, without the Kindergeld add-back. The ordinary base includes the effect of the § 35 credit. Remove § 32d(3)/(4) income tax for the limit/mitigation test; that investment tax has its separate surcharge. The ordinary limit is EUR 20,350, or EUR 40,700 in § 32a(5)/(6) cases; equality means no ordinary surcharge. Above it take the lower of 5.5% of the ordinary base and 11.9% of its excess over the limit. Drop fractions of a cent; add the separate 5.5% surcharge on § 32d(3)/(4) tax where applicable ([§ 3](https://www.gesetze-im-internet.de/solzg_1995/__3.html), [§ 4 SolzG](https://www.gesetze-im-internet.de/solzg_1995/__4.html)). The cases below assume no children, flat-tax investment income or other base adjustments.

**Church tax:** establish membership, state, base adjustments, paid-tax deduction, actual rate and rounding; do not default to a national rate or use the illustrative percentages below as a liability. Check this point with one of our partner accountants.

## The taxable base

### EÜR and bank transactions

EÜR (§ 4(3)) is available only if there is no legal duty to keep books and regular accounts **and** no voluntary books and accounts. Profit is business receipts less business expenses; pass-through sums received and spent in another's name and for their account are excluded. GWG, pooling, depreciation and the special asset registers still apply; specified non-depreciable assets, shares, securities/comparable rights and current-asset land/buildings have special cost-recognition timing ([§ 4(3) EStG](https://www.gesetze-im-internet.de/estg/__4.html)). Refer those asset-disposal cases before deducting their purchase costs. The prescribed EÜR dataset is electronic; the office may waive this on application for undue hardship, then a prescribed paper calculation is required ([§ 60(4) EStDV](https://www.gesetze-im-internet.de/estdv_1955/__60.html)).

Ordinary cash receipts belong to the year received and payments to the year paid. Regularly recurring items received/paid shortly around year end belong to their economically related year; prepaid use-right expenses covering more than five years are spread, subject to the statutory market-discount exception ([§ 11 EStG](https://www.gesetze-im-internet.de/estg/__11.html)). The precise year-end/due-date test, asset disposals and mixed VAT timing: Check this point with one of our partner accountants.

Business expenses are costs caused by the business, subject to specific disallowances ([§ 4(4)/(5)](https://www.gesetze-im-internet.de/estg/__4.html)). Match each bank line to its invoice and purpose: client fees/platform settlements; rent, software, supplies, advertising, fees, chamber dues and insurance; entertainment/gifts; home/car/travel; assets; insurance contributions; taxes; own-account transfers, loan principal, deposits/withdrawals; wages, letting and investments. A bank label alone proves neither business purpose nor immediate deduction. Reconcile VAT and other-income components separately. Private cash withdrawals need their use established.

Private living costs and income/personal taxes and related ancillary amounts are excluded, subject to the statute's express deduction exceptions ([§ 12 EStG](https://www.gesetze-im-internet.de/estg/__12.html)); trade tax and related ancillary amounts are not business expenses ([§ 4(5b)](https://www.gesetze-im-internet.de/estg/__4.html)). Health/pension deductions belong in the personal stage below. Fines, warning fines, penalties and disgorgement exceptions: Check this point with one of our partner accountants.

### Business expenses

- **Home days:** EUR 6 per qualifying calendar day, at most EUR 1,260 across all business/professional activities. Ordinarily work must be mainly at home with no visit to an outside first workplace. If no other workplace is permanently available, the day can also include outside/first-workplace work. No day deduction to the extent accommodation costs fall under no. 6a/§ 9(1) no. 5 or a room deduction under no. 6b applies ([§ 4(5) no. 6c](https://www.gesetze-im-internet.de/estg/__4.html)).
- **Separate home office:** room/furnishing costs are excluded unless the room is the centre of the entire business/professional activity. Then actual costs or EUR 1,260 yearly are possible; reduce the yearly amount by one twelfth per full nonqualifying month. Record room costs separately as § 4(7) requires ([§ 4(5) no. 6b and (7)](https://www.gesetze-im-internet.de/estg/__4.html)). Establish qualifying room and attributable costs before applying this.
- **Business entertainment:** 70% of reasonable, proved business-contact entertainment costs. Written proof includes place, day, participants, occasion and cost; restaurant entertainment needs participants/occasion and the attached invoice. Keep it separately recorded or no deduction ([§ 4(5) no. 2 and (7)](https://www.gesetze-im-internet.de/estg/__4.html)). Input-VAT recovery is a separate eligibility/documentation question: Check this point with one of our partner accountants.
- **Gifts to non-employees:** the year's acquisition/production costs of gifts to one recipient must not exceed EUR 50; above that the whole deduction is excluded. Keep the separately required records ([§ 4(5) no. 1 and (7)](https://www.gesetze-im-internet.de/estg/__4.html)). Establish VAT cost treatment and recipient totals first; employee gifts and recipient taxation are not determined here.
- **Phone/internet and mixed costs:** obtain the supported business share; do not import an employee flat rate. Unexplained/private costs remain unresolved.
- **Cars and commuting:** private-use valuation, business-use percentage, list-price/logbook choice, commuting adjustment, distance/attendance conditions, electric/hybrid relief and family-home trips require their complete method. Check this point with one of our partner accountants. Preserve the original ordinary-car checkpoint as **arithmetic only, non-usable for deduction**: list price EUR 40,000, 20 full km, 12 months, 200 days; 0.0003 × 40,000 × 20 × 12 = 2,880; 0.38 × 20 × 200 = 1,520; difference 1,360. Assumed actual commuting costs 1,000/2,000 give positive differences 0/480. Private-use add-back is unresolved separately.
- **Business travel/meals:** private-car mileage versus commuting, domestic full-day/arrival/departure/eight-hour branches, supplied meals/three-month limit and foreign country rates (including Austria): Check this point with one of our partner accountants.
- **Business loan interest:** overwithdrawal definition, prior balances, fixed-asset financing, EUR 2,050 cap component and mixed debt allocation: Check this point with one of our partner accountants. Do not deduct all interest merely because the bank labels it a business loan.
- **Flat expenses for main writers/journalists and side-line scientific/artistic/writing/teaching/examining work:** eligibility and replacement of actual expenses: Check this point with one of our partner accountants.

### Assets and investment deductions

**GWG:** for independently usable depreciable movable fixed assets, § 6(2) permits an immediate deduction when individual cost **less contained VAT for the threshold test** is no more than EUR 800. Technical dependence on other coordinated assets defeats independent use. Values above EUR 250 need a running register with date and cost unless those particulars are in the books. Recoverable input VAT is excluded from acquisition cost; do not confuse that with the threshold test ([§ 6(2)](https://www.gesetze-im-internet.de/estg/__6.html), [§ 9b](https://www.gesetze-im-internet.de/estg/__9b.html)). For the old chair case (2025 turnover EUR 22,000, 2026 forecast EUR 24,000; chair EUR 952 = EUR 800 + EUR 152 VAT), **assuming** eligible independent business use, those VAT components and the stated VAT-recovery status: the threshold test is EUR 800 in both cases; immediate deduction can be EUR 952 without recovery, or EUR 800 with EUR 152 recovered separately. Actual KU eligibility is held below; a forecast does not establish it.

**Pool instead:** the same independently usable depreciable movable fixed-asset conditions apply. Cost less contained VAT must be **over EUR 250 and no more than EUR 1,000**. The annual pool is released one fifth in its formation year and each of four following years; disposal of an item does not reduce it. Apply the election consistently to all qualifying acquisitions/manufactures/contributions of that financial year; the associated immediate-expense ceiling is EUR 250 ([§ 6(2a)](https://www.gesetze-im-internet.de/estg/__6.html)).

**Ordinary depreciation:** spread cost over useful life; in the acquisition/manufacture year deduct one twelfth less per full preceding month. Eligible movable fixed assets acquired/manufactured after 30 June 2025 and before 1 January 2028 may instead use declining balance at at most three times the straight-line rate and at most 30%, on remaining book value; first-year month reduction still applies. No extraordinary technical/economic depreciation alongside that method ([§ 7(1)/(2)](https://www.gesetze-im-internet.de/estg/__7.html)).

**Computers/software:** the BMF letter permits one-year useful life for its defined equipment/software; check the exhaustive computer categories, manufacturer product documentation and software definition in paragraphs 2–5. It remains § 7(1) depreciation, starts on acquisition/manufacture and requires the asset register. Paragraph 1.4 accepts full depreciation in that year, despite the ordinary month rule; it is not automatic immediate expensing of every electronic device. Applies to profit years ending after 31 December 2020 ([BMF 22 February 2022, paragraphs 1–6](https://usth.bundesfinanzministerium.de/esth/2022/C-Anhaenge/Anhang-01/V/anhang-1-V.html?nn=104174)).

**§ 7g investment deduction:** for future depreciable movable fixed assets that will be let or used exclusively/almost exclusively in a domestic establishment at least through the end of the financial year following acquisition/manufacture, up to 50% of expected cost may be deducted. Profit must be determined under § 4/§ 5 and no more than EUR 200,000 **before IAB deductions and § 7g(2) add-backs**; EUR 200,001 fails. Transmit prescribed datasets for deductions/add-backs/reversals, unless the office grants a hardship waiver and the filed documents supply the sums. A loss may result. Separately, total unadded/unreversed deductions of the year and three previous years must not exceed EUR 200,000 per business ([§ 7g(1)](https://www.gesetze-im-internet.de/estg/__7g.html)). Do not infer the business-use test from an asset's label.

In the investment year add back up to 50% of actual cost, limited to available deductions; cost may be reduced by no more than that add-back, correspondingly reducing depreciation/GWG/pool basis. For an IAB first claimed after the initial assessment/determination becomes final, the asset must not already have been acquired/manufactured when the claim is made. Unadded deductions must be reversed in their original year by the end of the third following financial year; purchase alone is insufficient. Failure of the required letting/domestic-use period reverses the cost reduction, reduced basis and add-back; final assessments can be changed and § 233a(2a)'s later interest start is excluded ([§ 7g(2)–(4)](https://www.gesetze-im-internet.de/estg/__7g.html)).

Special depreciation of up to 40% over the purchase/manufacture year and four following years requires a qualifying depreciable movable fixed asset, the § 7g profit limit in the preceding financial year and qualifying letting/domestic use in the acquisition/manufacture year **and** following year; reversal provisions apply ([§ 7g(5)/(6)](https://www.gesetze-im-internet.de/estg/__7g.html)). Partnership allocations and disputed use/foreign leasing: Check this point with one of our partner accountants. The separate electric-vehicle depreciation schedule, vehicle eligibility, acquisition dates and interaction with special depreciation: Check this point with one of our partner accountants.

### From profit to taxable income

Combine the relevant income categories; apply the statutory total-income adjustments, losses, special expenses/extraordinary burdens and child/other allowances, then the tariff and credits ([§ 2(2)–(6)](https://www.gesetze-im-internet.de/estg/__2.html)). Capital income under § 32d(1)/§ 43(5) is outside these income totals under § 2(5b). Check losses and child/benefit adjustments rather than assuming none.

- **Pension:** statutory/professional schemes, certified Rürup contracts, age/benefit restrictions, employer-share additions/subtractions and the indexed cap/reductions require the actual certificate. Check this point with one of our partner accountants. The examples stipulate already established deductible amounts; payments alone do not prove them.
- **Basic health/care:** use actual qualifying statutory/basic private health and mandatory care cover. Where statutory health contributions can provide sick pay, reduce them by 4%; private cover counts only for the equivalent statutory level. Check eligible provider/certified data, refunds/subsidies, tax-free-income connections and prepaid contributions before deducting ([§ 10(1) no. 3, (2), (4b)](https://www.gesetze-im-internet.de/estg/__10.html)).
- **Other insurance:** § 10(1) no. 3/3a expenses have a combined EUR 2,800 cap, reduced to EUR 1,900 where health-cost cover/refunds are available partly/wholly without own expense or the named § 3 no. 9/14/57/62 benefits are provided. Joint spouses add their individual caps. If qualifying basic health/care exceeds that combined ceiling, deduct it instead and no additional no. 3a insurance ([§ 10(4)](https://www.gesetze-im-internet.de/estg/__10.html)).
- **Special-expense lump sum:** EUR 36, doubled for joint spouses, only for § 10(1) nos. 4, 5, 7, 9, (1a) and § 10b expenses unless proved higher. It is separate from insurance deductions ([§ 10c](https://www.gesetze-im-internet.de/estg/__10c.html)).
- **Losses:** same-year set-off, carry-back/waiver, carry-forward limits, year-end determination and resulting filing duties, including the 2024–2027 versus later-year rules: Check this point with one of our partner accountants. Do not set a loss to zero or silently apply a later year's limits.

### Trade-tax credit

For an ordinary sole trader, start with established Gewerbeertrag, not automatically business profit. Round it down to EUR 100; deduct up to the EUR 24,500 allowance without going below zero, then apply the ordinary 3.5% base rate ([§ 11 GewStG](https://www.gesetze-im-internet.de/gewstg/__11.html)). Home-industry reduced-rate cases, add-backs/deductions/losses, actual municipal multiplier and its statutory minimum/transition: Check this point with one of our partner accountants. Use the issued base/tax notices for a real credit; the examples stipulate ordinary rates, no adjustments/losses and the municipal multiplier.

Under [§ 35(1) EStG](https://www.gesetze-im-internet.de/estg/__35.html), reduce the eligible sole trader's same-year income tax by at most four times the established Messbetrag, limited both to actual trade tax payable and to its share of the relevant income tax. The share is positive qualifying trade income divided by all positive income, times reduced tariff tax. Apply the statute's other-reduction/foreign-credit ordering and exclude trade profits barred from § 35; use notices. Do not treat four times Messbetrag as a refundable balance or a credit for a different year. With only ordinary qualifying trade income and no competing reductions, the share cap is the whole tariff tax, as in the examples.

## Deadlines and filing

Check the actual filing duty, demands and wage/side-income exceptions before treating the ordinary deadlines as applicable. The former EUR 410 shorthand and 2025-to-2026 form/box assumptions are not sufficient to file a return. Main form ESt 1 A, Anlage S/G, EÜR/AVEÜR, Vorsorgeaufwand and Sonderausgaben are retained as document subjects; confirm the year's actual form mapping. Check this point with one of our partner accountants.

For business income, § 25(4) generally requires electronic filing, except § 46(2) nos. 2–8 assessment cases; the office may waive it for undue hardship on application ([§ 25(4)](https://www.gesetze-im-internet.de/estg/__25.html)).

| Ordinary required-return deadline, subject to individual demands/extensions | 2026 return | 2025 return | Source |
| --- | --- | --- | --- |
| Own return: seven months after year end; weekend/public holiday moves to next working day | Monday 2 August 2027 (31 July is Saturday) | Friday 31 July 2026 | https://www.gesetze-im-internet.de/ao_1977/__149.html ; https://www.gesetze-im-internet.de/ao_1977/__108.html |
| Covered adviser-prepared return; voluntary § 46(2) no. 8 excluded; earlier call possible | Tuesday 29 February 2028 | Monday 1 March 2027 (28 February is Sunday) | https://www.gesetze-im-internet.de/ao_1977/__149.html ; https://www.gesetze-im-internet.de/ao_1977/__108.html |

Earlier calls under § 149(4) require four months after notice and cannot shorten the ordinary seven-month period. Pandemic transitional extensions cover 2020–2024, not these years ([Art. 97 § 36 EGAO](https://www.gesetze-im-internet.de/aoeg_1977/art_97__36.html)). Hardship/extensions under § 109 and any local public holiday or special-year circumstances: Check this point with one of our partner accountants.

Ordinary income-tax prepayments fall on 10 March, 10 June, 10 September and 10 December, set by notice generally using the last assessment after withholding credits. Initial amounts are set only if at least EUR 400 per calendar year **and** EUR 100 per due date ([§ 37](https://www.gesetze-im-internet.de/estg/__37.html)); actual notice/weekend rules control payment dates. Arithmetic: a stipulated EUR 10,548 annual notice split equally is EUR 2,637 on each date. First-year estimates, later adjustments, post-year increases and additional due dates: Check this point with one of our partner accountants.

Credit paid prepayments and eligible attributable tax withheld. The balance is due within one month after notice; the part matching due unpaid prepayments is immediate ([§ 36(2)/(4)](https://www.gesetze-im-internet.de/estg/__36.html)).

## Penalties and interest

**Annual late return:** § 152 allows a discretionary surcharge unless delay is excusable; representatives' fault is attributed. Normally it becomes mandatory after 14 months from year end, or on missing a § 149(4) early-demand date. The automatic rule does not apply if the deadline is extended/retroactively extended, tax is nil/negative or assessed tax does not exceed **assessed** prepayments plus creditable withheld tax; discretion remains. For an ordinary annual income-tax return, each started late month is 0.25% of tax less those prepayments/withholding, minimum EUR 25; round down to whole euros, maximum EUR 25,000. For a first demand after the legal deadline where the person could previously assume no filing duty, only months starting after the demanded deadline count ([§ 152(1)–(3), (5), (10)](https://www.gesetze-im-internet.de/ao_1977/__152.html)). Original case: 2026, no adviser/extension, three months and five days after 2 August 2027, residual base EUR 2,000: 0.25% × 2,000 = 5, so four started months × 25 = EUR 100 **if discretion is exercised**. The delay is measured from the actual filing deadline, not from year end.

**Late payment:** assessed/declared overdue tax attracts 1% per started month on the amount rounded down to the next EUR 50. No surcharge before assessment/declaration or on ancillary amounts. There is a grace period for delay up to three days, except § 224(2) no. 1 payments ([§ 240](https://www.gesetze-im-internet.de/ao_1977/__240.html)).

**Assessment/refund interest:** ordinary start versus retrospective events/losses, full months, rate, rounded base, refunds and payment dates: Check this point with one of our partner accountants. **Evasion (§ 370), reckless understatement (§ 378), fines and correction obligations:** Check this point with one of our partner accountants.

## Cross-border points

VAT status, KU turnover/start-up/exceeding/waiver tests, gross/net EÜR recording, year-end VAT, input-tax documents, foreign clients and EU services/recaps: use `germany-vat-return` and `de-vat-annual-and-special-schemes`. Do not infer status from a bank total or forecast. Check this point with one of our partner accountants.

Part-year residence/partnerships: `de-partners-and-part-year`; non-residents and foreign credits: `de-non-resident-tax`; treaty withholding: `de-treaty-withholding-rates`; leaving with holdings: `leaving-germany-exit-tax`. Treaty exemption, foreign establishments, progression and its exceptions, § 34/§ 34a extraordinary/retained profits, disposal/closure, different currencies and disputed classifications are non-usable holds here. Check this point with one of our partner accountants.

Other routes: corporate form `de-corporate-tax`/`germany-formation`; wages `de-employee-income-tax`; letting `de-rental-income`; investments `de-capital-gains`; crypto `de-crypto-tax`; staff `de-payroll`; contributions `de-social-contributions`; payments `de-estimated-tax`; records `germany-bookkeeping`.

## Worked examples

These are conditional computations, not findings that the supplied costs qualify. Assume full-year residence, ordinary tariff, no child/foreign/special-rate adjustments or other income except as stated, verified EÜR/VAT treatment and already established deductible personal amounts. The statutory conditions above still apply. Church calculations are preserved **arithmetic on the originally assumed 9%, not usable church-tax liabilities**. Real church base/rate/rounding and paid-tax deductions remain held.


**Example 1: translator (Freiberufler), zone 3, home office day rate.** A single translator, EÜR, Kleinunternehmer not used. Receipts EUR 72,000; other business expenses EUR 12,000; 150 days worked mainly at home, no centre-of-work room, and no outside first-workplace visit or overlapping accommodation deduction on those days, so 150 x EUR 6 = EUR 900 day rates (under the EUR 1,260 cap). Profit EUR 59,100. Qualifying pension and health expenses are stipulated at EUR 9,100, with no higher § 10c-category expenses: also deduct EUR 36. Taxable income is EUR 49,964. Zone 3: z = (49,964 − 17,799)/10,000 = 3.2165; raw tax EUR 10,535.690986475, rounded down to EUR 10,535. No ordinary surcharge on the stipulated base. Assumed 9% arithmetic gives EUR 948.15; actual church tax remains held. The former EUR 50,000 taxable income/EUR 10,548 tax/EUR 949.32 assumed church arithmetic omitted the separate EUR 36 and is not this case's result. The separate splitting checkpoint below intentionally stipulates EUR 100,000 joint taxable income.


```oa-check
name: DE 2026 translator, zone 3, home office day rate
inputs:
  receipts: 72000
  other_expenses: 12000
  home_days: 150
  special_expenses: 9100
steps:
  - day_rates: min(home_days * 6, 1260)
  - profit: receipts - other_expenses - day_rates
  - taxable: floor(profit - special_expenses - 36)
  - z: (taxable - 17799) / 10000
  - tax: floor((173.10 * z + 2397) * z + 1034.87)
  - soli: 0
  - church: tax * 0.09
expected:
  day_rates: 900
  profit: 59100
  taxable: 49964
  tax: 10535
  church: 948.15
```

**Example 2: consultant with an Investitionsabzugsbetrag, surcharge sliding zone.** A single IT consultant plans to buy equipment costing EUR 20,000 next year. Profit before the deduction EUR 100,000, within the EUR 200,000 tested-profit limit. Assume qualifying equipment, the required letting/domestic-use period, prescribed reporting and sufficient unused deduction capacity, so 50% x 20,000 = EUR 10,000 comes off: profit EUR 90,000. Total special expenses EUR 9,700 (including any § 10c amount): taxable income EUR 80,300, zone 4. Tax 0.42 x 80,300 - 11,135.63 = 22,590.37, so EUR 22,590. Surcharge: 5.5% x 22,590 = EUR 1,242.45; cap 11.9% x (22,590 - 20,350) = EUR 266.56; the lower, EUR 266.56, applies. The EUR 10,000 must be added back to an eligible investment by the end of the third following financial year; otherwise reverse the 2026 deduction under § 7g(3). The year of purchase also needs the add-back/cost-basis calculation above; acquisition alone does not close the IAB.

```oa-check
name: DE 2026 consultant, § 7g deduction and surcharge sliding zone
inputs:
  profit_before: 100000
  planned_cost: 20000
  special_expenses: 9700
steps:
  - iab: planned_cost * 0.5
  - profit: profit_before - iab
  - taxable: floor(profit - special_expenses)
  - tax: floor(0.42 * taxable - 11135.63)
  - soli_full: tax * 0.055
  - soli_cap: (tax - 20350) * 0.119
  - soli: min(soli_full, soli_cap)
expected:
  iab: 10000
  profit: 90000
  taxable: 80300
  tax: 22590
  soli_full: 1242.45
  soli_cap: 266.56
  soli: 266.56
```

**Example 3: sole trader with the § 35 credit, Hebesatz 400%.** A single online retailer (trade, § 15 EStG). Trade profit EUR 110,000, his only income; total special expenses EUR 10,000 (including any § 10c amount), so taxable income EUR 100,000, zone 4. Tariff tax 0.42 x 100,000 - 11,135.63 = 30,864.37, so EUR 30,864. Trade tax: trade income EUR 110,000 (already a multiple of EUR 100) less the EUR 24,500 allowance = EUR 85,500; base amount 85,500 x 3.5% = EUR 2,992.50 ([§ 11 GewStG](https://www.gesetze-im-internet.de/gewstg/__11.html)); at a 400% Hebesatz the municipality charges EUR 11,970. Credit: 4 x 2,992.50 = EUR 11,970. First cap: all his income is trade income, so the share of tariff tax on it is the full EUR 30,864. Second cap: trade tax payable EUR 11,970. The credit is EUR 11,970 ([§ 35(1) EStG](https://www.gesetze-im-internet.de/estg/__35.html)). Income tax EUR 18,894, below EUR 20,350, so no surcharge. The original assumed church arithmetic is 9% × 30,864 = EUR 2,777.76; the actual church-tax base and liability are held. Income tax plus stipulated trade tax is EUR 30,864. At this 400% input the stipulated trade tax is fully offset within both caps; that result does not establish eligibility in another case.


```oa-check
name: DE 2026 sole trader, § 35 trade tax credit at Hebesatz 400%
inputs:
  trade_profit: 110000
  special_expenses: 10000
  hebesatz_pct: 400
steps:
  - taxable: floor(trade_profit - special_expenses)
  - tariff_tax: floor(0.42 * taxable - 11135.63)
  - trade_income: floor(trade_profit / 100) * 100
  - messbetrag: max(0, trade_income - 24500) * 0.035
  - trade_tax: messbetrag * hebesatz_pct / 100
  - cap_share: tariff_tax * trade_profit / trade_profit
  - credit: min(4 * messbetrag, cap_share, trade_tax)
  - income_tax: tariff_tax - credit
  - church: tariff_tax * 0.09
expected:
  taxable: 100000
  tariff_tax: 30864
  messbetrag: 2992.5
  trade_tax: 11970
  credit: 11970
  income_tax: 18894
  church: 2777.76
```

Assume spouses eligible for and using joint assessment, no competing relief or child-base adjustment. A married couple with the same EUR 100,000 joint taxable income under splitting pays twice the tax on EUR 50,000: 2 x 10,548 = EUR 21,096, against EUR 30,864 for one single person; their EUR 40,700 surcharge limit is not exceeded.

**Example 4: Freiberufler designer, from the bank statement to the balance due.** Anna is a self-employed designer in Hamburg, single, no church, normal VAT scheme. 2026 fees net of VAT EUR 72,000. Ordinary costs (software, studio share, insurance, adviser) EUR 9,000. A client dinner EUR 400 net. A gift to one client EUR 80. 140 days worked mainly at home without going to the studio, no separate room or overlapping accommodation deduction. Assume documented reasonable entertainment, separate entertainment/gift records, the gift is to a non-employee and the only gift to that recipient, and the laptop meets the BMF definitions/documentation, is wholly business-used and acquired/available in 2026 with full purchase-year depreciation applied. All VAT she collected in 2026 she also paid over in 2026, so VAT nets to nil in the EÜR. A laptop for EUR 1,800 net. Basic health and care cover per the insurer's certificate (already net of the 4% cut) EUR 7,200. Private pension (Rürup) EUR 3,000, stipulated fully qualifying and deductible. No higher § 10c-category expenses. Prepayments paid EUR 10,000. (Invented case.) Dinner: 70% x 400 = EUR 280. Gift: over EUR 50, so EUR 0. Home office: 140 x 6 = EUR 840. Laptop: the stipulated BMF purchase-year depreciation treatment, EUR 1,800. Profit: 72,000 - 9,000 - 280 - 0 - 840 - 1,800 = EUR 60,080. Taxable income: 60,080 - 7,200 - 3,000 - 36 (lump sum) = EUR 49,844, zone 3. z = 3.2045; tax = (173.10 x 3.2045 + 2,397) x 3.2045 + 1,034.87 = 10,493.59, so EUR 10,493. Below EUR 20,350: no surcharge. Balance: 10,493 - 10,000 = EUR 493, due one month after the notice.

```oa-check
name: DE 2026 Freiberufler designer, single, profit from EÜR items, zone 3
inputs:
  fees: 72000
  ordinary_costs: 9000
  dinner: 400
  gift: 80
  home_days: 140
  laptop: 1800
  basic_cover: 7200
  pension: 3000
  prepaid: 10000
steps:
  - dinner_deductible: dinner * 0.70
  - gift_deductible: 0
  - home_office: min(home_days * 6, 1260)
  - profit: fees - ordinary_costs - dinner_deductible - gift_deductible - home_office - laptop
  - taxable: floor(profit - basic_cover - pension - 36)
  - z: (taxable - 17799) / 10000
  - tax: floor((173.10 * z + 2397) * z + 1034.87)
  - balance: tax - prepaid
expected:
  profit: 60080
  taxable: 49844
  tax: 10493
  balance: 493
```

`gift_deductible` is 0 because the EUR 80 gift is over the EUR 50 limit, so none of it counts.

**Example 5: sole trader with the § 35 credit capped by the trade tax payable, Hebesatz 360%.** Bernd runs an online shop in a town with a trade tax multiplier of 360%. 2026 profit EUR 95,000, his only income; no trade tax add-backs. Single, church member at 9%. Special expenses: basic health and care cover EUR 9,000, pension EUR 6,000. 2026 is his first year of trading, so no church tax or prepayments were paid in it and the EUR 36 lump sum applies. (Invented case; the multiplier is an input, each town sets its own.) Trade tax: 95,000 - 24,500 = 70,500 x 3.5% = Messbetrag EUR 2,467.50; x 360% = EUR 8,883. Not deductible, so profit stays EUR 95,000. Taxable income: 95,000 - 9,000 - 6,000 - 36 = EUR 79,964, zone 4: 0.42 x 79,964 - 11,135.63 = 22,449.25, so EUR 22,449. Credit: 4 x 2,467.50 = EUR 9,870. Cap on the trade share: all income is trade, so EUR 22,449. Cap on trade tax payable: EUR 8,883. The lowest is EUR 8,883; the other EUR 987 is lost. Income tax 22,449 - 8,883 = EUR 13,566. Below EUR 20,350: no surcharge. Original assumed church arithmetic: 9% × 22,449 = EUR 2,020.41; actual base/rate/rounding remain held. Compared with Example 3, the 360% input makes actual trade tax the binding cap. No unused notional difference is treated as a refund or carried to another year.


```oa-check
name: DE 2026 sole trader, § 35 credit capped by trade tax payable, church tax base
inputs:
  profit: 95000
  hebesatz: 3.60
  basic_cover: 9000
  pension: 6000
steps:
  - trade_income: floor(profit / 100) * 100
  - messbetrag: (trade_income - 24500) * 0.035
  - trade_tax: messbetrag * hebesatz
  - taxable: floor(profit - basic_cover - pension - 36)
  - tariff_tax: floor(0.42 * taxable - 11135.63)
  - credit: min(4 * messbetrag, tariff_tax, trade_tax)
  - income_tax: tariff_tax - credit
  - church_tax: tariff_tax * 0.09
expected:
  messbetrag: 2467.50
  trade_tax: 8883
  taxable: 79964
  tariff_tax: 22449
  credit: 8883
  income_tax: 13566
  church_tax: 2020.41
```

In `credit`, the second term is the tax on trade income: here trade income is all the income, so the share is the whole tariff tax.

## Ask the client first

Resolve the record requests at the top before finalising: classify each activity; confirm EÜR/books and VAT; reconcile cash/bank, assets and private use; prove home/entertainment/gift costs; obtain insurance and loss certificates, family/church details and actual notices/payments. Keep every referral above as an explicit open dependency for the real return. Check this point with one of our partner accountants.

## Sources

Reused operative reads are dated 26 November; newly read provisions are dated 27 November. Read dates do not imply an accountant has approved the Guide.

| Official source and operative unit | URL | Read on |
| --- | --- | --- |
| Residence § 1; classification §§ 15(2), 18 | https://www.gesetze-im-internet.de/estg/__1.html ; https://www.gesetze-im-internet.de/estg/__15.html ; https://www.gesetze-im-internet.de/estg/__18.html | 2026-11-26 |
| EÜR/expenses/records § 4(3)–(7); GWG/pool § 6(2)/(2a); § 9b | https://www.gesetze-im-internet.de/estg/__4.html ; https://www.gesetze-im-internet.de/estg/__6.html ; https://www.gesetze-im-internet.de/estg/__9b.html | 2026-11-27 |
| Timing § 11; excluded private/tax costs § 12; ordinary depreciation § 7(1)/(2) | https://www.gesetze-im-internet.de/estg/__11.html ; https://www.gesetze-im-internet.de/estg/__12.html ; https://www.gesetze-im-internet.de/estg/__7.html | 2026-11-27 |
| BMF computer letter 22 February 2022, paragraphs 1–6 | https://usth.bundesfinanzministerium.de/esth/2022/C-Anhaenge/Anhang-01/V/anhang-1-V.html?nn=104174 | 2026-11-27 |
| Investment deduction/special depreciation § 7g(1)–(6) | https://www.gesetze-im-internet.de/estg/__7g.html | 2026-11-27 |
| Base § 2(2)–(8); joint assessment § 26; tariff § 32a(1)/(5) | https://www.gesetze-im-internet.de/estg/__2.html ; https://www.gesetze-im-internet.de/estg/__26.html ; https://www.gesetze-im-internet.de/estg/__32a.html | 2026-11-26 |
| Health/insurance § 10(1) no. 3, (2), (4)/(4b); § 10c | https://www.gesetze-im-internet.de/estg/__10.html ; https://www.gesetze-im-internet.de/estg/__10c.html | 2026-11-26 |
| Solidarity surcharge §§ 3/4, 2026 limits | https://www.gesetze-im-internet.de/solzg_1995/__3.html ; https://www.gesetze-im-internet.de/solzg_1995/__4.html | 2026-11-26 |
| Trade base § 11; income-tax credit § 35(1) | https://www.gesetze-im-internet.de/gewstg/__11.html ; https://www.gesetze-im-internet.de/estg/__35.html | 2026-11-27 |
| Electronic return § 25(4); EÜR § 60(4) EStDV | https://www.gesetze-im-internet.de/estg/__25.html ; https://www.gesetze-im-internet.de/estdv_1955/__60.html | 2026-11-26 |
| Required-return dates AO §§ 149/108; pandemic transition EGAO Art. 97 § 36 | https://www.gesetze-im-internet.de/ao_1977/__149.html ; https://www.gesetze-im-internet.de/ao_1977/__108.html ; https://www.gesetze-im-internet.de/aoeg_1977/art_97__36.html | 2026-11-26 |
| Prepayments § 37(1)/(3)/(5); credit/payment § 36(2)/(4) | https://www.gesetze-im-internet.de/estg/__37.html ; https://www.gesetze-im-internet.de/estg/__36.html | 2026-11-26 |
| Annual late return AO § 152(1)–(3)/(5)/(10); late payment § 240 | https://www.gesetze-im-internet.de/ao_1977/__152.html ; https://www.gesetze-im-internet.de/ao_1977/__240.html | 2026-11-26 |

Not yet confirmed: the actual outcomes for the explicitly referred cases above. They are non-usable holds, not rates or conclusions to apply to a return. Check this point with one of our partner accountants.
