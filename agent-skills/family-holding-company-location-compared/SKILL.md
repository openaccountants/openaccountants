---
name: family-holding-company-location-compared
description: "Where to put a family holding company: Malta, Cyprus, Ireland, Luxembourg, the Netherlands, Switzerland, Singapore, the UAE and the UK compared on corporate rate, participation exemption for dividends and gains (holding size, period, subject-to-tax tests), withholding on dividends paid out, and Malta's refund system, with a worked hypothetical and the conditions that decide each answer."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/family-holding-company-location-compared"
  jurisdiction: "general"
  tax_year: "2026"
  last_updated: "2026-11-16"
---

# Where to put the family holding company: nine countries compared (2026, v1.0)

Figures are for tax year 2026. Compare a family-owned company holding operating subsidiaries in Malta, Cyprus, Ireland, Luxembourg, the Netherlands, Switzerland, Singapore, the UAE or the UK. Test incoming dividends, a disposal and cash paid to the family separately. A headline rate is not a final bill; a participation exemption is not a shareholder exemption. The actual operative sources and material neighbours were read on 16 November 2026 within the scopes in Sources. This is a source-cited draft, with the legal-version, translation and execution limits stated below. It makes no accountant-attestation claim.

This Guide is a first sort. It does not decide residence of the company, CFC exposure of the family member at home, or substance. For those, see `mt-company-residence-and-substance` and `cfc-and-substance-rules-compared`. For Malta in depth, see `mt-holding-company-participation-exemption`. For trusts and foundations as the top of the structure, see `trusts-vs-foundations-by-country`.

## The method, step by step

1. Fix the facts first: where each family member is tax resident, where the operating subsidiaries are resident, the size of each holding, the date each holding was acquired, and whether each subsidiary trades or mainly holds investments or property. Every exemption below turns on these. Use the questions in "Ask the client first".
2. For each candidate country, test the dividend exemption on its own conditions (holding size, holding period, subject-to-tax or anti-abuse test). The country sections below give each test with its law and link, for example Malta's article 12(1)(u) in the [Income Tax Act, Cap. 123](https://legislation.mt/eli/cap/123/eng/pdf).
3. Test the gains exemption separately. In most of these countries the gains test differs from the dividend test (the UK requires a trading subsidiary, Singapore requires a bigger stake held longer, Luxembourg has a higher acquisition-cost alternative). See the UK [CG53072](https://www.gov.uk/hmrc-internal-manuals/capital-gains-manual/cg53072) and Singapore's [section 13W e-Tax Guide](https://www.iras.gov.sg/docs/default-source/e-tax/etaxguide_certainty-of-non-taxation-of-companies-gain-on-disposal-of-equity-investments.pdf?sfvrsn=ceb9a99_18).
4. Work out what happens when money leaves the holding company for the family: the outbound dividend withholding or shareholder-level charge, for individuals and for companies. Malta works through refunds to the shareholder under article 48 of the [Income Tax Management Act, Cap. 372](https://legislation.mt/eli/cap/372/eng/pdf) with a separate 15% charge on untaxed-account payments to a defined recipient.
5. Check the family member's home country. A low-taxed holding company may be taxed in the shareholder's own country under its CFC rules, whatever the holding country charges. See `cfc-and-substance-rules-compared`.
6. Screen for Pillar Two separately under the applicable country law. The UK framework below uses its consolidated-revenue threshold in two of the four preceding periods ([MTT11010](https://www.gov.uk/hmrc-internal-manuals/multinational-top-up-tax-and-domestic-top-up-tax/mtt11010)). Do not assume a family group is outside that scope.
7. Run the worked hypothetical in "Worked hypothetical" with the client's own numbers, and record which condition each answer depends on.

## Comparison at a glance

Each value in this table is repeated from the sourced country table further down. Read the country section before relying on a row: every exemption has conditions; a failed exemption does not always make the entire receipt taxable at the headline rate.

| Country | Headline corporate rate 2026 | Dividend exemption: holding and period | Gains exemption: holding and period | Outbound dividend tax | Official sources |
| --- | --- | --- | --- | --- | --- |
| Malta | 35% (article 56(6)); elective 15%, final, subject to the statutory floor and election conditions (L.N. 188 of 2025) | Participating holding (at least 5% of equity with 5% of 2 rights, or EUR 1,164,000 held 183 days, among other routes) plus anti-abuse test | Same participating holding test; restricted for Malta-resident investees (art. 12(1)(u) proviso) | Refunds to the shareholder (6/7, 5/7, 2/3 or 100%) on taxed-account dividends; fifteen per cent deducted on untaxed-account dividends to a "recipient" (article 61: mainly Malta-resident persons other than companies, and non-residents controlled by Malta ordinarily resident and domiciled individuals) | https://legislation.mt/eli/cap/123/eng/pdf; https://legislation.mt/eli/cap/372/eng/pdf; https://legislation.mt/eli/ln/2025/188/eng/pdf |
| Cyprus | 15% | All dividends exempt from corporate tax, with one exclusion (dividend deductible for the payer) | All gains on "titles" (shares and similar) exempt | 5% SDC for resident and domiciled individuals on 2026+ profits; 5% or 17% only within the connected-company, jurisdiction and exception conditions below | https://www.cylaw.org/nomoi/enop/non-ind/2002_1_118/full.html; https://www.cylaw.org/nomoi/enop/non-ind/2002_1_117/full.html |
| Ireland | 12.5% trading; 25% non-trading | At least five per cent for 12 months, foreign subsidiary (from 1 January 2025) | At least 5 per cent for 12 months, trading test | 25% DWT, with exemptions for qualifying non-residents | https://www.revenue.ie/en/companies-and-charities/corporation-tax-for-companies/corporation-tax/basis-of-charge.aspx; https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-35/35-02-11.pdf; https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-20/20-01-14.pdf; https://www.revenue.ie/en/companies-and-charities/dividend-withholding-tax/index.aspx |
| Luxembourg | 16% above EUR 200,000 taxable income; 23.87% combined in Luxembourg City | 10% or EUR 1,200,000, held 12 months | 10% or EUR 6,000,000, held 12 months | 15% withholding | https://impotsdirects.public.lu/dam-assets/fr/legislation/LIR/texte-coordonn-en-vigueur-au-1er-janvier-2026-ver-08052026.pdf; https://impotsdirects.public.lu/fr/az/c/charg_fisc.html; https://data.legilux.public.lu/eli/etat/leg/rgd/2001/12/21/n5/consolide/20250101/fr/pdf |
| Netherlands | 19.0% up to EUR 200,000; 25.8% above | At least 5% (participation exemption) | Same participation exemption | 15% dividend tax | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/tarieven_vennootschapsbelasting; https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/deelnemingsvrijstelling/deelnemingen; https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/dividendbelasting/als_u_dividend_uitkeert/als_u_dividend_uitkeert |
| Switzerland | 8.5% federal only, plus cantonal tax | Participation reduction (not an exemption), 10% or CHF 1 million | 10% held at least one year | 35% withholding tax | https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/1991/1184_1184_1184/20260101/de/pdf-a/fedlex-data-admin-ch-eli-cc-1991-1184_1184_1184-20260101-de-pdf-a.pdf; https://www.estv.admin.ch/estv/de/home/verrechnungssteuer.html |
| Singapore | 17% | Singapore dividends one-tier and not taxable; foreign dividends exempt if conditions met (headline rate at least 15%) | At least 20% held 24 months (section 13W) | No tax on one-tier dividends in the shareholder's hands | https://www.iras.gov.sg/taxes/corporate-income-tax/basics-of-corporate-income-tax/corporate-income-tax-rate-rebates-and-tax-exemption-schemes; https://www.iras.gov.sg/media/docs/default-source/e-tax/tax-exemption-for-foreign-sourced-income285e5d43d6af4001b3ce35da1e9005b5.pdf; https://www.iras.gov.sg/docs/default-source/e-tax/etaxguide_certainty-of-non-taxation-of-companies-gain-on-disposal-of-equity-investments.pdf?sfvrsn=ceb9a99_18; https://www.iras.gov.sg/docs/default-source/e-tax/tax-treatment-of-gains-or-losses-from-the-sale-of-foreign-assets.pdf?sfvrsn=a0e0458b_15; https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/what-is-taxable-what-is-not/dividends |
| UAE | 9% above AED 375,000 | 5% or AED 4 million, 12 months, subject to tax at 9% or more | Same participation exemption | 0% withholding tax | https://tax.gov.ae/Datafolder/Files/Legislation/Corporate%20Tax/Cabinet%20Decision%20No.%20116%20of%202022%20-%20for%20publishing.pdf; https://mof.gov.ae/wp-content/uploads/2026/01/Federal-Decree-Law-No.-47-of-2022-and-its-amendments-ar-v13.1.26.pdf; https://mof.gov.ae/wp-content/uploads/2024/12/2-Ministerial-Decision-No-302-of-2024-on-the-Participation-Exemption-and-Foreign-Permanent-Establishment-Exemption-on-the-Taxation-of-Corporations-and-Businesses-for-publishing_ar.pdf |
| United Kingdom | 25% main rate; conditional 19% small profits rate, unavailable to close investment-holding companies (see UK section) | Distribution exemption (exempt classes, Part 9A of the Corporation Tax Act 2009) | Substantial shareholdings exemption, at least 10% for 12 months, trading investee | Not yet confirmed; do not infer zero | https://www.gov.uk/government/publications/rates-and-allowances-corporation-tax/rates-and-allowances-corporation-tax; https://www.gov.uk/hmrc-internal-manuals/capital-gains-manual/cg53072; https://www.gov.uk/hmrc-internal-manuals/multinational-top-up-tax-and-domestic-top-up-tax/mtt11010 |

Pillar Two is a screening flag, not an exemption for family ownership. The UK section states that framework’s EUR 750 million test; each candidate country’s implementation, excluded entities and minimum-tax calculation require separate work.


## Malta

Malta taxes a company at a flat rate on chargeable income and then refunds part or all of that tax to the shareholder when the profits are paid out as a dividend. A holding company can also take a participation exemption instead.

| Item | Value | Conditions / scope | Official source |
| --- | --- | --- | --- |
| Company rate, article 56(6) | 35% | Apply the complete conditions in this country section; this value is not an unconditional bill. | https://legislation.mt/eli/cap/123/eng/pdf |
| Participating holding, route (a) | at least five percent of the equity shares | Apply the complete conditions in this country section; this value is not an unconditional bill. | https://legislation.mt/eli/cap/123/eng/pdf |
| Participating holding, route (e) | EUR 1,164,000 | Apply the complete conditions in this country section; this value is not an unconditional bill. | https://legislation.mt/eli/cap/123/eng/pdf |
| Dividend anti-abuse, limb (i)(2) | 15% | Apply the complete conditions in this country section; this value is not an unconditional bill. | https://legislation.mt/eli/cap/123/eng/pdf |
| Dividend anti-abuse, limb (i)(3) | 50% | Apply the complete conditions in this country section; this value is not an unconditional bill. | https://legislation.mt/eli/cap/123/eng/pdf |
| Dividend anti-abuse, limb (ii)(2) | 5% | Apply the complete conditions in this country section; this value is not an unconditional bill. | https://legislation.mt/eli/cap/123/eng/pdf |
| Tax deducted from an untaxed dividend paid to a recipient, article 62(1) | 15% | Apply the complete conditions in this country section; this value is not an unconditional bill. | https://legislation.mt/eli/cap/123/eng/pdf |

Rules, from article 12(1)(u) of the [Income Tax Act](https://legislation.mt/eli/cap/123/eng/pdf):

- WHO: a company registered in Malta that holds a participating holding. An equity holding normally requires a company that is not a defined property company and at least 2 of votes, profits and winding-up assets. The property-company definition includes direct Malta immovable property or rights and specified indirect interests, with the statutory business-premises exception; test that definition before using any route. The definition in article 2(1) has several routes, any one of which is enough (OR): at least five percent of the equity shares with at least five percent of any two of votes, distributable profits and assets on a winding up; an option to acquire the entire remaining equity shares to the extent permitted by the investee country’s law; first refusal on a proposed disposal, redemption or cancellation of all remaining equity shares; the right to sit on or appoint a director to the board; an investment of at least the amount in the table held for an uninterrupted period of not less than 183 days; or a holding for the furtherance of its own business that is not trading stock.
- WHAT: income or gains from the participating holding, and gains on its transfer, are exempt where the company has not shown them as chargeable income in its return. The company may instead declare them; the shareholder may then claim a refund (below).
- DIVIDEND CONDITIONS: for a dividend from a participating holding acquired on or after 1 January 2007 (and, from 1 January 2011, also one acquired before), the exemption applies only if the subsidiary meets ANY ONE of: resident or incorporated in the EU; subject to foreign tax of at least the 15% in the table; not more than 50% of its income from passive interest or royalties. If it meets none of these, BOTH of these must hold: the holding is not a portfolio investment, AND the subsidiary or its passive interest or royalties were subject to foreign tax of at least 5%.
- EXCLUSION: the exemption does not apply to income from a participating holding in a body resident in a jurisdiction on the EU list of non-cooperative jurisdictions for at least three months in the year before the year of assessment, unless the company proves commensurate sufficient significant people functions there to the Commissioner. Consecutive months straddling two basis years can disqualify either year. For covered EU parent-subsidiary distributions, the exemption is also denied to the extent the subsidiary can deduct the distributed profits (the final provisos to article 12(1)(u)).
- GAINS: the dividend conditions above apply to dividends only. A separate proviso covers a participating holding "in a company or in a partnership, EEIG, other body of persons or collective investment scheme ... that is resident in Malta", and holdings that hold such interests directly or indirectly. Gains on those "shall only qualify for the exemption if such gains or profits would have been exempt in terms of sub-paragraph (ii) of paragraph (c) had the transfer of the holding been made by the beneficial owner". Article 12(1)(c)(ii) exempts gains of "any person not resident in Malta". Where there are several beneficial owners, the exemption applies only to the exempt owners' share.

| Item | Value | Conditions / scope | Official source |
| --- | --- | --- | --- |
| Standard refund, article 48(4A)(a) | 6/7 | Apply the complete conditions in this country section; this value is not an unconditional bill. | https://legislation.mt/eli/cap/372/eng/pdf |
| Passive interest or royalties, or a participating holding dividend that fails the anti-abuse test | 5/7 | Apply the complete conditions in this country section; this value is not an unconditional bill. | https://legislation.mt/eli/cap/372/eng/pdf |
| Profits from a participating holding distributed out of the foreign income account, article 48(4)(b) | all of the Malta tax | Apply the complete conditions in this country section; this value is not an unconditional bill. | https://legislation.mt/eli/cap/372/eng/pdf |
| Foreign income account profits, article 48(4)(a) (the route where the company claimed double taxation relief, since article 48(4A) is then barred) | 2/3 | Apply the complete conditions in this country section; this value is not an unconditional bill. | https://legislation.mt/eli/cap/372/eng/pdf |

- WHO claims: the shareholder who receives the dividend, and only once registered for the purpose ("provided that such person is for such purpose registered in such manner as may be prescribed").
- NO REFUND under article 48(4A) on foreign income account profits where the company claimed double taxation relief; a two-thirds refund under article 48(4)(a) may then be claimed.
- CAP: the refund never exceeds the tax the company actually paid on the profits distributed. The 2/3 route’s Malta-tax base can include the specified double-taxation relief, but its separate actual-paid cap still applies (article 48(4)(c)). The tax-return, FSS and VAT-return compliance gates in article 48(1A)–(1B) remain relevant; registration is not by itself a payment promise.
- NOT SETTLED for Malta-resident individuals: article 12(1)(c)(iii) of the [Income Tax Act](https://legislation.mt/eli/cap/123/eng/pdf) exempts some taxed-account dividends paid to individuals and ties that exemption to the refund bar in the last proviso to article 48(1) of Cap. 372. How that interacts with the article 48(4A) refund was not settled from the text. Refer before telling a Malta-resident individual shareholder to rely on a refund (see `mt-holding-company-participation-exemption`).
- The full refund under article 48(4)(b) for participating holding dividends carries the same anti-abuse conditions as the exemption.

Elective final tax. [L.N. 188 of 2025](https://legislation.mt/eli/ln/2025/188/eng/pdf), the Final Income Tax Without Imputation Regulations, lets an entity elect to be taxed "at the rate of fifteen cents (0.15) on every euro of the chargeable income, in lieu of the rate determined in article 56(6)". It applies to income of the fiscal year preceding year of assessment 2025 and later years. Once elected, the entity cannot switch back before the end of a five-year period, and after switching back the ordinary rules apply for at least five consecutive years of assessment. The election is made by notice in the form and by the date the Commissioner sets. The 15-cent tax "shall be final and shall not be available as a credit or set off against the tax liability of any individual or entity, or as a refund to any person" (reg. 3(4)(b)), so no shareholder refund follows it. It "shall in no case be lower than" the ordinary tax "reduced by the amount of refund claimed or claimable in terms of article 48(4) or (4A)" by all shareholders (reg. 3(4)(a)). The taxed profits go to the final tax account (reg. 3(4)(c)). Chargeable income under the election excludes dividends received from profits that are not "allocated to the final tax account of another company registered in Malta" and income already taxed at a final rate (reg. 3(1) proviso). These regulations are S.L. 123.217.

A Malta company paying a dividend out of its untaxed account to a recipient must, on that payment, "deduct therefrom tax at a rate of fifteen per cent." under article 62(1) of the [Income Tax Act](https://legislation.mt/eli/cap/123/eng/pdf). Article 61 also includes specified trustees and EU/EEA individuals. It defines a recipient as, among others, a person, other than a company, resident in "Malta in the year in which a dividend is received by him or by any person on his behalf", and "a non-resident person (including a non-resident company) who is owned and controlled by, directly or indirectly, or who acts on behalf of, an individual who is ordinarily resident and domiciled in Malta". The foreign income account holds profits only "to the extent that they result from taxable income"; the untaxed account is the residual distributable-profit account after other taxed accounts under article 2. Do not decide a specific exempt-participation distribution’s account allocation or the resident individual’s refund position without the full tax-account and shareholder computation; that individual execution question remains unconfirmed below. Article 62 excludes payments to exempt persons and requires payment to the Commissioner by the 14th day after the payment month. Under articles 64–65 the recipient can use the ordinary final treatment or elect to declare the dividend with a withholding credit; article 66 excludes a non-recipient from this untaxed-dividend charge. Taxed-account refunds remain conditional as above.

## Cyprus

Cyprus’s current Income Tax Law, Second Schedule paragraph 2, sets corporate income tax at 15%. Article 8(20) exempts dividend income, except to the extent a corporate recipient’s dividend is deductible in computing the payer’s foreign tax; that denied amount is not a dividend for SDC. Article 8(22) exempts gains on defined titles. Article 2 includes shares, debentures, bonds, founders’ and other corporate/legal-person titles and rights over them, for Cyprus and foreign issuers. These provisions do not impose a general minimum participation percentage or holding period. The retained text is the Cyprus Bar’s current statutory consolidation, not a government presentation or an opinion. [Income Tax Law 118(I)/2002, articles 2/8 and Second Schedule](https://www.cylaw.org/nomoi/enop/non-ind/2002_1_118/full.html)

| Item | Value | Conditions and period | Source |
| --- | --- | --- | --- |
| Corporate tax | 15% | Current Second Schedule paragraph 2; separate dividend/title exemptions and SDC apply | https://www.cylaw.org/nomoi/enop/non-ind/2002_1_118/full.html |
| Dividend SDC on a Cyprus-resident, domiciled individual | 5% | Current article 3(1)(a), subject to legacy-profit treatment and reductions for previously charged dividends | https://www.cylaw.org/nomoi/enop/non-ind/2002_1_117/full.html |
| Legacy dividends from a Cyprus company’s profits through 2025 | 17% | Received within the statutory 6-year window from the 2026 reform, through 31 December 2031; test the profit year and prior charges | https://www.cylaw.org/nomoi/enop/non-ind/2002_1_117/full.html |
| Foreign corporate dividend SDC | 5% | Article 3(1)(c): BOTH investment-income activities above 50% AND foreign burden below 50% of the Cyprus burden | https://www.cylaw.org/nomoi/enop/non-ind/2002_1_117/full.html |
| Outbound to a connected low-tax-jurisdiction company | 5% | Article 3(1)(d): qualifying jurisdiction/incorporation route AND connected-company gate; exceptions below | https://www.cylaw.org/nomoi/enop/non-ind/2002_1_117/full.html |
| Outbound to a connected non-cooperative-jurisdiction company | 17% | Same article; non-cooperative rule prevails if both jurisdiction tests apply | https://www.cylaw.org/nomoi/enop/non-ind/2002_1_117/full.html |
| Indirect property-rich shares for CGT | 20% of market value | CGT Law article 2: Cyprus immovable-property value, ignoring liabilities; direct property-holding shares have a separate limb | https://www.cylaw.org/nomoi/enop/non-ind/1980_1_52/full.html |
| Deemed distribution of 2024/2025 profits | 70% at 17% SDC | Article 3C: after corporate tax, at end of 2 years; reductions, resident-attribution and other exceptions below | https://www.cylaw.org/nomoi/enop/non-ind/2002_1_117/full.html |

For individuals, residence and domicile are separate tests; the non-dom regime is retained. The 5% dividend rate does not erase the 17% legacy-profit window. Article 3(1)(a) also counters artificial interposed companies. An exempt non-dom does not automatically prove exemption from every other Cyprus levy or residence obligation.

For foreign dividends into a Cyprus holding company, article 3(1)(c)’s two conditions are cumulative: more than 50% of the payer’s direct or indirect activity must produce investment income AND the foreign tax burden must be lower than half the Cyprus burden. A corporate-tax exemption alone does not settle SDC.

For outbound corporate dividends, article 3(1)(d)(ii) requires the specified direct or indirect connection: the recipient in the payer, the payer in the recipient, or the same person and connected persons in both, with MORE than 50% of votes, capital or profits. Low-tax means a third-country corporate rate below half the Cyprus corporate rate; non-cooperative status uses the statutory EU-list definition. Incorporation/residence alternatives, the regulated-market reasonable-knowledge exception, anti-abuse rules and qualified permanent-establishment exceptions must be tested. These are not universal 5%/17% charges on every foreign company. [SDC Law 117(I)/2002, articles 2 and 3(1)(d)](https://www.cylaw.org/nomoi/enop/non-ind/2002_1_117/full.html)

Property-rich shares: the separate CGT Law covers direct Cyprus property-holding shares and indirect shares where at least 20% of market value derives from Cyprus immovable property, without deducting liabilities. A corporate title exemption does not override that charge. Apply the actual treaty if relevant; the old unqualified 50% treaty statement is not a universal treaty rule and is held below. [CGT Law 52/1980, article 2](https://www.cylaw.org/nomoi/enop/non-ind/1980_1_52/full.html)

Deemed distributions: article 3C applies to 70% of the defined 2024/2025 accounting profits after corporate tax at the end of 2 years, reduced by actual dividends paid in the profit year or that period. It applies only to profits attributable directly or indirectly to an individual resident in Cyprus at the deemed-distribution date, subject to the statutory exceptions and domicile rules. Specific liquidation, restructuring, debt-write-off and reorganisation conditions remain relevant; the company initially pays and charges the shareholder. The new provision does not extend deemed distribution to profits of 2026 onward. Transitional intercompany dividends from 2024/2025 profits and older indirect distributions have separate article 3(1)(b) rules; obtain the profit-year chain before computing.

## Ireland

| Item | Value | Conditions / scope | Official source |
| --- | --- | --- | --- |
| Trading income | 12.5% | Apply the complete conditions in this country section; this value is not an unconditional bill. | https://www.revenue.ie/en/companies-and-charities/corporation-tax-for-companies/corporation-tax/basis-of-charge.aspx |
| Non-trading income (rental, investment) and excepted trades | 25% | Apply the complete conditions in this country section; this value is not an unconditional bill. | https://www.revenue.ie/en/companies-and-charities/corporation-tax-for-companies/corporation-tax/basis-of-charge.aspx |

| Item | Value | Conditions / scope | Official source |
| --- | --- | --- | --- |
| Dividend withholding tax (DWT), 2026 | 25% | Apply the complete conditions in this country section; this value is not an unconditional bill. | https://www.revenue.ie/en/companies-and-charities/dividend-withholding-tax/index.aspx |

- Foreign distributions, section 831B: a parent must be Irish resident, or EEA-resident for the specified foreign tax and not generally exempt, and otherwise within Irish Case III or section 138 Case IV. A qualifying participation requires at least 5% of ordinary capital, distributable profits and winding-up assets, directly or through a permitted chain, continuously for at least 12 months including the distribution date. Trading-stock shares and impermissible intermediary chains do not count. The 12 months may finish after a distribution where the conditions are subsequently fulfilled; correct the return if the expectation fails.
- The foreign subsidiary must be resident in a relevant territory and not generally exempt from the specified foreign tax on the distribution date. Throughout the relevant period it must instead have been either Irish resident OR resident for foreign tax in a relevant territory and not generally exempt from that tax. For distributions in 2025 the lookback was 5 years; from 1 January 2026 it is 3 years, or since incorporation/formation if later. EEA/treaty-in-force and signed-but-not-in-force territories qualify, subject to the listed-territory exclusion and the current statutory treaty rules. From 2026 a specified non-EEA/non-treaty territory can qualify only with its nominal cross-border withholding tax above 0%, actually paid on the FULL distribution and not refunded to any person. Pillar Two top-up tax is not that foreign corporate tax.
- The 2026 reference period for excluded business acquisitions and formation through excluded mergers is also 3 years; examine the transferor/merging entities’ territory history, not just the current subsidiary address. A share acquisition alone is not the excluded business acquisition. Section 831B(9)’s treaty-residence fallback for a jurisdiction without a domestic residence concept has its own conditions.
- The receipt must be income, from the relevant subsidiary’s share capital, out of profits or out of assets at a cost to the subsidiary. An asset distribution additionally requires a hypothetical section 626B-exempt share disposal on that date. Offshore-fund distributions, winding-up distributions and specified debt/interest-equivalent receipts are excluded. Foreign deductibility normally excludes the deductible part, including a deduction available but unused; from 2026 the narrowly specified foreign close-company-surcharge deduction is excepted. Genuine commercial reasons and the targeted tax-advantage anti-avoidance test apply.
- Claim on Form CT1 for the accounting period. The election covers ALL relevant distributions from ALL relevant subsidiaries for that period, never selected dividends; it can change next period. There is no additional foreign-tax credit on the exempt distributions; prior unused credits are not automatically forfeited. This is not a blanket exemption for trading receipts, section 110 companies or collective investment/life-business income. [Revenue TDM 35-02-11, March 2026, sections 2–7; TCA 831B](https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-35/35-02-11.pdf)
- Gains, [section 626B](https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-20/20-01-14.pdf): a gain on disposal of shares is not a chargeable gain where the investor company has held a "real" holding of at least 5 per cent for a continuous period of 12 months (the disposal must be while it is a parent or within 2 years after), the investee is resident in an EU state or a territory with an Irish treaty in force or signed but not yet in force, AND at the time of disposal the investee or the group is wholly or mainly (more than half) trading. The exemption excludes the specified Irish land/mineral/exploration-rights shares, life-business shares, section 627 deemed disposals and other listed disposals; anti-avoidance applies. The September 2026 manual’s liquidation trading concession requires written Revenue approval. “More than half trading” is assessed primarily using net trading profits and net trading assets, with other relevant factors; it is not simply a label on the company.
- Outbound: Irish companies withhold DWT at the rate in the table. A [qualifying non-resident](https://www.revenue.ie/en/companies-and-charities/dividend-withholding-tax/exemptions-for-non-residents.aspx) can claim exemption by declaration (Form V2B for a company, V2A for an individual). For an individual this means not resident or ordinarily resident in Ireland and resident in an EU or EEA state or treaty country. For a company it includes one resident in such a territory that is not directly or indirectly controlled by an Irish resident. The exemption is not automatic; current outbound defensive measures also apply. Forms V2A and V2C require foreign tax-authority certification; provide the declaration to the company/AWA/QI. It lasts until 31 December of the fifth year following issue and must be renewed. Other corporate control/listed-shareholding categories exist; the company’s form is V2B, other bodies use V2C.
- A family-owned Irish company will often be a [close company](https://www.revenue.ie/en/companies-and-charities/corporation-tax-for-companies/corporation-tax/close-companies.aspx) (controlled by five or fewer participators, or by its directors). Part 13 of the Tax and Duty Manuals then applies; its rates are not printed within the stated source scopes.

## Luxembourg

| Item | Value | Conditions / scope | Official source |
| --- | --- | --- | --- |
| Corporate income tax (IRC), taxable income above EUR 200,000, from tax year 2025 | 16% | Apply the complete conditions in this country section; this value is not an unconditional bill. | https://impotsdirects.public.lu/fr/az/t/tarif-applicable-collectivites/tarif-collect.html |

| Item | Value | Conditions / scope | Official source |
| --- | --- | --- | --- |
| Combined IRC, employment fund surcharge and municipal business tax, Luxembourg City, from 2025 | 23.87% | Apply the complete conditions in this country section; this value is not an unconditional bill. | https://impotsdirects.public.lu/fr/az/c/charg_fisc.html |

| Item | Value | Conditions / scope | Official source |
| --- | --- | --- | --- |
| Dividend exemption: minimum holding | 10% | Apply the complete conditions in this country section; this value is not an unconditional bill. | https://impotsdirects.public.lu/fr/az/r/regi_soc.html |
| Dividend exemption: alternative acquisition price | EUR 1,200,000 | Apply the complete conditions in this country section; this value is not an unconditional bill. | https://impotsdirects.public.lu/fr/az/r/regi_soc.html |
| Gains exemption: alternative acquisition price | EUR 6,000,000 | Apply the complete conditions in this country section; this value is not an unconditional bill. | https://impotsdirects.public.lu/fr/az/r/regi_soc.html |

The old agency page was last updated on 9 January 2017. The operative participation provisions were separately read in the 2026 LIR coordinated text and the regulation consolidated at 1 January 2025; the authority labels these consolidations documentary rather than legally authentic texts.

| Item | Value | Conditions / scope | Official source |
| --- | --- | --- | --- |
| Withholding tax rate on dividends, article 148 | 15% | Apply the complete conditions in this country section; this value is not an unconditional bill. | https://impotsdirects.public.lu/dam-assets/fr/legislation/LIR/texte-coordonn-en-vigueur-au-1er-janvier-2026-ver-08052026.pdf |

- The 16% in the first table applies to taxable income above EUR 200,000 and is corporate income tax only. The combined figure is the authority's own example for a company seated in the commune of Luxembourg; other communes differ. The coordinated law text in force on 1 January 2026 carries the same 16% in article 174.
- Dividend exemption (article 166 LIR): a fully taxable resident capital company, or a qualifying permanent establishment, holding directly a participation in a fully taxable resident company, a non-resident company fully subject to a tax corresponding to IRC, or an organism covered by article 2 of Directive 2011/96/EU (the applicable company-class, residence and tax-status conditions, not EU location alone), is exempt on the dividend where, on the date the income is made available, it holds or undertakes to hold the participation for an uninterrupted period of at least 12 months AND throughout that period the holding does not fall below 10% OR the acquisition price does not fall below the amount in the table. If the 12 months are not reached, the exemption is withdrawn by a corrective assessment. Article 166(2bis) denies deductible or non-genuine EU tax-advantage distributions; directly related expenses and distribution-linked write-downs are restricted. A cost-only dividend exemption can be waived annually per participation; specified exchanged holdings have a separate 5-year restriction.
- Gains: under the 21 December 2001 regulation, article 1, the 10% OR EUR 6,000,000 alternative and 12-month held/committed period apply to the specified article 166 recipient and investee classes. Transparent holdings count proportionately; securitisation interests are excluded. Prior negative participation income or deducted impairment, including qualifying subsidiary receivables, can be recaptured. Rolled-over gains under articles 53/54 and a specified exchanged participation’s first 5 years can also restrict exemption. A cost-only exemption may be waived per participation and tax year under article 1(2a), with separate recapture tracking. [Actual consolidated regulation, articles 1–3](https://data.legilux.public.lu/eli/etat/leg/rgd/2001/12/21/n5/consolide/20250101/fr/pdf)
- Outbound: current LIR article 147 exempts only its specified qualifying corporate/public/PE recipients with direct 10% OR EUR 1,200,000 participation for a held/committed 12 months and the relevant anti-abuse conditions; the future-commitment route is subject to article 149(4)’s applicable guarantee/procedure conditions. Without an undertaking, article 149(4a) instead requires withholding and permits a later refund after proof of the period and continuing holding threshold; an individual family shareholder does not qualify merely because the payer is a holding company. Article 148’s ordinary withholding is 15% of gross income; treaty relief is separate. The authority's page states that a company paying an exempt participation dividend is, under certain conditions, exempt from withholding. That page (last updated 9 January 2017) prints an older withholding rate; the law in force on 1 January 2026 prints the rate in the last table. Use the law.

## Netherlands

| Item | Value | Conditions / scope | Official source |
| --- | --- | --- | --- |
| Band limit | EUR 200,000 | Apply the complete conditions in this country section; this value is not an unconditional bill. | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/tarieven_vennootschapsbelasting |
| Rate up to and including the band limit | 19.0% | Apply the complete conditions in this country section; this value is not an unconditional bill. | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/tarieven_vennootschapsbelasting |
| Rate above the band limit | 25.8% | Apply the complete conditions in this country section; this value is not an unconditional bill. | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/tarieven_vennootschapsbelasting |

| Item | Value | Conditions / scope | Official source |
| --- | --- | --- | --- |
| Participation: minimum holding | 5% | Apply the complete conditions in this country section; this value is not an unconditional bill. | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/deelnemingsvrijstelling/deelnemingen |

| Item | Value | Conditions / scope | Official source |
| --- | --- | --- | --- |
| Dividend tax rate | 15% | Apply the complete conditions in this country section; this value is not an unconditional bill. | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/dividendbelasting/als_u_dividend_uitkeert/als_u_dividend_uitkeert |

- Participation exemption: where a participation exists (at least 5% of the paid-up nominal capital, among other routes on the page), profits from it are generally exempt. The basic ordinary-capital route starts at 5%, but statutory associated-body, profit-certificate and hybrid-loan extensions exist. Separately, a participation of at least 5% held for more than 1 year that falls below 5% keeps the exemption for 3 more years.
- The exemption "is niet van toepassing op een niet-kwalificerende beleggingsdeelneming"; participation credit (deelnemingsverrekening) may be available instead, subject to its conditions. Whether a participation is held as an investment "hangt onder meer af van het oogmerk"; a top holding company with a real management, policy or financing function for the group may not hold it as an investment. A participation whose assets are mostly holdings below 5%, or whose function is mostly group financing, is always a portfolio participation. See [Deelnemingsvrijstelling](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/deelnemingsvrijstelling/deelnemingsvrijstelling) and [Wanneer is een deelneming een beleggingsdeelneming?](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/deelnemingsvrijstelling/wanneer_is_een_deelneming_een_beleggingsdeelneming).
- Qualifying portfolio exception: exemption can still apply irrespective of purpose if the subsidiary bears a real profit tax by Dutch standards OR its assets generally consist for less than half, directly/indirectly, of low-tax free investments. A 10% rate is normally real only with the Dutch-comparable base; a headline rate alone is insufficient. Underlying-asset, external-financing and active-business exceptions need their own facts. [Qualifying investment participation](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/deelnemingsvrijstelling/kwalificerende_beleggingsdeelneming); [Low-tax free investments](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/deelnemingsvrijstelling/laagbelaste_vrije_beleggingen)
- Holding period: the agency’s basic 5% test does not state a general minimum period. This does not remove the separate more-than-1-year and 3-year continuation conditions. A fiscal investment institution cannot apply the participation exemption; acquisition/disposal costs are not deductible.
- Outbound to a Dutch resident individual: the paying company "meestal" withholds the rate in the table on a portfolio dividend.
- Outbound to a company: on a participation dividend (5% or more) to a Dutch company, the company usually applies the withholding exemption. To a company in a [country with which the Netherlands has a tax treaty](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/dividendbelasting/als_u_dividend_uitkeert/deelnemingsdividend-uitkeren-aan-aandeelhouder-buiten-nederland), the agency describes a withholding exemption where there is no abuse; report the exempt foreign participation dividend with an opgaaf. Do not turn that abbreviated agency route into a complete exclusion of every other statutory exemption. If a lower treaty rate is used instead, the agency requires prior permission; reporting and the actual recipient conditions still apply.
- For Dutch corporate tax in full, see `nl-corporate-tax`.

## Switzerland

| Item | Value | Conditions / scope | Official source |
| --- | --- | --- | --- |
| Withholding tax (Verrechnungssteuer) on investment income | 35% | Apply the complete conditions in this country section; this value is not an unconditional bill. | https://www.estv.admin.ch/estv/de/home/verrechnungssteuer.html |

The federal rules come from the [Federal Direct Tax Act (DBG), status 1 January 2026](https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/1991/1184_1184_1184/20260101/de/pdf-a/fedlex-data-admin-ch-eli-cc-1991-1184_1184_1184-20260101-de-pdf-a.pdf). Articles 68–70 were read in full with their neighbours; the statutory reduction and its net-income limits are:

- Rate, article 68: The federal company/cooperative profit tax is 8.5% of net profit. This is the federal tax only. Cantonal and communal profit taxes come on top and are not covered by this Guide.
- Participation reduction, article 69: the federal profit tax is REDUCED in the ratio of net participation income to total net profit (it is not an exemption) where the company holds at least 10% of capital OR at least 10% of profits and reserves of another company, OR holds participation rights with a market value of at least one million francs.
- Net income, article 70: participation income less related financing costs and a flat contribution of 5% for administration (or actual administrative costs if proved). Write-downs linked to the income reduce the relief. Income deductible as an expense by the payer and participation revaluation gains are excluded; unjustified intra-group tax savings can cause an adjustment.
- Gains, article 70(4): count only to the extent the sale price exceeds cost, AND only if the holding sold was at least 10% of capital or of profits and reserves AND was held for at least one year. After a part sale takes the holding below 10%, later sales qualify only if the holding had a market value of at least one million francs at the end of the tax year before the sale.
- Outbound: the withholding tax in the table is charged on dividends. For a Swiss-resident recipient relief requires correct declaration of the assets and income, or company booking of the income. Apply within 3 years after the end of the calendar year in which the taxable payment fell due, and test the anti-avoidance bar. For others, treaty relief applies on a qualifying claim. The treaty rates are not printed on the page read.

## Singapore

| Item | Value | Conditions / scope | Official source |
| --- | --- | --- | --- |
| Corporate income tax rate | 17% | Apply the complete conditions in this country section; this value is not an unconditional bill. | https://www.iras.gov.sg/taxes/corporate-income-tax/basics-of-corporate-income-tax/corporate-income-tax-rate-rebates-and-tax-exemption-schemes |

| Item | Value | Conditions / scope | Official source |
| --- | --- | --- | --- |
| Foreign headline tax rate condition | 15% | Apply the complete conditions in this country section; this value is not an unconditional bill. | https://www.iras.gov.sg/media/docs/default-source/e-tax/tax-exemption-for-foreign-sourced-income285e5d43d6af4001b3ce35da1e9005b5.pdf |

| Item | Value | Conditions / scope | Official source |
| --- | --- | --- | --- |
| Section 13W minimum shareholding | 20% | Apply the complete conditions in this country section; this value is not an unconditional bill. | https://www.iras.gov.sg/docs/default-source/e-tax/etaxguide_certainty-of-non-taxation-of-companies-gain-on-disposal-of-equity-investments.pdf?sfvrsn=ceb9a99_18 |

- Singapore dividends: under the one-tier system, dividends paid by a Singapore resident company are not taxable in the shareholder's hands ("as the tax paid by a company is final"), except dividends from co-operatives ([IRAS dividends page](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/what-is-taxable-what-is-not/dividends)).
- Foreign dividends received in Singapore by a resident company are exempt only if ALL three conditions hold: the income was subject to tax abroad; the foreign headline corporate rate is at least the 15% in the table when the income is received; AND the Comptroller is satisfied the exemption benefits the company. Foreign income can be received by remittance, paying a Singapore-business debt, or buying movable property brought into Singapore. For dividends, subject-to-tax includes qualifying underlying tax paid/payable, with the agency’s limited substantive-business incentive and custody conditions; a high headline rate alone is insufficient. The rate is the source country’s highest relevant rate in the receipt year, with the special-legislation qualification. Declare the qualifying income and retain the supporting documents; section 13(7A)–(11) and the January 2026 FSIE guide control.
- Gains, section 13W: for disposals from 1 January 2026, gains on ordinary shares and/or qualifying preference shares are not taxable if the divesting company held at least the 20% in the table for a continuous period of at least 24 months immediately before the disposal; for 2026 the threshold concerns the total paid-up capital of ordinary and equity-accounted qualifying preference shares. Group assessment requires the specified more-than-50% beneficial ordinary-share connections or common corporate parent, the continuously held shares throughout the 24 months, and FIFO tracking. RBTs/VCCs cannot use the group basis. Section 26 divesting companies are excluded; supply the election information in the income-tax return and keep records. The scheme does not apply to non-listed shares in a company that trades immovable property, or whose principal activity is holding immovable property whereby passive or no income is derived (Singapore or elsewhere, for disposals from 1 June 2022), or a company that "has undertaken property development activities (in Singapore or elsewhere)", unless it uses the property in its own trade and did no development in the past 60 months. A gain outside section 13W is not automatically taxable; ordinary income/capital analysis and section 10L must both be considered.

- Foreign-disposal override: section 10L can tax otherwise capital or exempt foreign disposal gains, including section 13W gains, from disposals on or after 1 January 2024 when received in Singapore by a covered relevant-group entity. A group’s foreign entity or foreign place of business, consolidation and the particular recipient matter. For a pure equity-holding entity, the non-IP exception requires regular legal filings, operations managed/performed in Singapore and adequate Singapore human resources/premises in the disposal period. A nominee director or unused registered address alone is insufficient. Non-pure entities, outsourcing and SPVs have separately defined conditions; foreign IP has different rules. No economic-substance result is inferred from a 30% holding alone. [IRAS foreign-assets guide, June 2025, sections 2–8](https://www.iras.gov.sg/docs/default-source/e-tax/tax-treatment-of-gains-or-losses-from-the-sale-of-foreign-assets.pdf?sfvrsn=a0e0458b_15)

## United Arab Emirates

| Item | Value | Conditions / scope | Official source |
| --- | --- | --- | --- |
| Rate on taxable income up to the threshold | 0% | Apply the complete conditions in this country section; this value is not an unconditional bill. | https://tax.gov.ae/Datafolder/Files/Legislation/Corporate%20Tax/Cabinet%20Decision%20No.%20116%20of%202022%20-%20for%20publishing.pdf |
| Threshold | AED 375,000 | Apply the complete conditions in this country section; this value is not an unconditional bill. | https://tax.gov.ae/Datafolder/Files/Legislation/Corporate%20Tax/Cabinet%20Decision%20No.%20116%20of%202022%20-%20for%20publishing.pdf |
| Rate above the threshold | 9% | Apply the complete conditions in this country section; this value is not an unconditional bill. | https://tax.gov.ae/Datafolder/Files/Legislation/Corporate%20Tax/Cabinet%20Decision%20No.%20116%20of%202022%20-%20for%20publishing.pdf |

| Item | Value | Conditions / scope | Official source |
| --- | --- | --- | --- |
| Minimum ownership | 5% | Apply the complete conditions in this country section; this value is not an unconditional bill. | https://mof.gov.ae/wp-content/uploads/2024/12/2-Ministerial-Decision-No-302-of-2024-on-the-Participation-Exemption-and-Foreign-Permanent-Establishment-Exemption-on-the-Taxation-of-Corporations-and-Businesses-for-publishing_ar.pdf |
| Alternative acquisition cost | AED 4 million | Apply the complete conditions in this country section; this value is not an unconditional bill. | https://mof.gov.ae/wp-content/uploads/2024/12/2-Ministerial-Decision-No-302-of-2024-on-the-Participation-Exemption-and-Foreign-Permanent-Establishment-Exemption-on-the-Taxation-of-Corporations-and-Businesses-for-publishing_ar.pdf |
| Subject-to-tax rate | 9% | Apply the complete conditions in this country section; this value is not an unconditional bill. | https://mof.gov.ae/wp-content/uploads/2024/12/2-Ministerial-Decision-No-302-of-2024-on-the-Participation-Exemption-and-Foreign-Permanent-Establishment-Exemption-on-the-Taxation-of-Corporations-and-Businesses-for-publishing_ar.pdf |
| Asset test | Not more than 50% | Apply the complete conditions in this country section; this value is not an unconditional bill. | https://mof.gov.ae/wp-content/uploads/2024/12/2-Ministerial-Decision-No-302-of-2024-on-the-Participation-Exemption-and-Foreign-Permanent-Establishment-Exemption-on-the-Taxation-of-Corporations-and-Businesses-for-publishing_ar.pdf |

| Item | Value | Conditions / scope | Official source |
| --- | --- | --- | --- |
| Withholding tax, article 45 | 0% | Apply the complete conditions in this country section; this value is not an unconditional bill. | https://mof.gov.ae/wp-content/uploads/2026/01/Federal-Decree-Law-No.-47-of-2022-and-its-amendments-ar-v13.1.26.pdf |

- Participation exemption: article 23’s ordinary route starts with 5% ownership; the holding/intention must be uninterrupted for at least 12 months, with at least 5% of distributable profits and liquidation proceeds, the specified 9%-similar-tax condition and other exclusions. MD302 article 8’s aggregated acquisition-cost alternative of at least AED 4,000,000 is treated as satisfying BOTH the minimum ownership requirement and the 5% profits/liquidation requirement. Do not incorrectly impose those ownership-rights tests again on that alternative.
- MD302 applies to tax periods beginning on or after 1 January 2025; MD116 remains for earlier periods. The ordinary asset test requires that not more than 50% of the participation’s direct and indirect assets consist of ownership interests that would not qualify for the exemption if held directly; MD302 limits that test to a participation that is a Related Party (article 9), and must be met throughout the period using the permitted consolidated-account or market-value method (article 10).
- The subject-to-tax rules permit specified statutory or effective-rate alternatives; taxes limited to selected activities, refunded on distribution or due only on distribution do not meet the similar-tax test. Qualifying holding-company participations have separate local management, filing, adequate people/premises, ancillary-activity and two-period income conditions; free-zone/exempt participations are separately addressed. An investee country’s headline rate is not the whole test.
- Dividends from a UAE-resident juridical person are exempt under article 22 without proving a foreign participating interest. For foreign interests, gains are exempt only after the applicable holding/acquisition period; failed 12-month conditions can recapture earlier exempt income. Deductible payer distributions and specified prior impairment deductions restrict relief; the 2-year acquisition-exchange rule, liquidation losses and the MD302 cost/repayment/continuity provisions require their own facts.
- Outbound: current article 45, as replaced in 2024 and included in the Ministry’s January 2026 Arabic consolidation, uses 0% withholding for the specified non-resident State-Sourced Income not attributable to a UAE PE or nexus, subject to Cabinet powers. This does not establish a universal absence of corporate tax or the recipient’s home-country tax. The ordinary 0%/9% taxable-income bands and AED 375,000 threshold are separate from free-zone qualifying income, minimum tax and any small-business relief. The retained CD116 English text expressly labels itself an unofficial translation; its ordinary bands and anti-fragmentation scope were personally read, with that limitation retained. [Current Arabic FDL47, articles 3/22–23/45](https://mof.gov.ae/wp-content/uploads/2026/01/Federal-Decree-Law-No.-47-of-2022-and-its-amendments-ar-v13.1.26.pdf); [Arabic MD302/2024](https://mof.gov.ae/wp-content/uploads/2024/12/2-Ministerial-Decision-No-302-of-2024-on-the-Participation-Exemption-and-Foreign-Permanent-Establishment-Exemption-on-the-Taxation-of-Corporations-and-Businesses-for-publishing_ar.pdf); [CD116 threshold decision](https://tax.gov.ae/Datafolder/Files/Legislation/Corporate%20Tax/Cabinet%20Decision%20No.%20116%20of%202022%20-%20for%20publishing.pdf)
- For setting up a UAE company, see `ae-company-formation`.

## United Kingdom

| Item | Value | Conditions / scope | Official source |
| --- | --- | --- | --- |
| Main rate, financial year from 1 April 2026, profits above GBP 250,000 before the limit adjustments below | 25% | Apply the complete conditions in this country section; this value is not an unconditional bill. | https://www.gov.uk/government/publications/rates-and-allowances-corporation-tax/rates-and-allowances-corporation-tax |
| Small profits rate, profits at or below GBP 50,000 before the limit adjustments below | 19% | Apply the complete conditions in this country section; this value is not an unconditional bill. | https://www.gov.uk/government/publications/rates-and-allowances-corporation-tax/rates-and-allowances-corporation-tax |

| Item | Value | Conditions / scope | Official source |
| --- | --- | --- | --- |
| Substantial shareholding | 10% | Apply the complete conditions in this country section; this value is not an unconditional bill. | https://www.gov.uk/hmrc-internal-manuals/capital-gains-manual/cg53072 |

| Item | Value | Conditions / scope | Official source |
| --- | --- | --- | --- |
| Pillar Two revenue threshold, 365-day period | EUR 750 million | Apply the complete conditions in this country section; this value is not an unconditional bill. | https://www.gov.uk/hmrc-internal-manuals/multinational-top-up-tax-and-domestic-top-up-tax/mtt11010 |

- Dividends: a company that is not small is exempt on a distribution that falls into an exempt class in sections 931E to 931I of the Corporation Tax Act 2009, is not a deemed interest distribution, AND is not deductible for any foreign resident ([INTM653010](https://www.gov.uk/hmrc-internal-manuals/international-manual/intm653010)). The exempt classes and anti-avoidance rules are in INTM653000 to INTM654000 and are not reproduced here.
- A small company has its own exemption ([INTM650000](https://www.gov.uk/hmrc-internal-manuals/international-manual/intm650000) lists "Exemption for small companies"), whose current section 931B conditions include a UK/qualifying-territory payer that is not dual-resident, no specified deemed-interest distribution, no foreign deduction and no tax-advantage scheme. “Small” uses section 931S, not merely the 19% profit band; detailed territory/class applications remain outside computation here. [INTM652010](https://www.gov.uk/hmrc-internal-manuals/international-manual/intm652010) The ordinary bands are 19% at profits of GBP 50,000 or less and 25% above GBP 250,000, with Marginal Relief between. For the rate bands, HMRC's [Marginal Relief page](https://www.gov.uk/guidance/corporation-tax-marginal-relief) says the limits are proportionately reduced for accounting periods shorter than 12 months and divided by the number of associated companies plus one, profits include "distributions from unrelated, unassociated companies", and that close investment-holding companies cannot claim Marginal Relief. More strongly, CTM03951 confirms they cannot use the 19% small-profits rate either: they pay the main rate. Not every holding company is a CIHC; a holding/service company in a qualifying trading or commercial unconnected-property-letting group can fall outside it. [CTA2010 section 18N / CTM03951](https://www.gov.uk/hmrc-internal-manuals/company-taxation-manual/ctm03951)
- Gains, substantial shareholdings exemption: the investing company must hold at least 10% of ordinary share capital AND be entitled to at least 10% of distributable profits and of assets on a winding up ([CG53072](https://www.gov.uk/hmrc-internal-manuals/capital-gains-manual/cg53072)), for a continuous period of at least 12 months; for disposals from 1 April 2017 that period may end up to five years before the disposal ([CG53078](https://www.gov.uk/hmrc-internal-manuals/capital-gains-manual/cg53078)). The investee must be a qualifying (trading) company throughout the qualifying period ([CG53106](https://www.gov.uk/hmrc-internal-manuals/capital-gains-manual/cg53106)). Since 1 April 2017 the investing company itself need not be trading.
- Pillar Two: under the cited UK framework the EUR 750 million threshold for a 365-day period must be exceeded in two of the four immediately preceding periods, with a UK member and the specified consolidated group revenue, including excluded entities. Adjust non-365-day periods and test merger/demerger rules separately. This one-line flag does not compute another country’s implementation.
- Outbound ordinary-company dividend withholding: not yet confirmed from an actual current operative official source in this review after targeted recovery; do not enter a zero rate or rank the UK on that basis. Fund/PID evidence is not a substitute for this ordinary-company question.

## Worked hypothetical

Hypothetical facts, not a real client. A family holding company receives a dividend of EUR 1,000,000 from an operating subsidiary and sells a stake at a gain of EUR 5,000,000. The subsidiary is a trading company resident in an EU state with a 15% or higher headline rate, the holding is 30% and has been held for 3 years, and no country's anti-abuse rule is triggered. Because the subsidiary is resident in the EU, not in Malta, and holds no Malta-resident interests, the article 12(1)(u) gains proviso above does not apply. All amounts are before any tax in the shareholder's home country.

| Item | Value | Conditions / scope | Official source |
| --- | --- | --- | --- |
| Hypothetical dividend | EUR 1,000,000 | Hypothetical arithmetic, not a real client; assumptions and gates in the case text. | https://legislation.mt/eli/cap/123/eng/pdf |
| Hypothetical gain | EUR 5,000,000 | Hypothetical arithmetic, not a real client; assumptions and gates in the case text. | https://legislation.mt/eli/cap/123/eng/pdf |

The old result that these facts prove every country’s exemption was too broad. Keep the EUR 1,000,000 dividend, EUR 5,000,000 gain, 30% holding, 3-year ownership, EU residence and 15% headline-rate assumptions unchanged, but obtain the missing facts before entering a nil bill:

| Candidate | Conditional result and facts still needed | Source |
| --- | --- | --- |
| Malta | Exemption can give nil on both items if the defined equity/participating holding, property restrictions, non-deductible EU distribution and remaining anti-abuse conditions hold. EU residence meets one dividend limb, not every prerequisite. | https://legislation.mt/eli/cap/123/eng/pdf |
| Cyprus | Nil corporate dividend/title-gain tax is conditional on classification, no deductible payer dividend and the separate Cyprus-property/SDC facts. A headline rate is not proof of the actual SDC burden comparison. | https://www.cylaw.org/nomoi/enop/non-ind/2002_1_118/full.html ; https://www.cylaw.org/nomoi/enop/non-ind/2002_1_117/full.html |
| Ireland | Nil requires the section 831B accounting-period election, real rights, residence/tax/M&A history and distribution conditions; the disposal needs the independent section 626B tests. Three years of share ownership does not prove all three years of subsidiary status. | https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-35/35-02-11.pdf ; https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-20/20-01-14.pdf |
| Luxembourg | Nil participation tax requires the recipient/investee classes, holding conditions and no recaptured negative income, rolled-over gain or restricted exchange; the acquisition-cost alternatives are not needed if 30% qualifies. | https://impotsdirects.public.lu/dam-assets/fr/legislation/LIR/texte-coordonn-en-vigueur-au-1er-janvier-2026-ver-08052026.pdf ; https://data.legilux.public.lu/eli/etat/leg/rgd/2001/12/21/n5/consolide/20250101/fr/pdf |
| Netherlands | Nil participation tax requires an eligible holder and the purpose/qualifying-portfolio tests; 30% is not the whole exemption. | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/deelnemingsvrijstelling/deelnemingsvrijstelling ; https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/deelnemingsvrijstelling/kwalificerende_beleggingsdeelneming |
| Singapore | Dividend FSIE requires actual/qualifying underlying tax and the beneficial condition, not just a 15% headline. The gain additionally needs section 13W and no overriding section 10L charge; actual Singapore operations/substance have not been supplied. | https://www.iras.gov.sg/media/docs/default-source/e-tax/tax-exemption-for-foreign-sourced-income285e5d43d6af4001b3ce35da1e9005b5.pdf ; https://www.iras.gov.sg/docs/default-source/e-tax/etaxguide_certainty-of-non-taxation-of-companies-gain-on-disposal-of-equity-investments.pdf?sfvrsn=ceb9a99_18 ; https://www.iras.gov.sg/docs/default-source/e-tax/tax-treatment-of-gains-or-losses-from-the-sale-of-foreign-assets.pdf?sfvrsn=a0e0458b_15 |
| UAE | Nil foreign-participation tax requires article 23 plus MD302’s current tax/rights/asset/holding and exclusion tests; the 15% foreign headline by itself does not settle them. | https://mof.gov.ae/wp-content/uploads/2026/01/Federal-Decree-Law-No.-47-of-2022-and-its-amendments-ar-v13.1.26.pdf ; https://mof.gov.ae/wp-content/uploads/2024/12/2-Ministerial-Decision-No-302-of-2024-on-the-Participation-Exemption-and-Foreign-Permanent-Establishment-Exemption-on-the-Taxation-of-Corporations-and-Businesses-for-publishing_ar.pdf |
| UK | Nil requires an actual dividend exempt class or the small-company route and its anti-avoidance gates; the disposal needs all SSE rights/trading/period conditions. | https://www.gov.uk/hmrc-internal-manuals/international-manual/intm653010 ; https://www.gov.uk/hmrc-internal-manuals/capital-gains-manual/cg53072 ; https://www.gov.uk/hmrc-internal-manuals/capital-gains-manual/cg53106 |
| Switzerland | A federal participation REDUCTION is not a full exemption. Net participation income deducts financing and normally 5% administration, so some federal tax can remain. Cantonal tax and the actual costs are unspecified. | https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/1991/1184_1184_1184/20260101/de/pdf-a/fedlex-data-admin-ch-eli-cc-1991-1184_1184_1184-20260101-de-pdf-a.pdf |

Malta, condition fails. Assume instead the subsidiary is outside the EU, all article 12(1)(u) dividend alternatives fail, the receipt is otherwise taxable in the stated amount, no double taxation relief is claimed, and the dividend is paid on to a registered shareholder. Supply that shareholder’s applicable refund eligibility, all article 48(1A)–(1B) compliance conditions and actual tax payment, and assume the case is outside the unresolved Malta-resident-individual exempt-dividend/refund-bar position above. The displayed refund is conditional on those gates.

| Step | Value | Conditions / scope | Official source |
| --- | --- | --- | --- |
| Malta tax at thirty-five cents per euro on the dividend | EUR 350,000 | Hypothetical arithmetic, not a real client; assumptions and gates in the case text. | https://legislation.mt/eli/cap/372/eng/pdf |
| Refund to shareholder at five-sevenths | EUR 250,000 | Hypothetical arithmetic, not a real client; assumptions and gates in the case text. | https://legislation.mt/eli/cap/372/eng/pdf |
| Malta tax left after refund | EUR 100,000 | Hypothetical arithmetic, not a real client; assumptions and gates in the case text. | https://legislation.mt/eli/cap/372/eng/pdf |

Malta refund on trading profit, for contrast. A Malta company with hypothetical trading profit of EUR 100,000 allocated to its Maltese taxed account, distributed to a registered shareholder. Assume the applicable shareholder/refund eligibility and article 48(1A)–(1B) compliance conditions are satisfied, the tax is actually paid and the case is outside the unresolved Malta-resident-individual exempt-dividend/refund-bar position. The displayed refund is conditional on those gates.

| Step | Value | Conditions / scope | Official source |
| --- | --- | --- | --- |
| Hypothetical trading profit | EUR 100,000 | Hypothetical arithmetic, not a real client; assumptions and gates in the case text. | https://legislation.mt/eli/cap/372/eng/pdf |
| Malta tax at thirty-five cents per euro | EUR 35,000 | Hypothetical arithmetic, not a real client; assumptions and gates in the case text. | https://legislation.mt/eli/cap/372/eng/pdf |
| Refund at six-sevenths | EUR 30,000 | Hypothetical arithmetic, not a real client; assumptions and gates in the case text. | https://legislation.mt/eli/cap/372/eng/pdf |
| Malta tax left after refund | EUR 5,000 | Hypothetical arithmetic, not a real client; assumptions and gates in the case text. | https://legislation.mt/eli/cap/372/eng/pdf |

Netherlands, condition fails. Assume the holding is below the ordinary 5% route, no associated-body/other participation extension applies, and it never met the more-than-1-year continuation rule, so the dividend is taxable, and the company has no other income or deductions.

| Step | Value | Conditions / scope | Official source |
| --- | --- | --- | --- |
| First EUR 200,000 at 19.0% | EUR 38,000 | Hypothetical arithmetic, not a real client; assumptions and gates in the case text. | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/tarieven_vennootschapsbelasting |
| Remaining EUR 800,000 at 25.8% | EUR 206,400 | Hypothetical arithmetic, not a real client; assumptions and gates in the case text. | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/tarieven_vennootschapsbelasting |
| Dutch corporate tax on the dividend | EUR 244,400 | Hypothetical arithmetic, not a real client; assumptions and gates in the case text. | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/tarieven_vennootschapsbelasting |

Netherlands, cash out to a Dutch-resident family member. A hypothetical EUR 1,000,000 portfolio dividend paid to a Dutch-resident individual usually carries dividend tax at the rate in the Dutch table, credited against the individual's income tax.

| Step | Value | Conditions / scope | Official source |
| --- | --- | --- | --- |
| Dividend tax withheld at 15% | EUR 150,000 | Hypothetical arithmetic, not a real client; assumptions and gates in the case text. | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/dividendbelasting/als_u_dividend_uitkeert/als_u_dividend_uitkeert |

Cyprus, condition fails. Assume the subsidiary is a non-resident company engaging directly or indirectly more than 50% in investment-income activities and taxed abroad at less than 50% of the Cyprus burden. Assume a current foreign-dividend charge within SDC article 3(1)(c), no deductible-distribution reclassification, and no relief reducing the stated base.

| Step | Value | Conditions / scope | Official source |
| --- | --- | --- | --- |
| SDC at 5% on the dividend | EUR 50,000 | Hypothetical arithmetic, not a real client; assumptions and gates in the case text. | https://www.cylaw.org/nomoi/enop/non-ind/2002_1_117/full.html |

Not computed: Ireland, Luxembourg, Switzerland, Singapore, the UAE and the UK fail cases. Each depends on facts this hypothetical does not fix (trading or non-trading rate in Ireland, commune in Luxembourg, canton in Switzerland, whether a gain is capital in Singapore, the AED threshold in the UAE, the GBP bands and marginal relief in the UK).

## How to choose

- If the family needs cash paid out regularly to individuals, compare the outbound row first: test Singapore’s one-tier treatment and the UAE’s specified current 0% withholding route against the actual receipt and recipient; Malta works through refunds and deducts fifteen per cent on untaxed-account dividends paid to Malta-resident individuals; Ireland, Luxembourg, the Netherlands and Switzerland withhold at the rates in their tables unless an exemption applies; Cyprus’s SDC also has specified resident-company, foreign-dividend, connected foreign-company and transitional profit-year rules.
- If the holding is small or recent, the thresholds decide: Singapore section 13W needs at least 20% for 24 months; Luxembourg needs 10% or a large acquisition price for 12 months; the UK needs 10% for 12 months and a trading investee; Ireland, the Netherlands, Malta and the UAE start at 5%; Cyprus’s statutory dividend/title exemptions state no general minimum ownership or holding period, but the separate SDC and property conditions remain.
- If the subsidiaries are in low-tax or non-EU countries, the subject-to-tax tests decide: Malta's anti-abuse limbs, Singapore's 15% headline test, the UAE's 9% test, Ireland's relevant-territory test, the Netherlands' portfolio participation test and Cyprus's passive-and-low-tax SDC rule.
- If a subsidiary holds property, check the property carve-outs: Ireland 626B (Irish land), Singapore section 13W (property-trading or property-holding investees), Cyprus capital gains tax on property-rich shares.
- Then check the family member's own country (CFC) and where the company is really managed (residence and substance) before deciding. See `cfc-and-substance-rules-compared` and `mt-company-residence-and-substance`.

## Ask the client first

- Where is each family shareholder tax resident and domiciled, and where will they be in five years?
- Where are the operating subsidiaries resident, what headline and actual tax do they pay, and do they trade or mainly hold investments or property?
- What percentage of each subsidiary will the holding own, at what acquisition cost, and since what date?
- Does the family need regular cash dividends, or will profits stay in the holding for reinvestment or a later sale?
- Where will the board meet and who will run the holding day to day?
- Does the group's consolidated revenue come anywhere near the Pillar Two threshold?

## When to refuse or refer

- Refer to a licensed adviser in the chosen country before relying on any exemption: every one has conditions, anti-avoidance rules and filings this Guide summarises but does not reproduce in full.
- Refer if any subsidiary is in a jurisdiction on the EU list of non-cooperative jurisdictions, or in a no-tax or low-tax country: several tests here fail in that case.
- Refer for Swiss cantonal tax, Luxembourg municipal tax outside Luxembourg City, Irish close company surcharges and UK exempt-class detail, which this Guide does not compute.
- Refer the shareholder's home-country position (CFC, exit tax, treaty residence) to an adviser in that country.
- Refuse to treat the comparison table as a recommendation for a specific family without the facts in "Ask the client first".
- Refer Malta-specific questions (refund mechanics, the elective final tax, residence and substance) to `mt-holding-company-participation-exemption` and `mt-company-residence-and-substance`; Malta also has `mt-capital-gains` for sales of shares.

## Worked boundary checks

These checks recompute the retained cases. The Dutch decision test assumes ordinary corporate ownership, no alternative participation route, an eligible holder and all purpose/portfolio conditions met; it does not turn 5% alone into a universal exemption.

```oa-check
name: Malta retained refund cases
inputs:
  failed_dividend: 1000000
  trading_profit: 100000
steps:
  dividend_company_tax: failed_dividend * 0.35
  dividend_refund: dividend_company_tax * 5 / 7
  dividend_net: dividend_company_tax - dividend_refund
  trading_company_tax: trading_profit * 0.35
  trading_refund: trading_company_tax * 6 / 7
  trading_net: trading_company_tax - trading_refund
expected:
  dividend_company_tax: 350000
  dividend_refund: 250000
  dividend_net: 100000
  trading_company_tax: 35000
  trading_refund: 30000
  trading_net: 5000
```

```oa-check
name: Dutch ordinary participation boundary with all other gates satisfied
inputs:
  dividend: 1000000
  holding_below_percent: 4.99
  holding_at_percent: 5
steps:
  below_route: 1 - min(1, max(0, ceil(5 - holding_below_percent)))
  at_route: 1 - min(1, max(0, ceil(5 - holding_at_percent)))
  failed_tax: min(dividend, 200000) * 0.19 + max(0, dividend - 200000) * 0.258
  below_tax: failed_tax * (1 - below_route)
  at_tax: failed_tax * (1 - at_route)
  outbound_portfolio_withholding: dividend * 0.15
expected:
  below_route: 0
  at_route: 1
  failed_tax: 244400
  below_tax: 244400
  at_tax: 0
  outbound_portfolio_withholding: 150000
```

## Sources

All assigned operative conditions and material neighbours below were personally read on 16 November 2026. Source scopes are bounded: an administrative explanation is not a whole current code; the Cyprus Bar and Luxembourg documentary consolidations and the UAE unofficial English threshold translation retain the limitations stated in the country text. Arabic UAE participation and current base-law provisions were also read visually from the actual Ministry PDFs. The per-rule ledger, original snapshots, ordinary failed requests, precise locators and source hashes are retained externally.

| Actual source | Personally read scope and version basis | Read on |
| --- | --- | --- |
| [01](https://legislation.mt/eli/cap/123/eng/pdf) | Read for Cap123 Art56(6), full paragraph and neighbouring company provisions; Art2 equity holding/property company/participating holding definitions, actual200–285/479–640; Art2 participating holding(a), whole489–500; Art2 participating holding(b–d)/(f), whole501–536; Art2 participating holding(e), whole518–525; Art12(1)(u)(1) opening and Art2 participation extension, whole4335–4365/537–579; Art12(1)(u)(1) dividend provisos(i)/(ii), whole; Art12(1)(u) final distribution/list provisos, whole through u(2) opening; pages84–85; Art12(1)(u)(1) domestic-interest provisos and12(1)(c)(ii)/(iii), all operative plus neighbours; Art2FIA/final/untaxeddefinitions;Arts61–66whole and67neighbour | 2026-11-16 |
| [04](https://legislation.mt/eli/cap/372/eng/pdf) | Read for Cap372Art48(1) final bar/1A/1B/2 and48(4)/(4A), whole assigned paragraphs; Art48(4A)(a) standard/passive proviso;48(4)(a)–(c) and4A DTR bar | 2026-11-16 |
| [06](https://legislation.mt/eli/ln/2025/188/eng/pdf) | Read for LN188/2025Regs1–3 all3pages | 2026-11-16 |
| [CY-IT](https://www.cylaw.org/nomoi/enop/non-ind/2002_1_118/full.html) | Read for Law118(I)/2002SecondSchedule2, current through67(I)/2026; actual1689; Art8(20)allprovisos/8(22) andArt2titlesdefinition; actual214/365–368/387 | 2026-11-16 |
| [CY-SDC](https://www.cylaw.org/nomoi/enop/non-ind/2002_1_117/full.html) | Read for Law117(I)/2002Arts2/3(1)(a)allnative116–124 andcurrentdefinitions; Art3(1)(c)whole with3(1)(b)/(d)neighbours; Art3(1)(d)(i)–(v)all+Art2jurisdictiondefs; native139–167; CurrentArt3C(1)–(7)whole258–288 and3(1)(b)whole124–138 | 2026-11-16 |
| [47](https://www.cylaw.org/nomoi/enop/non-ind/1980_1_52/full.html) | Read for CGTLaw52/1980Art2property(i)–(iv)whole64–80,Art4chargewith3/5neighbours | 2026-11-16 |
| [11](https://www.revenue.ie/en/companies-and-charities/corporation-tax-for-companies/corporation-tax/basis-of-charge.aspx) | Read for Revenuebasisofchargewholeoperativecurrent16Oct2026 | 2026-11-16 |
| [41](https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-35/35-02-11.pdf) | Read for TDM35-02-11March2026sections2/4, pp8–10/25–28whole; Sections3.1–3.3wholepp10–20, specifically3.2.3/3.2.4/3.2.6;actual294–706/706–1050; Section3.3wholeand3.4,pp16–24; Section5wholepp28–31and6whole31–32, neighbours; Section7wholepp32–33/8.1–8.3whole33;8.4/8.5onlyopeningneighbour | 2026-11-16 |
| [14](https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-20/20-01-14.pdf) | Read for TDM20-01-14September2026all5pagessections1–4 | 2026-11-16 |
| [43](https://www.revenue.ie/en/companies-and-charities/dividend-withholding-tax/index.aspx) | Read for RevenueDWTcurrent24Aug2026wholeoverview | 2026-11-16 |
| [15](https://www.revenue.ie/en/companies-and-charities/dividend-withholding-tax/exemptions-for-non-residents.aspx) | Read for RevenueExemptionsfornonresidentswholeoperative24Aug2026 | 2026-11-16 |
| [16](https://www.revenue.ie/en/companies-and-charities/corporation-tax-for-companies/corporation-tax/close-companies.aspx) | Read for Revenueclosecompanyoverviewwholecurrent16Oct2026 | 2026-11-16 |
| [17](https://impotsdirects.public.lu/fr/az/t/tarif-applicable-collectivites/tarif-collect.html) | Read for ACDtariffwholeoperative2025onward;LIR174 separatelyread | 2026-11-16 |
| [18](https://impotsdirects.public.lu/fr/az/c/charg_fisc.html) | Read for ACDchargefiscalecollectiviteswhole2025table/notes65–135 | 2026-11-16 |
| [20](https://impotsdirects.public.lu/dam-assets/fr/legislation/LIR/texte-coordonn-en-vigueur-au-1er-janvier-2026-ver-08052026.pdf) | Read for LIR166(1)–(2)whole+recipientannex10/currentcoordinated1Jan2026updated8May; LIR166(2bis)/(3)–(9), wholewith165/167neighbours; LIR147allwith146end/148all;149(1)–(6)actual8140–8173whole,especially4/4a andmaterialneighbours personallyread16Nov19:00UTC | 2026-11-16 |
| [61](https://data.legilux.public.lu/eli/etat/leg/rgd/2001/12/21/n5/consolide/20250101/fr/pdf) | Read for RGD21Dec2001current1Jan2025Art1(1)wholeand2–3neighbours,all2pages; Art1(2)/(2a)/(3)/(4)whole | 2026-11-16 |
| [21](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/tarieven_vennootschapsbelasting) | Read for 2026ratechartwholeoperative | 2026-11-16 |
| [22](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/deelnemingsvrijstelling/deelnemingen) | Read for Deelnemingenwholeoperative65–85 | 2026-11-16 |
| [24](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/deelnemingsvrijstelling/deelnemingsvrijstelling) | Read for Deelnemingsvrijstellingwholeoperative63–68 | 2026-11-16 |
| [25](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/deelnemingsvrijstelling/wanneer_is_een_deelneming_een_beleggingsdeelneming) | Read for Portfolioholdingpurposewholeoperative64–70 | 2026-11-16 |
| [63](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/deelnemingsvrijstelling/kwalificerende_beleggingsdeelneming) | Read for Wholeoperative63–78withtests/lastnegativeconclusion | 2026-11-16 |
| [64](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/deelnemingsvrijstelling/laagbelaste_vrije_beleggingen) | Read for Wholeoperative63–74 | 2026-11-16 |
| [23](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/dividendbelasting/als_u_dividend_uitkeert/als_u_dividend_uitkeert) | Read for Alsudividenduitkeertwholeoperative37–57 | 2026-11-16 |
| [26](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/dividendbelasting/als_u_dividend_uitkeert/deelnemingsdividend-uitkeren-aan-aandeelhouder-buiten-nederland) | Read for Foreignparticipationdividendwholeoperative38–71 | 2026-11-16 |
| [28](https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/1991/1184_1184_1184/20260101/de/pdf-a/fedlex-data-admin-ch-eli-cc-1991-1184_1184_1184-20260101-de-pdf-a.pdf) | Read for DBG68whole;67/69neighbours,current1Jan2026; DBG69whole; DBG70(1)–(3)/(5)/(6)whole; DBG70(4)whole | 2026-11-16 |
| [27](https://www.estv.admin.ch/estv/de/home/verrechnungssteuer.html) | Read for ESTVVerrechnungssteuerwholeoperative44–63 | 2026-11-16 |
| [29](https://www.iras.gov.sg/taxes/corporate-income-tax/basics-of-corporate-income-tax/corporate-income-tax-rate-rebates-and-tax-exemption-schemes) | Read for IRASCITratecurrentwhole990–1009 | 2026-11-16 |
| [31](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/what-is-taxable-what-is-not/dividends) | Read for IRASdividendswholeoperative1000–1047 | 2026-11-16 |
| [30](https://www.iras.gov.sg/media/docs/default-source/e-tax/tax-exemption-for-foreign-sourced-income285e5d43d6af4001b3ce35da1e9005b5.pdf) | Read for IRASFSIE5thed30Jan2026sections5–9allpp4–10with8.2tableandfootnotes | 2026-11-16 |
| [03](https://www.iras.gov.sg/docs/default-source/e-tax/etaxguide_certainty-of-non-taxation-of-companies-gain-on-disposal-of-equity-investments.pdf?sfvrsn=ceb9a99_18) | Read for IRAS4thed30Sep2025sections5.2–7allpp3–10; Section6all/7–8wholewith5.2.7neighbours | 2026-11-16 |
| [54](https://www.iras.gov.sg/docs/default-source/e-tax/tax-treatment-of-gains-or-losses-from-the-sale-of-foreign-assets.pdf?sfvrsn=a0e0458b_15) | Read for IRAS3rded6June2025wholepp1–12sections1–8.18;notIPsection9orcomputationlater | 2026-11-16 |
| [73](https://mof.gov.ae/ar/news/ministry-of-finance-confirms-applicable-taxable-income-threshold-for-corporate-tax-abu-dhabi-uae/) | Read for MoF1Feb2023actualArabicrelease349–361;CD116whole1–5Englishownactualreuse;FDL47Arabic3(1–2)p7 | 2026-11-16 |
| [72](https://mof.gov.ae/wp-content/uploads/2026/01/Federal-Decree-Law-No.-47-of-2022-and-its-amendments-ar-v13.1.26.pdf) | Read for ArabicFDL47Jan2026physical23–26Art22/23all,21/24neighbours; CurrentArabicArt45wholephysical42,44/46and43/47neighbours;amended40/2024cover;28/2025updates44not23 | 2026-11-16 |
| [66](https://mof.gov.ae/wp-content/uploads/2024/12/2-Ministerial-Decision-No-302-of-2024-on-the-Participation-Exemption-and-Foreign-Permanent-Establishment-Exemption-on-the-Taxation-of-Corporations-and-Businesses-for-publishing_ar.pdf) | Read for ArabicMD302all11pages;Art8(1)–(8),Art2ownership and3continuity neighbours; MD302ArabicArts4–10allphysical2–7;English44all13pagesowncrosscheck; MD302ArabicArts11–17wholephysical7–11;allpagesownread | 2026-11-16 |
| [35](https://www.gov.uk/government/publications/rates-and-allowances-corporation-tax/rates-and-allowances-corporation-tax) | Read for HMRCratesandallowances2026tablewhole70–111/125–131 | 2026-11-16 |
| [36](https://www.gov.uk/hmrc-internal-manuals/international-manual/intm653010) | Read for INTM653010wholeoperative67–77/CTA2009Part9A931D | 2026-11-16 |
| [56](https://www.gov.uk/hmrc-internal-manuals/international-manual/intm652010) | Read for INTM652010wholeoperative/931B,definition931S | 2026-11-16 |
| [55](https://www.gov.uk/hmrc-internal-manuals/company-taxation-manual/ctm03951) | Read for CTM03951wholeoperative67–72/CTA201018N | 2026-11-16 |
| [38](https://www.gov.uk/guidance/corporation-tax-marginal-relief) | Read for Marginalreliefwholeoperative75–99 | 2026-11-16 |
| [02](https://www.gov.uk/hmrc-internal-manuals/capital-gains-manual/cg53072) | Read for CG53072wholeoperative67–82/TCGA92Sch7AC8/17 | 2026-11-16 |
| [39](https://www.gov.uk/hmrc-internal-manuals/capital-gains-manual/cg53078) | Read for CG53078wholeoperative67–77/Sch7AC7 | 2026-11-16 |
| [40](https://www.gov.uk/hmrc-internal-manuals/capital-gains-manual/cg53106) | Read for CG53106wholeoperative68–83/Sch7AC18 | 2026-11-16 |
| [05](https://www.gov.uk/hmrc-internal-manuals/multinational-top-up-tax-and-domestic-top-up-tax/mtt11010) | Read for MTT11010wholeoperative67–132 | 2026-11-16 |

**Not yet confirmed:**
- UK ordinary-company outbound dividend withholding: the previous Guide had no printed official rate. Current ordinary-source recovery here did not establish its precise operative rule. Do not substitute a zero rate or the rules for funds/property-income distributions.
- Cyprus titles: the actual statute covers defined titles and rights. The former detailed list of options, futures, swaps and collective-investment units was on an inaccessible Tax Department page; product-specific inclusion is not confirmed by that unavailable page. Classify the actual instrument before applying article 8(22).
- Cyprus treaties: the old statement that a treaty with a 50% property-value threshold overrides the domestic 20% test is not a universal treaty promise. Identify the actual treaty, covered person, date and article before a treaty computation.
- Malta resident individual refunds and a specific exempt-participation distribution’s account allocation: the statutory definitions and refund bars are stated above, but the full personal/account computation is not established here. No automatic refund is promised to that shareholder.
- UK small-company qualifying-territory/exempt-class and anti-avoidance applications beyond the stated manual scope require their actual provisions and transaction facts; do not infer an exemption from the class name or a 19% rate alone.
- Ireland close-company surcharges, Swiss cantonal tax, Luxembourg communes outside Luxembourg City and the original uncomputed failure cases for Ireland/Luxembourg/Switzerland/Singapore/UAE/UK require their own tax-base and local facts. Their omission from arithmetic is explicit, not a nil result.
- Luxembourg future-commitment withholding relief: the underlying article 149(4) guarantee regulation and actual form/procedure implementation are not established here; no automatic advance relief is promised.
- The original empirical assertion that family groups rarely reach Pillar Two was not supported by an operative source and is not a legal safe harbour. Apply the actual group test.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-16. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `family-holding-company-location-compared` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/family-holding-company-location-compared. If neither is available, confirm every figure against the official source pages cited above before relying on it.
