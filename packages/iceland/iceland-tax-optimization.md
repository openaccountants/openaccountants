---
name: iceland-tax-optimization
description: Use this skill whenever asked about reducing tax in Iceland, tax planning, or legal strategies to minimise tax for a self-employed person or small company in Iceland, tax year 2026. Trigger on phrases like "reduce tax Iceland", "ehf vs self-employed", "Iceland dividends 22%", "reiknað endurgjald", "reference salary", "Iceland company tax 20%", "save tax Iceland", "tax planning Iceland". This skill covers the ehf-company-plus-dividend structure vs self-employment, the mandatory owner reference-salary rule (reiknað endurgjald), capital-income vs labour-income treatment, pension and personal reliefs, residential rental income, and the anti-avoidance red lines, with a worked own-name versus ehf decision. ALWAYS read this skill before advising on any Icelandic tax optimisation.
version: 1.0
jurisdiction: IS
tax_year: 2026
last_updated: 2026-11-14
category: tax-optimization
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: tax-optimization
type: situation-rules
---

# Iceland tax optimisation for owners of an ehf. and the self-employed v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

This skill sets out the legal choices an owner-manager in Iceland can make about how income is paid and taxed, and the conditions attached to each choice. Figures are for tax year 2026. It covers the choice between working in your own name and through a private limited company (einkahlutafélag, ehf.), the owner's calculated remuneration (reiknað endurgjald), dividends, pension deductions, the personal tax credit and rental income. It does not cover aggressive schemes. Every choice here is a choice the law offers openly, with its conditions.

Withholding rates in this skill include the weighted average municipal tax (útsvar). Each municipality sets its own útsvar, so a person's final rate is settled at assessment. Figures printed on the "Álagningarseðill og forsendur 2026" pages describe the 2026 assessment of 2025 income and are not used here as 2026 figures.

Who is in: an individual resident in Iceland who runs a business in their own name, or who owns and works in an ehf., in income year 2026. Who is out: non-resident owners, holding structures, short-term letting (heimagisting), listed-company employees with share plans (see `iceland-payroll`), and any scheme whose purpose is to hide income.

## Ask the client first

- Do you work in the business in your own name, or through a company? If a company, what share do you own, and what do your spouse, children, parents, siblings, other close relatives and working shareholders own together with you?
- Which category (A to H) describes your work, how many staff do you have, and is this your first year of business?
- Do you have another fixed paid job, and what does it pay?
- Is the company listed on a public securities market?
- Are you married or jointly taxed, and does your spouse use their personal tax credit in full?
- Are you buying a first home, or have you owned no home for five years?
- Do you let a home, how many separate dwellings, and is each lease registered in the HMS rental register?

## The method, step by step

1. Decide whether the person must compute calculated remuneration. A person who works in their own business in their own name must compute it. A person who works in a company must compute it if they are a controlling party (ráðandi aðili), as defined in the reiknað endurgjald table below. Source: [Reiknað endurgjald 2026](https://www.skatturinn.is/atvinnurekstur/stadgreidsla-og-reiknad-endurgjald/reiknad-endurgjald/2026/), lög nr. 90/2003 um tekjuskatt.
2. Pick the occupation category (A to H) and read the minimum monthly and yearly amount for 2026 from the [Reiknað endurgjald 2026](https://www.skatturinn.is/atvinnurekstur/stadgreidsla-og-reiknad-endurgjald/reiknad-endurgjald/2026/) page. Set the calculated remuneration at least at that amount unless there is evidence for a lower figure.
3. Run withholding (staðgreiðsla), employer social security tax (tryggingagjald) and pension contributions on that remuneration, as for any wage. Rates and brackets are in the tables from [Helstu tölur og prósentur 2026](https://www.skatturinn.is/einstaklingar/helstutolur/2026/helstu-tolur-og-prosentur-2026) and [Tryggingagjald](https://www.skatturinn.is/atvinnurekstur/skattar-og-gjold/tryggingagjald/).
4. In an ehf., the profit left after the remuneration is taxed at the company rate. Profit paid out as a lawful dividend is taxed on the shareholder as capital income, withheld by the company. Source: [Arður](https://www.skatturinn.is/einstaklingar/fjarmagnstekjur/ardur/).
5. Use the pension deductions: the mandatory contribution and, separately, a supplementary private pension (séreignarsparnaður), both paid regularly. Source: [Iðgjald í lífeyrissjóði](https://www.skatturinn.is/einstaklingar/tekjur-og-fradraettir/idgjald-i-lifeyrissjodi/).
6. Check the personal tax credit is used in full, including a spouse's unused credit where the couple is jointly taxed. Source: [Persónuafsláttur](https://www.skatturinn.is/einstaklingar/stadgreidsla/personuafslattur/).
7. For a first home, check the tax-free use of séreignarsparnaður under the first-home scheme. Source: [Fyrsta íbúð](https://www.skatturinn.is/einstaklingar/skattamal/nyting-sereignarsparnadar/fyrsta-ibud/).
8. Report the remuneration on the individual's tax return and as an expense in the business accounts. The tax authority (Ríkisskattstjóri) reviews it as it sees reason to. Source: [Reiknað endurgjald 2026](https://www.skatturinn.is/atvinnurekstur/stadgreidsla-og-reiknad-endurgjald/reiknad-endurgjald/2026/).

### Quick reference, 2026 ([Helstu tölur og prósentur 2026](https://www.skatturinn.is/einstaklingar/helstutolur/2026/helstu-tolur-og-prosentur-2026))

| Item | Value | Note | Source |
| --- | --- | --- | --- |
| Withholding rate, bracket 1, wages, 2026 (includes average útsvar) | 31.49% | "Skattþrep 1" | https://www.skatturinn.is/einstaklingar/helstutolur/2026/helstu-tolur-og-prosentur-2026 |
| Withholding rate, bracket 2, wages, 2026 (includes average útsvar) | 37.99% | "Skattþrep 2" | same |
| Withholding rate, bracket 3, wages, 2026 (includes average útsvar) | 46.29% | "Skattþrep 3" | same |
| Personal tax credit per month, 2026 | ISK 72,492 | "Persónuafsláttur á mánuði" | same |
| Personal tax credit per year, 2026 | ISK 869,898 | "Persónuafsláttur á ári" | same |
| Capital income tax, individuals, 2026 | 22% | "Skattur á fjármagnstekjur"; Act 90/2003, Article 66(3) | same |
| Capital income allowance per person (interest, and dividends and gains on listed shares only) | ISK 300,000 | "Frítekjumark er 300.000 kr. samtals á manni"; Act 90/2003, Article 66(3) | same |
| Capital income allowance, married couple | ISK 600,000 | "fyrir hjón" | same |
| Company income tax, hf. and ehf. | 20% | "hlutafélög, einkahlutafélög o.fl."; Act 90/2003, Article 71(1) | same |
| Income tax, partnerships taxed as separate entities (sf.), estates and similar | 37.6% | "sameignarfélög, dánarbú, þrotabú o.fl."; Act 90/2003, Article 71(2) | same |
| Tax rate on children's income (born 2011 or later) above the children's tax-free amount | 6% | "Skatthlutfall barna" | same |

The capital income allowance covers interest income on one side, and dividends and gains from shares in companies listed on a regulated market or trading facility on the other. The page reads "á annars vegar við vaxtatekjur og hins vegar tekjur af hlutabréfaeign í formi arðs og söluhagnaðar í félögum skráðum á skipulegum verðbréfamarkaði" (applies to interest income and to income from shareholdings as dividends and gains in companies listed on a regulated securities market). Dividends from an unlisted ehf. therefore get no allowance under this text. The law says the same: Article 66(3) of the Income Tax Act 90/2003 exempts "annars vegar vaxtatekjum og hins vegar tekjum af hlutabréfaeign í formi arðs og söluhagnaðar í félögum skráðum á skipulegum markaði eða markaðstorgi fjármálagerninga, samtals allt að 300.000 kr. á ári hjá manni", and uses the allowance first against interest, then dividends, then share gains. Skatturinn's [Arður](https://www.skatturinn.is/einstaklingar/fjarmagnstekjur/ardur/) page lists "Arðstekjur" without the listing condition; the statute governs, so do not apply the allowance to ehf. dividends.

#### 2026 thresholds from the ministry note of 22 December 2025

| Item | Value | Note | Source |
| --- | --- | --- | --- |
| Weighted average útsvar built into the withholding rates, 2026 | 14.94% | "þar af 14,94% útsvar" | https://www.stjornarradid.is/efst-a-baugi/frettir/stok-frett/2025/12/22/Breytingar-a-stadgreidslu-um-aramotin/ |
| Yearly income tax base where the middle bracket starts, 2026 | ISK 5,977,470 | "Þrepamörk upp í miðþrep" | same |
| Yearly income tax base where the top bracket starts, 2026 | ISK 16,781,397 | "Þrepamörk upp í háþrep" | same |
| Yearly tax-free amount of wages, 2026 (after the mandatory pension contribution) | ISK 2,877,560 | "Skattleysismörk launa" | same |
| Yearly tax-free amount for children under 16, 2026 | ISK 300,000 | "Skattleysismörk barna yngri en 16 ára" | same |

From tax year 2026 spouses and cohabitants lose the right to share the second and third brackets in the case where one has an income tax base in the third bracket and the other does not. Act 99/2025, Article 30, repealed the bracket-sharing paragraph (Article 66(1), point 4) of the Income Tax Act. The note reads "Á tekjuárinu 2026 fellur út heimild hjóna og sambúðaraðila að samnýta annað og þriðja þrep" (in income year 2026 the right of spouses and cohabitants to share the second and third bracket falls away). In that case, do not plan on shifting bracket room between the two for 2026.

#### Monthly withholding brackets, 2026

| Item | Value | Note | Source |
| --- | --- | --- | --- |
| Top of bracket 1, per month, wages | ISK 498,122 | "Skattþrep 1 Af tekjum" | https://www.skatturinn.is/einstaklingar/stadgreidsla/skattthrep/2026/ |
| Top of bracket 2, per month, wages | ISK 1,398,450 | "Skattþrep 2 Af tekjum" | same |

### Own name or an ehf.

| Route | Treatment |
| --- | --- |
| Business in own name (eigin kennitala) | The owner computes calculated remuneration, taxed as wages. The rest of the business profit is also the owner's income. |
| ehf. (private limited company) | The controlling owner computes calculated remuneration, taxed as wages. The company pays company income tax on its profit. A lawful dividend is capital income of the shareholder. |

The reason owners use an ehf. is that profit above a fair salary can be taxed at the company rate and, when paid out, at the capital income rate, both in the quick reference table, instead of at the wage withholding rates. The calculated remuneration rule limits this: an active controlling owner must first take the remuneration the rules require, and that part is taxed as wages. Whether the combined company and dividend burden is lower than wage tax depends on the facts. No allowed page prints a combined rate, and this skill does not compute one.

A distribution that is not a lawful dividend is not taxed as a dividend. The [Arður](https://www.skatturinn.is/einstaklingar/fjarmagnstekjur/ardur/) page reads "Ef um er að ræða óheimila úthlutun arðs fer með þær tekjur annað hvort sem laun eða sem gjöf" (an unlawful distribution of dividends is treated either as wages or as a gift), taxed at the ordinary income tax rates and útsvar. The law decides which: under Article 11(2) of the Income Tax Act, a distribution that is unlawful under the company acts is wages if the shareholder is also an employee of the company or a related company, and a taxable gift under Article 7(A)(4) for any other shareholder.

| Item | Value | Note | Source |
| --- | --- | --- | --- |
| Capital income tax rate on dividends, since 1 January 2018 | 22% | "er 22% frá og með 1. janúar 2018" | https://www.skatturinn.is/einstaklingar/fjarmagnstekjur/ardur/ |

A dividend counts as income in the year the decision to distribute is made, not necessarily when it is paid. The paying company withholds the capital income tax. If the dividend is not paid in the year of the decision, the withholding is due at the latest with the return for October to December of the decision year (same page).

A special rule taxing excess dividends of controlling working shareholders as wages ("Arður talinn sem laun") applied only at the assessment years 2011 to 2014, per the same page. It is not current law and is not used in this skill.

### Calculated remuneration (reiknað endurgjald), the key constraint

Who must compute it. A person working in their own business, alone or in a business run in common with others, must compute remuneration and treat it as wages: withholding, tryggingagjald and pension contribution. A person working in a company must do so if they are a controlling party by ownership or management participation (ráðandi aðili vegna eignar- eða stjórnunaraðildar). A controlling party is a person who, alone or together with a spouse, children, parents, siblings or other close relatives, or working shareholders, owns the share in the table below or more, AND personally owns the own-share figure in the table or more. Both conditions must be met. Indirect ownership or management counts in the same way, for example work for a subsidiary or associate of a company the person controls. For a group of working shareholders who are not related, the page states the group test as more than the group share in the table, with the same personal minimum: "eigi hópur starfandi hluthafa meira en 50% í lögaðila þá skulu viðmiðunarreglur um reiknað endurgjald gilda um þá ef eignarhlutur viðkomandi er a.m.k. 5%" (if a group of working shareholders owns more than 50% of a legal entity, the rules apply to them if the person's own share is at least 5%). The rule does not apply to work for a company listed on a public securities market. The statutory basis is Article 58 of the Income Tax Act 90/2003; Article 58(4) sets the same 50% group and 5% own-share test ("enda eigi hver um sig a.m.k. 5% hlut").

How much. The remuneration must not be lower than the person would have earned working for an unrelated party. The tax authority sets minimum amounts each year by category A to H. Benefits in kind (for example a company car) are added on top. The amounts below are 2026 minimums for selected categories; the full list is on the page.

| Item | Value | Note | Source |
| --- | --- | --- | --- |
| Controlling party test: share owned with family or working shareholders, at least | 50% | "á samtals 50% hlut eða meira í lögaðila" | https://www.skatturinn.is/atvinnurekstur/stadgreidsla-og-reiknad-endurgjald/reiknad-endurgjald/2026/ |
| Controlling party test: share owned personally, at least | 5% | "og á sjálfur 5% hlut eða meira í lögaðilanum" | same |
| A(6) specialist working alone, per month | ISK 1,440,000 | "Mánaðarlaun" | same |
| A(6) specialist working alone, per year | ISK 17,280,000 | "Árslaun" | same |
| B(5) general business, alone or with fewer than two staff, per month | ISK 933,000 | "Mánaðarlaun" | same |
| B(5) general business, alone or with fewer than two staff, per year | ISK 11,196,000 | "Árslaun" | same |
| B(9) general business starting for the first time, alone or with one employee, first year only, per month | ISK 681,000 | "Mánaðarlaun" | same |
| B(9) general business starting for the first time, first year only, per year | ISK 8,172,000 | "Árslaun" | same |
| C(5) category C with fewer than two staff, per month | ISK 1,129,000 | "Mánaðarlaun" | same |
| C(5) category C with fewer than two staff, per year | ISK 13,548,000 | "Árslaun" | same |
| C(6) category C working alone, per month | ISK 795,000 | "Mánaðarlaun" | same |
| C(6) category C working alone, per year | ISK 9,540,000 | "Árslaun" | same |
| Floor when the person has another paid job or another job that itself requires calculated remuneration: never below this share of the benchmark, plus any increase set under the minimum rules | 25% | "aldrei lægra en 25% af viðmiðunarfjárhæðinni" | same |
| Estimated yearly remuneration below this amount falls outside withholding (still taxable) | ISK 700,000 | "Reiknað endurgjald innan við 700.000 kr." | same |

Lower than the benchmark. A person who considers the remuneration should be lower than the benchmark must attach documents and reasons to the tax return. The tax authority may accept a lower figure if the reasons and documents justify it. If it does not, it raises the remuneration to the benchmark. For a self-employed person, a raise by the tax authority may not create a loss in the business beyond the year's ordinary depreciation, and for an old-age, disability or partial disability pensioner with their own business it may not create a loss at all (Article 58(3) of the Income Tax Act names "elli- og örorkulífeyrisþega [og hlutaörorkulífeyrisþega]"). This limit does not apply to a company or to a person who computes remuneration for work in a company. The page reads "hún gildir ekki um rekstur lögaðila og þeirra sem reikna ber sér endurgjald vegna starfa hjá þeim" (it does not apply to the business of a legal entity or to those who must compute remuneration for work for one).

Another job. If the person has another fixed paid job, or another job for which remuneration must be computed, the benchmark may be reduced by the amount by which the pay or remuneration for the other job exceeds half of the benchmark, but never below the floor in the table plus any increase set under the minimum rules.

Spouses in one business. Where spouses or jointly taxed cohabitants run a business together, each sets their own remuneration and the profit is split in proportion to it. Where only one runs the business and the other works in it, remuneration is computed for the other's work as if an unrelated person did it.

> **Audit point.** Remuneration below the benchmark without documents and reasons on the return will be raised to the benchmark. Set it at or above the benchmark for the category, or document the lower figure.

#### Social security tax on the remuneration

| Item | Value | Note | Source |
| --- | --- | --- | --- |
| Tryggingagjald total, 2026 | 6.35% | "tryggingagjaldshlutfallið samtals" | https://www.skatturinn.is/atvinnurekstur/skattar-og-gjold/tryggingagjald/ |
| Minimum yearly base for the self-employed on own work, full time | ISK 748,224 | "en þó ekki lægri en 748.224 kr. árstekjur" | same |

### Deductions and reliefs

#### Pension contributions

| Item | Value | Note | Source |
| --- | --- | --- | --- |
| Maximum deduction, mandatory pension contribution | 4% | "Hámarksfrádráttur er 4% af iðgjaldsstofni" | https://www.skatturinn.is/einstaklingar/tekjur-og-fradraettir/idgjald-i-lifeyrissjodi/ |
| Additional deduction, supplementary private pension (séreign) | 4% | "allt að 4% vegna iðgjalda samkvæmt samningi um viðbótartryggingavernd" | same |

These are two separate deductions, each a share of the contribution base. Both require regular payment: "Skilyrði frádráttar er í báðum tilvikum að iðgjöld séu greidd reglulega" (in both cases the condition is that contributions are paid regularly). The same rules apply to employees and to a person working in their own business.

#### Personal tax credit (persónuafsláttur)

Residents of Iceland aged 16 or older get the personal tax credit in the quick reference table. It reduces income tax on wages and pension; it is not a deduction from income. Unused credit in one month builds up and can be used later in the same year. Unused credit does not carry to the next year: "Ónýttur persónuafsláttur færist ekki á milli ára". A spouse's credit may be used "að fullu eða að hluta ef maki nýtir hann ekki sjálfur" (in full or in part if the spouse does not use it). For 2026 the whole of it may be used in withholding: "Heimilt er að nýta allan (100%) ónýttan persónuafslátt maka á árinu 2026" ([Staðgreiðsla 2026](https://www.skatturinn.is/einstaklingar/stadgreidsla/stadgreidsla/2026)); the employer must be told. At assessment, Article 67(A) of the Income Tax Act adds a jointly taxed spouse's unused credit to the other spouse's credit. Source: [Persónuafsláttur](https://www.skatturinn.is/einstaklingar/stadgreidsla/personuafslattur/).

#### Séreign for a first home

| Item | Value | Note | Source |
| --- | --- | --- | --- |
| Maximum tax-free use per person per year | ISK 500,000 | "Árleg hámarksnýting séreignarsparnaðar" | https://www.skatturinn.is/einstaklingar/skattamal/nyting-sereignarsparnadar/fyrsta-ibud/ |
| Total maximum over the 10-year period | ISK 5,000,000 | "Samtals nemur hámarksheimild" | same |
| Minimum ownership share the applicant must acquire | 30% | "Umsækjandi eignist 30% eignarhlut í eigninni" | same |
| Own contribution counted, at most | 4% of the contribution base, up to ISK 333,000 a year | "allt að 4% af iðgjaldsstofni og að hámarki 333 þús. kr." | same |
| Employer contribution counted, at most | 2%, up to ISK 167,000 a year | "allt að 2% og að hámarki 167 þús. kr." | same |

Conditions, all of which must be met: the applicant acquires at least the ownership share in the table, applies within 12 months of signing the purchase contract, and is buying a first home or has not owned residential property for five years. Use can run for at most a continuous 10-year period. The own contribution may not be lower than the employer's ("Framlag einstaklingsins getur ekki verið lægra en framlag launagreiðandans").

The general scheme for using séreign tax-free on a home for own use ended at the end of 2025. The [Nýting séreignarsparnaðar](https://www.skatturinn.is/einstaklingar/skattamal/nyting-sereignarsparnadar/) page reads "féll úr gildi í lok árs 2025 og hefur ekki verið framlengd" (lapsed at the end of 2025 and has not been extended). For 2026 only the first-home scheme is available.

#### Rental income from a home

| Item | Value | Note | Source |
| --- | --- | --- | --- |
| Share of residential rent taxed as capital income, from 2026 | 75% | "færast því einungis til skattskyldra tekna 75% af fenginni leigu" | https://www.skatturinn.is/einstaklingar/fjarmagnstekjur/leigutekjur/ |
| Share exempt before 2026 (old rule) | 50% | "Frítekjumarkið var áður 50%" | same |

The relief applies to letting residential property for the tenant to live in. Letting counts as capital income only where it falls under the Rent Act (húsaleigulög) and no more than two separate dwellings are let; the page reads "ef um er að ræða útleigu sem fellur undir húsaleigulög og hinar útleigðu sérgreindu íbúðir ekki fleiri en tvær" (where the letting falls under the Rent Act and the separate dwellings let are not more than two). Letting of more dwellings, or letting property to a business, is business income and gets no exemption. For qualifying residential letting, from 2026 a quarter of the gross rent is exempt and the rest is capital income taxed at 22%, with no deduction for costs; the page says "Þetta gildir frá og með árinu 2026" (this applies from 2026). The law adds a condition the page does not print: Article 66(3) of the Income Tax Act grants the 25% exemption only "enda hafi leigusamningur verið skráður í leiguskrá húsnæðisgrunns" (provided the lease has been registered in the rental register of the housing database, run by Húsnæðis-, mannvirkja- og skipulagsstofnun). Register the lease before relying on the exemption. Rent against rent: a person who lets a home they used themselves, under the Rent Act, and pays rent for another home for their own use may deduct the rent paid from the rent received (same page; Article 58a(1)(a) of the Income Tax Act). Short-term letting (heimagisting, for example Airbnb) is taxed either as business income or as capital income and is not covered by this skill.

#### Business expenses

Genuine costs of the business are deductible against business income, whether in own name or in an ehf. Private spending booked as a company expense is not a deduction.

### Red lines (do not cross)

- **Remuneration red line.** Never set a controlling owner's remuneration below the category benchmark without documents and reasons that justify it.
- **Lawful dividends only.** A distribution that is not a lawful dividend is taxed as wages or a gift.
- **No unlawful shareholder loans.** A loan to a shareholder or board member that the company acts forbid is a taxable gift: "Til skattskyldra gjafa teljast lán til hluthafa og stjórnarmanna sem eru óheimil samkvæmt lögum um hlutafélög og lögum um einkahlutafélög" (Income Tax Act 90/2003, Article 7(A)(4)).
- **Substance.** The ehf. must carry on a genuine business.
- **Private spending.** Private costs booked as company expenses are not deductions.

### Prohibitions

- **Prohibition 1.** NEVER advise a controlling owner to take remuneration below the benchmark to maximise dividends.
- **Prohibition 2.** NEVER present the ehf. route as avoiding wage tax entirely; the calculated remuneration is taxed as wages.
- **Prohibition 3.** NEVER state the ISK 300,000 capital income allowance as covering dividends from an unlisted ehf.
- **Prohibition 4.** NEVER present this skill as definitive advice; route to a licensed Icelandic tax adviser.

## Boundary and exception table

| Situation | Rule | What to do |
| --- | --- | --- |
| Owner holds under 5% personally, family holds 50% or more | Both limbs of the controlling-party test must be met | No calculated remuneration duty from the company; ordinary wages if paid |
| Unrelated working shareholders hold more than 50% together | Group test with at least 5% own share applies | Each with 5% or more computes remuneration |
| Company listed on a public securities market | Rule does not apply | Ordinary payroll only |
| Owner has another fixed paid job | Benchmark reduced, floor 25% of the benchmark | Compute the reduction, keep the payslips |
| Remuneration set below benchmark | Documents and reasons on the return; otherwise raised | Refer, do not advise below benchmark |
| Dividend not lawful under the company acts | Wages (shareholder-employee) or gift (other shareholder) | Treat at ordinary rates; never as a 22% dividend |
| Loan to shareholder or board member forbidden by company law | Taxable gift, Article 7(A)(4) | Do not plan with it |
| Dividends from an unlisted ehf. | No ISK 300,000 allowance | Tax the whole dividend at 22% |
| Residential letting, more than two dwellings or letting to a business | Business income, no 25% exemption | Refer |
| Residential letting, lease not registered in the HMS register | Article 66(3) exemption condition not met | Register first; until then do not apply the 25% exemption |
| Spouses where one is in the top bracket | Bracket sharing repealed from 2026 | Do not plan on shifting bracket room |
| General séreign use for a home | Lapsed at end of 2025 | Only the first-home scheme in 2026 |

## Worked cases

Both cases use the 2026 annual bands and the average municipal rate built into withholding (14.94%); the final municipal rate is the rate of the person's municipality. Pension contributions are left out because they are the same in both routes of case 1.

### Case 1 (decision): own name or an ehf., profit ISK 20,000,000 before the owner's pay

A consultant in category B(5) (alone, fewer than two staff) earns a profit of ISK 20,000,000 before any pay to herself in 2026. In both routes she takes the B(5) minimum remuneration of ISK 11,196,000 as wages, and the business pays tryggingagjald of 6.35% on it (ISK 710,946). That leaves ISK 8,093,054.

- **Own name.** The ISK 8,093,054 is also her earned income, so the earned base is ISK 19,289,054. State tax 4,265,726.93, municipal tax 2,881,784.67, less the personal credit 869,898: ISK 6,277,613.60.
- **ehf.** Wage tax on ISK 11,196,000 is ISK 2,994,926.85. Company tax at 20% on ISK 8,093,054 is ISK 1,618,610.80, and the 22% dividend tax on the ISK 6,474,443.20 paid out is ISK 1,424,377.50. Total ISK 6,037,915.15.

The ehf. route costs ISK 239,698.45 less tax in this case. The figure that decides it is the slice of profit above the remuneration: it is taxed at 31.35% plus municipal tax in her own name (she is above the top threshold), against 20% plus 22% of the remaining 80% (37.6% combined) in the ehf. Below the top threshold the own-name marginal rate (23.05% plus 14.94%, 37.99%) is close to 37.6%, and the company's running costs can decide it the other way. The remuneration floor is the same in both routes, so the ehf. never removes wage tax on it.

```oa-check
name: IS 2026 own name versus ehf, profit 20,000,000, B5 remuneration
inputs:
  profit: 20000000
  remuneration: 11196000
  levy_rate: 0.0635
  m: 0.1494
  credit: 869898
  t1: 5977470
  t2: 16781397
steps:
  - levy: remuneration * levy_rate
  - rest: profit - remuneration - levy
  - base_a: remuneration + rest
  - state_a: min(base_a, t1) * 0.1655 + (min(base_a, t2) - t1) * 0.2305 + max(base_a - t2, 0) * 0.3135
  - tax_a: round(state_a + base_a * m - credit, 2)
  - state_w: min(remuneration, t1) * 0.1655 + (min(remuneration, t2) - t1) * 0.2305 + max(remuneration - t2, 0) * 0.3135
  - wage_b: round(state_w + remuneration * m - credit, 2)
  - company_tax: round(rest * 0.20, 2)
  - dividend_tax: round((rest - company_tax) * 0.22, 2)
  - tax_b: wage_b + company_tax + dividend_tax
  - saving: tax_a - tax_b
expected:
  levy: 710946.00
  rest: 8093054.00
  tax_a: 6277613.60
  wage_b: 2994926.85
  company_tax: 1618610.80
  dividend_tax: 1424377.50
  tax_b: 6037915.15
  saving: 239698.45
```

### Case 2: two flats let to residents, lease registered or not

An individual lets two flats under the Rent Act for ISK 3,600,000 gross in 2026. With both leases in the HMS rental register, 75% of the rent (ISK 2,700,000) is capital income at 22%: ISK 594,000, with no deduction for costs. The ISK 300,000 allowance does not apply to rent. If the leases are not registered, the Article 66(3) condition for the 25% exemption is not met, so the whole rent is taxed: ISK 792,000. Registering the leases saves ISK 198,000.

```oa-check
name: IS 2026 residential rent, registered versus unregistered lease
inputs:
  rent: 3600000
  rate: 0.22
steps:
  - tax_registered: rent * 0.75 * rate
  - tax_unregistered: rent * rate
  - saving: tax_unregistered - tax_registered
expected:
  tax_registered: 594000
  tax_unregistered: 792000
  saving: 198000
```

## When to refuse or refer

- Refer any plan that sets remuneration below the benchmark; the documents and reasons must come from an adviser who knows the business.
- Refer cross-border cases (non-resident owners, foreign companies, double tax treaties).
- Refer holding structures and dividends between companies; this skill does not cover them.
- Refer short-term letting (heimagisting) and rental of more than ordinary residential letting.
- Before applying the 25% rental exemption, ask whether the lease is registered in the HMS rental register; if not, register it first.
- Refuse any scheme that hides private spending in the company or pays disguised dividends.
- For the full 2026 wage withholding, pension and capital income computation use `iceland-income-tax`; for running the remuneration through payroll use `iceland-payroll`.

## Filing and payment

- Calculated remuneration runs through monthly withholding and the employer return like any wage, and the tryggingagjald with it; see `iceland-payroll` for the return, the due dates and the annual option for small payrolls.
- The individual reports the remuneration, rent and dividends on the annual return (skattframtal) filed in March of the following year; the 2026 income is filed in 2027. See `iceland-income-tax`.
- The ehf. withholds 22% on a dividend in the year of the decision; if unpaid in that year, the withholding is due at the latest with the October to December return of that year. The company files its own return: see `is-corporate-income-tax`.
- First-home séreign use needs an application within 12 months of signing the purchase contract.

## Completion checklist

- Controlling-party test applied with both limbs, and the category (A to H) chosen with evidence.
- Remuneration at or above the 2026 benchmark, or documents and reasons attached.
- Dividends lawful under the company acts and decided in a year the company had distributable funds.
- No ISK 300,000 allowance on unlisted ehf. dividends; no 25% rental exemption without a registered lease.
- Pension deductions paid regularly; spouse credit transfer told to the employer.
- Red lines and prohibitions checked.

### Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a licensed tax adviser in Iceland) before acting upon.

## Sources

Pages dated 2026-11-14 were opened again today and the figures named were found on them. Alþingi's law pages returned HTTP 403 on 14 Nov 2026.

| Source | URL | Read on |
| --- | --- | --- |
| Read for Income Tax Act 90/2003 (consolidated text 158a, 1 October 2026), Articles 7(A)(4), 11(2), 58, 58a, 66, 67(A), 71; not reopened 14 Nov 2026 (403) | https://www.althingi.is/lagas/nuna/2003090.html | 2026-10-30 |
| Read for Skatturinn, Helstu tölur og prósentur 2026: withholding rates, credit, capital income tax 22%, allowance 300,000 and 600,000, company rates 20% and 37.6%, child rate 6% | https://www.skatturinn.is/einstaklingar/helstutolur/2026/helstu-tolur-og-prosentur-2026 | 2026-11-14 |
| Read for Ministry of Finance, Breytingar á staðgreiðslu um áramótin (22 December 2025): 14.94%, 5,977,470, 16,781,397, 2,877,560, end of bracket sharing | https://www.stjornarradid.is/efst-a-baugi/frettir/stok-frett/2025/12/22/Breytingar-a-stadgreidslu-um-aramotin/ | 2026-11-14 |
| Read for Skatturinn, Skattþrep 2026: monthly bracket tops 498,122 and 1,398,450 | https://www.skatturinn.is/einstaklingar/stadgreidsla/skattthrep/2026/ | 2026-11-14 |
| Read for Skatturinn, Staðgreiðsla 2026: spouse's credit 100% in 2026 | https://www.skatturinn.is/einstaklingar/stadgreidsla/stadgreidsla/2026 | 2026-11-14 |
| Read for Skatturinn, Reiknað endurgjald 2026: controlling-party test, categories A(6), B(5), B(9), C(5), C(6), 25% floor, 700,000 | https://www.skatturinn.is/atvinnurekstur/stadgreidsla-og-reiknad-endurgjald/reiknad-endurgjald/2026/ | 2026-11-14 |
| Read for Skatturinn, Tryggingagjald: 6.35% total and the 748,224 floor | https://www.skatturinn.is/atvinnurekstur/skattar-og-gjold/tryggingagjald/ | 2026-11-14 |
| Read for Skatturinn, Arður: 22% since 2018, unlawful distributions, timing and withholding | https://www.skatturinn.is/einstaklingar/fjarmagnstekjur/ardur/ | 2026-11-14 |
| Read for Skatturinn, Iðgjald í lífeyrissjóði: 4% plus 4%, regular payment | https://www.skatturinn.is/einstaklingar/tekjur-og-fradraettir/idgjald-i-lifeyrissjodi/ | 2026-11-14 |
| Read for Skatturinn, Persónuafsláttur: monthly build-up, no carry to next year, spouse use | https://www.skatturinn.is/einstaklingar/stadgreidsla/personuafslattur/ | 2026-11-14 |
| Read for Skatturinn, Nýting séreignarsparnaðar: general scheme lapsed end of 2025 | https://www.skatturinn.is/einstaklingar/skattamal/nyting-sereignarsparnadar/ | 2026-11-14 |
| Read for Skatturinn, Fyrsta íbúð: 500,000 a year, 5,000,000 total, 30%, 333,000 and 167,000 | https://www.skatturinn.is/einstaklingar/skattamal/nyting-sereignarsparnadar/fyrsta-ibud/ | 2026-11-14 |
| Read for Skatturinn, Leigutekjur: 75% taxable from 2026, old 50%, two-dwelling and Rent Act conditions | https://www.skatturinn.is/einstaklingar/fjarmagnstekjur/leigutekjur/ | 2026-11-14 |

Not yet confirmed: the Alþingi text of the Income Tax Act as at 14 Nov 2026 (403 today), including the Article 66(3) lease-registration condition and the Article 58(3) and 58(4) wording quoted here from the 30 Oct 2026 reading; the statute behind the first-home scheme (Act 111/2016), not opened; the municipal rate of the client's municipality, which replaces the 14.94% average in the worked cases.
