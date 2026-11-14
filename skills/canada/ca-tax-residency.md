---
name: ca-tax-residency
description: Determine Canadian individual tax residence from actual residential ties, sojourning days and the applicable treaty. Prepare arrival and departure working papers, T1243 deemed gains, T1161 property reporting, T1244 payment deferral, T2061A elections, returning-resident adjustments and Canadian non-resident withholding or section 216/217 handoffs. Use for moving into or out of Canada, dual residence, the 183-day rule, NR73 and NR74. Distinguish an opinion, an election, accountant approval and an actual filing receipt.
version: 1.1
jurisdiction: CA
tax_year: 2026
last_updated: 2026-11-14
depends_on:
  - income-tax-workflow-base
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: cross-border
type: situation-rules
---

# Canada individual tax residence, arrival, departure and non-resident income, v1.1

## Scope

Decide an individual's Canadian federal income-tax residence and its dates, then prepare the resulting Canadian arrival/departure and non-resident working papers. Cover factual residence, ordinarily resident, deemed residence, treaty-deemed non-residence, part-year reporting, departure tax and its exceptions, Forms T1243/T1161/T1244/T2061A, returning-resident elections, Part XIII withholding, sections 216/217 and NR73/NR74 opinions. This is Canadian-side work. An existing Canadian treaty example does not determine another country's domestic tax, immigration status or filing obligations. Trusts, corporations, disputed treaty residence and section 116 dispositions need their separate analysis. [R01][R02][R04][R05][R08]

Use the actual calendar year and facts. Primary provisions and specified CRA portions below were read on 14 November 2026. Several return pages still describe 2025 and the actual currently linked forms have older revision dates. An older form revision is not a tax year. The 2026 deadlines below are derived from the legislation and current timing rules; do not invent a final 2026 return package or certified software capability. Valid 2025 preparation/amendment jobs remain covered by the separate dated bridge. This guide remains tier 2 with no professional approval claimed for this replacement.

### Answer layer

Days alone do not establish that someone left Canadian tax residence. First weigh the person's ordinary life and residential ties. Only someone who is not factually resident moves to the section 250(1) deemed-residence test. Count actual **sojourning** days, not every physical visit: at least 183 in the calendar year can produce full-year deemed residence. For either factual or deemed residence, still apply the actual treaty where dual-residence evidence exists. Section 250(5) can override that domestic residence from the relevant time. Give a dated, evidenced result, or identify the missing fact instead of asserting a final status. [R01][R04]

| Possible result | Canadian treatment, subject to the actual treaty and income rule |
|---|---|
| Factual resident throughout | Normally worldwide income throughout the year; no automatic exemption merely because the person works abroad |
| Part-year factual resident | Worldwide income during the resident part; applicable Canadian-source income during the non-resident part under 114/115, with credit restrictions |
| Deemed resident under 250(1) | Normally full-year worldwide income for a 183-day sojourner; other statutory categories and 250(2) can differ. Federal surtax/provincial consequences need their own check |
| Non-resident | Applicable Canadian-source Part I income and/or listed Part XIII payments; not worldwide income simply because a Canadian account remains |
| Deemed non-resident under 250(5) | Treaty resident elsewhere and not in Canada; Canadian non-resident consequences, including cessation/departure where applicable, from that time |

The same person can have different statuses in different periods. Do not add the table's categories together or apply a full-year deemed outcome to a factual resident who entered or left part way through the year. [R01][R02][R04]

## Ask the client first

Read existing records before asking. These six groups preserve the original input purposes and supply the form/election facts:

1. **Identity and dated history:** individual, actual year, entry/departure dates, prior Canadian residence and returns, travel records for this and any open previous year, reasons for each stay, nights/time away from work and whether each visit is sojourning or same-day commuting. Ask about Forces/government/development-program employment and related dependent or treaty-exempt family status where relevant.
2. **Ties in both places:** each owned/rented home and dates available, actual lease/tenant relationship/market terms, spouse or common-law partner, dependants, pre-existing relationship breakdown, furniture/vehicles, employment/business/investments/banks/cards, health coverage, licences/registrations, memberships, passport, work/immigration permits, mailing/telephone/subscription ties. Record intention, a promised Canadian job, length/frequency of returns and established ties abroad.
3. **Treaty facts and dates:** destination/origin country, actual treaty and amended residence article, evidence of full tax liability there, certificates/returns/opinions, permanent homes, personal/economic relations, habitual abode and citizenship if that treaty reaches them, disagreements and previous claims. For a potentially grandfathered case, continuous dual residence since 24 February 1998 matters.
4. **Property and moves:** complete worldwide legal/beneficial inventory, acquisition and inheritance dates, cost/adjustments, arrival/departure FMV evidence and currency conversion, ownership throughout any return interval, Canadian property/business/permanent establishment, registered plans/options/trust/insurance rights, months resident in the preceding 120 months and previous departure tax/security/elections. Do not substitute brokerage market value for adjusted cost base.
5. **Canadian income after/before residence:** payer, recipient/beneficial owner, payment type and date, treaty entitlement, gross amount and tax remitted date/currency, NR4 slips; Canadian employment/business/property dispositions; all Canadian rent/timber royalties and itemised expenses, Canadian-resident agent, CCA history and actual NR6 approval; pensions/benefits, world income, credits and any NR5 approval/basis.
6. **Filing and evidence:** actual return/form year, CRA correspondence/demands, NR73/NR74 opinions and changes since them, signer/representative authority, intended accepted filing channel, prior submissions/receipts, money already withheld/paid and missing records. Record deadlines separately for each return, election, information form and payment. Preparation does not authorize submission or payment.

## The method, step by step

### 1. Establish factual residence from the whole record

Apply section 250(3) and Folio 1.5-1.9: where the individual regularly lives in the settled routine of life, considering all ties, length, object, intention and continuity of stays. Factual residence comes before 250(1). Citizenship, a visa, a bank account,183 days abroad or an intention to return alone is not a complete test. A person can be domestically resident in two countries; establishing foreign ties does not itself sever Canada. [R01][R04]

**Primary ties.** A Canadian dwelling available to occupy, spouse/common-law partner and dependants will almost always be significant. A home leased to a third party on arm's-length terms may cease to be significant by itself, but review the relationship, market conditions, purpose and other ties; a lease is not an automatic safe harbour. A spouse from whom the person was already living separate and apart because the relationship broke down is not treated as an ordinary remaining spousal tie. Evidence dates matter. [R01:1.10-1.13]

**Secondary ties collectively.** Retain all the original categories: furniture/clothing/cars/recreational vehicles; social/religious/recreational memberships; Canadian employer and active business involvement; banks, cards, retirement plans and securities accounts; landed status/work permits; provincial health insurance; driver's licence/vehicle registration; seasonal or leased dwelling; passport; union/professional memberships. A **single** secondary tie alone would unusually establish residence, but several together can be significant. Mailing addresses, post-office/safety-deposit boxes, stationery/business cards, phone listings and subscriptions usually have limited weight separately, not no weight. [R01:1.14-1.15]

**Intention, duration and conduct.** No fixed period abroad automatically ends residence. A return foreseen at departure, such as a Canadian job contract, can give retained ties more weight. Intention to return without ties is insufficient by itself. Occasional visits after genuine severance do not ordinarily restore residence, but regular/lengthy visits combined with ties matter. Consider departure-tax compliance and notifications to Canadian payers as evidence of intention, not legal prerequisites that manufacture non-residence. Keep both adverse and favourable facts. [R01:1.16-1.21]

For an arrival, apply the same ties in reverse. Landed status together with provincial health coverage will usually be significant under Folio 1.25, subject to exceptional circumstances. A home bought for future retirement and leased out is not necessarily a current residential tie; the Folio also recognises limited never-before-resident/non-arm's-length sibling-letting circumstances. Do not turn that exception into a universal related-party lease rule. [R01:1.25-1.28]

Output a dated factual-residence conclusion with its supporting/opposing evidence and unresolved facts. If factual residence is established, skip only the competing 250(1) classification, **not** the treaty check in Method 3.

### 2. If not factually resident, test actual deemed-residence categories

#### Sojourning, not all physical presence

Under 250(1)(a), total 183 or more **sojourning** days in the calendar year deems residence throughout that year, before treaty override. A part of an actual sojourning day counts as a day. Determine each stay's nature first. A same-day commuter who works in Canada and returns each night to their ordinary home abroad is not sojourning on those workdays. Holiday days or work stays where off-duty time is spent in Canada can count. Keep a day ledger: date, entry/exit, purpose, sleeping/off-duty location, count/no-count/reason and evidence. Add each counted date once. Under 183 does not disprove factual residence or another 250(1) category. [R01:1.30-1.33][R04]

#### Other 250(1) categories and conditions

Do not conclude “not deemed resident” from the day count without checking applicable alternatives: Canadian Forces membership; specified federal/provincial officers or servants with the statutory prior-residence or representation-allowance condition; prescribed overseas international-development services with residence in the preceding 3 months; overseas Canadian Forces school staff filing on the specified resident basis; a dependent child of a qualifying person subject to the statutory income limit; and the treaty-exempt related/family category in 250(1)(g), with its all-or-substantially-all condition. Not every diplomat, overseas worker, spouse or child qualifies. Section 250(2) can end specified deemed treatment part way through a year; apply its exact category and date. Do not copy an old basic-personal-amount figure into the child's condition without reading the year's section 118 reference. [R04(1)-(2)][R01:1.34-1.36]

An ordinary full-year deemed resident is generally not resident in a province for provincial tax, pays the federal surtax instead and lacks provincial credits/direct tax-based provincial benefits. Folio 1.31 identifies a Quebec exception: someone resident there immediately before leaving can also be deemed resident under Quebec law and seek CRA surtax relief on filing. Refer rather than calculating both systems blindly. Do not select a province merely from the airport of entry. [R01:1.30-1.31]

### 3. Apply the specific treaty even after domestic residence is found

For potential dual residence, establish residence under the actual treaty's entry test, then use that treaty's ordered tie-breakers. Folio 1.40-1.43 treats “liable to tax” as the most comprehensive liability of the state, generally worldwide, not just tax on local-source income. Actual tax paid can be zero without destroying liability; the claimant needs evidence and abusive arrangements are not automatically accepted. A foreign passport, withholding slip or assertion alone does not prove the test. [R01]

Section 250(5) applies where otherwise resident in Canada but, under the treaty, resident in the other country **and not in Canada**. It operates from the relevant time and can trigger departure-tax and non-resident withholding consequences then. Keep the Folio's 24 February 1998 continuous-dual-residence grandfathering exception as a historical issue to verify, not a general opt-out for a person who once lived abroad. [R04(5)][R01:1.37-1.39]

#### Existing Canadian-side Canada-US residence example

Use the current Canadian published consolidated Convention, checked against the Canadian implementing Act and protocols, rather than the original 1980 schedule alone. Article IV(1) governs entry. The Folio's green-card discussion does not authorize ignoring the actual Article IV wording, including its stated substantial-presence/permanent-home/habitual-abode and closer-relations condition for the case described there. A card does not by itself settle dual residence or the Canadian result. No foreign domestic-law calculation is made here. [R01:1.44-1.45][R09][R34]

For an individual who actually satisfies Article IV(1) in **both** states, Article IV(2) proceeds as follows:

1. Permanent home available in only one state: that state. A rented room can qualify if continuously available for permanent use; ownership, size and a short hotel holiday are not the deciding labels.
2. Home in **both or neither**: state with closer personal and economic relations, the centre of vital interests. That “neither” branch is expressly in this Convention; do not replace it with a remembered generic model-treaty sequence.
3. If the centre cannot be determined: habitual abode.
4. Habitual abode in both or neither: citizenship.
5. Citizenship of both or neither: competent authorities settle by mutual agreement; do not invent a winner.

For centre of vital interests retain family/social relations, occupations, political/cultural and other activities, place of business, property management and the circumstances as a whole. Retaining the original home/family/possessions while establishing another home can be important. Read another country's own Canadian treaty before transplanting this order or any rate. [R01:1.46-1.51][R34:IV(2)]

### 4. Fix dates, periods, province and the return basis

**Leaving.** Folio 1.22 generally uses the date ties are severed, usually the latest of departure, spouse/dependants leaving and residence in the new country. These are factual indicators, not three mandatory dates to override 250(5). Preserve Folio 1.23's return-to-former-country exception: non-residence may start on leaving even while a spouse temporarily remains to sell the home or finish a school year. Record treaty-effective dates separately where they change the result. [R01]

**Entering.** Residence generally begins on entry when residential ties are established, not always the immigration-document or later bank-opening date. If the person remains merely a visitor without ties, apply Method 2 and 3 instead. A permanent entrant/exit with factual part-year residence is not automatically a full-year sojourner. [R01:1.25-1.32]

**Part-year income.** Under 114, separate worldwide income during residence from specified Canadian-source income/losses during non-residence; section 115/treaty rules govern the latter. Do not add all post-departure foreign income to the T1 or omit Canadian employment/business/taxable-property income simply because residence ended. Credits/deductions have period and income conditions, not necessarily a full-year allowance. The CRA's current pages describe limits and, where applicable, a 90% net-world-income test for the non-resident portion. Use the actual year's T1 method for the complete credit calculation. [R02][R03][R16][R18]

**Province.** Generally use significant ties at 31 December; if resident in more than one province then, use the most significant ties. The departure-year package instead uses the province/territory of residence when leaving; an arrival-year return generally uses residence at 31 December. Quebec needs its own return and analysis. A full-year deemed resident's surtax is not an arbitrary provincial-rate substitution. [R01:1.2-1.4,1.30-1.31][R03][R16]

Prepare the actual year's residence information/date on the return, identity/address, spouse/common-law partner net-world-income fields and the required split-period evidence. Keep “spouse's whole-year income” and “income for the period the taxpayer was resident” distinct where the form asks both. For someone not required to file, still notify CRA promptly of the departure date and assess separate mandatory information/election forms. Tax owing or a refund is not the complete 150 filing test: a resident-period capital disposition/gain, relevant non-resident taxable Canadian property or positive HBP/LLP balance can also require a return. [R03][R16][R32]

### 5. Build the departure property schedule and T1243

Under 128.1(4)(b),(c), property within the rule is deemed disposed at FMV and reacquired at that amount at the specified cessation times, even without a real sale. Prepare the gross gain/loss from substantiated Canadian-dollar FMV less the appropriate adjusted cost/basis, then apply the actual year's capital-gain/income rules through the T1/Schedule 3 method. A gross 60,000 gain is not 60,000 tax. Do not assume every property is capital, every loss deductible, or an inclusion rate without its own sourced year rule. [R05][R06][R38]

For each property record description/identifier and shares, beneficial ownership/share, Canadian or foreign location, acquisition year/date, original/adjusted tax basis, currency/rates, cessation-date FMV and evidence, legal classification, specific exception/election, computed gain/loss and destination. Reconcile this **complete** inventory separately to T1243, T1161, registered-plan records and later deferral/returning-resident records.

#### Departure exclusions are not the T1161 exclusions

Check all four groups in 128.1(4)(b), not only registered accounts:

| Property/group | Departure disposition treatment and qualifications |
|---|---|
| Canadian real/immovable, Canadian resource or timber resource property | Excluded by(b)(i), subject to a valid optional(d) election; later Canadian disposal may have its own tax/section 116 requirements |
| Canadian permanent-establishment business | Capital property used in, Class 14.1 property in respect of, and inventory of the business through the Canadian PE under(b)(ii). Do not require only an office label or omit Class 14.1 |
| Excluded right or interest | Use the current 128.1(10) definition below, not any asset called a “retirement investment” |
| Short-term resident, not a trust | At most 60 resident months in the preceding 120 months: property owned at the last Canadian-residence start **or acquired by inheritance/bequest afterwards** is excluded under(b)(iv). Canadian-acquired purchases are not covered merely because the person is a short-term resident |

The statutory(b)(v) returning-resident-election interaction is distinct from a voluntary departure election; inspect Method 8 before asserting a final prior-year result. [R05]

**Complete excluded-right categories.** Read 128.1(10)(a)-(l) against the actual contract: RRSP/amended plan, RRIF, RESP, RDSP, TFSA, FHSA, DPSP/revoked plan, employee profit-sharing/benefit/life-and-health arrangements, specified remuneration arrangements, pension/superannuation, retirement compensation, foreign retirement arrangement and supplementary-unemployment plan; qualifying benefit rights attributable to Canadian services; section 7 employee-option rights; retiring allowance; employee/amateur-athlete/cemetery-care/eligible-funeral trusts; annuity/income-averaging-annuity rights; CPP/provincial-plan/OAS/foreign-social-security rights and specified 56 benefits; NISA Fund No. 2; qualifying never-purchased Canadian-resident personal-trust interests; qualifying non-resident testamentary-estate interests with the 36-month condition; and Canadian life-insurance interests except the segregated-fund portion. Keep each definition's ownership, consideration, service, age and plan conditions. Private-company shares, foreign trusts and employee benefits are not automatically exempt merely by name. Arrival treatment differs for paragraph(k). [R05(10)]

**T2061A optional election.** The operative elective inclusion is **128.1(4)(d)**, not(b)(v). An individual other than a trust can elect prescribed Canadian property from(b)(i)/(ii) into a FMV disposition/reacquisition. The election also carries the income and loss limitations in(d)(ii)/(iii); it is not a free loss-creation choice. Prepare T2061A's identification, current/former addresses, cessation date/SIN, each property's description/ACB/FMV and actual authorized certification/date/position, attaching the form and applicable Schedule 3/supporting forms to the cessation-year return. Current catalogue links the 2005 revision, whose “eligible capital property” wording must be read with current Class 14.1 legislation. Do not invent a 2026 edition or use a stale form phrase to override the law. [R05][R41]

**Actual T1243.** Current catalogue links E(22), two pages. Complete the person's name/SIN/mailing address/emigration date and, on page 2, shares if applicable, property description, Canadian(C)/foreign(F), acquisition year, FMV, adjusted cost base and gain/loss. For portfolios give the full breakdown, not one unexplained net amount. Attach T1243 and applicable Schedule 3 to the return, with T2061A for an elected inclusion. Keep real pre-departure sales, principal-residence reporting and deemed dispositions separate; an excluded residence is not a finding that an actual sale is tax-free. [R38]

### 6. Test and prepare T1161 separately

Section 128.1(9) requires an emigrant individual owning **reportable property with total FMV greater than 25,000** at cessation to file the prescribed list by the individual's filing-due date. Exactly 25,000 does not trigger that rule. It covers Canadian as well as foreign reportable property and can be required even if no income-tax return is required. It is not T1135's foreign cost test, nor a list confined to departure-taxable assets. [R05][R39]

Apply the actual 128.1(10) reportable-property exclusions:

1. Money that is legal tender in Canada and deposits of such money. **Source difference:** CRA's current page and T1161 simplify this to “cash (including bank deposits)”; the statute is expressly Canadian-money wording. Do not silently exclude every foreign-currency deposit on that summary. Record currency, amount and the statutory reading; resolve any broader administrative treatment with the responsible reviewer/CRA before a foreign-cash-driven non-filing conclusion. Keep a conservative inclusion/reconciliation and the actual source difference visible.
2. Excluded rights/interests read **without** paragraphs(c),(j),(l). Employee security-option rights, the specified Canadian personal-trust interests and Canadian life-insurance interests therefore are not excluded by that cross-reference. Assess them and their FMV rather than automatically copying the departure-tax exclusion list.
3. For the same qualifying short-term non-trust resident, property brought on last arrival **or inherited/bequeathed afterwards**, only where it is **not taxable Canadian property**. The TCP condition distinguishes this reporting exclusion from the departure exclusion.
4. Each personal-use item with FMV **less than 10,000**. Exactly 10,000 is not excluded on this ground. Test per item before summing reportable property, not total household contents against 10,000.

The current E(22) one-page form asks identity/SIN/address/date, shares if applicable, full description, C/F and departure-date FMV, with extra sheets as needed. Its examples include a principal residence, shares, debt, trust/partnership interests, business/inventory, real property and security options, subject to the exclusions. Complete all reportable assets, not only the 25,000 excess. Attach to the return or send by the filing-due date even without a return. Retain a copy and actual transmission/receipt evidence. [R05][R39]

For an applicable late information return under 162(7), compute greater of 100 and 25 per late day capped at 100 days, so maximum 2,500. An on-time form does not owe the minimum 100. Do not label that ordinary example a complete analysis of all penalties or discretionary relief. [R39][R48]

### 7. Consider T1244 payment deferral and monitor it

Section 220(4.5)-(4.54) deals with a timely election and adequate/deemed security, not exemption from the gain or permission to omit the return. It excludes the specified employee-benefit-plan right/interest. Current T1244 and CRA instructions use **30 April after emigration**, even for an otherwise later self-employed T1. A2026 emigrant should arrange election/security by 30 April 2027. Deferral is available regardless of the amount where conditions are met; interest protection follows the statute's accepted/deemed-security terms, not a blanket guarantee after any late or inadequately secured election. [R06][R15][R40]

The current guidance/form requires adequate security where federal deemed-disposition tax exceeds 16,500, or 13,777.50 for a former Quebec resident, and potentially for applicable provincial/territorial tax. Exactly the stated federal amount does not cross that threshold; the form is still required. These are **tax** amounts, not gains or asset FMV. The statutory deemed-security measure uses the tax on 50,000 of trust taxable income, with the other limits in 220; do not describe the displayed threshold as a universal fixed unindexed statute or simply subtract it from a security amount without an actual CRA arrangement. Contact CRA before the due date and record the accepted amount/type/conditions. Quebec needs separate provincial handling. [R15][R40]

**Actual E(22) form, both pages:** identity/emigration fields; line 1 taxable income; lines 2-6 taxable gains/other departure income and related deductions (68900); line 7 adjusted taxable income floored at zero; lines 8-10 federal tax with/without that income, using Quebec abatement if relevant; lines 11-13 provincial/territorial tax difference, which former Quebec residents do **not** complete; line 14 total. On page 2 list property if the election covers only some T1243 assets, choose federal amount 68910 up to line 10 and provincial/territorial 68920 up to line 13, actual signature/date. Leave CRA's security-use area for CRA. Do not calculate a final T1244 tax by multiplying an unrealised gain by one flat rate. [R40]

Attach the election to the return and ensure its earlier deadline is actually met; if the return will be filed later, resolve the separate timely election channel with CRA. Record the actual election sent, acknowledgment, accepted/deemed-security analysis and continuing monitoring, not “approved” because a PDF exists. Later sales/dispositions can make deferred amounts payable: report original T1243 property description, shares and actual disposition date to Non-Resident T1 Adjustments at the Winnipeg Tax Centre; CRA instructs payment by 30 April after the disposition year. Re-entry can also crystallise deferred tax, subject to eligible unwinding. The statute permits specified discretionary extensions and a 90-day security-replacement process after written inadequacy notification; neither is automatic. [R06][R15]

### 8. Arrival FMV and returning-resident elections

On becoming resident,128.1(1)(b),(c) generally gives a deemed disposition and new Canadian acquisition cost at FMV. Keep contemporaneous valuation/currency evidence. Individual exceptions include TCP; Canadian-business inventory; Class 14.1 property in respect of a business carried on in Canada; and excluded rights/interests **other than** the defined(k)non-resident-testamentary-estate interest. Do not apply the exit-exclusion list unchanged or step up every pension/TCP asset. Cost may step down as well as up. [R05][R16]

Worldwide income is reported for the resident period. Pre-arrival foreign-source income is generally outside that Canadian income-tax base, but specified pre-arrival Canadian-source income and credit calculations still matter under 114/115. Benefit applications may require both spouses' world-income history for up to 2 years before arrival; that information is not itself a Canadian income-tax charge on the old foreign income. Use current newcomer benefit/application guidance and report even nil amounts where required. Current names include Canada child benefit and Canada Groceries and Essentials Benefit; do not promise eligibility or import obsolete benefit amounts. On leaving, notify CRA: non-residents generally lose eligibility for those resident benefits. HBP/LLP special departure rules require their own check. [R02][R03][R16][R17]

#### Returning after a previous departure

For a qualifying return after a cessation **after 1 October 1996**, inspect 128.1(6) and previous filings before claiming relief. Keep continuous ownership evidence, prior FMV/ACB/proceeds/gain, current FMV, TCP status throughout and the requested amount. Written elections are due by the **return-year filing-due date**, with property/FMV details. [R05][R06]

* **Continuously TCP branch,128.1(6)(a):** election switches off the prior(4)(b)/(c) treatment for eligible continuously taxable-Canadian properties, subject to(6)(b)'s 40(3.7)loss-reduction adjustments. The CRA summary describes reducing the old gain up to the requested amount; do not treat that summary as an unrestricted partial-gain formula that omits the statutory branch. Preserve(6.1)'s pre 5 March 2010/March 4 TCP transitional test where applicable.
* **Other eligible property,128.1(6)(c):** must be continuously owned and within the arrival deemed-disposition provision. Reduce **both** the previous departure proceeds and new arrival acquisition cost by the least of the old departure gain, current return-date FMV and the amount specified. The new basis reduction prevents giving relief twice. Complete the old-year adjustment and new-year basis schedule together.
* The election can reduce old departure tax and release some/all security, but do not promise a refund or total release before assessments/CRA confirmation. Previously deferred tax may otherwise become payable on re-entry. Trust distributions and other statutory branches are specialist work, not automatically this individual's election.

For later disposal of TCP, or an unlisted share thought to be TCP, determine actual statutory/treaty property status and section 116 duties separately. A Canadian incorporation label alone is not proof every unlisted share is TCP. This guide prepares the referral and original departure/basis records; it does not issue a compliance certificate or complete a section 116 calculation. [R05][R06]

### 9. Route Canadian non-resident income correctly

**Part I return route.** Canadian employment, business carried on in Canada, applicable Canadian scholarships/research grants and taxable gains on TCP may need a Canadian return, subject to the actual exemption/treaty. Section 2(3),114/115 and T4058 determine the base. This differs from a final withholding payment. [R02][R08][R18]

**Part XIII route.** Section 212 ordinarily imposes 25% on specified gross payments to a non-resident, subject to statutory exclusions and applicable treaty. Retain the original families: dividends; real-property rent/timber royalties; pension/superannuation/OAS/CPP-QPP benefits; retiring allowances; RRSP/RRIF/PRPP/FHSA payments; annuities; royalties and estate/trust income. Qualify by the actual payment provision, not the label alone. Interest at arm's length is generally exempt, but participating-debt interest can remain caught; non-arm's-length interest also has fully-exempt-interest exceptions. Separate residency, beneficial entitlement, income character and treaty qualification. [R07][R08]

**Registered accounts and TFSA.** Departure exclusion does not determine later payment tax. RRSP/RRIF or pension payments can fall under Part XIII; an existing TFSA holder's ordinary income/withdrawals remain exempt in Canada under the current TFSA guidance. Do not call all TFSA payments 25%withheld: death/designated-beneficiary growth has distinct rules. A non-resident can retain a TFSA, but ordinary non-resident contributions generally incur 1%monthly tax under 207.03, except qualifying transfers/exempt contributions; an excess may generate a separate tax. No new annual room accumulates for a **wholly** non-resident year; a part-year resident gets that year's annual room, which does not authorize tax-free contributions after cessation. Track resident dates, actual contributions, qualifying exceptions, designated distributions and re-entry, and use the specific TFSA method for a complete tax return. [R33][R47]

**Canadian treaty withholding examples.** For qualifying beneficial owners resident in the other state under the Canada-US Convention, Article X(2) limits Canadian portfolio dividends ordinarily to 15%, with 5% for a qualifying company owning at least 10%of the voting stock (including the specified transparent-entity ownership rule). This is not the original schedule's generic 10%company rate. Preserve Article X(7)(a)'s special 10%cap for its specified Canadian non-resident-owned investment-corporation payer/company recipient. Check effectively-connected holding/beneficial entitlement/limitation-on-benefits conditions before applying a reduced rate. Article XVIII(2)(a)'s 15%cap covers **periodic pension** payments, not all lump sums or every CPP/OAS benefit; social-security payments have separate Article XVIII(5)treatment. Read the actual payment's article. These are Canadian source-tax caps, no US domestic-tax advice. [R09][R34]

Notify Canadian payers/financial institutions of the correct residence and provide the actual treaty-entitlement evidence. Proper final Part XIII tax is generally not put on the T1 as if refundable by default. Sections 216/217 are specific alternatives below, not a universal elective refund. [R03][R08]

**Excess withholding and NR7-R.** Normally apply within 2 years after the end of the calendar year the payer **remitted** the withholding, not automatically the income year or payment date; a treaty may permit longer. Use the current form for the appropriate claim unit. The actual NR7-R requires applicant/Canadian identifier/address, gross income/currency/year, remitted/payable/refund amounts and rates, income/security/payment details, exact treaty article/residence/beneficial ownership reason, payer/nominee/custodian chain and required NR4/ownership/supporting evidence. Security payments have payment-date/security/CUSIP/ownership-specific requirements; do not combine every payer/payment into one annual lump claim. Certification is by a genuinely authorized person. The payer's withholding certificate is required in specified circumstances, especially where a slip is not in the beneficial owner's name. Keep the remittance-date proof and actual filed claim/receipt/outcome; a completed application is not an accepted refund. [R08][R42]

### 10. Section 216 rental/timber election and NR6 undertaking

Section 216 can substitute a Part I calculation on net Canadian real-property rental income/timber royalties for the usual 25%gross Part XIII tax. It is a separate return covering **all** the person's Canadian rental properties, including the actual partnership share, not only the profitable one. Business rental income, CCA recapture and an actual property sale may need different/additional returns or section 116 work. No automatic personal credits/deductions beyond 216's permitted calculation: apply its subsections rather than treating the person as an unrestricted ordinary resident. [R10][R36]

**Decision first:** compare proper final gross withholding with the complete 216 net-tax result and costs/conditions; this guide's illustrative comparison supplies a stipulated verified net-tax amount, not a complete bracket engine. Ordinary deadline is 2 years after the income year. A valid NR6 undertaking moves the required return to 6 months after year-end, and a relevant CCA-recapture disposition can make 30 April the applicable filing deadline. Verify the actual return/payment case. A balance under the current rental guide generally must be paid 30 April after the year to avoid interest; extra time to file is not extra time to pay. [R10][R11][R36]

**NR6 is advance withholding, not final 216 tax.** Use a separate actual NR6 for each year and each applicable non-resident partner. The agent must be a resident of Canada to whom the rents are paid/credited for the non-resident. Supply the taxpayer/agent identity/accounts, year/first-rent month, every property/address, ownership share, estimated gross rent and itemised expenses/net amount. For this withholding working paper exclude CCA/depreciation/amortisation; they are not interchangeable with expenses used to compute available rents. Both actual non-resident/authorized representative and agent must sign their undertakings, with representative authority if needed. [R43]

Send before/on 1 January or before the first rent is due according to the actual CRA instructions. **Continue gross withholding until written CRA approval.** Once approved, agent withholds 25%of the actual available net rents under 216(4), remits by the 15 thof the following month subject to the actual due-date rules, and keeps the approval, rent/expense ledger and NR4 evidence. The agent also has NR4-reporting duties; use that specific guide for its complete process. A positive/negative estimate alone is not written approval. [R36][R43]

**Prepare the separate T1159/section 216 return:** record identity/SIN or ITN/address, calendar year/residence, all Canadian rental-property income/expenses for the applicable non-resident period and actual ownership share, rental statements and CCA schedule where applicable. For a part-year resident, put resident-period rent on the ordinary T1 and only non-resident-period Canadian rent/related expenses on the separate section 216 return, across all applicable properties; do not count the same period twice; reconcile gross rents and withholding to all NR4 slips; carry allowable tax/credit and balance/refund through the actual year's form; obtain real certification/authority, transmit by its accepted channel and retain acknowledgment/assessment plus payment evidence separately. Current T4144 is the 2025 guide and the catalogue links the actual T1159; do not invent 2026 line numbers or assume the T1's software transmits this separate election. [R36][R37]

**Actual 2025 T1159 field bridge, not a 2026 rate card.** The downloaded E(25)has identification/SIN-ITN-TTN/address/birth/death/language fields; gross 12599 and net 12600 rent/timber income, total 15000, only actually allowable deductions 20800/20805/22000/23200, total 23300 and taxable 26000 floored at zero. Its annual tax table and non-resident surtax calculation lead to 43500. Withholding 43700 requires NR4 slips; recapture tax 47600 requires the indicated T2064/T2068 copy; totalcredits 48200 then refund 48400 or balance 48500. Do not reuse the 2025 table's rates/bands for 2026. Use T4144 for the actual deduction conditions and no double claim, including special RRSP administrative-limit treatment, rather than assuming every field permits a deduction. The real certification includes signature/telephone/date; a tax professional's fee yes/no/name/telephone has its own box. [R36][R52]

For the 2025 paper route, T4144 directs residents of Denmark, France, Netherlands, UK and US to Winnipeg Tax Centre, PO Box 14001, Station Main, Winnipeg MB R3C 3M3; other countries to Sudbury Tax Centre, 1050 Notre Dame Ave, Sudbury ON P3A 5C2. Recheck the current guide for an actual later-year submission. These mailing destinations differ from the Part XIII NR7-R/NR6 application instructions. Save the signed packet, proof of mailing/receipt, assessment and separate payment record; no actual filing is performed here. [R36]

An approved NR6 requires timely filing even with loss, no tax or no refund. Failure can restore 25%gross liability and an agent assessment for the shortfall plus applicable interest/penalties. **Do not say every late 216 return is irretrievably invalid:** CRA's 216(1)late-filing policy can give eligible voluntary applicants one opportunity, excluding cases already told about Part XIII responsibilities, CRA action and approved NR6. The policy says penalties will not be charged but interest may remain. Rare extraordinary 216(4)extensions under 220(3)are discretionary, not the 216(1)policy or a promised waiver. Preserve the normal deadline, communication chronology, application and actual decision. [R11][R35][R36]

### 11. Section 217 pension/benefit election and NR5

Check statutory “Canadian benefits” in 217(1)against 212(1)(h),(j)-(m),(q), not every Canadian payment. T4058 lists OAS, CPP/QPP, superannuation/pension, RRSP/PRPP/RRIF, death benefits, EI, retiring allowances, supplementary-unemployment, DPSP, retirement-compensation arrangement/purchase amounts, prescribed government assistance and Auto Pact benefits. OAS may also have a separate T1136/OASRI requirement. A treaty-exempt or non-qualifying amount is not automatically brought into 217 merely to reclaim withholding. [R07][R08][R12]

Compute the actual 217 alternative using world income and required schedules, compare with correct non-resident tax, then make the election on the return. Section 217(3)uses its greater-of bases; (4)/(5)limit credits and (6)provides a special credit. The CRA's “same rate as residents” summary does not mean unrestricted resident credits or tax only on one selected pension. Full applicable credits need the statutory all-or-substantially-all test; otherwise apply the permitted capped alternatives. Preserve post-departure eligible income for an emigrant, without treating the whole resident year as non-resident. [R03][R08][R12]

Ordinarily file within 6 months after year-end (30 June), with any balance paid 30 April. The current due-date page warns the filing date can differ with other Canadian employment/business, specified partnership or TCP income; use the actual non-resident guide/return deadline and do not promise a later election opportunity. Weekend/recognised-holiday rules apply. CRA states an ordinary late 217 election cannot be accepted; if correct non-resident tax was withheld it remains final, otherwise CRA can assess the shortfall. Do not import the 216(1)late policy into 217. [R13]

Prepare actual identity/year/residence, eligible-income and withholding reconciliation, world-income Schedule A and applicable credit/election schedules for the actual year; use the actual T4145 [R54] and the applicable non-resident package for the complete return fields, not a fabricated 2026 box. Keep the comparative calculation, election instruction, authorized certification, filing confirmation/assessment and separate payment record. A source-audited method is not evidence the real client has filed or an accountant approved their result. [R08][R12][R13]

**Actual 2025 T4145 execution bridge.** Write “Section 217” atop page 1. Report all eligible 217 income and required other Canadian employment/business/limited-partner/TCP income, with resident-period world income for a part-year resident. For the full-year non-resident case complete Schedule C Part 1 to establish the non-resident tax actually required, distinct from withholding. Complete Schedule Aworld income, then the greater-of taxable income/net-world-income-after-adjustments tax step; calculate applicable Schedule Bcredit limits and Schedule C Part 2 adjustment where required. Attach actual A/B/Cschedules and slips; withholding goes to 43700 and the alternative tax payable to 43500. Part-year residents use the applicable provincial return rather than blindly applying the full-year non-resident surtax. Additional provincial business/employment or Quebec work needs its own form/return check. [R54]

Compare that alternative 43500 with the required withholding on Schedule C44300 plus applicable tax on other Canadian income. CRA says it takes the election into account only if beneficial. If not beneficial, excess withholding may instead support NR7-R; if underwithheld, the shortfall remains payable. If beneficial but underwithheld, there can still be a balance. This is why a promise of a refund from the pension amount alone is wrong. The 2025 guide's percentage tables are not 2026 figures; retain the method, obtain the actual year's forms/rates. [R54]

**NR5 advance reduction.** For a 217-based application the current T4145 instructs sending NR5 on/before 1 Octoberor before the first payment is due; record the intended income/approval year. [R54] Current form can cover 5 tax years subject to actual approval and changed facts. For a **217-based** reduction the applicant must file a timely 217 return for every covered year; reduced withholding is not final relief without those returns. Record actual approved years/rates/payers, not “five years from the form download.” Current NR5 also contains a separate treaty-exemption-only route for residents of its listed countries who are **not** electing 217; do not force those approvals into the 217 annual-return rule. Read that form's current country list and exact qualifying income, rather than inventing a universal treaty exemption. [R44]

The actual NR5 has identification/spouse/departure/date-of-birth fields, qualifying benefit types and payer/account/periodic-or-lump-sum amounts, estimated other Canadian and foreign world income, non-refundable-credit/dependant information and real certification. Where estimated world income changes, it instructs an amended application within 30 days. Direct registered-plan transfers may use NRTA1 instead. Submission options on the current form include My Account Submit Documents, mail or fax; approval evidence must precede payer reduction. Keep actual application/decision and annual 217 control separately. [R44]

### 12. NR73/NR74 opinions, working-paper output and completion controls

Use NR73 for someone leaving/planning to leave and NR74 for entering/brief stays if an opinion would help. These are optional requests, not residence elections, tax returns or binding clearance certificates. A person's legal status does not await their completion. The opinion depends entirely on full and accurate facts and is not binding on CRA; changed facts can change it. A binding advance ruling may be available in appropriate prospective cases where facts can be known; Competent Authority Services may assist in treaty disputes. [R01:1.53-1.57][R45][R46]

Use the actual 2024 revision's relevant identification/addresses, move purpose/dates/usual residence, employment/relationships, prior residence and treaty statement, all Canadian/foreign ties, intention/visits and additional information. Do not preselect “non-resident” merely to obtain a desired response. Obtain the actual person's certification/date, attach needed facts/authority, and follow the current form's online Submit Documents via My Account/Represent a Client, or mail/fax instructions. The old Folio's mail/fax paragraph is not the only current channel. Retain submitted version, receipt, CRA questions/opinion, actual scope/date and subsequent changes. [R45][R46]

For each case produce these complete handoff artifacts:

* **Residence memo:** actual year/timeline, factual ties both ways, separate sojourning ledger, applicable 250 category and conditions, treaty entry/tie-breakers with article and evidence, resulting status for each period/province, uncertainty and specific owner/action.
* **Arrival/departure property paper:** complete inventory, ownership, original/adjusted costs and CAD/FX evidence, arrival/exit FMV s, classification/exception/election for each asset, T1243 gains, separate T1161 inclusion/test/list, T2061Aand T1244 choices/deadlines/security, return-year unwinding link and both basis adjustments.
* **Non-resident income paper:** payer/payment/treaty table, proper gross withholding vs actual tax, remittance date and NR7-R claim units, all Canadian rental/NR6 and 216 details, eligible 217 benefits/world-income/credits/NR5 basis, required returns and dated filing/payment/approval evidence.
* **Action register:** actual responsible person, deadline source/raw date/adjusted-date check, intended valid channel, genuine signature/authority, draft/submitted/acknowledged/assessed status, separate payment/security evidence and outstanding facts. Prepared forms are **PREPARED FOR REVIEW**, not filed or approved. READY requires the applicable case-review record (reviewer, exact version/scope/date), resolved material gaps and authorization under the workflow dependency. Do not mark a case complete because this source method passed AI checks.

Retain the original ten completion controls: factual/deemed/treaty sequence; evidenced ties/dates; separated commuting/sojourning count; actual treaty/liable-to-tax proof; complete departure inventory/T1243/Schedule 3/T1161; timely T1244/security; arrival FMV basis; correct payer notices and refund/reduction applications;216/217 deadlines; and NR73/74 where useful. Add the specific source-conflict, inherited-property, TFSA, unwind-basis and actual receipt checks above. Missing records get a partial, labelled working paper with a focused request, not guessed facts or a blanket refusal.

## Rates, bands and thresholds

All monetary amounts below are CAD. Conditions belong with each number. Security measures, plan amounts and administrative timing must be rechecked for the actual year; the old blanket claim that none of these amounts is indexed is not used.

| Item | Actual rule and conditions | Official URL |
|---|---|---|
| Sojourner |183 or more actual sojourning days/parts in a calendar year, only after no factual residence; treaty overlay still required |https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-250.html and https://www.canada.ca/en/revenue-agency/services/tax/technical-information/income-tax/income-tax-folios-index/series-5-international-residency/folio-1-residency/income-tax-folio-s5-f1-c1-determining-individual-s-residence-status.html |
| Short residence |Not more than 60 resident months in preceding 120 months; non-trust and actual last-arrival/inheritance property conditions; T1161 also needs non-TCP |https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-128.1.html |
| T1161 |Reportable-property total FMV strictly over 25,000; each personal-use item under 10,000 excluded, exactly 10,000 not excluded on that ground |https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-128.1.html |
| Ordinary late T1161 |Where 162(7)applies,25/day, minimum 100, capped 100 days/2,500; no minimum for on-time filing |https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-162.html and https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t1161/t1161-22e.pdf |
| T1244 |30 April after emigration; security where federal tax exceeds 16,500 or 13,777.50 for former Quebec residents, possible provincial security; actual 220 conditions |https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t1244/t1244-22e.pdf and https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-220.html |
| Part XIII |Ordinarily 25%gross of listed 212 payments, with statutory/treaty exemptions; not 25%of all payments to a non-resident |https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-212.html |
| Canadian treaty dividends |Canada-US X(2):15%ordinarily;5%qualifyingcompany with at least 10%voting ownership; X(7)(a)special 10%branch preserved |https://www.canada.ca/en/department-finance/programs/tax-policy/tax-treaties/country/united-states-america-convention-consolidated-1980-1983-1984-1995-1997-2007.html |
| Canadian treaty periodic pension |XVIII(2)(a)15%cap for qualifying beneficial owner's periodic pension; social-security and lump sums require distinct treatment |https://www.canada.ca/en/department-finance/programs/tax-policy/tax-treaties/country/united-states-america-convention-consolidated-1980-1983-1984-1995-1997-2007.html |
| NR7-R |Normally 2 years after end of **remittance** year; a treaty may extend; actual ownership/payment claim units matter |https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4058/non-residents-income-tax.html and https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/nr7-r/nr7-r-18e.pdf |
|216 filing |Normally 2 years after income year;6 months if undertaking; relevant recapture case 30 April; separate payment and discretionary late-policy conditions |https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-216.html and https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/individuals-leaving-entering-canada-non-residents/electing-under-section-216/when-file.html |
| NR6 |Written approval before 25%net-available withholding; exclude CCA from withholding expenses; remit ordinarily 15 thfollowingmonth |https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/nr6/nr6-23e.pdf |
|217 filing/payment |Ordinarily 6 months/30 June election;30 Aprilbalance; other income can change filing date; not the 216 late policy |https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-217.html and https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/individuals-leaving-entering-canada-non-residents/electing-under-section-217/when-file.html |
| NR5 |Actual 5 tax-year approval scope; annual 217 returns for 217-based reduction, distinct treaty-only branch; changed world-income estimate amended within 30 days |https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/nr5/nr5-23e.pdf |
| TFSA non-resident contribution |207.03:1%monthly contribution tax with qualifying-transfer/exempt-contribution and cessation/distribution conditions; possible separate excess tax |https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-207.03.html and https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/tax-free-savings-account/non-resident.html |

## Boundary and exception table

| Original situation retained | Actual qualified result |
|---|---|
| Leaving, available Canadian home and family remain |Strong factual-residence evidence, then actual treaty overlay if dual resident, not unconditional Canadian residence |
| Home let at arm's length, no other significant ties |May cease to be significant alone; all circumstances/other ties still matter |
| Only secondary ties remain |One tie alone unusually sufficient; weigh several together, no automatic non-residence |
| Intention to return but no ties |Intention alone insufficient; no universal days-abroad test |
| Non-factual resident,183 days in Canada |Classify actual sojourning first;183 sojourning days gives domestic deemed residence, then treaty |
| Same-day foreign-home commuter |Workday presence not automatically sojourning; separately count holiday/other stays |
| Treaty favours other country |Apply 250(5)and its effective time/historical exception, with departure/non-resident consequences |
| At most 60 resident months of 120 |Specified arrival/inherited property exclusion, not all Canadian-purchased property; T1161 non-TCP condition separate |
| RRSP/RRIF/TFSA on departure |Excluded qualifying rights; later payment tax differs, ordinary TFSA-holder withdrawals not blanket Part XIII |
| Late 216/217 |Separate 216(1)discretionary policy/216(4)exceptional extension from ordinary 217 non-acceptance; no promised relief |

## Filing and payment

Dates below are standard individual cases, not deceased/other special extensions.150 allows the qualifying business/cohabiting-spouse 15 June filing date except primarily tax-shelter expenditures; tax/payment remains separate. Check current CRA recognised holidays and actual receipt/postmark/payment rules, especially a year-end window. A calendar computation does not prove portal acceptance. [R11][R13][R32][R51][R50]

| Job |2026 income/departure or return year |2025 dated bridge |
|---|---|---|
| Ordinary T1/arrival/departure plus applicable T1243/T1161/T2061A |30 April 2027; qualifyingbusiness/spouse 15 June 2027; T1161 also due without T1 |30 April 2026 or qualifying 15 June 2026 |
| Ordinary balance/T1244 and security |30 April 2027; later T1 filing does not delay election |30 April 2026 |
|217 ordinary filing |30 June 2027; actual other income/death conditions checked |30 June 2026, ordinarily already past |
|216 ordinary filing without undertaking |Raw 2-year endpoint 31 December 2028 is Sunday. Apply CRA next-business-day rule and check the following recognised holiday before finalising adjusted filing date |31 December 2027, Friday |
|216 approved NR6 required filing |30 June 2027 even if loss/nil; recapture case 30 April 2027 |30 June 2026 or recapture 30 April 2026 |
|216 balance |Generally 30 April 2027 under current T4144 timing; later election-filing window is not an interest-free payment extension |30 April 2026 |
| NR7-R tax remitted in named year |Raw 2-year endpoint 31 December 2028; Sunday/next-business-day and treaty extension need actual applicable confirmation |31 December 2027 for 2025 remittances |
| Return-year unwinding election |By actual 2026 return-year filing-due date in 2027, not automatically departure's T1244 date |By actual 2025 return-year filing-due date in 2026 |

For 216/217, CRA explicitly treats a return received/postmarked by the next business day as timely when its due date is a recognised holiday/weekend; apply the payment method's actual receipt/postmark rule. T4144 distinguishes bank credit to CRA, a bank-stamped remittance voucher, a pre-authorized debit's negotiable date and mailed-payment postmark. Its holiday/weekend payment paragraph accepts the specified next-business-day receipt or postmark; the section 217 due-date page gives its own payment-receipt wording. Keep the actual method and applicable authority rather than claiming all payments share one receipt rule. [R36] For NR7-R keep the raw statutory/administrative limit and confirm the actual applicable extension rather than importing a 216 page as its sole authority. Do not file at the raw Sunday endpoint in reliance on a guessed Monday date. NR73/NR74 have no election deadline in this method and do not postpone any tax obligation. [R08][R11][R13][R42][R51][R50]

## Worked cases

These cases test the Canadian rules from the stated facts. Their arithmetic does not independently prove residence, treaty eligibility, a tax engine's result or filing. Obtain the missing evidence rather than turning a numeric example into a client conclusion.

### Case 1. Priya's departure with listed shares

Preserve the original family: resident since birth, Priya leaves for Australia on 15 August 2026, having sold her Toronto condo before departure. **Assume the documented ties and applicable treaty establish cessation on that date**; a flight alone does not. Her remaining listed shares have CAD 40,000 ACB and 100,000 FMV. Gross deemed gain is 60,000, reported on T1243/Schedule 3 under the year's applicable capital-gain rules. Her qualifying RRSP/TFSA rights are excluded from departure disposition. Assuming no other reportable property, the shares'100,000 FMV alone exceeds 25,000, so T1161 is required. The earlier condo sale has its separate reporting/principal-residence analysis, not an automatic exemption here. [R05][R38][R39]

Priya may consider T1244 by 30 April 2027; its federal-tax difference must first be computed, not equated to the 60,000 gain. In this **stipulated non-Quebec form arithmetic only**, taxable income 100,000 includes 30,000 of taxable departure income, no related deductions; the independently supplied annual tax calculation gives federal tax 20,000 versus 10,000 and provincial tax 6,000 versus 3,000. T1244 adjusted income 70,000, federal difference 10,000, provincial difference 3,000 and line 14 total 13,000. Federal 10,000 is below 16,500, but actual form/election and any provincial security treatment still need checking. No gain inclusion rate is certified by the supplied 30,000 input. [R15][R40]

```oa-check
name: Priya gross departure gain and supplied T1244 form differences
inputs:
  acb: 40000
  fmv: 100000
  taxable_income: 100000
  taxable_departure_income: 30000
  federal_with: 20000
  federal_without: 10000
  provincial_with: 6000
  provincial_without: 3000
steps:
  - gross_gain: fmv - acb
  - adjusted_taxable_income: max(0, taxable_income - taxable_departure_income)
  - federal_difference: federal_with - federal_without
  - provincial_difference: provincial_with - provincial_without
  - total_difference: federal_difference + provincial_difference
expected:
  gross_gain: 60000
  adjusted_taxable_income: 70000
  federal_difference: 10000
  provincial_difference: 3000
  total_difference: 13000
```

### Case 2. The three original T1161 late examples and an on-time control

For an actual 162(7)failure,30 late days gives 750,3 days gives the minimum 100, and 120 days is capped at 100 days/2,500. No such failure for on-time filing means 0, not 100. These ordinary examples do not decide discretionary cancellation or other penalties. [R39][R48]

```oa-check
name: T1161 applicable late penalty with cap and on-time control
inputs:
  per_day: 25
  minimum: 100
  cap_days: 100
  late_30: 30
  late_3: 3
  late_120: 120
  on_time_failure: 0
steps:
  - penalty_30: max(minimum, per_day * min(late_30, cap_days))
  - penalty_3: max(minimum, per_day * min(late_3, cap_days))
  - penalty_120: max(minimum, per_day * min(late_120, cap_days))
  - on_time_penalty: on_time_failure * minimum
expected:
  penalty_30: 750
  penalty_3: 100
  penalty_120: 2500
  on_time_penalty: 0
```

### Case 3. Tom, short residence and inherited-property reporting

Tom moves from the UK in March 2022 and leaves in February 2026. Assume records establish Canadian residence of no more than 60 months in the preceding 120 months, actual cessation, and no trust. Shares he owned when last becoming resident fall within 128.1(4)(b)(iv); shares bought during Canadian residence do not qualify merely from the short stay. Add the missing inherited branch: shares inherited/bequeathed after that arrival can qualify too. Do not call a purchase an inheritance or infer residency months solely from an immigration card. [R05]

Illustrative departure FMV s: arrival-owned non-TCP shares 40,000; later inherited non-TCP shares 20,000; Canadian-residence purchases 30,000; inherited TCP 25,000. The first two are excluded from both the departure disposition under this short-term rule and T1161 reportable property. The inherited TCP can be excluded under the departure short-term property rule but **not** the T1161 short-term reporting exclusion. Assuming no other exceptions, T1161 includes 30,000+25,000=55,000, the complete inventory is 115,000, of which the 60,000 non-TCP arrival/inherited property is excluded from the reporting sum. Only a property-by-property schedule gives the right answer. The purchase's gain still needs its own ACB. [R05][R39]

```oa-check
name: Short-resident separate departure and T1161 property inventories
inputs:
  arrival_non_tcp: 40000
  inherited_non_tcp: 20000
  purchased: 30000
  inherited_tcp: 25000
steps:
  - inventory_fmv: arrival_non_tcp + inherited_non_tcp + purchased + inherited_tcp
  - short_reporting_exclusions: arrival_non_tcp + inherited_non_tcp
  - reportable_fmv: inventory_fmv - short_reporting_exclusions
  - reporting_tcp_retained: reportable_fmv - purchased
expected:
  inventory_fmv: 115000
  short_reporting_exclusions: 60000
  reportable_fmv: 55000
  reporting_tcp_retained: 25000
```

### Case 4. The original 190-day visitor and commuter, corrected

The original visitor is a US retiree with no Canadian home/family ties, staying 190 days in 2026. **First classify those dates as actual sojourning, not merely part-day border presence.** If 190 qualify and she is not factually resident,250(1)(a)gives domestic full-year deemed residence. That does **not** yet prove Canadian worldwide-income tax: check actual Article IV residence in both countries, permanent homes/centre/habitual abode and the other treaty steps. If the treaty assigns exclusive residence elsewhere,250(5)changes the Canadian result. With insufficient treaty facts the output is a provisional domestic result and focused request, not unconditional full-year tax/surtax. The domestic federal-surtax result applies only if Canadian deemed residence survives that check, with the Quebec exception considered. [R01][R04][R34]

The original same-day commuter who works in Canada and returns to a foreign home each night is not sojourning on those workdays. For a separate day-count control, a documented set has 170 whole sojourning dates and 13 distinct part-day sojourns, no duplicates:183, meeting the domestic threshold. Another set has 190 same-day commuting workdays and 12 holiday-sojourning dates:12 counted, below 183. Neither count decides factual residence or the treaty. [R01:1.33]

```oa-check
name: Distinct sojourning dates and excluded commuting control
inputs:
  whole_sojourns: 170
  distinct_part_sojourns: 13
  commuting_days: 190
  counted_per_commuting_day: 0
  holiday_sojourns: 12
steps:
  - qualifying_sojourns: whole_sojourns + distinct_part_sojourns
  - commuter_sojourns: commuting_days * counted_per_commuting_day + holiday_sojourns
  - commuter_shortfall: 183 - commuter_sojourns
expected:
  qualifying_sojourns: 183
  commuter_sojourns: 12
  commuter_shortfall: 171
```

### Case 5. The original Canadian dividend/refund and corporate-rate correction

Preserve the original 1,000 Canadian listed-company dividend to a qualifying US-resident individual beneficial owner: statutory default 250, treaty cap 150, excess 100 if 250 was remitted. NR7-R needs actual treaty qualification, claim-unit evidence and the **remittance-year** time limit. It is not automatically every person's 100 refund. [R07][R08][R34][R42]

For comparison only, an otherwise qualifying company with at least 10%voting ownership under X(2)(a)has a 50 cap, not the old guide's 100. The special X(7)(a)non-resident-owned-investment-corporation branch, if its distinct facts hold, has 100 cap. These separate facts must not be merged into a generic company rate.

```oa-check
name: Canadian treaty dividend source-tax caps on distinct qualified facts
inputs:
  gross: 1000
  default_rate: 0.25
  portfolio_rate: 0.15
  qualified_company_rate: 0.05
  special_investment_company_rate: 0.10
steps:
  - default_tax: gross * default_rate
  - portfolio_cap: gross * portfolio_rate
  - potential_portfolio_refund: default_tax - portfolio_cap
  - ordinary_company_cap: gross * qualified_company_rate
  - special_company_cap: gross * special_investment_company_rate
expected:
  default_tax: 250
  portfolio_cap: 150
  potential_portfolio_refund: 100
  ordinary_company_cap: 50
  special_company_cap: 100
```

### Case 6. The original 24,000 rent,216 decision and NR6 CCA distinction

A non-resident receives 24,000 gross Canadian property rent in 2026. Without a valid alternative,25%gross tax is 6,000. For a useful **decision both ways**, suppose a separate verified 216 annual calculation gives 3,000 tax from the actual facts: timely election would produce 3,000 potential refund of the 6,000 already remitted. If that calculation instead gives 6,500, the election would leave 500 payable; do not elect reflexively or promise a refund just because expenses exist. The alternative taxes are stipulated inputs, not a complete tax calculation from this guide. [R10][R36]

Separately, an approved NR6 with 24,000 gross rent and 8,000 eligible cash expenses gives 16,000 available net rent and 4,000 withholding at 25%;3,000 CCA is **excluded** from this withholding-expense paper. Wrongly subtracting it would produce 3,250, short 750. Actual annual 216 tax may use allowable CCA subject to its own rules and is not 4,000 simply because that was remitted. Until written approval, keep gross withholding. [R43]

The 2026 ordinary 216 filing raw endpoint is 31 December 2028, a Sunday, subject to the applicable next-business-day rule; an approved NR6 requires 30 June 2027 even for a loss/nil return, or the earlier relevant 30 Aprilrecapture branch. Do not omit the generally 30 Aprilbalance deadline. If ordinary filing was late, assess the actual 216(1)policy eligibility and communications; approved NR6 does not qualify under that policy. [R11][R35][R36]

```oa-check
name: Rental election comparison and approved NR6 cash-expense base
inputs:
  gross: 24000
  rate: 0.25
  verified_low_216_tax: 3000
  verified_high_216_tax: 6500
  eligible_cash_expenses: 8000
  cca_not_withholding_expense: 3000
steps:
  - gross_tax: gross * rate
  - low_case_refund: gross_tax - verified_low_216_tax
  - high_case_payable: verified_high_216_tax - gross_tax
  - available_net: gross - eligible_cash_expenses
  - approved_net_withholding: available_net * rate
  - wrong_withholding: (available_net - cca_not_withholding_expense) * rate
  - withholding_shortfall: approved_net_withholding - wrong_withholding
expected:
  gross_tax: 6000
  low_case_refund: 3000
  high_case_payable: 500
  available_net: 16000
  approved_net_withholding: 4000
  wrong_withholding: 3250
  withholding_shortfall: 750
```

### Case 7. Returning-resident basis relief is not free double relief

Assume an individual ceased residence after 1 October 1996, continuously owns eligible non-TCP property, and the full 128.1(6)(c)conditions are met. Original ACB 40,000, departure FMV/proceeds 100,000 and gain 60,000; return-date FMV 90,000; specified reduction 30,000. Least-of reduction 30,000 means old proceeds 70,000 and old gain 30,000, **and** new arrival basis 60,000 instead of 90,000. Reducing only the old gain while retaining 90,000 new basis would overstate future basis by 30,000. A later sale 80,000 would yield 20,000 gross gain using that adjusted basis, before its own tax rules. This arithmetic is not the continuously-TCP/(6)(a)/(b)branch or a trust election. [R05][R06]

```oa-check
name: Returning resident least-of reduction applied to both years
inputs:
  old_acb: 40000
  old_proceeds: 100000
  return_fmv: 90000
  specified: 30000
  later_sale: 80000
steps:
  - old_gain: old_proceeds - old_acb
  - reduction: min(old_gain, return_fmv, specified)
  - adjusted_old_proceeds: old_proceeds - reduction
  - adjusted_old_gain: adjusted_old_proceeds - old_acb
  - new_basis: return_fmv - reduction
  - later_gross_gain: later_sale - new_basis
expected:
  old_gain: 60000
  reduction: 30000
  adjusted_old_proceeds: 70000
  adjusted_old_gain: 30000
  new_basis: 60000
  later_gross_gain: 20000
```

### Case 8. TFSA contribution tax and ordinary holder withdrawal

A non-resident contributes 2,000 while non-resident. Assume no qualifying transfer/exempt contribution, no designated distribution or residence resumption before the relevant 3 month-ends, and 3 taxable monthly periods under 207.03. Non-resident contribution tax is 20 a month,60 total. If a separately established 2,000 excess also remains for 3 taxable periods, an additional illustrative 60 could arise under that separate excess regime; this method does not adjudicate excess-room records. An ordinary holder's 1,000 TFSA withdrawal is not 250 Part XIII tax: Canadian tax on that ordinary withdrawal is 0 under the TFSA guidance. Foreign tax and death-beneficiary growth are different questions. [R33][R47]

```oa-check
name: TFSA stipulated non-resident contribution months and holder withdrawal
inputs:
  contribution: 2000
  monthly_rate: 0.01
  taxable_months: 3
  separately_established_excess: 2000
  separate_excess_months: 3
  ordinary_holder_withdrawal: 1000
  canadian_ordinary_withdrawal_rate: 0
steps:
  - monthly_nonresident_tax: contribution * monthly_rate
  - nonresident_tax: monthly_nonresident_tax * taxable_months
  - illustrative_separate_excess_tax: separately_established_excess * monthly_rate * separate_excess_months
  - ordinary_withdrawal_tax: ordinary_holder_withdrawal * canadian_ordinary_withdrawal_rate
expected:
  monthly_nonresident_tax: 20
  nonresident_tax: 60
  illustrative_separate_excess_tax: 60
  ordinary_withdrawal_tax: 0
```

### Decision regressions which arithmetic cannot prove

1. A factual resident below 183 days: do not skip residence or its treaty overlay.
2.183 physical days made solely of same-day commuting: do not mechanically deem residence.
3.190 actual sojourning days plus credible foreign treaty residence: domestic result provisional until treaty, not unconditional worldwide tax.
4. Canadian-US treaty home in neither country: actual IV(2)(a)still goes to centre of vital interests; do not “correct” this into another treaty's order.
5. Canadian home/family retained plus foreign treaty residence: factual ties are not the end of the sequence.
6.60 versus 61 resident months in the 120-month window: the short-resident exception switches only on actual qualifying facts; inheritance-after-arrival retained.
7. T1161 reportable FMV exactly 25,000 versus 25,000.01: only the latter exceeds the threshold. Personal-use item 9,999.99 versus 10,000: only the former meets the “less than” exclusion.
8. Foreign-currency cash: actual statutory CAD wording/CRA-summary difference remains visible; do not silently drop it.
9. Federal T1244 tax 16,500 exactly versus 16,500.01; Quebec 13,777.50 versus 13,777.51: threshold crossing differs, but the timely election remains required on both sides.
10. Ordinary 216 late voluntary request versus approved NR6 or prior CRA action: different policy eligibility;217 has no borrowed 216 policy.
11. NR5 approvedfor 217 reduction versus actual treaty-exemption-only branch: annual 217 obligation is not identical.
12. TFSA ordinaryholder versus registered pension versus death-beneficiarygrowth: departure-excluded does not mean all later payments share a tax.
13. Unwinding without continuous ownership/TCP proof: do not apply the numerical example until the branch qualifies, and adjust both basis/proceeds where required.
14. Draft form versus real signed submission/receipt/assessment/payment: none is interchangeable; no invented accountant approval or filing completion.

## When to refuse or refer

Preserve all original referral purposes while still completing useful supported work:

* **R1, disputed ties/material bill:** record the evidence and alternative dated outcomes; refer the contested residence conclusion to the responsible professional. NR73/NR74 can help; a prospective ruling may be appropriate. Do not refuse the entire inventory or deadline paper because one tie is uncertain.
* **R2, treaty dispute or later tie-breakers:** retain the actual treaty/article and missing permanent-home/centre/habitual-abode/citizenship facts; route unresolved dual residence or another country's disagreement to competent-authority/professional assistance. Do not manufacture a mutual-agreement outcome.
* **R3, separate taxpayer/system:** Quebec provincial residence/return/surtax/security, trusts/corporations and actual section 116/TCP sales need their own method. Preserve individual inputs, form history and basis schedules for that handoff.
* **R4, difficult departure property/security:** private-company valuations, businesses/PE/Class 14.1, options, foreign trusts, life insurance, post-departure losses, unusual returning-resident elections and negotiated security require specialist review. State which classification/valuation/acceptance is missing and the deadline at risk. No invented CRA acceptance or universal collateral formula.
* **R5, foreign/treaty claims not read:** do not assert a foreign domestic tax result, foreign filing obligation or reduced treaty rate without its actual current article and entitlement evidence. Existing Canadian treaty examples are conditional Canadian source-tax analysis.
* **R6, days-only non-residence:** never tell someone they ceased residence simply because they spent a set number of days abroad, surrendered a licence or filed NR73. Produce the ties/day/treaty analysis and request only what is missing.

Hold a final non-filing/election/refund conclusion where the unresolved foreign-cash source difference, actual annual form/channel, treaty entitlement, late-policy decision, missing basis/valuation or review/authority record could change it. Continue the evidence-backed working paper. Independent AI source review is not professional approval of this method or the person's filing.

## Sources

These are the actual bounded portions read on14November2026, not whole-Act audits or a count of successful downloads. Actual T1161and both T1244pages were also rendered and visually inspected. Current older-revision PDFs and dated2025return materials are identified explicitly.

| Source and actual portion read | Official URL | Read on |
|---|---|---|
|R01: Read for Folio1.1-1.57, all operative residence/ties/day/date/province/treaty/opinion/ruling/MAP paragraphs|https://www.canada.ca/en/revenue-agency/services/tax/technical-information/income-tax/income-tax-folios-index/series-5-international-residency/folio-1-residency/income-tax-folio-s5-f1-c1-determining-individual-s-residence-status.html|2026-11-14|
|R02: Read for ITA114(a)-(c), full operative part-year income/deduction rule|https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-114.html|2026-11-14|
|R03: Read for CRA emigrant page, package/return/identification/income/credits/notification/afterdeparture sections|https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/individuals-leaving-entering-canada-non-residents/leaving-canada-emigrants.html|2026-11-14|
|R04: Read for ITA250(1)-(3),(5), exact statutory deemed classes/part-year/treaty override; corporate(4)read only as neighboring out-of-scope context|https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-250.html|2026-11-14|
|R05: Read for ITA128.1(1),(4),(6),(6.1),(8)-(10), exact arrival/exit/elective/unwind/reporting/excluded rights and neighboring postdeparture-loss boundary|https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-128.1.html|2026-11-14|
|R06: Read for CRA dispositions page, full operative deemed/list/deferral/unwind/subsequent-disposition guidance|https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/individuals-leaving-entering-canada-non-residents/dispositions-property.html|2026-11-14|
|R07: Read for ITA212(1)opening,(b),(h), benefit-payment provisions,(2),(3)interest definitions; no all-PartXIII Act audit|https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-212.html|2026-11-14|
|R08: Read for CRA T4058 actual2025 opening/filing-date bridge/PartXIII andPartI methods/NR7R/transfers/216-217eligibleincome/world-income-credit portions|https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4058/non-residents-income-tax.html|2026-11-14|
|R09: Read for Canadian Convention Act C-10.7, originalIV2/X plus actual amended residence entry/protocolArticle3 at163558 and dividendArticle5 at167036/227987; bounded Canadian treaty portions only|https://laws-lois.justice.gc.ca/eng/acts/C-10.7/FullText.html|2026-11-14|
|R10: Read for ITA216(1)-(6),(8), complete operative ordinary/undertaking/net-income/refund/recapture/restriction rules|https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-216.html|2026-11-14|
|R11: Read for CRA216when-file entire operative page, actual2025dates and generic period/recapture/weekend/late policy link|https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/individuals-leaving-entering-canada-non-residents/electing-under-section-216/when-file.html|2026-11-14|
|R12: Read for ITA217(1)-(6), all operative Canadian-benefits/election/base/credit provisions|https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-217.html|2026-11-14|
|R13: Read for CRA217when-file full operative page, filing/payment/otherincome/weekend/late branches|https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/individuals-leaving-entering-canada-non-residents/electing-under-section-217/when-file.html|2026-11-14|
|R15: Read for ITA220(3),(4.5)-(4.54), complete election/security/formula/deemed-security/limits/replacement/extension provisions|https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-220.html|2026-11-14|
|R16: Read for CRA completing-newcomer return, identity/spouse/property/unwind/income and credit/province operative portions|https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/individuals-leaving-entering-canada-non-residents/newcomers-canada-immigrants/completing-return-newcomers.html|2026-11-14|
|R17: Read for CRA newcomers overview, prearrival-income/benefit-application/SOI/currentbenefitnames and filing portions; unrelated annual benefit quantum not used|https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/individuals-leaving-entering-canada-non-residents/newcomers-canada-immigrants.html|2026-11-14|
|R18: Read for ITA2(1)-(3), full operative residence/nonresident taxable-income rule|https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-2.html|2026-11-14|
|R32: Read for ITA150(1)(b)-(d),(1.1)(b), ordinary individual/death/business/spouse filing dates and individual filing triggers; neighboring trust provisions not used|https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-150.html|2026-11-14|
|R33: Read for ITA207.03 full operative nonresident-contribution tax and cessation rules|https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-207.03.html|2026-11-14|
|R34: Read for Finance current consolidated Canadian Convention, actualIV1/2, X2/4/7a, XVIII1/2/3/5; selectedneighborparagraphs read, no wholeforeignlaw audit|https://www.canada.ca/en/department-finance/programs/tax-policy/tax-treaties/country/united-states-america-convention-consolidated-1980-1983-1984-1995-1997-2007.html|2026-11-14|
|R35: Read for CRA216(1)late policy, complete operative eligibility/exclusions/extraordinary216(4)/interest/normal timing text|https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/competent-authority-agreements-notices/subsection-216-1-late-filing-policy.html|2026-11-14|
|R36: Read for T4144Rev25, operative scope/216decision/allproperties/NR6/deadlines/payment/actualspecified deduction sections/partyearincome andpaymentmethod postmark-receipt rules/paper mailing table; not whole publication read|https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4144/income-tax-guide-electing-under-section-216.html|2026-11-14|
|R37: Read for Actual T1159 catalogue, purpose/current25fillableandprintlinks and historical-year labels only|https://www.canada.ca/en/revenue-agency/services/forms-publications/forms/t1159.html|2026-11-14|
|R38: Read for ActualT1243E22PDF,bothpages allinstructions andpropertytable|https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t1243/t1243-22e.pdf|2026-11-14|
|R39: Read for ActualT1161E22PDF,wholepage instructions/exclusions/fields/deadline/penalty, renderedandvisuallyread|https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t1161/t1161-22e.pdf|2026-11-14|
|R40: Read for ActualT1244E22PDF,bothpages instructions/lines1-14/68900,68910,68920/property/election/signature/CRAarea, renderedandvisuallyread|https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t1244/t1244-22e.pdf|2026-11-14|
|R41: Read for ActualT2061AE05PDF,wholeform purpose/election/property/certification/attachments|https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t2061a/t2061a-05e.pdf|2026-11-14|
|R42: Read for ActualNR7-RE18PDF,bothpages alloperative applicant/payment/currency/treaty/ownership/certification/claim-unit/time-limit instructions|https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/nr7-r/nr7-r-18e.pdf|2026-11-14|
|R43: Read for ActualNR6E23PDF,bothpages identification/property/undertakings/agent/signatures/allinstructions|https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/nr6/nr6-23e.pdf|2026-11-14|
|R44: Read for ActualNR5E23PDF,sections1-8including217versustreaty-onlybranch/worldincomechanges/creditdependants/certification|https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/nr5/nr5-23e.pdf|2026-11-14|
|R45: Read for ActualNR73E24PDF,identification/address/leaving/usualresidence/relationships/employment/treatystatement/ties/intention/visits/foreign-ties/certification headings and relevantfields; not all instructions transcribed|https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/nr73/nr73-24e.pdf|2026-11-14|
|R46: Read for ActualNR74E24PDF,identification/address/arrival/usualresidence/priorresidence/treatystatement/ties/purpose/foreign-ties/certification headings and relevantfields; not all instructions transcribed|https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/nr74/nr74-24e.pdf|2026-11-14|
|R47: Read for CRA TFSA nonresidency page, all operative holder/room/contribution/withdrawal and designated-beneficiary distinctions read; historical examples not used for current annual limits|https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/tax-free-savings-account/non-resident.html|2026-11-14|
|R48: Read for ITA162(7)whole ordinary information-return penalty; neighboring7.01read only to distinguish prescribedmulti-return regime|https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-162.html|2026-11-14|
|R50: Read for CRA public-holidays page, generic payment/weekend/provincialqualification and actual2026list only; no2029listpublished here|https://www.canada.ca/en/revenue-agency/services/tax/public-holidays.html|2026-11-14|
|R51: Read for Actual CRA important-dates landing page,2025return/payment and qualifying selfemployed bridge only|https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/important-dates-individuals.html|2026-11-14|
|R52: Read for Actual2025T1159E25PDF,bothpages fullidentity/income/deduction/tax/refund/certifier/preparerfields; year-specificratetable read, not reused as2026|https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t1159/t1159-25e.pdf|2026-11-14|
|R54: Read for ActualT4145Rev25, all operative election/eligibility/exclusions/partyear/decision/NR5/deadlines/return/SchedulesA-B-C/credit/adjustment/tax portions through refund; unrelatedservicecomplaints notclaimed|https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4145/t4145-electing-under-section-217-income-tax-act.html|2026-11-14|

Not yet confirmed: the actual person's residence/treaty entitlement, valuations/costs, foreign-currency T1161cash source difference, complex TCP/trust/employee-benefit classification, special death/extension/security decisions, actual accepted annual filing channel, final2026annual forms and actual later recognised-holiday calendar require the stated case evidence. No foreign domestic tax, real-client computation, portal transmission, CRA acceptance, payment or professional approval is claimed. The guessed nested due-date URL returned404; the actual CRA important-dates link above was then followed and read. No access block was bypassed.

[R01]: https://www.canada.ca/en/revenue-agency/services/tax/technical-information/income-tax/income-tax-folios-index/series-5-international-residency/folio-1-residency/income-tax-folio-s5-f1-c1-determining-individual-s-residence-status.html
[R02]: https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-114.html
[R03]: https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/individuals-leaving-entering-canada-non-residents/leaving-canada-emigrants.html
[R04]: https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-250.html
[R05]: https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-128.1.html
[R06]: https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/individuals-leaving-entering-canada-non-residents/dispositions-property.html
[R07]: https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-212.html
[R08]: https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4058/non-residents-income-tax.html
[R09]: https://laws-lois.justice.gc.ca/eng/acts/C-10.7/FullText.html
[R10]: https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-216.html
[R11]: https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/individuals-leaving-entering-canada-non-residents/electing-under-section-216/when-file.html
[R12]: https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-217.html
[R13]: https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/individuals-leaving-entering-canada-non-residents/electing-under-section-217/when-file.html
[R15]: https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-220.html
[R16]: https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/individuals-leaving-entering-canada-non-residents/newcomers-canada-immigrants/completing-return-newcomers.html
[R17]: https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/individuals-leaving-entering-canada-non-residents/newcomers-canada-immigrants.html
[R18]: https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-2.html
[R32]: https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-150.html
[R33]: https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-207.03.html
[R34]: https://www.canada.ca/en/department-finance/programs/tax-policy/tax-treaties/country/united-states-america-convention-consolidated-1980-1983-1984-1995-1997-2007.html
[R35]: https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/competent-authority-agreements-notices/subsection-216-1-late-filing-policy.html
[R36]: https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4144/income-tax-guide-electing-under-section-216.html
[R37]: https://www.canada.ca/en/revenue-agency/services/forms-publications/forms/t1159.html
[R38]: https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t1243/t1243-22e.pdf
[R39]: https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t1161/t1161-22e.pdf
[R40]: https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t1244/t1244-22e.pdf
[R41]: https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t2061a/t2061a-05e.pdf
[R42]: https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/nr7-r/nr7-r-18e.pdf
[R43]: https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/nr6/nr6-23e.pdf
[R44]: https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/nr5/nr5-23e.pdf
[R45]: https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/nr73/nr73-24e.pdf
[R46]: https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/nr74/nr74-24e.pdf
[R47]: https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/tax-free-savings-account/non-resident.html
[R48]: https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-162.html
[R50]: https://www.canada.ca/en/revenue-agency/services/tax/public-holidays.html
[R51]: https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/important-dates-individuals.html
[R52]: https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t1159/t1159-25e.pdf
[R54]: https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4145/t4145-electing-under-section-217-income-tax-act.html
