---
name: cross-border-tax-router
description: "Entry point for cross-border personal tax questions, tax year 2026: US citizens abroad, dual residence, moves, non-dom enquiries, expatriation, foreign companies and trusts. Collect the country, citizenship, residence, domicile and event map; select country, corridor and topic Guides; identify gaps and a proposed sequence; hand off to cross-border-tax-workflow-base. This router computes no tax and determines no residence, treaty entitlement, reporting obligation or filing position."
version: "1.0"
jurisdiction: GLOBAL
tax_year: 2026
last_updated: 2026-11-26
category: international
type: router
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: cross-border
---

# Cross-border tax router: which Guides to load when a case touches more than one country v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope and who this is for

Tax year 2026. Use this router for personal tax facts touching more than one country. It collects facts and selects Guides; it does not settle citizenship, residence, domicile, source, entity characterisation, tax liability, return lines or reporting duties. Country and topic Guides need their own applicable-year sources and conditions checked. Listing a destination here does not prove its contents or guarantee complete coverage.

Preserve the person's case, including every country, date, amount and event. For example, a **US citizen living in Australia who wants to sell shares** needs both countries kept in the plan. Route the US questions to the US Guides and the Australian questions to `au-tax-residency-2` and the relevant Australian Guide. Do not supply Australian rules from this router.

The output is an unreviewed working paper, not advice, an engagement or a filed return. Hand it to a licensed accountant in each relevant jurisdiction before action.

## Ask for missing facts

Read the existing case materials first. Collect together:

- All citizenships, whether or not a passport is held; current and former US green-card status and dates. Record green-card status separately from citizenship.
- Countries lived in during the year, arrival/departure dates, homes available, family and economic ties, and proposed moves.
- Each income item, sale, gift or other event, its country connections and exact date; preserve the original amounts and years.
- Foreign companies, trusts, partnerships, pensions and investment funds owned or benefited from.
- Returns already filed, treaty claims, elections and taxes already paid or withheld in each country.

## The method, step by step

### Step 0: Build the map; leave unresolved facts unresolved

For every country, record citizenship, possible domestic tax residence and dates, domicile or newcomer-regime questions, source-country connections, and the events being planned. Request the applicable domestic test from that country's Guide. Do not assume that residence, citizenship or source alone establishes every taxing right.

| Question to investigate | Where to route; no tax result is stated here |
| --- | --- |
| US citizenship and worldwide-income questions | `us-citizen-moving-abroad-tax`, `us-foreign-earned-income-2555`, `us-foreign-tax-credit-1116` |
| Domestic residence, including green-card, substantial-presence, first-year-election or UK statutory-residence-test questions | `us-tax-residency`, `uk-statutory-residence-test`, `ca-tax-residency`, `in-tax-residency`, `sg-tax-residency`, `za-tax-residency`, `nz-tax-residency`, `au-tax-residency-2`, `ae-tax-residency` |
| Domicile, non-dom or newcomer questions | `mt-non-dom`, `ie-non-dom`, `cy-non-dom`, `uk-non-dom` |
| Income, assets, property or business connections to a source country | The relevant country Guide; `us-nonresident-cgt`; `permanent-establishment-risk` |

**US boundary.** US citizens and resident aliens generally come within US worldwide-income taxation; do not assume that living abroad settles US liability. Determine applicable Code and treaty exceptions, relief and filing requirements in the US Guides and operative sources. Do not replace this with “the US right is always on” or “residence changes only relief.” [IRS, citizens and resident aliens abroad](https://www.irs.gov/individuals/international-taxpayers/us-citizens-and-resident-aliens-abroad).

**UK non-dom boundary.** The 4-year foreign income and gains (FIG) regime replaced the remittance basis on **6 April 2025**. That date is a routing warning, not a finding that the person qualifies: send eligibility, remaining years, qualifying income/gains, claims and lost allowances to `uk-non-dom`. [HMRC, FIG regime](https://www.gov.uk/guidance/check-if-you-can-claim-the-4-year-foreign-income-and-gains-regime).

If any material fact is missing, label the affected tax or filing conclusion **undetermined; do not use**. Ask for the missing evidence and list the issue for review. A conservative scenario may be shown separately with explicit assumptions; it is not a legal conclusion or an instruction to file an unnecessary return. Apply this boundary when using the conservative-default discussion in `cross-border-tax-workflow-base` too. Do not compute until the necessary citizenship/status, residence evidence and event facts are established.

### Step 1: Select topics and corridors

These are search signals, not findings of liability, entitlement or a filing duty. Retrieve the current destination; check its scope, year and operative sources before applying it. All Australian, Indian, Singaporean, Chinese, South African and New Zealand references here are routes only.

| Signal in the facts | Topic Guides to retrieve |
| --- | --- |
| US citizen or green-card holder abroad; foreign salary or foreign taxes | `us-foreign-earned-income-2555`, `us-foreign-tax-credit-1116`; assess eligibility and interaction there |
| Foreign bank, brokerage or pension accounts and a possible US connection | `us-fbar-fatca-reporting`, `us-fbar-and-fatca-8938` |
| Foreign company with US owners or a US person's foreign-company interest | `us-gilti-fdii-beat` for subpart F / net CFC tested income enquiries; `us-form-5471-cfc-information` for Form 5471 enquiries |
| Foreign trust grantor, owner or beneficiary; gifts or inheritances from non-US persons | `us-foreign-trust-reporting` |
| US citizen or long-term green-card holder considering giving up status | `us-expatriation-exit-tax` |
| Possible US residence, or arrival/departure mid-year | `us-tax-residency` |
| Non-US person selling US assets | `us-nonresident-cgt` |
| Treaty residence, reduced withholding or double-tax relief | `oecd-model-treaty-defaults` as a model-text reference only; `withholding-tax-matrix`; the actual treaty and protocols, followed by the treaty gate below |
| Departure-tax question | `us-expatriation-exit-tax`, `leaving-australia-tax-residency-cgt`, `leaving-france-exit-tax`, `leaving-south-africa-tax-emigration`, `ca-tax-residency`, `norway-to-switzerland-wealth-tax-exit`, `germany-to-switzerland-cross-border-tax` |
| Non-dom or newcomer question | `uk-non-dom`, `mt-non-dom`, `ie-non-dom`, `cy-non-dom`, `moving-to-malta-tax-residence` |
| Worker connected to multiple EU, EEA, Swiss or UK social-security systems | `eu-social-security-coordination`, `cross-border-payroll-coordination` |
| Exchange of account information between authorities | `fatca-crs-automatic-exchange` |
| Foreign family holding company / possible CFC issue | `cfc-and-substance-rules-compared` |

| Move or corridor from the original case | Corridor Guide to retrieve |
| --- | --- |
| US citizen moving abroad | `us-citizen-moving-abroad-tax` |
| UK to the UAE | `uk-to-uae-relocation-tax` |
| UK to Italy | `uk-to-italy-flat-tax-relocation` |
| India to the UAE or Singapore | `india-to-uae-singapore-nri-tax` |
| China to Singapore | `china-to-singapore-relocation-tax` |
| Germany to Switzerland | `germany-to-switzerland-cross-border-tax` |
| Leaving Australia | `leaving-australia-tax-residency-cgt` |
| Moving between US states | `us-multi-state-residency-and-allocation` |

Also retrieve a relevant country Guide for every country in the map. Do not silently discard an uncovered country or present the covered country's answer as the whole answer.

### Step 2: Scope and treaty gates

Check the current catalog rather than asserting that a topic has no dedicated Guide. Use this referral for any unresolved or specialist application: **Check this point with one of our partner accountants.** Identify the affected topic, country and missing evidence alongside that sentence.

| Question needing a gate | Action |
| --- | --- |
| Another country's treatment, or a missing/insufficient country or corridor Guide | Keep the country's issue in the plan; use the partner-accountant referral above for the unresolved treatment. Never borrow another country's rule. |
| Actual treaty residence, a reduced rate, relief or a named treaty article | Retrieve and read the operative treaty, protocols and effective dates. Check person/tax coverage, domestic-law interaction, residence definition, any tie-breaker and saving-clause exceptions. Use the partner-accountant referral above for the application. Never adopt a model result as the actual treaty result. |
| US state residence or sourcing | Retrieve `us-multi-state-residency-and-allocation` and the relevant state Guide; refer the unresolved application. |
| Foreign mutual funds or ETFs held by a US person / PFIC | Search current Guides; retain `us-fbar-and-fatca-8938` as a reporting pointer. Use the partner-accountant referral above for PFIC classification and treatment. |
| Social security beyond the EU, EEA, Swiss and UK routes; foreign pension character | Search applicable country/coordination Guides. Use the partner-accountant referral above for the unresolved issue. |
| Cross-border estate, gift or inheritance | Retrieve `inheritance-estate-gift-matrix` as a starting point; use the partner-accountant referral above for the actual application. |
| Non-US anti-deferral / EU or UK CFC question | Retrieve `cfc-and-substance-rules-compared` and `eu-directives-cross-border`; retain Malta, Ireland, Cyprus, Netherlands, Luxembourg and UK as country questions to investigate. Use the partner-accountant referral above for the national application. |

**UK–US treaty example retained as a reading route.** In the [UK–US convention](https://www.gov.uk/government/publications/usa-tax-treaties/2001-uk-usa-double-taxation-convention-as-amended-by-the-2002-protocol-in-force), request review of Article 4(1)–(2) before the individual tie-breaker in Article 4(4). Preserve the questions of permanent home, centre of vital interests, habitual abode, nationality and competent-authority mutual agreement for that review; this router does not decide their outcome. Read Article 1(4) together with **all** Article 1(5) saving-clause exceptions. Do not import the OECD Model Article 4(2) into an actual treaty. For the person's treaty position: **Check this point with one of our partner accountants.**

For a dual-resident non-citizen's US income-tax computation, other-purpose resident status, Form 1040-NR and Form 8833 questions, retrieve `us-tax-residency` and check the applicable provisions. For the actual filing position: **Check this point with one of our partner accountants.** No universal dual-resident filing rule is supplied here.

Tell the person which part can be researched from retrieved Guides, which part remains undetermined, and which specialist must clear it. Do not turn a coverage gap into an assumed tax result.

### Step 3: Propose a sequence for review

Keep the actual chronology. The order below is a research dependency list, not a finding that a tax is imposed or relief is available. Review the relevant country and treaty rules before recommending an event date.

| Combined fact pattern retained | Questions to resolve before computation or action |
| --- | --- |
| Changing residence and selling an asset | Establish potential residence-change and sale dates for each country, then investigate sale and departure treatment, source-country issues and any relief. Keep Canada's deemed-disposition / departure-tax question in `ca-tax-residency` and the UK's temporary-non-residence / return question in `uk-statutory-residence-test`. For their application: **Check this point with one of our partner accountants.** |
| US citizen and anything else | Include the US topic review alongside every other relevant country. Test applicable exceptions and relief; never promise that a credit, exclusion or treaty removes all double tax. |
| Green-card holder considering treaty residence elsewhere | Retrieve `us-tax-residency` and `us-expatriation-exit-tax` together before an election or filing. Preserve long-term-resident status, section 7701(b)(6), section 877A, treaty-benefit waiver, IRS notification, and Forms 8833 and 8854 as questions to check, not established requirements or a finding of exit tax. For the application: **Check this point with one of our partner accountants.** |
| Foreign trust distribution or sale | Ask `us-foreign-trust-reporting` to investigate grantor/non-grantor status, ownership, the sale/distribution and reporting before determining who is taxed. |
| Expatriation followed by a sale | Retrieve `us-expatriation-exit-tax`; ask for the applicable section 877 / 877A, long-term-resident and covered-expatriate analysis before recommending the sale sequence. For the application: **Check this point with one of our partner accountants.** |
| Foreign-company income followed by a distribution | Retrieve `us-gilti-fdii-beat` and `us-form-5471-cfc-information`; investigate any prior inclusion and later distribution together, without assuming a particular inclusion or automatic relief from double counting. |

Explain the proposed order using the person's actual dates: residence/status questions, the country A and country B event questions, then any available relief and reporting. State which dependency remains undetermined; do not imply that residence at sale is the sole taxing test.

### Step 4: Handoff and self-check

1. Load `cross-border-tax-workflow-base`, subject to this router's missing-facts and treaty boundaries.
2. Load the selected topic, corridor and country Guides; confirm each exists in the current catalog.
3. Produce an ordered working-paper plan showing the country map, evidence, event dates, rules still to establish, potential relief and forms to check, and every issue for the reviewing accountants. Say only what was actually retrieved.
4. Check that every original country, example, amount, year and topic remains accounted for; citizenship and green-card status are separate; unresolved residence/source/domicile questions remain visible; no uncovered treatment is invented; and no calculation has started inside the router.
## When to refuse or refer

Refer unresolved applications through Step 2. Hand off before any sale, distribution, residence/status change, citizenship or green-card surrender, election or filing. Do not take those actions through this router.

## Sources

These reads support only the limited boundary statements or named reading routes above, not approval of the linked Guides or an individual outcome.

| Source and scope actually read | URL | Read on |
| --- | --- | --- |
| IRS citizens and resident aliens abroad: opening worldwide-income statement; relevant-return relief caveat | https://www.irs.gov/individuals/international-taxpayers/us-citizens-and-resident-aliens-abroad | 2026-11-26 |
| HMRC FIG guidance: replacement date; eligibility, claims and allowance sections checked to keep the route from implying entitlement | https://www.gov.uk/guidance/check-if-you-can-claim-the-4-year-foreign-income-and-gains-regime | 2026-11-26 |
| UK–US convention: Article 4(1)–(4) and Article 1(4)–(5), reading route only | https://www.gov.uk/government/publications/usa-tax-treaties/2001-uk-usa-double-taxation-convention-as-amended-by-the-2002-protocol-in-force | 2026-11-26 |

Not yet confirmed: this router establishes no individual residence, treaty entitlement, tax, relief or filing outcome. Unresolved applications remain referred or marked undetermined; do not use.
