---
name: us-foreign-tax-credit-1116
description: Tier 2 US federal content skill for §901 Foreign Tax Credit (Form 1116) covering tax year 2025. Includes the basket separation under §904 (passive, general, GILTI, foreign branch, §901(j) sanctioned countries), the §904(a) limitation formula, the $300/$600 de minimis no-Form-1116 election, §904(j) high-tax kick-out for passive income, the 2022 T.D. 9959 attribution/nexus/cost-recovery requirements with Notice 2023-55/2024-44 (and successor) relief, the FEIE-vs-FTC strategic choice for US expats, 1-year back / 10-year forward credit carries, and the AMT FTC computation. Schedule A itemized deduction alternative when credit isn't useful.
jurisdiction: US
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: James Wallach
review_status: current
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# US Foreign Tax Credit 1116

## 1. Scope

This skill covers the §901 Foreign Tax Credit (FTC) for **individual** US taxpayers filing Form 1040 — citizens and resident aliens with foreign-source income on which a foreign income tax has been paid or accrued. It is a Tier 2 federal content skill consumed by `us-federal-return-assembly` and by the US expat workflows.

**In scope:**
- Form 1116 preparation for individuals (citizens, green-card holders, resident aliens).
- The five separate §904 baskets (passive, general, GILTI, foreign branch, §901(j) sanctioned).
- The §904(a) limitation formula and the basket-by-basket overall foreign loss / overall domestic loss accounting at a summary level.
- The de minimis $300 / $600 no-Form-1116 election.
- The high-tax kick-out rule for passive income.
- Carryback (1 year) and carryforward (10 years) of excess credits.
- The 2022 T.D. 9959 / 2024 T.D. 9982 attribution-and-nexus regulations and the temporary relief in Notice 2023-55 and Notice 2023-80 relief, which Pub. 514 describes as extended until further notice.
- The strategic choice between §911 FEIE and the FTC for US expats.
- AMT FTC computation on a second Form 1116.
- The Schedule A itemized deduction alternative under §164(a)(3).

**Out of scope — refer out:**
- C corporation FTC and the §960 deemed-paid credit for **corporate** US shareholders of CFCs — refer to a corporate-tax skill (or `us-gilti-fdii-beat` if added later). This skill addresses §951A GILTI **only** for individual §962 electors at a high level.
- Treaty re-sourcing under §865(h) and §904(d)(6) for sophisticated treaty positions — flag and refer to a credentialed international tax practitioner.
- §901(m) covered asset acquisitions — cross-border step-up structuring; refer out.
- §901(k)/(l) holding-period restrictions on dividends and the §901(l) substantially-similar-position rules — flag at the intake stage and refer out for material exposures.
- §905(c) foreign tax redetermination procedures requiring a Form 1040-X — refer out.
- Form 8865, Form 5471, Form 8858, Form 8621 informational compliance — refer out (this skill consumes their outputs as foreign-source income inputs, but does not prepare them).
- State conformity beyond a general "most states do not allow an FTC" warning — state-tax skills handle their own jurisdictions.

**Workflow base:** load alongside `us-tax-workflow-base` v0.2+.

## 2. Why the FTC exists: the §901 policy

The US taxes its citizens and residents on worldwide income. Foreign countries tax the same income (typically on a source basis). Without relief, the same dollar would be taxed twice. §901 allows the US taxpayer to **credit** foreign income taxes paid or accrued against the US tax otherwise due on the same foreign income, dollar for dollar, subject to the §904(a) limitation.

The credit is non-refundable: it can reduce US tax to zero but not below. Excess credits become a carryback / carryforward (see §6).

## 3. Credit vs. deduction — the §164(a)(3) choice

- **Election is annual and applies to all foreign income taxes** — A taxpayer may either credit the foreign income tax under §901 (Form 1116, flows to Schedule 3 line 1) or deduct it as an itemized deduction under §164(a)(3) (Schedule A). The election is annual and applies to all foreign income taxes of the year — you cannot credit some and deduct others (§275(a)(4) bars double benefit).  _(§164(a)(3); §275(a)(4))_

**Factors favoring credit vs deduction**

**Factors favoring credit vs deduction**  _(§164(a)(3) vs §901)_

| Factor | Favors credit (Form 1116) | Favors deduction (Schedule A) |
| --- | --- | --- |
| Effect on tax | Dollar-for-dollar reduction of US tax | Reduction of taxable income at the marginal rate |
| US tax liability | Any positive US tax | Only useful if itemizing — and even then worth ~22-37 cents per dollar of foreign tax |
| Standard vs. itemized | Works alongside standard deduction | Requires itemizing (lose standard deduction worth $15,750 single / $31,500 MFJ for 2025) |
| Excess foreign tax | Carries 1 back / 10 forward | No carry — use it or lose it |
| Form 1116 complexity | Required (unless de minimis election applies) | No Form 1116 needed |

- **Default rule for choosing credit vs deduction** — The credit is almost always better. Take the deduction only if (a) the taxpayer itemizes for other reasons (large mortgage interest, state SALT cap room, large charitable), AND (b) US tax in the current year is too low to absorb the credit, AND (c) carryforward is not useful (e.g., taxpayer is permanently leaving the US tax system after this year).  _(§901 vs §164(a)(3))_

**Reviewer note:** the §164(a)(3) deduction is sometimes mistakenly claimed alongside Form 1116. §275(a)(4) prohibits this — either credit OR deduct. If both appear, fix it.

## 4. The five §904 baskets (separate-limitation categories)

- **Separate limitation computed per basket** — §904(d) requires the FTC limitation to be computed separately for each basket. Income, deductions, foreign tax, and the resulting credit limitation are tracked basket-by-basket. Excess credit in one basket cannot offset US tax on income in another basket.  _(§904(d))_

**The Form 1116 separate categories**  _([Form 1116 instructions; §904(d)](https://www.irs.gov/instructions/i1116))_

| # | Form 1116 category | Checkbox | Typical income | Notes |
| --- | --- | --- | --- | --- |
| 1 | Section 951A category income | Box a | A CFC shareholder's §951A inclusion; individuals generally need a §962 election to claim deemed-paid taxes through Form 1118. | Separate category; unused credits generally cannot be carried back or forward for this category. |
| 2 | Foreign branch category income | Box b | Business profits attributable to a qualified business unit (QBU) in a foreign country. | Separate from general category income under §904(d)(2)(J). |
| 3 | Passive category income | Box c | Interest, dividends, rents, royalties, annuities, passive asset gains, and similar investment income. | High-taxed passive income is moved out of passive under Reg. §1.904-4(c). For the no-Form-1116 election, high-taxed income is still treated as passive. |
| 4 | General category income | Box d | Wages, self-employment net income, active business income, and other income not assigned to another category. | General category includes high-taxed income that would otherwise be passive. |
| 5 | Section 901(j) income | Box e | Income from activities in sanctioned countries. | Use a separate Form 1116 for each sanctioned country. Taxes paid to sanctioned countries are not creditable; Pub. 514 lists Iran, Libya, North Korea, Sudan, and Syria for 2025, with Libya subject to the Presidential waiver note. |
| 6 | Certain income re-sourced by treaty | Box f | U.S.-source income treated as foreign-source under an income tax treaty resourcing rule. | Use when treaty resourcing is needed to claim the additional credit for U.S. citizens/residents in certain treaty countries. |
| 7 | Lump-sum distributions | Box g | Foreign tax on a lump-sum distribution where the special Form 1116 category applies. | Do not confuse this with §901(j) income; it has its own checkbox. |

- **Treaty re-sourcing sixth pseudo-category** — A sixth pseudo-category is treaty re-sourcing income (§865(h) / §904(d)(6)) — income that a treaty re-sources to the foreign country to permit a credit. Each re-sourcing treaty is its own separate basket. Rare for individual returns; flag and refer out if it appears.  _(§865(h); §904(d)(6))_
- **One Form 1116 per basket** — One Form 1116 per basket. A taxpayer with both passive (1099-DIV foreign tax) and general (foreign salary) income files two Form 1116s.  _(§904(d))_

### 4.1 Lookthrough and re-characterization

- **High-tax kick-out (Reg. §1.904-4(c))** — Passive income does not include high-taxed income. High-taxed income is income for which the foreign taxes paid on the income, after expense allocation, exceed the highest U.S. tax that can be imposed on that income. It is reported using an HTKO column and reclassified to the applicable non-passive category.  _([Reg. §1.904-4(c); Form 1116 instructions](https://www.irs.gov/instructions/i1116))_
- **§904(d)(3) lookthrough for CFCs** — Dividends, interest, rents, royalties from a CFC are characterized by reference to the underlying earnings — flagged for individuals only where they have a §962 election or are otherwise treated as a corporate shareholder; refer out.  _(§904(d)(3))_
- **§861 source rules for wages** — §861 source rules determine whether income is foreign-source or US-source. A common error: a US employee paid by a US employer for work performed in Germany has foreign-source wages (place-of-performance rule, §861(a)(3)). Conversely, a US contractor who travels to a client in France for two weeks but otherwise works from a US office sources only the work-days-abroad portion as foreign.  _(§861(a)(3))_

## 5. The §904(a) limitation formula

- **Maximum FTC (basket) formula** — Maximum FTC (basket) = US tax before FTC × (Foreign taxable income (basket) / Total taxable income)  _(§904(a))_
- **US tax before FTC** — Form 1040 line 16 + Schedule 2 line 2 (AMT, if applicable, separately for AMT FTC) − certain credits taken before the FTC.  _(§904(a))_
- **Foreign taxable income (basket)** — Gross foreign-source income in that basket less deductions definitely related to that income less a ratable share of deductions not definitely related (the apportionment in Form 1116 Part I).  _(§904(a))_
- **Total taxable income** — Form 1040 line 15, with adjustments for capital gain rate differentials (the "qualified dividends and capital gain rate adjustment" — Form 1116 line 18 worksheet) and the standard deduction.  _(§904(a); Form 1116 line 18 worksheet)_
- **Adjusted foreign-source income (capital gain rate adjustment)** — If the taxpayer has qualified dividends or long-term capital gains taxed at preferential rates, the foreign-source income in the limitation numerator must be scaled down by the ratio of the preferential rate to the ordinary rate so the limitation does not over-credit. Form 1116 line 18 worksheet handles this. The adjustment is mandatory unless the de minimis rule applies (foreign-source qualified dividends + LTCG ≤ $20,000 and the taxpayer is in the 32% bracket or below — see Form 1116 instructions for the 2025 figures and re-verify).  _(Form 1116 line 18 worksheet)_
- **Allocation and apportionment of deductions** — Form 1116 Part I requires the taxpayer to assign deductions to foreign-source income: - Definitely related deductions (e.g., expenses of producing the foreign income — see Schedule C lines apportioned to foreign work) — assigned 100%. - Standard deduction — apportioned ratably between US-source and foreign-source income on Form 1116 line 3a. - Itemized deductions not definitely related (state tax, charitable, medical) — also ratably apportioned. - Interest expense — apportioned by the asset method under Reg. §1.861-9T for sophisticated cases; for individuals usually de minimis. - R&E expense — refer out (rarely material for sole props).  _(Form 1116 Part I; Reg. §1.861-9T)_
- **Limitation is lesser of foreign tax paid or formula** — The limitation is the lesser of (a) foreign tax paid in basket OR (b) the formula above. Excess foreign tax → carryback/carryforward (§6).  _(§904(a))_

## 6. Carryback and carryforward (§904(c))

- **1 year back, 10 years forward** — Excess foreign tax (foreign tax paid > limitation) in a basket carries 1 year back (file a Form 1040-X for the prior year), then 10 years forward in the same basket.  _(§904(c))_
- **GILTI basket no carry** — GILTI basket (§951A): no carryback and no carryforward. Use-it-or-lose-it. This is one of the most punitive features of the GILTI regime and a primary reason individual taxpayers consider the §962 election (which makes them taxable as a domestic corporation on the GILTI inclusion and unlocks the §960 deemed-paid credit but introduces a double-tax problem on distribution).  _(§951A)_
- **Tracking carries via Schedule B** — Maintain a basket-by-basket schedule showing, for each year of origination, the foreign tax paid, the limitation, the excess, the amount used in each subsequent year, and the remaining balance. Form 1116 Schedule B (separate one-page schedule introduced for the 2021 form year) is the IRS form for this; required from 2021 forward whenever carryover exists. Always attach Schedule B if there is any prior carryover or any current excess.  _(Form 1116 Schedule B)_
- **Ordering rule for use of carries** — Current-year credit first, then carryback from a future year (rare in practice), then carryforward from oldest to newest within the basket.  _(§904(c))_

## 7. The $300 / $600 de minimis no-Form-1116 election (§904(j))

- **Total creditable foreign tax cap** — $300 (single, HoH, MFS, QSS) or $600 (MFJ) USD  _([§904(j); Form 1116 instructions](https://www.irs.gov/instructions/i1116))_
- **Four conditions for de minimis election** — A simplified election that lets an individual claim the credit on Schedule 3 line 1 without filing Form 1116. All conditions must be met: (1) total creditable foreign taxes are not more than $300, or $600 if married filing jointly; (2) all foreign-source gross income is passive category income for this purpose, including high-taxed income and export financing interest; (3) all income and foreign taxes are reported on qualified payee statements such as Form 1099-DIV, Form 1099-INT, Schedule K-1, Schedule K-3, or similar substitute statements; and (4) the filer is an individual, not an estate or trust.  _([§904(j); Form 1116 instructions](https://www.irs.gov/instructions/i1116))_
- **Effect of election** — When the election applies, you skip Form 1116 entirely. Put the foreign tax on Schedule 3 line 1 and check the box. No carryforward results when this election is used — but in practice no carryforward should exist because by definition the credit is small and absorbed.  _([§904(j); Form 1116 instructions](https://www.irs.gov/instructions/i1116))_

**Reviewer trap:** if the taxpayer has $250 of mutual-fund foreign tax AND $50 of foreign tax withheld on a paid foreign consulting gig (general category), the election is unavailable because not all foreign tax is from passive payee-statement income. File Form 1116 (one for passive, one for general).

## 8. High-tax kick-out for passive income

- **High-taxed passive income threshold** — Foreign tax after expense allocation exceeds the highest U.S. tax that can be imposed on the income  _([Reg. §1.904-4(c); Form 1116 instructions](https://www.irs.gov/instructions/i1116))_
- **Kick-out mechanics** — If passive income is high-taxed income under Reg. §1.904-4(c), report the item in an HTKO column. On the passive-category Form 1116, include the income in the country column and enter it as a negative amount in the HTKO column. On the other category Form 1116, enter the high-taxed income as a positive amount in the HTKO column.  _([Reg. §1.904-4(c); Form 1116 instructions](https://www.irs.gov/instructions/i1116))_

The General basket typically has more limitation headroom because it includes the taxpayer's foreign wages (which generate a large numerator) but the foreign tax on those wages may already exceed the wage-only limitation. Kicking high-taxed passive items into General can absorb existing General-basket excess.

- **Automatic classification, not a separate election** — The high-taxed passive income rule is a classification rule, not a separate election. Form 1116 instructions direct taxpayers with passive high-taxed income to use HTKO columns on the passive Form 1116 and on the other category Form 1116.  _([Reg. §1.904-4(c); Form 1116 instructions](https://www.irs.gov/instructions/i1116))_
- **Mechanical test for effective rate** — Compare foreign tax paid on the income after expense allocation with the highest U.S. tax that can be imposed on that income. The test is not a flat percentage shortcut; qualified dividends, capital gains, and ordinary income can have different highest U.S. rates.  _([Reg. §1.904-4(c); Form 1116 instructions](https://www.irs.gov/instructions/i1116))_

## 9. GILTI basket (§951A) and §960 deemed-paid credit — at a glance for individuals

- **Without §962 election** — The GILTI inclusion is taxed at the individual's ordinary rates (no §250 deduction; no 50% GILTI deduction available). No §960 deemed-paid credit is available — the credit flows only to corporate US shareholders. The individual sees the full GILTI inclusion at ordinary rates with no FTC offset for the foreign corporate-level tax. This is the worst-case outcome.  _(§951A)_
- **With §962 election** — The individual is taxed on the GILTI inclusion as if a domestic corporation. The §250 deduction is 50% for 2025 GILTI and 40% for post-2025 NCTI under OBBBA; the §960 deemed-paid credit is limited to 80% of foreign tax for 2018–2025 GILTI and 90% after 2025 under OBBBA NCTI rules. On distribution from the CFC, the previously-taxed earnings are subject to a second layer of individual tax, but only to the extent the distribution exceeds the §962 PTI (a complicated mechanic).  _(§962; Reg. §1.962-1)_

This is sophisticated territory. Defer to a corporate/international skill or to a credentialed international practitioner. This skill flags GILTI exposure and computes the individual-level Form 1116 GILTI basket only at the most basic level.

## 10. The 2022 attribution-and-nexus regulations: T.D. 9959 / T.D. 9982 and the Notice relief

### 10.1 What changed

- **Four-prong test for creditable foreign income tax** — T.D. 9959 (published Jan 4 2022) and clarifying amendments in T.D. 9982 (published July 27 2022 / further refined in 2024) rewrote the definition of a creditable "foreign income tax" in Reg. §1.901-2. The new four-prong test requires: 1. Realization — tax imposed on a realization event recognizable under US concepts. 2. Gross receipts — tax computed on gross receipts (or a close proxy). 3. Cost recovery — the foreign tax base permits recovery of significant costs (depreciation, interest, COGS, wages). 4. Attribution — the foreign country has a sufficient nexus to the income; for non-residents this means an activities-based or source-based nexus consistent with US sourcing concepts. The attribution prong was the most disruptive: a foreign tax imposed on a US person purely because a customer or service recipient is located in the foreign country, with no source-based nexus to activities, fails attribution and is non-creditable.  _(Reg. §1.901-2; T.D. 9959; T.D. 9982)_

**Casualties of the new regulations (without relief):**
- **Brazil's withholding tax on royalties paid to foreign licensors** — historically creditable; now arguably non-creditable because Brazil's source rule (payor-based) does not match US sourcing.
- **Digital services taxes (DSTs)** in France, UK, Italy, Spain, Austria, India equalization levy — fail attribution and/or the gross-receipts prong.
- **Some withholding taxes** on services to non-residents where the foreign country uses a customer-location source rule.

### 10.2 The Notice relief

- **Notice 2023-55 relief** — Notice 2023-55 (July 21 2023): for tax years beginning on or after Dec 28 2021 and ending on or before Dec 31 2023, taxpayers may disregard the attribution and cost-recovery prongs and use the pre-2022 standards (former Reg. §1.901-2 as in effect Dec 27 2021) — i.e., go back to the old, taxpayer-friendly definition.  _(Notice 2023-55)_
- **Notice 2023-80 extension** — Notice 2023-80 modified the Notice 2023-55 temporary relief rules, addressed partnerships and partners, coordinated Pillar 2 issues, and extended the relief period until further notice.  _([Notice 2023-80; Pub. 514](https://www.irs.gov/publications/p514))_
- **Current relief status** — Pub. 514 describes the Notice 2023-55 relief, as modified by Notice 2023-80, as extended until further notice. Do not require newer IRS guidance as a filing prerequisite unless the IRS later changes this relief posture.  _([Notice 2023-80; Pub. 514](https://www.irs.gov/publications/p514))_

**Current relief posture:** Pub. 514 describes the Notice 2023-55 relief, as modified by Notice 2023-80, as extended until further notice. Document reliance on the Notice relief in the workpaper for Brazilian, Indian, DST-type, and similar taxes.

### 10.3 Treaty override

- **Treaty override of the new regs** — §894 and §7852(d) preserve treaty benefits. If a US income tax treaty with the foreign country grants creditability (most US treaties have an Article 23 / Article 24 relief-from-double-taxation article), the treaty position can override the new regulatory denial. Document the treaty article and attach a Form 8833 disclosure where the treaty position is contrary to the Code or regulations.  _(§894; §7852(d))_

### 10.4 Reviewer checklist for 2022+ foreign taxes

- **Checklist for foreign taxes > $5,000** — For every foreign tax > $5,000 (rule of thumb): 1. Identify the foreign tax statute and rate. 2. Is it imposed on a realization event? (Most income taxes — yes; DSTs — sometimes no.) 3. Is it on gross receipts or net income? (Withholding on gross is OK if a permissible proxy.) 4. Is cost recovery permitted in the foreign tax base? (Withholding on gross receipts — typically yes by IRS concession; DSTs — often no.) 5. Is there source-based attribution? (Salary for work performed in the foreign country — yes; royalty paid from foreign-country customer to US licensor for use of US-developed IP — depends.) 6. Is the Notice 2023-55 / 2024-44 / 2025 extension still in effect for this tax year? FLAG if uncertain. 7. If still non-creditable, is there a treaty article that grants the credit? File Form 8833.  _(Reg. §1.901-2)_

## 11. Form 1116 walkthrough

One Form 1116 per basket. Follow these parts.

### Part I — Foreign income and deductions (per basket)

**Part I table**  _(Form 1116 Part I)_

| Line | Item | Note |
| --- | --- | --- |
| (above Part I) | Check box a-h for category | One box per Form 1116. Must check exactly one. |
| (i) Name of foreign country | List each foreign country separately in columns A, B, C | Up to three per form; use additional Forms 1116 if more |
| 1a | Gross foreign-source income in this category | Wages, dividends, interest, etc., sourced to the foreign country |
| 1b | If compensation for personal services >$250,000, attach worksheet | Sourcing rule check |
| 2 | Expenses definitely related to 1a | Direct expenses of earning the foreign income |
| 3a | Pro-rata standard or itemized deductions | Allocable to foreign-source income |
| 3b | Other deductions |  |
| 3c-3g | Apportionment ratios | Foreign gross income ÷ total gross income |
| 4a-4b | Home mortgage interest apportionment | Reg. §1.861-9T asset method |
| 5 | Losses from foreign sources |  |
| 6 | Taxable income from sources outside US (per basket) | Line 1a − line 2 − line 3a-g − line 4 − line 5 |
| 7 | Adjustments | Qualified dividend and capital gain rate adjustment (line 18 worksheet) |

### Part II — Foreign taxes paid or accrued

**Part II table**  _(Form 1116 Part II)_

| Line | Item | Note |
| --- | --- | --- |
| (j) Country | One row per country | Same countries as Part I |
| (l) Date paid/accrued | Cash basis: date paid. Accrual basis: date the foreign tax accrued (year-end usually). |  |
| (n)(o)(p) In foreign currency | Amount in foreign currency by category (taxes withheld at source on dividends, on interest, on royalties; other foreign tax paid) | Optional detail |
| (q)(r)(s)(t) In US dollars | Convert at the **average exchange rate** for the year (Rev. Rul. 74-310 + IRS yearly tables). For accrual basis: end-of-year rate for accrued; payment-date rate for actual remittance. Differences are §988 currency gain/loss. |  |
| 8 | Total foreign taxes paid/accrued in USD |  |

- **Cash basis vs. accrual basis (§905(a))** — Default: cash basis (claim in year paid). An accrual-basis election is irrevocable once made. Most individuals stay on cash. Accrual is useful where the foreign country's tax year mismatches the US calendar year (e.g., UK April-to-April) and the taxpayer wants to match credit with US income.  _(§905(a))_

### Part III — Limitation calculation

**Part III table**  _(Form 1116 Part III)_

| Line | Item |
| --- | --- |
| 9 | Total foreign tax (Part II line 8) plus carrybacks/carryforwards (from Schedule B) |
| 10 | Carrybacks/carryforwards used this year |
| 11 | Total available foreign tax |
| 12 | Reduction for International Boycott Operations (§999) — rare |
| 13 | Foreign tax available for credit |
| 14 | Combined foreign-source taxable income (from Part I line 7 across countries) |
| 15-17 | Adjustments |
| 18 | Adjusted total taxable income from Form 1040 (with capital gain rate adjustment) — **use the worksheet in the instructions** |
| 19 | Divide line 14 by line 18 |
| 20 | US tax before FTC (Form 1040 line 16 + Schedule 2 line 2 net of certain credits) |
| 21 | Maximum credit = line 19 × line 20 |
| 22 | Foreign tax credit for this basket = **lesser of line 13 or line 21** |

### Part IV — Cumulative summary

**Part IV table**  _(Form 1116 Part IV)_

| Line | Item |
| --- | --- |
| 23-32 | Sum of line 22 across all Form 1116s by basket |
| 33 | Total FTC — flows to Schedule 3 line 1 |

- **Excess flows to Schedule B** — Excess (line 13 − line 22, basket-by-basket) flows to Schedule B for carryback/carryforward tracking.  _(Form 1116 Schedule B)_

## 12. AMT FTC — Form 1116 (AMT version)

- **AMT Form 1116 mechanics** — For taxpayers with AMT exposure (Form 6251), a separate Form 1116 is computed on the AMT base: - AMT taxable income replaces regular taxable income in the limitation denominator (line 18). - Foreign-source AMT income may differ from foreign-source regular income because preferences and adjustments (notably the §911 exclusion adjustment, depreciation differences, ISO exercises) flow through. - Foreign tax in the AMT computation is the same dollar amount as for regular tax (§59(a)(1)). - §59(a)(2) repealed the 90% AMT FTC limit for tax years beginning after Dec 31 2004 — the AMT FTC can fully eliminate AMT. - Excess AMT FTC carries on a separate AMT track with its own 1-back / 10-forward.  _(§59(a)(1); §59(a)(2))_
- **Marking the AMT form** — Mark the AMT Form 1116 clearly ("AMT" written on top per instructions). Attach to Form 6251.  _(Form 6251)_

**Reviewer note:** the AMT computation is often skipped by less-experienced preparers when AMT applies. If Form 6251 shows AMT > 0 and the taxpayer has any FTC, the AMT FTC must be computed.

## 13. §901(j) sanctioned-country list (verify currency)

- **§901(j) denial** — §901(j) denies the FTC for income from, and taxes paid to, countries the US has designated as supporting international terrorism, with which the US has severed diplomatic relations, or which the US does not recognize.  _(§901(j))_
- **Designated countries for 2025** — Pub. 514 lists Iran, Libya, North Korea, Sudan, and Syria as countries whose 2025 income taxes do not qualify for the credit under §901(j). The same Pub. 514 section notes a Presidential waiver for Libya for qualified income taxes arising after December 9, 2004 and shows Cuba as a prior sanction period that ended December 21, 2015.  _([§901(j); Pub. 514](https://www.irs.gov/publications/p514))_
- **Reporting sanctioned-country income** — Income from each sanctioned country is reported on a separate Form 1116 checked as Section 901(j) income (Box e for the 2025 form). The credit for taxes paid to the sanctioned country is denied, but Pub. 514 notes that tax paid to a non-sanctioned residence country on income derived from a sanctioned country may still be creditable if the other requirements are met.  _([§901(j); Form 1116 instructions; Pub. 514](https://www.irs.gov/instructions/i1116))_

A taxpayer with sanctioned-country income should also consider OFAC compliance — usually a referral matter beyond tax.

## 14. FEIE (§911) vs. FTC — the strategic choice for US expats

A US citizen or resident alien living abroad faces a binary decision: claim the §911 foreign earned income exclusion (FEIE — up to $130,000 per qualifying individual for 2025) and foreign housing exclusion/deduction, or forgo §911 and rely on the FTC, or combine both (excluding up to the §911 cap and crediting the foreign tax on the remainder).

### 14.1 Why you can't double-dip

- **§911(d)(6) denies FTC on excluded income** — §911(d)(6) and Reg. §1.911-6(c) deny the FTC for foreign tax on excluded income. If the taxpayer excludes $130,000 of German wages under §911 and Germany taxes them at 35%, the German tax on that excluded $130,000 is not creditable. Only foreign tax on the residual (income above the §911 cap) is creditable.  _(§911(d)(6); Reg. §1.911-6(c))_

### 14.2 The high-tax-country case (Germany, UK, France, Australia, Japan, Netherlands)

- **FTC preferred in high-tax countries** — In a high-tax country, the foreign effective rate on wages typically exceeds the US rate on the same income. The FTC fully eliminates US tax on the foreign wages and generates excess credit (carryforward 10 years). §911, by contrast, excludes only up to $130,000, and the §911 exclusion stacks under the §911(f) anti-stacking rule (the remaining income is taxed at the rate that would apply as if §911 had not been claimed) — reducing its value. **Default for high-tax country residents: skip §911, use FTC, claim foreign housing as a deduction (rare, only with self-employment) or just rely on FTC.** This typically yields lower US tax, generates carryforward, and avoids the §911 "tax-rate stacking" trap.  _(§911(f))_

### 14.3 The low-tax / no-tax country case (UAE, Bermuda, Cayman, Bahamas, Saudi Arabia, Qatar, Monaco)

- **§911 preferred in no-tax countries** — In a no-income-tax country, there is no foreign tax to credit. The taxpayer's only way to reduce US tax on the foreign wages is the §911 exclusion. Default for low-tax country residents: use §911.  _(§911)_

### 14.4 The mid-tax country case (Italy, Spain, Portugal NHR, Ireland)

- **Breakeven analysis** — Run both computations. The breakeven is roughly where the foreign effective rate equals the taxpayer's US effective rate on the same income. Below breakeven → §911 + housing exclusion. Above breakeven → FTC. At the margin → §911 up to the cap and FTC on the excess.  _(§911; §901)_

### 14.5 The §911 revocation trap (§911(e))

- **5-year lock-out after revocation** — A §911 election, once revoked, cannot be re-elected for 5 tax years without IRS consent (PLR procedure, user fee). This makes the choice consequential. A taxpayer who claims §911 in year 1, moves to a higher-tax country in year 2, and revokes is locked out of §911 for years 3-7. Conservative default: for a taxpayer who anticipates fluctuating between low- and high-tax countries, lean toward FTC from the start (no §911 revocation lock-in problem) unless the §911 savings in the current year are large and the situation is stable.  _(§911(e))_

### 14.6 Reviewer checklist — FEIE vs FTC

- **Checklist steps** — 1. Determine residency: bona fide resident under §911(d)(1)(A) or physical presence under §911(d)(1)(B) (330 days in 12 months). 2. Compute the foreign effective tax rate on the foreign wages. 3. Compute US tax under three scenarios: (a) §911 alone, (b) FTC alone, (c) §911 + FTC on residual. 4. Project forward 3-5 years if the taxpayer's situation is stable; consider carryforward value of excess FTC. 5. Document the choice. If §911 is claimed and later revoked, ensure the 5-year lock-out is understood.  _(§911(d)(1)(A); §911(d)(1)(B))_

## 15. State conformity

- **Most states do not allow an FTC** — Most states do NOT allow an FTC for state income tax purposes. The state generally treats the foreign income tax as a non-deductible item (or, in a few states, as an itemized deduction at the state level, but not a credit). California (R&TC §17131 et seq.) does not conform to §901 and provides no state FTC. The same is true for most other states with an income tax.  _(Cal. R&TC §17131 et seq.)_

A US expat in Germany who is fully relieved at the federal level by the FTC may still owe California or New York state tax on the foreign wages if state residency persists. Resolving state residency (severing domicile, establishing a new domicile) is the primary state-tax planning move for expats — not the FTC.

State-specific conformity is handled by the state-tax skills (e.g., `ca-540-individual-return` for California, where the foreign tax is generally a non-event and the foreign income remains in California taxable income for residents).

## 16. Worked examples

### Example A — High-tax German salary using the FTC

**Facts.** Taxpayer is a US citizen, single, age 35, working in Berlin for a German employer. 2025 facts:
- Foreign wages (Germany): €120,000 ≈ $130,000 at the 2025 average rate.
- German income tax + solidarity surcharge withheld: €42,000 ≈ $45,500 (effective rate ~35%).
- No US-source income.
- Takes the standard deduction ($15,750 for single).
- Eligible for §911 (physical presence: 340 days outside US).

**Decision: skip §911, use FTC.**

Reason: German effective rate (35%) > US marginal rate on $130k of taxable income (~22-24% net of standard deduction). §911 excludes only $130,000 (the entire wage, so US tax would be zero under §911 alone — but no carryforward generated). FTC: US tax ≈ $20,000 on $115k taxable, eliminated by ~$45,500 of foreign tax → ~$25,000 of excess credit carryforward.

**Form 1116 (General basket, box d):**
- Part I line 1a: $130,000
- Part I line 3a: standard deduction apportionment: $15,750 × ($130,000 / $130,000) = $15,750
- Part I line 7: $115,000 (foreign-source taxable income, general basket)
- Part II line 8: $45,500 (foreign tax paid)
- Part III line 18: $115,000 (total taxable income — entirely foreign)
- Part III line 19: $115,000 / $115,000 = 1.0000
- Part III line 20: US tax before FTC ≈ $20,000 (2025 single brackets on $115k)
- Part III line 21: Maximum FTC = 1.0000 × $20,000 = $20,000
- Part III line 22: lesser of $45,500 or $20,000 = $20,000 credit
- Excess: $45,500 − $20,000 = $25,500 carryforward in the General basket
- Form 1040 line 16: $20,000; Schedule 3 line 1: $20,000; net federal tax = $0

**Schedule B (Form 1116):** open General basket with $25,500 carryforward to 2026.

**Sanity check.** Carryforward is unlikely to be used unless the taxpayer returns to a lower-tax foreign country or has US-source income with no foreign tax. Document as suspended; consider planning moves (US-side business income that could be re-sourced under treaty re-sourcing, holding the carryforward across the 10-year window).

### Example B — Dubai resident using §911 (no FTC because no foreign tax)

**Facts.** US citizen, single, age 32, working in Dubai for a Dubai employer. 2025 facts:
- Foreign wages (UAE): $200,000.
- UAE income tax: $0 (no personal income tax).
- Eligible for §911 (bona fide resident — full calendar year in UAE).
- Modest US-source dividend income: $4,000 with $200 of qualified foreign tax (passive — from US mutual fund holding foreign stocks).

**Decision: §911 on the wages; de minimis no-Form-1116 election on the $200 of mutual-fund foreign tax.**

Reason: no UAE tax to credit on the wages → §911 is the only way to reduce US tax on the $200k. The $200 of passive foreign tax is below $300 and all from a 1099-DIV → de minimis election applies; no Form 1116 needed.

**Form 2555 (Foreign Earned Income Exclusion):**
- Line 45 exclusion: $130,000 (2025 cap)
- Foreign housing exclusion (employer-provided housing in Dubai, $31,500 rent): qualified housing expenses limited to ~30% of $130k = $39,000 minus a base of 16% of $130k = $20,800 → exclusion of up to ~$18,200, but Dubai is on the IRS high-cost city list so the cap may be higher — verify Form 2555 instructions and the high-cost city table.
- Total exclusion: ~$148,000.
- Taxable wages: $200,000 − $148,000 = $52,000.

**§911(f) stacking:** the $52,000 of residual wages is taxed at the rate as if the §911 exclusion had not been claimed — i.e., at the rate that applies to the full $200,000. For 2025 single brackets, this stacks the $52,000 into the 24-32% bands rather than the 12-22% bands.

**Schedule 3 line 1:** $200 of foreign tax (de minimis election, no Form 1116). Check the box.

**Sanity check.** US tax on the residual $52,000 (stacked) ≈ $11,000 — $200 = ~$10,800 final. Materially lower than US tax with no §911 (~$40,000). §911 is the right call.

### Example C — Multi-country freelancer splitting baskets

**Facts.** US citizen freelance software developer, single, age 40, US-domiciled but spent 2025 in multiple countries. Schedule C net SE income: $180,000 allocated as:
- Work performed in Germany (4 months, on-site at a German client): $60,000 — German tax withheld $18,000 (30%).
- Work performed in Brazil (2 months on-site): $31,500 — Brazil withheld $7,500 (25%, "imposto de renda na fonte" on services).
- Work performed remotely from US for various clients: $90,000.
- Passive dividend income from a US brokerage with $850 of foreign tax (1099-DIV box 7) on foreign mutual fund holdings.

**Sourcing.**
- $60,000 Germany — foreign-source general basket (place-of-performance §861(a)(3)).
- $31,500 Brazil — foreign-source general basket.
- $90,000 US work — US-source.
- $850 foreign tax on $4,200 of dividends — passive basket.

**Brazilian tax creditability check (§10).** Brazil's withholding on services is on gross. Realization, gross receipts, cost recovery: arguably fails the new regs' attribution prong if Brazil sources by payor location. Under Notice 2023-55 relief as modified and extended by Notice 2023-80, the pre-2022 standards apply and the Brazilian withholding remains creditable. Document reliance on the Notice relief in the workpaper.

**Form 1116 — General basket (one form with two columns, Germany and Brazil):**
- Part I line 1a column A (Germany): $60,000; column B (Brazil): $31,500; total $90,000
- Part I line 2: Schedule C expenses definitely related to the foreign work — assume $9,000 (the foreign-work share of total $27,000 of Schedule C expenses, allocated by gross income ratio: $90k/$180k × $27k = $13,500; refine if any expense is definitely US or definitely foreign). Use $13,500.
- Part I line 3a: standard deduction apportioned: $15,750 × ($90,000 / $180,000) = $7,500
- Part I line 6: $90,000 − $13,500 − $7,500 = $69,000 foreign-source taxable income
- Part II line 8: $18,000 (Germany) + $7,500 (Brazil) = $25,500 foreign tax paid
- Part III line 18: total taxable income from Form 1040 line 15: $180,000 − $13,500 SE-deduction half − $13,500 Schedule C expenses already in line 1a − adjust for the half-SE tax deduction (~$12,700) and QBI deduction (~$33,000 if non-SSTB, see `us-qbi-deduction`) and standard deduction ($15,750) → call it $105,000 for illustration (worked out by `us-schedule-c-and-se-computation` + `us-qbi-deduction`).
- Part III line 19: $69,000 / $105,000 = 0.6571
- Part III line 20: US tax before FTC on $105,000 single ≈ $17,500
- Part III line 21: max FTC = 0.6571 × $17,500 = $11,500
- Part III line 22: lesser of $25,500 or $11,500 = $11,500 General-basket credit
- Excess: $25,500 − $11,500 = $14,000 General-basket carryforward

**Form 1116 — Passive basket:**
- $850 foreign tax, $4,200 foreign dividend income.
- De minimis election unavailable because the taxpayer also has general-basket foreign tax. (The $300 cap is total across all baskets.)
- Compute the passive-basket Form 1116 in full. With $4,200 of foreign-source qualified dividends (Part I line 1a after qualified-dividend rate adjustment — multiplied by the rate ratio 15%/37% = 0.4054 for QD-rate adjustment if not in de minimis, → ~$1,703 adjusted), the limitation is small (probably absorbs all $850). Confirm with the worksheet.

**Schedule 3 line 1:** ~$12,350 total FTC (General $11,500 + Passive $850).

**Sanity check.** Brazil and Germany combined effective tax (28.3% on $90k of foreign wages) exceeded the US average rate, generating a $14,000 carryforward. With future foreign work the carryforward will absorb. Document on Schedule B.

## 17. Practitioner cautions

- **Full cautions list** — 1. Always file Schedule B (Form 1116) if any carryforward exists or originates. A missing Schedule B can cause the IRS to deny the carryforward in a later year on audit. 2. One Form 1116 per basket; do not combine. Combining baskets is a common error and produces incorrect limitations. 3. Convert foreign tax at the average exchange rate for cash-basis taxpayers; document the rate source (IRS yearly rate table, OANDA, ECB, BoE). 4. Reconcile foreign tax to the foreign tax return. If the taxpayer is going to amend the foreign return (refund claim), §905(c) requires a US 1040-X. Flag. 5. §911 + FTC interaction: if §911 is elected, reduce the foreign-source income on Form 1116 by the excluded amount, and reduce foreign tax proportionately. 6. §901(m) covered asset acquisitions, §901(k)(l) holding period, §901(j) sanctioned — flag and refer out for any non-trivial exposure. 7. Brazilian, Indian, and DST taxes post-2022: rely on Notice relief and document the reliance; FLAG 2025 relief status if uncertain. 8. Treaty positions (§894 override of T.D. 9959): attach Form 8833 if claiming a credit based on treaty article contrary to the regs. 9. AMT FTC: separate Form 1116 required when Form 6251 shows AMT. 10. State conformity: warn the client that the FTC does not reduce state tax in most states; state residency planning is a separate exercise.  _(§905(c); §894; §901(m); §901(k); §901(l); §901(j))_

## 18. Self-checks (before sign-off)

- [ ] One Form 1116 per basket; box at top correctly marked.
- [ ] Foreign-source income sourced under §861-§865; place-of-performance for wages; payor-location only where treaty/source rule supports.
- [ ] Standard or itemized deductions apportioned on line 3a per the worksheet.
- [ ] Qualified dividend / LTCG rate adjustment applied on line 18 (unless de minimis exception applies).
- [ ] Foreign tax at average exchange rate; source documented.
- [ ] High-tax kick-out evaluated for any passive items above the highest applicable U.S. tax rate.
- [ ] §901(j) sanctioned countries — credit denied if applicable.
- [ ] Schedule B prepared if any carryforward originates or is used.
- [ ] AMT Form 1116 prepared if Form 6251 shows AMT.
- [ ] FEIE-vs-FTC choice documented; §911 lock-out (5 years post-revocation) explained if §911 revoked.
- [ ] Notice 2023-55/2024-44/2025-XX reliance documented if relying on pre-2022 attribution rules for Brazilian, Indian, or DST-type taxes. FLAG if 2025 relief status not confirmed.
- [ ] Treaty position (Form 8833) attached if relying on treaty over the new regs.
- [ ] Schedule 3 line 1 ties to sum of Form 1116 line 33 across baskets.
- [ ] State conformity warning issued to client.

## 19. Refusal catalogue (this skill)

- **R-FTC-1** — Corporate FTC and §960 deemed-paid credit for C corp shareholders of CFCs. (This skill: individuals only. Refer to a corporate-international skill.)  _(R-FTC-1)_
- **R-FTC-2** — §962 election preparation and computation for individual GILTI taxpayers beyond basic flagging. (Refer to credentialed international practitioner.)  _(R-FTC-2)_
- **R-FTC-3** — Treaty re-sourcing under §865(h) / §904(d)(6). (Flag and refer out.)  _(R-FTC-3)_
- **R-FTC-4** — §901(m) covered asset acquisitions. (Refer out.)  _(R-FTC-4)_
- **R-FTC-5** — Form 5471, 8865, 8858, 8621 preparation. (This skill consumes their inputs only.)  _(R-FTC-5)_
- **R-FTC-6** — §905(c) foreign tax redetermination requiring 1040-X. (Refer out.)  _(R-FTC-6)_
- **R-FTC-7** — State-specific FTC conformity beyond a general "most states don't allow" warning. (State-tax skills handle their jurisdictions.)  _(R-FTC-7)_
- **R-FTC-8** — Non-resident alien FTC computations on Form 1040-NR. (This skill: US persons only.)  _(R-FTC-8)_

## 20. Provenance

- **Statutory citations** — IRC §901 (allowance of the credit; "compulsory amount" rule); IRC §902 (repealed 2018; historical reference for pre-TCJA deemed-paid credit); IRC §903 (taxes in lieu of income tax); IRC §904 (limitation: §904(a) formula, §904(c) carryback/carryforward, §904(d) baskets, High-tax kick-out, §904(j) de minimis election); IRC §905 (cash/accrual basis; redeterminations); IRC §911 (FEIE — interaction); IRC §951A (GILTI inclusion); IRC §960 (deemed-paid credit, corporate); IRC §962 (individual election to be taxed as corporation on subpart F / GILTI); IRC §164(a)(3) (foreign tax deduction alternative); IRC §275(a)(4) (no double benefit); IRC §861-§865 (source rules); IRC §894 (treaty override); IRC §59(a) (AMT FTC)  _(IRC §901; §902; §903; §904; §905; §911; §951A; §960; §962; §164(a)(3); §275(a)(4); §861-§865; §894; §59(a))_
- **Regulations** — Reg. §1.901-2 (definition of "foreign income tax" — as rewritten by T.D. 9959 and T.D. 9982); Reg. §1.904-4 (separate categories; high-tax kick-out); Reg. §1.904-6 (allocation and apportionment of foreign tax); Reg. §1.904-2 (carryback and carryforward); Reg. §1.911-6 (no FTC for excluded income); Reg. §1.861-9T (interest expense allocation); Reg. §1.962-1 (§962 election)  _(Reg. §1.901-2; §1.904-4; §1.904-6; §1.904-2; §1.911-6; §1.861-9T; §1.962-1)_
- **Treasury Decisions and Notices** — T.D. 9959 (Jan 4 2022) — new attribution/nexus/cost-recovery requirements; T.D. 9982 (July 27 2022) — clarifying amendments; Notice 2023-55 (July 21 2023) — temporary relief for 2022 and 2023; Notice 2023-80 (Dec 11 2023) — extended relief and Pillar 2 coordination; Notice 2023-80 — modified the Notice 2023-55 rules and extended the relief period until further notice  _(T.D. 9959; T.D. 9982; Notice 2023-55; Notice 2023-80)_
- **Forms and instructions** — Form 1116, Foreign Tax Credit (Individual, Estate, or Trust) — 2025 version; Form 1116 Schedule B, Foreign Tax Carryover Reconciliation Schedule (2021+); Form 1116 instructions (2025); Form 6251, Alternative Minimum Tax — Individuals; Form 2555, Foreign Earned Income; Form 8833, Treaty-Based Return Position Disclosure; Schedule 3 (Form 1040) line 1; Schedule A (Form 1040) line 6 (foreign tax deduction alternative)  _(Form 1116; Form 1116 Schedule B; Form 6251; Form 2555; Form 8833; Schedule 3; Schedule A)_
- **§911(b)(2)(D) exclusion cap 2025** — $130,000 for 2025 (inflation-adjusted) USD  _(§911(b)(2)(D))_
- **§904(j) de minimis amounts** — $300 single / $600 MFJ USD  _([§904(j); Form 1116 instructions](https://www.irs.gov/instructions/i1116))_
- **High-taxed passive income threshold** — Foreign tax after expense allocation exceeds the highest U.S. tax that can be imposed on the income  _([Reg. §1.904-4(c); Form 1116 instructions](https://www.irs.gov/instructions/i1116))_
- **§951A GILTI carry and deemed-paid credit rate** — §951A GILTI: no carry; 80% deemed-paid (corporate)  _(§951A)_
- **§250 deduction rate** — 50% for 2025 → 37.5% post-2025 (verify) percent  _(§250)_

`us-tax-workflow-base` v0.2+ (load alongside); `us-sole-prop-bookkeeping` (Schedule C inputs for general basket); `us-schedule-c-and-se-computation` (taxable income inputs); `us-qbi-deduction` (taxable income denominator); `us-federal-return-assembly` (orchestration); `ca-540-individual-return` and other state skills (state conformity); `us-quarterly-estimated-tax` (estimated tax accounting for projected FTC)

Drafted: 2025-11-15
Tax year covered: 2025
Reviewer status: pending credentialed reviewer (Circular 230 — EA, CPA, or attorney) sign-off before any output is delivered to a taxpayer or filed with the IRS.
Open verification items: Form 1116 line 18 qualified-dividend/LTCG rate adjustment de minimis thresholds and any post-publication IRS Form 1116 developments.

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
