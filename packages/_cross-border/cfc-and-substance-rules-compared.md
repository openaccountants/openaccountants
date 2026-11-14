---
name: cfc-and-substance-rules-compared
description: "Will a family's home country tax its foreign holding company anyway? Compares controlled foreign company (CFC) and substance rules for family holding structures in tax year 2026. Covers the EU anti-tax-avoidance CFC rules as Malta, Ireland, Cyprus, the Netherlands and Luxembourg apply them (companies only, control and low-tax tests, carve-outs, significant people functions), the UK CFC gateway and exemptions, US subpart F and net CFC tested income for US-person families, and what Switzerland, Singapore and the UAE print, with a worked case for a UK individual, a Malta company and a US citizen owner."
version: "1.0"
jurisdiction: GLOBAL
category: international
type: cross-country-method
tax_year: 2026
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: cross-border
---

# Will the family's home country tax the holding company anyway? CFC and substance rules compared v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope and who this is for

Tax year 2026. This skill answers one question a family's adviser asks before choosing where a holding company sits: if the family lives in country X and the holding company sits in country Y, will X tax the holding company's income anyway? It covers the controlled foreign company (CFC) rules of Malta, Ireland, Cyprus, the Netherlands, Luxembourg, the United Kingdom and the United States, and what the official pages of Switzerland, Singapore and the United Arab Emirates print on the same point. For each country it says who is caught (companies only, or individuals too), the control threshold, the low-tax test, which income is attributed, the carve-outs, and the year the rule applies from. Every figure sits in a table row that carries its official URL. Where an official page read does not print a rule, the skill says "not printed on an official page read". Pages were read on 14 November 2026.

The most common mistake is to assume a CFC rule reaches the family members themselves. In the five EU countries covered here, and in the UK, the CFC charge falls on a company (or a body taxed like a company), not on an individual. A family of individuals who own the holding company directly is usually outside those CFC rules. Other rules may still tax the individuals; this skill names only the UK one (transfer of assets abroad) and does not cover the others. The United States is different: its rules reach a US person, including an individual US citizen, who is a "United States shareholder".

Out of scope: where the holding company itself is resident, its participation exemption, and how its dividends are taxed on the way out. For those, see `family-holding-company-location-compared`, `mt-company-residence-and-substance` and `mt-holding-company-participation-exemption`. For the US computations, see `us-gilti-fdii-beat` (subpart F, net CFC tested income and the corporate deduction) and `us-form-5471-cfc-information` (Form 5471); this skill does not repeat them. For a family member changing country of residence, see `family-office-residency-regimes-compared`.

## Ask the client first

- Who exactly owns the holding company: individuals, companies, trusts or foundations, and in which country is each tax resident? Is any family member a US citizen or green card holder?
- Where are the holding company's decisions on its assets and risks actually taken, and by whom? Does it have its own staff, premises and operating costs?
- What does the holding company earn: dividends from trading subsidiaries, interest, royalties, portfolio income, gains? How much, and how much is distributed each year?
- What tax does the holding company actually pay in its own country, and on which profits?
- Is the holding company's country on the EU list of non-cooperative jurisdictions, or on the Netherlands' designated list for the year?
- Is any family member planning to move country in the next few years? A move can bring a CFC rule into play for the first time.

## The method, step by step

1. List every shareholder of the holding company, direct and indirect, with its residence and its legal form (individual, company, trust or foundation). The CFC rules below turn first on WHO the shareholder is: for example, Ireland's charge "can only arise to companies" ([Tax and Duty Manual Part 35B-01-01](https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-35b/35b-01-01.pdf)). Use the questions in "Ask the client first".
2. For each shareholder that is a company resident in Malta, Ireland, Cyprus, the Netherlands or Luxembourg, apply that country's control test and low-tax test from its section below. Each test is in that country's law: for Malta, regulation 7 of [S.L. 123.187](https://legislation.mt/eli/sl/123.187/eng/pdf).
3. If the holding company is a CFC, test the carve-outs (profit size, profit margin, effective tax rate, substantial economic activity) before computing anything. A carve-out that applies ends the inquiry for that period. For Cyprus they are in article 36A of the [Income Tax Law](https://www.gov.cy/media/sites/167/2026/01/IT118I-2002.pdf); for Luxembourg in article 164ter of the [L.I.R.](https://impotsdirects.public.lu/dam-assets/fr/legislation/LIR/texte-coordonn-en-vigueur-au-1er-janvier-2026-ver-08052026.pdf).
4. If no carve-out applies, find the income that is attributed. In Malta, Ireland, Cyprus and Luxembourg that is only undistributed income from "non-genuine arrangements", limited to income linked to significant people functions carried out by the controlling company (in Malta and Ireland, the law requires those functions to be in that country). In the Netherlands it is listed categories of passive income ("besmette voordelen"), unless the CFC carries on a substantial economic activity ([Wet op de vennootschapsbelasting 1969, article 13ab](https://wetten.overheid.nl/BWBR0002672/2026-01-01)).
5. For a UK-resident company shareholder, apply the UK gateway and the five entity-level exemptions ([INTM191100](https://www.gov.uk/hmrc-internal-manuals/international-manual/intm191100)). For a UK-resident individual, the CFC charge does not apply (see the UK section) but refer the transfer of assets abroad rules to a UK adviser.
6. For any US person (citizen, green card holder or US resident, and US entities), test "United States shareholder" under [26 U.S.C. 951(b)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partIII-subpartF-sec951.htm) and "controlled foreign corporation" under [26 U.S.C. 957](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partIII-subpartF-sec957.htm), apply the 2026 ownership change in [Public Law 119-21](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) (see the US section), then go to `us-gilti-fdii-beat` for subpart F and net CFC tested income and to `us-form-5471-cfc-information` for the information return.
7. For a holding company in Switzerland, Singapore or the UAE, do not assume those countries tax foreign subsidiaries of their own companies under a CFC rule; the pages read for this skill print none, and that is not a statement that none exists. Check instead the substance the holding company itself needs to keep its own regime, for example a UAE Qualifying Free Zone Person under article 18 of [Federal Decree-Law No. 47 of 2022](https://tax.gov.ae/Datafolder/Files/Legislation/Corporate%20Tax/CT%20law%20final/Federal%20Decree-Law%20No.%2047%20of%202022%20-%20For%20publishing.pdf).
8. Run the worked case with the client's own numbers and record which condition each answer depends on, starting from the Malta carve-outs in regulation 7(3) of [S.L. 123.187](https://legislation.mt/eli/sl/123.187/eng/pdf).

### Comparison at a glance

Each entry in this table is repeated from a sourced country table further down. Read the country section before relying on a row.

| Country of the shareholder | Who is caught | Control test | Low-tax test | What is attributed | Main carve-outs |
| --- | --- | --- | --- | --- | --- |
| Malta | Companies and entities taxed as companies (reg. 2(2)); not individuals | More than 50% of votes, capital or profits, with associated enterprises | Actual tax lower than the difference between Malta tax and the actual tax | Undistributed income from non-genuine arrangements, limited to significant people functions in Malta | EUR 750,000 profits and EUR 75,000 non-trading income; or profits no more than 10% of operating costs |
| Ireland | Companies only ("chargeable companies") | More than 50% (share capital, votes, distributions or assets) | Effective tax rate exemption if the CFC's tax is at least half the Irish tax | Undistributed income from non-genuine arrangements, linked to Irish significant people functions | EUR 750,000 / EUR 75,000; EUR 75,000 profits; profits less than 10% of relevant operating costs; effective tax rate; exempt period (the low profit, low margin and effective tax rate exemptions are not available for CFCs in EU-listed non-cooperative jurisdictions) |
| Cyprus | Cyprus-resident companies | More than 50% of votes, capital or profits, with associated enterprises | Actual tax lower than 50% of the Cyprus tax | Undistributed income from non-genuine arrangements, limited to significant people functions in Cyprus | EUR 750,000 and EUR 75,000; or profits no more than 10% of operating costs |
| Netherlands | Corporate income taxpayers | More than 50% of capital, OR of votes, OR of profits | Designated state: no profit tax or a rate below 9%, or on the EU non-cooperative list | Listed passive categories ("besmette voordelen") | Mainly non-tainted income; substantial economic activity |
| Luxembourg | Corporate taxpayers (article 159 bodies and Luxembourg permanent establishments) | More than 50% of votes, capital or profits | Actual tax lower than the difference between Luxembourg corporate tax and the actual tax | Undistributed income from non-genuine arrangements, limited to important functions of the controlling taxpayer | EUR 750,000 profit; or profit no more than 10% of operating costs |
| United Kingdom | UK-resident companies with at least a 25% share ("chargeable companies"); not individuals | Legal, economic or accounting control by UK persons | Tax exemption if local tax is 75% or more of the corresponding UK tax | Chargeable profits that pass through the gateway | Exempt period; excluded territories; low profits (GBP 500,000, GBP 50,000 non-trading); low profit margin (10%); tax exemption |
| United States | US persons owning 10% or more of vote or value, including individuals | More than 50% of vote or value owned by United States shareholders | No low-tax test in the definition (see `us-gilti-fdii-beat`) | Subpart F income and net CFC tested income | See `us-gilti-fdii-beat` |
| Switzerland | Not printed on an official page read | Not printed on an official page read | Not printed on an official page read | Not printed on an official page read | Not printed on an official page read |
| Singapore | Not printed on an official page read | Not printed on an official page read | Not printed on an official page read | Not printed on an official page read | Not printed on an official page read |
| UAE | No CFC rule printed in the Corporate Tax Law or General Guide read; Free Zone substance applies to the UAE company itself | n/a | n/a | n/a | n/a |

## Malta

| Item | Value | Note (verbatim from the page) | Source |
| --- | --- | --- | --- |
| Control threshold, reg. 7(1)(a) | 50% | "participation of more than fifty per cent (50%) of the voting rights" | https://legislation.mt/eli/sl/123.187/eng/pdf |
| Carve-out (a): accounting profits, reg. 7(3)(a) | EUR 750,000 | "no more than seven hundred and fifty thousand euro (€750,000)" | same |
| Carve-out (a): non-trading income, reg. 7(3)(a) | EUR 75,000 | "non-trading income of no more than seventy-five thousand euro (€75,000)" | same |
| Carve-out (b): profits against operating costs, reg. 7(3)(b) | 10% | "of which the accounting profits amount to no more than ten per cent (10%) of its operating costs" | same |
| Associated enterprise threshold, reg. 3 | 25% | "twenty- five per cent (25%) or more of the profits of that entity" | same |

Rules, from the European Union Anti-Tax Avoidance Directives Implementation Regulations, [S.L. 123.187](https://legislation.mt/eli/sl/123.187/eng/pdf) (L.N. 411 of 2018, in force from 1 January 2019, amended by L.N. 348 of 2019 and L.N. 29 of 2020):

- WHO: the regulations apply "to all companies as well as other entities, trusts and similar arrangements that are subject to tax in Malta in the same manner as companies", including non-residents with a Malta permanent establishment taxed as companies (reg. 2(2)). A Malta-resident individual who owns a foreign company directly is not a "taxpayer" under these regulations.
- CONTROL AND LOW TAX, BOTH required (AND): (a) the Malta taxpayer, alone or with its associated enterprises, holds directly or indirectly more than the 50% in the table of the voting rights, OR owns more than 50% of the capital, OR is entitled to more than 50% of the profits; AND (b) "the actual corporate tax paid on its profits by the entity or permanent establishment is lower than the difference between the tax that would have been charged on the entity or permanent establishment under the Income Tax Acts and the actual corporate tax paid". The Malta tax for this comparison is computed under the Income Tax Acts.
- WHAT IS ATTRIBUTED (model B, non-genuine arrangements): the CFC's "non-distributed income ... arising from non-genuine arrangements which have been put in place for the essential purpose of obtaining a tax advantage" (reg. 7(2)). An arrangement is non-genuine to the extent the CFC would not own the assets or bear the risks "if it were not controlled by a company where the significant people functions, which are relevant to those assets and risks, are carried out and are instrumental in generating the controlled company's income: Provided that the said company is the taxpayer and the said significant people functions are carried out in Malta." If those functions are not carried out in Malta, nothing is attributed.
- CARVE-OUTS (OR): reg. 7(2) does not apply to a CFC with accounting profits no more than the EUR 750,000 in the table AND non-trading income no more than EUR 75,000; OR whose accounting profits are no more than the 10% in the table of its operating costs for the tax period. Operating costs exclude the cost of goods sold outside the CFC's country and payments to associated enterprises.
- COMPUTATION (reg. 8): income is limited to amounts generated through assets and risks linked to significant people functions carried out by the controlling company, priced at arm's length; it is included in proportion to the taxpayer's participation; it is included in the tax period in which the CFC's tax year ends; it is deducted again when a later distribution is included in the taxpayer's taxable income, or when the participation is sold, to avoid double taxation; and a credit is given for the CFC's tax under articles 77 and 82 of the Income Tax Act.
- For whether the Malta holding company is itself resident and has substance, see `mt-company-residence-and-substance`.

## Ireland

| Item | Value | Note (verbatim from the page) | Source |
| --- | --- | --- | --- |
| Control: share of distributions | 50 per cent | "more than 50 per cent of the distribution" | https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-35b/35b-01-01.pdf |
| Low accounting profit exemption: profits | EUR 750,000 | "a CFC with accounting profits of less than €750,000 where any non- trading income stream amounts to less than €75,000" | same |
| Low accounting profit exemption: profits only | EUR 75,000 | "a CFC with accounting profits of less than €75,000." | same |
| Low profit margin exemption | 10% | "10% of its relevant operating costs for the relevant period" | same |

Rules, from Revenue's Tax and Duty Manual Part 35B-01-01 (document last updated January 2025), on sections 835I to 835YA of the Taxes Consolidation Act:

- WHEN: "The rules came into effect from 1 January 2019." Part 35B implements the ATAD articles on CFCs.
- WHO: "The CFC charge can only arise to companies (known as ‘chargeable companies’)." The control rules count all shareholders, companies and individuals, but an individual is never charged.
- WHEN A CHARGE ARISES, ALL of these: a CFC resident in a foreign territory; controlled by a company resident in the State; the controlling company or a connected company carries out relevant Irish activities (significant people functions or key entrepreneurial risk-taking functions) relating to the CFC's assets or risks; the arrangements are non-genuine and in place for the essential purpose of securing a tax advantage; Irish transfer pricing has not applied or the arrangements are not at arm's length; AND no exemption applies.
- CONTROL: in broad terms more than 50% of issued share capital, voting power or the distribution amount (the table above prints the distribution limb), or of assets on a winding up, or the power to control the board.
- EXEMPTIONS (any one is enough): low accounting profit (the EUR 750,000 / EUR 75,000 test in the table, or accounting profits below EUR 75,000), reduced proportionately for a period shorter than 12 months; low profit margin (profits below 10% of relevant operating costs); effective tax rate ("the tax paid by the CFC on its profits ... is at least half of the tax that would have been paid by the CFC if it were an Irish resident company"); and a one-year grace period for newly acquired CFCs where certain conditions apply. The manual states the low profit, low margin and effective tax rate exemptions "will not be available to CFCs resident in a jurisdiction listed on the EU list of non-cooperative jurisdictions for tax purposes" (section 835YA).

## Cyprus

| Item | Value | Note (verbatim from the page) | Source |
| --- | --- | --- | --- |
| Control threshold, article 36A(1)(a) | 50% | "συμμετοχή σε ποσοστό άνω του πενήντα τοις εκατό (50%) των δικαιωμάτων ψήφου" | https://www.gov.cy/media/sites/167/2026/01/IT118I-2002.pdf |
| Low-tax test, article 36A(1)(b) | 50% | "είναι χαμηλότερος του πενήντα τοις εκατό (50%) του φόρου που θα επιβαλλόταν" | same |
| Carve-out (a): accounting profits | EUR 750,000 | "Λογιστικά κέρδη που δεν υπερβαίνουν τις επτακόσιες πενήντα χιλιάδες ευρώ (€750.000)" | same |
| Carve-out (a): non-trading income | EUR 75,000 | "που δεν υπερβαίνει τις εβδομήντα πέντε χιλιάδες ευρώ (€75.000)" | same |
| Carve-out (b): profits against operating expenses | 10% | "λογιστικά κέρδη που δεν υπερβαίνουν το δέκα τοις εκατό (10%) των δαπανών λειτουργίας" | same |

Rules, from article 36A of the Income Tax Law, N. 118(I)/2002, in the Tax Department's consolidated text (its latest amending law shown is N. 219(I)/2025). The margin note reads "Ισχύει από 1/1/2019" (in force from 1 January 2019). The consolidated text read does not include the 2026 amending law N. 244(I)/2025; whether that law touches article 36A, or articles 35 and 36 named below, is on the "Not yet confirmed:" line under Sources.

- WHO: a non-resident company, or a foreign permanent establishment of a Cyprus-resident company, is a CFC in relation to "εταιρεία κάτοικος της Δημοκρατίας" (a company resident in the Republic). The attributed income is added to the taxable income of that resident company. An individual shareholder is not named in article 36A.
- CONTROL AND LOW TAX, BOTH required (AND): the Cyprus-resident company, alone or with associated enterprises, holds more than the 50% in the table of the votes, OR of the capital, OR is entitled to more than 50% of the profits; AND the actual corporate tax paid by the foreign company is lower than 50% of the tax that would be charged if the profits were taxed in Cyprus, computed under the Cyprus law.
- WHAT IS ATTRIBUTED: the undistributed income from non-genuine arrangements put in place for the essential purpose of obtaining a tax advantage. Undistributed income is the after-tax accounting profit not distributed during the tax year and the following seven months; the foreign tax is added back before inclusion. The inclusion is limited to amounts generated through assets and risks linked to the functions of significant people ("σημαινόντων στελεχών") carried out in the Cyprus-resident company, at arm's length.
- CARVE-OUTS (OR): accounting profits no more than the EUR 750,000 in the table AND non-trading income no more than EUR 75,000; OR accounting profits no more than the 10% in the table of operating expenses for the tax period. Operating expenses exclude the cost of goods sold outside the CFC's country and payments to associated enterprises (article 36A(4)).
- RELIEF: amounts already included are deducted when profits later distributed are included in the Cyprus company's taxable income and not exempt under article 8, or when the holding is sold, and foreign tax is credited under articles 35 and 36.

## Netherlands

| Item | Value | Note (verbatim from the page) | Source |
| --- | --- | --- | --- |
| Control threshold, article 13ab(3)(a) | 50% | "van meer dan 50% van de aandelen in het nominaal gestorte kapitaal" | https://wetten.overheid.nl/BWBR0002672/2026-01-01 |
| Low-tax state: profit tax rate, article 13ab(3)(d) | 9% | "niet of naar een tarief van minder dan 9% onderwerpt aan een belasting naar de winst" | same |
| Associated body or individual, article 13ab(10) | 25% | "ten minste 25% bedraagt van de aandelen in het nominaal gestorte kapitaal" | same |

Rules, from article 13ab of the Corporate Income Tax Act 1969 (text valid on 1 January 2026) and the Belastingdienst page [Voordelen uit een gecontroleerd lichaam](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/voordelen-uit-een-gecontroleerd-lichaam):

- WHO: the rule sits in the Corporate Income Tax Act and adds the CFC income to the "winst" of the corporate taxpayer ("belastingplichtige"). The controlling interest may be held together with an associated body or an associated individual ("gelieerde natuurlijk persoon"), but the inclusion is made by the corporate taxpayer.
- CONTROL: more than the 50% in the table of the paid-up nominal capital, OR more than 50% of the statutory voting rights, OR an interest entitled to more than 50% of the profit.
- LOW TAX: the body must be established in a state designated by ministerial regulation that, on 1 October of the preceding calendar year, levies no profit tax or one at a rate below the 9% in the table, OR was on the EU list of non-cooperative jurisdictions in the preceding calendar year. A body that is subject to profit tax as a resident of another, non-designated state is not a CFC. The Belastingdienst page links the yearly lists ("Overzicht laagbelastende staten 2026").
- WHAT IS ATTRIBUTED (model A, categories): the CFC's tainted income of the year, less related costs: interest and other income from financial assets; royalties and other income from intangible assets; dividends and gains on shares; financial leasing; insurance, banking or other financial activities; and low or no value-adding invoicing with related parties. Only a positive balance not distributed before the end of the year is included, in proportion to the interest and the time held. A negative balance is carried forward against the next six years.
- CARVE-OUTS: no CFC if its income usually consists mainly of income other than tainted income, or for a qualifying financial undertaking whose tainted income comes mainly from unrelated parties (article 13ab(4)); AND article 13ab(1) does not apply if the CFC carries on a substantial economic activity ("een wezenlijke economische activiteit", article 13ab(5)). Conditions set by ministerial regulation create a presumption of substance, which the inspector may rebut; otherwise the taxpayer must show it.
- The start year of article 13ab is not printed in the text read.

## Luxembourg

| Item | Value | Note (verbatim from the page) | Source |
| --- | --- | --- | --- |
| Control threshold, article 164ter(1) | 50 pour cent | "plus de 50 pour cent des droits de vote" | https://impotsdirects.public.lu/dam-assets/fr/legislation/LIR/texte-coordonn-en-vigueur-au-1er-janvier-2026-ver-08052026.pdf |
| Carve-out (a): commercial balance sheet profit | EUR 750,000 | "qui n’est pas supérieur à 750 000 euros" | same |
| Carve-out (b): profit against operating costs | 10 pour cent | "qui ne dépasse pas 10 pour cent des coûts de fonctionnement" | same |
| Associated enterprise threshold, article 164ter(2) | 25 pour cent | "une participation de 25 pour cent ou plus des droits de vote ou du capital" | same |

Rules, from article 164ter of the income tax law (L.I.R.), coordinated text in force on 1 January 2026. The margin note cites the laws of 21 December 2018 and 20 December 2019 ("L.21.12.18,2,1° - L.20.12.19,2,1°").

- WHO: "Par contribuable, il y a lieu d’entendre aux fins du présent article un organisme visé par l’article 159 ou un établissement stable indigène d’un organisme visé par l’article 160". Article 159 covers resident collective bodies (companies). An individual is not a "contribuable" for this article.
- CONTROL AND LOW TAX, BOTH required ("simultanément remplies"): the taxpayer, alone or with associated enterprises, holds more than the 50 pour cent in the table of the votes, OR of the capital, OR is entitled to more than 50 pour cent of the profits; AND the actual tax paid by the foreign body is lower than the difference between the Luxembourg corporate income tax it would have borne and that actual tax.
- CARVE-OUTS (OR): a CFC whose commercial balance sheet profit is no more than the EUR 750,000 in the table, OR no more than 10 pour cent of its operating costs. Unlike Malta, Cyprus and Ireland, the text prints no separate non-trading income limit for carve-out (a).
- WHAT IS ATTRIBUTED (model B): the net income of the year not distributed to the taxpayer during the same year "et qui proviennent de montages non authentiques mis en place essentiellement dans le but d’obtenir un avantage fiscal", limited to amounts generated by assets and risks linked to the important functions ("fonctions importantes") carried out by the controlling taxpayer, at arm's length, pro rata to the participation, taxed in the year in which the CFC's financial year ends. A negative total is not included but may be carried forward against later positive inclusions.

## United Kingdom

| Item | Value | Note (verbatim from the page) | Source |
| --- | --- | --- | --- |
| Interest held by a UK interest holder, with connected companies | 25% | "together with connected companies) holds an interest of at least 25%" | https://www.gov.uk/hmrc-internal-manuals/international-manual/intm191100 |
| Joint venture CFC: UK resident company's share (only where a non-UK resident person also controls the CFC, within the range on the page) | 40% | "one of those persons is a UK resident company that controls at least 40%" | same |
| Low profits exemption: profits | GBP 500,000 | "assumed taxable total profits are no more than £500,000, and the amount of those profits that are non-trading income is no more than £50,000" | https://www.gov.uk/hmrc-internal-manuals/international-manual/intm225550 |
| Low profits exemption: non-trading income | GBP 50,000 | "non-trading income is no more than £50,000" | same |
| Low profit margin exemption | 10 per cent | "no more than 10 per cent of the CFC’s relevant operating expenditure" | https://www.gov.uk/hmrc-internal-manuals/international-manual/intm225800 |
| Tax exemption: local tax against corresponding UK tax | 75% | "if the local tax amount in step 2 is 75% or more of the corresponding UK tax in step 3" | https://www.gov.uk/hmrc-internal-manuals/international-manual/intm226100 |

Rules, from HMRC's International Manual. The guidance applies "for accounting periods of CFCs starting on or after 1 January 2013" under Part 9A of the Taxation (International and Other Provisions) Act 2010 ([INTM190000](https://www.gov.uk/hmrc-internal-manuals/international-manual/intm190000)).

- WHAT IS A CFC: "The CFC regime applies to companies resident outside the UK that are controlled by UK residents." Control can be legal, economic or by accounting standards ([INTM191100](https://www.gov.uk/hmrc-internal-manuals/international-manual/intm191100); [INTM236000](https://www.gov.uk/hmrc-internal-manuals/international-manual/intm236000)).
- WHEN A CHARGE ARISES, ALL of these ("if (and only if)"): the CFC has chargeable profits; none of the CFC exemptions applies; AND there is a UK interest holder that is not exempt and that, with connected companies, holds an interest of at least the 25% in the table.
- WHO IS CHARGED: the charge is restricted "to UK resident companies" that meet section 371BD; a UK resident company is a chargeable company only to the extent that the profits apportioned to it and to connected or associated persons "(whether corporate or individual)" reach 25% of the CFC's chargeable profits ([INTM194500](https://www.gov.uk/hmrc-internal-manuals/international-manual/intm194500)). An individual is counted in that test but is not a chargeable company. HMRC's manual has a separate chapter, Transfer of assets abroad ([INTM600000](https://www.gov.uk/hmrc-internal-manuals/international-manual/intm600000)), with an "income charge" and a "benefits charge"; it is not covered here.
- GATEWAY: chargeable profits are the profits that pass through the "CFC charge gateway" in Chapters 3 to 9 of Part 9A. Chapter 4 (profits attributable to UK activities) applies "unless any one or more of four conditions (A to D) is met", and HMRC says it will bring overseas trading profits into charge "in relatively few circumstances" ([INTM197200](https://www.gov.uk/hmrc-internal-manuals/international-manual/intm197200)). Other gateway chapters cover non-trading finance profits, trading finance profits, captive insurance and solo consolidation ([INTM190000](https://www.gov.uk/hmrc-internal-manuals/international-manual/intm190000)).
- ENTITY EXEMPTIONS, any one is enough ([INTM224000](https://www.gov.uk/hmrc-internal-manuals/international-manual/intm224000)): the exempt period (CFCs under UK control for the first time, "usually 12 months"); excluded territories; low profits (the GBP 500,000 and GBP 50,000 limits in the table: accounting profits OR assumed taxable total profits no more than GBP 500,000, AND non-trading income no more than GBP 50,000); low profit margin (accounting profits before interest no more than 10 per cent of relevant operating expenditure); and the tax exemption (local tax 75% or more of the corresponding UK tax). The tax exemption cannot apply where the CFC has no territory of residence under the general rule, which "will normally apply to CFCs that are incorporated in a tax shelter where there is no liability to tax" ([INTM226100](https://www.gov.uk/hmrc-internal-manuals/international-manual/intm226100)).

## United States

| Item | Value | Note (verbatim from the page) | Source |
| --- | --- | --- | --- |
| United States shareholder: vote or value, 26 U.S.C. 951(b) | 10 percent or more | "10 percent or more of the total combined voting power of all classes of stock entitled to vote" | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partIII-subpartF-sec951.htm |
| Controlled foreign corporation: ownership by United States shareholders, 26 U.S.C. 957(a) | more than 50 percent | "any foreign corporation if more than 50 percent of" | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partIII-subpartF-sec957.htm |

- WHO: a "United States shareholder" is a United States person (as defined in section 957(c)) owning, directly, indirectly or constructively, 10 percent or more of the total voting power OR 10 percent or more of the total value of the foreign corporation's shares (section 951(b)). A US citizen is a US person wherever the citizen lives, so an individual US citizen in the family can be caught. That is the main difference from the EU and UK rules above.
- CFC: a foreign corporation is a controlled foreign corporation if more than 50 percent of the total combined voting power, OR of the total value of its stock, is owned (within the meaning of section 958) by United States shareholders on any day during its taxable year (section 957(a)).
- 2026 CHANGE TO OWNERSHIP: Public Law 119-21, section 70353, restores section 958(b)(4), so that section 318(a)(3)(A), (B) and (C) "shall not be applied so as to consider a United States person as owning stock which is owned by a person who is not a United States person", for "taxable years of foreign corporations beginning after December 31, 2025". The same section adds section 951B for foreign controlled United States shareholders. Apply the 2026 rule when counting constructive ownership; the computation sits in `us-gilti-fdii-beat`.
- WHAT IS INCLUDED: each United States shareholder includes its share of subpart F income (section 951(a)) and its "net CFC tested income" (section 951A(a)). Public Law 119-21, section 70323(a)(1), struck "global intangible low-taxed income" from section 951A(a) and inserted "net CFC tested income", and section 70323(c) applies the change "to taxable years beginning after December 31, 2025" ([Public Law 119-21](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm)).
- For the computations, elections and the corporate deduction, use `us-gilti-fdii-beat`; for Form 5471, use `us-form-5471-cfc-information`. This skill does not repeat them.

## Switzerland, Singapore and the United Arab Emirates

Switzerland. Not printed on an official page read. The Federal Direct Tax Act (DBG) text and the ESTV pages read for the sibling skill `family-holding-company-location-compared` do not state whether Switzerland taxes a Swiss company on the income of a controlled foreign subsidiary. Do not state that Switzerland has, or lacks, a CFC rule on the strength of this skill.

Singapore. Not printed on an official page read. No IRAS page read for this skill states whether Singapore has a CFC regime, and the IRAS guidance on section 10L (gains from the sale of foreign assets) could not be located on iras.gov.sg on 4 October 2026 (not searched again on 14 November 2026). What IRAS does print is the foreign-sourced income exemption for foreign dividends, foreign branch profits and foreign service income "received in Singapore" by specified resident taxpayers: exempt only if the "subject to tax" condition, the foreign headline tax rate condition and the "beneficial tax exemption" condition are ALL met ([FSIE e-Tax Guide](https://www.iras.gov.sg/media/docs/default-source/e-tax/tax-exemption-for-foreign-sourced-income285e5d43d6af4001b3ce35da1e9005b5.pdf)). The headline rate in that condition is in the table below. See `family-holding-company-location-compared` for its table.

| Item | Value | Note (verbatim from the page) | Source |
| --- | --- | --- | --- |
| Foreign headline tax rate condition | 15% | "Foreign headline tax rate of at least 15%” condition" | https://www.iras.gov.sg/media/docs/default-source/e-tax/tax-exemption-for-foreign-sourced-income285e5d43d6af4001b3ce35da1e9005b5.pdf |

United Arab Emirates. A search of the Corporate Tax Law and the FTA's General Corporate Tax Guide read for this skill found no rule that taxes a UAE person on the undistributed income of a controlled foreign company. The substance test the UAE prints applies to a UAE Free Zone company itself, to keep the Free Zone rate.

| Item | Value | Note (verbatim from the page) | Source |
| --- | --- | --- | --- |
| Qualifying Free Zone Person, Qualifying Income, article 3(2)(a) | 0% | "a. 0% (zero percent) on Qualifying Income." | https://tax.gov.ae/Datafolder/Files/Legislation/Corporate%20Tax/CT%20law%20final/Federal%20Decree-Law%20No.%2047%20of%202022%20-%20For%20publishing.pdf |
| Qualifying Free Zone Person, other taxable income, article 3(2)(b) | 9% | "b. 9% (nine percent) on Taxable Income that is not Qualifying Income" | same |
| De minimis: non-qualifying revenue cap, amount | AED 5,000,000 | "does not exceed the lower of" (footnote 60), first limb "AED 5,000,000" | https://tax.gov.ae/DataFolder/Files/Guides/CT/CT%20General%20Guide%20-%20EN%20-%2010%2009%202023.pdf |
| De minimis: share of total revenue | 5% | "5% of total Revenue (calculated as total amount of non-qualifying Revenue" | same |

- WHO: a Free Zone Person is a Qualifying Free Zone Person only if it meets ALL the conditions of article 18(1) of Federal Decree-Law No. 47 of 2022 (unofficial English translation): maintains adequate substance in the State; derives Qualifying Income; has not elected to be subject to Corporate Tax; complies with articles 34 and 55 (transfer pricing); and meets any other conditions the Minister prescribes. Failing any condition at any time in a tax period ends the status from the beginning of that tax period (article 18(2)). Article 18(3) lets the Minister prescribe otherwise. The [General Guide](https://tax.gov.ae/DataFolder/Files/Guides/CT/CT%20General%20Guide%20-%20EN%20-%2010%2009%202023.pdf) adds that such a person "will be taxed at the general rates of Corporate Tax for five Tax Periods starting with the Tax Period in which the conditions have not been met".
- SUBSTANCE: the General Guide (CTGGCT1, September 2023) says the Free Zone Person must have its core income-generating activities "performed within the Free Zone", either itself or outsourced to a party located in a Free Zone under its adequate supervision, and must show "adequate staff and assets" and adequate operating expenditure in the Free Zone. It is decided case by case.
- DE MINIMIS: non-qualifying revenue in the tax period must not exceed the lower of the AED 5,000,000 and the 5% of total revenue in the table.

## Worked cases

Hypothetical facts, not a real client. A family holding company ("HoldCo") is incorporated and managed in a country that charges it no profit tax. In 2026 it earns EUR 1,000,000 of interest and portfolio dividends, all retained, and has operating costs of EUR 40,000. It has no staff of its own: investment decisions are taken by whoever owns it. The case assumes HoldCo stays resident only in its own country. If its owner takes its decisions at home, HoldCo may itself be resident there (in Malta, a body of persons "the control and management of whose business are exercised in Malta" is resident, [Income Tax Act, Cap. 123](https://legislation.mt/eli/cap/123/eng/pdf)). Check that first in `mt-company-residence-and-substance` or `family-holding-company-location-compared`. Each of the three owners below is taken in turn as the sole owner of all of HoldCo's shares. Nothing is computed for a country whose page does not print the rule.

| Item | Value | Note | Source |
| --- | --- | --- | --- |
| Hypothetical retained passive income of HoldCo | EUR 1,000,000 | assumption, tested against the Malta rules | https://legislation.mt/eli/sl/123.187/eng/pdf |
| Hypothetical operating costs of HoldCo | EUR 40,000 | assumption | same |
| Hypothetical tax paid by HoldCo | EUR 0 | assumption | same |

(a) Owner is an individual resident in the UK. The UK CFC charge falls only on UK resident companies ([INTM194500](https://www.gov.uk/hmrc-internal-manuals/international-manual/intm194500)). The individual is not a chargeable company, so no CFC charge arises, whatever HoldCo earns. That is not the end of the UK analysis: refer the transfer of assets abroad rules ([INTM600000](https://www.gov.uk/hmrc-internal-manuals/international-manual/intm600000)) and the individual's own position to a UK adviser. If the same individual instead held HoldCo through a UK company, the UK company would be a chargeable company; HoldCo's profits exceed the GBP 500,000 low profits limit in the UK table, and with no local tax the tax exemption cannot apply, so the gateway chapters would have to be worked through.

(b) Owner is a Malta company. Under S.L. 123.187 reg. 7(1): control is met (holding all the shares is more than the 50% in the Malta table); the low-tax test is met if the interest and dividends would be chargeable under the Income Tax Acts had the Malta company earned them (assumed here; confirm no exemption applies), because actual tax of EUR 0 is then lower than the Malta tax less EUR 0. Neither carve-out applies: the accounting profits exceed the EUR 750,000 in the Malta table (and the non-trading income exceeds EUR 75,000), and profits far exceed 10% of operating costs. What is attributed then depends on the facts the case fixes: only income from non-genuine arrangements, limited to income generated through assets and risks linked to significant people functions carried out by the Malta company in Malta (reg. 7(2) and reg. 8(a)). If the Malta company's board in Malta takes all the investment decisions and HoldCo has no people of its own, the whole EUR 1,000,000 could be linked to Malta functions, and it is included in the tax period in which HoldCo's year ends, with credit for any foreign tax (EUR 0 here). If those functions are carried out elsewhere, nothing is attributed. The Malta tax on an inclusion, and any refund to the Malta company's shareholders, is not computed here: the pages read do not settle how an inclusion is allocated to the Malta tax accounts. Refer to a Malta adviser and `mt-holding-company-participation-exemption`.

```oa-check
name: Malta company owns all of a zero-tax HoldCo (S.L. 123.187 reg. 7(3) and 8)
inputs:
  accounting_profits: 1000000
  non_trading_income: 1000000
  operating_costs: 40000
  participation: 1
  share_linked_to_malta_functions: 1
steps:
  - profits_over_carve_out_a_limit: accounting_profits - 750000
  - non_trading_over_carve_out_a_limit: non_trading_income - 75000
  - carve_out_b_profit_ceiling: operating_costs * 0.10
  - profits_over_carve_out_b_ceiling: accounting_profits - carve_out_b_profit_ceiling
  - maximum_inclusion: accounting_profits * participation * share_linked_to_malta_functions
expected:
  profits_over_carve_out_a_limit: 250000
  non_trading_over_carve_out_a_limit: 925000
  carve_out_b_profit_ceiling: 4000
  profits_over_carve_out_b_ceiling: 996000
  maximum_inclusion: 1000000
```

Each "over" figure is positive, so each carve-out fails; the maximum inclusion holds only if every significant people function sits in Malta. If they sit elsewhere, `share_linked_to_malta_functions` is 0 and nothing is included.

(c) Owner is a US citizen (wherever resident). The citizen is a United States person owning all the shares, more than the 10 percent United States shareholder threshold, and United States shareholders own more than 50 percent of HoldCo, so HoldCo is a controlled foreign corporation (sections 951(b) and 957(a)). The citizen must then work out subpart F income and net CFC tested income for taxable years beginning after December 31, 2025 (Public Law 119-21, section 70323(c)). Whether interest and portfolio dividends are subpart F income, and the tax that follows, are in `us-gilti-fdii-beat`; Form 5471 is in `us-form-5471-cfc-information`. They are not computed here.

Same HoldCo, owner is an Irish, Cypriot or Luxembourg company. Control is met in each case. The Cypriot and Luxembourg low-tax tests are met if the income would be taxed there, and Ireland's effective tax rate exemption fails because HoldCo pays no tax. The EUR 750,000 carve-outs fail on these numbers, and so does Ireland's EUR 75,000 profit exemption. As in Malta, the attribution then turns on where the significant people functions (in Luxembourg, "fonctions importantes") are carried out. Owner is a Dutch company: if HoldCo's state is on the designated list, the interest and dividends are tainted income and are included unless HoldCo carries on a substantial economic activity, which a company with no staff of its own is unlikely to show.

## When to refuse or refer

- Refer every case where a company shareholder resident in Malta, Ireland, Cyprus, the Netherlands, Luxembourg or the UK controls a low-taxed holding company. The attribution tests (significant people functions, non-genuine arrangements, the UK gateway) are fact-heavy and this skill states them but does not apply them to a client.
- Refer a UK-resident individual owner to a UK adviser for the transfer of assets abroad rules, which this skill does not cover.
- Refer any US person to `us-gilti-fdii-beat`, `us-form-5471-cfc-information` and a US adviser. Do not apply the EU "companies only" conclusion to a US citizen.
- Refuse to state that Switzerland or Singapore has, or lacks, a CFC rule on the basis of this skill. Its pages do not print one either way.
- Refer if the holding company sits in a jurisdiction on the EU list of non-cooperative jurisdictions: Ireland removes its main exemptions there, and the Dutch test includes such states.
- Refer the holding company's own residence and substance to `mt-company-residence-and-substance` (Malta) or the adviser in its country, and its exemptions to `family-holding-company-location-compared`.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Malta, S.L. 123.187 (ATAD Implementation Regulations). Read for reg. 2(2), reg. 3 (25%), reg. 7(1) to (3) (50%, EUR 750,000, EUR 75,000, 10%) and reg. 8. | https://legislation.mt/eli/sl/123.187/eng/pdf | 2026-11-14 |
| Malta, Income Tax Act, Cap. 123. Read for art. 2, the definition of a resident body of persons (control and management). | https://legislation.mt/eli/cap/123/eng/pdf | 2026-11-14 |
| Ireland, Revenue Tax and Duty Manual Part 35B-01-01. Read for who is charged, control (50 per cent), the exemptions (EUR 750,000, EUR 75,000, 10%, effective tax rate) and section 835YA. | https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-35b/35b-01-01.pdf | 2026-11-14 |
| Cyprus, Income Tax Law N. 118(I)/2002, consolidated text. Read for art. 36A(1) to (5) (50%, EUR 750,000, EUR 75,000, 10%), opened through a rendering service because the site serves a script check to direct downloads. | https://www.gov.cy/media/sites/167/2026/01/IT118I-2002.pdf | 2026-11-14 |
| Netherlands, Wet op de vennootschapsbelasting 1969, valid 1 January 2026. Read for art. 13ab(1), (3) (50%, 9%), (4), (5) and (10) (25%). | https://wetten.overheid.nl/BWBR0002672/2026-01-01 | 2026-11-14 |
| Netherlands, Belastingdienst, Voordelen uit een gecontroleerd lichaam. Read for the link to the 2026 list of low-tax states. | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/voordelen-uit-een-gecontroleerd-lichaam | 2026-11-14 |
| Luxembourg, L.I.R. coordinated text in force on 1 January 2026. Read for art. 164ter(1) to (2) (50 pour cent, EUR 750,000, 10 pour cent, 25 pour cent) and the attribution rule. | https://impotsdirects.public.lu/dam-assets/fr/legislation/LIR/texte-coordonn-en-vigueur-au-1er-janvier-2026-ver-08052026.pdf | 2026-11-14 |
| UK, HMRC INTM190000. Read for the start date (1 January 2013) and the gateway chapters. | https://www.gov.uk/hmrc-internal-manuals/international-manual/intm190000 | 2026-11-14 |
| UK, HMRC INTM191100. Read for the CFC definition, the 25% interest and the 40% joint venture test. | https://www.gov.uk/hmrc-internal-manuals/international-manual/intm191100 | 2026-11-14 |
| UK, HMRC INTM194500. Read for who is a chargeable company (UK resident companies, 25%). | https://www.gov.uk/hmrc-internal-manuals/international-manual/intm194500 | 2026-11-14 |
| UK, HMRC INTM197200. Read for Chapter 4 conditions A to D. | https://www.gov.uk/hmrc-internal-manuals/international-manual/intm197200 | 2026-11-14 |
| UK, HMRC INTM224000. Read for the list of entity exemptions and the exempt period. | https://www.gov.uk/hmrc-internal-manuals/international-manual/intm224000 | 2026-11-14 |
| UK, HMRC INTM225550. Read for the low profits exemption (GBP 500,000, GBP 50,000). | https://www.gov.uk/hmrc-internal-manuals/international-manual/intm225550 | 2026-11-14 |
| UK, HMRC INTM225800. Read for the low profit margin exemption (10 per cent). | https://www.gov.uk/hmrc-internal-manuals/international-manual/intm225800 | 2026-11-14 |
| UK, HMRC INTM226100. Read for the tax exemption (75%) and the tax shelter limit. | https://www.gov.uk/hmrc-internal-manuals/international-manual/intm226100 | 2026-11-14 |
| UK, HMRC INTM236000. Read for the meaning of control. | https://www.gov.uk/hmrc-internal-manuals/international-manual/intm236000 | 2026-11-14 |
| UK, HMRC INTM600000. Read for the existence of the transfer of assets abroad income and benefits charges only. | https://www.gov.uk/hmrc-internal-manuals/international-manual/intm600000 | 2026-11-14 |
| US, 26 U.S.C. 951 (govinfo, 2024 edition). Read for sec. 951(a) and (b) (10 percent). | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partIII-subpartF-sec951.htm | 2026-11-14 |
| US, 26 U.S.C. 957 (govinfo, 2024 edition). Read for sec. 957(a) (more than 50 percent). | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partIII-subpartF-sec957.htm | 2026-11-14 |
| US, Public Law 119-21 (govinfo). Read for sec. 70323(a)(1) and (c) (net CFC tested income, years after 31 December 2025) and sec. 70353 (sec. 958(b)(4), sec. 951B). | https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm | 2026-11-14 |
| Singapore, IRAS FSIE e-Tax Guide. Read for the three FSIE conditions and the 15% headline rate. | https://www.iras.gov.sg/media/docs/default-source/e-tax/tax-exemption-for-foreign-sourced-income285e5d43d6af4001b3ce35da1e9005b5.pdf | 2026-11-14 |
| UAE, Federal Decree-Law No. 47 of 2022. Read for art. 3(2) (0%, 9%) and art. 18. | https://tax.gov.ae/Datafolder/Files/Legislation/Corporate%20Tax/CT%20law%20final/Federal%20Decree-Law%20No.%2047%20of%202022%20-%20For%20publishing.pdf | 2026-11-14 |
| UAE, FTA General Corporate Tax Guide (CTGGCT1). Read for the Free Zone substance part, the de minimis (AED 5,000,000, 5%) and the five-period rule. | https://tax.gov.ae/DataFolder/Files/Guides/CT/CT%20General%20Guide%20-%20EN%20-%2010%2009%202023.pdf | 2026-11-14 |

Not yet confirmed: whether the Cyprus amending law N. 244(I)/2025 (in force 1 January 2026) changes article 36A or the credit articles 35 and 36 (the 4 October 2026 reading of the Tax Department's presentation said 36A was not among the amended articles but 35 and 36 were; the presentation was not reopened on 14 November 2026 because the site serves a script check); the start year of Dutch article 13ab; whether Switzerland or Singapore has a CFC rule (no official page read prints one either way); IRAS guidance on Singapore section 10L (not located on 4 October 2026, not searched again); the Malta tax on a CFC inclusion and its allocation to the Malta tax accounts; whether the 2026 IRS forms and instructions for Form 5471 reflect section 958(b)(4) as restored (see `us-form-5471-cfc-information`).
