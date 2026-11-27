---
name: ca-tax-residency
description: Determine Canadian individual tax residence from actual residential ties, sojourning days and the applicable treaty. Prepare arrival and departure working papers, T1243 deemed gains, T1161 property reporting, T1244 payment deferral, T2061A elections, returning-resident adjustments and Canadian non-resident withholding or section 216/217 handoffs. Use for moving into or out of Canada, dual residence, the 183-day rule, NR73 and NR74. Distinguish an opinion, an election, accountant approval and an actual filing receipt.
version: 1.2
jurisdiction: CA
tax_year: 2026
last_updated: 2026-11-27
depends_on:
  - income-tax-workflow-base
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: cross-border
type: situation-rules
---

# Canada individual tax residence, arrival, departure and non-resident income

## Scope

Determine an individual's Canadian federal residence and dates, then prepare arrival, departure and non-resident working papers for the actual year. Cover factual and deemed residence, treaty override, part-year income, departure property, T1243/T1161/T1244/T2061A, returning-resident adjustments, withholding, sections 216/217 and NR73/NR74. Foreign domestic law, Quebec calculations, trusts, corporations and section 116 sales require the specific handoffs below.

**Answer first:** examine ordinary life and residential ties; if not factually resident, examine statutory deemed residence; then apply the actual treaty even if domestic residence was established. Neither days abroad nor a filed NR73 decides cessation. A factual resident can owe tax on worldwide income below the sojourning threshold. A treaty can change either factual or deemed residence. [R01][R04]

Keep five outcomes distinct: full-year factual resident, part-year factual resident, statutory deemed resident, non-resident, and treaty-deemed non-resident. Worldwide income belongs to the resident period; applicable Canadian-source Part I income and listed Part XIII payments remain relevant outside it. A full-year sojourner result is not automatically the treatment of a permanent factual arrival or departure. [R01][R02][R18]

This is a 2026 method with a separately labelled 2025 filing bridge. Older form revision dates do not change the income year. Do not use a 2025 tax table for 2026 or claim that final 2026 software, forms or a transmission channel has been confirmed.

## Ask the client first

Read the record before asking. Collect:

- Identity, actual years, entry/departure dates, earlier residence/returns, travel evidence, purposes and sleeping/off-duty locations. Record any Forces, government, development-program or dependent-family circumstances.
- Homes and availability/leases/tenants/market terms; spouse, dependants and any prior relationship breakdown; possessions, jobs/businesses, investments/banks/cards, health coverage, licences/registrations, memberships, immigration/work status, passport, address/telephone/subscriptions, expected return/job and foreign ties.
- Actual treaty and amended residence article; liability-to-tax evidence, certificates/returns/opinions, homes, personal/economic relations, habitual abode, citizenship and disputes. Flag continuous dual residence since 24 February 1998 for historical review.
- Worldwide legal/beneficial property inventory, acquisition/inheritance dates, CAD adjusted costs and FX, move-date FMV evidence, Canadian business/PE/property, plans/options/trust/insurance rights, resident months in the preceding 120 months, and earlier departure elections/security/continuous ownership.
- All Canadian payments, dates, payer/beneficial owner, character/treaty entitlement, NR4s, tax withheld and remitted dates/currency; all rental properties/expenses/CCA/agent/NR6; pensions/world income/credits/NR5 and its actual basis.
- Actual form year, correspondence/demands/opinions, prior receipts, signature/representative authority and payment/security evidence. Keep each filing, election, information return and payment deadline separate.

## The method, step by step

### 1. Factual residence and ties

Section 250(3) includes ordinary residence. Weigh the settled routine of life and every relevant fact: ties, duration, object, intention and continuity. Canadian citizenship, a visa, an account or an intention alone is insufficient. Foreign residence does not itself sever Canadian residence. [R01] (¶1.5–1.9, 1.16–1.21)[R04]

An available Canadian dwelling, spouse/common-law partner and dependants are normally significant. An arm's-length letting requires all circumstances, including tenant relationship, market conditions and purpose; it is not a safe harbour. A spouse already separated because of relationship breakdown is treated differently. Weigh secondary ties collectively: furniture/clothing/vehicles; social/religious/recreational ties; jobs/business/banks/plans/cards/securities; landed status/work permits; provincial health coverage; licence/registration; seasonal/leased dwelling; passport; union/professional membership. Address, post-box, safe-deposit, stationery/business-card, telephone and subscription ties have limited individual weight. [R01] (¶1.10–1.15)

No fixed period abroad ends residence. An anticipated Canadian job/return can increase the weight of retained ties; occasional visits after severance ordinarily differ from regular visits plus ties. Departure-tax compliance and payer notifications evidence intention rather than creating non-residence. For arrivals apply ties in reverse: landed status plus provincial health coverage usually matters, subject to exceptional facts. A future retirement home let out, including the Folio's limited never-resident/sibling example, is not automatically a current significant tie. [R01] (¶1.16–1.28)

### 2. Deemed residence, day count and province

Only after ruling out factual residence, section 250(1)(a) deems full-year residence for **183 or more actual sojourning days** in a calendar year, subject to treaty. Part of a sojourning day counts; classify each stay first. Same-day commuting to work and returning nightly to the normal foreign home is not sojourning; holidays or off-duty stays in Canada may be. Keep one row per distinct date with purpose, entry/exit, off-duty location and reason for counting. [R04][R01] (¶1.30–1.33)

**Other statutory categories remain in scope but a days-only conclusion is unusable for them:** Forces members; specified public officers/servants; prescribed overseas development services; overseas Forces school staff; qualifying dependent children; treaty-exempt family members; and cessation under 250(2). Do not apply these without their exact prior-residence, allowance, programme, return-basis, dependency/income and exemption conditions. Check this point with one of our partner accountants. [R04] (1)–(2)

Provincial residence normally follows significant ties at 31 December, using the strongest ties if more than one province. In the departure year use the province/territory of residence on leaving. Full-year deemed residents normally pay federal surtax instead of provincial tax and do not obtain provincial credits or direct tax-based benefits. The Folio's possible Quebec deemed-residence/surtax relief requires a separate Quebec handoff. [R01] (¶1.2–1.4, 1.30–1.31)[R03]

### 3. Treaty entry and tie-breakers

Obtain the actual treaty's residence entry test. CRA's liable-to-tax interpretation concerns comprehensive tax liability, generally worldwide, rather than source-only taxation; tax actually paid may be nil. The claimant must establish the entitlement; abusive arrangements are not automatically accepted. Under 250(5), a person otherwise Canadian resident is deemed non-resident at the relevant time only if treaty-resident in the other country **and not Canada**. Departure and withholding consequences can begin then. Historical continuous dual residence since 24 February 1998 is a specific grandfathering question, not a general opt-out; hold its application for partner review. [R01] (¶1.37–1.45)[R04] (5)

**Canada-US example, Canadian-side only:** Article IV(1) governs entry, including its stated substantial-presence/permanent-home/habitual-abode and closer-relations condition in the specified US citizen/green-card case. A green card alone does not determine the Canadian outcome. For an individual actually resident in both states under IV(1), IV(2) orders: permanent home in one state; if in **both or neither**, closer personal/economic relations; if indeterminate, habitual abode; if both/neither, citizenship; if both/neither citizenship, mutual agreement. Do not invent an agreement or transplant this treaty's “neither home” branch into another treaty. [R34] (IV(1)–(2))

A permanent home can be a continuously available rented room. Its permanence matters more than size or ownership. Assess family/social ties, occupations, political/cultural activities, business/property management and all circumstances when locating the centre of vital interests. Unresolved treaty residence, later tie-breakers or a foreign-authority dispute: hold the final conclusion. Check this point with one of our partner accountants. [R01] (¶1.46–1.57)

### 4. Dates, part-year income and filing triggers

Departure is factual: normally the date ties are severed, usually the latest of leaving, family leaving and residence abroad. Preserve the return-to-former-country exception where family temporarily stays to sell the home or finish school. Apply any treaty-effective date separately. Arrival generally begins on entry when ties are established; a visitor without ties needs the deemed/treaty analysis. [R01] (¶1.22–1.28)

Section 114 separates resident-period worldwide income from specified 115 Canadian-source income/losses during non-residence and restricts deductions. Do not include all foreign pre-arrival/post-departure income in taxable income. Credit eligibility has period/income conditions; the current newcomer instructions use a 90% net-world-income test for relevant non-resident-period credits, subject to the full-year ceiling. A detailed credit calculation needs the year's return method. [R02][R16][R56]

Prepare the actual return's residence/date and identity/spouse fields with both whole-year and relevant-period world-income evidence. Filing can be required for tax payable, resident-period capital dispositions/gains, relevant full-year non-resident TCP dispositions/gains, or a positive HBP/LLP balance; also track CRA demands. Even if no T1 is required, notify CRA of departure and assess separate information/election obligations. HBP/LLP departure treatment itself is held for its specific method. [R03][R16][R32] (1), (1.1)

### 5. Departure inventory, T1243 and T2061A

Under 128.1(4)(b)–(c), property within the rule is deemed disposed of at FMV and reacquired, despite no sale. For capital property calculate gross gain/loss from CAD FMV less substantiated adjusted cost; apply the actual year's inclusion/loss rules separately. Record ownership/share, description, Canadian/foreign location, acquisition date, basis/FX, FMV/evidence, classification, exception/election and destination for **every** asset. [R05][R38]

| Departure exception | Conditions | Official URL |
|---|---|---|
| Canadian real/resource/timber property | 128.1(4)(b)(i); optional (d) election considered separately | https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-128.1.html |
| Canadian PE business property | Capital property used in, Class 14.1 in respect of, and inventory of the business through a Canadian PE | https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-128.1.html |
| Excluded right or interest | Actual 128.1(10) definition; not every investment called retirement savings | https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-128.1.html |
| Short resident | Non-trust; no more than 60 resident months in the preceding 120 months; last-arrival-owned property **or later inheritance/bequest**, not ordinary later purchases | https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-128.1.html |

Qualifying RRSP/RRIF/RESP/RDSP/TFSA/FHSA rights are within the definition. Preserve the other original categories as **classification holds**, not assumed exemptions: amended/revoked plans; PRPP and DPSP, employee profit-sharing/benefit/life-and-health and remuneration arrangements; pensions/RCA/foreign retirement/SUB plans; Canadian-service benefit rights; employee options/retiring allowances; employee/amateur-athlete/cemetery/funeral trusts; annuities; CPP/OAS/foreign social-security and specified 56 benefits; NISA Fund No. 2; never-purchased Canadian personal-trust interests; non-resident testamentary estates and their 36-month condition; life insurance/segregated funds. Check the actual contract and each statutory condition. Check this point with one of our partner accountants. [R05] (10)

**T2061A:** 128.1(4)(d), not (b)(v), permits a non-trust individual's election for (b)(i)/(ii) property, with the income/loss limitations in (d)(ii)/(iii). Use identity/current and former addresses/SIN/cessation date, property ACB/FMV and genuine certification; attach the election and applicable Schedule 3/supporting forms to the cessation return. The 2005 revision's eligible-capital wording does not replace current Class 14.1 law. [R05][R41]

**T1243 E(22):** identity/SIN/address/date; property/share description, C/F, acquisition year, FMV, ACB and gross gain/loss. Supply portfolio detail and attach the form/Schedule 3 as applicable. Prior real sales and principal-residence reporting remain separate from an exit exclusion. [R38]

### 6. Separate T1161 reporting

128.1(9) requires the list where total **reportable-property FMV exceeds CAD 25,000** at cessation, by the filing-due date even without a T1. Exactly 25,000 does not exceed it. List all reportable property, Canadian and foreign, not only the excess and not only departure-taxable assets. It is not T1135's foreign-cost test. [R05][R39]

Reporting exclusions in 128.1(10) differ: Canadian legal tender/deposits of that money; excluded rights read **without (c), (j), (l)** (so options, specified Canadian personal trusts and Canadian life insurance require separate analysis); qualifying short-resident arrival/inherited property only when **not TCP**; each personal-use item worth **less than 10,000**, not exactly 10,000. [R05]

**Foreign-cash hold:** CRA/T1161 says “cash (including bank deposits)” while the law specifies Canadian legal tender. Keep currency and the conservative statutory reconciliation; no foreign-cash-driven non-filing conclusion is usable until the administrative/statutory difference is resolved. Check this point with one of our partner accountants. [R05][R39]

The E(22) form records identity/SIN/address/date, property/share description, C/F and FMV with extra sheets. Under ordinary 162(7), an applicable late failure attracts the greater of 100 and 25 per day, capped at 100 days/2,500. On-time filing creates no such minimum penalty; other penalties/relief require separate review. [R39][R48]

### 7. T1244 election, security and later monitoring

Make the deferral election by **30 April after emigration**, even if the T1's filing date is later; for 2026, 30 April 2027. It does not omit the gain/return or cover the excluded employee-benefit-plan right. Current guidance/form requires security when federal deemed-disposition tax **exceeds 16,500**, or **13,777.50 for former Quebec residents**, with possible provincial/territorial security. Exactly the amount is not above it; the form is still required. Contact CRA before the deadline for acceptable arrangements. [R06][R15][R40]

Under 220(4.5)–(4.54), interest/penalty protection depends on accepted/deemed security and its statutory amount/period; the deemed-security measure references tax on 50,000 trust taxable income and is not a universal fixed collateral deduction. Written inadequacy notification has a 90-day replacement provision; extensions and negotiated security are discretionary. Hold any actual adequacy, acceptance or extension conclusion. Check this point with one of our partner accountants. [R15]

T1244 E(22) lines 1–7 reconcile taxable income, departure income/deductions (68900) and non-negative adjusted income; lines 8–10 compare federal taxes, allowing Quebec abatement; lines 11–13 compare provincial taxes and are not completed by former Quebec residents; line 14 totals the differences. List selected property on page 2 if only some assets are covered; choose federal 68910/provincial 68920 up to the corresponding calculated maximum; obtain real signature/date and leave CRA's security area to CRA. The example uses supplied tax outputs rather than a flat gain-tax rate. [R40]

Record the actual timely election separately if the return follows later. Monitor actual sales and re-entry: send original T1243 property description, share count and disposition date to Non-Resident T1 Adjustments, Winnipeg Tax Centre. CRA specifies payment by 30 April after the disposition year. Re-entry may crystallise deferred tax, subject to eligible unwind relief. [R06]

### 8. Arrival and returning-resident relief

128.1(1)(b)–(c) generally gives an FMV acquisition cost on arrival, which can step down. Individual exceptions include TCP, Canadian-business inventory/Class 14.1 and excluded rights **other than definition (k)**. Keep valuation/FX evidence; do not copy the exit exceptions unchanged. [R05][R16]

For a return after a cessation **after 1 October 1996**, 128.1(6)(c) needs continuous ownership and property within the arrival disposition rule. A timely written election reduces **both** old departure proceeds and new acquisition cost by the least of old departure gain, return FMV and the specified amount. File by the return-year filing-due date with property/FMV details and reconcile both years. Relief/security release awaits actual assessments/confirmation. [R05][R06]

Continuously TCP relief under (6)(a), the (6)(b)/40(3.7) loss adjustment, the pre-5 March 2010 transition in (6.1), returning trust beneficiaries and post-emigration losses are **non-usable specialist holds**. Preserve continuous-ownership/TCP status and old proceeds/basis for review. Check this point with one of our partner accountants. [R05]

Pre-arrival foreign income can still be requested for benefits/credits: CRA asks for both spouses' income for up to two prior years, including nil amounts where required; that request does not itself impose Canadian income tax on it. Benefit eligibility, current benefit names (CCB and Canada Groceries and Essentials Benefit), departure cessation and HBP/LLP consequences need their own benefit/plan analysis. Do not promise eligibility or amounts. [R02][R03][R17]

### 9. Canadian non-resident payments and treaty examples

Distinguish a Part I return for applicable Canadian employment/business/TCP gains  from listed Part XIII payments. Section 212's ordinary **25% gross** rule is subject to each payment's statutory exclusions and actual treaty. Record dividends, rent/timber, pension/OAS/CPP-QPP, retiring allowances, RRSP/RRIF/PRPP/FHSA, annuities, royalties and estate/trust receipts by their actual provision. Arm's-length interest is generally exempt but participating-debt interest can remain caught; non-arm's-length interest has fully-exempt-interest exceptions. Notify payers and document treaty entitlement. Correct final withholding is not automatically a T1 refund. Scholarship/research-grant liability or exemptions require their specific analysis: hold the conclusion. Check this point with one of our partner accountants. [R18][R02][R07]

For qualifying US-resident beneficial owners, Canada-US X(2) ordinarily caps portfolio dividends at **15%**, or **5%** for a company with at least **10% voting ownership** (including its transparent-entity rule). X(7)(a)'s distinct branch for a Canadian non-resident-owned investment corporation paying its qualifying US-resident company beneficial owner with at least 10% voting ownership has a **10%** cap. Verify residence, beneficial entitlement and limitation-on-benefits qualification; an effectively connected holding is outside X(2). XVIII(2)(a)'s **15%** cap is for periodic pensions, not all lump sums; XVIII(5) separately governs social-security benefits. No foreign domestic tax is calculated. [R34]

**NR7-R:** normally apply within two years after the end of the year the payer **remitted** tax; check any longer treaty period. Capture income/payment/tax/remittance currency, identifiers, actual article/residence/beneficial entitlement, payer/custodian chain and slips/ownership evidence. Security payments require payment-date/type/ownership/CUSIP/payer-account claim units; other payments normally use year/type/owner/payer-account units. Genuine authorized certification and specified payer certificates/affidavits are needed. Preserve actual submission/receipt and outcome; a completed form is not a granted refund. [R42][R57]

**TFSA:** an ordinary holder can retain it and withdraw free of Canadian tax. No new room accrues in a wholly non-resident year; part-year annual room does not permit tax-free contributions after cessation. 207.03 imposes **1% per applicable month** on a non-resident contribution, except qualifying transfers/exempt contributions, until the statutory designated-distribution or re-residence endpoint. A separately established excess can attract additional tax. Death/designated-beneficiary growth, foreign tax and final room/excess calculations remain separate. Check this point with one of our partner accountants. [R33][R47][R55]

### 10. Section 216 rent, NR6 and the dated 2025 bridge

216 permits a separate net-rent/timber return in place of gross Part XIII tax for the covered income, including the actual partnership share. Include **all** Canadian rental properties; part-year residents separate resident-period rent on T1 from non-resident-period rent on this return. Business rental income, sale gains/section 116 and recapture need their proper separate treatment. Compare the full permitted calculation with proper withholding; income/credit deductions are restricted by 216 and the applicable law, not those of an unrestricted resident. [R10][R36]

NR6 requires the real non-resident/authorized representative and Canadian-resident agent's undertaking, year/first-rent month, every property/share and estimated gross rent/itemised expenses/net amount. Exclude CCA/depreciation/amortisation from withholding expenses. Send on/before 1 January or before first rent is due. **Continue gross withholding until written approval**; then withhold 25% of actual available net rent and remit ordinarily by the following month's 15th. File the required 216 return even for loss/nil/refund nil; keep NR4 and actual approval/return controls separately. [R43][R36]

216 ordinarily allows two years after year-end; an undertaking makes it six months; the relevant CCA-recapture disposal case can require 30 April. A balance is generally due 30 April after the income year. CRA's voluntary 216(1) late policy gives one opportunity only to qualifying applicants: excluded if already informed of responsibilities, CRA has acted, or NR6 was approved. It promises no penalties under that policy but interest may remain. Extraordinary 216(4)/220(3) extensions are discretionary. Hold a late-policy outcome until decided. Check this point with one of our partner accountants. [R10][R11][R35][R36]

**2025 execution bridge only:** T1159 E(25) identity/SIN-ITN-TTN/address/birth/death/language; gross 12599/net 12600, income 15000; only actually allowable deductions 20800/20805/22000/23200, total 23300, taxable 26000 floored at zero; annual tax/surtax to 43500; NR4 withholding 43700; recapture remittance 47600 with T2064/T2068 copy; credits 48200; refund 48400/balance 48500; genuine certification and preparer-fee/name/phone fields. Follow T4144's deduction conditions, no double claims and special administrative RRSP-limit treatment. This bridge does not authorize a deduction from the existence of a box. Hold any unverified detailed deduction eligibility. [R36][R52]

For the 2025 paper route, T4144 sends Denmark/France/Netherlands/UK/US residents to Winnipeg Tax Centre, PO Box 14001, Station Main, Winnipeg MB R3C 3M3; other countries to Sudbury Tax Centre, 1050 Notre Dame Ave, Sudbury ON P3A 5C2. Recheck for a later actual submission. Keep rental statements/CCA schedule, signed packet, valid channel, actual receipt/assessment and separate payment evidence. [R36]

### 11. Section 217, NR5 and the dated 2025 bridge

217's “Canadian benefits” are defined through 212(1)(h), (j)–(m), (q). Retain pension/OAS/CPP-QPP/RRSP/PRPP/RRIF/death/EI/retiring/SUB/DPSP/RCA/government-assistance/Auto Pact receipts for eligibility review, not a blanket election for every payment. OASRI/T1136 may be separate. Use the greater-of income bases, statutory credit limitations and special adjustment; world income matters and full resident credits are not automatic. For an emigrant distinguish eligible post-departure payments from resident-period world income. [R12][R54]

Ordinary filing is within six months/30 June, payment 30 April; other employment/business/partnership/TCP income may alter the filing date. CRA states ordinary late 217 elections cannot be accepted; correct withholding remains final, or a shortfall is assessed. The 216 late policy does not apply. Weekend/holiday return and payment rules differ; record the relevant receipt/postmark rule. [R12][R13]

**2025 execution bridge only:** write “Section 217” on page 1; complete the applicable identity/income/withholding fields. Full-year non-residents use Schedule C Part 1 for tax actually required, Schedule A world income, greater-of taxable/net-world-income-after-adjustments tax base, Schedule B credit limits and Schedule C Part 2 adjustment as applicable. Attach A/B/C and slips; withholding 43700 and tax 43500. Part-year residents use their applicable provincial method; additional provincial/Quebec work has a separate handoff. Compare 43500 with required non-resident tax at C44300 plus tax on other relevant Canadian income. CRA takes the election into account only if beneficial; excess withholding may instead support NR7-R, while underwithholding can leave a balance. No 2025 rates are carried into 2026. [R54]

**NR5:** the 217-based request goes on/before 1 October or before first payment; its actual approval may cover five tax years, with a timely 217 return for every approved year. Record approved years/rates/payers. The form's distinct listed-country treaty-exemption-only branch is not a 217 annual-return undertaking: hold actual country/payment entitlement until read for the case. Check this point with one of our partner accountants. Record identity/spouse/departure, benefits/payers/periodic or lump-sum, other Canadian/foreign income, credits/dependants and authorized certification. Changed estimated world income requires amendment within 30 days. For the pension, retiring-allowance or RRSP amounts being transferred to an RRSP/RPP as identified on NR5, use NRTA1 instead. Current form offers My Account Submit Documents, mail or fax; reduction awaits actual approval. [R44][R54]

### 12. NR73/NR74, working papers and completion

NR73 is for leaving/planning departure; NR74 for entering/brief stays. They request opinions rather than electing residence. The opinion rests on full facts and is not binding on CRA; a prospective ruling or competent-authority assistance may be appropriate. Use the actual forms' identity/address/history/purpose/employment/family/treaty/ties/visits/certification fields and current Submit Documents/My Account/Represent a Client or mail/fax instructions. Keep the signed request, receipt, questions/opinion, dates/scope and later changed facts; no request postpones a tax deadline. [R01] (¶1.53–1.57)[R45][R46]

Produce a dated residence memo/day ledger; complete property/T1243/T1161/basis/election schedules; payer/treaty/NR7-R and rental/217/NR5 papers; and an action register naming owner, source/raw/adjusted deadline, channel, authority, status and payment/security evidence. Complete the ten original controls: factual/deemed/treaty sequence; evidenced ties/dates; separated commute/sojourn days; actual treaty/liable-to-tax proof; inventory/T1243/Schedule 3/T1161; timely T1244/security; arrival basis; payer notices/refund or reduction applications; 216/217 deadlines; NR73/74 where useful. Check inherited property, cash conflict, TFSA and both unwind bases too. Prepared forms are **PREPARED FOR REVIEW**. Only a genuine case-review/authorization record and actual submission/receipt can establish the corresponding later status. AI source checking is not professional approval or filing.

## Rates, bands and thresholds

Amounts are CAD; the conditions in the method and cases remain part of each rule.

| Item | Rule and conditions | Official URL |
|---|---|---|
| Sojourning | At least 183 actual sojourning days in a calendar year; only after no factual residence and subject to treaty | https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-250.html |
| Short residence | Non-trust, no more than 60 resident months of the preceding 120; arrival-owned or later inherited property; T1161 also requires non-TCP | https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-128.1.html |
| T1161 | Reportable FMV strictly over 25,000; personal-use exclusion strictly below 10,000 per item | https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-128.1.html |
| Ordinary late T1161 | Applicable failure only: greater of 100 or 25/day, capped at 100 days (computed maximum 2,500); on-time zero | https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-162.html |
| T1244 security | Federal tax exceeds 16,500, or 13,777.50 for former Quebec resident; possible provincial security and timely election still required | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t1244/t1244-22e.pdf |
| Part XIII | Ordinary 25% gross on specified payments, subject to actual statutory/treaty exclusions | https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-212.html |
| Canada-US dividends | Qualified beneficial owner: 15% ordinary portfolio; 5% qualifying company with at least 10% voting stock; special X(7)(a) 10% branch has its own payer/owner conditions | https://www.canada.ca/en/department-finance/programs/tax-policy/tax-treaties/country/united-states-america-convention-consolidated-1980-1983-1984-1995-1997-2007.html |
| Canada-US periodic pension | 15% cap for qualifying beneficial owner's periodic pension; social-security and lump-sum treatment separate | https://www.canada.ca/en/department-finance/programs/tax-policy/tax-treaties/country/united-states-america-convention-consolidated-1980-1983-1984-1995-1997-2007.html |
| TFSA contribution | 1% each applicable month under 207.03; exceptions/endpoints apply; separately established excess under 207.02 can add its own tax | https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-207.03.html and https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-207.02.html |

## Filing and payment

Standard individual dates below exclude death/special extensions. Section 150 allows the qualifying business/cohabiting-spouse 15 June filing date, except primarily tax-shelter expenditures. Later filing does not delay payment. [R32][R51]

| Job | 2026 year, derived from current timing rule | 2025 dated bridge | Official URL |
|---|---|---|---|
| Ordinary T1 and applicable T1243/T1161/T2061A | Derived: 30 April 2027; qualifying business/spouse 15 June 2027 | 30 April or qualifying 15 June 2026 | https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-150.html |
| Balance/T1244 | Derived: 30 April 2027 | 30 April 2026 | https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/individuals-leaving-entering-canada-non-residents/dispositions-property.html and https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/important-dates-individuals.html |
| Ordinary 217 filing | Derived: 30 June 2027, check other-income exception | 30 June 2026 | https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/individuals-leaving-entering-canada-non-residents/electing-under-section-217/when-file.html |
| Ordinary 216 without undertaking | Derived raw two-year endpoint 31 December 2028 is Sunday; final adjusted date held pending applicable holiday/receipt check | 31 December 2027 | https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-216.html and https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/individuals-leaving-entering-canada-non-residents/electing-under-section-216/when-file.html |
| Approved NR6/216 filing | Derived: 30 June 2027 even if nil/loss; relevant recapture case 30 April 2027 | 30 June or recapture 30 April 2026 | https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/individuals-leaving-entering-canada-non-residents/electing-under-section-216/when-file.html |
| 216 balance | Derived: generally 30 April 2027 | 30 April 2026 | https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4144/income-tax-guide-electing-under-section-216.html |
| NR7-R for remittances in the named year | Raw two-year endpoint 31 December 2028; final extension/treaty date held | 31 December 2027 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/nr7-r/nr7-r-18e.pdf |
| Returning-resident election | Derived: return-year filing-due date in 2027 | Return-year filing-due date in 2026 | https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-128.1.html |

For 216/217 returns CRA accepts the next-business-day receipt/postmark after a recognised holiday/weekend. T4144 payment timing distinguishes bank credit/stamped voucher, PAD negotiable date and mailed-payment postmark; 217 specifies receipt on the first business day. Do not assume a payment instruction is a return or NR7-R extension. The available CRA holiday list is 2026, not a confirmed 2029 calendar. For any unresolved adjusted deadline: Check this point with one of our partner accountants. [R11][R13][R36][R50]

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

The original same-day commuter who works in Canada and returns to a foreign home each night is not sojourning on those workdays. For a separate day-count control, a documented set has 170 whole sojourning dates and 13 distinct part-day sojourns, no duplicates:183, meeting the domestic threshold. Another set has 190 same-day commuting workdays and 12 holiday-sojourning dates:12 counted, below 183. Neither count decides factual residence or the treaty. [R01] (¶1.33)

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

Preserve the original 1,000 Canadian listed-company dividend to a qualifying US-resident individual beneficial owner: statutory default 250, treaty cap 150, excess 100 if 250 was remitted. NR7-R needs actual treaty qualification, claim-unit evidence and the **remittance-year** time limit. It is not automatically every person's 100 refund. [R07][R34][R42]

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

A non-resident contributes 2,000 while non-resident. Assume no qualifying transfer/exempt contribution, no designated distribution or residence resumption before the relevant 3 month-ends, and 3 taxable monthly periods under 207.03. Non-resident contribution tax is 20 a month,60 total. If a separately established 2,000 excess also remains for 3 taxable periods, an additional illustrative 60 could arise under that separate excess regime; this method does not adjudicate excess-room records. An ordinary holder's 1,000 TFSA withdrawal is not 250 Part XIII tax: Canadian tax on that ordinary withdrawal is 0 under the TFSA guidance. Foreign tax and death-beneficiary growth are different questions. [R33][R47][R55]

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

Continue supported working papers while holding the unresolved conclusion. For each hold below: **Check this point with one of our partner accountants.**

| Original referral purpose retained | Non-usable conclusion and handoff |
|---|---|
| R1 disputed ties or material bill | Final residence/date until evidence is resolved; retain opposing facts and NR73/NR74/ruling options |
| R2 treaty dispute/later tests | Treaty winner, foreign disagreement or competent-authority outcome; retain actual article and missing facts |
| R3 separate taxpayer/system | Quebec/provincial surtax/security, trusts/corporations, actual TCP/section 116 sales; hand over original residence, inventory, basis and form history |
| R4 complex property/security | Private-company valuation, PE/Class 14.1, employee options/benefits, foreign trusts/insurance, post-departure loss, continuously-TCP/returning-beneficiary elections, negotiated security or extensions; retain deadline and precise unresolved classification/acceptance |
| R5 unread foreign/treaty claim | Foreign domestic tax/filing and any other treaty rate without the actual operative article and entitlement evidence |
| R6 days-only cessation | Final non-residence from days abroad, a surrendered licence or NR73 alone; complete the ties/day/treaty sequence |
| Specific retained holds | Foreign-cash T1161 non-filing; dependent/government deemed categories; benefit/HBP/LLP treatment; actual rental deductions/CCA/loss/short-term-rental eligibility; TFSA death/excess/room; detailed NR5 treaty-only entitlement; late-policy decisions; future annual forms/channels and adjusted year-end deadlines |

## Sources

Read on **27 November 2026**: the bounded operative portions listed below. HTML and PDF text were read directly in memory; PDF field labels are text checks, not a fresh visual-layout audit. Prior 14 November evidence links were unavailable with the external volume. No successful fetch alone is counted as a completed read. Annual 2025 material is retained only for its labelled bridge; no 2026 tax-rate table or accepted filing channel is inferred from it.

| Source | Portion actually read | Official URL | Date read |
|---|---|---|---|
| R01 | Read for: Folio ¶1.1–1.57: residence, ties, dates, days, province, treaty, opinions/rulings | https://www.canada.ca/en/revenue-agency/services/tax/technical-information/income-tax/income-tax-folios-index/series-5-international-residency/folio-1-residency/income-tax-folio-s5-f1-c1-determining-individual-s-residence-status.html | 2026-11-27 |
| R02 | Read for: ITA 114(a)–(c), part-year income and deductions | https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-114.html | 2026-11-27 |
| R03 | Read for: Emigrant package, identity/date, split income and notifications | https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/individuals-leaving-entering-canada-non-residents/leaving-canada-emigrants.html | 2026-11-27 |
| R04 | Read for: ITA 250(1)–(3), (5), individual categories and treaty override | https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-250.html | 2026-11-27 |
| R05 | Read for: ITA 128.1(1), (4), (6)–(10), individual move/property/reporting provisions; rare branches held | https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-128.1.html | 2026-11-27 |
| R06 | Read for: Departure dispositions, forms, security, unwinding and subsequent-disposal guidance | https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/individuals-leaving-entering-canada-non-residents/dispositions-property.html | 2026-11-27 |
| R07 | Read for: ITA 212(1) opening/interest and payment categories; individual applicability still needs the precise provision | https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-212.html | 2026-11-27 |
| R10 | Read for: ITA 216(1)–(6), (8), election, undertaking, base and restrictions | https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-216.html | 2026-11-27 |
| R11 | Read for: 216 filing/NR6/recapture, weekend and late-policy link | https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/individuals-leaving-entering-canada-non-residents/electing-under-section-216/when-file.html | 2026-11-27 |
| R12 | Read for: ITA 217(1)–(6), benefits, election, bases, credit limits and adjustment | https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-217.html | 2026-11-27 |
| R13 | Read for: 217 filing/payment, other-income exception, weekend and ordinary late outcome | https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/individuals-leaving-entering-canada-non-residents/electing-under-section-217/when-file.html | 2026-11-27 |
| R15 | Read for: ITA 220(4.5)–(4.54), security/limits/replacement/extension terms | https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-220.html | 2026-11-27 |
| R16 | Read for: Newcomer return identity, property, income and period-credit conditions | https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/individuals-leaving-entering-canada-non-residents/newcomers-canada-immigrants/completing-return-newcomers.html | 2026-11-27 |
| R17 | Read for: Newcomer benefit application/pre-arrival world-income information and current benefit labels; no quantum | https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/individuals-leaving-entering-canada-non-residents/newcomers-canada-immigrants.html | 2026-11-27 |
| R18 | Read for: ITA 2(1)–(3), residence and non-resident Part I framework | https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-2.html | 2026-11-27 |
| R32 | Read for: ITA 150(1)(b)–(e), (1.1)(b), individual filing dates/triggers | https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-150.html | 2026-11-27 |
| R33 | Read for: ITA 207.03, complete non-resident contribution provision | https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-207.03.html | 2026-11-27 |
| R34 | Read for: Canada-US consolidated Convention IV(1)–(2), X(1)–(4)/(7)(a), XVIII(1)–(5); Canadian-side only | https://www.canada.ca/en/department-finance/programs/tax-policy/tax-treaties/country/united-states-america-convention-consolidated-1980-1983-1984-1995-1997-2007.html | 2026-11-27 |
| R35 | Read for: 216(1) late policy, complete eligibility/exclusions and discretionary 216(4) boundary | https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/competent-authority-agreements-notices/subsection-216-1-late-filing-policy.html | 2026-11-27 |
| R36 | Read for: T4144 Rev25: scope, all properties, NR6, due dates, 2025 fields/deductions, payment method and mailing table | https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4144/income-tax-guide-electing-under-section-216.html | 2026-11-27 |
| R38 | Read for: T1243 E(22), both pages: instructions and all property fields | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t1243/t1243-22e.pdf | 2026-11-27 |
| R39 | Read for: T1161 E(22), full page: threshold, exclusions, fields, due date/penalty | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t1161/t1161-22e.pdf | 2026-11-27 |
| R40 | Read for: T1244 E(22), both pages: instructions, thresholds, lines 1–14 and election fields | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t1244/t1244-22e.pdf | 2026-11-27 |
| R41 | Read for: T2061A E(05), full election/instructions and certification, read alongside current statute | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t2061a/t2061a-05e.pdf | 2026-11-27 |
| R42 | Read for: NR7-R E(18), applicant/payment/ownership/claim-unit/certification/time-limit instructions | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/nr7-r/nr7-r-18e.pdf | 2026-11-27 |
| R43 | Read for: NR6 E(23), undertaking fields and full withholding/agent/expenses instructions | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/nr6/nr6-23e.pdf | 2026-11-27 |
| R44 | Read for: NR5 E(23), terms, treaty-only distinction, estimated income, amendment/certification/channel instructions | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/nr5/nr5-23e.pdf | 2026-11-27 |
| R45 | Read for: NR73 E(24), purpose, channel instructions and relevant identity/history/ties/certification fields; no visual layout audit | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/nr73/nr73-24e.pdf | 2026-11-27 |
| R46 | Read for: NR74 E(24), purpose, channel instructions and relevant identity/history/ties/certification fields; no visual layout audit | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/nr74/nr74-24e.pdf | 2026-11-27 |
| R47 | Read for: TFSA non-resident holder, contribution/room and beneficiary distinctions | https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/tax-free-savings-account/non-resident.html | 2026-11-27 |
| R48 | Read for: ITA 162(7), ordinary failure rule; neighbouring 7.01 distinguished | https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-162.html | 2026-11-27 |
| R50 | Read for: CRA 2026 recognised-holiday list and geographic qualification; no 2029 calendar verified | https://www.canada.ca/en/revenue-agency/services/tax/public-holidays.html | 2026-11-27 |
| R51 | Read for: Actual 2025 ordinary/business filing and payment date bridge | https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/important-dates-individuals.html | 2026-11-27 |
| R52 | Read for: T1159 E(25), both pages: fields and certification; annual rates not reused for 2026 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t1159/t1159-25e.pdf | 2026-11-27 |
| R54 | Read for: T4145 Rev25, eligibility, NR5, deadlines, 2025 A/B/C calculation and beneficial-election comparison | https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4145/t4145-electing-under-section-217-income-tax-act.html | 2026-11-27 |
| R55 | Read for: ITA 207.02, full excess-tax provision; excess itself stipulated in case 8 | https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-207.02.html | 2026-11-27 |
| R56 | Read for: ITA 118.91, full part-year credit limits, read with newcomer instructions | https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-118.91.html | 2026-11-27 |
| R57 | Read for: ITA 227(6), ordinary written refund application period and outstanding-liability offset | https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-227.html | 2026-11-27 |

Not yet confirmed: individual case facts/entitlement/values, specialist classifications and outcomes listed in the referral table, actual approval/signatures/submission/receipts, final 2026 annual rates/forms/channel, and adjusted 2028/2029 deadline endpoints. These are non-usable holds; the worked cases preserve stipulated inputs and do not certify these matters. Check this point with one of our partner accountants.

[R01]: https://www.canada.ca/en/revenue-agency/services/tax/technical-information/income-tax/income-tax-folios-index/series-5-international-residency/folio-1-residency/income-tax-folio-s5-f1-c1-determining-individual-s-residence-status.html
[R02]: https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-114.html
[R03]: https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/individuals-leaving-entering-canada-non-residents/leaving-canada-emigrants.html
[R04]: https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-250.html
[R05]: https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-128.1.html
[R06]: https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/individuals-leaving-entering-canada-non-residents/dispositions-property.html
[R07]: https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-212.html
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
[R55]: https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-207.02.html
[R56]: https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-118.91.html
[R57]: https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-227.html
