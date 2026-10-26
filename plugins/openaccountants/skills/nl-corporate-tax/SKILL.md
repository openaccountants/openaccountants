---
name: nl-corporate-tax
description: "Dutch corporate income tax (vennootschapsbelasting, Vpb) for a resident bv or nv, tax year 2026. Covers the 19% and 25.8% rates with the EUR 200,000 bracket, the fiscal profit and what is not deductible, partly deductible costs (EUR 5,700 or 73.5%), depreciation caps and the building floor value, the director-shareholder usual salary, the participation exemption, the fiscal unity, earnings stripping (24.5% of tax EBITDA or EUR 1,000,000), loss carry-back of one year and unlimited carry-forward with the EUR 1,000,000 plus 50% cap, the 30% ownership-change rule, the innovation box, liquidation and cessation losses, provisional assessments, the return deadline and extensions, tax interest (belastingrente) and penalties. Trigger on: vennootschapsbelasting, Vpb aangifte, gemengde kosten, bodemwaarde, gebruikelijk loon, Dutch corporate tax, BV tax, fiscale eenheid, deelnemingsvrijstelling, earnings stripping, verliesverrekening, innovatiebox, liquidatieverlies, voorlopige aanslag, belastingr"
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/nl-corporate-tax"
  jurisdiction: "NL"
  tax_year: "2026"
  last_updated: "2026-10-24"
  authored_by: "Michael Cutajar and the OpenAccountants team"
  trust_label: "Built by Michael Cutajar and the OpenAccountants team"
  review_status: "pending_review"
---

# Netherlands corporate income tax (vennootschapsbelasting, Vpb), 2026

This skill covers Dutch corporate income tax for a Dutch-resident bv (private limited company) or nv (public limited company) for financial years in 2026. The law is the Wet op de vennootschapsbelasting 1969 (Wet Vpb) as in force from 1 January 2026. The Belastingplan 2026 (Stb. 2025, 444) changes the Wet Vpb only from 1 January 2029, so the 2026 rates and limits are the same as 2025. Related skills: [nl-dividend-withholding](nl-dividend-withholding.md), [netherlands-transfer-pricing](netherlands-transfer-pricing.md), [nl-cross-border](nl-cross-border.md), [nl-double-tax-relief](nl-double-tax-relief.md), [nl-box2-substantial-interest](nl-box2-substantial-interest.md), [nl-tax-objection](nl-tax-objection.md), [netherlands-financial-statements](netherlands-financial-statements.md).

## Who this applies to

- **A bv or nv always files** a Vpb return. Foundations (stichtingen) and associations (verenigingen) file only in certain cases; they are out of scope.
- **Residence.** A body incorporated under Dutch law is deemed established in the Netherlands for most of the Wet Vpb (art. 2(5)). Otherwise residence follows the facts: where management sits, the head office, where shareholder meetings are held. See [nl-cross-border](nl-cross-border.md).
- **Financial year.** Usually the calendar year. A broken year (for example May to April) is allowed if it matches the articles of association. The first and last years may be longer or shorter.
- **A non-resident company** with a Dutch permanent establishment is taxed on that Dutch income only. See [nl-dividend-withholding](nl-dividend-withholding.md) for the permanent establishment rules.
- **Out of scope:** banks and insurers (extra interest rule at 89.4% of the balance sheet total in 2026), fiscal and exempt investment institutions (fbi, vbi), limited partnerships (cv) and mutual funds (fgr) under the 2025 classification reform, housing corporations, mergers and demergers.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source URL |
|---|---|---|---|
| Vpb on taxable amount up to and including EUR 200,000 (Wet Vpb art. 22) | 19% | 2026 (same 2023 to 2025) | https://wetten.overheid.nl/BWBR0002672/2026-01-01 |
| Vpb on taxable amount above EUR 200,000 (art. 22: EUR 38,000 plus 25.8% of the excess) | 25.8% | 2026 | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/tarieven_vennootschapsbelasting |
| Earnings stripping: net interest not deductible above the higher of (art. 15b(1)) | 24.5% of adjusted profit, or EUR 1,000,000 | 2026 (and 2025; 20% in 2023 and 2024) | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/veranderingen-vennootschapsbelasting-2026 |
| Loss carry-back (art. 20(2)) | 1 year | 2026 | https://wetten.overheid.nl/BWBR0002672/2026-01-01 |
| Loss carry-forward (art. 20(2)) | No time limit | Losses from 2022 on, and older losses still open at end 2021 | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/verrekenen_van_verliezen |
| Yearly loss offset cap (art. 20(2)) | EUR 1,000,000 plus 50% of taxable profit above EUR 1,000,000 | 2026 | https://wetten.overheid.nl/BWBR0002672/2026-01-01 |
| Ownership change that blocks loss carry-forward (art. 20a) | 30% or more of the ultimate interest | 2026 | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/verrekenen_van_verliezen/belangenwijziging |
| Provisional loss carry-back | At most 80% of the loss declared | 2026 | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/verrekenen_van_verliezen |
| Participation exemption threshold (art. 13(2)(a)) | At least 5% of nominal paid-up capital | 2026 | https://wetten.overheid.nl/BWBR0002672/2026-01-01 |
| Subject-to-tax test for an investment participation | A 10% profit tax normally counts as realistic | 2026 | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/deelnemingsvrijstelling/kwalificerende_beleggingsdeelneming |
| Fiscal unity holding (art. 15(1)) | At least 95% of shares, votes, profit and capital | 2026 | https://wetten.overheid.nl/BWBR0002672/2026-01-01 |
| Fiscal unity earliest start (art. 15(9)) | 3 months before the request | 2026 | https://wetten.overheid.nl/BWBR0002672/2026-01-01 |
| Innovation box (art. 12b) | Qualifying benefits count for 9/25.8, an effective 9% | 2026 | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/innovatiebox |
| Innovation box fixed option (art. 12bd(1)) | 25% of profit before the box, at most EUR 25,000 | 2026 | https://wetten.overheid.nl/BWBR0002672/2026-01-01 |
| Innovation box smaller taxpayer | Gross IP benefit under EUR 37.5 million and net turnover at most EUR 250 million, over the year plus 4 prior years | 2026 | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/innovatiebox/kleinere-en-grotere-belastingplichtigen |
| Liquidation loss cap (art. 13d(2)) and cessation loss cap (art. 15i(4)) | EUR 5,000,000 unless the EU/EEA and control conditions are met | 2026 | https://wetten.overheid.nl/BWBR0002672/2026-01-01 |
| Partly deductible costs: threshold, company with employees (art. 8(5); Wet IB 2001 art. 3.15(1)) | Not deductible up to the higher of EUR 5,700 and 0.4% of the year's taxed wages | 2026 (EUR 5,700 also in 2025) | https://wetten.overheid.nl/BWBR0002672/2026-01-01 |
| Partly deductible costs: alternative if chosen in the return (art. 8(5); Wet IB 2001 art. 3.15(5)) | 73.5% deductible | 2026 | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/veranderingen-inkomstenbelasting-2026/drempel-beperkt-aftrekbare-kosten-2026 |
| Yearly depreciation cap (art. 8(1); Wet IB 2001 art. 3.30(2)) | Goodwill at most 10%, other assets at most 20% of cost | 2026 | https://wetten.overheid.nl/BWBR0011353/2026-01-01 |
| Floor value for depreciation of buildings (art. 8(1); Wet IB 2001 art. 3.30a) | WOZ value of the building for the calendar year of the depreciation | 2026 | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/afschrijving-vennootschapsbelasting |
| Usual salary of a director-shareholder (gebruikelijk loon, wage tax rule, pointer) | At least EUR 58,000 (EUR 56,000 in 2024 and 2025) | 2026 | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/prive/vermogen_en_aanmerkelijk_belang/aanmerkelijk_belang/loon_en_aanmerkelijk_belang/loon_en_aanmerkelijk_belang |
| Dividend tax on distributions (pointer) | 15% | 2026 | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/dividendbelasting/als_u_dividend_uitkeert |
| Minimum tax (Pillar Two, pointer) | 15%, groups with revenue of at least EUR 750 million | 2026 | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/minimumbelasting |
| Tax interest (belastingrente) on Vpb | 5% from 1 January 2026; 6.5% in 2025 | 2026 | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/standaard_functies/prive/contact/rechten_en_plichten_bij_de_belastingdienst/belastingrente/overzicht_percentages_belastingrente |
| Late or missing Vpb return penalty | EUR 3,354, up to EUR 6,709 for several years in a row | 2026 | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/standaard_functies/prive/contact/rechten_en_plichten_bij_de_belastingdienst/boete |
| Late payment penalty | 5% of the unpaid amount, minimum EUR 50, maximum EUR 6,709 each time | 2026 | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/standaard_functies/prive/contact/rechten_en_plichten_bij_de_belastingdienst/boete |

The rate bracket is "tot en met EUR 200,000": a taxable amount of exactly EUR 200,000 is taxed wholly at 19%.

## The taxable base

**Start from the commercial result.** The taxable amount (belastbaar bedrag) is the taxable profit of the financial year minus losses that can still be offset. Taxable profit applies tax rules to the commercial accounts under sound business practice (goed koopmansgebruik). Many income tax profit rules apply through art. 8(1): business costs, depreciation, investment deductions, tax reserves. The self-employed deduction does not apply to a company.

**Add back what is never deductible.** Profit distributions, under whatever name or form (art. 10(1)(a)); the Vpb, the minimum tax and foreign profit taxes relieved under a double tax arrangement (art. 10(1)(e)); criminal and administrative fines, including comparable foreign and EU fines (art. 8(1) applying Wet IB 2001 art. 3.14(1)(c)).

**Partly deductible costs (art. 8(5)).** In a year in which the company has one or more employees, costs of food, drink and stimulants, of representation (receptions, parties, entertainment) and of congresses, seminars, excursions and study trips, with the related travel and stay, are not deductible up to a threshold (Wet IB 2001 art. 3.15(1) and (2)). The threshold is EUR 5,700, or 0.4% of the total wages of the employees taxed under Wet LB 1964 arts. 20a, 20b, 26 and 26b if that is higher. The company may choose in the return to leave wages from former employment out of that total. Instead of the threshold, the company may choose in the return to deduct 73.5% of these costs (art. 8(5), applying art. 3.15(5)). The limit does not apply where the company's business is supplying these goods or services as part of its turnover (art. 3.15(3)).

**Depreciation (art. 8(1) applying Wet IB 2001 arts. 3.30 and 3.30a).** Depreciation per year is at most 10% of cost for goodwill and at most 20% of cost for other assets (art. 3.30(2)). These are ceilings: the yearly amount still follows cost, residual value and useful life. A building is depreciated only while its book value is above its floor value (bodemwaarde), and by at most the difference (art. 3.30a(1)). The floor value is the WOZ value set for the building for the calendar year of the depreciation; for a broken financial year, the calendar year in which it ends (art. 3.30a(3) and (4)). Land is not depreciated.

**Director-shareholder salary.** A shareholder with a substantial interest who works for the company is deemed to receive a usual salary (gebruikelijk loon) of at least the highest of: the pay in the most comparable employment, the pay of the company's (or a related company's) highest-paid employee, and EUR 58,000 for 2026. A lower amount applies only if the shareholder shows that comparable work is usually paid less; if the usual salary across all the person's companies is EUR 5,000 or less and that is shown, the actual pay is used. This is a wage tax rule; the salary paid is a deductible cost in the company's profit.

**Participation exemption (art. 13).** Dividends and gains on a participation are exempt. Losses on it are not deductible, and costs of buying or selling it are not deductible either. A participation is at least 5% of the nominal paid-up capital of a company with share capital, or one of the other routes in art. 13(2) (a 5% fgr holding, a cooperative membership, the pull-along rules). A holding that falls below 5% after more than one year keeps the exemption for 3 more years, if it was exempt without a break. An investment participation (one whose assets are mainly portfolio investments, or that mainly finances the group) is exempt only if it passes the subject-to-tax test or the asset test; otherwise a credit applies instead (deelnemingsverrekening): the benefit is grossed up by 100/95 and included in profit, and the company credits the lower of 5% of the grossed-up benefit and the Vpb attributable to it. Credit not used for lack of Vpb carries forward to the next year by decision.

**Liquidation and cessation losses.** A loss on a participation that shows up after the subsidiary is dissolved (liquidatieverlies) is deductible despite the participation exemption (art. 13d(1)). The loss is the amount paid for the participation minus the liquidation distributions (art. 13d(5)). It counts only up to EUR 5,000,000 unless, just before the liquidation ends, the company holds a qualifying interest (one that lets it decide the subsidiary's activities, art. 13d(4)) in a subsidiary established in the Netherlands, the EU or the EEA, and has met that condition without a break for the 5 years before (art. 13d(2)). A cessation loss on closing a foreign permanent establishment (stakingsverlies, art. 15i) has the same EUR 5,000,000 cap unless the establishment was in the EU or EEA, and is deductible only if the activities are not largely continued by a related body.

**Fiscal unity (art. 15).** On request of both companies, a parent and a subsidiary in which it holds the full legal and economic ownership of at least 95% of the shares, with at least 95% of the votes and rights to at least 95% of profit and capital, are taxed as one taxpayer. The parent files; the subsidiary no longer files on its own. Losses of one member offset profits of another. Both must use the same financial years and profit rules and be established in the Netherlands, with EU exceptions for a Dutch granddaughter or Dutch sisters held through an EU company. The unity starts on the date named in the request, but not earlier than 3 months before the request (art. 15(9)). It ends when the conditions are no longer met (art. 15(10)). A Vpb fiscal unity is not a VAT fiscal unity.

**Earnings stripping (art. 15b).** Net interest is interest costs on loans minus interest income on loans, at least nil. It is not deductible to the extent it exceeds the higher of 24.5% of adjusted profit and EUR 1,000,000. Adjusted profit (gecorrigeerde winst) is profit before this limit, plus depreciation, plus write-downs (minus reversals), plus net interest: broadly tax EBITDA, at least nil. The disallowed amount carries forward without time limit and is deducted in a later year to the extent that year's net interest is below the limit, oldest first. The inspector fixes it in a decision open to objection (art. 15b(5)).

**Innovation box (art. 12b).** If the company chooses it in the return, qualifying benefits from an intangible it developed itself count for 9/H, where H is the top rate (25.8%), an effective rate of 9%. It applies only while the balance of qualifying benefits is positive, and only above the production costs already deducted (the box threshold). A smaller taxpayer needs an R&D declaration (S&O-verklaring from RVO); a larger one also needs a further right such as a patent, plant breeder's right or software. A company that created a qualifying asset in the year or the 2 prior years may instead take a fixed 25% of profit before the box, at most EUR 25,000, if that profit is positive (art. 12bd(1)). Innovation losses are deductible at the normal rate.

**Losses (art. 20 and 20a).** A loss is carried back to the previous year first, then forward without time limit. In each year the offset is capped at EUR 1,000,000 plus 50% of the taxable profit above EUR 1,000,000; a taxable profit of EUR 1,000,000 or less can be fully offset. Losses are used in the order they arose, and only once the inspector has fixed them in a decision open to objection. If the ultimate interest in the company changes by 30% or more, earlier losses can no longer be carried forward, unless the asset test (assets not more than 50% investments for more than 3 months) and the activities and intention tests are met. Exceptions: inheritance or matrimonial property, and an acquirer who already held at least one third at the start of the oldest loss year (art. 20a(2)).

**Order of the computation.** Commercial result, add-backs (including the partly deductible costs and any depreciation above the caps or below the building floor value), participation exemption, earnings stripping, innovation box, then loss offset, then the rate table on the taxable amount.

## Deadlines and filing

- **Return.** Calendar year: before 1 June of the next year (the 2026 return is due before 1 June 2027; the 2025 return was due before 1 June 2026). Broken year: within 5 months after the end of the financial year. Short year ending 31 December: by 1 June of the next year; short year ending in another month: before 1 April of the next calendar year.
- **How.** Through Mijn Belastingdienst Zakelijk, tax software or a tax service provider.
- **Extension.** Online in Mijn Belastingdienst Zakelijk to 1 November, for a calendar year only; apply before 1 June (the form is open from 1 March to 1 June). For a longer extension or a broken year, use the paper form with reasons, within 5 months after the end of the financial year. A tax service provider can also request it.
- **Provisional assessments (voorlopige aanslag).** Most companies get one at the start of the year, based on earlier years. The company must check it and ask for a change if it expects a higher or lower profit; changes can be passed on until the return is filed, and the Belastingdienst processes at most 3 increases for one year. There is no objection against a provisional assessment, only a request to change it. If none arrives and tax is expected, ask for one. The final assessment credits all provisional assessments.
- **Asking for a return.** A company that receives no return invitation must ask for one within 6 months after the tax debt arose.
- **Loss and interest decisions.** Losses and carried-forward interest are fixed in decisions open to objection. See [nl-tax-objection](nl-tax-objection.md).

## Penalties and interest

- **Tax interest (belastingrente).** Charged if the return is received on or after 1 June after the tax year, or if the assessment departs from the return (even one filed before 1 June). It runs from 1 July after the tax year. If the return is followed unchanged, it runs at most to 19 weeks after the return is received, or to 6 weeks after the assessment date if earlier. No tax interest if the return is filed before 1 June and followed unchanged, or if a provisional assessment is requested before 1 May and imposed as asked. For a broken year, read the 5th month after year end for 1 May and the 6th month for 1 June. Interest is computed with 30-day months and a 360-day year, rounded down to whole euros.
- **Rate.** 5% from 1 January 2026, 6.5% for 2025. The Supreme Court (Hoge Raad) ruled on 16 January 2026 that the higher Vpb rate could not be used, and the Belastingdienst cut the Vpb rates from 2022 to the general rate (2026 had been 7.5%).
- **Late or missing return.** Filed after the deadline in the demand (aanmaning), or not at all: EUR 3,354, rising to EUR 6,709 for several years in a row. No penalty if the company is not at all to blame.
- **Not asking for a return in time:** EUR 3,354 (none if asked within 2 weeks after the 6-month term).
- **Late payment.** 5% of the unpaid amount of the (provisional) assessment, minimum EUR 50, maximum EUR 6,709 each time.
- **Incorrect return.** 25% of the tax withheld for gross negligence, 50% for intent, up to 100% for fraud or a repeat offence. Correcting the return in time avoids this penalty.

## Cross-border points

- **Dividends paid.** A bv or nv paying a dividend usually withholds 15% dividend tax, with exemptions for qualifying shareholders. Payments to affiliates in listed low-tax jurisdictions also attract the conditional withholding tax. See [nl-dividend-withholding](nl-dividend-withholding.md).
- **Foreign branches.** Profit from a foreign permanent establishment is exempt under the object exemption (art. 15e); a final cessation loss is deductible within the art. 15i limits. See [nl-double-tax-relief](nl-double-tax-relief.md).
- **Transfer pricing.** Related-party prices must be at arm's length (art. 8b). See [netherlands-transfer-pricing](netherlands-transfer-pricing.md).
- **Foreign subsidiaries.** They qualify for the participation exemption on the same 5% test; an investment participation needs the subject-to-tax or asset test. A foreign liquidation loss above EUR 5,000,000 counts only for EU or EEA subsidiaries.
- **Minimum tax (Pillar Two).** Groups with consolidated revenue of at least EUR 750 million fall under the Wet minimumbelasting 2024 at 15%. The top-up information return (BIA) is due within 15 months after the reporting year (18 months for the first year); a top-up tax return within 17 months (20 for the first year). Refer to a specialist.
- **Residence and migration.** Moving a company's place of management in or out of the Netherlands is in [nl-cross-border](nl-cross-border.md).

## Worked examples

**Example 1: small bv with a participation dividend (2026).** A calendar-year bv has a commercial profit before tax of EUR 480,000. This includes EUR 60,000 of dividend from a 40% held active trading subsidiary, and is after EUR 5,000 of administrative fines that the bv paid. There are no losses to offset and net interest is far below EUR 1,000,000. The dividend is exempt under the participation exemption, so it comes out. The fines are not deductible, so they are added back. Taxable amount: 480,000 minus 60,000 plus 5,000 = EUR 425,000. Tax: 19% on EUR 200,000 is EUR 38,000, plus 25.8% on EUR 225,000 is EUR 58,050, total EUR 96,050. The provisional assessments already paid are credited against this.

```oa-check
name: NL bv, commercial profit EUR 480,000 with exempt dividend and fines (2026)
inputs:
  commercial_profit: 480000
  participation_dividend: 60000
  fines: 5000
  bracket: 200000
steps:
  - taxable_amount: commercial_profit - participation_dividend + fines
  - tax_low: min(taxable_amount, bracket) * 19 / 100
  - tax_high: max(taxable_amount - bracket, 0) * 25.8 / 100
  - vpb: tax_low + tax_high
expected:
  taxable_amount: 425000
  tax_low: 38000
  tax_high: 58050
  vpb: 96050
```

**Example 2: interest limit and loss cap in the same year (2026).** A bv has a profit before the interest limit of EUR 4,500,000. It booked depreciation of EUR 1,000,000 and net interest of EUR 2,500,000. Adjusted profit is 4,500,000 plus 1,000,000 plus 2,500,000 = EUR 8,000,000. 24.5% of that is EUR 1,960,000, higher than EUR 1,000,000, so that is the limit. EUR 540,000 of interest is not deductible this year and carries forward. Taxable profit becomes EUR 5,040,000. The bv has a 2025 loss of EUR 4,000,000 that it could not carry back. The offset cap is EUR 1,000,000 plus 50% of EUR 4,040,000 = EUR 3,020,000, so only EUR 3,020,000 of the loss is used and EUR 980,000 carries forward. Taxable amount: EUR 2,020,000. Tax: EUR 38,000 plus 25.8% of EUR 1,820,000 (EUR 469,560) = EUR 507,560. The edge: the interest add-back raises the profit, and the loss cap stops the loss from wiping it out.

```oa-check
name: NL bv, earnings stripping then capped loss offset (2026)
inputs:
  profit_before_limit: 4500000
  depreciation: 1000000
  net_interest: 2500000
  loss_brought_forward: 4000000
  threshold: 1000000
  bracket: 200000
steps:
  - adjusted_profit: profit_before_limit + depreciation + net_interest
  - interest_limit: max(adjusted_profit * 24.5 / 100, threshold)
  - interest_disallowed: max(net_interest - interest_limit, 0)
  - taxable_profit: profit_before_limit + interest_disallowed
  - offset_cap: threshold + max(taxable_profit - threshold, 0) * 50 / 100
  - loss_used: min(loss_brought_forward, offset_cap)
  - loss_left: loss_brought_forward - loss_used
  - taxable_amount: taxable_profit - loss_used
  - vpb: min(taxable_amount, bracket) * 19 / 100 + max(taxable_amount - bracket, 0) * 25.8 / 100
expected:
  adjusted_profit: 8000000
  interest_limit: 1960000
  interest_disallowed: 540000
  taxable_profit: 5040000
  offset_cap: 3020000
  loss_used: 3020000
  loss_left: 980000
  taxable_amount: 2020000
  vpb: 507560
```

## Ask the client first

1. The financial year (calendar, broken, short or long) and which return this is (2025 being finalised, or 2026).
2. Every shareholding the company holds: percentage, how long, and what the subsidiary does (active business, investments, group financing); any subsidiary liquidated or foreign branch closed.
3. Is there a fiscal unity decision, which companies, and from which date?
4. Interest paid and received, including group loans, plus depreciation, to test the EUR 1,000,000 and 24.5% limits.
5. Losses still open by year (the loss decisions), and any change of 30% or more in the ultimate ownership since the oldest loss year.
6. Provisional assessments received and paid, and whether an extension was granted.
7. Whether the company had employees in the year, its total taxed wages, and its costs of food, drink, representation and congresses, to pick between the threshold and the 73.5% method.
8. Buildings owned (book value and WOZ value for the year), and any goodwill; and the salary paid to each director-shareholder.

## Sources

| Source | URL | Read on |
|---|---|---|
| Wet op de vennootschapsbelasting 1969, arts. 2, 8, 10, 12b, 12bd, 13, 13d, 15, 15b, 15i, 20, 20a, 22 (in force from 1 January 2026) | https://wetten.overheid.nl/BWBR0002672/2026-01-01 | 2026-10-24 |
| Wet Vpb 1969, change overview (Belastingplan 2026, Stb. 2025, 444; Overige fiscale maatregelen 2026, Stb. 2025, 445) | https://wetten.overheid.nl/BWBR0002672/2026-01-01/0/informatie | 2026-10-24 |
| Belastingplan 2026, Stb. 2025, 444 (art. IXA: Wet Vpb change from 1 January 2029) | https://zoek.officielebekendmakingen.nl/stb-2025-444.html | 2026-10-24 |
| Wet inkomstenbelasting 2001, arts. 3.14 (fines not deductible), 3.15 (partly deductible costs), 3.30 and 3.30a (depreciation caps, building floor value), version in force from 1 January 2026 | https://wetten.overheid.nl/BWBR0011353/2026-01-01 | 2026-10-24 |
| Belastingdienst, threshold for partly deductible costs 2026 (EUR 5,700; 73.5% for Vpb) | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/veranderingen-inkomstenbelasting-2026/drempel-beperkt-aftrekbare-kosten-2026 | 2026-10-24 |
| Belastingdienst, depreciation for Vpb (buildings stop at WOZ value) | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/afschrijving-vennootschapsbelasting | 2026-10-24 |
| Belastingdienst, salary and substantial interest (gebruikelijk loon EUR 58,000 in 2026) | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/prive/vermogen_en_aanmerkelijk_belang/aanmerkelijk_belang/loon_en_aanmerkelijk_belang/loon_en_aanmerkelijk_belang | 2026-10-24 |
| Belastingdienst, credit for investment participations (deelnemingsverrekening) | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/deelnemingsvrijstelling/deelnemingsverrekening | 2026-10-24 |
| Belastingdienst, Vpb rates | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/tarieven_vennootschapsbelasting | 2026-10-24 |
| Belastingdienst, changes to Vpb 2026 | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/veranderingen-vennootschapsbelasting-2026 | 2026-10-24 |
| Belastingdienst, earnings stripping | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/generieke-renteaftrekbeperking | 2026-10-24 |
| Belastingdienst, offsetting losses | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/verrekenen_van_verliezen | 2026-10-24 |
| Belastingdienst, change of ownership | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/verrekenen_van_verliezen/belangenwijziging | 2026-10-24 |
| Belastingdienst, participations | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/deelnemingsvrijstelling/deelnemingen | 2026-10-24 |
| Belastingdienst, qualifying investment participation | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/deelnemingsvrijstelling/kwalificerende_beleggingsdeelneming | 2026-10-24 |
| Belastingdienst, fiscal unity | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/fiscale_eenheid_vennootschapsbelasting | 2026-10-24 |
| Belastingdienst, innovation box | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/innovatiebox | 2026-10-24 |
| Belastingdienst, innovation box smaller and larger taxpayers | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/innovatiebox/kleinere-en-grotere-belastingplichtigen | 2026-10-24 |
| Belastingdienst, filing the Vpb return | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/aangifte-vennootschapsbelasting-doen | 2026-10-24 |
| Belastingdienst, extension for the Vpb return | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/uitstel_aangifte_vennootschapsbelasting | 2026-10-24 |
| Belastingdienst, provisional assessment | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/voorlopige_aanslag_vennootschapsbelasting | 2026-10-24 |
| Belastingdienst, tax interest on Vpb | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/standaard_functies/prive/contact/rechten_en_plichten_bij_de_belastingdienst/belastingrente/belastingrente_betalen_bij_vennootschapsbelasting | 2026-10-24 |
| Belastingdienst, tax interest rates | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/standaard_functies/prive/contact/rechten_en_plichten_bij_de_belastingdienst/belastingrente/overzicht_percentages_belastingrente | 2026-10-24 |
| Belastingdienst, penalties | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/standaard_functies/prive/contact/rechten_en_plichten_bij_de_belastingdienst/boete | 2026-10-24 |
| Belastingdienst, paying a dividend (15% dividend tax) | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/dividendbelasting/als_u_dividend_uitkeert | 2026-10-24 |
| Belastingdienst, minimum tax | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/minimumbelasting | 2026-10-24 |

Not yet confirmed: the tax interest rate for 2027 (set once a year from the ECB rate before 1 November); the measures in the Belastingplan 2027 presented on 15 September 2026, which are not yet law; how the earnings stripping limit is split inside a fiscal unity when pre-joining losses are offset.

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

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-10-24. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `nl-corporate-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/nl-corporate-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
