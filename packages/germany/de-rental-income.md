---
name: de-rental-income
description: Use this skill whenever asked about German rental income taxation (Vermietung und Verpachtung). Trigger on phrases like "Mieteinnahmen", "Vermietung", "Verpachtung", "Anlage V", "§21 EStG", "AfA", "Abschreibung", "Werbungskosten Vermietung", "Hausgeld", "Grundsteuer deduction", "Erhaltungsaufwand", "Herstellungskosten", "verbilligte Vermietung", "Möblierungszuschlag", "rental income Germany", "German property tax deduction", "depreciation German property", "Verlustverrechnung", "rental loss Germany", or any question about computing, filing, or optimising income from letting immovable property in Germany. Covers Anlage V structure, AfA depreciation rates, Werbungskosten, repairs vs improvements, reduced-rent rules, furnished premium, and loss offset. ALWAYS read this skill before touching any German rental income work.
version: 1.0
jurisdiction: DE
tax_year: 2026
last_updated: 2026-09-27
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - de-income-tax
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Rental income tax in Germany (Vermietung und Verpachtung)

## Scope

An individual's income from letting land, buildings and flats held as **private assets** ([§ 21 EStG](https://www.gesetze-im-internet.de/estg/__21.html)): income, deductible costs (Werbungskosten), building depreciation (AfA, including the 3% and declining-balance rules for new builds and § 7b), maintenance versus acquisition cost (the 15% rule), cheap lets (the 66% rule), holiday and short-term lets, losses, a sale within ten years, and Anlage V.

- **Who.** Private landlords resident in Germany and their preparers. Letting income that belongs to another kind of income, such as property held in a business or by a trading partnership, is taxed there (§ 21(3) EStG) and is outside this Guide.
- **Which year.** Tax year 2026, the calendar year. The consolidated EStG as read applies from 2026 ([§ 52(1) EStG](https://www.gesetze-im-internet.de/estg/__52.html): "erstmals für den Veranlagungszeitraum 2026 anzuwenden"). For the 2025 returns being filed now, see "Returns being filed now: tax year 2025".
- **Forms.** The 2026 instructions were not on ELSTER on 27 September 2026. Form names, line numbers, the cheap-let forecast test and the official example come from the [ELSTER instructions for the 2025 return](https://www.elster.de/eportal/helpGlobal?themaGlobal=help_est_ufa_10_2025) ("2025 instructions"). Check the 2026 form when published.
- **Measure.** Receipts less Werbungskosten ([§ 2(2) EStG](https://www.gesetze-im-internet.de/estg/__2.html)), cash basis. The result joins the client's other income at the normal tariff, plus solidarity surcharge and church tax (tariff: `de-einkommensteuer-freelancer`).
- **Related Guides.** `de-capital-gains` (sales), `germany-vat-return` (VAT), `de-trade-tax` (a letting activity that is a trade), `de-freelance-intake` (intake and routing).

## Ask the client first

- When was the building completed, and when did you buy it (contract date, and date benefit and burden passed)? Which depreciation method and rate did past returns use?
- Is the property held privately or in a business? What share of the floor area is housing?
- How was the price split between land and building, and by whom?
- What rent and running costs (Umlagen) does each tenant pay? What is the local market rent? Is the tenant a relative? Is the let permanent?
- What works were done since the purchase, when, and at what cost without VAT?
- Is any unit a holiday flat or let short-term through a platform? Any own use? Is VAT charged?
- For a new flat: date of the building application or notice, start of construction, living space in m², cost per m², energy standard.
- Co-owners? Loans? Any sale made or planned? Is the client an employee with wage tax withheld?

**Defaults when a fact is missing.** Completion date, land share, market rent for a cheap let, or private versus business status unknown: stop and ask, because each changes the result. Unsure whether work is maintenance or production cost: treat it as production cost (capitalise) until resolved. Housing use unknown: ask, because § 7(5a), § 7b, § 21(2) and § 82b apply only to housing.

## The method, step by step

1. **Confirm § 21 income**: private asset, not a business, no trade in property (refer).
2. **Pick the forms**: one Anlage V per built-on property; add Anlage V-FeWo for holiday or short-term lets; Anlage V-Sonstige for shares in communities, subletting, land without buildings, rights.
3. **Add up 2026 receipts** on a cash basis ([§ 11 EStG](https://www.gesetze-im-internet.de/estg/__11.html)): rent, Umlagen, settlement back-payments, deposits kept, VAT received.
4. **Fix the depreciation base**: split the total cost between land and building. Land is never depreciated.
5. **Set the method and rate** by completion date ([§ 7 EStG](https://www.gesetze-im-internet.de/estg/__7.html)); test the 5% declining-balance method; cut the first year by months.
6. **Test § 7b** for a new rental flat ([§ 7b EStG](https://www.gesetze-im-internet.de/estg/__7b.html)). Old window: 2026 is the last year.
7. **Sort building costs** into maintenance and production or acquisition cost; for a building bought in the last three years run the 15% test ([§ 6(1) no. 1a EStG](https://www.gesetze-im-internet.de/estg/__6.html)).
8. **Decide on spreading** larger maintenance over two to five years ([§ 82b EStDV](https://www.gesetze-im-internet.de/estdv_1955/__82b.html)).
9. **List the other Werbungskosten paid** ([§ 9 EStG](https://www.gesetze-im-internet.de/estg/__9.html)). Leave out principal and maintenance-reserve payments.
10. **Run the cheap-let test** for every home ([§ 21(2) EStG](https://www.gesetze-im-internet.de/estg/__21.html)). Below 50%: enter the cut. 50% to under 66%: refer the forecast.
11. **Work out the surplus or loss** per property, share it between co-owners, and apply the loss rules ([§ 10d EStG](https://www.gesetze-im-internet.de/estg/__10d.html)).
12. **File and pay** (see "Filing and payment"); review prepayments.
13. **On a sale**, test ten years under [§ 23 EStG](https://www.gesetze-im-internet.de/estg/__23.html) and add back depreciation.

Order matters: fix the building share (step 4) before the three-year test (step 7), which measures against it; complete the costs (step 9) before the cheap-let cut (step 10), which applies to their total.

## Figures for 2026

All apply to tax year 2026 and were the same in 2025 unless marked.

| Rule | Figure | Source |
| --- | --- | --- |
| Straight-line AfA: completed after 31 Dec 2022 / 1925 to 2022 / before 1925 | 3% / 2% / 2.5% a year | [§ 7(4) EStG](https://www.gesetze-im-internet.de/estg/__7.html) |
| Declining-balance AfA (choice, housing) | 5% of remaining value | § 7(5a) EStG |
| § 7b special depreciation, four years | up to 5% a year | [§ 7b EStG](https://www.gesetze-im-internet.de/estg/__7b.html) |
| § 7b cost cliff / base cap, new window | EUR 5,200 / EUR 4,000 per m² | § 7b(2), (3) EStG |
| § 7b cost cliff / base cap, old window | EUR 3,000 / EUR 2,000 per m² | § 7b(2), (3) EStG |
| Works within three years capitalised if | more than 15% of building cost, without VAT | [§ 6(1) no. 1a EStG](https://www.gesetze-im-internet.de/estg/__6.html) |
| Low-value item deducted at once | not more than EUR 800 net | § 6(2) EStG |
| Cheap let: split / fully paid | under 50% / at least 66% of market rent | [§ 21(2) EStG](https://www.gesetze-im-internet.de/estg/__21.html) |
| Car travel to the property | 30 cents per km driven | [§ 5(2) BRKG](https://www.gesetze-im-internet.de/brkg_2005/__5.html) |
| Commuting allowance (only if a first place of activity), 2026 | EUR 0.38 per full km one way | [§ 9(1) no. 4 EStG](https://www.gesetze-im-internet.de/estg/__9.html) |
| Loss carry-back | EUR 1,000,000 (EUR 2,000,000 joint) | [§ 10d EStG](https://www.gesetze-im-internet.de/estg/__10d.html) |
| Loss carry-forward above EUR 1 million (EUR 2 million joint) | 70% of the excess | § 10d(2) EStG |
| Private sale exempt if total gains are | less than EUR 1,000 | [§ 23(3) EStG](https://www.gesetze-im-internet.de/estg/__23.html) |
| Employee must file if untaxed income is | more than EUR 410 | [§ 46(2) EStG](https://www.gesetze-im-internet.de/estg/__46.html) |
| VAT on an opted let | 19% | [§ 12 UStG](https://www.gesetze-im-internet.de/ustg_1980/__12.html) |
| Prepayments set only if | at least EUR 400 a year and EUR 100 per date | [§ 37(5) EStG](https://www.gesetze-im-internet.de/estg/__37.html) |
| Late-filing surcharge per month | 0.25%, at least EUR 25 | [§ 152(5) AO](https://www.gesetze-im-internet.de/ao_1977/__152.html) |

## The rules

### Income and timing

- **Income**: rent, Umlagen, settlement back-payments, a deposit once kept and set off, a furniture surcharge, VAT received on an opted let. A refundable deposit is not income while held.
- **Umlagen count twice**: income when received; the running costs paid are Werbungskosten.
- **Cash basis** (§ 11 EStG): income when received, costs when paid; regularly recurring items paid shortly around the turn of the year belong to their year. Rent received in advance for more than five years **may** be spread; costs paid in advance for more than five years **must** be spread. A market-level loan discount (Disagio) is deductible when paid.

### Building depreciation (AfA, [§ 7 EStG](https://www.gesetze-im-internet.de/estg/__7.html))

- **Completion date decides the rate**, not the purchase date. The rates apply to every privately held building, housing or not, including condominiums and separate parts of a building (§ 7(5b)). The separate 3% rate for **business-asset** buildings not used for housing (§ 7(4) sentence 1 no. 1) is outside this Guide; never use it for a private shop or office completed before 2023.
- **Shorter actual life.** If the actual useful life is under 33 years (built after 2022), 50 years (1925 to 2022) or 40 years (before 1925), that life may be used (§ 7(4) sentence 2). The 2025 instructions call this an exceptional case needing proof and cite the BMF letter of 22 February 2023. Refer.
- **Older staged rates.** A building built or bought in its completion year under an application or contract before 1 January 2006 (housing; earlier dates otherwise) may be on the staged rates of § 7(5). Ask what past returns used; refer any change of method.
- **Acquired for free**: continue the previous owner's rate (2025 instructions).
- **Declining-balance, § 7(5a).** 5% of the remaining value, so far as the building is used for **housing**, if: it is in Germany, the EU or the EEA; the client built it or bought it by the end of the completion year; and construction started (per the construction-start notice required by state law, not the application date; where none is required, the client declares a voluntary report), or the binding purchase contract was made, after 30 September 2023 and before 1 October 2029. No extraordinary write-down while it runs. Switching to straight-line is allowed, then on remaining value and remaining life.
- **Base.** Price plus side costs (transfer tax, notary, land register, the buyer's broker) under [§ 255 HGB](https://www.gesetze-im-internet.de/hgb/__255.html), less the land share. A maintenance reserve bought with a flat is excluded; grants reduce the base (line 89). A former own home let for the first time needs a first computation.
- **Price split.** By the ratio of market values, "nicht nach der sogenannten Restwertmethode". The [BMF price-split tool](https://www.bundesfinanzministerium.de/Content/DE/Downloads/Steuern/Berechnung-Aufteilung-Grundstueckskaufpreis.html) (March 2026) makes or tests a split. A contract split at arm's length or an expert valuation may also be used; the tax office may challenge a high building share.
- **First-year month cut.** Cut one twelfth for each full month before the month of acquisition or completion (§ 7(1) sentence 4), applied to § 7(5a) by statute and to straight-line by the finance ministry ("bei Fertigstellung nach dem 31. Januar wäre eine zeitanteilige Kürzung der linearen AfA im Jahr der Fertigstellung erforderlich", BMF letter of 21 May 2025, example 7). Only the old staged rates of § 7(5) take a full first year.
- **End**: until fully written off or sold.

### Special depreciation for new rental flats ([§ 7b EStG](https://www.gesetze-im-internet.de/estg/__7b.html))

Up to 5% of the base in the year of acquisition or production and the three following years, on top of normal AfA. All must hold:

- The work creates **new** flats. Building application (or notice) in the **old window**, after 31 August 2018 and before 1 January 2022, or the **new window**, after 31 December 2022 and before 1 October 2029. Nothing made in 2022 qualifies.
- Cost per m² of living space **not more than** the cliff (EUR 5,200 new, EUR 3,000 old), or no § 7b at all. The base is capped per m² (EUR 4,000 new, EUR 2,000 old); normal AfA still runs on full cost.
- In the EU or a state giving the required administrative assistance. If bought, bought by the end of the completion year; only the buyer claims.
- Let **for housing, against payment**, in that year and the **nine** following years. Short-term guest accommodation is not housing.
- New window: "Effizienzhaus 40" with sustainability class, proven by the "Qualitätssiegel Nachhaltiges Gebäude".

Also:

- **Old window ends with 2026**: claims "letztmalig für den Veranlagungszeitraum 2026" ([§ 52(15a) EStG](https://www.gesetze-im-internet.de/estg/__52.html)), even if four years have not run. A buyer who started in 2024 claims 2024 to 2026 and loses the fourth year (BMF letter, paragraph 16). No end date for the new window.
- **Claw-back** for the past if the flat is not let for housing for ten years, is sold in that time with the gain untaxed, or later costs push it over the cliff within three years after the year of acquisition or production (§ 7b(4)).
- **After four years**, normal AfA runs on the remaining value ([§ 7a(9) EStG](https://www.gesetze-im-internet.de/estg/__7a.html); BMF letter, paragraph 66). Refer the computation.
- **De minimis**: for the new window only for claimants with farming, business or self-employed income (§ 7b(5)); the 2025 instructions treat the old window as de minimis aid and ask for a checklist.

Source: [BMF letter of 21 May 2025 on § 7b EStG](https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Einkommensteuer/2025-05-21-anwendungsschreiben-7b-estg-neu.pdf?__blob=publicationFile&v=5).

### Werbungskosten ([§ 9 EStG](https://www.gesetze-im-internet.de/estg/__9.html))

Costs to get, secure and keep the income (§ 9(1) EStG), deductible in the year paid, only for a flat that earns or is intended to earn rent. Not for a flat the client lives in or lets for free.

- **Deductible**: loan interest so far as linked to the property, and costs of raising the loan; AfA and § 7b; property tax, public charges and building insurance (§ 9(1) sentence 3 no. 2); liability insurance; running costs passed on; Hausgeld **except** the maintenance-reserve part, which is deductible only when the community spends it; management; the tax adviser's rental share; tenancy legal fees; tenant advertising and broker; rent-account fees; maintenance.
- **Travel**: actual cost or 30 cents per km **driven** (§ 5(2) BRKG through § 9(1) sentence 3 no. 4a and § 9(3) EStG). If the property were a first place of activity, the commuting allowance applies instead: EUR 0.38 per full km one way in 2026. When a let property is one is unsettled on the pages read: ask the accountant.
- **Not deductible**: principal (Tilgung); transfer tax on the purchase (acquisition cost); reserve payments until spent; own-use or free flats; the unpaid part of a cheap let; private costs; fines (§ 9(5) with § 4(5) no. 8 EStG); income tax, solidarity surcharge, church tax.

### Maintenance or production cost ([§ 6(1) no. 1a EStG](https://www.gesetze-im-internet.de/estg/__6.html))

- **Maintenance** (Erhaltungsaufwand) keeps or restores the condition: repainting, like-for-like heating, roof repair, equivalent windows. Deductible when paid, or spread under § 82b.
- **Production cost** creates something new, extends, or substantially improves beyond the original condition ([§ 255(2) HGB](https://www.gesetze-im-internet.de/hgb/__255.html)): balcony, attic conversion, lift, lifting the standard (judged mainly by heating, sanitary, electrics and windows). Capitalised.
- **Bought in a poor state**: making non-functioning essential parts work again (defective heating, water or fire damage), and change-of-use works before first use, are **acquisition** cost (2025 instructions).
- **15% rule** (§ 6(1) no. 1a EStG, applied by § 9(5) sentence 2). Repair and modernisation works carried out **within three years** of acquisition become production cost if their total cost **without VAT** is **more than** 15% of the **building's** acquisition cost ("ohne die Umsatzsteuer 15 Prozent der Anschaffungskosten des Gebäudes übersteigen"). A cliff: over it, **all** are capitalised. The three years are added up, so a later job can pull earlier deductions in. Exactly 15% is not over. Not counted: extensions, and maintenance that usually recurs yearly (servicing).
- **Spreading, § 82b EStDV.** Larger maintenance may be spread evenly over two to five years if, **when incurred**, the building is not a business asset and is **mainly** housing: housing floor area more than half the usable area; garages count as housing up to one car per flat. On sale, move into a business or end of letting, the rest is deducted that year. Co-owners use one period. Works in redevelopment areas and on listed buildings (§§ 11a, 11b EStG): refer.

### Furniture

A furniture surcharge is rent. Furniture and fitted kitchens are depreciated over their useful life (§ 7(1) EStG; lines 42 to 45). An item usable on its own costing not more than EUR 800 net may be deducted at once ([§ 6(2) EStG](https://www.gesetze-im-internet.de/estg/__6.html)). How a furniture surcharge enters the cheap-let comparison is not on an official page read: refer.

### Cheap lets: the 50% and 66% rules ([§ 21(2) EStG](https://www.gesetze-im-internet.de/estg/__21.html))

Applies to letting a **home for living in**, to any tenant; it mostly bites on relatives.

| Rent as share of local market rent | Result |
| --- | --- |
| Less than 50% ("weniger als 50 Prozent") | Split into paid and unpaid parts; costs deductible only for the paid part |
| At least 50% and less than 66% | No split **only if** no loss is expected over the let (surplus forecast); 50% alone is not enough (2025 instructions: "mindestens 50 % , jedoch weniger als 66 %") |
| At least 66%, permanent home let ("mindestens 66 Prozent") | Fully paid; all costs deductible |

- **Compare** rent paid **including** Umlagen with market rent **including** passable running costs. Not cold rent with cold rent.
- **Split**: costs in the ratio of agreed to market rent. On the 2025 form enter all costs in full (lines 33 to 84) and the cut percentage in line 87, or an amount in line 88 if only part is let cheaply. The tax office makes the cut.
- **Forecast**: per the BMF letter of 8 October 2004 (paragraph 33 onward), not found on an allowed page. Refer.
- **Market rent**: the local rent index (Mietspiegel); failing that, as equal-ranking examples, a sworn expert's report, a rent database, or three comparable flats (§ 558a(2) nos. 2 to 4 BGB).
- **Outside**: commercial space; the 66% sentence covers only permanent home lets.

### Vacancy, holiday flats and short-term lets

- **Vacancy.** Costs stay deductible while the client intends to let. Keep evidence (listings, agent mandate, realistic rent); a long unmarketed vacancy risks denial.
- **Form.** A holiday flat or house, or any object let **short-term** (for example through an internet platform), needs **Anlage V-FeWo** as well as Anlage V; up to 4 flats per form.
- **Day counts** where the owner used it, left it free to others, or could use it at any time: days of own use (including free use by others; not short stays for servicing, cleaning, renovation or checks), letting and vacancy. Own use possible at any time: split vacancy by the ratio of own use to letting. Own use limited to set times (for example via an agent): only reserved time is own use; vacancy counts as letting. Never used by the owner: give the letting days usual in that place.
- **Intention to make a surplus**: the instructions cite the BMF letter of 8 October 2004, not read on an allowed page. Refer holiday homes with own use.
- **Trade and VAT.** Hotel-like services may make it a trade (`de-trade-tax`). Short-term guest accommodation is not VAT-exempt ([§ 4 no. 12 UStG](https://www.gesetze-im-internet.de/ustg_1980/__4.html)); where VAT is due it takes the reduced rate of seven per cent ([§ 12(2) no. 11 UStG](https://www.gesetze-im-internet.de/ustg_1980/__12.html)). The reduced rate does not cover services not directly part of the letting, such as breakfast, even if included in the price (§ 12(2) no. 11 sentence 2). Whether it is due depends on the small-business rule: `germany-vat-return`. No § 7b for short-term lets.

### VAT option on commercial lets

Letting is VAT-exempt (§ 4 no. 12 sentence 1 letter a UStG), except short-term accommodation, parking spaces, short-term campsites and operating fixtures. The landlord may opt only on a let **to a business for its business** ([§ 9 UStG](https://www.gesetze-im-internet.de/ustg_1980/__9.html)), and for land only so far as the tenant uses it **only** for sales that allow input VAT deduction, which the landlord must prove. Not to a private tenant. Some buildings started before 1 June 1984 or 11 November 1993 escape that test ([§ 27(2) UStG](https://www.gesetze-im-internet.de/ustg_1980/__27.html)). If opted: VAT at 19% of net rent, input VAT recoverable; on the income tax return VAT received is income (line 27) and input VAT a cost (lines 80 to 82).

### Losses ([§ 10d EStG](https://www.gesetze-im-internet.de/estg/__10d.html))

- **Same year**: against other rental income, then other kinds of income (§ 2(3) EStG).
- **Carry-back**: up to EUR 1,000,000 (EUR 2,000,000 joint), to the year before and then the second year before; waivable only in full ("insgesamt abzusehen").
- **Carry-forward**: no time limit; unlimited up to total income of EUR 1 million (EUR 2 million joint), then 70% of the excess (from 2024, § 52(18b)). The page shows no end date; the share for later years is marked "check": confirm it on the current statute before planning a large carry-forward. Fixed by a separate notice (§ 10d(4)).
- **Schemes**: §§ 15a, 15b apply by analogy (§ 21(1) sentence 2). Refer.
- **Lasting losses** with no surplus in sight may be denied; no allowed page sets the test. A permanent home let at 66% or more is fully paid by statute. Refer doubtful cases.
- **Prepayments**: a building's rental loss reduces prepayments only for calendar years beginning **after** its acquisition or completion ([§ 37(3) sentence 8 EStG](https://www.gesetze-im-internet.de/estg/__37.html)); if the building is bought before the year it is completed, count from completion (sentence 9). The bar does not apply where § 7b is claimed (sentence 10). The same timing governs a wage tax allowance ([§ 39a(1) no. 5 EStG](https://www.gesetze-im-internet.de/estg/__39a.html)).

### Sale within ten years ([§ 23 EStG](https://www.gesetze-im-internet.de/estg/__23.html))

- A private sale if acquisition and sale are **not more than** ten years apart; buildings put up or extended in the period are included.
- **Own-use exception**: used **only** for own housing throughout, **or** for own housing in the year of sale and the two years before (the statute does not say "full" years). A flat let up to the sale meets neither.
- **Depreciation comes back**: the cost is **reduced** by AfA, increased and special depreciation deducted (§ 23(3) sentence 4). Gain = price less reduced cost less selling costs.
- **Exemption limit**: tax-free only if all private-sale gains in the year are **less than** EUR 1,000; otherwise all is taxed.
- **Gift**: a single successor takes the donor's acquisition date (§ 23(1) sentence 3); heirs are not named: ask the accountant.
- **Also**: deduct any rest of a § 82b spread, and check § 7b claw-back. More in `de-capital-gains`.

## Boundaries and exceptions

| Situation | Treatment |
| --- | --- |
| Completed 31 Dec 2022 vs 1 Jan 2023 | 2% vs 3% ([§ 7(4) EStG](https://www.gesetze-im-internet.de/estg/__7.html)) |
| Construction started 30 Sep 2023 vs 1 Oct 2023, or on or after 1 Oct 2029 | Declining-balance closed / open / closed (§ 7(5a)) |
| Mixed building, declining-balance | Only the housing part (§ 7(5a)) |
| § 7b application in 2022 | No special depreciation (§ 7b(2)) |
| § 7b cost exactly EUR 5,200 per m² | Qualifies ("nicht übersteigen"); above it nothing does |
| § 7b old window in 2027 | No claim (§ 52(15a)) |
| Works within three years at exactly 15% | Not over: normal rules (§ 6(1) no. 1a) |
| Building half housing, half office by floor area | Not "mainly" housing: no § 82b spread |
| Rent incl. Umlagen just under half / exactly half / exactly 66% of market rent | Split / forecast band / fully paid (§ 21(2)) |
| Cheap let of an office to a relative | Outside § 21(2): refer |
| Sale exactly ten years after acquisition | Still inside ("nicht mehr als zehn Jahre") |
| Total private-sale gains EUR 999 vs EUR 1,000 | Tax-free vs fully taxed (§ 23(3)) |
| Loss in the year the building is bought | Not used for that year's prepayments unless § 7b is claimed (§ 37(3)) |
| Employee, untaxed income EUR 410 vs EUR 411 | No duty from this trigger vs must file (§ 46(2) no. 1) |
| Let to a private tenant with VAT | Not possible (§ 9(1) UStG) |

## Worked cases

Inputs are invented and labelled, except the official example in Case 3. Every amount is recomputed.

### Case 1: new flat, first year ([§ 7 EStG](https://www.gesetze-im-internet.de/estg/__7.html))

Completed February 2026; contract March 2026; benefit and burden pass 1 April 2026. Total cost EUR 400,000; split: land EUR 100,000, building EUR 300,000. Rent EUR 1,200 a month plus Umlagen EUR 250 from April. Paid in 2026: interest EUR 9,000, running costs EUR 2,250, management EUR 600.
- Income: 9 × 1,200 = EUR 10,800, plus 9 × 250 = EUR 2,250; total EUR 13,050.
- Declining-balance (bought in completion year, inside the window, housing): 300,000 × 5% = EUR 15,000; × 9/12 = EUR 11,250 (January to March cut).
- Other costs 9,000 + 2,250 + 600 = EUR 11,850. Result 13,050 − 11,850 − 11,250 = loss of EUR 10,050.
- Straight-line instead: 300,000 × 3% = EUR 9,000; × 9/12 = EUR 6,750; loss EUR 5,550.
- 2027 declining-balance: (300,000 − 11,250) × 5% = EUR 14,437.50.

### Case 2: the 15% cliff ([§ 6(1) no. 1a EStG](https://www.gesetze-im-internet.de/estg/__6.html))

Building completed 1970, bought May 2025; building share EUR 200,000, so the limit is EUR 30,000. Works without VAT: EUR 12,000 in 2025 (deducted in 2025) and EUR 19,000 in 2026; yearly boiler servicing left out.
- Total EUR 31,000 is more than EUR 30,000: **all** of it is production cost, including 2025.
- Depreciated at 2%: 31,000 × 2% = EUR 620 a year. Refer the correction of the 2025 assessment.
- Variant: 2026 works of EUR 18,000 give exactly EUR 30,000: not over; judge each job separately.

### Case 3: cheap let to parents ([official example, 2025 instructions](https://www.elster.de/eportal/helpGlobal?themaGlobal=help_est_ufa_10_2025))

Cold rent EUR 270 plus Umlagen EUR 150 a month; market rent 60 m² × EUR 15 = EUR 900 plus EUR 150 = EUR 1,050.
- Paid share EUR 420 / EUR 1,050 = 40.00%, under 50%: split. Line 87: 60.00%.
- Income (line 32) EUR 5,040; costs in full (line 83) EUR 4,920; cut 60% = EUR 2,952; allowed EUR 1,968.
- Net EUR 5,040 − EUR 1,968 = EUR 3,072, EUR 1,536 per spouse.
- Variants: EUR 700 is 66.67%, fully paid; EUR 600 is 57.14%, forecast band: refer.

### Case 4: § 7b, new window ([§ 7b EStG](https://www.gesetze-im-internet.de/estg/__7b.html))

80 m² flat, application 2024, completed and bought January 2026, Effizienzhaus 40 with QNG seal, let long-term. Building cost EUR 400,000.
- Per m²: 400,000 / 80 = EUR 5,000, not over EUR 5,200: qualifies.
- Base cap 80 × EUR 4,000 = EUR 320,000; special depreciation 320,000 × 5% = EUR 16,000 a year, 2026 to 2029.
- Straight-line on full cost 400,000 × 3% = EUR 12,000 (January: no cut). 2026 total EUR 28,000.
- Variant: EUR 420,000 is EUR 5,250 per m²: no § 7b.

### Case 5: sale inside ten years ([§ 23 EStG](https://www.gesetze-im-internet.de/estg/__23.html))

Bought March 2019 for EUR 300,000 (building EUR 240,000 at 2% = EUR 4,800 a year); sold end of February 2026 for EUR 340,000; selling costs EUR 10,000.
- AfA deducted: 2019, ten months (January and February cut) = EUR 4,000; 2020 to 2025, 6 × 4,800 = EUR 28,800; 2026, two months to the sale, assumed = EUR 800 (confirm the sale-year treatment with the accountant). Total EUR 33,600.
- Reduced cost 300,000 − 33,600 = EUR 266,400. Gain 340,000 − 266,400 − 10,000 = EUR 63,600, all taxed.

### Case 6: new landlord's prepayments ([§ 37 EStG](https://www.gesetze-im-internet.de/estg/__37.html))

The Case 1 client asks in autumn 2026 to cut 2026 prepayments for her EUR 10,050 loss.
- Refused for 2026: the building was acquired in 2026 (§ 37(3) sentence 8). Allowed from 2027. With § 7b claimed the bar would not apply.
- Her adviser-prepared 2025 return is due Monday 1 March 2027.

## When to refuse or refer

- Business property, trading partnerships, or a possible trade in property (gewerblicher Grundstückshandel).
- Non-resident landlords and foreign property (Anlage AUS, treaties).
- The cheap-let forecast band; doubted intention to make a surplus; lasting losses.
- Holiday homes with own use; short-term lets with hotel-like services.
- Shorter actual useful life; change of method on older buildings.
- Doubtful § 7b cases, claw-back, the post-four-year computation; §§ 7h, 7i.
- Correcting an earlier year after the three-year works rule is triggered.
- Co-ownership determinations, heirs' communities, funds, usufruct (Nießbrauch), heritable building rights (Erbbaurecht).
- §§ 15a, 15b loss limits; furniture surcharges in the market-rent test; cheap commercial lets.
- Sale computations beyond the ten-year test (`de-capital-gains`); VAT beyond the basics (`germany-vat-return`); the tariff (`de-einkommensteuer-freelancer`).

## Filing and payment

- **Return**: Anlage V per property, plus V-FeWo and V-Sonstige as needed, through ELSTER.
- **Employees**: must file if untaxed income (rent counts) is **more than** EUR 410; if assessed, such income of **not more than** EUR 410 in total is taken off again, phased out above ([§ 46(2) no. 1, (3), (5) EStG](https://www.gesetze-im-internet.de/estg/__46.html)). One trigger among several.
- **Deadlines** ([§ 149 AO](https://www.gesetze-im-internet.de/ao_1977/__149.html)): unadvised, seven months after the year; for 2026 that is 31 July 2027, a Saturday, so Monday 2 August 2027. Advised: last day of February of the second following year, for 2026 Tuesday 29 February 2028; the tax office may call for it earlier (§ 149(4)). Weekend and holiday deadlines move to the next working day ([§ 108(3) AO](https://www.gesetze-im-internet.de/ao_1977/__108.html)).
- **Late filing** ([§ 152 AO](https://www.gesetze-im-internet.de/ao_1977/__152.html)): compulsory if the return is filed "nicht binnen 14 Monaten nach Ablauf des Kalenderjahrs" (§ 152(2) no. 1), advised or not, so for an advised return it applies from the day after the advised deadline; also compulsory if a return the office called in early is not filed by the date set (no. 3). The 19-month period in no. 2 is only for farmers and foresters with a non-calendar financial year (§ 149(2) sentence 2), not for advised returns. It is 0.25% a month of the tax less prepayments and withheld tax, at least EUR 25 per month or part month. Not compulsory (but still possible at discretion) if the deadline was extended, tax is nil or below, or tax does not exceed prepayments and withheld tax (§ 152(3)).
- **Prepayments** ([§ 37 EStG](https://www.gesetze-im-internet.de/estg/__37.html)): 10 March, 10 June, 10 September, 10 December; set only if at least EUR 400 a year and EUR 100 per date. See the new-building loss rule above.

## Returns being filed now: tax year 2025

- **Unadvised**: due Friday 31 July 2026; passed. A return filed now is late; the compulsory surcharge starts after 14 months (end of February 2027).
- **Advised**: last day of February 2027, a Sunday, so **Monday 1 March 2027**. The compulsory surcharge applies to a return filed after that date. The extensions in Art. 97 § 36(3) EGAO cover only "die Besteuerungszeiträume 2020 bis 2024" ([EGAO](https://www.gesetze-im-internet.de/aoeg_1977/art_97__36.html)); for 2024 the advised date was 30 April 2026.
- Use the 2025 Anlage V and the line map below. Rules are the same for 2025 except the commuting allowance, which rose for 2026 (check the 2025 rate). 2025 is the second-last year for the old § 7b window.

## Anlage V line map (2025 form)

From the 2025 instructions; check the 2026 form. Bank-text keywords in brackets.

| Lines | Content |
| --- | --- |
| 6 to 12 | File number; purchase, completion, sale dates; use (holiday: V-FeWo); living space, own or free part |
| 13 to 19 | Rent without Umlagen: homes 13-15 (MIETE), other rooms 16-18, relatives 19 |
| 20 to 24 | Umlagen (NEBENKOSTEN); 21 settlement (NACHZAHLUNG); 22-23 relatives |
| 25 to 31 | Deposit kept (KAUTION) 25; antenna sites 26; VAT received 27; grants 29-31 |
| 32 | Total income |
| 33 to 45 | Building AfA 33-35; § 7b 36-38; §§ 7h, 7i 39-41; furniture 42-45 |
| 46 to 51 | Interest (DARLEHENSZINSEN) 46-48; loan costs 49-51 |
| 55 to 72 | Maintenance (REPARATUR, HANDWERKER), incl. § 82b spreads |
| 73 to 78 | Running costs passed on 73-75 (GRUNDSTEUER, insurance, Hausgeld settlement); not passed on 76-78 (management, Hausgeld without reserve, KONTOFÜHRUNG) |
| 80 to 83 | Other costs (travel, adviser, tenant broker, low-value items, input VAT); 83 total |
| 85 to 89 | Result and sharing 85-86; cheap-let cut 87-88; acquisition grants 89 |

The instructions name the content of lines 46 to 51 and 55 to 72, the Hausgeld settlement (73 to 75) and, in the official example, account fees (76 to 78); other keyword placements are this Guide's reading of the headings and do not change the total in line 83. **Exclude**: principal (TILGUNG), own transfers, deposit refunds, reserve payments until spent, personal taxes. Transfer tax (GRUNDERWERBSTEUER) goes into acquisition cost.

## Completion checklist

- [ ] § 21 income from a private asset; right forms and form year.
- [ ] Cash-basis income incl. Umlagen, settlements, deposits kept, VAT.
- [ ] Land split off by market values; rate by completion date; declining-balance conditions; month cut; no business-asset rate.
- [ ] § 7b window, cliff, cap, ten-year let; old window not after 2026.
- [ ] Three-year works test, without VAT, on building cost; § 82b only if mainly housing; co-owners on one period.
- [ ] No principal, reserve payments or fines deducted.
- [ ] Cheap-let test per home; line 87 or 88; forecast band referred.
- [ ] Loss offset, carry-back, carry-forward; prepayment rule for new buildings.
- [ ] Sale: ten years, AfA added back, exemption limit.
- [ ] Deadline and surcharge checked; results labelled estimates until an accountant signs off.

## Sources

Statutes on gesetze-im-internet.de (EStG, EStDV, HGB, BRKG, UStG, AO, EGAO), ELSTER's 2025 instructions, and finance-ministry pages, all linked where used above. Also: [§ 7b EStG](https://www.gesetze-im-internet.de/estg/__7b.html), [§ 10d EStG](https://www.gesetze-im-internet.de/estg/__10d.html), [§ 152 AO](https://www.gesetze-im-internet.de/ao_1977/__152.html), [§ 46 EStG](https://www.gesetze-im-internet.de/estg/__46.html), [§ 82b EStDV](https://www.gesetze-im-internet.de/estdv_1955/__82b.html).

## Disclaimer

For information and computation only; not tax, legal or financial advice. OpenAccountants accepts no liability for errors, omissions or outcomes. Have every output reviewed by a qualified professional, such as a Steuerberater, before filing or acting on it.

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
