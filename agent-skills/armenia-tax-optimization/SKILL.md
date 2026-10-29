---
name: armenia-tax-optimization
description: "Use for 2026 Armenian business-regime comparisons and lawful tax planning for a company or individual entrepreneur. Separates ordinary company profit tax, turnover-tax eligibility and activity rates, entrepreneur profit tax and micro-business conditions. Test the legal form, activity classification, exclusions, turnover and election dates before comparing amounts. Trigger on Armenia tax regime, microenterprise, turnover tax, individual entrepreneur, LLC comparison or business tax planning. Includes preserved calculation and threshold controls with explicit eligibility assumptions. Read alongside the detailed personal, corporate, VAT and payroll Guides. Includes ordinary aggregation, entry and exit dates, documented cost-reduction carries, asset transitions and published filing forms. Checked against the law; independent source review is recorded in the country research; named professional attestation remains pending."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/armenia-tax-optimization"
  jurisdiction: "AM"
  tax_year: "2026"
  last_updated: "2026-10-27"
  trust_label: "Built by Michael Cutajar and the OpenAccountants team"
  review_status: "pending_review"
---

# Armenia business tax planning v0.4

## Do the eligibility test before the arithmetic

Do not choose a regime from a headline rate. First classify each actual activity using the Armenian economic-activity classification, identify every legal and natural person involved, total the relevant turnover and related-party amounts, and test each exclusion. Check registration date and the required tax-authority statement. This Guide gives a screening method, not a conclusion that a particular taxpayer qualifies. [Tax Code, Articles 30, 254 and 267](https://www.arlis.am/hy/acts/215611/latest)

| Route | Basic starting point | Tax result that must be modelled |
| --- | --- | --- |
| Resident commercial organisation, ordinary system | Generally available when no special status applies | Generally 18% profit tax on the statutory tax base; VAT is separately tested. A later dividend payment can create a separate personal withholding obligation. [Tax Code, Articles 103, 125, 150](https://www.arlis.am/hy/acts/215611/latest) |
| Registered individual entrepreneur, ordinary system | Separate business and personal income; establish the general-system period | 23% profit tax on the positive statutory business base. Personal income is excluded from that business object. Use the [entrepreneur base and annual/advance method](armenia-income-tax.md). [Tax Code, Articles 103–105, 125(3.1), 134–136](https://www.arlis.am/hy/acts/215611/latest) |
| Resident commercial organisation, turnover tax | Prior-year sales must not exceed AMD 115 million, and the business and all activity tests must pass | Turnover tax replaces profit tax and/or VAT for a qualifying resident commercial organisation. Rates and cost reductions depend on activity. [Tax Code, Articles 253–258](https://www.arlis.am/hy/acts/215611/latest) |
| Individual entrepreneur, turnover-tax regime | Eligibility and activity tests still apply | Turnover tax replaces VAT, but the entrepreneur's profit-tax treatment is separate; the Code prescribes AMD 5,000 per month for the specified turnover-regime entrepreneur case. Do not model this as a single company tax. [Tax Code, Articles 125(3), 253](https://www.arlis.am/hy/acts/215611/latest) |
| Micro-business | Prior-year sales must not exceed AMD 24 million, and the person and activity must qualify | The micro-business exemption has stated exceptions, including import tax, certain withholding duties, excise, environmental and road taxes. It is not a blanket exemption from every tax or contribution. [Tax Code, Articles 267, 269–270](https://www.arlis.am/hy/acts/215611/latest) |

For an existing taxpayer the turnover and micro thresholds use “did not exceed,” so equality at AMD 115 million or AMD 24 million is within the numeric test. This does not override exclusions or other eligibility conditions. New registrants have separate 20-day statement deadlines; an existing taxpayer generally makes the annual statement by 20 February. Confirm the exact route and effective date before starting activity. [Tax Code, Articles 254, 267](https://www.arlis.am/hy/acts/215611/latest)

## The exclusions are different

The turnover-tax exclusions include specified financial, insurance, crypto-asset and notarial activity, along with activities classified in groups 69 (legal and accounting), 70 (head offices and management consultancy), 78.2 (temporary employment agency activity) and 78.3 (other human-resource provision). Test the legal classification of the service; do not assume that every technology, engineering, marketing or advisory service is excluded from turnover tax merely because it sounds professional. Other exclusions, aggregation and linked-activity rules still apply. [Tax Code, Articles 254(3)–(3.1), 30](https://www.arlis.am/hy/acts/215611/latest)

The micro-business exclusions are broader and separately listed. They include specified professional and advisory activity such as legal, accounting, audit, consulting, engineering, advertising, marketing, translation and expert services, as well as other listed activity classes. Some listed hospitality activities have specific exceptions. The Code's actual class and exception control the result, not the label used in an invoice or website. Review the complete current Article 267(5) and Annex 3 against the taxpayer's actual activity before treating income as micro-business income. [Tax Code, Articles 267(3)–(5), Annex 3](https://www.arlis.am/hy/acts/215611/latest)

The turnover-tax rates are activity-specific. Under the current Code, the starting rates include 10% for ordinary trade, 5% for listed secondary raw-material trade, 7% for production, 10% for rent, interest and royalties, 12% for catering, 1.5% for newspaper editorial sales, 10% for other assets including immovable property, and 10% for other activity. The 1% high-technology rate is confined to activity types on the Government's list and is provided for through 31 December 2031. A catering taxpayer that files the required election applies the separate catering schedule. These are not interchangeable rates. [Tax Code, Articles 258(1), (8)](https://www.arlis.am/hy/acts/215611/latest)

## Enter and leave a regime on the statutory date

For resident commercial organisations and registered entrepreneurs, first total **all activities** in the preceding tax year, including the other special regime: micro turnover enters the AMD 115 million turnover-tax test, and turnover-tax turnover enters the AMD 24 million micro test. Equality passes only the numeric test. For a division or spin-off, each resulting entity uses the predecessor's entire prior-year turnover, not an allocated fraction; for a merger or absorption, add the relevant predecessors' turnover. This prevents a new registration from restarting the limit. [Tax Code, Articles 254(2), 267(3)][regimecode]

Apply the two related-person rules separately. Article 30(1) covers the stated **20% or greater** resident-company ownership links, including a common non-entrepreneur individual owning that share in multiple resident companies. The corresponding special-regime exclusion applies even below the turnover limit unless the linked persons have filed suspension declarations and actually stopped activity from the relevant declared date. Article 30(2) instead requires an SRC-head decision recognising coordinated action in common economic interests; for that branch, test the recognised group's aggregate prior- or current-year turnover against AMD 115 million or AMD 24 million. An ordinary invoice between unrelated businesses is not itself such a decision. Joint-activity, goods-commission and goods-agency contracts in the agent's own name are separate exclusions. [Articles 30, 254(3)(5)–(7), 267(5)(6)–(8)][regimecode]

| Entry route | Required statement and start date |
|---|---|
| Continuing eligible company or entrepreneur | File the chosen special-regime declaration by **20 February inclusive** for status from 1 January. A small turnover without that declaration is insufficient. |
| New company/entrepreneur | File by the **20th day after registration inclusive** for status from registration. Reorganisation has the specific predecessor-turnover rules above. |
| Suspended through 20 February, then resumes | File by the **20th day after resumption inclusive** for status from resumption. |
| Entrepreneur deregisters and registers again | Use the specific prior-year/current-year re-registration branches. A current-year re-registration does not erase earlier VAT status; for micro it also does not erase earlier turnover-tax status. |
| Micro business chooses turnover tax | The declared start cannot precede filing by more than 20 days. If micro status ends before that chosen start, submit a **new** declaration within 20 days after the actual exit to obtain turnover status from exit. The earlier future-dated declaration is disregarded for that event. |
| Micro status ends compulsorily | If turnover-tax eligibility is satisfied, elect turnover tax from exit by the 20th day after exit inclusive. Otherwise the company/entrepreneur enters ordinary VAT status from exit, with the Article 59 declaration. |

These are the distinct routes in Articles 254(1), 267(1) and 59(1)(1)–(3), not a general permission to backdate any return. [regimecode]

An ordinary turnover taxpayer exits when current-year all-activity sales **exceed AMD 115 million**, or on the occurrence of the listed prohibited activity, statutory ownership link or prohibited contract. File the exit/VAT declaration identifying the ground and date within 20 days after the event. The threshold-crossing VAT rule applies to the **excess**, not to earlier turnover simply because the threshold was crossed. Voluntary VAT entry uses its declared date, no earlier than 20 days before filing. [Articles 59(1)(4)–(5), 255(1)–(2)][regimecode]

Micro status ends when relevant current-year turnover **exceeds AMD 24 million**, on the listed exclusions, or on voluntary VAT/turnover entry. Switching between entrepreneur and non-entrepreneur micro status does not bypass a compulsory exit. For the SRC-decision aggregation branch, Articles 255(1)(5)/268(1)(5) specify exit from the beginning of the event's tax year, or later registration; an appeal preserves special status pending the stated court outcome. Keep this retrospective branch separate from an ordinary threshold crossing. The historical constitutional annotation to Article 255 limits application to relationships predating the law; it is not a current universal exemption from the statutory branch. [Articles 255, 268][regimecode]

## Run the complete micro activity screen

Article 267(5)'s exclusions cover financial/insurance/investment/payment/crypto providers and the other expressly named regulated businesses; notaries; gambling/lotteries; saunas/baths/steam baths; audit organisations; and **commercial buying-and-selling by companies or entrepreneurs**. The professional-services exclusion includes consultancy, law, accounting, engineering, advertising, design, marketing, translation, expert/examination work, medical care and services, dental technology, hair/body care, vehicle repair, intermediary services, software development, data processing/transmission, R&D/experimental work, construction works, architectural/construction-design documentation, and property valuation/measurement, plus similar listed work. Head-office/management consultancy (70), temporary labour (78.2), other labour supply (78.3), and inter-/intra-regional bus-route operation/passenger services have separate exclusions. [Article 267(5)(1)–(2.2)][regimecode]

Yerevan catering is excluded, with the express exception for meals directly connected to Annex 3 tourist-house hotel services. Activities in State Duty Law 19.7/19.8 are excluded **for those activities**. A current agreement to receive rent, interest or royalties excludes a company/entrepreneur, except interest on the positive balance of its servicing-bank current account. The ownership, SRC-decision aggregation and prohibited-contract screens above still apply. Do not revive repealed retail-location or business-customer prohibitions from an older form. [Article 267(5)(4), (6)–(11)][regimecode]

A **non-entrepreneur individual** has a different route: exclusively Annex 3 activity, prior-year relevant turnover no more than AMD 24 million, a declaration **before starting or continuing** the chosen activity period, and an SRC licence issued within one working day after declaration. The individual cannot use other non-entrepreneur individuals' labour in that activity. Annex 3 permits the specified customer-ordered footwear/leather, clothing, hats, carpets, wood/furniture, non-precious jewellery, computer/household-appliance repair and software servicing, bicycle/wheelchair and other household repairs, pottery/ceramics and sheet-metal work; clock/timepiece/instrument repair; listed specialist/language/admission courses; dance/singing and performing/creative work; event-hosting; sports education; private-household own-consumption services; smithing; and tourist-house hotel services with directly connected meals. Preserve the exact activity conditions: software **servicing** in the annex is not the excluded software-**development** business. [Articles 267(2)–(5), Annex 3][regimecode]

Micro exempts the covered activity's state taxes, including profit-tax advances, but does **not** remove import taxes (including EAEU), withholding/PIT on taxable income paid/accrued to non-entrepreneur/non-notary individuals, excise, environmental or road taxes. Monthly PIT calculations remain due by the following month's 20th. The annual turnover report is due by the next year's **1 February inclusive**, except for entrepreneurs whose micro activity is exclusively Annex 3 activity. Article 270 separately retains the stated import, improperly invoiced VAT, excise and environmental/natural-resource returns. Social, stamp and health obligations need their own laws; “micro” is not an exemption from them. [Articles 269–270][regimecode]

## Map the actual declarations and returns

| Instrument | Fields and use |
|---|---|
| **191-N**, current turnover-status declaration | TIN, taxpayer, address, proposed start, confirmations of the prior-year threshold and each activity/relationship/contract exclusion, and signature/name. This is the ordinary declaration, not the catering exception election. [191-N][turnstatement] |
| **558-N Annex 1**, company/entrepreneur micro declaration | TIN/name/address/start; non-VAT/non-turnover status; prior-year AMD 24 million test; current exclusion confirmations; signature. Use the current incorporated form, including the separate labour-route, crypto and rent/interest/royalty confirmations. [558-N][microforms] |
| **558-N Annexes 2/3**, non-entrepreneur declaration/licence | Identity/passport, public-service number or absence certificate, TIN, residence, exact Annex 3 activities/places and start/end periods; licence records the approved person, activities, place and period. [558-N][microforms] |
| **558-N Annex 4**, annual turnover/stamp report | Identity/year; production 5, services 6, works 7, specified state-duty activities 9, other 10; total 11 = 5+6+7+9+10. Stamp base 12 follows 11 and stamp 13 is automatically completed for an entrepreneur exclusively in micro for that year. Activity-code shares are reported separately. Check the separate stamp-law method rather than inventing a micro-only exemption. [558-N][microforms] |
| **299-N**, quarterly turnover calculation | TIN/name/address and year/quarter; AMD without luma. For trade, table 5 records base, gross tax, eligible current costs, current reduction, opening reduction carry, total available reduction, tax floor, payable tax and closing carry. Tables 6/7/9 do the same for production/catering/other activity. Total income/tax is row 22; row 27 adds the separately identified non-turnover-tax categories. To correct a period, submit a new calculation with corrected data. [299-N, instructions 1–29, 30–41, 49–70][turnreturn] |

The old **table 8** outside-Yerevan catering computation is expressly for periods before 1 January 2026; do not carry its old 4% floor into 2026. The special catering election under Articles 254(6)–(8) uses **626-N**, not the ordinary 191-N declaration: the Code permits the stated threshold/relationship/contract exceptions, but not the prohibited regulated/professional activities in 254(3)(3)/(3.1), and voluntary VAT entry ends the route. A qualifying current-year event requires the catering election within 20 days. Under 258(8), the elected route applies **12% to catering and 20% to the specified other assets/activity**, with the catering cost-reduction method where applicable. [Articles 254, 258][regimecode]; [626-N][cateringstatement]; [299-N, instructions 30, 42–48][turnreturn]

The **1% high-technology** entry is income from the activities on **Government 142-N's annex**, not every receipt of a technology-labelled business. Match the actual activity to the annex's complete 32-code list and the 874-N classification; for example software development J62.01.0, other software publishing J58.29.0 and web portals J63.12.0 are listed. Keep unlisted receipts in their own statutory activity line. The 142-N list applies from 2025; the Code's 1% entry runs through 31 December 2031. This turnover-tax entry is distinct from separate state-aid or R&D deduction qualification. [258(1)(8)][regimecode]; [142-N, paragraphs 1–3/annex][hightechlist]

**Future enactments are not current restrictions.** Actual 1001-N starts its bank-shareholder form addition on 1 February 2027 and its real-estate-service addition on 1 June 2027. Neither starts merely because the order was published in September 2026. [1001-N, paragraphs 1–2][microfuture]

## Carry cost reductions and assets through an exit

For each qualifying activity, calculate gross tax **G = base × activity rate**, current expense reduction plus the **same activity's** opening unused tax reduction **R**, and its statutory floor **F = base × minimum rate**. Pay **max(G−R, F)** and carry **max(R−(G−F), 0)**. A period without that activity's base does not consume its carry. The carry is an amount of **tax reduction**, not an expense balance. Allocate unsegregated administrative/sales expense using that activity's base as a share of **all activities'** total turnover, not only the eligible streams. [Articles 258(2)–(7), 260(3)][regimecode]; [299-N, instructions 12–17, 24–29, 36–41, 55–60][turnreturn]

On turnover-to-ordinary exit, apply the ordinary method to bases arising after exit. Reconstruct fixed/intangible asset carrying values with the depreciation that would have accrued under Article 121 during the special period; ordinary depreciation deduction begins on the **first day of the following month**. Prorate the specified non-production/financial expenses for the exit month by days from exit through month-end divided by all days of that month. Other asset costs follow Article 264(3), with its express exclusion for assets in the turnover expense-reduction branches: do not deduct the same cost again. Unused turnover **tax reductions** become gross-income deductions in the exit reporting period at **10× trade, 20× production, 10× catering and 15× other activity**. [Article 264(1)–(4)][regimecode]

For micro-to-turnover or micro-to-ordinary exit, Article **272** applies the new system to the post-exit bases. A direct micro-to-ordinary asset roll-forward similarly counts Article 121 depreciation during micro, begins ordinary depreciation deduction the following month, prorates the specifically listed administrative/selling/non-production/financial exit-month costs, and recognises the other asset initial costs under the ordinary rules. The turnover-tax reduction multipliers are **not** a micro carry-forward. Cross-check the separate VAT stock/asset method in the [VAT Guide](armenia-vat.md); a profit-tax deduction is not itself an input-VAT credit. [Article 272][regimecode]

[regimecode]: https://www.arlis.am/hy/acts/215611/latest
[turnstatement]: https://www.arlis.am/hy/acts/209026/latest
[microforms]: https://www.arlis.am/hy/acts/200746/latest
[turnreturn]: https://www.arlis.am/hy/acts/201377/latest
[cateringstatement]: https://www.arlis.am/hy/acts/172557/latest
[hightechlist]: https://www.arlis.am/hy/acts/203094/latest
[microfuture]: https://www.arlis.am/hy/acts/231487/latest

## Activity-specific cost reductions

For the activities in Article 258(1)(1), (4), (6) and (10), documented eligible expenses reduce the calculated turnover tax, subject to separate rules and minimums:

- Ordinary trade: subtract 9.5% of eligible expenses; tax cannot fall below 1% of the trade tax base.
- Production: subtract 5% of eligible expenses; tax cannot fall below 3% of that activity's base.
- Catering: subtract 9% of eligible expenses; tax cannot fall below 3.5% of that activity's base.
- Other activity: subtract 6% of eligible expenses; tax cannot fall below 4.5% of that activity's base.

The expense categories are activity-specific and require statutory supporting documents. The Code excludes, among other items, fixed-asset and intangible-asset acquisition or creation costs, capital and current improvements, depreciation, liquidation, free inputs, business-trip costs and representation costs from this reduction. Unused eligible expense reductions can carry forward in the corresponding activity branch, subject to the same rules. Separate activity and expense records are required; if administrative or sales costs cannot be separately tracked for the specified branches, Article 260 requires allocation by the relevant turnover proportions. [Tax Code, Articles 258(2)–(7), 260](https://www.arlis.am/hy/acts/215611/latest)

## Computation checks

These examples show the statutory arithmetic only. They do not establish that a business is eligible, that its records support the expenses, or that the assumed activity classification is correct.

**Trade example.** Assume eligible trade base AMD 10,000,000 and documented eligible expenses AMD 9,000,000. Initial tax is AMD 1,000,000. The expense reduction is AMD 855,000 (9.5% × AMD 9,000,000), leaving AMD 145,000. The minimum is AMD 100,000 (1% × base), so calculated tax is AMD 145,000. If eligible expenses were AMD 9,800,000, the reduction could not bring the tax below AMD 100,000.

**Production example.** Assume production base AMD 5,000,000 and eligible expenses AMD 3,000,000. Initial tax is AMD 350,000. The 5% reduction is AMD 150,000, leaving AMD 200,000; the 3% minimum is AMD 150,000.

**Ordinary company example.** If a resident company's statutory profit-tax base is AMD 10,000,000 and no special rate or adjustment applies, 18% produces AMD 1,800,000 profit tax. This does not calculate VAT, advance payments, loss relief, extraction or any available special regime. [Tax Code, Articles 125(1)](https://www.arlis.am/hy/acts/215611/latest)

## Compare the whole outcome

For each eligible route, calculate the tax base from the Code, then include VAT, payroll and social contributions, withholding on payments or dividends, compliance costs, asset purchases, cash extraction, loss use and the tax year of entry or exit. A special regime can cost more if its turnover base is large relative to profit or its VAT treatment prevents recovery. The LLC's ordinary 18% corporate rate and 5% dividend withholding are separate layers; a combined effective rate depends on the dividend amount, shareholder status and any applicable relief. See [individual income tax](armenia-income-tax.md), [corporate tax](am-corporate-income-tax.md), [VAT](armenia-vat.md) and [payroll](armenia-payroll.md).

## Executable screening controls

| Control | Input | Expected result |
| --- | --- | --- |
| Trade turnover reduction | Base 10,000,000; eligible expense 9,000,000 | Initial 10% tax 1,000,000; reduction 855,000; result 145,000; minimum 100,000 does not bind |
| Trade floor | Base 10,000,000; eligible expense 9,800,000 | Tax after reduction is below 100,000; cap the reduction at 900,000 and retain tax of 100,000 |
| Production reduction | Base 5,000,000; eligible expense 3,000,000 | Initial 7% tax 350,000; reduction 150,000; result 200,000; 150,000 minimum does not bind |
| Ordinary company tax | Statutory base 10,000,000; ordinary rate applies | 18% gives 1,800,000 before any other tax or payment |
| Threshold boundary | Prior-year eligible sales 115,000,000 for turnover-tax threshold | Numeric “did not exceed” test passes; still run every exclusion and aggregation rule |
| Threshold boundary | Prior-year eligible sales 24,000,000 for micro-business threshold | Numeric “did not exceed” test passes; still run every person, activity and exception rule |

## Filing and status limits

The entrepreneur's fixed AMD 5,000 monthly profit tax is separate from turnover tax and any applicable social payment. Properly declared suspension excludes only full months; it is not daily proration or a zero-revenue election. Article 136(4) makes that profit-tax payment due by 20 April of the following year. Under current 749-N Annex 1 instruction 1, an entrepreneur in turnover tax for the whole year files only section 1 field 107 in the profit-tax calculation; midyear transitions require the general computation for the relevant period. The ordinary-system 23% rate comes from Article 125(3.1), which the printed form's field-88 rate instruction does not expressly include; the [personal/business Guide](armenia-income-tax.md) records that implementation discrepancy. [Tax Code, Articles 125(3)/(3.1), 134–136](https://www.arlis.am/hy/acts/215611/latest); [749-N Annex 1 instructions 1, 7, 19, 36](https://www.arlis.am/hy/acts/226558/latest)

Turnover-tax returns and payment are quarterly and due by the 20th day of the following month. Micro-business companies and entrepreneurs file the preceding year's turnover report by 1 February, except entrepreneurs exclusively carrying on Annex 3 micro activity; separate monthly withholding and exception returns remain. Use the actual forms and entry/exit method above. [Tax Code, Articles 261–262, 270](https://www.arlis.am/hy/acts/215611/latest)

**Scope limits:** specialist investment/sector incentives, tax disputes and penalties, and taxpayer-specific treaty interaction require their own instruments and facts. Ordinary regime entry, activity exclusions, aggregation, computation, published declarations and asset/cost transitions are supplied above. Independent source review is recorded in the country research; Armenian professional attestation remains pending. The English translation is supporting text only; the current Armenian Code controls where its language or subsequent changes differ. No accountant has attested to this Guide.

## Sources

| Official source and retained original read scope | URL | Read on |
|---|---|---|
| Current Armenian Tax Code, Articles 103, 125, 253–270 | https://www.arlis.am/hy/acts/215611/latest | 2026-10-24 |
| Official English Tax Code translation; checked against current Armenian provisions | https://www.arlis.am/en/acts/231892 | 2026-10-24 |
| HO-76-N annual personal declaration transition | https://www.arlis.am/hy/acts/206337 | 2026-10-24 |
| Targeted current entrepreneur business object, rate, advances and payment rules, Articles 103–105, 125, 134–136 | https://www.arlis.am/hy/acts/215611/latest | 2026-10-25 |
| 749-N current Annex 1, targeted entrepreneur and settlement instructions | https://www.arlis.am/hy/acts/226558/latest | 2026-10-25 |
| Native Code, complete Articles 30, 254–270, 272 and Annex 3; targeted 59(1) | https://www.arlis.am/hy/acts/215611/latest | 2026-10-26 |
| Current 191-N ordinary turnover declaration | https://www.arlis.am/hy/acts/209026/latest | 2026-10-26 |
| Current 558-N Annexes 1–4, micro declarations/licence/annual turnover and stamp report | https://www.arlis.am/hy/acts/200746/latest | 2026-10-26 |
| Current 299-N form and instructions 1–70, quarterly turnover calculation | https://www.arlis.am/hy/acts/201377/latest | 2026-10-26 |
| 626-N separate catering election | https://www.arlis.am/hy/acts/172557/latest | 2026-10-26 |
| Government 142-N, full 32-code high-technology activity annex | https://www.arlis.am/hy/acts/203094/latest | 2026-10-26 |
| 1001-N, future 2027 micro declaration amendments and commencement | https://www.arlis.am/hy/acts/231487/latest | 2026-10-26 |

- [Current Armenian Tax Code, official Armenian text](https://www.arlis.am/hy/acts/215611/latest), especially Articles 30, 103, 125, 150, 253–270.
- [Official English Tax Code translation](https://www.arlis.am/en/acts/231892), checked against the current Armenian provisions.
- [HO-76-N annual declaration transition](https://www.arlis.am/hy/acts/206337), relevant only to the personal-return context in the comparison.

**Not yet confirmed:** taxpayer-specific classification and facts, the specialist incentives/disputes/treaty matters stated outside this ordinary comparison, fresh independent whole-country review and named professional attestation. No live taxpayer portal or return was accessed.

> Contributed by Michael Cutajar.

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

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-10-27. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `armenia-tax-optimization` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/armenia-tax-optimization. If neither is available, confirm every figure against the official source pages cited above before relying on it.
