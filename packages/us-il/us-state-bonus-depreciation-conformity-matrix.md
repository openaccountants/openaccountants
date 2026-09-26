---
name: us-state-bonus-depreciation-conformity-matrix
description: Tier 2 US federal-level reference skill providing the 50-state matrix of conformity to federal §168(k) bonus depreciation and §179 expensing. Covers tax year 2025 including state-by-state add-back requirements (CA never conforms with $25k §179 cap, NY decoupled since 2003, NJ partial, PA decoupled bonus with §179 conformity, etc.), recovery mechanisms for state add-backs (typically over 5 years or via decoupled MACRS lifetime), §163(j) interest limit conformity, NOL post-TCJA conformity, and the OBBBA-era bonus depreciation status with the TCJA phase-down (60% 2024 → 0% 2027 absent extension).
jurisdiction: US
tax_year: 2026
last_updated: 2026-09-25
authored_by: OpenAccountants team
review_status: pending_review
trust_label: By OpenAccountants
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# US state conformity to federal bonus depreciation (§168(k)) and §179: 2026 matrix, with 2025 return notes

Figures are for tax year 2026 unless a line says 2025. Federal amounts come from Rev. Proc. 2025-32 and IRS Publication 946 (2025), after the One Big Beautiful Bill Act (P.L. 119-21, "OBBBA"). Each state row was checked on 25 September 2026 against that state's revenue department or legislature. A row marked **check** could not be confirmed from an official page on that date: do not rely on it until you have read the state's current instructions. A separate section covers 2025 returns. Extended 2025 federal returns are due by October 15, 2026 ([IRS extensions](https://www.irs.gov/filing/get-an-extension-to-file-your-tax-return)).

## Scope and who this is for

- **Covers:** individuals with business or rental income (Schedule C, E or F, and owners of partnerships and S corporations) who claimed federal bonus depreciation under IRC §168(k), the §168(n) allowance for qualified production property, or §179 expensing, and who file a state income tax return.
- **Does not cover:** C corporation returns (rules often differ; Florida is noted only because it has no personal income tax), franchise, gross-receipts and business-activity taxes, §163(j) interest, net operating losses and research expensing under §174A.
- **Where our state Guides go further:** Connecticut, Arkansas, Delaware, Kentucky, Maryland, New York, California and Virginia each have their own Guide (for example `ct-income-tax`, `ca-540-individual-return`). This matrix uses the same rules; use the state Guide for the full return.

## Ask the client first

- Which tax year is being prepared (2025 or 2026), and in which states does the client file (residence, and every state where the business or a pass-through has income)?
- For each asset: the date it was **acquired** (the date of any written binding contract), the date it was placed in service, its cost, its MACRS class and life, and whether it is new or used.
- Did the federal return claim §168(k) bonus depreciation, the §168(n) allowance, or §179? Was the 40% (or 60%) transition election made for the first tax year ending after January 19, 2025 ([26 U.S.C. §168(k)(10)](https://www.law.cornell.edu/uscode/text/26/168))? Was an election out of bonus made for any class?
- The fixed-asset register from prior years, with each state's separate basis and depreciation, and any add-backs still being recovered (Connecticut, Minnesota, North Carolina and Ohio spread recoveries over later years).
- For pass-through owners: the state K-1 schedules showing the entity's bonus and §179 amounts, and whether the entity already made the adjustment (some states adjust at entity level, others at owner level).
- Any disposal of an asset that had a state adjustment, since state gain or loss differs from federal.

## The method, step by step

1. **Fix the federal numbers first.** For each asset, split federal depreciation into §179, §168(k) or §168(n) allowance, and regular MACRS. Check the acquisition date: property acquired after January 19, 2025 gets 100% bonus; property acquired earlier and placed in service in 2025 gets 40% ([Pub. 946](https://www.irs.gov/publications/p946)).
2. **Find each state's row** in the matrix below. Use the table for the year being prepared; several states changed their rules for 2026 (Delaware, Oregon, Hawaii, Arizona, Minnesota).
3. **Recompute state depreciation** the way the state requires: no bonus at all (most decoupled states), a reduced bonus (Delaware 2026), or federal bonus with a percentage add-back and a fixed recovery (Connecticut, Minnesota, North Carolina, Ohio). Apply the state's own §179 limit if it has one.
4. **Enter the add-back** on the state form named in the row, in the year the federal deduction was taken.
5. **Schedule the recovery.** Either a fixed fraction in later years (Connecticut, Minnesota, North Carolina, Ohio), or the extra state depreciation each later year until the asset is fully depreciated. Keep a separate state depreciation schedule for every asset; the state basis differs from federal.
6. **On disposal,** compute state gain or loss with the state basis. Several states say so expressly (Maine, New Jersey, Illinois, Wisconsin).
7. **Nonresidents and part-year residents:** the add-back and subtractions follow the state's sourcing and apportionment rules. Record open recoveries for next year.

## Federal figures with years

### Bonus depreciation, §168(k) ([Pub. 946 (2025)](https://www.irs.gov/publications/p946); [26 U.S.C. §168](https://www.law.cornell.edu/uscode/text/26/168); [IR-2026-06, Notice 2026-11](https://www.irs.gov/newsroom/treasury-irs-issue-guidance-on-the-additional-first-year-depreciation-deduction-amended-as-part-of-the-one-big-beautiful-bill))

| Property | Bonus rate | Conditions |
| --- | --- | --- |
| Acquired after January 19, 2025 (2025 and 2026) | 100% | Permanent under OBBBA. Property is not treated as acquired after the date a written binding contract for it was entered into ([§168 note](https://www.law.cornell.edu/uscode/text/26/168)). |
| Same property, first tax year ending after January 19, 2025 | 40% by election (60% for long production period property and certain aircraft) | Election instead of 100% |
| Acquired after September 27, 2017 and before January 20, 2025, placed in service in 2025 | 40% (60% for long production period property and certain aircraft) | Pre-OBBBA phase-down ([Pub. 946](https://www.irs.gov/publications/p946)) |
| Qualified production property, §168(n) | 100% | Elective; the portion of nonresidential real property used as an integral part of a qualified production activity, original use beginning with the taxpayer, placed in service in the United States or a US possession; construction begins after January 19, 2025 and before January 1, 2029; placed in service after July 4, 2025 and before January 1, 2031 |

- **Qualified property** is generally tangible property depreciated under MACRS with a recovery period of 20 years or less, certain computer software, water utility property, and qualified film, television, live theatrical and sound recording productions ([Pub. 946](https://www.irs.gov/publications/p946)).
- **Election out:** made for a whole class of property for the year, and covers all qualified property in that class placed in service that year. It is made on a timely filed return (including extensions) and can be revoked only with IRS consent ([26 U.S.C. §168(k)(7)](https://www.law.cornell.edu/uscode/text/26/168); [Pub. 946](https://www.irs.gov/publications/p946)). Electing out avoids the state bonus add-back, at a federal cost.

### §179 expensing ([Rev. Proc. 2025-32](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf); [Pub. 946 (2025)](https://www.irs.gov/publications/p946))

| Item | 2026 | 2025 |
| --- | --- | --- |
| Maximum deduction | $2,560,000 | $2,500,000 |
| Reduced dollar for dollar once §179 property placed in service in the year costs more than | $4,090,000 | $4,000,000 |
| Sport utility vehicle cap | $32,000 | $31,300 |

- The 2025 amounts apply to property placed in service in tax years beginning after December 31, 2024 ([Rev. Proc. 2025-32 §3.02](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf)). The old $1,220,000 and $3,050,000 figures are 2024 amounts.
- §179 is also limited to taxable income from the active conduct of a trade or business (the business income limit), and applies to each taxpayer, not each business ([Pub. 946](https://www.irs.gov/publications/p946)).

## State matrix, tax year 2026

Read the row for the year you are preparing. "Follows" means no state adjustment for federal bonus depreciation. Where a state has not yet published 2026 forms, the row gives the rule in force and the 2025 form that carries it.

### States that follow federal bonus depreciation for individuals

| State | Conformity | §168(k) | §179 | OBBBA response | Source |
| --- | --- | --- | --- | --- | --- |
| Alabama | Tied to federal for depreciation | Follows 100% bonus for property placed in service on or after January 19, 2025 | Follows | ADOR analysis (October 2025): "Tied to Federal: Yes" | [ADOR OBBBA summary](https://www.revenue.alabama.gov/wp-content/uploads/2025/11/OBBBA-Executive-Summary_FinalwAppendixA_10.31.25.pdf) |
| Arizona | IRC as of January 1, 2026, retroactive to 2025 (HB 4168, Laws 2026 ch. 140) | Follows (full §168(k) allowed for taxable years after 2016) | Follows | Adds back the §168(n) allowance from 2026 | [Enacted fact sheet](https://www.azleg.gov/legtext/57leg/2R/summary/S.1861-4168ATT_ASENACTED.DOCX.htm); [A.R.S. 43-1022](https://www.azleg.gov/ars/43/01022.htm) |
| Colorado | Rolling | Follows | Follows | A 2026 bill to add back OBBBA bonus (HB26-1222) was postponed indefinitely on May 11, 2026 | [HB26-1222](https://leg.colorado.gov/bills/hb26-1222); [Book 104](https://tax.colorado.gov/sites/tax/files/documents/Book104_2025.pdf) |
| Iowa | Rolling since tax year 2020 | Fully conforms for tax years beginning on or after January 1, 2021 | Follows | Rolling conformity picks it up | [IA 4562A instructions](https://revenue.iowa.gov/media/4407/download?inline=); [LSA](https://www.legis.iowa.gov/docs/publications/FTNO/1543015.pdf) |
| Louisiana | Starts from federal AGI | Follows; plus an optional Louisiana 100% expensing deduction for qualified property, QIP and R&E for periods beginning on or after January 1, 2025 | Follows | None found | [LDR FAQ](https://revenue.louisiana.gov/tax-education-and-faqs/faqs/income-tax-reform/does-louisiana-offer-a-deduction-for-bonus-depreciation/) |
| Missouri | Starts from federal AGI | Follows; only a legacy subtraction for 30% bonus on assets bought July 1, 2002 to June 30, 2003 | Follows | None found | [MO-1040 instructions](https://dor.mo.gov/forms/MO-1040%20Instructions_2025.pdf) |
| Montana | Starts from federal taxable income | Follows: depreciation must be the same for federal and Montana | Follows | None found | [Form 2 instructions](https://revenuefiles.mt.gov/files/Forms/Montana-Individual-Income-Tax-Return-Form-2-Instructions/2025_Montana_Individual_Income_Tax_Return_Form_2_Instructions.pdf) |
| Nebraska | Rolling | Follows: no add-back for tax years beginning on or after January 1, 2006 | Follows | **Check** for any 2026 legislation on §168(n) | [NDOR](https://revenue.nebraska.gov/individuals/bonus-depreciation-and-enhanced-section-179-expense-deduction-nebraska-income-tax) |
| North Dakota | "Perpetually conforms" to federal taxable income | Follows | Follows | Rolling | [2025 booklet](https://www.tax.nd.gov/sites/www/files/documents/forms/individual/2025-iit/2025-individual-income-tax-booklet.pdf) |
| Oklahoma | Starts from federal | Follows; plus an Oklahoma 100% bonus deduction on Schedule 511-A for qualified property and QIP (useful where federal bonus was less than 100%) | Follows | None found | [Form 511 packet](https://oklahoma.gov/content/dam/ok/en/tax/documents/forms/individuals/current/511-Pkt.pdf) |

### States that decouple, with the add-back and recovery method

| State | Conformity | §168(k) and §168(n) | Add-back and recovery | §179 | OBBBA response | Source |
| --- | --- | --- | --- | --- | --- | --- |
| Arkansas | Selected IRC sections at fixed dates | Not adopted | Report the federal/Arkansas depreciation difference (Form AR-OI); gain or loss uses Arkansas basis | IRC §179 as in effect on January 1, 2022, for purchases after 2022: 2025 limit $1,250,000, cost-of-property limit $3,130,000 | Fixed-date; 2026 limits: **check** | [2025 AR1000F instructions](https://www.dfa.arkansas.gov/wp-content/uploads/2025_AR1000F_and_AR1000NR_Instructions.pdf) |
| California | IRC as of January 1, 2025; does not conform to OBBBA | Not allowed at any percentage | Recompute on form 3885A; Schedule CA (540) Section B adjustment each year | $25,000, reduced once §179 property costs more than $200,000; no §179 for off-the-shelf software or qualified real property | None | [3885A instructions](https://www.ftb.ca.gov/forms/2025/2025-3885a-instructions.html); [FTB Pub. 1001](https://www.ftb.ca.gov/forms/2025/2025-1001-publication.pdf); [Schedule CA instructions](https://www.ftb.ca.gov/forms/2025/2025-540-ca-instructions.html) |
| Connecticut | Starts from federal AGI | Add back 100% of §168(k) (Schedule 1, line 36) | Subtract 25% of the add-back in each of the four following years (line 48a) | Add back 80% of the §179 deduction (line 36a); subtract 25% of that add-back in each of the four following years | Statute has no end date; applies to 2026 | [2025 CT-1040 instructions](https://portal.ct.gov/-/media/drs/forms/2025/income/2025-ct-1040-instructions_1225.pdf) |
| Delaware | Rolling, with a 2026 decoupling (HB 255, 85 Del. Laws c. 231, § 1106(d)) | Property acquired and placed in service after December 31, 2025 and before January 1, 2031 that would get OBBBA 100% bonus is depreciated under the pre-OBBBA Code: 20% bonus in 2026, 0% from 2027. Same rule for §168(n) property | Separate Delaware schedule; Delaware basis and gain differ. 2026 form line not yet published | Follows (not named in the Act) | Individuals: from 2026. 2025 returns follow federal | [HB 255](https://delcode.delaware.gov/sessionlaws/ga153/chp231.shtml); [Delaware memo 2025-2](https://revenuefiles.delaware.gov/2025/TIMs/HB_255_TIM.pdf) |
| District of Columbia | Own rules for business income (Form D-30; for Form D-40 individuals: **check**) | No §168(k), no §168(n) | Recompute depreciation without bonus; attach a computation showing the DC basis was not reduced by federal bonus (D-30 instructions) | Lesser of $25,000 or cost | None | [D.C. Code 47-1803.03](https://code.dccouncil.gov/us/dc/council/code/sections/47-1803.03); [2025 D-30](https://otr.cfo.dc.gov/sites/default/files/dc/sites/otr/publication/attachments/2025_D30_Book_Final_wLinks_02232026.pdf) |
| Georgia | Annual fixed-date update | §168(k) not adopted | Georgia Form 4562 depreciation without bonus; difference on the return | 2025: $2,500,000, phase-out $4,000,000; no §179(e) real property. 2026: **check** | §174A not adopted; new §168(n) qualified production property: **check** | [2025 GA 4562 instructions](https://dor.georgia.gov/document/document/2025-4562-depreciation-amortization-including-information-listed-property/download) |
| Hawaii | IRC as amended as of December 31, 2025, for years beginning after December 31, 2025 (Act 35, 2026) | §168(k) and §168(n) not operative | Separate Hawaii Form 4562 | $25,000; reduction begins above $200,000; no software | Act 35 conformed to parts of OBBBA, not bonus | [Announcement 2026-06](https://files.hawaii.gov/tax/news/announce/ann26-06.pdf); [HB 2329 CD1](https://data.capitol.hawaii.gov/sessions/session2026/bills/HB2329_CD1_.pdf); [N-11 instructions](https://files.hawaii.gov/tax/forms/2025/n11ins.pdf) |
| Illinois | Rolling | Reverses §168(k) (and §168(n) from 2026) on Form IL-4562 | Add back the bonus. For 100% bonus assets, each later year subtract the depreciation you would have claimed had you elected out (Line 16). For 30%, 40%, 50%, 60% or 80% bonus assets, use the IL-4562 Step 3 lines for that percentage. Reverse on sale or at end of life | No §179 line on IL-4562 | Added §168(n) for years beginning on or after January 1, 2026 | [IL-4562 instructions](https://www.illinois.gov/content/dam/soi/en/web/tax/forms/incometax/documents/currentyear/miscellaneous/il-4562-instr.pdf) |
| Indiana | Largely decoupled since 2002 | Add back bonus minus depreciation without bonus (code 104); §168(n) disallowed, depreciated as 39-year nonresidential real property | Negative adjustments in later years | Capped at $25,000 (code 105); later deductions for the difference | Bulletin 118 (May 2026) covers §168(n) | [Information Bulletin 118](https://www.in.gov/dor/files/ib118.pdf) |
| Kentucky | IRC as of December 31, 2024 | Property placed in service after September 10, 2001: §168 as in effect on December 31, 2001 (no bonus) | Kentucky Form 4562; Schedule M add-back and subtraction | Property placed in service on or after January 1, 2020: §179 as in effect on December 31, 2003, no phase-out | OBBBA not adopted | [740 instructions](https://revenue.ky.gov/Forms/740%20Packet%20Instructions.pdf) |
| Maine | Selective | Add back the net increase from §168(k) | Later years: subtract the extra depreciation that would have been allowed without §168(k); adjust gain or loss on disposal | Full conformity for property placed in service in 2020 or later | **Check** 2026 conformity | [MRS guidance](https://www.maine.gov/revenue/sites/maine.gov.revenue/files/inline-files/Bonusdep_guidance_2022.pdf) |
| Maryland | Decoupled by statute | No §168(k) (Form 500DM, code l; later subtraction code bb); §168(n): decoupled for 2025 (code dc); 2026: **check** | Recompute without bonus. Neither the bonus nor the §179 decoupling applies to property placed in service by a manufacturing entity on or after January 1, 2019 | $25,000, phase-out from $200,000 | 2025: automatically decoupled from §168(n); 2026 position: **check** the 2026 Form 500DM instructions | [Tax-General §10-210.1](https://mgaleg.maryland.gov/mgawebsite/Laws/StatuteText?article=gtg&section=10-210.1&enactments=false); [2025 resident booklet](https://www.marylandtaxes.gov/content/dam/mdcomp/tax/instructions/2025/resident-booklet.pdf) |
| Minnesota | IRC as amended through May 1, 2026, retroactive to federal effective dates (Laws 2026, ch. 128) | Add back 80% of the §168(k) deduction (§290.0131 subd. 9) | Subtract one-fifth of the addition in each of the five following years (§290.0132 subd. 9). The addition is written for §168(k) only; for §168(n) property, **check** the department's 2026 guidance | No addition for property placed in service in taxable years beginning after 2019 (the §179 addition applies only before January 1, 2020) | Conformity advanced in 2026 | [§290.0131](https://www.revisor.mn.gov/statutes/cite/290.0131); [§290.0132](https://www.revisor.mn.gov/statutes/cite/290.0132); [Laws 2026 ch. 128](https://www.revisor.mn.gov/laws/2026/0/Session+Law/Chapter/128/) |
| New Jersey (Gross Income Tax) | Own depreciation rules | Only a 30% allowance, and only if taken federally; 50% and higher not permitted | Worksheet GIT-DEP; same method and life as federal; disposal adjustment | Maximum $25,000; the federal reduced dollar limitation for asset cost applies, computed with the $25,000; no business income limit; unused amounts cannot be carried forward | None | [GIT-DEP](https://www.nj.gov/treasury/taxation/pdf/current/gitdep.pdf); [NJ-1040 instructions](https://www.nj.gov/treasury/taxation/pdf/current/1040i.pdf) |
| New York | Rolling, with decouplings | No §168(k) for property placed in service on or after June 1, 2003 (except resurgence zone and Liberty Zone property); §168(n) decoupled from 2025 | Add back (A-209); subtract New York depreciation (S-213); disposal adjustment (S-214); Form IT-398 | Generally follows; SUVs have their own modification (A-208) | Notice N-26-1 | [IT-225 instructions](https://www.tax.ny.gov/pdf/current_forms/it/it225i.pdf); [N-26-1](https://www.tax.ny.gov/forms/n-notices/n-26-1.htm) |
| North Carolina | Own adjustments | §168(k) and §168(n) not adopted | Add 85% of federal bonus; deduct 20% of the amount added back in each of the first five taxable years beginning with the next year | $25,000 and $200,000; add 85% of the difference | Not adopted | [2025 D-401 instructions](https://www.ncdor.gov/2025-d-401-individual-income-tax-instructions/open) |
| Ohio | Starts from federal AGI | Add 5/6 of §168(k) bonus | Deduct 1/5 of a 5/6 add-back in each later year (see the boundary table for 2/3 and 6/6) | Add 5/6 of §179 above the amount allowed under §179 as it existed on December 31, 2002 | None | [2025 IT 1040 instructions](https://dam.assets.ohio.gov/image/upload/tax.ohio.gov/forms/ohio_individual/individual/2025/it1040-booklet.pdf) |
| Oregon | IRC updated to December 31, 2025 or January 1, 2026 (SB 1507, Laws 2026 ch. 142) | 2025: follows. 2026 and later: bonus disallowed | Add back; recover through Oregon depreciation without bonus. Form line: **check** the 2026 Oregon instructions | Not addressed in the department's summary: **check** | A referendum petition (filed April 10, 2026) seeks to repeal the disconnection: **check** its status | [Oregon 2026 legislation summary](https://www.oregon.gov/dor/Pages/2026-summary-of-legislation.aspx) |
| Pennsylvania (PIT) | Own rules | Not allowed | Recompute without bonus; where PA and federal basis differ, PA requires straight-line depreciation | Follows federal limits for tax years beginning on or after January 1, 2023 | None | [PA PIT Guide](https://www.pa.gov/agencies/revenue/forms-and-publications/pa-personal-income-tax-guide/net-income-loss-from-the-operation-of-a-business,-profession-or-farm) |
| South Carolina | IRC as amended through December 31, 2024 (2025 returns) | Not recognized | Add back the excess in the first year; extra SC depreciation in later years; same life | **Check** (the fixed date means OBBBA §179 changes are not adopted for 2025) | Not adopted for 2025 | [SC1040 instructions](https://dor.sc.gov/sites/dor/files/forms/SC1040Instr_2025.pdf) |
| Vermont | Own add-back for bonus | Not allowed: Vermont has never conformed to federal bonus (disallowance dates from Act 190 of 2008) | Recompute as if no bonus; form line: **check** the Vermont instructions | Conforms to pre-OBBBA law; OBBBA update: **check** | "Never conformed" to bonus | [TB-44](https://tax.vermont.gov/sites/tax/files/documents/TB44.pdf); [Joint Fiscal Office presentation](https://legislature.vermont.gov/Documents/2026/Workgroups/House%20Ways%20and%20Means/Corporate%20Income%20Tax/W~Michael%20Hackett~Vermont%20Tax%20Link-Up%20Presentation~2-5-2026.pdf) |
| Virginia | IRC as of December 31, 2025 (fixed date from 2025 returns) | Continues to deconform from bonus; deconforms from §168(n) | Fixed-date conformity addition; later subtractions; separate Virginia records | Deconforms from the OBBBA increases | Tax Bulletin 26-1 | [TB 26-1](https://www.tax.virginia.gov/sites/default/files/inline-files/tb-26-1-date-of-irc-conformity-advanced.pdf) |
| Wisconsin | Federal law amended to December 31, 2022 (2025 returns) | Not allowed | Schedule I adjustment each year until fully depreciated or disposed | **Check** | Later federal laws apply only if adopted | [2025 Form 1 instructions](https://www.revenue.wi.gov/TaxForms2025/2025-Form1-Inst.pdf) |

### No personal income tax on wages or business income

Alaska, Florida, Nevada, South Dakota, Tennessee, Texas, Washington and Wyoming have no broad personal income tax on wages or business income, so a resident sole proprietor or pass-through owner has no individual add-back there. New Hampshire does not tax wages; its business profits tax can reach some sole proprietors (**check**). Entity-level taxes are outside this Guide; check each one separately:

- Florida corporate income tax: add back §168(k) for property placed in service before January 1, 2027, and subtract one seventh of the addition each year over seven years ([F-1120 instructions](https://floridarevenue.com/Forms_library/current/f1120n.pdf)).
- Texas franchise tax, Tennessee franchise and excise tax, Washington B&O tax and the New Hampshire business profits tax: **check**.

### States we could not verify (check)

Idaho, Kansas, Massachusetts, Michigan, Mississippi, New Mexico, Rhode Island, Utah and West Virginia: **check**. On 25 September 2026 their revenue department or legislature pages either refused our requests or did not state the rule. Do not assume they follow federal law. Read the state's 2025 individual instructions and any 2026 conformity act. Points to confirm:

- Idaho, New Mexico: confirm any 2026 conformity act and its treatment of §168(k) and §168(n).
- West Virginia: the Governor proposed restoring full bonus depreciation for the 2026 session ([Governor's release](https://governor.wv.gov/article/governor-patrick-morrisey-proposes-tax-relief-package-upcoming-legislative-session-build)); confirm what was enacted.
- Michigan: confirm its IRC conformity date and its treatment of §168(k) and §168(n).
- Massachusetts, Rhode Island, Mississippi, Kansas, Utah: confirm whether the state decouples from §168(k) and whether it has its own §179 limit.

## Boundaries and exceptions

| Situation | Rule | Source |
| --- | --- | --- |
| Asset under a written binding contract signed before January 20, 2025, placed in service in 2025 | Federal bonus is 40% (60% for long production period property and certain aircraft), not 100%; the state add-back base is the 40% | [Pub. 946](https://www.irs.gov/publications/p946); [§168 note](https://www.law.cornell.edu/uscode/text/26/168) |
| Ohio employer that increased Ohio withholding by at least 10% over the previous year | Add back 2/3 instead of 5/6; deduct 1/2 of the 2/3 add-back in each later year | [Ohio instructions](https://dam.assets.ohio.gov/image/upload/tax.ohio.gov/forms/ohio_individual/individual/2025/it1040-booklet.pdf) |
| Ohio federal net operating loss caused by §168(k) or §179 | Add back 6/6; deduct 1/6 each later year | same |
| Ohio employer whose withholding increase is at least the total §168(k) and §179, or owner of less than 5% of a pass-through | No Ohio add-back | same |
| Ohio year with an NOL, NOL carryback or NOL carryforward (any add-back type) | No deduction of prior add-backs that year; carry the deduction forward to the next tax year with no NOL, carryback or carryforward | same |
| Ohio later-year deduction not used (other than one deferred because of an NOL) | Taken in equal consecutive increments; an unused portion from any given year does not carry forward | same |
| Minnesota bonus in an activity with a disallowed loss | The bonus counted for the addition is limited to the excess of the bonus over the disallowed loss; the rest is added when the loss is allowed | [§290.0131 subd. 9](https://www.revisor.mn.gov/statutes/cite/290.0131) |
| Minnesota federal net operating loss in the year of the addition | The amount recovered in the five later years is the addition minus the NOL generated that year, not below zero | [§290.0132 subd. 9](https://www.revisor.mn.gov/statutes/cite/290.0132) |
| Maryland manufacturing entity, property placed in service on or after January 1, 2019 | No §168(k) or §179 decoupling | [§10-210.1](https://mgaleg.maryland.gov/mgawebsite/Laws/StatuteText?article=gtg&section=10-210.1&enactments=false) |
| Indiana property that would have qualified for a §1031 deferral before 2018 | Part of the bonus and §179 is allowed, up to the "Section 1031 Income" | [IB 118](https://www.in.gov/dor/files/ib118.pdf) |
| Maine property placed in service before 2020 | Older rules apply (see Parts 2 to 4 of the MRS guidance) | [MRS guidance](https://www.maine.gov/revenue/sites/maine.gov.revenue/files/inline-files/Bonusdep_guidance_2022.pdf) |
| Delaware property placed in service in 2025 | Follows federal for individuals; the decoupling starts with property placed in service after December 31, 2025 | [Delaware memo 2025-2](https://revenuefiles.delaware.gov/2025/TIMs/HB_255_TIM.pdf) |
| New Jersey partnership or S corporation | The entity computes the adjustment; each entity is limited to a $25,000 §179 deduction | [GIT-DEP](https://www.nj.gov/treasury/taxation/pdf/current/gitdep.pdf) |
| Federal election out of bonus for a class | No bonus, so no state bonus add-back for that class; the state §179 limit still applies | [Pub. 946](https://www.irs.gov/publications/p946) |

## Worked cases

### Case 1: Connecticut, 2026 ([CT-1040 instructions](https://portal.ct.gov/-/media/drs/forms/2025/income/2025-ct-1040-instructions_1225.pdf))

A sole proprietor deducts $100,000 of bonus depreciation and a $40,000 §179 deduction on the 2026 federal return. Connecticut additions: $100,000 (line 36) and 80% × $40,000 = $32,000 (line 36a). In each of 2027 to 2030, subtract 25% × $100,000 = $25,000 (line 48a) and 25% × $32,000 = $8,000.

### Case 2: North Carolina, 2025 return ([D-401 instructions](https://www.ncdor.gov/2025-d-401-individual-income-tax-instructions/open))

Federal bonus depreciation of $50,000 in 2025. Add 85% × $50,000 = $42,500 on the 2025 return. Deduct 20% × $42,500 = $8,500 in each of 2026 to 2030.

### Case 3: Minnesota, 2026 ([§290.0131](https://www.revisor.mn.gov/statutes/cite/290.0131); [§290.0132](https://www.revisor.mn.gov/statutes/cite/290.0132))

Federal bonus depreciation of $50,000 in 2026, no disallowed loss and no federal NOL. Add 80% × $50,000 = $40,000. Subtract one-fifth of $40,000 = $8,000 in each of 2027 to 2031.

### Case 4: Ohio, 2026 ([IT 1040 instructions](https://dam.assets.ohio.gov/image/upload/tax.ohio.gov/forms/ohio_individual/individual/2025/it1040-booklet.pdf))

Federal bonus depreciation of $60,000; the business did not raise Ohio withholding and has no federal NOL. Add 5/6 of $60,000 = $50,000. Deduct 1/5 of $50,000 = $10,000 in each of the next five years. If a later year has an NOL, NOL carryback or NOL carryforward, that year's $10,000 is not claimed then but carried to the next year without one. Confirm the line numbers in the 2026 instructions when published.

### Case 5: California §179, 2026 ([3885A instructions](https://www.ftb.ca.gov/forms/2025/2025-3885a-instructions.html))

Machinery costing $210,000 is placed in service and fully expensed federally. California limit: $25,000 − ($210,000 − $200,000) = $15,000, provided business income is at least that. The remaining $195,000 is depreciated on form 3885A with no bonus.

### Case 6: Delaware, 2026 ([Delaware memo 2025-2](https://revenuefiles.delaware.gov/2025/TIMs/HB_255_TIM.pdf))

A machine costing $100,000 is acquired and placed in service in June 2026, with 100% federal bonus. Delaware bonus is 20% × $100,000 = $20,000. The remaining $80,000 is depreciated under regular MACRS. The Delaware addition is the federal deduction minus the Delaware depreciation for the year.

### Case 7: Indiana §179, 2026 ([IB 118](https://www.in.gov/dor/files/ib118.pdf))

Property costing $225,000 is expensed in full under federal §179. Indiana allows $25,000, so add back $225,000 − $25,000 = $200,000 (code 105). The $200,000 is then depreciated for Indiana, and each later year's Indiana depreciation is a deduction.

### Case 8: federal acquisition date, 2025 ([Pub. 946](https://www.irs.gov/publications/p946))

Equipment was bought under a written binding contract signed on January 10, 2025 and placed in service in March 2025. It counts as acquired before January 20, 2025, so federal bonus is 40%, not 100%. Every state add-back in this Guide starts from that 40% figure.

## 2025 returns (tax year 2025; extended federal deadline October 15, 2026)

- Federal: 100% bonus for property acquired after January 19, 2025; 40% for property acquired earlier; §179 limit $2,500,000, reduction above $4,000,000, SUV cap $31,300 ([Pub. 946](https://www.irs.gov/publications/p946)).
- **Delaware and Oregon follow federal bonus for 2025**; their decouplings start in 2026.
- **Hawaii 2025:** no bonus and the $25,000 §179 limit under the earlier conformity law ([N-11 instructions](https://files.hawaii.gov/tax/forms/2025/n11ins.pdf)).
- **Arizona:** the 2026 Act adopted the P.L. 119-21 changes retroactively for 2025 ([enacted fact sheet](https://www.azleg.gov/legtext/57leg/2R/summary/S.1861-4168ATT_ASENACTED.DOCX.htm)).
- **Virginia:** the December 31, 2025 conformity date was enacted February 20, 2026 and applies to 2025. Returns filed before then may need amending ([TB 26-1](https://www.tax.virginia.gov/sites/default/files/inline-files/tb-26-1-date-of-irc-conformity-advanced.pdf)).
- **New York:** it does not conform to §168(n) for tax years beginning on or after January 1, 2025. If a 2025 return has been filed, an amended return must be filed to report the §168(n) modifications ([Notice N-26-1](https://www.tax.ny.gov/forms/n-notices/n-26-1.htm)).
- **Minnesota:** until Laws 2026, ch. 128, Minnesota used the IRC as amended through May 1, 2023, so bonus on 2025 returns filed before that law was figured under pre-OBBBA rules. The law moved the date to May 1, 2026, effective retroactively with the federal changes. **Check** the department's guidance on whether a 2025 return already filed should be amended ([Laws 2026 ch. 128](https://www.revisor.mn.gov/laws/2026/0/Session+Law/Chapter/128/)).
- **Georgia 2025 §179:** $2,500,000, phase-out $4,000,000 ([GA 4562 instructions](https://dor.georgia.gov/document/document/2025-4562-depreciation-amortization-including-information-listed-property/download)). **Arkansas 2025 §179:** $1,250,000, cost limit $3,130,000 ([AR instructions](https://www.dfa.arkansas.gov/wp-content/uploads/2025_AR1000F_and_AR1000NR_Instructions.pdf)).
- **South Carolina 2025:** IRC as amended through December 31, 2024 ([SC1040 instructions](https://dor.sc.gov/sites/dor/files/forms/SC1040Instr_2025.pdf)).

## When to refuse or refer

- Refer any state marked **check** until you have read that state's current instructions and any 2026 conformity act.
- Refer if the client's records do not show each asset's state basis in a decoupled state and the asset is several years old; rebuilding the schedule is a separate engagement.
- Refer C corporation returns, franchise and gross-receipts taxes, and combined or unitary filings.
- Refer Oregon 2026 returns until the SB 1507 referendum outcome is known.
- Refer §168(n) qualified production property; the federal election and the state treatment are both new.
- Do not give a combined federal-and-state figure where the federal acquisition date (before or after January 20, 2025) is not documented.

## Filing and payment

- Federal: Form 4562 for §179, bonus and MACRS; the §179 election and any election out of bonus are made on a timely filed return, including extensions ([Pub. 946](https://www.irs.gov/publications/p946)).
- State: the add-back and later recovery go on the form named in each row (for example CT-1040 Schedule 1, NC Schedule S, Ohio Schedule of Adjustments, IL-4562, Indiana codes 104 and 105, CA form 3885A and Schedule CA, MD Form 500DM, NY Form IT-398 and IT-225, NJ GIT-DEP). 
- An add-back raises state taxable income in the year of purchase. Check the client's state estimated payments for that year.

## Completion checklist

- [ ] Federal acquisition date and bonus rate confirmed for each asset; any election out or 40% election recorded.
- [ ] Every filing state identified, and its row read for the correct year (2025 or 2026).
- [ ] States marked **check** confirmed from the state's own current instructions.
- [ ] State depreciation recomputed where required; state §179 limit applied (California, Hawaii, DC, Indiana, Maryland, New Jersey, North Carolina, Kentucky, Arkansas).
- [ ] Add-backs entered on the right state line; fixed-fraction recoveries scheduled (Connecticut, Minnesota, North Carolina, Ohio).
- [ ] Prior-year recoveries claimed this year.
- [ ] Disposals: state gain or loss computed on state basis.
- [ ] Pass-through K-1 state amounts reconciled, with no double adjustment.
- [ ] State estimated payments reviewed.

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
