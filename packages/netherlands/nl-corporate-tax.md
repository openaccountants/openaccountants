---
name: nl-corporate-tax
description: Use this skill whenever asked about Dutch corporate income tax (vennootschapsbelasting / VPB) for BV entities. Trigger on phrases like "vennootschapsbelasting", "VPB aangifte", "corporate tax Netherlands", "BV belasting", "fiscal unity", "fiscale eenheid", "innovatiebox", "verliesverrekening", "carry forward losses", "DGA salary", "gebruikelijk loon", "deelnemingsvrijstelling", "participation exemption", "fiscal profit bridge", "commercial to fiscal result", "liquidatieverliesregeling", or any question about computing or filing corporate income tax for a Dutch BV or NV. Also trigger when preparing annual accounts-to-tax reconciliation, computing VPB liability, or advising on fiscal adjustments. This skill covers VPB rates, fiscal profit computation, loss relief, fiscal unity, the innovation box, participation exemption, DGA salary rules, filing deadlines, and penalties. ALWAYS read this skill before touching any Dutch corporate tax work.
version: 1.0
jurisdiction: NL
tax_year: 2026
last_updated: 2026-09-25
authored_by: OpenAccountants team
review_status: pending_review
trust_label: By OpenAccountants
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Netherlands corporate income tax (vennootschapsbelasting, Vpb)

## Scope and who this is for ([Belastingdienst: tax liability and return](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/belastingplicht_en_aangifte))

This Guide covers Dutch corporate income tax (vennootschapsbelasting, "Vpb") for a Dutch-resident **bv** (private limited company) or **nv** (public limited company). The primary year is **tax year 2026** (financial years that are the calendar year 2026). There is a dated section for the **2025 returns** being filed now.

- A bv and an nv must always file a Vpb return. Foundations (stichtingen), associations (verenigingen) and similar bodies file only in certain situations, and those are outside this Guide.
- A body set up under Dutch law is treated as established in the Netherlands. Otherwise residence depends on where management sits, where the head office is and where shareholder meetings are held.
- From 1 January 2025 the rules changed for the tax liability of limited partnerships (cv), mutual funds (fgr), fiscal investment institutions (fbi), exempt investment institutions (vbi) and foreign legal forms. These are outside this Guide.

Tax is charged on the **taxable amount** (belastbaar bedrag) of a financial year: the profit minus losses that can still be offset ([Belastingdienst: taxable amount and financial year](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/belastbaar_bedrag)). The financial year is usually the calendar year, but a broken year (for example May to April) is allowed. It must match the financial year in the articles of association. The first and last years may be longer or shorter. Changing the financial year only to get a one-off tax advantage is not allowed.

Practical rules come from the Belastingdienst's Dutch pages. Statute points cite the Wet op de vennootschapsbelasting 1969 ("Wet Vpb 1969") as in force from 1 January 2026 ([wetten.overheid.nl](https://wetten.overheid.nl/BWBR0002672/2026-01-01)).

This Guide does not cover banks and insurers (special interest rules), fiscal investment institutions, cross-border groups beyond the summary of the minimum tax, transfer pricing, mergers and demergers, or the liquidation loss rule. See "When to refuse or refer".

## Ask the client first

- Legal form (bv or nv) and whether it is Dutch-resident. Any foreign shareholders, subsidiaries or permanent establishments?
- The financial year: calendar year or broken year, and is this the first or a shortened year?
- Which year is being worked on: the 2025 return (filing now) or 2026 (provisional assessment and planning)?
- Annual accounts (jaarrekening), trial balance and fixed asset register.
- Prior-year assessments, the loss decisions (verliesbeschikkingen) and how much of each loss is left, and whether any **30% or more** change in ultimate ownership has happened since the oldest loss year ([change of ownership](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/verrekenen_van_verliezen/belangenwijziging)).
- Every shareholding the company holds: percentage of nominal paid-up capital, voting rights, how long held, and what the subsidiary does (active business or mainly investments or group financing).
- Is there a fiscal unity decision (beschikking) from the Belastingdienst? Which companies, from which date?
- Interest paid and received (including to and from group companies), depreciation and write-downs for the year.
- Innovation: any S&O-verklaring (R&D declaration issued by RVO), patents or software developed in-house?
- Representation, food, drink and gift costs for the year.
- Director-major shareholder (dga) salary actually paid.
- Provisional assessments (voorlopige aanslagen) received and paid for the year, and any extension already granted.
- Group consolidated revenue, if the company belongs to a group (for the minimum tax test).

## The method, step by step

1. **Confirm liability and the year.** A bv or nv files every year. Fix the financial year and the return deadline before anything else (see "Filing and payment"). If the company is in a fiscal unity, only the parent files; work at the parent level.
2. **Start from the commercial result, then apply tax rules.** Fiscal profit is computed by applying tax rules to the commercial profit and loss account and balance sheet, using sound business practice (goed koopmansgebruik). Tax values may differ from the accounts ([taxable amount](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/belastbaar_bedrag)). Most income tax profit rules also apply here: deduction of business costs, investment deductions, some tax reserves and work-in-progress valuation. The self-employed deduction (zelfstandigenaftrek) and the partner's work deduction (meewerkaftrek) do **not** apply to a company.
3. **Limit partly deductible costs.** Representation costs and some business gifts are partly deductible. Use either the threshold or the percentage method, not both (see "Figures by year").
   **Not deductible at all:** profit distributions, whatever they are called or however they are made (article 10(1)(a) Wet Vpb 1969); the Vpb itself, the minimum tax and foreign profit taxes relieved under a double tax arrangement (article 10(1)(e)) ([Wet Vpb 1969](https://wetten.overheid.nl/BWBR0002672/2026-01-01)); and fines and bribes. Article 8(1) Wet Vpb 1969 applies article 3.14(1) Wet IB 2001, which bars costs connected with criminal and administrative fines (including sums paid to avoid prosecution) and with gifts, promises or services that are a criminal offence such as bribery ([Wet IB 2001](https://wetten.overheid.nl/BWBR0011353/2026-01-01) lists the other barred items). Add these back to the commercial result in full.
4. **Apply tax depreciation.** Buildings stop at the WOZ value. Goodwill is limited to 10% a year and other assets to 20% a year of cost ([depreciation](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/afschrijving/hoe_berekent_u_het_bedrag_van_de_afschrijving)).
5. **Take out participation income.** Dividends and gains from a qualifying participation are exempt. Losses on it are not deductible, and costs of buying or selling it are not deductible either. Test first whether the holding is a participation, then whether it is an investment participation, then whether it qualifies (see "Boundary and exception table").
6. **Apply the earnings stripping limit.** Net interest (interest costs minus interest income on loans, at least nil) is not deductible to the extent it exceeds the **higher** of 24.5% of the adjusted profit and €1,000,000 (2025 and 2026). The excess carries forward ([earnings stripping](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/generieke-renteaftrekbeperking)).
7. **Apply the innovation box if elected.** Qualifying benefits above the box threshold count for only 9/25.8 of their amount, which gives an effective 9% at the top rate ([innovation box](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/innovatiebox)). The election is made in the return.
8. **Offset losses.** Carry a loss back one year first, then forward without a time limit. Each year's offset is capped: €1,000,000 plus 50% of that year's taxable profit above €1,000,000. Check the ownership-change and holding-loss restrictions first ([loss offset](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/verrekenen_van_verliezen)).
9. **Compute tax.** 19% on the first €200,000 of the taxable amount and 25.8% on the rest (2023 to 2026) ([rates](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/tarieven_vennootschapsbelasting)).
10. **Credit provisional assessments** and any withholding taxes, then compare with the final assessment when it arrives. Check for tax interest (belastingrente).
11. **File by the deadline or get an extension in time.** Otherwise a late-filing penalty follows.

If you do these steps in a different order, you get the wrong answer. Losses are offset against the taxable profit **after** the participation exemption and the interest limit. The €200,000 bracket applies to the taxable amount **after** loss offset ([rates](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/tarieven_vennootschapsbelasting)).

## Figures by year

### Vpb rates, 2023 to 2026 ([Belastingdienst: Vpb rates](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/tarieven_vennootschapsbelasting))

| Part of the taxable amount | Rate 2026 | Rate 2025 | Rate 2024 | Rate 2023 |
| --- | --- | --- | --- | --- |
| Up to and including €200,000 | 19.0% | 19.0% | 19.0% | 19.0% |
| Above €200,000 | 25.8% | 25.8% | 25.8% | 25.8% |

The 2026 changes page confirms "Het vennootschapsbelastingtarief is in 2026 niet gewijzigd" ([Changes to Vpb 2026](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/veranderingen-vennootschapsbelasting-2026)). Article 22 Wet Vpb 1969 sets the same table: tax on the first €200,000 is €38,000, and 25.8% applies to the part above ([wetten.overheid.nl](https://wetten.overheid.nl/BWBR0002672/2026-01-01)).

### Earnings stripping (generieke renteaftrekbeperking) ([Belastingdienst: earnings stripping](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/generieke-renteaftrekbeperking))

| Year | Net interest not deductible to the extent it exceeds |
| --- | --- |
| 2026 | 24.5% of the adjusted profit **and** €1,000,000 |
| 2025 | 24.5% of the adjusted profit **and** €1,000,000 |
| 2023 and 2024 | 20% of the profit **and** €1,000,000 |

- Article 15b(1) Wet Vpb 1969 puts it as "het hoogste van de volgende bedragen: a. 24,5% van de gecorrigeerde winst; b. € 1.000.000" ([wetten.overheid.nl](https://wetten.overheid.nl/BWBR0002672/2026-01-01)).
- **Net interest** (saldo aan renten) is interest costs on loans minus interest income on loans. It is at least nil.
- **Adjusted profit** (gecorrigeerde winst, article 15b(3)) is the profit before this limit, plus depreciation of the year, plus write-downs to lower business value (minus reversals of write-downs), plus the net interest of the year. It is at least nil. This is broadly tax EBITDA.
- Interest not deductible in one year carries forward. It is deducted in a later year to the extent that year's net interest is below the limit, oldest first. The inspector sets the amount carried forward in a decision open to objection (article 15b(5)).
- Within a fiscal unity the limit is computed for the unity as a whole. When profit must be split per company to offset losses from before a company joined (articles 15ae and 15ah), each company's profit is first computed on its own, with a standalone earnings stripping calculation, and any difference from the unity's profit is then allocated between the companies ([KG:032:2025:3](https://kennisgroepen.belastingdienst.nl/publicaties/kg03220253-winstsplitsing-bij-fiscale-eenheid-samenloop-artikel-15b-en-artikel-15ah-wet-vpb-1969/)).
- Banks and insurers have an extra rule: in 2025 and 2026 interest is not deductible to the extent debt exceeds 89.4% of the balance sheet total ([2026 changes](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/veranderingen-vennootschapsbelasting-2026); [2025 changes](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/veranderingen-vennootschapsbelasting-vorige-jaren/veranderingen-vennootschapsbelasting-2025)). Refer these.

### Loss offset (verliesverrekening) ([Belastingdienst: offsetting losses](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/verrekenen_van_verliezen))

| Rule | What the Belastingdienst says |
| --- | --- |
| Carry-back | Against the taxable profit of the **previous** financial year, first |
| Carry-forward | Losses from 2022 and later: no time limit. Also losses from financial years starting on or after 1 January 2013 that could still be carried forward at the end of 2021 |
| Yearly cap (offset against profits of 2022 onward) | Taxable profit €1,000,000 or less: offset up to the full profit. Above €1,000,000: €1,000,000 plus 50% of the remaining profit |
| Provisional loss carry-back | On written request when filing the loss-year return, if the assessment for the earlier year is final; at most 80% of the loss declared |
| Loss overview | Ask the tax office in writing; issued within 6 weeks |

- Article 20(2) Wet Vpb 1969 applies the cap to both the previous year and later years, and allows offset only once the inspector has set the loss in a decision open to objection ([wetten.overheid.nl](https://wetten.overheid.nl/BWBR0002672/2026-01-01)). Losses are offset in the order they arose.
- **Change of ownership (belangenwijziging)** ([Belastingdienst](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/verrekenen_van_verliezen/belangenwijziging)): losses can no longer be carried forward if the ultimate interest in the company changes by **30% or more**. They can still be used if, in the loss year and the profit year, assets were not for more than 3 months more than 50% investments, **and** activities just before the change were not less than 30% of those at the start of the oldest loss year, **and** there was no intention to shrink activities below 30% within 3 years. If only the asset test is met (the activities test or intention test fails), the losses can still be offset, but only against profits from the activities continued after the change. Carry-back to profit from before the change is blocked when a loss arises after the change and both apply: activities have stopped by 90% or more, and assets were for more than 3 months more than 50% investments in the profit and loss years. In the year of the change the result is computed separately for 2 periods, before and after the change; a loss before the change is attributed to the previous year and a loss after it to the next year. Exceptions: inheritance or matrimonial property law; an acquirer who already held at least 33 1/3% at the start of the oldest loss year; a company that did not and could not know of the change.
- **Holding and finance company losses** ([Belastingdienst](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/verrekenen_van_verliezen/houdsterverliezen)) can only be offset against profits of years in which the company was also a holding or finance company, with a test on the balance of receivables and debts with related entities.
- From 2025, a debt-forgiveness profit (kwijtscheldingswinst) is first offset against the loss of that year and past losses; any remainder is fully exempt ([2025 changes](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/veranderingen-vennootschapsbelasting-vorige-jaren/veranderingen-vennootschapsbelasting-2025)).

### Participation exemption (deelnemingsvrijstelling) ([Belastingdienst: participations](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/deelnemingsvrijstelling/deelnemingen))

| Condition | Rule |
| --- | --- |
| Basic holding | At least 5% of the nominal paid-up capital of a company with share capital (such as a bv or nv) |
| Other routes | At least 5% of units in a mutual fund (fgr); member of a cooperative; at least 5% as limited partner in an open cv; at least 5% of voting rights in an EU company where a tax treaty reduces dividend tax by voting rights; deemed participation (meesleepregeling); related-party pull-along (meetrekregeling) |
| Below 5% | No participation. One exception: a holding of at least 5% held for more than 1 year, and exempt without a break ("onafgebroken") throughout that time, that falls below 5% keeps the exemption for 3 more years (article 13(16) Wet Vpb 1969) |
| Non-qualifying investment participation | No exemption; a credit (deelnemingsverrekening) may apply instead ([credit method](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/deelnemingsvrijstelling/deelnemingsverrekening)): gross up the income by 100/95 and credit the lower of 5% of the grossed-up income and the Vpb attributable to it |

- **Effect** ([Belastingdienst](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/deelnemingsvrijstelling)): dividends and gains on sale are not taxed; losses on sale are not deductible; costs of buying and selling the participation are not deductible. The exemption does not apply to a fiscal investment institution's return.
- **Qualifying investment participation** ([Belastingdienst](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/deelnemingsvrijstelling/kwalificerende_beleggingsdeelneming)): the exemption still applies if **either** the subsidiary is subject to a profit tax that is realistic by Dutch standards (subject-to-tax test; "Een tarief van 10% geldt normaal gesproken als reële heffing", with the base compared to Dutch rules) **or** its assets usually consist, directly or indirectly, of less than half low-taxed free portfolio investments (asset test).

### Fiscal unity (fiscale eenheid) ([Belastingdienst: fiscal unity](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/fiscale_eenheid_vennootschapsbelasting))

| Condition | Rule |
| --- | --- |
| Parent's holding | At least 95% of the shares, entitled to at least 95% of the profit **and** at least 95% of the capital, and at least 95% of the voting rights |
| Parent's form | bv, nv, mutual insurer, cooperative, or a foundation or association acting as housing corporation, or a comparable foreign form |
| Subsidiary's form | bv or nv, or a comparable foreign form |
| Both | Same financial years and same profit rules; actually established in the Netherlands |
| Start date | Only on request, from the date named in the request, but "niet eerder dan drie maanden voor het tijdstip waarop het verzoek is gedaan" (article 15(9) Wet Vpb 1969, [wetten.overheid.nl](https://wetten.overheid.nl/BWBR0002672/2026-01-01)) |
| End | Among other cases, when the conditions are no longer met (article 15(10)) |

- Effect: the subsidiary's results are attributed to the parent. The subsidiary still exists but no longer files. Losses of one member can be set against profits of another.
- EU exceptions: a Dutch parent with a Dutch granddaughter held through an intermediate company in another EU state; or Dutch sisters held by the same top company in another EU state (one sister is treated as the parent). The EU company itself is not in the unity.
- A Vpb fiscal unity is **not** the same as a VAT fiscal unity.

### Innovation box (innovatiebox) ([Belastingdienst: innovation box](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/innovatiebox))

| Point | Rule |
| --- | --- |
| Effective rate | 9% on qualifying profits from innovative activities with an S&O-verklaring issued by RVO |
| How it works | Qualifying benefits count for 9/H of their amount, where H is the top rate for the year (25.8% in 2025 and 2026), and only while the balance of qualifying benefits is positive (article 12b Wet Vpb 1969, [wetten.overheid.nl](https://wetten.overheid.nl/BWBR0002672/2026-01-01)) |
| Self-developed | The company must have developed the intangible itself, at its own account and risk. A bought intangible does not qualify; only a new asset created by further development does ([conditions](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/innovatiebox/voorwaarden-aan-immateriele-activa)) |
| Smaller taxpayer | Gross benefit from all intangibles over the year plus the 4 previous years less than €37.5 million, **and** net turnover over the same 5 years at most €250 million (group turnover if in a group) ([smaller and larger taxpayers](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/innovatiebox/kleinere-en-grotere-belastingplichtigen)) |
| Smaller taxpayer needs | An S&O-verklaring |
| Larger taxpayer needs | An S&O-verklaring **and** one of: patent (or application), plant breeder's right (or application), new biological crop protection, software, a medicines marketing authorisation, a registered utility model, or a supplementary protection certificate |
| Box threshold | Benefits enter the box only above the production costs deducted (balance still to recover plus costs of the year, plus unrecovered innovation losses) ([threshold](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/innovatiebox/boxdrempel)) |
| Fixed-percentage option | 25% of the profit before the box, at most €25,000, in the year the asset is created and the 2 following years. Only available when that profit is positive (article 12ba(1)) ([fixed percentage](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/innovatiebox/kiezen-voor-een-vast-bedrag)) |
| Election | Made in the return for the first year of use, while that year's assessment is not yet final. One box per company. Not for an asset still in development ([choosing](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/innovatiebox/kiezen-voor-innovatiebox)) |
| Losses | Innovation losses are deductible at the normal rate |

If a patent or breeder's right application is later refused, the normal rate applies after all.

### Partly deductible costs (representation, food, drink, some gifts) ([Threshold 2026](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/veranderingen-inkomstenbelasting-2026/drempel-beperkt-aftrekbare-kosten-2026))

| Year | Threshold method | Percentage method for Vpb | Source |
| --- | --- | --- | --- |
| 2026 | Deductible only above €5,700 | 73.5% deductible | [Threshold 2026](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/veranderingen-inkomstenbelasting-2026/drempel-beperkt-aftrekbare-kosten-2026) |
| 2025 | Deductible only above €5,700 | 73.5% deductible | [Threshold 2025](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/verandering_inkomstenbelasting_vorige_jaren/veranderingen-inkomstenbelasting-2025/drempel-beperkt-aftrekbare-kosten-2025) |

The percentage is the part that **is** deductible. The Belastingdienst says entrepreneurs may deduct a percentage of these costs instead of applying the threshold, "Voor ondernemers voor de vennootschapsbelasting geldt het percentage van 73,5%."

### Depreciation ([Belastingdienst: Vpb depreciation](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/afschrijving-vennootschapsbelasting))

| Asset | Rule |
| --- | --- |
| Buildings | No more depreciation for Vpb once the WOZ value is reached (the floor value, bodemwaarde). Use the WOZ value as at 1 January of the previous year ([business premises](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/afschrijving/afschrijving_bedrijfspand)). No depreciation on land |
| Goodwill | At most 10% a year ([how to compute depreciation](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/inkomstenbelasting_voor_ondernemers/afschrijving/hoe_berekent_u_het_bedrag_van_de_afschrijving)) |
| Other assets | At most 20% a year of cost |
| Accelerated (willekeurige) depreciation | Only for designated assets, such as environmental assets; book value may not fall below residual value |

### Director-major shareholder salary (gebruikelijk loon) ([Belastingdienst: salary and substantial interest](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/prive/vermogen_en_aanmerkelijk_belang/aanmerkelijk_belang/loon_en_aanmerkelijk_belang/loon_en_aanmerkelijk_belang))

| Year | Minimum amount in the test |
| --- | --- |
| 2026 | €58,000 |
| 2025 and 2024 | €56,000 |

The salary must be at least the **highest** of: pay in the most comparable employment; pay of the highest-paid employee of the company or of a related company; and the amount in the table. A lower figure is accepted only if the shareholder shows that comparable work is usually paid less. If the usual salary is €5,000 or lower (in total across all the person's companies) and that can be shown, the actual pay is used. This is a wage tax rule, but the salary is a cost in the company's Vpb profit.

### Tax interest (belastingrente) on Vpb ([Belastingdienst: tax interest rates](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/standaard_functies/prive/contact/rechten_en_plichten_bij_de_belastingdienst/belastingrente/overzicht_percentages_belastingrente))

| Period | Vpb rate as now published |
| --- | --- |
| From 1 January 2026 | 5% (was 7.5%) |
| 2025 | 6.5% (was 9%) |
| 2024 | 7.5% (was 10%) |

On 16 January 2026 the Supreme Court (Hoge Raad) ruled that the higher Vpb rate may not be used; the same rate as for other taxes applies, and the Belastingdienst corrected the rates from 2022. For corrections of past assessments, check the Belastingdienst's current news on the mass objection.

## Boundary and exception table

| Situation | Treatment | Source |
| --- | --- | --- |
| Taxable amount exactly €200,000 | All at 19% ("tot en met") | [Rates](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/tarieven_vennootschapsbelasting) |
| Taxable profit exactly €1,000,000 | Losses can be offset up to the full profit ("€ 1.000.000 of lager") | [Loss offset](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/verrekenen_van_verliezen) |
| Net interest exactly €1,000,000 | Not limited: interest is disallowed only to the extent it is **more than** the limit | [Earnings stripping](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/generieke-renteaftrekbeperking) |
| Holding of exactly 5% | A participation ("ten minste 5%") | [Participations](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/deelnemingsvrijstelling/deelnemingen) |
| Holding fell from at least 5% to below 5% after more than 1 year | Exemption continues for 3 years, but only if the holding was exempt without a break during the time it was held (article 13(16)) | [Participations](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/deelnemingsvrijstelling/deelnemingen) |
| Subsidiary mainly holds interests below 5%, or mainly does group financing | Always an investment participation, whatever the intention | [Investment participation](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/deelnemingsvrijstelling/wanneer_is_een_deelneming_een_beleggingsdeelneming) |
| Subsidiary's business is an extension of the parent's, or top holding with a real group function | Not an investment participation | [Investment participation](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/deelnemingsvrijstelling/wanneer_is_een_deelneming_een_beleggingsdeelneming) |
| Ownership change of exactly 30% | Counts ("30% of meer"): loss carry-forward restricted unless the tests are met | [Change of ownership](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/verrekenen_van_verliezen/belangenwijziging) |
| Parent holds 94% | No fiscal unity (needs at least 95%) | [Fiscal unity](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/fiscale_eenheid_vennootschapsbelasting) |
| Innovation box, bought patent not developed further | Not eligible | [Conditions](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/innovatiebox/voorwaarden-aan-immateriele-activa) |
| Provisional assessment disagreed with | No objection possible; ask for a change instead | [Provisional assessment](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/voorlopige_aanslag_vennootschapsbelasting) |

## Worked cases

These cases use rounded inputs chosen for illustration. Each result follows from the rules above.

### Case 1: tax on a taxable amount of €500,000 (2026) ([Rates](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/tarieven_vennootschapsbelasting))

- First €200,000 at 19%: €38,000.
- Remaining €300,000 at 25.8%: €77,400.
- Vpb due: €115,400, before crediting provisional assessments.

### Case 2: capped loss offset (the Belastingdienst's own example) ([Loss offset](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/verrekenen_van_verliezen))

- Profit 2026 €9,000,000; loss 2025 €7,000,000 (nothing left to carry back).
- Offset allowed: €1,000,000 plus 50% of €8,000,000 (€4,000,000) = €5,000,000.
- Taxable amount 2026: €4,000,000. Loss left for 2027 and later: €2,000,000.

### Case 3: earnings stripping (2026) ([Earnings stripping](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/generieke-renteaftrekbeperking))

- Company A: adjusted profit €10,000,000; net interest €3,000,000. 24.5% of the adjusted profit is €2,450,000, which is higher than €1,000,000. Deductible €2,450,000; not deductible €550,000, carried forward.
- Company B: adjusted profit €2,000,000; net interest €800,000. 24.5% is €490,000, but the limit is the higher amount, €1,000,000, and net interest does not exceed it, so all €800,000 is deductible.

### Case 4: innovation box fixed percentage (2026) ([Fixed percentage](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/innovatiebox/kiezen-voor-een-vast-bedrag))

- A smaller taxpayer with an S&O-verklaring created software in 2026 and elects the box. Profit before the box is €80,000. 25% is €20,000, under the €25,000 cap, so €20,000 is the box benefit.
- Under article 12b the box benefit counts for 9/25.8 of its amount: €6,977 (rounded). The taxable amount falls by €13,023.
- With profit before the box of €200,000, 25% would be €50,000, so the cap applies and the box benefit is €25,000.
- The box threshold (production costs) must still be passed first.

### Case 5: partly deductible costs (2026) ([Threshold 2026](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/veranderingen-inkomstenbelasting-2026/drempel-beperkt-aftrekbare-kosten-2026))

- Representation and food and drink costs of €20,000.
- Threshold method: deductible €20,000 minus €5,700 = €14,300.
- Percentage method: 73.5% of €20,000 = €14,700 deductible, so €5,300 is added back.
- The percentage method gives the higher deduction here.

### Case 6: participation that drops below 5% ([Participations](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/deelnemingsvrijstelling/deelnemingen))

- A bv held 6% of an active trading company for 4 years, then was diluted to 3%. Dividends in the next 3 years stay exempt. A holding that was always 3% was never a participation, so its dividends are taxed.

### Case 7: fiscal unity start date ([wetten.overheid.nl, article 15(9)](https://wetten.overheid.nl/BWBR0002672/2026-01-01))

- A request filed on 1 May 2026 can take effect on 1 February 2026 at the earliest. A start date of 1 January 2026 is too early.

### Case 8: late return (2025 return, calendar year) ([Penalties](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/standaard_functies/prive/contact/rechten_en_plichten_bij_de_belastingdienst/boete))

- No extension was requested and the return was not filed by 1 June 2026. The Belastingdienst sends a demand (aanmaning) with a deadline. Filing after the demand deadline brings a default penalty of €3,354, rising to €6,709 for repeated years. Because the return is received on or after 1 June, tax interest also runs from 1 July 2026 on the tax due.

## When to refuse or refer

- Cross-border elements: a foreign shareholder, a foreign subsidiary or permanent establishment, withholding taxes, controlled foreign company income, or a fiscal unity using the EU exceptions. Refer to an international tax adviser.
- Fiscal unity formation, termination or a break (a member leaves or falls below 95%) ([fiscal unity](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/fiscale_eenheid_vennootschapsbelasting)). Refer.
- Transfer pricing or undocumented intercompany loans and charges. Refer.
- Earnings stripping where net interest is near or above €1,000,000, or within a fiscal unity ([earnings stripping](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/generieke-renteaftrekbeperking)). Refer.
- Innovation box claims, other than confirming whether an S&O-verklaring exists. The allocation of profit to the box is technical. Refer.
- Any 30% or more ownership change with losses, or holding company losses ([change of ownership](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/verrekenen_van_verliezen/belangenwijziging)). Refer.
- Investment participations, the credit method, or a participation of less than 5% with a history above 5% ([participations](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/deelnemingsvrijstelling/deelnemingen)). Refer.
- Liquidation or cessation losses, mergers, demergers, share-for-share exchanges. Refer.
- Groups with consolidated revenue of at least €750 million: the minimum tax ([minimum tax](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/minimumbelasting)). Refer.
- Banks, insurers, housing corporations, fiscal or exempt investment institutions, foundations and associations. Refer.
- No annual accounts, or no trial balance and profit and loss account: refuse to compute; ask for them.
- Uncertain positions with a material tax effect: flag them for a Dutch belastingadviseur before filing.

## Filing and payment

### Return deadlines ([Belastingdienst: filing the Vpb return](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/aangifte-vennootschapsbelasting-doen))

| Financial year | Deadline |
| --- | --- |
| Calendar year | Before 1 June of the next year (2025 return: before 1 June 2026) |
| Broken year | Within 5 months after the end of the financial year |
| Short year ending 31 December | By 1 June of the next year |
| Short year ending in another month | Before 1 April of the next calendar year, as the page states; confirm with the Belastingdienst if that date comes before the year's accounts can be ready |

- File through Mijn Belastingdienst Zakelijk, with tax software, or through a tax service provider.
- **Extension** ([Belastingdienst](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/uitstel_aangifte_vennootschapsbelasting)): online, for a calendar year, to 1 November (5 months after 1 June). Apply before 1 June; the online form is open from 1 March to 1 June. For a broken year or a longer extension, use the paper form with reasons, within 5 months after the end of the financial year. Tax service providers can also request extension.
- 2025 returns: due before 1 June 2026, or by 1 November 2026 if extended online.

### Provisional assessments ([Belastingdienst: provisional assessment](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/voorlopige_aanslag_vennootschapsbelasting))

- Most companies receive a provisional assessment at the start of the year, based on earlier years. The company must check it and ask for a change if it expects a higher or lower profit. Changes can be passed on until the return is filed. The Belastingdienst processes at most 3 increases for one year.
- No objection against a provisional assessment; ask for a change instead.
- No assessment received but tax expected? Request one.
- **Paying** ([in instalments](https://www.belastingdienst.nl/wps/wcm/connect/nl/betalenenontvangen/content/in-termijnen-betalen)): a provisional assessment for the current year is paid in equal monthly instalments, fully by 31 December. If fewer than 2 whole months remain after the date on the assessment, the term is 6 weeks. The date of the first payment is on the assessment ([when to pay](https://www.belastingdienst.nl/wps/wcm/connect/nl/betalenenontvangen/content/wanneer-moet-ik-betalen)).
- The final assessment credits all provisional assessments. Its payment date is printed on it.

### Tax interest ([Belastingdienst: tax interest on Vpb](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/standaard_functies/prive/contact/rechten_en_plichten_bij_de_belastingdienst/belastingrente/belastingrente_betalen_bij_vennootschapsbelasting))

- Tax interest is charged if the return is received **on or after 1 June** after the tax year, or if the assessment departs from the return (even if filed before 1 June). It runs from 1 July. For a broken year read the 6th month after year end for 1 June.
- No tax interest if the return is filed before 1 June and followed unchanged, or if a provisional assessment is requested before 1 May after the tax year and imposed as requested. For a broken year read the 5th month after year end for 1 May.
- Rates: see "Figures by year".

### Objection ([Belastingdienst: how to object](https://www.belastingdienst.nl/wps/wcm/connect/nl/bezwaar-en-beroep/content/eisen-bezwaar))

- Object within 6 weeks after the date of the assessment, decision or payment. Vpb objections can be made in Mijn Belastingdienst Zakelijk or by letter. After 6 weeks, a request for reduction (verzoek om vermindering) is still possible.

### Penalties ([Belastingdienst: penalties](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/standaard_functies/prive/contact/rechten_en_plichten_bij_de_belastingdienst/boete))

| Default | Penalty |
| --- | --- |
| Not asking for a return in time (Vpb: within 6 months after the tax debt arose; no penalty if asked within 2 weeks after that) | €3,354 |
| Vpb return not filed, or filed after the deadline in the demand (aanmaning) | €3,354, rising to €6,709 if missed several years in a row |
| Assessment not paid, paid late or paid short | 5% of the unpaid amount of the (provisional) assessment, minimum €50, maximum €6,709 each time |
| Intentionally incorrect or no return | 50% of the tax intentionally withheld (25% for gross negligence), before increases or reductions; up to 100% for fraud or a previous offence |

No penalty is imposed for a missing or late return if the company is not at all to blame.

### Minimum tax (Pillar Two), summary only ([Belastingdienst: minimum tax](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/minimumbelasting))

- The Wet minimumbelasting 2024 applies to group entities of multinational and domestic groups with annual revenue of at least €750 million in the ultimate parent's consolidated accounts. The rate is 15%.
- Per country, if the effective tax rate is below 15%, the difference is charged as a top-up tax (bijheffing).
- A top-up tax information return (BIA) is due within 15 months after the end of the reporting year (18 months for the first year), unless filed in another country and exchanged; then a notification is due in the same period.
- A tax return is due, if Dutch top-up tax is payable, within 17 months (20 months for the first year).
- No default penalty for late minimum tax returns or payments up to and including 31 October 2026 ([news, 18 August 2026](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/berichten/nieuws/geen-verzuimboete-minimumbelasting-tot-en-met-31-oktober-2026)).
- Groups below the threshold are outside the minimum tax. Every group in scope needs specialist advice.

## Completion checklist ([Belastingdienst: Vpb rates](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/tarieven_vennootschapsbelasting))

- [ ] Legal form, residence and financial year confirmed; year of the return identified (2025 or 2026).
- [ ] Return deadline and any extension recorded; tax interest risk checked (filed before 1 June?).
- [ ] Commercial result reconciled to fiscal profit; partly deductible costs limited by one method only.
- [ ] Buildings not depreciated below WOZ value; goodwill at most 10% and other assets at most 20% a year.
- [ ] Each shareholding tested: at least 5%, investment participation, qualifying; losses and acquisition costs on participations not deducted.
- [ ] Fiscal unity decision in hand and all members still meet the 95% conditions.
- [ ] Net interest compared with the higher of 24.5% of adjusted profit and €1,000,000; excess carried forward.
- [ ] Innovation box: S&O-verklaring (and, for larger taxpayers, the extra right) on file; election made in the return.
- [ ] Losses carried back first, then forward within the cap; ownership changes of 30% or more checked.
- [ ] Tax computed at 19% up to €200,000 and 25.8% above; provisional assessments credited.
- [ ] Dga salary at least the highest of the three tests (€58,000 minimum amount for 2026).
- [ ] Group revenue checked against the €750 million minimum tax threshold.
- [ ] Items in "When to refuse or refer" flagged for a Dutch belastingadviseur.

This Guide was first adapted from material by John in 't Hout (MIT licence) and has since been rewritten from official sources. It is not tax advice.

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
