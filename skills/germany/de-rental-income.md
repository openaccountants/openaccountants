---
name: de-rental-income
description: "German private rental income for 2026: receipts, expenses, building depreciation, new rental flats, maintenance, below-market rents, property sales and ELSTER. Trigger on Mieteinnahmen, Vermietung, Anlage V, AfA, Werbungskosten, Erhaltungsaufwand and verbilligte Vermietung. Includes dated historical cases and explicit specialist holds."
version: 1.9
jurisdiction: DE
tax_year: 2026
last_updated: 2026-11-27
depends_on:
  - de-einkommensteuer-freelancer
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: situation-rules
---

# Rental income tax in Germany 2026 (Vermietung und Verpachtung)

> **General reference only.** This skill is general tax reference material for AI-assisted work. It has not been reviewed for any specific landlord's facts. A Steuerberater should confirm results before a return is filed.

## Who this applies to

Individuals letting privately held land, buildings, flats or rooms. [§ 21(1), (3) EStG](https://www.gesetze-im-internet.de/estg/__21.html) covers immovable property, bundles of movable assets, temporary rights and rent claims, but assigns income to another income category where it belongs there. Business property, trading partnerships, property trading and hotel services: Check this point with one of our partner accountants. See `de-trade-tax`.

This computes the rental result before the personal tariff. Use `de-einkommensteuer-freelancer` for the tariff, solidarity surcharge and church tax. Current rules are for 2026; dated historical examples retain their original years. Establish completion/acquisition dates, prior AfA, land split, ownership/use, actual and market rents and all works since purchase before calculating. Missing facts stop the computation; do not assume housing use or capitalise an uncertain repair by default.

## Rates, bands and thresholds

Figures below are gateways; all conditions in the base section must also hold.

| Item | Figure and condition | Official source |
|---|---|---|
| Ordinary private building, completed after 2022 / during 1925–2022 / before 1925 | Straight-line AfA 3% / 2% / 2.5% annually; prorate first year | https://www.gesetze-im-internet.de/estg/__7.html |
| Eligible housing under § 7(5a) | 5% of remaining value; construction start or binding acquisition contract after 30 September 2023 and before 1 October 2029 | https://www.gesetze-im-internet.de/estg/__7.html |
| Eligible new rental flat, § 7b | Up to 5% of capped base in acquisition/completion year and three following years; old-window claims end with 2026 | https://www.gesetze-im-internet.de/estg/__7b.html; https://www.gesetze-im-internet.de/estg/__52.html |
| § 7b new / old application window | Cost ceiling EUR 5,200 / EUR 3,000 per m²; base cap EUR 4,000 / EUR 2,000 per m², subject to all conditions below | https://www.gesetze-im-internet.de/estg/__7b.html |
| Acquisition-related works | Capitalise qualifying works within three years if aggregate cost without VAT exceeds 15% of building acquisition cost | https://www.gesetze-im-internet.de/estg/__6.html |
| Larger maintenance, eligible private mainly residential building | Even spread over two to five years; housing area must exceed half of usable area | https://www.gesetze-im-internet.de/estdv_1955/__82b.html |
| Home let below market | Below 50%: split; at least 66%, permanent housing let: fully paid; intermediate band needs forecast | https://www.gesetze-im-internet.de/estg/__21.html |

## The base

### Income and timing

- **Income**: rent; Umlagen (running costs paid by the tenant); settlement back-payments; a deposit kept and set off against rent, running costs or damage; payments for antenna, wind or Wi-Fi sites; a furniture surcharge; VAT received on an opted let; grants for rent (2025 instructions, lines 13 to 31). A refundable deposit is not income while held.
- **Umlagen count twice**: income when received; the running costs paid are Werbungskosten.
- **Ordinary cash timing:** receipts in the calendar year received and expenses in the year paid ([§ 11 EStG](https://www.gesetze-im-internet.de/estg/__11.html)); capitalisation, AfA and maintenance spreading take precedence where applicable. Recurring items around year-end, long-term advance rent/costs and loan discounts (Disagio): Check this point with one of our partner accountants. Do not apply the ordinary rule mechanically.

### Werbungskosten ([§ 9 EStG](https://www.gesetze-im-internet.de/estg/__9.html))

Costs "zur Erwerbung, Sicherung und Erhaltung der Einnahmen", deductible in the year paid, only for a property that earns or is intended to earn rent. Costs attributable to the owner’s private use or free-use parts are not rental expenses. Letting individual rooms within the owner’s home can generate deductible rental costs; allocate those costs to the actual let part.

- **Deductible**: loan interest so far as linked to the property, and the cost of raising the loan (§ 9(1) no. 1); property tax, other public charges and building insurance (no. 2); AfA and § 7b (no. 7); liability insurance; running costs, including those passed on; Hausgeld **except** the maintenance-reserve part, which is deductible only when the owners' association spends it; management; the tax adviser's rental share; tenancy legal fees; advertising and the broker for finding a tenant; rent-account fees; maintenance.
- **Travel:** for a personally used car on qualifying non-commuting rental journeys, actual costs or EUR 0.30 per kilometre **driven** ([§ 9(1) no. 4a, (3) EStG](https://www.gesetze-im-internet.de/estg/__9.html), importing the highest applicable [§ 5 BRKG](https://www.gesetze-im-internet.de/brkg_2005/__5.html) mileage rate). Property-as-first-place classification and differing 2025/2026 commuting rules: Check this point with one of our partner accountants. Do not assume a travel category or use a one-way inspection rate.
Loan principal is not interest; purchase transfer tax, notary and buyer's broker costs form acquisition cost instead of an immediate expense ([§ 255(1) HGB](https://www.gesetze-im-internet.de/hgb/__255.html)). Do not deduct private-only/free-use costs or reserve contributions. Personal taxes, fines, energy works and the own-home § 35c credit interaction: Check this point with one of our partner accountants. Do not treat them as ordinary rental expenses by default.

For mixed private/rental use, directly attribute identifiable costs and document a justified allocation of shared costs ([ELSTER 2026, Werbungskosten](https://www.elster.de/eportal/helpGlobal?themaGlobal=help_est_ufa_10_2026)). The original allocation example remains: rented-room repair EUR 1,000 plus shared roof repair EUR 10,000 at an independently supported 20% rental share gives EUR 3,000 before capital/spreading/cheap-let limits. The 20% is a stipulated fact, not a universal prescribed percentage.

### Building depreciation (AfA, [§ 7 EStG](https://www.gesetze-im-internet.de/estg/__7.html))

- **Completion date decides the straight-line rate**, not the purchase date: 3% after 2022, 2% for 1925 to 2022, 2.5% before 1925 (§ 7(4) sentence 1 no. 2). This covers every privately held building, housing or not, including flats and separate parts of a building (§ 7(5b)). The separate 3% rate in no. 1 is for business-asset buildings not used for housing: never use it for a private shop or office completed before 2023.
- **Historic and exceptional AfA:** shorter actual life, old § 7(5) staged rates/method changes and gifts/inheritances require actual historical records. Check this point with one of our partner accountants. Do not overwrite previous deductions.
- **Declining-balance AfA, § 7(5a).** Instead of 3% straight-line, 5% of the remaining value ("Restwert") each year, so far as the building is used for **housing**, if all hold: it is in Germany, the EU or the EEA; the client built it, or bought it by the end of the completion year; and construction started (the date on the construction-start notice required by state law; where none is required, the client declares a voluntary notice) or the binding purchase contract was made after 30 September 2023 and before 1 October 2029. No extraordinary write-down while it runs. Switching to straight-line is allowed, then on the remaining value and remaining life.
- **Base:** individually attributable acquisition and incidental cost under [§ 255 HGB](https://www.gesetze-im-internet.de/hgb/__255.html), split between building and non-depreciable land by relative market values, not the residual method. Exclude a purchased maintenance reserve ([ELSTER 2026](https://www.elster.de/eportal/helpGlobal?themaGlobal=help_est_ufa_10_2026)). The [BMF price-split tool](https://www.bundesfinanzministerium.de/Content/DE/Downloads/Steuern/Berechnung-Aufteilung-Grundstueckskaufpreis.html) makes or tests a split. Contract splits, expert valuations, acquisition grants and a former own home's first computation: Check this point with one of our partner accountants.
- **First-year month cut.** Cut one twelfth for each full month before the month of acquisition or completion (§ 7(1) sentence 4). Statute applies it to § 7(5a) (sentence 5). For straight-line AfA, the BMF letter of 21 May 2025 on § 7b says so too: "bei Fertigstellung nach dem 31. Januar wäre eine zeitanteilige Kürzung der linearen AfA im Jahr der Fertigstellung erforderlich" (example 7). The historical staged-method computation remains referred above.
- **For example**: completed February 2026, bought with benefit and burden from 1 April 2026, building share EUR 300,000. Declining-balance: 300,000 × 5% × 9/12 = EUR 11,250 in 2026; 2027: (300,000 − 11,250) × 5% = EUR 14,437.50. Straight-line instead: 300,000 × 3% × 9/12 = EUR 6,750. The binding contract was made in March 2026. Total acquisition cost is EUR 400,000, including land of EUR 100,000. From April, rent is EUR 1,200 plus Umlagen of EUR 250 a month: income is 9 × (1,200 + 250) = EUR 13,050. Interest of EUR 9,000, running costs of EUR 2,250 and management of EUR 600 total EUR 11,850. The declining-balance loss is 13,050 − 11,850 − 11,250 = EUR 10,050; with straight-line AfA the loss is EUR 5,550.
- **End:** until fully written off. Sale-year AfA: Check this point with one of our partner accountants.

### § 7b special depreciation for new rental flats ([§ 7b EStG](https://www.gesetze-im-internet.de/estg/__7b.html))

Up to 5% of the base in the year of acquisition or production and the three following years, on top of normal AfA under § 7(4) or § 7(5a). All must hold:

- The building work creates **new** flats that did not exist before and satisfy [§ 181(9) BewG](https://www.gesetze-im-internet.de/bewg/__181.html): a structurally separate, self-contained household unit, independent access, kitchen, bathroom/shower and toilet, normally at least 20 m², under a building application or notice in the **old window** (after 31 August 2018 and before 1 January 2022) or the **new window** (after 31 December 2022 and before 1 October 2029). Nothing applied for in 2022 qualifies.
- Cost per m² of living space **not more than** the cliff (EUR 3,000 old window, EUR 5,200 new window), or no § 7b at all. The base is capped per m² (EUR 2,000 old, EUR 4,000 new). Normal AfA still runs on full cost (BMF letter of 21 May 2025, para. 65).
- In the EU, or a state giving the required administrative help. If bought, bought by the end of the completion year; only the buyer claims.
- Let **for housing, against payment**, in that year and the **nine** following years. Short-term guest accommodation is not housing (§ 7b(2) no. 3).
- New window only: the building meets "Effizienzhaus 40" with sustainability class, proven by the "Qualitätssiegel Nachhaltiges Gebäude".
- **Old window ends with 2026**: claims are allowed "letztmalig für den Veranlagungszeitraum 2026" ([§ 52(15a)](https://www.gesetze-im-internet.de/estg/__52.html)), even if four years have not run. A qualifying buyer who started in 2024 can claim 2024 to 2026 and loses the fourth year (BMF letter, para. 16, example 1). The new window has no such end.
- **Claw-back** of all past claims if the flat is not let for housing for ten years, is sold in that time with the gain untaxed, or later costs push it over the cliff within three years after the year of acquisition or production (§ 7b(4)).
- **After the four-year benefit period**, regular AfA uses the remaining value and the § 7(4) percentage determined from the remaining mathematical useful life; for § 7(5a), apply its 5% rate to that remaining value ([§ 7a(9) EStG](https://www.gesetze-im-internet.de/estg/__7a.html); BMF letter, para. 66). The old-window 2026 sunset does not shorten that four-year period: the 2024 buyer above still uses unchanged regular AfA in 2027 and changes to § 7a(9) in 2028 (BMF para. 16). Establish the actual historical normal/special deductions and useful-life branch before computing; do not substitute a guessed partial-year balance.
- **De minimis aid:** under § 7b(5), the new-window aid test is restricted to claimants with farming, business or self-employed income; the old-window branch also needs its aid conditions. Eligibility, limits, cumulation and proof: Check this point with one of our partner accountants. Do not claim until this is resolved.
- **For example**: an 80 m² flat applied for in 2024, completed and bought January 2026, Effizienzhaus 40 with the seal, let long-term; assume qualifying dwelling/location and cleared aid conditions, cost of the flat without land EUR 400,000 (land never enters § 7b: BMF letter, para. 43). 400,000 / 80 = EUR 5,000 per m², not over 5,200: qualifies. Base cap 80 × 4,000 = EUR 320,000; § 7b 320,000 × 5% = EUR 16,000 a year for 2026 to 2029, plus straight-line 400,000 × 3% = EUR 12,000 (January, no cut). At EUR 420,000 (EUR 5,250 per m²) there is no § 7b.

Continuing that fully qualifying January 2026 straight-line example, four full years through 2029 deduct 4 × (EUR 12,000 regular AfA + EUR 16,000 special AfA). The residual building value is EUR 288,000. The mathematical 3% life is 100/3 years; after four years, 88/3 years remain. Regular annual AfA from 2030 is therefore EUR 288,000 ÷ (88/3) = EUR 9,818.1818… (EUR 9,818.18 displayed). This display rounding is not an independently established assessment-rounding rule. It is a January full-year fixture, not a formula for unverified historical partial-year or shorter-life facts.

Source for the letter: [BMF letter of 21 May 2025 on § 7b EStG](https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Einkommensteuer/2025-05-21-anwendungsschreiben-7b-estg-neu.pdf?__blob=publicationFile&v=5).

### Maintenance or production cost

- **Maintenance** preserves or restores the condition, subject to the acquisition/production-cost rules and three-year test. Repainting, heating, roof and window labels alone do not decide deductibility. Doubtful classifications: Check this point with one of our partner accountants.
- **Production cost** creates something new, extends, or substantially improves beyond the original condition ([§ 255(2) HGB](https://www.gesetze-im-internet.de/hgb/__255.html)): balcony, attic conversion, lift, lifting the standard (judged mainly by heating, sanitary and electrical installations and windows). The 2025 instructions: works that bring the flat or building "auf einen höheren Standard" are production or acquisition cost. Capitalised and depreciated with the building.
- **Bought in a poor state**: making non-working essential parts work again (defective heating, water or fire damage), and change-of-use works before first use, are **acquisition** cost (2025 instructions).
- **The 15% rule, acquisition-related production cost** ([§ 6(1) no. 1a EStG](https://www.gesetze-im-internet.de/estg/__6.html), applied to Werbungskosten by § 9(5) sentence 2). Repair and modernisation works carried out **within three years** of acquisition become production cost if their total cost **without VAT** "15 Prozent der Anschaffungskosten des Gebäudes übersteigen". It is a cliff: over it, **all** of them are capitalised. The three years are added up, so a later job can pull earlier deductions back in. Exactly 15% is not over. Not counted: extensions, and maintenance that usually recurs every year, such as servicing.
- **For example**: building completed 1970, bought May 2025, building share EUR 200,000, so the limit is EUR 30,000. Works without VAT: EUR 12,000 in 2025 (deducted on the 2025 return) and EUR 19,000 in 2026. Total EUR 31,000 is over EUR 30,000: all of it is production cost, including 2025, and is depreciated at 2% with the building: EUR 31,000 × 2% = EUR 620 for a full year. Correcting the 2025 assessment: Check this point with one of our partner accountants. With 2026 works of EUR 18,000 the total is exactly EUR 30,000: not over, judge each job on its own.
- **Spreading, [§ 82b EStDV](https://www.gesetze-im-internet.de/estdv_1955/__82b.html).** Larger maintenance may be spread evenly over two to five years if, **when paid**, the building is not a business asset and is **mainly** housing: housing floor area more than half the usable area; garages count as housing up to one car per flat. On sale, transfer into a business or end of letting, the rest is deducted that year. Co-owners must use the same period. Works in redevelopment areas and on listed buildings (§§ 11a, 11b EStG, §§ 7h, 7i): Check this point with one of our partner accountants.

### Furniture

Furniture premiums are rent. Furniture/kitchen useful lives and immediate deduction of low-value items: Check this point with one of our partner accountants. No automatic ten-year life or bare net-cost threshold is supplied. For the cheap-let comparison, use a furniture adjustment already provided by the local rent index without adding it twice. Otherwise add a surcharge only if it can be established from the local market for furnished lets; if no market value can be determined, no surcharge is added. Never derive it from monthly furniture AfA or a standard investment return ([BFH, 6 February 2018, IX R 14/17, paras. 18 to 20](https://www.bundesfinanzhof.de/de/entscheidung/entscheidungen-online/detail/pdf/STRE201810105?type=1646225765)).

### Cheap lets: the 50% and 66% rules ([§ 21(2) EStG](https://www.gesetze-im-internet.de/estg/__21.html))

Applies to letting a **home for living in**, to any tenant; it mostly bites on relatives.

| Rent including Umlagen, as share of local market rent including passable costs | Result |
|---|---|
| Less than 50% | Split into a paid and an unpaid part; costs deductible only for the paid part |
| At least 50% and less than 66% | Under the 2026 ELSTER instructions, no split if the forecast expects no loss, including zero; the forecast itself remains expressly referred below. |
| At least 66%, permanent home let | Deemed fully paid; ordinary expense conditions still apply |

- **Compare** rent paid including Umlagen with market rent including passable running costs, never cold rent with cold rent (2025 instructions).
- **The split**: costs in the ratio of agreed rent to market rent. On the 2025 form enter all costs in full (lines 33 to 84) and the cut percentage in line 87, or an amount in line 88 if only part of the property is let cheaply. The tax office makes the cut.
- **Forecast:** the [2026 ELSTER instructions](https://www.elster.de/eportal/helpGlobal?themaGlobal=help_est_ufa_10_2026) retain the no-loss test for the band at least 50% but below 66%, including a zero result. Constructing the forecast, its period, ordinary AfA, averages, margins and sale exclusions: Check this point with one of our partner accountants. Do not supply an assumed outcome.
- **Market rent**: the local rent index (Mietspiegel); failing that, equally valid: a publicly appointed and sworn expert's reasoned report, a rent database, or rents for at least three comparable flats (§ 558a(2) nos. 2 to 4 BGB, per the 2026 instructions).
- **Outside § 21(2)**: commercial space; the 66% sentence covers only permanent home lets. A cheap let of an office to a relative: Check this point with one of our partner accountants.

### Vacancy, holiday lets, VAT and losses

Vacancy before/between lets, serious letting efforts, long-term home presumption, temporary lettings, commercial premises/undeveloped land, holiday own-use and vacancy allocation, no-own-use evidence, local letting days, surplus forecasts and retrospective denial: Check this point with one of our partner accountants. Keep actual use days and marketing evidence; recurring annual losses alone do not establish an answer.

VAT exemption/option, tenant input-tax use, historic-building exceptions, accommodation/breakfast/parking, small-business status and input-tax recovery: Check this point with one of our partner accountants. See `germany-vat-return` and `de-vat-annual-and-special-schemes`.

Same-year rental loss offset, carry-back, carry-forward, separate loss notices and §§ 15a/15b: Check this point with one of our partner accountants. A computed rental loss is not proof of available tax relief.

### Sale within ten years ([§ 23 EStG](https://www.gesetze-im-internet.de/estg/__23.html), the Spekulationsfrist)

- A sale of land or a flat is a private sale if acquisition and sale are **not more than** ten years apart. Buildings put up or extended in the period are included.
- **Own-use exception**: used **only** for own housing between acquisition (or completion) and sale, **or** for own housing in the year of sale and the two years before. The old claim that two full preceding calendar years are always required is incorrect. Applying an own-housing exception: Check this point with one of our partner accountants.
- **Depreciation comes back**: the cost is **reduced** by AfA, increased depreciation and special depreciation claimed (§ 23(3) sentence 4). Gain = price less reduced cost less selling costs.
- **Exemption limit**: tax-free only if all private-sale gains in the year total **less than** EUR 1,000; at EUR 1,000 or more, all is taxed. Private-sale losses do not simply offset rent and are excluded from § 10d deduction; restricted same-year/carry-back/carry-forward treatment: Check this point with one of our partner accountants.
- **Gift**: gifts, inheritance and communities require an actual succession analysis. Check this point with one of our partner accountants.
- **Also:** apply the § 82b termination rule and investigate § 7b claw-back; assessment correction/interest: Check this point with one of our partner accountants.
- **For example**: bought March 2019 for EUR 300,000 (building EUR 240,000 at 2% = EUR 4,800 a year); sold at the end of February 2026 for EUR 340,000; selling costs EUR 10,000. AfA claimed: 2019, ten months = EUR 4,000; 2020 to 2025, 6 × 4,800 = EUR 28,800; 2026, two months to the sale, assumed EUR 800. Total EUR 33,600. Reduced cost EUR 266,400; gain 340,000 − 266,400 − 10,000 = EUR 63,600 on the old assumed inputs. **Non-usable tax conclusion:** the EUR 800 sale-year deduction and actual historic deductions are unverified. Check this point with one of our partner accountants. Do not file or quote EUR 63,600 as an established taxable gain. More in `de-capital-gains`.

### Order of work

Fix the building share before the three-year 15% test, which measures against it. Complete the costs before the cheap-let cut, which applies to their total. Then work out the surplus or loss per property; co-owner attribution and use of losses remain expressly referred.

**Missing facts:** stop the affected computation. Uncertain repair classification, housing use, completion dates, land split, ownership or comparable rent: Check this point with one of our partner accountants. Do not capitalise by default or fill a missing input with zero.

## Deadlines and filing

- **Forms:** ELSTER's [2026 instructions](https://www.elster.de/eportal/helpGlobal?themaGlobal=help_est_ufa_10_2026) are now substantive. Use Anlage V per built-on property and add V-FeWo for holiday/short-term letting. V-Sonstige covers the other routes such as communities/funds, subletting, undeveloped land and rights; specialist determinations remain referred. **2026 V-FeWo:** separate form per corresponding Anlage V, space for up to **three holiday flats and three short-term lettings**, with more forms as needed. The four-flat layout is historical 2025. For exclusively holiday-let properties the 2026 form compares actual/local average letting days over a continuous **three-to-five-year** period starting, ending or including 2026; tax treatment remains referred above.
- **Filing duty:** employee EUR 410 trigger, hardship relief, other filing triggers and electronic exceptions: Check this point with one of our partner accountants. Do not infer no filing duty from a small rental result.
- **2026 return** ([§ 149 AO](https://www.gesetze-im-internet.de/ao_1977/__149.html)): for an ordinary required calendar-year return, without an adviser, seven months after the year: 31 July 2027 is a Saturday, so **Monday 2 August 2027** ([§ 108(3) AO](https://www.gesetze-im-internet.de/ao_1977/__108.html)). With an adviser, the last day of February of the second following year: **Tuesday 29 February 2028**. The tax office may call for an advised return earlier (§ 149(4)); effective extensions and local statutory holidays can change the actual due date.
- **2025 returns being filed now.** Without an adviser: due Friday 31 July 2026, passed. With an adviser: the last day of February 2027 is a Sunday, so **Monday 1 March 2027**. The extended dates in Art. 97 § 36(3) EGAO cover only "die Besteuerungszeiträume 2020 bis 2024" ([EGAO](https://www.gesetze-im-internet.de/aoeg_1977/art_97__36.html)). The advised 2024 return was due 30 April 2026 under that transitional rule. Use the 2025 Anlage V. Historical commuting rates and travel category: Check this point with one of our partner accountants.
- **Prepayments** ([§ 37 EStG](https://www.gesetze-im-internet.de/estg/__37.html)): 10 March, 10 June, 10 September, 10 December; set only if at least EUR 400 a year and EUR 100 per date. A building's rental loss reduces prepayments only for calendar years beginning **after** its acquisition or completion (§ 37(3) sentence 8); a building bought before the year it is completed counts from completion (sentence 9); the bar does not apply where § 7b is claimed (sentence 10). The wage-tax allowance under § 39a and special prepayment adjustments: Check this point with one of our partner accountants. For example, a landlord who bought a new flat in 2026 with a EUR 10,050 loss cannot cut her 2026 prepayments for it; the timing bar clears from 2027, or where a valid § 7b claim removes it. Other notice/eligibility conditions remain.
- **Form workflow:** use the actual year's headings for receipts, building/furniture AfA, interest/finance costs, maintenance/spreads, running/other costs, result/shares and cheap-let adjustments. Bank-text keywords are intake clues, not legal or line-placement authority. Reconcile a property schedule, transmit the relevant return, retain its acknowledgement and compare the assessment. Exact line placement outside the dated official example: Check this point with one of our partner accountants.

## Penalties and interest

Late filing/payment, discretionary or compulsory surcharge conditions, back-tax/refund interest, § 7b claw-back procedure/interest, under-declaration, correcting returns/assessments and offences: Check this point with one of our partner accountants. Establish year, actual notice, extension, tax credits and dates before calculating; no bare rate or automatic penalty is supplied here.

## Cross-border points

Non-resident landlords (`de-non-resident-tax`), residents' foreign property (actual treaty, Anlage AUS, exemption/credit/progression), part-year moves (`de-partners-and-part-year`) and foreign depreciation eligibility: Check this point with one of our partner accountants. Do not infer German liability, basic allowance or treaty relief from this rental calculation.

## Two worked examples that recompute

Inputs are invented except the dated official 2025 parents case. Establish all expense/eligibility facts; a numeric loss does not prove usable tax relief.

### Example 1: a let flat bought in 2019, full year 2026

A flat completed in 1995, bought in 2019, let all of 2026 at market rent. Building share of cost EUR 180,000, so straight-line AfA at 2% (§ 7(4) no. 2(b)) is EUR 3,600. Rent EUR 950 a month plus Umlagen EUR 180. Paid in 2026: interest EUR 4,200; running costs EUR 2,160 (all passed on); Hausgeld excluding the reserve EUR 540 (the reserve part of EUR 600 is left out); a repair EUR 1,500; account fees EUR 60; principal EUR 6,000 (not deductible). Six trips by personally used car, 300 km driven in all, at 30 cents, assuming qualifying non-commuting rental travel.

Income is (950 + 180) × 12 = EUR 13,560. Werbungskosten are 3,600 + 4,200 + 2,160 + 540 + 1,500 + 90 + 60 = EUR 12,150. The conditional rental surplus is EUR 1,410 before the tariff; no 2026 form-line conclusion is inferred from a historical line map.

```oa-check
name: DE 2026 let flat, 2% AfA, surplus
inputs:
  monthly_rent: 950
  monthly_umlagen: 180
  building_cost: 180000
  interest: 4200
  running_costs: 2160
  hausgeld_without_reserve: 540
  repairs: 1500
  km_driven: 300
  account_fees: 60
steps:
  - income: (monthly_rent + monthly_umlagen) * 12
  - afa: building_cost * 0.02
  - travel: km_driven * 0.30
  - costs: afa + interest + running_costs + hausgeld_without_reserve + repairs + travel + account_fees
  - surplus: income - costs
expected:
  income: 13560
  afa: 3600
  travel: 90
  costs: 12150
  surplus: 1410
```

### Example 2: cheap let to parents, original official tax year 2025

In the official **2025** case a married couple own a 60 m² flat and let it to the wife's parents for EUR 270 cold rent plus EUR 150 Umlagen a month. Local market rent is 60 m² × EUR 15 = EUR 900 plus EUR 150 passable costs = EUR 1,050. Costs: AfA EUR 3,000, running costs EUR 1,800, account fees EUR 120.

Rent paid including Umlagen is EUR 420, which is 40.00% of EUR 1,050: under 50%, so costs are split. The **2025** form shows income EUR 5,040 (line 32), costs in full EUR 4,920 (line 83), result before the cut EUR 120 (line 85), and the cut of 60.00% in line 87. After the cut only EUR 1,968 of costs is deductible, so the taxable surplus is EUR 3,072, EUR 1,536 for each spouse. Variants: rent of EUR 700 including Umlagen is 66.67%, fully paid; EUR 600 is 57.14%, in the forecast band: Check this point with one of our partner accountants.

```oa-check
name: DE 2025 cheap let to relatives at 40% of market rent
inputs:
  cold_rent: 270
  umlagen: 150
  market_cold_rent: 900
  afa: 3000
  running_costs: 1800
  account_fees: 120
steps:
  - rent_paid: cold_rent + umlagen
  - market_rent: market_cold_rent + umlagen
  - paid_share: rent_paid / market_rent
  - income: rent_paid * 12
  - costs_in_full: afa + running_costs + account_fees
  - line85_before_cut: income - costs_in_full
  - cut_percent: (1 - paid_share) * 100
  - deductible_costs: costs_in_full * paid_share
  - surplus: income - deductible_costs
  - per_spouse: surplus / 2
expected:
  paid_share: 0.40
  income: 5040
  costs_in_full: 4920
  line85_before_cut: 120
  cut_percent: 60
  deductible_costs: 1968
  surplus: 3072
  per_spouse: 1536
```

### Restored original 2025 cases

These invented inputs were in the first 2025 version. Their years and numbers are preserved; the added conditions must be established before using a tax result.

- **January 2023 completion:** price EUR 400,000, building EUR 300,000 and land EUR 100,000; rent including running-cost receipts EUR 14,400, interest EUR 8,000, property tax EUR 600, insurance EUR 400, management EUR 1,200. Assuming a full eligible 2025 rental year and ordinary 3% AfA EUR 9,000, costs total EUR 19,200 and rental loss EUR 4,800. Usable offset remains referred.
- **1965 building:** building EUR 200,000, rent EUR 9,600, heating replacement EUR 12,000, other expenses EUR 2,000. Assuming actual maintenance outside capital rules, § 82b eligibility and five-year election, 2% AfA EUR 4,000 plus annual maintenance EUR 2,400 plus EUR 2,000 = costs EUR 8,400; surplus EUR 1,200. A like-for-like label alone does not prove those conditions.
- **Daughter's let:** EUR 400/month against EUR 700/month gives 57.142857%, not a rounded legal threshold. The old facts do not say whether both include the same passable costs. Reconcile the comparison first; forecast band/outcome: Check this point with one of our partner accountants.
- **Year 2 renovation:** property EUR 250,000, building EUR 180,000, bathroom/kitchen works EUR 30,000. If qualifying works within three years and the EUR 30,000 excludes VAT, the threshold is EUR 27,000; 30,000 / 180,000 = 16.6667%, so all EUR 30,000 is capitalised and building basis becomes EUR 210,000. VAT measurement, item classification and depreciation schedule are absent: Check this point with one of our partner accountants.

## Ask the client first

- When was the building completed, and when did you buy it (contract date, and the date benefit and burden passed)? Which AfA method and rate did past returns use? For a new flat: date of the building application, start of construction, living space in m², cost per m², energy standard.
- Is the property held privately or in a business? What share of the floor area is housing? Is any unit let short-term or as a holiday flat, and is there any own use?
- How was the price split between land and building, and who made the split?
- What rent and Umlagen does each tenant pay, and what is the local market rent? Is any tenant a relative?
- What works were done since the purchase, when, and at what cost without VAT?
- Do you live in Germany? Any co-owners, loans, a sale made or planned, or wage tax withheld on a job? Read existing records first. Co-ownership determinations, heirs, funds, usufruct/paid waiver, heritable building rights and special building regimes: Check this point with one of our partner accountants.

## Sources

Read dates identify substantive operative text, not HTTP status. Unchanged ordinary deadlines reuse the completed 26 November German proof; rental-specific missing dependencies and current forms were read afresh.

| Source and operative scope | Official URL | Read on |
|---|---|---|
| EStG letting scope and cheap-housing tests | https://www.gesetze-im-internet.de/estg/__21.html | 2026-11-27 |
| EStG rental expense/travel/acquisition-works bridges | https://www.gesetze-im-internet.de/estg/__9.html | 2026-11-27 |
| EStG ordinary cash timing; exceptions referred | https://www.gesetze-im-internet.de/estg/__11.html | 2026-11-27 |
| EStG building AfA, first-year cut and declining balance | https://www.gesetze-im-internet.de/estg/__7.html | 2026-11-27 |
| EStG new rental-flat eligibility/caps/claw-back | https://www.gesetze-im-internet.de/estg/__7b.html | 2026-11-27 |
| EStG remaining-value depreciation | https://www.gesetze-im-internet.de/estg/__7a.html | 2026-11-27 |
| EStG old-window sunset | https://www.gesetze-im-internet.de/estg/__52.html | 2026-11-27 |
| Statutory self-contained dwelling definition | https://www.gesetze-im-internet.de/bewg/__181.html | 2026-11-27 |
| Acquisition-related works test | https://www.gesetze-im-internet.de/estg/__6.html | 2026-11-27 |
| Maintenance spreading/termination | https://www.gesetze-im-internet.de/estdv_1955/__82b.html | 2026-11-27 |
| Acquisition/production-cost definitions | https://www.gesetze-im-internet.de/hgb/__255.html | 2026-11-27 |
| Imported car mileage rate | https://www.gesetze-im-internet.de/brkg_2005/__5.html | 2026-11-27 |
| Private sale period/exceptions, gain and restricted losses | https://www.gesetze-im-internet.de/estg/__23.html | 2026-11-27 |
| Rental-building prepayment timing and ordinary notice rules | https://www.gesetze-im-internet.de/estg/__37.html | 2026-11-27 |
| AO ordinary return deadlines/earlier demand and weekends, completed proof reused | https://www.gesetze-im-internet.de/ao_1977/__149.html; https://www.gesetze-im-internet.de/ao_1977/__108.html | 2026-11-26 |
| EGAO advised historical return transition, completed proof reused | https://www.gesetze-im-internet.de/aoeg_1977/art_97__36.html | 2026-11-26 |
| BMF relative-market-value price split | https://www.bundesfinanzministerium.de/Content/DE/Downloads/Steuern/Berechnung-Aufteilung-Grundstueckskaufpreis.html | 2026-11-27 |
| BMF new-flat letter: paras. 16, 59–66 and example 7 first-year note | https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Einkommensteuer/2025-05-21-anwendungsschreiben-7b-estg-neu.pdf?__blob=publicationFile&v=5 | 2026-11-27 |
| BFH furniture premium, paras. 18–20; no historical rate-band import | https://www.bundesfinanzhof.de/de/entscheidung/entscheidungen-online/detail/pdf/STRE201810105?type=1646225765 | 2026-11-27 |
| ELSTER current Anlage V/V-FeWo, income/costs/cheap-let band, capacity and comparison period | https://www.elster.de/eportal/helpGlobal?themaGlobal=help_est_ufa_10_2026 | 2026-11-27 |
| ELSTER historical expense/depreciation instructions and original official parents' case | https://www.elster.de/eportal/helpGlobal?themaGlobal=help_est_ufa_10_2025 | 2026-11-27 |

Not yet confirmed: individual eligibility on expressly referred historic/exceptional AfA, travel category/commuting, furniture/GWG, cash exceptions/subsidies, personal taxes/fines/energy credits, forecast/vacancy/holiday tax treatment, loss use, sale-year AfA/exceptions, aid eligibility/claw-back procedure, ownership/rights/special-building issues, filing duty/line details, penalties/interest/corrections, foreign/non-resident/treaty/business/VAT treatment. These are explicit non-usable holds, not default conclusions.
