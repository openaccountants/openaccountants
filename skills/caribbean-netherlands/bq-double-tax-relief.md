---
name: bq-double-tax-relief
description: >
  Analyse 2026 double-tax relief for Bonaire, Sint Eustatius and Saba.
  Use for the European Netherlands arrangement, residence, permanent establishments,
  employment, dividends, pensions and unilateral income-tax relief. Separates taxing
  rights from domestic liability, exemption from credit, and tax from social
  insurance. Includes primary decrees, current authority guidance, conditional
  calculations, evidence controls and carry-forward decisions. This source-cited
  draft holds other bilateral instruments, actual relief forms, complex residence,
  foreign-law eligibility, rounding and operational cases. Load with the universal
  workflow base and applicable BES income, corporate and payroll companions;
  professional review remains required before reliance.
jurisdiction: BQ
category: international
tax_year: 2026
tax_year_notes: "2026 reference using BRN current from 2025 and unilateral decree current from 2011; verify each source country and relevant period"
tier: 2
last_updated: 2026-10-17
version: 0.2
review_status: pending_review
depends_on:
  - workflow-base
  - cross-border-workflow-base
---

# Bonaire, Sint Eustatius and Saba: double-tax relief in 2026

Establish residence, income classification, source, period and the applicable
instrument before selecting a rate or relief. The Belastingwet BES distinguishes
European Netherlands from BES; general residence/establishment is assessed from
the circumstances. USD means United States dollar. Belastingwet BES articles
8.120 and 8.121 provide separate delegated bases for other-state and Netherlands
relief. A geographical connection alone does not establish a tax or exemption.
[B1, articles 1.1–1.5 and 8.120–8.121][B1]

Load `workflow-base`, `cross-border-workflow-base` and every applicable BES
tax/domain companion, including
`bq-income-tax`, `bq-corporate-tax`, `bq-payroll`, `bq-social-contributions` and
`bq-tax-compliance`. Preserve source gates, confirmed profile, refusals, the
four universal outputs and all applicable domain outputs/checks. This Tier 2
reference establishes selected relief components. Unknown mandatory conditions
hold the complete financial output package; it does not complete every
cross-border slot or certify a country pack.

## Choose the instrument and the tax

| Instrument | Scope and control |
|---|---|
| Belastingregeling voor het land Nederland (BRN) | Persons resident in European Netherlands or BES; the taxes listed in article 1.3. It allocates taxing rights between these two areas. |
| Besluit voorkoming dubbele belasting BES (unilateral decree) | BES income tax, wage tax and the specified gambling tax, only to the extent prevention is not otherwise provided, article 1. |
| Another bilateral or Kingdom instrument | Establish its own territorial reach, taxes, residence, dates and relief procedure. Neither decree proves that every other instrument is absent. |
| Social insurance | Separate applicable social-security legislation/agreements. The authority expressly says BRN and the unilateral decree do not supply national/employee insurance-premium rules. |

[BRN, articles 1.1–1.3][BRN]; [UNI, article 1][UNI]; [G-FOREIGN]

The authority's resident page describes worldwide income and unilateral relief.
Its account of arrangements before 2011 is historical, not an exhaustive 2026
treaty roster. Its Netherlands-income page links to an older 2019 BRN version;
the current registry selects **1 January 2025**, which is the text used here.
The unilateral decree's current registry selects **5 March 2011**. An old
commencement date does not by itself make a provision obsolete. [G-RESIDENT];
[G-FOREIGN]; [BRN]; [UNI]

The BRN list includes European income, wage, corporate and dividend taxes, and
BES income, wage, property, distribution and specified natural-resource
profit-sharing taxes. It does not establish relief for ABB, customs, every
local charge, social premiums or minimum tax merely because a payment crosses
between the areas. Tax-specific and foreign rules still need their own sources.
[BRN, article 1.3][BRN]

## BRN residence and permanent establishments

Article 1.4 uses domestic residence/deeming provisions. A dual-resident
individual's order is permanent home, then closest personal/economic relations
where homes exist in both, then habitual abode where the stated uncertainty or
no-home condition exists. Do not substitute a nationality tie-breaker that this
text does not contain. A dual-resident entity normally uses actual management;
paragraphs 6–7 have third-country and deemed-Netherlands exceptions. Unresolved
facts remain held. [BRN]

In particular, an entity within article 1.4(2)(d) is treated as Netherlands
resident for distribution tax, Netherlands corporate tax and Netherlands
dividend tax, while paragraph 7 treats it as BES resident for the other listed
taxes. A BES incorporation address or one residence certificate does not decide
every tax. Apply `bq-corporate-tax` and the actual article 5.2 status/decision.
[BRN, article 1.4][BRN]

BRN article 1.5 defines a fixed business establishment, with examples and
exceptions. Construction/installation must exceed twelve months for paragraph
3; paragraph 4 has a separate **at least 30 days in any twelve months** offshore
resource rule, specified exclusions and related-enterprise aggregation in
paragraph 5. Paragraphs 6–9 address preparatory/auxiliary activities, contract
agents, independent agents and control of another entity. Do not apply the
construction threshold to every activity or treat group ownership alone as a
permanent establishment. Actual contracts, functions, assets, risks and day
aggregation require evidence. [BRN]

## BRN income classification and taxing rights

The phrases 'may be taxed' and 'only taxable' allocate rights under the
arrangement; they do not create a domestic tax charge or set a universal rate.
Retain the domestic base and relief analysis separately. [BRN]

| Income | BRN branch to establish |
|---|---|
| Real-property income | Article 2.1 generally permits the property's area to tax; it defines property and resource rights, and has a specific deemed-Netherlands-entity exception. |
| Business profits | Article 2.2 normally uses the enterprise's area unless a permanent establishment exists in the other area; attributable profit uses independent-enterprise functions/assets/risks. Separately classified income retains its own article. |
| International shipping/air transport | Article 2.3 uses the enterprise's area, including the specified pool/joint-operation branch; distinguish transport wholly within one area. |
| Dividends | Article 2.4 generally permits residence and source taxation, with specific Netherlands-source exemptions and PE/exit-assessment exceptions below. |
| Capital gains | Article 2.5 separately addresses property, PE assets, international transport and other assets; emigration/outstanding-assessment and basis safeguards matter. No universal tax-free-gain conclusion follows. |
| Employment | Article 2.6 normally permits the work area to tax; its cumulative short-stay exception and special-category overrides matter. |
| Directors/commissioners | Article 2.7 permits taxation in the entity's area; do not apply the ordinary employment exception automatically. |
| Entertainers/sportspersons | Article 2.8 permits the performance area to tax, including income allocated to another person. |
| Pensions, annuities and social-security benefits | Article 2.9 normally uses recipient residence, subject to government-service and specified early lump-sum exceptions. Social-security benefit income is different from insurance premiums. |
| Government service | Article 2.10 distinguishes central government, BES civil servants and subdivisions, with work/residence and government-business exceptions. |
| Students/trainees | Article 2.11 protects qualifying maintenance/study/training amounts from outside the host area; it is not a blanket exemption for local work. |
| Other income | Article 2.12 uses residence, with its PE-connected-right/asset exception. Classify under earlier articles first. |

[BRN, articles 2.1–2.12][BRN]

### Ordinary employment and the 183-day exception

Subject to articles 2.7, 2.9, 2.10 and 2.11, BRN article 2.6(2) leaves ordinary
employment remuneration taxable only in the residence area when **all** apply:

1. Presence in the other area totals no more than 183 days in a twelve-month
   period beginning or ending in the relevant tax year.
2. The employer paying, or on whose behalf remuneration is paid, is not resident
   in that other area.
3. The remuneration is not borne by the employer's PE in that other area.

An annual workday total alone does not test the rolling presence period or
employer/PE conditions. Keep the presence calendar, work allocation and payer/
cost-bearing evidence distinct. International-transport crew has paragraph 3's
separate rule. [BRN]

These fictional classifications stipulate an ordinary BES-resident employee,
work in European Netherlands, no special-category override and a fully tested
relevant twelve-month presence period. They establish no amount of domestic
tax or allocation between work locations. [BRN]

| Presence and employer facts | Article 2.6 component |
|---|---|
| 180 days; BES employer; no Netherlands PE bearing remuneration | All three conditions met: only BES may tax under this employment branch. |
| 184 days; otherwise the same facts | Presence condition fails: Netherlands may tax remuneration attributable to the work there, subject to the remaining analysis. |
| 90 days; Netherlands-resident employer | Employer condition fails despite the short stay: Netherlands may tax the relevant work remuneration. |

### Dividends and pensions

BRN article 2.4(3) exempts qualifying Netherlands-source dividends for a
BES-resident pension fund that is the beneficial owner. Paragraph 4's separate
Netherlands-source exemption requires a qualifying share-capital entity,
BES residence, beneficial ownership and a direct holding of **at least 10%**
in the distributing entity. That is a participation threshold, not a 10%
withholding rate. Paragraph 5 requires the prescribed refund/exemption
conditions; eligibility is not authority to omit withholding without that
procedure. Actual forms, decisions and domestic/anti-abuse conditions remain
held until established. [BRN]

Paragraph 8 routes its specified PE-connected dividends to article 2.2.
Paragraph 9 has a ten-year post-emigration branch while the specified exit
assessment remains outstanding. Retain basis, emigration and assessment
history. Neither the BRN nor a holding percentage establishes that the
underlying company's profits escape corporate taxation. [BRN]

The authority confirms Netherlands AOW benefits for a BES resident are included
in BES worldwide income and allocated to BES under BRN. This is not a rule
for every pension or an instruction to ignore wrongly withheld Netherlands
tax. Article 2.9 and government-service article 2.10 must be applied to the
actual payment; early lump sums and tax-facilitated origin require their full
conditions. An objection to Netherlands withholding has its Netherlands route,
not automatically `bq-tax-compliance`'s BES objection clock. [G-FOREIGN]; [BRN]

## BRN relief is directional

Article 3.1 permits residence-area inclusion, then supplies the relevant
exemption or capped credit. Its lists differ by direction. For a BES resident,
paragraph 7 includes the specified Netherlands-taxable directors' income in
its exemption list, while paragraph 8 covers the listed dividends, entertainers/
sportspersons and early pension/annuity lump sums by credit. For a Netherlands
resident, directors' income is in paragraph 3's credit list. Do not copy one
direction's table into the other. [BRN]

Paragraphs 4–5 also alter relief for specified PE/deemed-Netherlands-entity
cases. The credit is limited by the relevant residence-area relief calculation,
not an unlimited refund of foreign tax. This guide does not complete European
Netherlands tax computation, corporate participation exemption or an actual
BRN relief claim. [BRN, article 3.1][BRN]

## Unilateral exemption and credit

Use the unilateral decree only after article 1's priority test. Its PE/agent
definitions in article 2 are its own; do not import every BRN definition.
Article 5 excludes the specified emigration income/tax from its income-tax
chapter. [UNI]

Articles 6–7 cover qualifying foreign business/PE profits and specified private
employment, public employment and public-law periodic benefits, subject to the
foreign income-tax condition. Foreign business attribution uses independent-
enterprise treatment. For private employment performed abroad for **less than
30 consecutive days**, article 7(3) requires proof that foreign tax was paid
to meet its stated subject-to-tax test. This is separate from BRN's 183-day
exception. The source of every receipt and the relevant foreign assessment/
payment must be established; a foreign bank deposit is not sufficient. [UNI]

Article 8 calculates exemption relief **separately per foreign jurisdiction**:
established BES calculated tax multiplied by qualifying foreign income divided
by the statutory denominator income. Paragraph 4 refers to article 24A's
calculated tax; paragraph 5 adjusts the denominator for the specified losses
from other years. Total relief, including other applicable relief, cannot
exceed the stated BES tax. Do not substitute gross world receipts or cash
withholding for these established amounts. Zero/negative denominators and
loss interactions remain held here. [UNI]

Article 11 instead credits eligible foreign income tax on dividends, interest
and royalties included in income and outside article 7 income. It uses the
lesser of eligible foreign tax and the proportional BES limit, with its
overall limit. Foreign tax counted on dividends is capped at **5% of the
dividend** under paragraph 3. This is a relief ceiling, not authority for a
foreign payer to withhold 5%. Dividend/interest amounts are reduced by related
costs for the proportional limit; royalties by directly attributable costs.
Article 12 requires beneficial ownership and has transaction-series rules.
[UNI, articles 11–12][UNI]

### Fictional positive-income relief components

Each example stipulates residence, priority, qualifying foreign source and
tax treatment, beneficial ownership where needed, no other relief or carry
balances, and established BES tax/denominator. Amounts are USD. They do not
recompute the domestic tariff, approve a foreign assessment, establish actual
eligibility or select fractional-cent rounding. [UNI]

| Component | Stipulated inputs and arithmetic |
|---|---|
| Single-jurisdiction exemption | BES tax 12,000; denominator 60,000; qualifying foreign income 15,000. Relief 12,000 × 15,000 / 60,000 = 3,000; remaining BES tax 9,000. |
| Separate second jurisdiction | Same tax/denominator; foreign incomes 15,000 and 10,000. Separate relief 3,000 and 2,000; total 5,000; remaining tax 7,000. |
| Overall exemption ceiling | Tax 12,000; denominator 60,000; qualifying foreign income 75,000. Proportional amount 15,000, limited to 12,000; no negative remaining BES tax or invented refund. Any carry requires its own rule/decision. |
| Dividend credit ceiling | Tax 12,000; denominator 60,000; gross dividend 10,000; related costs 1,000; foreign tax 1,500. Proportional limit 12,000 × 9,000 / 60,000 = 1,800; eligible foreign tax capped at 500; credit 500; remaining BES tax 11,500. |
| Interest credit ceiling | Same tax/denominator; gross interest 8,000; related costs 500; foreign tax 2,000. Proportional limit 12,000 × 7,500 / 60,000 = 1,500; credit 1,500; remaining BES tax 10,500. The dividend-specific 5% cap is not applied. |

### Carry balances and distinct tax branches

Articles 9–10 distinguish excess exemptible foreign income from negative
foreign income. Articles 14–15 prescribe per-jurisdiction decisions, revision
and the negative-income exception; a missing decision does not always erase
the specified negative-income effect. Articles 13 and 16 govern the stated
uncredited-tax carry and decision. Do not label every difference between
foreign tax and current credit as an eligible carry. In particular, tax beyond
article 11(3)'s 5% dividend ceiling is not established as carryable merely by
the amount being withheld. Keep income, loss and tax-credit ledgers separate.
[UNI]

Article 17 provides its specified return-to-residence rule within eight years
after the end of the emigration year for prior established balances; it is
not a universal eight-year expiry for all relief. Article 18 has a separate
qualifying foreign-wage exemption. Article 19 has a foreign-prize gambling-tax
exemption where its similar-tax condition is met. Neither rule follows merely
from the recipient having a foreign address. Actual wage/prize treatment,
delegated rules, carry/revision periods and form mapping remain held until
their complete sources and facts are established. [UNI]

## Evidence, reconciliation and completion holds

Keep a jurisdiction-by-jurisdiction schedule of instrument/version, residence,
income character, work/presence dates, payer, PE and cost bearing, gross income,
costs, foreign taxable base, assessed/paid/refunded tax, domestic tax, denominator,
relief limit and separately established carry decisions. Reconcile the foreign
and BES assessments, source certificates and receipts. Later foreign refunds
or reassessments need review; do not preserve a credit for an amount no longer
supported or count the same tax as both exemption and credit.

The reviewer retains actual identities, tax numbers, bank details and private
returns outside the agent. Use stable case references, sanitised established
amounts and confirmation that evidence matches. Do not collect or submit ID
documents, tax numbers or bank details. No filing/payment is authorised here.

Unknown source, instrument priority, residence, period, foreign-law condition,
classification, PE, denominator, method or relief decision remains Needs Input
or a hold. Follow each applicable refusal and its canonical message. Test both
directions and every cumulative condition; 'may tax' is not a final liability.
Preserve all applicable universal/domain outputs and obtain professional review.

This reference does not establish the complete 2026 bilateral/Kingdom treaty
roster, other countries' rates and anti-abuse rules, full transfer-pricing/
reporting duties, information exchange, import/indirect tax, inheritance,
operational relief forms, rounding or a complete country pack. No actual
taxpayer, authority submission, portal or engagement workbook was tested.

## Primary sources and read scope

Read on 17 October 2026. All operative articles of the current BRN and
unilateral decree were read in context, with their current registry dates.
Selected Belastingwet BES introductory and relief-delegation articles and
both current authority pages were read. Older authority links and historical
descriptions were not used as proof of the current text or an exhaustive
treaty list. The cited decrees' delegated implementing conditions, every
foreign statute, original gazette chain, court interpretation and actual
form mapping were not completed. A captured text alone is not eligibility.

[B1]: https://wetten.overheid.nl/BWBR0029244/2026-04-11
[BRN]: https://wetten.overheid.nl/BWBR0029675/2025-01-01
[UNI]: https://wetten.overheid.nl/BWBR0029674/2011-03-05
[G-FOREIGN]: https://www.belastingdienst-cn.nl/onderwerpen/belastingzaken-particulieren/inkomstenbelasting/inkomen-van-buiten-caribisch-nederland
[G-RESIDENT]: https://www.belastingdienst-cn.nl/onderwerpen/belastingzaken-particulieren/inkomstenbelasting/binnenlands-belastingplichtigen

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained in the
[ryanduguid/openaccountants fork](https://github.com/ryanduguid/openaccountants).
Check its quality tier, recorded review status and cited sources before use.
Choose a practitioner whose credentials and engagement scope you have verified.
The links below are optional upstream services; they do not publish or verify
this fork's changes.

- Upstream connection service: https://www.openaccountants.com/connect
- Upstream accountant network: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
