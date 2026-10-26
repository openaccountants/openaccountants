---
name: nl-zzp-deductions
description: "Dutch business-profit reliefs for a self-employed individual (zzp'er, eenmanszaak, partner in a vof or maatschap) for tax year 2026, under Wet IB 2001 chapter 3. Covers the hours test (urencriterium, 1,225 hours), the 2026 zelfstandigenaftrek (EUR 1,200) and startersaftrek (EUR 2,123), the profit cap and nine-year carry-forward, meewerkaftrek, S&O-aftrek, startersaftrek bij arbeidsongeschiktheid, stakingsaftrek, the 12.7% MKB-winstvrijstelling, the KIA table and disinvestment, the closed FOR, starter free depreciation, the capped benefit rate (tariefsaanpassing, 37.56%), mixed costs and the car addition, and filing by 1 May. Trigger on: zelfstandigenaftrek, startersaftrek, urencriterium, MKB-winstvrijstelling, KIA, oudedagsreserve, zzp deductions, Dutch freelancer tax relief. Out of scope: the full box 1 bill and credits (nl-income-tax), personal deductions (nl-deductions), company cars in payroll (nl-company-car), a bv (nl-corporate-tax)."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/nl-zzp-deductions"
  jurisdiction: "NL"
  tax_year: "2026"
  last_updated: "2026-10-24"
  authored_by: "Michael Cutajar and the OpenAccountants team"
  trust_label: "Built by Michael Cutajar and the OpenAccountants team"
  review_status: "pending_review"
---

# Netherlands: self-employed deductions and business reliefs (2026)

> **Source-cited draft.** No accountant has reviewed this skill yet. Every figure comes from wetten.overheid.nl (Wet IB 2001 as in force from 21 February 2026, AWR) or belastingdienst.nl, read on 24 October 2026. It prepares working papers; it does not file a return.

This skill takes a self-employed person's fiscal profit and works out the reliefs between that profit and taxable profit from business (belastbare winst uit onderneming). The law is Wet inkomstenbelasting 2001 (Wet IB 2001), chapter 3: art. 3.6 (hours test), art. 3.41 to 3.47 (investment deductions), art. 3.74 to 3.79 (ondernemersaftrek), art. 3.79a (MKB-winstvrijstelling), and art. 2.10(2) (the capped benefit rate). The order is fixed: fiscal profit, then ondernemersaftrek, then MKB-winstvrijstelling. The result goes to box 1 in `nl-income-tax`.

## Who this applies to

- **Entrepreneurs for income tax (ondernemers).** A person who runs an enterprise for their own account: a sole trader (eenmanszaak), or a partner in a vof, maatschap or cv. The Belastingdienst judges this on the facts (independence, several clients, own risk, size of the activity). A KvK registration or a VAT number alone does not make someone an entrepreneur for income tax.
- **Not in scope:** income from other work (resultaat uit overige werkzaamheden, for example a single freelance job that is not an enterprise), co-owners (medegerechtigden) and lenders (geldverstrekkers). They get no ondernemersaftrek and no MKB-winstvrijstelling (Fiscale informatie 2026, ch. 8.1).
- **Hours test.** The zelfstandigenaftrek, startersaftrek, S&O-aftrek and meewerkaftrek need the urencriterium (art. 3.6). The MKB-winstvrijstelling, KIA and stakingsaftrek do not.
- **Non-residents** with a Dutch permanent establishment get the same reliefs on that profit (art. 7.2(2)(a) refers to taxable profit under art. 3.2 and 3.3). See `## Cross-border points`.
- **Out of scope here:** the full box 1 tax bill and tax credits (`nl-income-tax`), personal deductions such as mortgage interest, gifts and healthcare costs (`nl-deductions`), people above state pension age in full (`nl-income-tax-special-groups`), a bv and its director (`nl-corporate-tax`, `nl-box2-substantial-interest`), and the energy and environmental investment deductions (EIA, MIA, Vamil), which need an RVO listing and a EUR 2,500 minimum per asset (art. 3.45(4)(b)).

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Urencriterium: minimum business hours in the calendar year (no pro-rating for a part year) | 1,225 hours | 2026 | Wet IB 2001 art. 3.6(1), https://wetten.overheid.nl/BWBR0011353/2026-02-21 ; https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/voorwaarden_urencriterium |
| Pregnancy: unworked hours that still count | the period of employee pregnancy and maternity leave (16 weeks on the Belastingdienst page) | 2026 | art. 3.6(5); same Belastingdienst page |
| Zelfstandigenaftrek, below state pension (AOW) age at 1 January | EUR 1,200 | 2026 | art. 3.76(2), https://wetten.overheid.nl/BWBR0011353/2026-02-21 ; https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/veranderingen-inkomstenbelasting-2026/ondernemersaftrek-2026/zelfstandigenaftrek-2026 |
| Zelfstandigenaftrek (for a 2025 return) | EUR 2,470 | 2025 | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/verandering_inkomstenbelasting_vorige_jaren/veranderingen-inkomstenbelasting-2025/ondernemersaftrek-2025/zelfstandigenaftrek-2025 |
| Startersaftrek (added to the zelfstandigenaftrek) | EUR 2,123 | 2026 (also 2025) | art. 3.76(3); zelfstandigenaftrek-2026 page above |
| Zelfstandigenaftrek and startersaftrek at or above AOW age on 1 January | 50% (EUR 600 and EUR 1,062) | 2026 | art. 3.76(4); https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/ondernemersaftrek_en_investeringsaftrek |
| Carry-forward of unused zelfstandigenaftrek | 9 years, oldest first | 2026 | art. 3.76(5) to (8) |
| Aftrek speur- en ontwikkelingswerk (S&O), with at least 500 S&O hours | EUR 15,979 | 2026 | art. 3.77(1); Fiscale informatie 2026 ch. 8.3 |
| S&O starter increase | EUR 7,996 | 2026 | art. 3.77(2) |
| Meewerkaftrek, partner works 525 to under 875 / 875 to under 1,225 / 1,225 to under 1,750 / 1,750 or more hours | 1.25% / 2% / 3% / 4% of profit | 2026 | art. 3.78(2) |
| Partner pay: deductible only if the pay is at least | EUR 5,000 | 2026 | art. 3.16(4); https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/arbeidsbeloning_aan_fiscale_partner |
| Startersaftrek bij arbeidsongeschiktheid (reduced hours test 800 hours), by prior uses 0 / 1 / 2 | EUR 12,000 / 8,000 / 4,000, capped at profit | 2026 | art. 3.78a(3), (4) |
| Stakingsaftrek (lifetime maximum, less earlier use) | EUR 3,630 | 2026 | art. 3.79(2), (4) |
| MKB-winstvrijstelling, of profit after ondernemersaftrek | 12.7% | 2026 (also 2025) | art. 3.79a; https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/mkb_winstvrijstelling |
| Tariefsaanpassing: extra tax on deductions above the top-band threshold | 11.94% of the lower of the deductions and the excess over EUR 78,426 | 2026 | art. 2.10(2), (3) |
| Effective maximum benefit rate of ondernemersaftrek and MKB-winstvrijstelling | 37.56% (2025: 37.48%) | 2026 | art. 2.10(1); zelfstandigenaftrek-2026 page; MKB page |
| KIA: total qualifying investment up to EUR 2,900 | nil | 2026 | art. 3.41(2), https://wetten.overheid.nl/BWBR0011353/2026-02-21 ; https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/veranderingen-inkomstenbelasting-2026/investeringsaftrek-2026/kleinschaligheidsinvesteringsaftrek-2026 |
| KIA: EUR 2,901 to EUR 71,683 | 28% of the investment | 2026 | art. 3.41(2) |
| KIA: EUR 71,684 to EUR 132,746 | EUR 20,072 | 2026 | art. 3.41(2) |
| KIA: EUR 132,747 to EUR 398,236 | EUR 20,072 less 7.56% of the investment above EUR 132,746 | 2026 | art. 3.41(2) |
| KIA: above EUR 398,236 | nil | 2026 | art. 3.41(2) |
| KIA for a 2025 return | 28% from EUR 2,901 to EUR 70,602; EUR 19,769 to EUR 130,744; then less 7.56% of the excess; nil above EUR 392,230 | 2025 | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/verandering_inkomstenbelasting_vorige_jaren/veranderingen-inkomstenbelasting-2025/investeringsaftrek-2025/kleinschaligheidsinvesteringsaftrek-2025 |
| KIA: minimum per asset | EUR 450 | 2026 | art. 3.45(2)(b) |
| Starter free depreciation (willekeurige afschrijving): ceiling on the year's qualifying investment | EUR 398,236 (the top of the KIA table) | 2026 | Uitvoeringsregeling willekeurige afschrijving 2001 art. 7, 8, https://wetten.overheid.nl/BWBR0012035/2025-01-01 ; art. 3.41(2) |
| Disinvestment addition: disposals in the year above, within 5 years | EUR 2,900 | 2026 | art. 3.47(1), (2) |
| Fiscale oudedagsreserve (FOR): new additions | none since 1 January 2023 | 2026 | art. 3.67 (repealed 1 January 2023); art. 10a.29 |
| Mixed costs (food, drink, entertainment, congresses): non-deductible threshold, or elect 80% deductible | EUR 5,700, or 80% | 2026 | art. 3.15(1), (5); https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/veranderingen-inkomstenbelasting-2026/drempel-beperkt-aftrekbare-kosten-2026 |
| Business use of a privately owned or privately rented vehicle (car, motorbike, bike) | EUR 0.23 per km in the law in force; the Belastingplan 2027 bill raises it to EUR 0.25 back to 1 January 2026, and the Belastingdienst page already says EUR 0.25 | 2026 | art. 3.15(6), 3.17(1)(b); Kamerstuk 37022 nr. 2, art. I parts C and D, art. LXIII(1)(a), https://zoek.officielebekendmakingen.nl/kst-37022-2.html ; https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/veranderingen-inkomstenbelasting-2026/zakelijk-gebruik-privevervoermiddel-2026 |
| Business car used privately: minimum addition to profit | 22% of the car's value (35% if first used more than 16 years ago); none if private use is 500 km or less a year | 2026 | art. 3.20(1) |
| Assessment threshold (aanslaggrens): no assessment unless tax due exceeds prepaid tax by more than | EUR 58 | 2026 | art. 9.4(1)(a), https://wetten.overheid.nl/BWBR0011353/2026-02-21 |
| Tax interest (belastingrente), income tax | 5% | from 1 January 2026 | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/standaard_functies/prive/contact/rechten_en_plichten_bij_de_belastingdienst/belastingrente/overzicht_percentages_belastingrente |
| Default penalty for a late income tax return | EUR 469, up to EUR 6,709 | 2026 | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/standaard_functies/prive/contact/rechten_en_plichten_bij_de_belastingdienst/boete |

## The taxable base

**Step 1: confirm the enterprise and the hours.** Count every hour actually worked for the enterprise, not only billed hours: quotations, bookkeeping and the business website count; standby time without work does not. At least 1,225 hours in the calendar year, even if the business started on 1 July. Unless the person was not an entrepreneur in one or more of the five previous years, more of their total working time must go to the enterprise than to other work such as a job (art. 3.6(1)(a), (b)). In a partnership with household members or direct-line relatives, hours do not count if the work is mainly supportive (the Belastingdienst uses 70% or more) and unrelated parties would not form such a partnership, or if the partnership serves an enterprise from which only the related person draws profit (art. 3.6(2) to (4)). The client must make the hours plausible with a diary, invoices, quotations or timesheets. Failing the hours test does not turn business profit into other income; it only removes the hours-dependent deductions.

**Step 2: fiscal profit.** Start from the annual profit under sound business practice (art. 3.25), not from bank receipts. Adjust for:
- **Mixed costs (art. 3.15).** Food, drink, entertainment, receptions, congresses and study trips: either the first EUR 5,700 is not deductible, or the client elects in the return to deduct 80%.
- **Costs barred or limited for the entrepreneur personally (art. 3.16, 3.17).** A workspace in a home that is not business property is not deductible unless it is a self-contained part of the home and the income tests of art. 3.16(1)(a) or (b) are met. Ordinary clothing, non-trade literature and a home phone subscription are not deductible. A privately owned or privately rented vehicle used for the business: EUR 0.23 per km under the law in force, covering fuel, insurance, tolls and parking (art. 3.17(1)(b)); see the pending-law note in `## Sources` for EUR 0.25. Pay to a fiscal partner is deductible only if it is EUR 5,000 or more (art. 3.16(4)); the partner then declares it as income. Recoverable VAT is not a cost.
- **Business car used privately (art. 3.20).** Add at least 22% of the car's value to profit (35% for a car first used more than 16 years ago), with a reduction for a zero-emission car (art. 3.20(2)). No addition if the client proves private use of 500 km or less a year. The 2026 detail (value, reductions, the zero-emission cap) is in `nl-company-car`.
- **Depreciation.** Assets are depreciated over their life down to residual value. Buildings stop at a floor value (art. 3.30a). A starter may depreciate freely (willekeurige afschrijving, art. 3.34 and Uitvoeringsregeling willekeurige afschrijving 2001 art. 7 to 9) on assets committed to in a year in which the startersaftrek applies, or in the year just before such a year if no zelfstandigenaftrek applied in it. The KIA exclusions of art. 3.45(1), (2) and (5) and the related-party rule of art. 3.46 apply. Free depreciation is limited to investments of up to EUR 398,236 in the year, the top of the KIA table; above that the client picks which assets to depreciate freely. The KIA minimum of EUR 2,900 does not apply. If within five years from the start of the investment year the asset is rented out, used for a business whose profit falls under a double-taxation rule, or used for forestry, the book value is restated to normal depreciation and the difference is profit (art. 3.38; regulation art. 9; Belastingdienst, willekeurige afschrijving startende ondernemer).
- **KIA (art. 3.41).** If the client invested more than EUR 2,900 in the year in qualifying assets and chooses it in the return, deduct the KIA from profit on top of normal depreciation; do not expense the asset. Investing means entering the obligation (art. 3.43). If the asset is not in use at year end, KIA is limited to what was paid, with the rest following later payments (art. 3.44). Excluded: land, homes, ordinary passenger cars not for professional road transport, securities, goodwill, permits, animals (art. 3.45(1)), assets mainly made available to third parties, and any asset under EUR 450 (art. 3.45(2)). Purchases from household members, direct-line relatives or a company in which the client holds a third or more do not count (art. 3.46). In a partnership the investments are added together and the KIA split by share (art. 3.41(3)).
- **Disinvestment (art. 3.47).** If assets sold in a year fetch more than EUR 2,900 and the sale is within five years of the start of the investment year, add back the same percentage of the sale price as the KIA originally given, capped at the investment that got KIA. Taking an asset into private use counts as a disposal at market value. Not paying 25% within twelve months (unless in use) or not using the asset within three years undoes the investment.
- **FOR (old age reserve).** No additions since 2023. An existing reserve stays on the balance sheet under the old release rules (art. 10a.29, applying the old art. 3.70 to 3.73). It decreases when the client buys a qualifying annuity and records the same release. It is released into profit when it exceeds business equity and either the client reached AOW age by 1 January or failed the hours test this year and last year, on cessation, and on death unless a partner continuing the business takes it over (Belastingdienst, oudedagsreserve).

**Step 3: ondernemersaftrek (art. 3.74).** The sum of:
- **Zelfstandigenaftrek (art. 3.76).** EUR 1,200 if the hours test is met. It cannot exceed profit before ondernemersaftrek, unless the client also gets the startersaftrek. The unused part becomes niet-gerealiseerde zelfstandigenaftrek, set by an appealable decision on the assessment, usable in the next nine years against profit above that year's zelfstandigenaftrek, oldest first. A year where the cap cut the deduction to nil still counts as a year of use for the starter lookback (art. 3.76(5)).
- **Startersaftrek (art. 3.76(3)).** EUR 2,123 on top, if the client was not an entrepreneur in one or more of the five previous years and used the zelfstandigenaftrek no more than twice in those five years. Not available after a tax-neutral return of a business from a bv (art. 14c Wet Vpb 1969) in the year or the five years before. It is not optional: if due, it is claimed with the zelfstandigenaftrek, and together they may create a loss.
- **S&O-aftrek (art. 3.77).** EUR 15,979 if the hours test is met and at least 500 hours went to work covered by an RVO S&O declaration; EUR 7,996 more for a starter with declarations for no more than two of the previous five years.
- **Meewerkaftrek (art. 3.78).** For an entrepreneur who meets the hours test and whose partner works in the business at least 525 hours unpaid (the Belastingdienst also accepts pay under EUR 5,000). A percentage of profit by partner hours, excluding expropriation, cessation and exit profit. Not combined with deductible partner pay.
- **Startersaftrek bij arbeidsongeschiktheid (art. 3.78a).** For a starter on a disability benefit who works at least 800 hours but fails the 1,225-hour test, below AOW age. EUR 12,000, 8,000 or 4,000 depending on earlier uses in the previous five years, capped at profit.
- **Stakingsaftrek (art. 3.79).** Up to EUR 3,630 of profit on ceasing a whole business, less amounts used in earlier years.

At AOW age on 1 January, the zelfstandigenaftrek and startersaftrek are halved (art. 3.76(4)).

**Step 4: MKB-winstvrijstelling (art. 3.79a).** 12.7% of profit after ondernemersaftrek. No hours test. If the result is a loss, the exemption reduces the loss.

**Step 5: capped benefit (art. 2.10(2), (3)).** Ondernemersaftrek and a positive MKB-winstvrijstelling are base-reducing items. If box 1 income plus these items exceeds EUR 78,426, tax rises by 11.94% of the lower of (a) the items and (b) the excess. In effect they save tax at no more than 37.56%. Own-home costs and personal deductions share the same cap; `nl-deductions` handles them.

**Losses.** A box 1 loss is set off against box 1 income of the previous three years and the next nine (art. 3.150; `nl-income-tax`). This is separate from the unused zelfstandigenaftrek ledger.

## Deadlines and filing

- An entrepreneur for income tax reports the profit and the reliefs above in the income tax return (aangifte inkomstenbelasting), filed digitally. A non-resident files in Mijn Belastingdienst or on paper.
- The return for 2026 is due by the date in the invitation letter, usually 1 May 2027 (AWR art. 9(1): at least one month after the invitation).
- Extension: request it before the due date with the paper form "Aanvraag uitstel aangifte inkomstenbelasting" (no online request); it gives four extra months. A return filed on or after 1 May 2027 does not get the art. 30fc(4) interest exemption, so belastingrente runs from 1 July 2027.
- No invitation letter: a person who owes tax above the assessment threshold must ask for a return and file (AWR art. 6(3)). For 2026 the threshold is EUR 58: an assessment follows if tax due exceeds prepaid tax by more than EUR 58 (Wet IB art. 9.4(1)(a)).
- Choices made in the return: the KIA (art. 3.41(1)) and the 80% option for mixed costs (art. 3.15(5)).
- The assessment shows the niet-gerealiseerde zelfstandigenaftrek and its use. Keep those decisions; the carry-forward depends on them.

## Penalties and interest

- **Late or no return:** default penalty (verzuimboete) of EUR 469 for income tax, rising to EUR 6,709 for repeat failures. Failing to ask for a return in time: EUR 3,354 (Belastingdienst, boete; AWR art. 67a).
- **Late payment** of an assessment: 5% of the unpaid amount, minimum EUR 50, maximum EUR 6,709.
- **Wrong return:** offence penalty (vergrijpboete) of 25% of the tax for gross negligence and 50% for intent, higher for repeat offences or fraud.
- **Tax interest (belastingrente):** 5% a year from 1 January 2026. For income tax it runs from 1 July 2027 (six months after the year) until the assessment is payable (AWR art. 30fc(1), (2)). None if the assessment is set in line with a return received before 1 May 2027 (art. 30fc(4)). If the assessment follows the return, interest stops at the latest 19 weeks after the return was received (art. 30fc(3)).

## Cross-border points

- **Non-resident with a Dutch business.** Taxable profit from a Dutch enterprise (run through a permanent establishment or permanent representative in the Netherlands) is computed under art. 3.2 and 3.3, so ondernemersaftrek and MKB-winstvrijstelling apply to it (art. 7.2(2)(a)).
- **Resident with a foreign permanent establishment.** Profit is computed under Dutch rules on worldwide income; relief for double taxation follows the treaty or the Besluit voorkoming dubbele belasting 2001 (`nl-double-tax-relief`).
- **KIA and foreign use.** Assets meant mainly for a business, or part of one, whose profit falls under a double-taxation rule get no investment deduction (art. 3.45(1)(a)(2)). Moving an asset to that use within five years counts as a disposal (art. 3.47(3)(c)). Starter free depreciation is restated in the same case.
- **Emigration.** Moving business assets abroad or ending Dutch liability triggers a final settlement (art. 3.60, 3.61), and that profit is excluded from the meewerkaftrek base (art. 3.78(3)(c)). See `nl-cross-border`.

## Worked examples

### Example 1: established freelancer with new equipment (2026)

A designer, below AOW age, has been self-employed for eight years and works 1,600 hours, all in the business. Profit after normal depreciation is EUR 52,800. In 2026 she bought equipment for EUR 10,000 (each item above EUR 450). The investment is between EUR 2,901 and EUR 71,683, so KIA is 28% of EUR 10,000 = EUR 2,800. Profit before ondernemersaftrek: EUR 50,000. She is not a starter, so the zelfstandigenaftrek is EUR 1,200, within profit. Profit after ondernemersaftrek is EUR 48,800. The MKB-winstvrijstelling is 12.7% of that, EUR 6,197.60. Taxable profit is EUR 42,602.40. She has no other income, so box 1 income plus the deductions (EUR 50,000) stays under EUR 78,426: no tariefsaanpassing.

```oa-check
name: Established freelancer, KIA, zelfstandigenaftrek and MKB (2026)
inputs:
  profit_after_depreciation: 52800
  investment: 10000
  kia_rate: 0.28
  zelfstandigenaftrek: 1200
  mkb_rate: 0.127
  top_band_threshold: 78426
steps:
  - kia: investment * kia_rate
  - profit_before_oa: profit_after_depreciation - kia
  - za: min(zelfstandigenaftrek, profit_before_oa)
  - profit_after_oa: profit_before_oa - za
  - mkb: profit_after_oa * mkb_rate
  - taxable_profit: profit_after_oa - mkb
  - excess_over_top_band: max(taxable_profit + za + mkb - top_band_threshold, 0)
expected:
  kia: 2800.00
  profit_before_oa: 50000.00
  profit_after_oa: 48800.00
  mkb: 6197.60
  taxable_profit: 42602.40
  excess_over_top_band: 0.00
```

### Example 2: high-earning starter hit by the tariefsaanpassing (2026)

A consultant started in 2025 after years in employment and works 1,500 hours, all in the business. 2026 is her second year of zelfstandigenaftrek, so she gets the startersaftrek. Profit before ondernemersaftrek is EUR 120,000 and she has no other box 1 income. Ondernemersaftrek is EUR 1,200 + EUR 2,123 = EUR 3,323. Profit after ondernemersaftrek is EUR 116,677. MKB-winstvrijstelling is 12.7% of that, EUR 14,817.98. Taxable profit is EUR 101,859.02. The deductions total EUR 18,140.98. Box 1 income plus the deductions is EUR 120,000, which is EUR 41,574 above EUR 78,426. The deductions are the lower figure, so the tariefsaanpassing is 11.94% of EUR 18,140.98 = EUR 2,166.03. At the 49.50% top rate the deductions would save EUR 8,979.79; after the adjustment they save EUR 6,813.76, which is 37.56% of the deductions (EUR 6,813.75) to within one cent of rounding.

```oa-check
name: Starter with profit EUR 120,000, capped benefit (2026)
inputs:
  profit_before_oa: 120000
  zelfstandigenaftrek: 1200
  startersaftrek: 2123
  mkb_rate: 0.127
  top_band_threshold: 78426
  adjustment_rate: 0.1194
  top_rate: 0.495
steps:
  - ondernemersaftrek: zelfstandigenaftrek + startersaftrek
  - profit_after_oa: profit_before_oa - ondernemersaftrek
  - mkb: profit_after_oa * mkb_rate
  - taxable_profit: profit_after_oa - mkb
  - deductions: ondernemersaftrek + mkb
  - excess: max(taxable_profit + deductions - top_band_threshold, 0)
  - tariefsaanpassing: round(min(deductions, excess) * adjustment_rate, 2)
  - saving_at_top_rate: round(deductions * top_rate, 2)
  - net_saving: saving_at_top_rate - tariefsaanpassing
expected:
  ondernemersaftrek: 3323.00
  profit_after_oa: 116677.00
  mkb: 14817.98
  taxable_profit: 101859.02
  deductions: 18140.98
  excess: 41574.00
  tariefsaanpassing: 2166.03
  saving_at_top_rate: 8979.79
  net_saving: 6813.76
```

## Ask the client first

1. Hours worked for the business in 2026, how they are recorded, and hours in any job or other work. Was there a pregnancy break?
2. Were you an entrepreneur in each of 2021 to 2025, and in which of those years was the zelfstandigenaftrek applied (including years where profit cut it to nil)? Did a business come back to you from a bv?
3. Your age on 1 January 2026 against your AOW date.
4. Assets bought or sold in 2026: dates, amounts excluding recoverable VAT, sellers, whether in use and paid; any car, and private kilometres.
5. Does a fiscal partner work in the business: hours and any pay?
6. Earlier assessments showing niet-gerealiseerde zelfstandigenaftrek, losses, or an FOR balance.

## Sources

| Source | URL | Read on |
|---|---|---|
| Wet inkomstenbelasting 2001, art. 2.10, 3.6, 3.15 to 3.17, 3.20, 3.30a, 3.34, 3.41 to 3.47, 3.67, 3.74 to 3.79a, 3.150, 7.2, 10a.29 (version from 21 February 2026) | https://wetten.overheid.nl/BWBR0011353/2026-02-21 | 2026-10-24 |
| Algemene wet inzake rijksbelastingen, art. 6, 8, 9, 30fa to 30fc, 67a | https://wetten.overheid.nl/BWBR0002320/2026-01-01 | 2026-10-24 |
| Belastingdienst, Fiscale informatie 2026 ch. 8, Ondernemersaftrek en investeringsaftrek | https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/ondernemersaftrek_en_investeringsaftrek | 2026-10-24 |
| Belastingdienst, Zelfstandigenaftrek 2026 | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/veranderingen-inkomstenbelasting-2026/ondernemersaftrek-2026/zelfstandigenaftrek-2026 | 2026-10-24 |
| Belastingdienst, Zelfstandigenaftrek 2025 | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/verandering_inkomstenbelasting_vorige_jaren/veranderingen-inkomstenbelasting-2025/ondernemersaftrek-2025/zelfstandigenaftrek-2025 | 2026-10-24 |
| Belastingdienst, Startersaftrek | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/ondernemersaftrek/startersaftrek | 2026-10-24 |
| Belastingdienst, Verrekenen niet-gerealiseerde zelfstandigenaftrek | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/ondernemersaftrek/zelfstandigenaftrek1/verrekenen_niet_gerealiseerde_zelfstandigenaftrek | 2026-10-24 |
| Belastingdienst, Voorwaarden urencriterium | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/voorwaarden_urencriterium | 2026-10-24 |
| Belastingdienst, Wanneer bent u ondernemer voor de inkomstenbelasting? | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/wanneer_bent_u_ondernemer_voor_de_inkomstenbelasting/ | 2026-10-24 |
| Belastingdienst, Mkb-winstvrijstelling | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/mkb_winstvrijstelling | 2026-10-24 |
| Belastingdienst, Kleinschaligheidsinvesteringsaftrek 2026 | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/veranderingen-inkomstenbelasting-2026/investeringsaftrek-2026/kleinschaligheidsinvesteringsaftrek-2026 | 2026-10-24 |
| Belastingdienst, Kleinschaligheidsinvesteringsaftrek 2025 | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/verandering_inkomstenbelasting_vorige_jaren/veranderingen-inkomstenbelasting-2025/investeringsaftrek-2025/kleinschaligheidsinvesteringsaftrek-2025 | 2026-10-24 |
| Belastingdienst, Willekeurige afschrijving startende ondernemer | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/afschrijving/willekeurige_afschrijving/startende_ondernemer | 2026-10-24 |
| Belastingdienst, Oudedagsreserve | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/fiscale_reserves/oudedagsreserve | 2026-10-24 |
| Belastingdienst, Arbeidsbeloning aan fiscale partner | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/arbeidsbeloning_aan_fiscale_partner | 2026-10-24 |
| Belastingdienst, Drempel beperkt aftrekbare kosten 2026 | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/veranderingen-inkomstenbelasting-2026/drempel-beperkt-aftrekbare-kosten-2026 | 2026-10-24 |
| Belastingdienst, Afbouw tarief aftrekposten bij hoog inkomen | https://www.belastingdienst.nl/wps/wcm/connect/nl/aftrek-en-kortingen/content/afbouw-tarief-aftrekposten-bij-hoog-inkomen | 2026-10-24 |
| Belastingdienst, Aangifte inkomstenbelasting voor ondernemers | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/aangifte_inkomstenbelasting_voor_ondernemers | 2026-10-24 |
| Belastingdienst, Wanneer moet mijn aangifte inkomstenbelasting binnen zijn? | https://www.belastingdienst.nl/wps/wcm/connect/nl/belastingaangifte/content/wanneer-moet-ik-aangifte-doen | 2026-10-24 |
| Belastingdienst, Uitstel aanvragen belastingaangifte | https://www.belastingdienst.nl/wps/wcm/connect/nl/belastingaangifte/content/kan-ik-nog-uitstel-aanvragen-belastingaangifte | 2026-10-24 |
| Belastingdienst, Moet ik aangifte doen? | https://www.belastingdienst.nl/wps/wcm/connect/nl/belastingaangifte/content/moet_ik_aangifte_doen | 2026-10-24 |
| Uitvoeringsregeling willekeurige afschrijving 2001, art. 7 to 9 (version in force from 1 January 2025, still current) | https://wetten.overheid.nl/BWBR0012035/2025-01-01 | 2026-10-24 |
| Belastingdienst, Zakelijk gebruik privévervoermiddel 2026 | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/veranderingen-inkomstenbelasting-2026/zakelijk-gebruik-privevervoermiddel-2026 | 2026-10-24 |
| Kamerstuk 37022 nr. 2, Belastingplan 2027 (bill) | https://zoek.officielebekendmakingen.nl/kst-37022-2.html | 2026-10-24 |
| Kamerstuk 37022 nr. 3, Belastingplan 2027, memorie van toelichting par. 5.5 | https://www.tweedekamer.nl/kamerstukken/wetsvoorstellen/detail?cfg=wetsvoorsteldetails&qry=wetsvoorstel%3A37022 | 2026-10-24 |
| Belastingdienst, Boete | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/standaard_functies/prive/contact/rechten_en_plichten_bij_de_belastingdienst/boete | 2026-10-24 |
| Belastingdienst, Overzicht percentages belastingrente | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/standaard_functies/prive/contact/rechten_en_plichten_bij_de_belastingdienst/belastingrente/overzicht_percentages_belastingrente | 2026-10-24 |

Pending law: the Belastingplan 2027 bill (Kamerstuk 37022, sent to the Tweede Kamer on 15 September 2026, not enacted on 24 October 2026) raises the business car rate in art. 3.15(6) and 3.17(1)(b) from EUR 0.23 to EUR 0.25 with effect back to 1 January 2026 (art. I parts C and D, art. LXIII(1)(a)); the Belastingdienst already applies EUR 0.25 for 2026. The same bill cuts the startersaftrek in art. 3.76(3) to EUR 10 (art. I part G) and repeals it from 1 January 2028; the explanatory memorandum (nr. 3, par. 5.5) says the cut applies from 1 January 2027 and that starters can still use the startersaftrek in 2026. Starter free depreciation is to end from 1 January 2028 through the Eindejaarsregeling 2026, and the startersaftrek bij arbeidsongeschiktheid from 1 January 2029. Recheck once the Staatsblad text is published.

Not yet confirmed: the commencement clause of the bill as introduced (art. LXIII(1)(a)) lists art. I part G among the parts backdated to 1 January 2026, which conflicts with the memorandum; this skill follows the law in force (EUR 2,123 for 2026) until the enacted text settles it; the statute says the meewerkaftrek partner works "without any remuneration" while the Belastingdienst also accepts pay under EUR 5,000, so that point rests on the authority's reading; the 70% figure for supportive work in a related-person partnership comes from the Belastingdienst page, not the statute.

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

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-10-24. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `nl-zzp-deductions` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/nl-zzp-deductions. If neither is available, confirm every figure against the official source pages cited above before relying on it.
