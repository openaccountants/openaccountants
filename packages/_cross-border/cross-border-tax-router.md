---
name: cross-border-tax-router
description: Entry point for the OpenAccountants cross-border / international personal-tax skill library. ALWAYS load this skill first when a person's facts touch more than one country — e.g. a US citizen living abroad, a dual resident, someone moving countries, a non-dom, an expatriating citizen, a foreign trust or foreign company owner, or "how is this taxed in country A and country B". The router computes nothing. It (1) builds the person's residency / citizenship / domicile map, (2) identifies which country skills and which international topic skills the facts engage, (3) gates out corridors the library does not yet cover, (4) SEQUENCES the steps — in cross-border, the order of events changes the tax (sever residency before vs. after a sale), and (5) hands off to cross-border-tax-workflow-base plus the topic skills. Every international topic skill (FEIE/FTC, FBAR/FATCA, CFC/GILTI, foreign trusts, exit tax) assumes this routing step has happened first.
version: 0.1
jurisdiction: GLOBAL
tax_year: 2026
last_updated: 2026-10-05
authored_by: OpenAccountants team
review_status: pending_review
trust_label: Written by the OpenAccountants team
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Cross-border tax router: which Guides to load when a case touches more than one country

Figures are for tax year 2026. This Guide carries no rates, thresholds or amounts. Those live in the country Guides it routes to, and each country Guide proves its own figures against its own tax authority. This Guide is the entry point for any personal tax question whose facts touch more than one country. It builds the person's map (citizenship, residence and domicile in each country), names the country and topic Guides the facts engage, fixes the order in which the events must be tested, and hands off to `cross-border-tax-workflow-base`. It computes no tax.

## What this file is

The entry point for the cross-border personal tax Guides. Before any topic Guide runs, three things must be settled: who the person is to each tax system (citizenship, residence, domicile), which countries' rules engage, and in what order the events happen. This Guide settles all three, then loads `cross-border-tax-workflow-base` and the right country and topic Guides.

The person never needs to see this Guide. They describe a situation in plain words, such as being a US citizen living in Australia who wants to sell shares, and the assistant uses this Guide to decide what to load.

The router computes nothing: no tax, no characterisation, no return lines. If you find yourself computing a liability here, you have skipped the hand-off.

Why a router exists. Within one country the rules fit together. Across borders the same income can be taxed by two systems, a treaty can reallocate the taxing right, and the order of events (when residence ends, when an asset is sold, when a person gives up citizenship) can change which country taxes at all. A single-country answer to a two-country question is incomplete by construction.

## The method, step by step

1. **Build the map for every country in play.** For each country record citizenship, tax residence under that country's own domestic test, and domicile where the country still uses it. Residence is decided country by country, each under its own law, and a person can be resident in two countries at once. The US test for non-citizens is the green card test or the substantial presence test for the calendar year ([IRS: determining an individual's tax residency status](https://www.irs.gov/individuals/international-taxpayers/determining-an-individuals-tax-residency-status)); route the detail to `us-tax-residency`. The UK decides residence one tax year at a time under the statutory residence test ([HMRC RDR3](https://www.gov.uk/government/publications/rdr3-statutory-residence-test-srt/guidance-note-for-statutory-residence-test-srt-rdr3)); route the detail to `uk-statutory-residence-test`.
2. **Mark every taxing basis.** A US citizen or resident alien is taxed on worldwide income wherever they live ([IRS: US citizens and resident aliens abroad](https://www.irs.gov/individuals/international-taxpayers/us-citizens-and-resident-aliens-abroad)). So for a US citizen the US taxing right is always on, and a finding that the person is not resident in the US changes only the relief, never the right. Income can also be taxed both by the country of residence and by the country it comes from: HMRC says a UK resident "may be taxed on your foreign income by the UK and by the country where your income is from" ([GOV.UK: if you're taxed twice](https://www.gov.uk/tax-foreign-income/taxed-twice)). A domicile test still matters in some countries (see the table in Step 0); the UK replaced its remittance basis with the 4-year foreign income and gains (FIG) regime on 6 April 2025, which is only available to a qualifying resident ([GOV.UK: 4-year foreign income and gains regime](https://www.gov.uk/guidance/check-if-you-can-claim-the-4-year-foreign-income-and-gains-regime)).
3. **If two countries both treat the person as resident, flag the treaty tie-breaker.** A treaty tie-breaker decides a single treaty residence. In the UK and US convention the order is a permanent home; if there is a permanent home in both States, the centre of vital interests; if that cannot be determined, or there is no permanent home in either State, habitual abode; then nationality; then mutual agreement ([UK and US double taxation convention, Article 4](https://www.gov.uk/government/publications/usa-tax-treaties/2001-uk-usa-double-taxation-convention-as-amended-by-the-2002-protocol-in-force)). Other treaties use their own text, so read the named treaty. `oecd-model-treaty-defaults` carries the model tie-breaker cascade (Article 4(2) of the OECD Model). `cross-border-tax-workflow-base` carries the tie-breaker step for the UK and US convention (Article 4(4)) and the treaty-bridge convention, including the check of the US saving clause. The tie-breaker does not take a US citizen out of US tax. The UK and US convention keeps each State's right to tax "by reason of citizenship ... its citizens, as if this Convention had not come into effect" (Article 1(4), subject to the exceptions in Article 1(5)) ([UK and US double taxation convention](https://www.gov.uk/government/publications/usa-tax-treaties/2001-uk-usa-double-taxation-convention-as-amended-by-the-2002-protocol-in-force)). A dual-resident taxpayer who claims treaty benefits "must file a return using Form 1040-NR with Form 8833 attached, and compute your tax as a nonresident alien", and is treated as a US resident "for purposes other than figuring your tax" ([IRS Publication 519](https://www.irs.gov/publications/p519)).
4. **Pick the Guides the facts engage** from the tables in Step 1: one residence or country Guide per country in the map, plus the topic Guides the facts trigger, including reporting the person did not ask about.
5. **Run the scope gate** in Step 2. Say plainly which part no Guide covers.
6. **Fix the order of events** with Step 3 before anything is computed, and tell the person the order and why.
7. **Hand off** as in Step 4: load `cross-border-tax-workflow-base` first, then the topic Guides, then the country Guides in the order fixed in Step 3.

## Ask the client first

- Which citizenships do you hold, with or without a passport, and do you hold, or have you ever held, a US green card?
- Which countries were you living in during the tax year, on which dates did you arrive and leave, and where do you have a home available to you?
- Are you moving, or planning to move, and when exactly will each move happen?
- What is the income, sale, gift or other event, and on what date will it happen?
- Do you own or benefit from any foreign company, trust, partnership, pension or investment fund?
- Have you already filed returns, or claimed treaty relief, in any of these countries for this year?

## Step 0: Build the residency, citizenship and domicile map

**Basis a country may tax on**

| Basis a country may tax on | Typical trigger | Where to route |
| --- | --- | --- |
| Citizenship (worldwide, wherever the person lives) | Being a citizen of that country (a passport is not the test) | The United States: `us-citizen-moving-abroad-tax`, `us-feie-ftc` |
| Tax residence (worldwide while resident) | Days present, a home, ties, centre of interests, each under that country's own test | `us-tax-residency`, `uk-statutory-residence-test`, `ca-tax-residency`, `in-tax-residency`, `sg-tax-residency`, `za-tax-residency`, `nz-tax-residency`, `au-tax-residency-2`, `ae-tax-residency` |
| Domicile or a special regime for newcomers | Domicile, or a time-limited regime for new arrivals | `mt-non-dom`, `ie-non-dom`, `cy-non-dom`; for the UK from 6 April 2025, `uk-non-dom` |
| Source (that country's income only) | Income arising there, property there, a business presence there | The country Guide for the source country; `us-nonresident-cgt`; `permanent-establishment-risk` |

Capture, in one structured block:

~~~
Cross-border map: for each country in play, record
  1. Citizenship(s) held, including any US green card (citizenship taxation and exit-tax tests)
  2. Tax residence(s) now, and any change of residence in play, with dates (each country's residence test)
  3. Domicile, where a country in the map still uses it (non-dom and newcomer regimes)
  4. The income, asset or event in question, and WHEN each happens (sequencing)
  5. Any foreign companies, trusts, partnerships, pensions or funds owned or benefited from (anti-deferral and reporting Guides)
If one of these is missing, assume the position that gives the broader taxing right
and triggers the reporting obligation (cross-border-tax-workflow-base, conservative default),
and say so.
~~~

Do not go past Step 0 until citizenship, current residence in each country, and the event in question are known. Those three decide which Guides load.

## Step 1: Identify the corridors and topics the facts engage

**Signal in the facts and the topic Guide to load**

| Signal in the facts | Topic Guide |
| --- | --- |
| US citizen or green card holder living or working abroad; foreign salary; foreign taxes paid | `us-feie-ftc`, then `us-foreign-earned-income-2555` or `us-foreign-tax-credit-1116` |
| US person with foreign bank, brokerage or pension accounts | `us-fbar-fatca-reporting`, `us-fbar-and-fatca-8938` |
| US person owning a large stake in a foreign company; a foreign company with US owners | `us-cfc-gilti`, `us-form-5471-cfc-information` |
| US person who is a grantor, owner or beneficiary of a foreign trust; gifts or inheritances from non-US persons | `us-foreign-trust-reporting` |
| US citizen or long-term green card holder giving up US status | `us-expatriation-exit-tax` |
| Non-citizen who may be a US resident, or who arrives or leaves the US mid-year | `us-tax-residency` |
| Non-US person selling US assets | `us-nonresident-cgt` |
| A position that relies on a tax treaty (residence tie-breaker, reduced withholding, relief article) | `oecd-model-treaty-defaults` for the model wording; the named treaty itself for the actual article; `withholding-tax-matrix` for withholding |
| Someone leaving a country that may charge tax on departure | `us-expatriation-exit-tax`, `leaving-australia-tax-residency-cgt`, `leaving-france-exit-tax`, `leaving-south-africa-tax-emigration`, `ca-tax-residency`, `norway-to-switzerland-wealth-tax-exit`, `germany-to-switzerland-cross-border-tax` |
| A non-dom or newcomer regime | `uk-non-dom`, `mt-non-dom`, `ie-non-dom`, `cy-non-dom`, `moving-to-malta-tax-residence` |
| A worker whose social security could fall in more than one EU, EEA, Swiss or UK system | `eu-social-security-coordination`, `cross-border-payroll-coordination` |
| Accounts reported between tax authorities | `fatca-crs-automatic-exchange` |

**Corridor Guides already written for a whole move**

| Move | Corridor Guide |
| --- | --- |
| US citizen moving abroad | `us-citizen-moving-abroad-tax` |
| UK to the UAE | `uk-to-uae-relocation-tax` |
| UK to Italy | `uk-to-italy-flat-tax-relocation` |
| India to the UAE or Singapore | `india-to-uae-singapore-nri-tax` |
| China to Singapore | `china-to-singapore-relocation-tax` |
| Germany to Switzerland | `germany-to-switzerland-cross-border-tax` |
| Leaving Australia | `leaving-australia-tax-residency-cgt` |
| Moving between US states | `us-multi-state-residency-and-allocation` |

Then load the country Guides for each country in the map through the normal single-country flow. The router's job is to bind the topic Guides to the country Guides in the right order.

If the facts match a topic, route to it (Step 4). If a needed country or corridor is missing, go to Step 2.

## Step 2: Scope gate, what the library does not cover yet

The library covers the US citizen and US resident side in depth, the residence tests of the countries listed in Step 0, the non-dom and newcomer regimes listed there, and the corridor Guides in Step 1. Many situations still sit partly outside it. Route the covered part to the closest Guide, and name the part that needs a local accountant.

**If the person actually needs... and what to say**

| If the person actually needs... | What to say |
| --- | --- |
| The other country's own treatment of the same event, where no Guide for that country covers it | Load that country's Guide if it exists. If not, name it as an open item for a local accountant. Never borrow another country's rule. |
| A specific article of a named treaty, read in full | `oecd-model-treaty-defaults` gives the model wording only. Actual treaties differ from the model and from each other. Flag the named article for human review. |
| US state residency or sourcing | `us-multi-state-residency-and-allocation` and the relevant state Guide. Flag it if a state is in play. |
| Foreign mutual funds or ETFs held by a US person (PFIC) | No dedicated Guide yet. `us-fbar-and-fatca-8938` touches the regime. Flag it for a specialist. |
| Social security outside the EU, EEA, Swiss and UK coordination rules, or a foreign pension's character | Not covered beyond `eu-social-security-coordination`. Flag it. |
| Estate, gift or inheritance tax across borders | `inheritance-estate-gift-matrix` is a starting point only. Situs and treaty rules differ sharply from income tax. Flag it. |
| A non-US anti-deferral regime (an EU or UK controlled foreign company rule) | `eu-directives-cross-border` describes the EU directive layer only. The national rule needs a local accountant. |

### Out-of-scope message template

> Tell the person that the [covered part] can be worked using [Guide], but [the other country's treatment / the named treaty article / PFIC / estate tax] is not covered and turns on facts that should not be guessed across a border. Flag that part to a local accountant rather than improvising, and ask whether to handle the covered part and mark the rest as open items for sign-off.

Never invent another country's treatment or a treaty outcome. The conservative default in `cross-border-tax-workflow-base` governs missing facts inside a covered topic. It is not permission to invent an uncovered country's rule.

## Step 3: Sequence, the order of events changes the tax

When two or more steps apply, test them in the order the events occur and the taxing rights attach. Later steps depend on earlier ones.

**Combined fact pattern, order, and why**

| Combined fact pattern | Order | Why |
| --- | --- | --- |
| Changing tax residence and selling an asset | Fix the date residence ends in each country first, then test the sale under each country's rule as of that date | Whether a country can tax a gain often turns on residence at the moment of sale. Some countries also treat a departing resident as having sold certain property on departure: Canada calls this a deemed disposition, on which the person may have to report a capital gain known as departure tax ([CRA: leaving Canada](https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/individuals-leaving-entering-canada-non-residents/leaving-canada-emigrants.html)). The UK can tax certain income and gains on return after a period of temporary non-residence ([HMRC RDR3](https://www.gov.uk/government/publications/rdr3-statutory-residence-test-srt/guidance-note-for-statutory-residence-test-srt-rdr3)). |
| US citizen and anything else | Apply the US topic Guide to every item, then use the credit, exclusion or treaty to relieve double tax | Citizenship taxation means a non-US residence finding never removes the US right; it changes only the relief. |
| A green card holder who becomes treaty resident elsewhere | Test the treaty tie-breaker and the expatriation rules together, before the return is filed | If a treaty tie-breaker treats the person as a non-resident alien, this can in certain instances trigger the section 877A expatriation tax ([IRS Publication 519](https://www.irs.gov/publications/p519)). The IRS says a long-term resident (section 7701(b)(6)) stops being a lawful permanent resident for this purpose if the individual "commences to be treated as a resident of a foreign country under the provisions of a tax treaty", "does not waive the benefits of the treaty" and "notifies the IRS of such treatment on Forms 8833 and 8854" ([IRS: expatriation tax](https://www.irs.gov/individuals/international-taxpayers/expatriation-tax)). A green card holder who is not a long-term resident is outside this rule. Route to `us-tax-residency` and `us-expatriation-exit-tax`. |
| Foreign trust distribution or sale | Characterise the trust (grantor or non-grantor) first, then the distribution | Who is taxed on the trust's income depends on that first answer. Route to `us-foreign-trust-reporting`. |
| Expatriation in play | Run the covered expatriate and exit tax test before planning any later sale | The expatriation rules in sections 877 and 877A apply to US citizens who renounce and to long-term residents who end their US resident status; whether exit tax is due turns on further tests ([IRS: expatriation tax](https://www.irs.gov/individuals/international-taxpayers/expatriation-tax)). Route to `us-expatriation-exit-tax`. |
| Controlled foreign company income plus a later distribution | The shareholder's inclusion first, then the distribution | Avoids counting the same income twice. Route to `us-cfc-gilti`. |

State the order to the person before anything is computed:

> Tell the person that the order matters: fix [the date your residence ends] first, because [whether the gain is taxed depends on residence at the sale], then apply [country A] and [country B] to the sale as of that date, then [the relief].

## Step 4: Handoff

1. Load `cross-border-tax-workflow-base`. It is the shared method: the residence map, the treaty bridge, the conservative default, the flash points and the hand-off to a licensed accountant.
2. Load the topic Guides identified in Step 1.
3. Load the country Guides for each country in the map, applied in the order fixed in Step 3.

Then tell the person, in one line, what you loaded and what you will produce:

> Tell the person that the cross-border workflow, [topic Guides] and the [country] Guides have been loaded. Produce an ordered plan: the steps in order, each country's treatment at each step, how double tax is relieved, the forms each step triggers, and the open points for a licensed accountant in the lead country. Ask for any missing facts first.

Hand control to the structured intake in `cross-border-tax-workflow-base`. Do not start computing inside the router.

## Router self-checks

Before handing off, confirm:

- [ ] Citizenship, residence and (where used) domicile captured for every country in play
- [ ] Every taxing basis identified: citizenship for the US, residence, domicile or newcomer regime, source
- [ ] A possible dual residence flagged for the treaty tie-breaker
- [ ] Every topic the facts touch identified, including reporting the person did not ask about
- [ ] Every uncovered part (another country's rule, a named treaty article, PFIC, estate tax) named, not improvised
- [ ] The order of events fixed and stated to the person before any computation
- [ ] `cross-border-tax-workflow-base` loaded alongside the topic Guides, never a topic Guide alone
- [ ] Every Guide named in the plan is one the catalog returns

## When to refuse or refer

- Refuse to give a single-country answer to a question whose facts touch two countries. Route it instead.
- Refer to a licensed accountant in the relevant country any part that no Guide covers, including the domestic rule of a country with no Guide.
- Refer any position that depends on a specific article of a named treaty, after reading that article.
- Refer before the person acts on anything that cannot be undone: a sale, a distribution, giving up residence, giving up citizenship or a green card, or filing.
- Refer any foreign fund held by a US person, and any cross-border estate, gift or inheritance question.
- Refuse to state another country's rate, threshold or rule from memory. Load the country Guide or flag the gap.

## PROHIBITIONS

- Never compute or characterise tax inside the router. Route and hand off.
- Never load a topic Guide without also loading `cross-border-tax-workflow-base`.
- Never answer a multi-country question one country at a time as if the others did not exist.
- Never assume a non-US residence finding removes the US citizenship taxing right. It changes only the relief.
- Never invent another country's domestic rule or a treaty outcome. Name it and flag it for a local accountant.
- Never plan a sale before fixing the date residence ends and, where relevant, the expatriation test.

## Sources

- [IRS: determining an individual's tax residency status](https://www.irs.gov/individuals/international-taxpayers/determining-an-individuals-tax-residency-status)
- [IRS: US citizens and resident aliens abroad](https://www.irs.gov/individuals/international-taxpayers/us-citizens-and-resident-aliens-abroad)
- [IRS Publication 519, US tax guide for aliens](https://www.irs.gov/publications/p519)
- [IRS: expatriation tax](https://www.irs.gov/individuals/international-taxpayers/expatriation-tax)
- [UK and US double taxation convention, as amended by the 2002 protocol](https://www.gov.uk/government/publications/usa-tax-treaties/2001-uk-usa-double-taxation-convention-as-amended-by-the-2002-protocol-in-force)
- [HMRC RDR3, statutory residence test guidance](https://www.gov.uk/government/publications/rdr3-statutory-residence-test-srt/guidance-note-for-statutory-residence-test-srt-rdr3)
- [GOV.UK: check if you can claim the 4-year foreign income and gains regime](https://www.gov.uk/guidance/check-if-you-can-claim-the-4-year-foreign-income-and-gains-regime)
- [GOV.UK: if you're taxed twice](https://www.gov.uk/tax-foreign-income/taxed-twice)
- [CRA: leaving Canada, emigrants](https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/individuals-leaving-entering-canada-non-residents/leaving-canada-emigrants.html)

## Disclaimer

This Guide routes between cross-border tax Guides. It is not tax, legal or financial advice, is not an engagement, and does not produce a filed return. Cross-border outcomes turn on entity and treaty facts and significant judgement, and the order of events often changes the result. Everything the loaded Guides produce is a working paper until a licensed accountant in the relevant country reviews and signs it off, and the work must end by handing that working paper to that accountant.

The most up-to-date version of this Guide is maintained at openaccountants.com.

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
