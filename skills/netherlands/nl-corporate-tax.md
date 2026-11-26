---
name: nl-corporate-tax
description: "Dutch corporate income tax (vennootschapsbelasting, Vpb) for a resident bv or nv, tax year 2026. Covers the 19% and 25.8% rates with the EUR 200,000 bracket, the fiscal profit and what is not deductible, partly deductible costs (EUR 5,700 or 73.5%), depreciation caps and the building floor value, the director-shareholder usual salary, the participation exemption, the fiscal unity, earnings stripping (24.5% of tax EBITDA or EUR 1,000,000), loss carry-back of one year and unlimited carry-forward with the EUR 1,000,000 plus 50% cap, the 30% ownership-change rule, the innovation box, liquidation and cessation losses, provisional assessments, the return deadline and extensions, tax interest (belastingrente) and penalties. Trigger on: vennootschapsbelasting, Vpb aangifte, gemengde kosten, bodemwaarde, gebruikelijk loon, Dutch corporate tax, BV tax, fiscale eenheid, deelnemingsvrijstelling, earnings stripping, verliesverrekening, innovatiebox, liquidatieverlies, voorlopige aanslag, belastingrente Vpb. Out of scope: dividend tax and conditional withholding tax (nl-dividend-withholding), transfer pricing (netherlands-transfer-pricing), residence and emigration (nl-cross-border), foreign tax relief (nl-double-tax-relief), the shareholder's box 2 tax (nl-box2-substantial-interest), objections (nl-tax-objection)."
version: 1.4
jurisdiction: NL
tax_year: 2026
last_updated: 2026-11-26
depends_on:
  - income-tax-workflow-base
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
---

# Netherlands corporate income tax (vennootschapsbelasting, Vpb), 2026

This skill covers Dutch corporate income tax for a Dutch-resident bv (private limited company) or nv (public limited company) for financial years in 2026. The law is the Wet op de vennootschapsbelasting 1969 (Wet Vpb) as in force from 1 January 2026. Related skills: [nl-dividend-withholding](nl-dividend-withholding.md), [netherlands-transfer-pricing](netherlands-transfer-pricing.md), [nl-cross-border](nl-cross-border.md), [nl-double-tax-relief](nl-double-tax-relief.md), [nl-box2-substantial-interest](nl-box2-substantial-interest.md), [nl-tax-objection](nl-tax-objection.md), [netherlands-financial-statements](netherlands-financial-statements.md).

## Who this applies to

- **A bv or nv always files** a Vpb return. Foundations (stichtingen) and associations (verenigingen) file only in certain cases; they are out of scope.
- **Residence.** A body incorporated under Dutch law is deemed established in the Netherlands for most of the Wet Vpb (art. 2(5)). Otherwise residence follows the facts: where management sits, the head office, where shareholder meetings are held. See [nl-cross-border](nl-cross-border.md).
- **Financial year.** Usually the calendar year. A broken year (for example May to April) is allowed if it matches the articles of association. The first and last years may be longer or shorter. Changing the financial year only to get a one-off tax advantage is not allowed ([Belastingdienst, taxable amount and financial year](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/belastbaar_bedrag)).
- **A non-resident company** with a Dutch permanent establishment is taxed on that Dutch income only. For permanent-establishment scope see [nl-cross-border](nl-cross-border.md); dividend withholding is in [nl-dividend-withholding](nl-dividend-withholding.md).
- **Out of scope:** banks and insurers, fiscal and exempt investment institutions (fbi, vbi), limited partnerships (cv) and mutual funds (fgr), housing corporations, mergers and demergers.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source URL |
|---|---|---|---|
| Vpb on taxable amount up to and including EUR 200,000 (Wet Vpb art. 22) | 19% | 2026 | https://wetten.overheid.nl/BWBR0002672/2026-01-01 |
| Vpb on taxable amount above EUR 200,000 (art. 22: EUR 38,000 plus 25.8% of the excess) | 25.8% | 2026 | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/tarieven_vennootschapsbelasting ; https://wetten.overheid.nl/BWBR0002672/2026-01-01 |
| Earnings stripping: net interest not deductible above the higher of (art. 15b(1)) | 24.5% of adjusted profit, or EUR 1,000,000 | 2026 | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/veranderingen-vennootschapsbelasting-2026 |
| Loss carry-back (art. 20(2)) | 1 year | 2026 | https://wetten.overheid.nl/BWBR0002672/2026-01-01 |
| Loss carry-forward (art. 20(2)) | No time limit | Losses from 2022 on, and older losses still open at end 2021 | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/verrekenen_van_verliezen |
| Yearly loss offset cap (art. 20(2)) | EUR 1,000,000 plus 50% of taxable profit above EUR 1,000,000 | 2026 | https://wetten.overheid.nl/BWBR0002672/2026-01-01 |
| Ownership change that blocks loss carry-forward (art. 20a) | 30% or more of the ultimate interest | 2026 | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/verrekenen_van_verliezen/belangenwijziging |
| Provisional loss carry-back | At most 80% of the loss declared | 2026 | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/verrekenen_van_verliezen |
| Participation exemption threshold (art. 13(2)(a)) | At least 5% of nominal paid-up capital | 2026 | https://wetten.overheid.nl/BWBR0002672/2026-01-01 |
| Subject-to-tax test for an investment participation | A nominal 10% profit tax alone is insufficient: establish the comparable Dutch tax base and the full subject-to-tax/asset-test conditions | 2026 | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/deelnemingsvrijstelling/kwalificerende_beleggingsdeelneming |
| Fiscal unity holding (art. 15(1)) | At least 95% of shares, votes, profit and capital | 2026 | https://wetten.overheid.nl/BWBR0002672/2026-01-01 |
| Fiscal unity earliest start (art. 15(9)) | 3 months before the request | 2026 | https://wetten.overheid.nl/BWBR0002672/2026-01-01 |
| Innovation box (art. 12b) | Qualifying benefits count for 9/25.8 in taxable profit; 9% effective tax assumes that fraction is taxed at 25.8%, rather than being a separate flat tax | 2026 | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/innovatiebox |
| Innovation box fixed option (art. 12bd(1)-(2)) | 25% of positive profit before the box, at most EUR 25,000; if all relevant assets are in qualifying partnerships, use the art. 12bd(2) benefit-share percentage | 2026 | https://wetten.overheid.nl/BWBR0002672/2026-01-01 |
| Innovation box smaller taxpayer | Gross IP benefit under EUR 37.5 million and company net turnover (consolidated group turnover where applicable) strictly below EUR 250 million, over the year plus 4 prior years; use the highest-turnover group where the statutory multiple-group rule applies and include acquisition costs in the gross-IP-benefit test | 2026 | https://wetten.overheid.nl/BWBR0002672/2026-01-01#HoofdstukII_Afdeling2.3_Artikel12ba ; https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/innovatiebox/kleinere-en-grotere-belastingplichtigen |
| Liquidation and cessation losses (arts. 13d and 15i) | Specialist calculation, including the EUR 5,000,000 restriction and statutory exceptions: Check this point with one of our partner accountants. | 2026 | https://wetten.overheid.nl/BWBR0002672/2026-01-01 |
| Partly deductible costs: threshold, company with employees (art. 8(5); Wet IB 2001 art. 3.15(1)) | Not deductible up to the higher of EUR 5,700 and 0.4% of the year's taxed wages | 2026 | https://wetten.overheid.nl/BWBR0002672/2026-01-01 |
| Partly deductible costs: alternative if chosen in the return (art. 8(5); Wet IB 2001 art. 3.15(5)) | 73.5% deductible | 2026 | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/veranderingen-inkomstenbelasting-2026/drempel-beperkt-aftrekbare-kosten-2026 |
| Yearly depreciation cap (art. 8(1); Wet IB 2001 art. 3.30(2)) | Goodwill at most 10%, other assets at most 20% of cost | 2026 | https://wetten.overheid.nl/BWBR0011353/2026-01-01 |
| Floor value for depreciation of buildings (art. 8(1); Wet IB 2001 art. 3.30a) | WOZ value of the building for the calendar year of the depreciation | 2026 | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/afschrijving-vennootschapsbelasting |
| Usual salary of a director-shareholder (gebruikelijk loon, wage tax rule, pointer) | At least EUR 58,000 (EUR 56,000 in 2024 and 2025) | 2026 | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/prive/vermogen_en_aanmerkelijk_belang/aanmerkelijk_belang/loon_en_aanmerkelijk_belang/loon_en_aanmerkelijk_belang |
| Dividend tax on distributions (pointer) | 15% | 2026 | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/dividendbelasting/als_u_dividend_uitkeert |
| Minimum tax (Pillar Two, pointer) | Scope, computation and filing/payment dates: Check this point with one of our partner accountants. | 2026 | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/minimumbelasting |
| Tax interest (belastingrente) on Vpb | 5% from 1 January 2026; 6.5% in 2025 | 2026 | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/standaard_functies/prive/contact/rechten_en_plichten_bij_de_belastingdienst/belastingrente/overzicht_percentages_belastingrente |
| Late or missing Vpb return penalty | EUR 3,354, up to EUR 6,709 for several years in a row | 2026 | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/standaard_functies/prive/contact/rechten_en_plichten_bij_de_belastingdienst/boete |
| Late payment penalty | 5% of the unpaid amount, minimum EUR 50, maximum EUR 6,709 each time | 2026 | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/standaard_functies/prive/contact/rechten_en_plichten_bij_de_belastingdienst/boete |

The rate bracket is "tot en met EUR 200,000": a taxable amount of exactly EUR 200,000 is taxed wholly at 19%.

For an investment participation, a nominal 10% rate does not establish a realistic tax charge: compare the applicable base with the Dutch base. The alternative asset test ordinarily requires strictly less than half low-tax free portfolio investments, with the statutory look-through and financing exceptions; establish those definitions before applying the exemption (art. 13(11)).

## The taxable base

**Start from the commercial result.** The taxable amount (belastbaar bedrag) is the taxable profit of the financial year minus losses that can still be offset. Taxable profit applies tax rules to the commercial accounts under sound business practice (goed koopmansgebruik). Many income tax profit rules apply through art. 8(1): business costs, depreciation, investment deductions, tax reserves. The self-employed deduction does not apply to a company.

**Add back what is never deductible.** Profit distributions, under whatever name or form (art. 10(1)(a)); the Vpb, the minimum tax and foreign profit taxes relieved under a double tax arrangement (art. 10(1)(e)); criminal and administrative fines, including comparable foreign and EU fines (art. 8(1) applying Wet IB 2001 art. 3.14(1)(c)); and gifts, promises or services that are a criminal offence such as bribery (Wet IB 2001 art. 3.14(1)(h)).

**Debt-forgiveness profit (art. 8(4)).** A profit from a creditor giving up rights that cannot be realised (kwijtscheldingswinst) is not part of the profit to the extent it exceeds the loss of that year plus the losses still to be offset. If the losses still to be offset are more than EUR 1,000,000, the profit is exempt to the extent it exceeds the loss of the year, and the open losses are reduced by the exempt amount, oldest first. A debt that becomes unenforceable under art. 358 Faillissementswet counts as given up. Article 8(4) does not apply within six years after leaving a fiscal unity, except to the extent the company shows the benefit would have been excluded without that unity (art. 8(16)). For a former unity member: Check this point with one of our partner accountants.

**Partly deductible costs (art. 8(5)).** In a year in which the company has one or more employees, costs of food, drink and stimulants, of representation (receptions, parties, entertainment) and of congresses, seminars, excursions and study trips, with the related travel and stay, are not deductible up to a threshold (Wet IB 2001 art. 3.15(1) and (2)). The threshold is EUR 5,700, or 0.4% of the total wages of the employees taxed under Wet LB 1964 arts. 20a, 20b, 26 and 26b if that is higher. The company may choose in the return to leave wages from former employment out of that total. Instead of the threshold, the company may choose in the return to deduct 73.5% of these costs (art. 8(5), applying art. 3.15(5)). The limit does not apply where the company's business is supplying these goods or services as part of its turnover (art. 3.15(3)).

**Depreciation (art. 8(1) applying Wet IB 2001 arts. 3.30 and 3.30a).** Depreciation per year is at most 10% of cost for goodwill and at most 20% of cost for other assets (art. 3.30(2)). These are ceilings: the yearly amount still follows cost, residual value and useful life. A building is depreciated only while its book value is above its floor value (bodemwaarde), and by at most the difference (art. 3.30a(1)). The floor value is the WOZ value set for the building for the calendar year of the depreciation; for a broken financial year, the calendar year in which it ends (art. 3.30a(3) and (4)). Land is not depreciated. Accelerated (willekeurige) depreciation is allowed only for designated assets, such as environmental assets (MIA/Vamil); the book value may not fall below the residual value, and before the asset is in use the depreciation is at most the amount paid in the year ([Belastingdienst, Vpb depreciation](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/afschrijving-vennootschapsbelasting)).

**Director-shareholder salary.** A shareholder with a substantial interest who works for the company is deemed to receive a usual salary (gebruikelijk loon) of at least the highest of: the pay in the most comparable employment, the pay of the company's (or a related company's) highest-paid employee, and EUR 58,000 for 2026. A lower amount applies only if the shareholder shows that comparable work is usually paid less; if the usual salary across all the person's companies is EUR 5,000 or less and that is shown, the actual pay is used. This is a wage tax rule. Genuine salary expense is ordinarily deductible, but establish the applicable deemed-additional-salary and arm’s-length/excessive-remuneration adjustments; cash paid alone does not settle the fiscal deduction.

**Participation exemption (art. 13).** Under the ordinary participation exemption, qualifying dividends and gains are exempt; losses and acquisition/disposal costs are not deductible. The exemption does not cover payments the subsidiary can deduct, legally or in fact, directly or indirectly, from a profit-tax base, or receipts replacing those payments (art. 13(17)). Specific taxpayer and CFC rules also apply; for those cases: Check this point with one of our partner accountants. A participation is at least 5% of the nominal paid-up capital of a company with share capital, or one of the other routes in art. 13(2) (a 5% fgr holding, a cooperative membership, shares carrying at least 5% of the votes in a company in an EU member state whose tax treaty with the Netherlands reduces dividend tax by voting rights, the pull-along rules) ([Belastingdienst, participations](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/deelnemingsvrijstelling/deelnemingen)). A holding that falls below 5% after more than one year keeps the exemption for 3 more years, if it was exempt without a break. An investment participation (one whose assets are mainly portfolio investments, or that mainly finances the group) is exempt only if it passes the subject-to-tax test or the asset test; A participation is always an investment participation, whatever the intention, if the subsidiary's consolidated assets consist mostly of interests below 5%, or if its function (with its 5% subsidiaries) is mostly financing the taxpayer or related bodies or their business assets (art. 13(10)). Subject to the mandatory art. 13(10) classification just stated, the purpose-based assessment can exclude an investment purpose where the subsidiary’s business extends the taxpayer’s own, or a top/intermediate holding has a genuine management, policy or financing function for the group; purpose alone cannot override art. 13(10) ([Belastingdienst, investment participation](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/deelnemingsvrijstelling/wanneer_is_een_deelneming_een_beleggingsdeelneming)). For a nonqualifying investment participation, the participation-credit calculation (deelnemingsverrekening), including related costs and any Directive election: Check this point with one of our partner accountants.

**Liquidation and cessation losses (arts. 13d and 15i).** A liquidation loss starts with the amount sacrificed for the participation less liquidation distributions, subject to statutory adjustments. Eligibility depends on completion, other relief, continuation, timing and, above EUR 5,000,000, additional control/location rules and their exceptions. Foreign-branch cessation losses have separate eligibility, timing and restart-recapture rules. Check this point with one of our partner accountants.

**Fiscal unity (art. 15).** On request of both companies, a parent and a subsidiary in which it holds the full legal and economic ownership of at least 95% of the shares, with at least 95% of the votes and rights to at least 95% of profit and capital, are taxed as one taxpayer. The parent files; the subsidiary no longer files on its own. Ordinary current-period profits/losses can be pooled, but art. 15ae restricts pre-joining loss use by attribution; historical losses are not freely pooled. The companies need matching tax periods and profit rules (or the statutory permitted rule adjustment), qualifying legal forms and Dutch residence including the applicable treaty test; the shares must not be inventory. EU/EEA intermediary/top-company and qualifying nonresident-PE routes have separate conditions (art. 15(4)-(8)): Check this point with one of our partner accountants. The unity starts on the date named in the request, but not earlier than 3 months before the request (art. 15(9)). It ends when the conditions cease to be met, on the migration/top-company events in art. 15(10)(b)-(g), or on joint request of the parent and subsidiary from the requested date, no earlier than submission (art. 15(10)(h)). Ending it for one subsidiary does not itself end it for the other members. Migration, top-company changes and pre-joining loss/interest allocation: Check this point with one of our partner accountants. A Vpb fiscal unity is not a VAT fiscal unity.

**Earnings stripping (art. 15b).** Net interest is interest costs on loans minus interest income on loans, at least nil; costs on loans and on hedges of their interest or currency risk, currency results on loans and results on those hedges also count (art. 15b(6)(b) and (c)), so refer cases with loan fees, currency or hedging results. It is not deductible to the extent it exceeds the higher of 24.5% of adjusted profit and EUR 1,000,000. Adjusted profit (gecorrigeerde winst) starts with profit before this limit, plus the applicable depreciation, net write-downs and net interest, with a nil floor. Do not add back capitalized interest again or include interest attributable to exempt foreign business; establish the statutory definitions rather than applying a broad EBITDA label. The ordinary disallowed amount carries forward without time limit and uses later headroom, oldest first, subject to the ownership-change block in art. 15ba and its statutory exceptions; carry-forward is not unconditional after a substantial ownership change. The inspector fixes it in a decision open to objection (art. 15b(5)).

**Innovation box (art. 12b).** If the company chooses it in the return, qualifying benefits from an intangible it developed itself count for 9/H, where H is the top rate (25.8%), 9% effective tax only where the included fraction is taxed at the top rate; apply the actual rate table to taxable profit, rather than a separate flat 9% charge. It applies only while the balance of qualifying benefits is positive, and only above the production costs already deducted (the box threshold). A smaller taxpayer needs an R&D declaration (S&O-verklaring from RVO); a larger one also needs one of: a patent or plant breeder's right (granted or applied for), software, a permit to use a non-chemical crop protection method, an EU marketing authorisation for a medicine, a supplementary protection certificate, a registered utility model, or an intangible connected with one of these (art. 12ba(1)(b)). Trademarks and logos never qualify (art. 12ba(6)). A bought intangible qualifies only to the extent further R&D created a new intangible (art. 12ba(5)). Under the ordinary method with T greater than zero, apply min(1, K/T) to the qualifying-asset benefits after the box threshold, where K is 1.3 times statutory qualifying R&D costs in the current and all prior years and T is statutory total R&D costs over those years. Establish the cost definitions, any qualifying cooperation route and specific zero-cost/transitional treatment before using the formula (art. 12bb). Related-party outsourcing can restrict the amount; a referral alone does not establish the qualifying benefit. The company has one innovation box for all its qualifying intangibles; it elects in the return for the first year it wants to apply the box, while that year's assessment is not final, and cannot elect for an asset still in development ([Belastingdienst, choosing the innovation box](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/innovatiebox/kiezen-voor-innovatiebox)). If a patent or breeder’s right application is refused, apply art. 12be(1)’s cessation/recapture rule only after checking art. 12be(3): another independently qualifying route, such as software, can preserve eligibility. Refusal alone does not always end the box treatment. A company that created a qualifying asset in the year or the 2 prior years may instead take a fixed 25% of profit before the box, at most EUR 25,000, if that profit is positive (art. 12bd(1)); in that case the box threshold reduction is nil (art. 12bd(3)). If all qualifying assets produced in the year or the two preceding years belong to qualifying partnerships with other taxpayers, the percentage is the sum of 25 times the company’s benefit share in each partnership, capped at 25% (art. 12bd(2)); the EUR 25,000 maximum remains. For joint development: Check this point with one of our partner accountants. Innovation losses are deductible at the normal rate.

**Losses (art. 20 and 20a).** A loss is carried back to the previous year first, then forward without time limit. In each year the offset is capped at EUR 1,000,000 plus 50% of the taxable profit above EUR 1,000,000; a taxable profit of EUR 1,000,000 or less can be fully offset. Losses are used in the order they arose, and only once the inspector has fixed them in a decision open to objection. If the ultimate interest in the company changes by 30% or more, earlier losses can no longer be carried forward, unless the asset test (assets not predominantly investments for at least 9 months of the loss year) and the statutory activities and intention tests are met. Those tests require the 30% activity floor against the prescribed comparison year and the absence of an intention to fall below it within three years; establish the oldest-loss/alternative-year rule and the actual asset/activity definitions rather than inferring eligibility from continuing some business. Under art. 20a(6), the later profit year must also satisfy the 9-month asset test. If only the asset test is met, the continued-activity relief requires a request and attribution to the qualifying pre-change activities; it is not automatic general loss carry-forward. A loss made after a 30% change is generally barred from carry-back to profit from before the change. Subject to the statutory exceptions, art. 20a(9) preserves carry-back only if the activities have neither ceased nor almost entirely ceased, and the assets were not predominantly investments for at least 9 months in each of the loss year and the profit year. Both conditions must hold. In the year of the change the result is computed separately for the period before and after it: ordinarily a loss before the change goes to the previous year and a loss after it to the next year. Where the statutory first/last-year circumstances prevent that allocation, the negative amount is not recognised under the corresponding rule; do not assume it is always usable. Exceptions: inheritance or matrimonial property, an acquirer who already held at least one third at the start of the oldest loss year and extends it (art. 20a(2)), and a company that did not and could not know of the change, provided the change is no greater than usual trading under art. 20a(3) ([Belastingdienst, change of ownership](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/verrekenen_van_verliezen/belangenwijziging)).

**Old holding and finance company losses (art. 34i).** Pre-2019 holding/finance losses can remain subject to the incorporated historical restrictions. Check this point with one of our partner accountants.

**Loss overview and provisional carry-back.** A total overview of offset and open losses is issued within 6 weeks of a written request to the tax office. A provisional carry-back (voorlopige verliesverrekening) is asked for in writing when the loss-year return is filed; the assessment of the earlier year must be final, and at most 80% of the declared loss is offset ([Belastingdienst, offsetting losses](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/verrekenen_van_verliezen)).

**Order of the computation.** Commercial result, add-backs (including the partly deductible costs and any depreciation above the caps or below the building floor value), participation exemption, earnings stripping, innovation box, then loss offset, then the rate table on the taxable amount. This is an ordinary-case outline: establish fiscal-unity, foreign-exemption and capitalized-interest interactions before using it as a complete computation.

## Deadlines and filing

- **Return.** Calendar year: before 1 June of the next year (the 2026 return is due before 1 June 2027; the 2025 return was due before 1 June 2026). Broken year: within 5 months after the end of the financial year. Short year ending 31 December: by 1 June of the next year; short year ending in another month: before 1 April of the next calendar year.
- **How.** Through Mijn Belastingdienst Zakelijk, tax software or a tax service provider.
- **Extension.** Online in Mijn Belastingdienst Zakelijk to 1 November, for a calendar year only; apply before 1 June (the form is open from 1 March to 1 June). For a longer extension or a broken year, use the paper form with reasons, within 5 months after the end of the financial year. A tax service provider can also request it.
- **Provisional assessments (voorlopige aanslag).** Most companies get one at the start of the year, based on earlier years. The company must check it and ask for a change if it expects a higher or lower profit; changes can be passed on until the return is filed, and the Belastingdienst processes at most 3 increases for one year. There is no objection against a provisional assessment, only a request to change it. If none arrives and tax is expected, ask for one. The final assessment credits all provisional assessments.
- **Paying a provisional assessment.** One received in the year it covers is paid in equal monthly instalments, in full by 31 December; if fewer than 2 whole months remain after its date, the term is 6 weeks ([Belastingdienst, paying in instalments](https://www.belastingdienst.nl/wps/wcm/connect/nl/betalenenontvangen/content/in-termijnen-betalen)).
- **Asking for a return.** A company that receives no return invitation must ask for one within 6 months after the tax debt arose.
- **Loss and interest decisions.** Losses and carried-forward interest are fixed in decisions open to objection. See [nl-tax-objection](nl-tax-objection.md).

## Penalties and interest

- **Tax interest (belastingrente).** Charged if the return is received on or after 1 June after the tax year, or if the assessment departs from the return (even one filed before 1 June). It runs from 1 July after the tax year. If the return is followed unchanged, it runs at most to 19 weeks after the return is received, or to 6 weeks after the assessment date if earlier. No tax interest if the return is filed before 1 June and followed unchanged, or if a provisional assessment is requested before 1 May and imposed as asked. For a broken year, read the 5th month after year end for 1 May and the 6th month for 1 June. Interest is computed with 30-day months and a 360-day year, rounded down to whole euros.
- **Rate.** Tax interest is 5% from 1 January 2026 and 6.5% for 2025; apply the rate for each relevant period.
- **Late or missing return.** Filed after the deadline in the demand (aanmaning), or not at all: EUR 3,354, rising to EUR 6,709 for several years in a row. No penalty if the company is not at all to blame.
- **Not asking for a return in time:** EUR 3,354 (none if asked within 2 weeks after the 6-month term).
- **Late payment.** 5% of the unpaid amount of the (provisional) assessment, minimum EUR 50, maximum EUR 6,709 each time.
- **Incorrect return.** 25% for gross negligence, 50% for intent, up to 100% for fraud or a repeat offence, applied to the statutory penalty base: tax that would otherwise escape assessment as a result of the taxpayer's intent or gross negligence, calculated before loss offsets where required. Initial-assessment art. 67d requires intent; additional-assessment art. 67e also covers gross negligence ([AWR arts. 67d(1)-(2) and 67e(1)-(2)](https://wetten.overheid.nl/BWBR0002320/2026-10-01#HoofdstukVIIIA_Afdeling1_Paragraaf2_Artikel67d)). The statute describes tax that "niet zou zijn geheven". Automatic voluntary-correction relief requires correction within two years and before discovery is known or reasonably suspected (AWR art. 67n). A later qualifying correction ordinarily mitigates rather than automatically removes the penalty.

## Cross-border points

- **Dividends paid.** A bv or nv paying a dividend usually withholds 15% dividend tax, with exemptions for qualifying shareholders. For conditional withholding on affiliate payments: Check this point with one of our partner accountants. See [nl-dividend-withholding](nl-dividend-withholding.md).
- **Foreign branches.** Under the ordinary object exemption (art. 15e), qualifying foreign-PE results are excluded; establish the low-tax-investment, disregarded-PE and tainted-income exceptions. Negative foreign results are not an ordinary current deduction; a final cessation loss must satisfy the full art. 15i conditions. See [nl-double-tax-relief](nl-double-tax-relief.md).
- **Transfer pricing.** Related-party prices must be at arm's length (art. 8b). See [netherlands-transfer-pricing](netherlands-transfer-pricing.md).
- **Foreign subsidiaries.** Apply the participation rules above, including the deductible-payment exclusion. For investment participations and foreign liquidation losses: Check this point with one of our partner accountants.
- **Minimum tax (Pillar Two).** Scope, excluded entities, adjusted jurisdictional calculations, information returns, notification, tax returns and payment have separate rules and transition conditions under the [Wet minimumbelasting 2024](https://wetten.overheid.nl/BWBR0049111/2026-04-11). Check this point with one of our partner accountants.
- **Residence and migration.** Moving a company's place of management in or out of the Netherlands is in [nl-cross-border](nl-cross-border.md).

## Worked examples

Example 1 assumes the participation otherwise qualifies for the exemption and the subsidiary cannot deduct the dividend under art. 13(17). Example 2 assumes the booked interest is expensed, no exempt foreign-business interest is included, and the loss/interest amounts are eligible without ownership-change or pre-joining fiscal-unity restrictions. Apply the conditions above before using either result for a real company.

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
| Wet Vpb arts. 13(17) and 15(10): deductible participation payments, replacement receipts and fiscal-unity termination; complete operative clauses read. | https://wetten.overheid.nl/BWBR0002672/2026-01-01 | 2026-11-26 |
| Wet Vpb 1969, arts. 12ba(2)(b), 20a(4), 20a(6) and 20a(9). Read these operative provisions for the strict turnover boundary, nine-month asset tests and cumulative carry-back exception; the conflicting authority summaries do not override the statute. | https://wetten.overheid.nl/BWBR0002672/2026-01-01 | 2026-11-23 |
| Algemene wet inzake rijksbelastingen, arts. 67d(2) and 67e(2). Read for the assessed-tax penalty base, including the loss-offset adjustment. | https://wetten.overheid.nl/BWBR0002320/2026-10-01 | 2026-11-23 |
| Wet op de vennootschapsbelasting 1969, bounded operative provisions: arts. 2, 8, 10, 12b–12be, 13, 13d, 15, 15b, 15i, 20, 20a and 22; reused completed reads | https://wetten.overheid.nl/BWBR0002672/2026-01-01 | 2026-11-23 |
| Wet inkomstenbelasting 2001, arts. 3.14 (fines not deductible), 3.15 (partly deductible costs), 3.30 and 3.30a (depreciation caps, building floor value), version in force from 1 January 2026 | https://wetten.overheid.nl/BWBR0011353/2026-01-01 | 2026-11-23 |
| Belastingdienst, threshold for partly deductible costs 2026 (EUR 5,700; 73.5% for Vpb). Read for the threshold for partly deductible costs. | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/veranderingen-inkomstenbelasting-2026/drempel-beperkt-aftrekbare-kosten-2026 | 2026-11-23 |
| Belastingdienst, depreciation for Vpb (buildings stop at WOZ value). Read for the depreciation limit on buildings. | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/afschrijving-vennootschapsbelasting | 2026-11-23 |
| Belastingdienst, salary and substantial interest (gebruikelijk loon EUR 58,000 in 2026). Read for the customary salary amount. | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/prive/vermogen_en_aanmerkelijk_belang/aanmerkelijk_belang/loon_en_aanmerkelijk_belang/loon_en_aanmerkelijk_belang | 2026-11-23 |
| Belastingdienst, credit for investment participations (deelnemingsverrekening). Read for the credit for investment participations. | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/deelnemingsvrijstelling/deelnemingsverrekening | 2026-11-23 |
| Belastingdienst, Vpb rates. Read for the 2026 Vpb rates and bracket. | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/tarieven_vennootschapsbelasting | 2026-11-23 |
| Belastingdienst, changes to Vpb 2026. Read for what changed in Vpb for 2026. | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/veranderingen-vennootschapsbelasting-2026 | 2026-11-23 |
| Belastingdienst, earnings stripping. Read for the earnings stripping limit. | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/generieke-renteaftrekbeperking | 2026-11-23 |
| Belastingdienst, offsetting losses. Read for loss offset rules. | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/verrekenen_van_verliezen | 2026-11-23 |
| Belastingdienst, change of ownership. Read for the change of ownership rule. | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/verrekenen_van_verliezen/belangenwijziging | 2026-11-23 |
| Belastingdienst, participations. Read for the participation exemption. | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/deelnemingsvrijstelling/deelnemingen | 2026-11-23 |
| Belastingdienst, qualifying investment participation. Read for the qualifying investment participation test. | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/deelnemingsvrijstelling/kwalificerende_beleggingsdeelneming | 2026-11-23 |
| Belastingdienst, fiscal unity. Read for the fiscal unity conditions. | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/fiscale_eenheid_vennootschapsbelasting | 2026-11-23 |
| Belastingdienst, innovation box | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/innovatiebox | 2026-11-23 |
| Belastingdienst, innovation box smaller and larger taxpayers | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/innovatiebox/kleinere-en-grotere-belastingplichtigen | 2026-11-23 |
| Belastingdienst, filing the Vpb return. Read for how and when to file. | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/aangifte-vennootschapsbelasting-doen | 2026-11-23 |
| Belastingdienst, extension for the Vpb return. Read for extension of the filing date. | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/uitstel_aangifte_vennootschapsbelasting | 2026-11-23 |
| Belastingdienst, provisional assessment. Read for the provisional assessment. | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/voorlopige_aanslag_vennootschapsbelasting | 2026-11-23 |
| Belastingdienst, tax interest on Vpb. Read for how tax interest runs on Vpb. | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/standaard_functies/prive/contact/rechten_en_plichten_bij_de_belastingdienst/belastingrente/belastingrente_betalen_bij_vennootschapsbelasting | 2026-11-23 |
| Belastingdienst, tax interest rates. Read for the tax interest rates. | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/standaard_functies/prive/contact/rechten_en_plichten_bij_de_belastingdienst/belastingrente/overzicht_percentages_belastingrente | 2026-11-23 |
| Belastingdienst, penalties. Read for the penalty rules. | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/standaard_functies/prive/contact/rechten_en_plichten_bij_de_belastingdienst/boete | 2026-11-23 |
| Belastingdienst, paying a dividend (15% dividend tax). Read for the dividend tax rate and return. | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/dividendbelasting/als_u_dividend_uitkeert | 2026-11-23 |
| Belastingdienst, minimum tax. Read for the Pillar Two minimum tax. | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/minimumbelasting | 2026-11-23 |

Source dates above refer to completed bounded reads reused from 23 November 2026. Articles 13(17) and 15(10) were read again on 26 November 2026. Unchanged research is reused; no whole-Act read is claimed.

Not yet confirmed: none retained as usable guidance. Historical source-date assertions and unsupported future-period assertions were removed; specialist cases are referred above.
