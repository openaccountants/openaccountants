---
name: us-multi-state-residency-and-allocation
description: Tier 2 US federal-level content skill for multi-state residency, domicile, part-year residency, statutory residency (e.g. NY 183-day + abode rule), nonresident income sourcing, the convenience-of-the-employer rule (NY, NJ, CT, PA, NE, AR — partially), equity compensation allocation (stock options grant-to-exercise, RSU grant-to-vest), §4 USC 114 federal preemption of pension source taxation, resident credit for taxes paid to other states, reciprocal-agreement states (PA-NJ, OH-WV-KY-IN-MI-PA-VA), and post-COVID telework sourcing. Covers tax year 2025.
jurisdiction: US
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: James Wallach
review_status: current
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# US Multi State Residency And Allocation

## US Multi-State Residency and Income Allocation (TY 2025)

Note on scope. This skill sits in the us-federal/ package because the federal Form 1040 starting point and the §4 USC 114 federal preemption of pension source taxation are federal in character. The bulk of the analysis, however, is state-by-state. This skill provides the FRAMEWORK and the federal overlay; individual state nuances (e.g. CA FTB Pub. 1031, NY TSB-M-19(1)I, NJ GIT-6, MA TIR 95-7) are referenced but a credentialed state preparer must finalize the return for each state involved. This is also the single most-litigated area of US state tax law — the worked examples and case citations matter. Read the whole skill.

## 1. Scope, refusal catalogue, and reviewer assumption

### 1.1 In scope

- **In-scope taxpayer situations** — US individual taxpayers (citizens, resident aliens, dual-status residents handled by us-tax-workflow-base) who, during the tax year: Moved between US states (a "move year" — part-year residency); Have homes in more than one state ("snowbirds", dual residents); Work remotely for an employer in a state different from the employee's physical work location; Vest in equity compensation (stock options, RSU, ESPP) spanning a multi-state service period; Receive pension, IRA, or qualified-plan distributions after moving from a former work state; Receive K-1 income from pass-through entities operating in multiple states; Sell real estate located in a state other than the state of residence. Filings: federal Form 1040; resident state Form 540/IT-201/equivalent; nonresident state Form 540-NR/IT-203/equivalent; part-year forms; resident-credit schedules (CA Sch. S, NY IT-112-R, etc.)  _(Section 1.1)_

### 1.2 Out of scope — refer to a state-licensed practitioner or another skill

- **Out-of-scope items and referrals** — Foreign (non-US) residency and tax treaty residency tie-breakers → see us-foreign-earned-income-2555 and us-foreign-tax-credit-1116; US territory residency (Puerto Rico, USVI, Guam, AS, CNMI) — Act 60/22 PR, possessions source rules — REFUSE in this skill; Nonresident alien (NRA) federal source rules under §861-§865 — REFUSE; that is a §1.861 / §871 / §1441 problem, not a state residency problem; Trust and estate residency (the trust situs question) — REFUSE for the trust itself; beneficiary residency is in scope only insofar as it affects the beneficiary's 1040; Multistate corporate apportionment (UDITPA, MTC factors) — REFUSE; this skill is individual only; State income tax of professional athletes ("jock tax" duty-day allocation) and entertainers — REFUSE; specialized; State and local credits for taxes paid to foreign countries (CA's foreign-country credit is a separate issue) — REFUSE; not the §901 problem; Local-only taxes: NYC UBT, NYC personal income tax (resident definition differs from NY State), Philadelphia wage tax, Yonkers, San Francisco gross receipts — flag and refer  _(Section 1.2)_

### 1.3 Reviewer assumption

- **Reviewer assumption** — A credentialed practitioner (CPA, EA, or attorney admitted under Circular 230) and a state-licensed preparer for each state involved must review and sign off. Multi-state residency audits are aggressive, fact-intensive, and frequently appealed (see Section 14 for famous cases). This skill does NOT substitute for state-licensed review.  _(Section 1.3)_

### 1.4 Conservative defaults

- **Conservative default assumptions** — When in doubt about domicile, default to the more aggressive state (the "audit risk" state) as the resident state. When in doubt about a day in NY, count it as a NY day (the taxpayer bears the burden of proving non-NY presence on a given day — N.Y. Tax Law §605(b)(1)(B); 20 NYCRR §105.20). When in doubt about a remote-work day, default to the convenience-rule jurisdiction (NY/NJ/CT/PA/NE/AR/DE — see Section 8). When in doubt about equity comp sourcing, use the workday-allocation method from grant to vest (RSU) or grant to exercise (NQSO). Do not use the simpler "state of residence at vest" method unless the state allows it (most do not for taxpayers who worked in multiple states).  _(Section 1.4; N.Y. Tax Law §605(b)(1)(B); 20 NYCRR §105.20)_

## 2. The fundamental distinction: domicile vs residency

This is the single most common source of taxpayer confusion. They are NOT synonyms.

### 2.1 Domicile

- **Domicile** — Domicile is a common-law concept. A person has exactly ONE domicile at any moment in time. Domicile is the state (or country) the person regards as their permanent home — the place they intend to return to when absent. Three classical elements: 1. Physical presence in the state at some point; 2. Intent to make it home (the animus manendi); and 3. No present intent to leave for somewhere else (the animus non revertendi to the old place). Domicile persists until affirmatively changed. You do not lose your old domicile until you have (a) physically moved to a new state AND (b) formed the intent to make the new state your permanent home AND (c) abandoned the intent to return to the old state. All three are required. This is the "two-prong move + intent" rule. Burden of proof. When a taxpayer claims to have changed domicile, they bear the burden of proving the change by clear and convincing evidence. The old state's revenue agency presumes domicile has not changed.  _(Section 2.1)_

### 2.2 Residency (tax-purposes)

- **Residency** — Residency is a creature of state statute and varies state to state. A person can be a resident of MORE THAN ONE state simultaneously (a "dual resident"). The most common forms: Domiciliary resident: the state of domicile is automatically a resident state for tax. Always. Statutory resident: even if domiciled elsewhere, you can be a resident of a state under that state's statutory test (typically: maintain a permanent place of abode in the state for substantially all the year AND spend more than 183 days there). See Section 3. Part-year resident: you became a resident or ceased to be a resident during the tax year (move-in or move-out year). Nonresident: neither domiciled in the state nor a statutory resident, but received income from sources in the state.  _(Section 2.2)_

### 2.3 Why the distinction matters

**Why the distinction matters**  _(Section 2.3)_

| Question | Domicile answer | Residency answer |
| --- | --- | --- |
| Where do I file as a resident? | Domiciliary state always | Domiciliary state PLUS any statutory-resident state |
| Where is my intangible income (dividends, interest, capital gains on stocks) taxed? | Domiciliary state | Domiciliary state (intangibles follow the person) |
| Where is my pension taxed? | State of residence at time of payment, only — federal preemption under §4 USC 114 (Section 9) | Same |
| Can I be taxed by TWO states on the same wages? | Possibly yes, with a resident credit | Possibly yes — and the resident credit may not eliminate all double tax |

### 2.3 Why the distinction matters

AUDIT FLASH POINT. New York audits ex-residents who claim to have moved out. The audit theory is: you may have moved out for domicile purposes, but you remain a NY statutory resident if you kept a place of abode AND spent more than 183 days in NY. Statutory residency is a separate, independent hook from domicile. Many "I moved to Florida" cases lose on statutory residency despite winning on domicile.

## 3. Statutory residency — the 183-day + permanent place of abode rule

### 3.1 The classic rule (NY, NJ, CT, MA, IL, MN, and many others)

- **NY statutory residency rule** — N.Y. Tax Law §605(b)(1)(B): an individual is a New York State resident if the individual: (a) is domiciled in NY, OR (b) maintains a permanent place of abode in NY for substantially all of the tax year AND spends in the aggregate more than 183 days of the tax year in NY. The (b) prong is the "statutory resident" trap. It is an independent ground for NY residency that does not require NY domicile. Both elements must be present: (i) Permanent place of abode = a dwelling place permanently maintained by the taxpayer, whether or not owned, and whether or not in the taxpayer's name, that is suitable for year-round living. A vacation cottage used only seasonally is NOT a permanent place of abode (20 NYCRR §105.20(e)). A studio apartment owned by an employer and used by the employee on business days IS. A bedroom in a parent's house occasionally used IS NOT, IF the taxpayer cannot freely access it and does not maintain it (the Gaied case — see Section 14). (ii) More than 183 days = 184 or more days physically present in NY. ANY PART of a day in NY counts as a NY day except: Pure transit (changing planes at JFK; driving through NY on I-95 without stopping for a meaningful purpose); Days entirely in a NY hospital as a patient (medical exception); Days in NY solely for boarding a flight to another country (limited). ALL OTHER part-days count as full NY days, including: Commuting in for one meeting (one day); A 4-hour stop for a meal at a NY restaurant (one day); A day where you arrive at LaGuardia at 11 PM (one day); A day you leave NY at 6 AM (one day). This makes the 183-day count brutal in practice for commuters. NY business commuters from CT and NJ can hit 184 days easily without realizing it.  _(N.Y. Tax Law §605(b)(1)(B); 20 NYCRR §105.20(e))_

### 3.2 "Substantially all" the year

- **Substantially-all-year abode maintenance test** — Pre-2022: 11 months (TSB-M and audit guidance). 2022-forward: NY DTF has softened in some guidance to "more than 10 months" or "substantially all" — but auditors still apply 11 months in practice. If you bought the NY apartment in March and sold it in November (9 months), arguably NO statutory residency even with 200 NY days. If you bought January 5 and sold December 20 (about 11.5 months), almost certainly statutory residency.  _(TSB-M and audit guidance)_

### 3.3 Other states' statutory residency thresholds (selection)

**Other states' statutory residency thresholds**  _(See individual state statutes as noted in table)_

| State | Threshold | Notes |
| --- | --- | --- |
| NY | >183 days + permanent place of abode for substantially all year | Most aggressive |
| NJ | >183 days + permanent place of abode in NJ | N.J.S.A. 54A:1-2(m) |
| CT | >183 days + permanent place of abode | Conn. Gen. Stat. §12-701(a)(1)(B) |
| MA | >183 days + permanent place of abode | M.G.L. ch. 62 §1(f) |
| IL | >9 months in IL | Treated as resident for full year; complex |
| CA | 9-month presumption + multi-factor closest-connections test | See Section 13 |
| MN | >183 days + abode | Aggressive — "Wynne" line of cases |
| MD | >6 months + abode | Aggressive |
| VA | >183 days + abode | Statutory resident if domiciled elsewhere |
| HI | >200 days | Higher threshold |
| WI | >183 days + abode | Reciprocal with IL/MI/IN/KY |

### 3.4 Day-counting in practice — recordkeeping

- **Day-counting evidence and recordkeeping** — The taxpayer bears the burden of proving non-presence on each disputed day. Modern audit evidence used: Cell phone tower records (subpoenaed by NY DTF) — this is the single most damning evidence; Credit card and debit card receipts with geocoded merchant locations; EZ-Pass / toll records; Subway / Metro card swipes (NY uses this aggressively); Calendar and email metadata; Building doorman/elevator logs for co-op and condo; Social media posts with geotags; Aircraft and yacht logs. The "diary defense" — a taxpayer-prepared calendar of where they were each day — is necessary but not sufficient. The taxpayer must also have contemporaneous corroborating evidence. A diary alone is regarded as self-serving. Practical recommendation. Any taxpayer with potential statutory-residency exposure (>150 days in NY/NJ/CT/MA + an abode there) should keep: 1. A daily location log (an app like TaxDay, Monaeo); 2. Backup credit card statements; 3. Cell tower records (download monthly from carrier); 4. Travel boarding passes.  _(Section 3.4)_

### 3.5 Dual residency

- **Dual residency mechanics** — You can be a statutory resident of NY AND a domiciliary resident of FL simultaneously. Both states tax 100% of your worldwide income. The resident credit (Section 10) provides PARTIAL relief — you get a credit in one state for tax paid to the other, but only up to the lesser of the two states' rates on the doubly-taxed income. The classic worst-case: FL-domiciled NY statutory resident with significant intangible income (capital gains, dividends). FL doesn't tax intangibles (no PIT), so there's nothing to credit against. NY taxes 100% of the intangibles. The taxpayer is in the same position as a NY domiciliary. AUDIT FLASH POINT. NY pursues "I moved to FL but kept the NYC pied-à-terre" cases hard. The taxpayer wins ONLY by: (a) selling the NY abode within reason after the move, OR (b) limiting NY days to ≤183 with rigorous proof. Keeping a $5M NYC apartment + visiting NY 190 days + claiming FL domicile = NY statutory residency + audit.  _(Section 3.5)_

## 4. The 6-factor domicile test

When a taxpayer claims to have changed domicile, state auditors (and the Tax Appeals Tribunals) apply a multi-factor test. NY uses a 5-primary-factor framework; CA uses a "closest-connections" multi-factor analysis; most other states use variants of the same six factors:

### 4.1 The six classical domicile factors

- **Six classical domicile factors** — 1. Home (residence) — Where is the more valuable home? Where is the larger home? Where is the home filled with the more sentimental possessions? "Move from a $5M townhouse to a $400k condo" weighs against change of domicile — the $5M house is presumed to remain home. Renting out vs selling the old home: selling is dispositive; renting is helpful; keeping vacant is bad (suggests intent to return). 2. Time (active business or employment) — Where does the taxpayer spend more time on income-producing activity? If retired, where is most leisure time spent? In move years, the "after-move" period is what counts. 3. Items "near and dear" — Where are family photos, heirlooms, jewelry, art collection, pets, wine cellar, family bible, important documents (wills, trusts, original life insurance policies)? This is the "what would you grab in a fire" test. Storage of items at the old home is bad evidence. 4. Active business involvement / Business activity — Where is the taxpayer's primary business or professional practice? This is less determinative for retirees but very determinative for working-age taxpayers. 5. Family ties — Where is the spouse domiciled? (Spouses can have different domiciles but it's unusual.) Where do minor children attend school? Where are college kids' "home" addresses? Where are aging parents who the taxpayer visits/supports? 6. Other indicia — Voter registration, Driver's license, Vehicle registration, Professional licenses (CPA, bar, medical, real estate), Bank accounts (especially the primary checking), Country club / religious / professional / civic memberships, Doctors (PCP, dentist, specialists), Safety deposit box, Mailing address, Address on tax returns (including federal Form 1040), Will and trust references.  _(Section 4.1)_

### 4.2 NY 5-factor primary test (TSB-M-09(1)I + later guidance)

- **NY 5-factor primary and secondary test** — NY auditors apply five primary factors, plus secondary factors: Primary: 1. Home (size, value, use, ownership) 2. Active business involvement 3. Time (excluding statutory-residency days — independent count) 4. Items near and dear 5. Family connections (spouse, minor children). Secondary (use when primary factors are inconclusive): Mailing address used for important documents; Address on federal return; Voter registration; Driver's license / vehicle registration; Professional licenses; Telephone listings; Religious / club / civic affiliations.  _(TSB-M-09(1)I)_

### 4.3 CA closest-connections test

- **CA closest-connections multi-factor test** — CA uses an open-ended multi-factor analysis ("Corbett v. Franchise Tax Board" line). The FTB applies 20+ factors to determine "closest connections": Amount of time spent in CA vs. elsewhere; Location of spouse and children; Location of principal residence; Location of items of significant value; Location of professionals (doctor, dentist, attorney, accountant); Location of bank/savings accounts; Vehicle registration / driver's license / voter registration; Location of business activities; Membership in social/professional/religious organizations; Where mail is received; ... (FTB Pub. 1031 lists more). CA is famously sticky. The default audit theory is "once a Californian, presumed always a Californian." See Section 13.  _(Corbett v. Franchise Tax Board; FTB Pub. 1031)_

### 4.4 What changes domicile? — the clean break

- **Clean-break domicile checklist** — To win a domicile-change case, the taxpayer should be able to show: Sold (or at least put on the market) the prior-state primary residence; Bought or rented long-term in the new state; Re-registered to vote in the new state; Re-registered vehicles in the new state; Surrendered old-state driver's license and obtained new-state license; Transferred professional licenses (or noted change of address with each board); Closed old-state bank accounts or opened new-state primary account; Joined new-state social/religious/civic organizations; Disenrolled kids from old-state schools and enrolled in new-state schools (or established that kids are independent); Updated addresses on wills, trusts, life insurance, retirement accounts; Filed federal Form 1040 with new-state address; Filed old-state final part-year return with the "moved out" indicator; Filed new-state full-year resident return the first eligible year; Moved family heirlooms, art, important documents, pets; Switched doctors, dentists, financial advisors to new-state professionals; Resigned from old-state country clubs (if any) or converted to non-resident status; Wrote a contemporaneous "declaration of domicile" (FL has a statutory form; not legally binding but persuasive). The more of the above, the stronger the case. Going through HALF the list and stopping is worse than not starting — it suggests indecisiveness on intent.  _(Section 4.4)_

## 5. Part-year residency filing mechanics

### 5.1 The two-return year

- **Two-return filing year mechanics** — In the year of a move, the taxpayer typically files: Federal Form 1040 — single return, full year, with the new-state address (federal doesn't care about state-level moves). Old state — part-year resident return — covers the resident portion of the year; nonresident portion handled either on the same form (most states) or a separate nonresident return. New state — part-year resident return — covers the resident portion of the year. Most states use a combined "part-year/nonresident" form (CA Form 540-NR; NY Form IT-203; NJ Form NJ-1040NR; MA Form 1-NR/PY). The form asks the taxpayer to allocate income to each portion of the year.  _(Section 5.1)_

### 5.2 Allocation methodology

- **Allocation methodology by income type** — Wages and salary: Allocate by workdays in each state during the residency period. For W-2 employees with a single year-round job, the simplest method: (workdays in state during residency period / total workdays in year) × annual wage. For employees who change jobs mid-year, allocate per-job by the actual workdays. Interest and dividends: Allocate by month or by exact date. Pre-move dividends → old state. Post-move dividends → new state. Brokerage 1099-DIV with payment dates is the source document. Capital gains: Allocate by date of realization (sale date), not by holding-period state. Sold stock on June 15 having moved on May 1? Gain is new-state source for residency purposes. BUT: real estate gains are sourced to the property's state regardless of seller's residency (Section 6.4). Self-employment income: Allocate by where the work was performed AND by residency. If a freelancer moves June 1 and continues serving the same out-of-state client, post-move income is new-state-source for residency. See us-sole-prop-bookkeeping and us-schedule-c-and-se-computation for the Schedule C base computation. Pensions, IRA distributions, qualified plans: Federally preempted under §4 USC 114. Taxed only in state of residence at time of payment. Pre-move RMD → old state. Post-move RMD → new state. (Even though the pension was earned in the old state.) Trust distributions: Per beneficiary's residency at time of distribution. BUT: some old states tax the trust ITSELF based on trustor's residency at creation; that's a trust-level issue, not the beneficiary's residency issue.  _(Section 5.2; §4 USC 114)_

### 5.3 Standard deduction and personal exemptions

- **Pro-ration of standard deduction and exemptions** — Most states require the part-year resident to PRO-RATE the standard deduction and personal exemptions by the resident period. CA, NY, NJ apply this. The pro-ration is usually by days resident (e.g., 152/365). Some states (MA, MD) use a different method — the full deduction is allowed but the tax is computed as if the taxpayer were a full-year resident and then pro-rated.  _(Section 5.3)_

### 5.4 Withholding reconciliation

- **Withholding reconciliation for move-year taxpayers** — Year-of-move taxpayers often have withholding from BOTH states (old-state employer continued withholding through the move; new-state employer started withholding mid-year). The two-return filing reconciles: Old state: withholding through move date offset against part-year liability; New state: withholding from move date forward offset against part-year liability. Refund pattern: if old state withheld for the full year but taxpayer moved May 31, old state refunds the post-May withholding. Note. If old-state employer continued withholding after the move because the employee didn't update HR, AND the new state has its own tax, the taxpayer may have a cash-flow problem — old state holds withholding until the return is filed and refunded the following year, but new state may demand quarterly estimated payments. See us-quarterly-estimated-tax.  _(Section 5.4)_

### 5.5 The 6-month "snowbird" pattern

- **Snowbird 6-and-6 pattern requirements** — A common pattern: retiree spends 6 months in FL ("home") and 6 months in NY ("the cottage"). Goal: FL domicile, no NY residency. Required: ≤183 days in NY (count rigorously — every part-day counts); Either no permanent place of abode in NY OR abode held for <11 months (e.g., closed the NY co-op for 2 months in winter); All other domicile factors point to FL. The "I want to be a 6-and-6 snowbird and pay no NY tax" plan FAILS without rigorous day-counting and abode management. Many retirees blow it by spending 184 days (one too many) or by keeping the NY apartment open year-round.  _(Section 5.5)_

## 6. Nonresident income sourcing by income type

For each income type, two questions: 1. Is the income subject to nonresident-state taxation (the "sourcing" question)? 2. If yes, what's the apportionment between resident-state and source-state?

### 6.1 Wages and salary — base rule

- **Nonresident wage allocation formula** — Base rule (most states): wages are sourced to the state where the work is physically performed. A NY-domiciled employee who works from an Atlanta office for two weeks owes GA tax on those two weeks of wages (assuming GA threshold is met, typically $0 or a few days). Allocation formula for nonresidents: Nonresident-state wage = total wage × (days worked in state / total workdays in year). "Workdays" excludes weekends (if not worked), holidays, vacation, sick days. The taxpayer-favorable interpretation excludes any non-working day; the state-favorable interpretation includes weekends if "available for work." De minimis safe harbors (state-by-state): Some states: no withholding/filing required if ≤14-15 days in the state and wages ≤$1,500 (e.g., GA threshold). IL, NY, others: no de minimis — any work in the state triggers tax (subject to reciprocal agreements). Federal "Mobile Workforce State Income Tax Simplification Act" — proposed for years, NOT enacted as of TY 2025.  _(Section 6.1)_

### 6.2 Wages and salary — CONVENIENCE OF THE EMPLOYER RULE (NY, NJ, CT, PA, NE, AR, DE partial)

- **Convenience of the employer rule** — THE BIG EXCEPTION. A handful of aggressive states tax remote-work wages of nonresident employees AS IF the work were performed in the state, unless the remote work is required by the employer for bona fide business reasons (not the employee's mere preference). The states applying it: New York — TSB-M-06(5)I, codified in 20 NYCRR §132.18. Most aggressive. Default rule. New Jersey — adopted in 2023 for nonresidents of NJ working remotely for NJ employers, but only if the home state applies the convenience rule to NJ residents (the "reciprocal convenience rule"). Currently bites NY-resident, NJ-employer remote workers because NY applies the rule to NY-employer/NJ-resident workers. Connecticut — Conn. Gen. Stat. §12-711(b)(2)(C). Adopted 2018, post-COVID expanded. Pennsylvania — applies the rule in limited fashion (PA Rev-419). Nebraska — Neb. Rev. Stat. §77-2733(2). Applies to a NE-based employer's remote nonresident worker. Arkansas — Ark. Code §26-51-202. Delaware — partial application; limited to certain scenarios. The NY convenience rule, in detail. A nonresident employee of a NY-based employer who works from their out-of-state home is treated as performing the work in NY UNLESS: The remote location is a bona fide office of the employer; AND The employer requires the employee to work at the remote location for the employer's business necessity (not the employee's convenience). Factors NY considers in the "bona fide employer office" test (TSB-M-06(5)I): Does the employer have a NY office available for the employee? Does the employee have an established work pattern at the remote location? Is the remote location used for client visits, business calls? Does the employer reimburse the employee for the remote office expenses? Does the employer's business have a bona fide reason for the employee to work at the remote location (e.g., the employee covers a sales territory near the remote location)? Pre-2017 "secondary factors": items like "the work is the kind of work that requires a special environment that NY office can't provide" used to soften the rule. NY tightened these post-2017. COVID exception. NY granted a temporary safe harbor for employees who worked remotely DUE to government-mandated COVID restrictions — those days were treated as NY-source. The safe harbor expired in 2022. From 2023 forward, the standard convenience rule applies in full force. Practical consequences: A NY-employer's TX-resident remote worker: 100% NY-source unless employer's business requires TX location. A NY-employer's NJ-resident commuter who started working from home in 2023: NY-source on the home-office days too, unless employer requires NJ home location. A NY-resident who moved to FL on June 1 but kept the NY job: post-move wages still NY-source unless employer requires FL location. A CA-resident remote worker for a NY employer: 100% NY-source (because of convenience rule) AND 100% CA-source (because CA-resident worldwide tax). The CA-NY resident credit (Section 10) does NOT eliminate the double tax in the worst case — CA only gives credit for the CA-source portion of the NY tax. Reciprocal convenience. NJ in 2023 enacted N.J.S.A. 54A:5-1 to apply the convenience rule to NY-resident employees of NJ-based employers, but ONLY if NY applies the convenience rule to NJ-resident employees of NY-based employers (which it does). This creates symmetric audit risk. AUDIT FLASH POINT. Remote workers for NY employers who moved to no-tax states (FL, TX, TN, WA, NV, NH, SD, AK) thinking they'd save NY tax — they often haven't. NY DTF actively audits convenience-rule cases. The remote worker owes 100% NY tax on wages AND no resident credit because the new state has no tax to credit against.  _(TSB-M-06(5)I; 20 NYCRR §132.18; Conn. Gen. Stat. §12-711(b)(2)(C); PA Rev-419; Neb. Rev. Stat. §77-2733(2); Ark. Code §26-51-202; N.J.S.A. 54A:5-1)_

### 6.3 Reciprocal-agreement states (the workaround)

**Major reciprocal agreements (as of 2025)**  _(Section 6.3)_

| Resident state ↔ Work state |
| --- |
| NJ ↔ PA |
| OH ↔ IN, KY, MI, PA, WV |
| KY ↔ IL, IN, MI, OH, VA, WV, WI |
| MI ↔ IL, IN, KY, MN, OH, WI |
| PA ↔ IN, MD, NJ, OH, VA, WV |
| VA ↔ DC, KY, MD, PA, WV |
| WV ↔ KY, MD, OH, PA, VA |
| WI ↔ IL, IN, KY, MI |
| DC ↔ All other states (DC has the broadest reciprocal — DC nonresidents who work in DC pay no DC tax) |
| MD ↔ DC, PA, VA, WV |
| IL ↔ IA, KY, MI, WI |
| MN ↔ MI, ND |
| ND ↔ MN, MT |
| MT ↔ ND |
| IN ↔ KY, MI, OH, PA, WI |
| IA ↔ IL |

### 6.3 Reciprocal-agreement states (the workaround)

- **Notable absences and reciprocal withholding election forms** — Notable absences: NY has NO reciprocal agreement with NJ, CT, PA, or any other state. CA has NO reciprocal with any state. Employee form to elect reciprocal withholding: PA: REV-419; NJ: NJ-165; OH: IT-4NR; MI: MI-W4; KY: 42A809; Various others — check state. If the employee doesn't file the reciprocal form, the work-state employer withholds; the employee gets a refund by filing a work-state nonresident return claiming exemption under reciprocity.  _(Section 6.3)_

### 6.4 Capital gains and other intangibles

- **Capital gains sourcing rules and exceptions** — General rule: intangibles (publicly traded stock, mutual funds, bonds, money market funds, cryptocurrency under most state interpretations) follow the domicile of the owner. Only the domiciliary state taxes intangible gains. Exception 1 — real estate. Capital gains on real estate are sourced to the state where the real estate is located, regardless of the seller's domicile. A FL-resident selling a NY condo owes NY nonresident tax on the gain. Exception 2 — partnership/S-corp interests where the entity's assets are predominantly state-real-estate. Some states (CA most aggressively) treat the sale of a partnership interest as a sale of the underlying assets — if those assets include state-located real estate, gain is sourced to that state. See us-pte-state-matrix. Exception 3 — installment sales straddling a move. Pre-move installments are sourced to old state; post-move installments to new state. But some states (CA Revenue and Taxation Code §17952.5) apply a "look-back" rule: gain originally sourced to CA remains CA-source even if the installments are paid to a nonresident. Aggressive. Exception 4 — partnership distributions. A nonresident partner's distributive share of partnership income is sourced based on the partnership's apportionment (UDITPA factors). A NY-resident partner in a CA partnership has CA-source income on the CA-apportioned share.  _(CA Revenue and Taxation Code §17952.5)_

### 6.5 Interest and dividends

- **Interest and dividends sourcing** — Intangibles rule: domicile of the recipient governs. Exception: NY has historically attempted (and the courts have shut down) to source interest on a NY brokerage account to NY for a nonresident; that fails. Sourcing follows domicile.  _(Section 6.5)_

### 6.6 Rental real estate income

- **Rental real estate income sourcing** — Rule: sourced to the state where the property is located. A FL-resident with a NY rental owes NY nonresident tax on NY-source rental income; the NY tax is creditable on the FL return — except FL has no PIT, so no credit needed. Allocation of expenses: direct expenses allocated to the property's state. Indirect/overhead expenses allocated by property location. Depreciation recapture on sale: sourced to state where property located. Same as gain.  _(Section 6.6)_

### 6.7 K-1 income from pass-through entities

- **K-1 income sourcing rules** — K-1 income (partnership Schedule K-1, S-corp Schedule K-1) is sourced based on: The entity's APPORTIONMENT factors (sales, payroll, property within the state divided by everywhere); AND The partner/shareholder's residency. A nonresident partner's distributive share is taxable in the state to the extent of the state's apportionment of the entity's income. Beyond scope of this skill; see us-pte-state-matrix and us-form-1065-partnership. Many states require nonresident partners to file (no de minimis). Some states (CA, NY, OR, ND) allow composite returns or PTE tax elections (the "SALT cap workaround" enacted post-TCJA). See us-pte-state-matrix.  _(Section 6.7)_

### 6.8 Self-employment income / Schedule C

- **Self-employment income sourcing** — Rule: sourced to the state where the work is performed (most states). A few states (NY in some interpretations) source self-employment income to the state where the business is "based" — if the business has a fixed office. For a fully remote freelancer with no office: The freelancer's state of residence is also the state where work is performed → both source rules give the same answer. The freelancer who travels to client sites: per-day allocation by client-site state. Convenience rule does NOT apply to self-employment income — the convenience rule is a wage-employment rule. A self-employed person remote in TX serving NY clients owes NO NY tax on the SE income (assuming no NY office, no NY workdays). Schedule SE tax (federal, see us-schedule-c-and-se-computation) is unaffected by state issues.  _(Section 6.8)_

### 6.9 Retirement income — §4 USC 114 federal preemption

- **§4 USC 114 federal preemption of pension source taxation** — The federal preemption rule: 4 U.S.C. §114 ("Pension Source Tax Act of 1996," P.L. 104-95) bars any state from taxing the retirement income of a nonresident of that state. "Retirement income" means: Qualified plan distributions (401(k), 403(b), 457(b)); Traditional IRA, Roth IRA distributions; Defined-benefit pension distributions; Substantially equal periodic payments under §72(t); Excess pension benefits; Certain nonqualified deferred compensation under §457(f) (with conditions); IRC §3121(v)(2)(C) "specified plan" distributions paid in substantially equal periodic payments over the life expectancy of the recipient OR for a period of 10 years or more. What §4 USC 114 protects: Even if a taxpayer earned a pension while a NY resident and then moves to FL, NY may NOT tax the pension when paid. The only state that may tax the pension is the state of residence at the time of receipt. This is true even if the pension is paid by a NY employer. Important nonqualified deferred comp exception: §457(f) "top-hat" plan distributions and other nonqualified deferred comp paid in LUMP SUMS (not substantially equal periodic payments) are NOT protected. The old state CAN tax them. Many golden-parachute payments, severance lump sums, and §409A nonqualified deferred comp lump sums are NOT preempted and remain old-state-source. Practical advice for retirees: convert lump-sum nonqualified deferred comp to substantially equal periodic payments of 10+ years before retiring/moving, where the plan permits, to bring the payments within §4 USC 114 protection.  _(4 U.S.C. §114 (Pension Source Tax Act of 1996, P.L. 104-95); IRC §3121(v)(2)(C); §72(t); §457(f))_

### 6.10 Stock options, RSU, ESPP — separate Section 7

See Section 7 for the equity-comp deep dive.

## 7. Equity compensation allocation — the multi-state deep dive

Equity compensation is the single most error-prone area of multi-state allocation, and the area state auditors (especially CA FTB and NY DTF) most frequently challenge. Get this section right.

### 7.1 Non-qualified stock options (NQSO)

- **NQSO state sourcing formula and example** — Federal treatment (refresher): ordinary income at exercise = (FMV at exercise − exercise price) × shares. Reported on Form W-2 box 1 (employer reports) or 1099-NEC (consultant). State sourcing rule: the ordinary-income portion is allocated based on workdays in each state during the period from GRANT to EXERCISE. Formula: State-A source = exercise-spread × (workdays in state A from grant to exercise / total workdays from grant to exercise). Example: NQSO granted 1/1/2020 while CA resident. 100% vest 1/1/2024 (4 years). Exercised 6/1/2025 while TX resident (moved 7/1/2024). Grant-to-exercise period: 1/1/2020 to 6/1/2025 ≈ 1,400 workdays. CA workdays: 1/1/2020 to 7/1/2024 ≈ 1,150 workdays. TX workdays: 7/1/2024 to 6/1/2025 ≈ 250 workdays. CA-source = $100,000 spread × 1,150/1,400 = $82,143. TX-source = $100,000 × 250/1,400 = $17,857 (TX has no PIT, so no TX tax). Key authorities: IRS Notice 2002-47 (provides federal framework for source treatment by reference to the workday method); CA FTB Publication 1004 (CA's NQSO sourcing guidance); NY TSB-M-95(3)I and Matter of Stuckless (sourcing of options); Matter of Reilly (NY 2010 — option sourcing methodology). Common error: sourcing the ENTIRE NQSO ordinary income to the state of residence at exercise. This is WRONG. CA, NY, and most states require workday allocation across the grant-to-exercise period.  _(IRS Notice 2002-47; CA FTB Publication 1004; NY TSB-M-95(3)I; Matter of Stuckless; Matter of Reilly (NY 2010))_

### 7.2 Incentive stock options (ISO)

- **ISO state sourcing rules** — Federal treatment: generally no ordinary income at exercise (AMT preference instead). Capital gain (or ordinary income on disqualifying disposition) at sale. State sourcing: AMT spread at exercise (incentive stock): some states (CA) treat AMT preferences as resident state's preference only, no allocation. But check each state. Disqualifying disposition (ordinary income at sale): the ordinary-income portion is allocated by workdays in each state from grant to exercise (same as NQSO). The capital gain portion (excess of sale price over FMV at exercise) is sourced as a regular capital gain — intangibles follow domicile.  _(Section 7.2)_

### 7.3 Restricted stock units (RSU)

- **RSU state sourcing formula and example** — Federal treatment: ordinary income at VESTING = FMV at vest × shares vesting. Reported on W-2 box 1. State sourcing: allocated based on workdays in each state from GRANT to VEST. Formula: State-A source = vest FMV × (workdays in state A from grant to vest / total workdays from grant to vest). Example: RSU granted 1/1/2022 to a CA resident, 4-year cliff/quarterly vest. Q1 2025 vest of $200,000 (1/16 of total grant). Taxpayer moved to TX on 7/1/2024. Grant-to-vest period for the Q1 2025 vest: 1/1/2022 to 3/31/2025 ≈ 845 workdays. CA workdays: 1/1/2022 to 7/1/2024 ≈ 650 workdays. TX workdays: 7/1/2024 to 3/31/2025 ≈ 195 workdays. CA-source for this Q1 2025 vest = $200,000 × 650/845 = $153,846. TX-source = $200,000 × 195/845 = $46,154 (no TX PIT). This calculation is REPEATED FOR EVERY VEST DATE. A 4-year quarterly-vesting RSU grant has 16 separate allocations, each with a different grant-to-vest period. Practical: spreadsheet every vest event. CA FTB will request the workpapers in audit. Common error: sourcing the entire RSU income at vest to the resident state at vest. WRONG for CA, NY, MA, IL, and most states. Only TX, FL, NH, NV, SD, TN, WA, WY are agnostic (no PIT) — but the old state still taxes its allocable share.  _(Section 7.3)_

### 7.4 Employee stock purchase plan (ESPP) — §423 qualified

- **ESPP federal and state treatment** — Federal treatment: Qualifying disposition (held 2 yrs from grant, 1 yr from purchase): ordinary income = lesser of (a) actual discount, (b) discount based on offering-date price; capital gain on the rest. Disqualifying disposition: ordinary income = (FMV at purchase − purchase price) × shares; capital gain on the rest. State sourcing: Ordinary income portion (the discount): allocated by workdays in each state during the OFFERING PERIOD (the 6-month or 24-month look-back period during which contributions are made). Capital gain portion: domicile of seller at time of sale (intangibles).  _(IRC §423; Section 7.4)_

### 7.5 Restricted stock (§83(b) election)

- **§83(b) election sourcing** — Federal: taxpayer elects to include FMV at grant in income (forfeiting future capital gains conversion if forfeited). State: sourced to state of residence/work at the time of the §83(b) election (because that's when ordinary income is recognized).  _(IRC §83(b))_

### 7.6 Stock appreciation rights (SAR)

- **SAR sourcing treatment** — Treated like NQSO. Workday allocation from grant to exercise.  _(Section 7.6)_

### 7.7 Phantom stock / deferred cash bonus

- **Phantom stock and deferred cash bonus sourcing** — If paid in lump sum at vest/exercise: sourced to where work was performed during the deferral period (workday allocation, similar to NQSO/RSU). If paid in substantially equal periodic payments over 10+ years: potentially within §4 USC 114 retirement income preemption — only state of residence at payment can tax. See Section 6.9.  _(§4 USC 114)_

### 7.8 Carried interest

- **Carried interest sourcing** — Carried interest from a fund partnership: typically the partnership has an "office" or "principal place of business" in a particular state. The fund partner's distributive share is sourced based on the partnership's apportionment. Most fund managers' carried interest is sourced primarily to where the management activity occurs (NY for most hedge funds; CA for many VC funds). The K-1 will show state-apportioned amounts. A NY-based PE fund's partner who relocates to FL still has NY-source carried interest because the fund's management activity is in NY. Federal §1061 three-year holding rule does NOT change state sourcing.  _(IRC §1061)_

### 7.9 Severance, golden parachute, signing bonus

- **Severance and bonus sourcing** — Severance: sourced to where the underlying services were performed. Workday allocation over the service period. Golden parachute (§280G): sourced to where services were performed during the relevant pre-CIC period. Signing bonus paid before start of work: sourced to where the employee resides at time of payment (no service yet performed) — but some states (NY) source to where the employer is located if the bonus is for future NY work.  _(IRC §280G)_

### 7.10 Recordkeeping for equity comp

- **Equity comp recordkeeping requirements** — For every multi-state taxpayer with equity comp: Grant date, vest date, exercise date for every grant; FMV at each event; Days in each state during each relevant period; Per-grant workpaper showing the allocation. This is more recordkeeping than most taxpayers maintain. The reviewer should request the employer's stock-plan statements (E*TRADE / Schwab / Shareworks/Morgan Stanley) and reconcile to W-2 box 1 amounts.  _(Section 7.10)_

## 8. Convenience-of-the-employer rule deep dive (referenced from §6.2)

Most-cited examples to think through:

### 8.1 NY-employer + remote worker in TX

- **NY employer TX remote worker example** — NY-resident moved to TX 1/1/2025; continued working for NY employer fully remote. Federal: TX residence, no state tax. NY: 100% NY-source under convenience rule (employer in NY; remote location for employee's convenience, not employer's bona fide business need). TX: no PIT. Result: 100% NY tax on all 2025 wages. No resident credit available (TX has no PIT to credit). Net: same as if still NY resident. To escape the convenience rule: employee must establish a "bona fide employer office" in TX. Factors: Employer leases or owns TX space available to employee; Employee meets clients in TX or works on TX-specific business; Employer requires the TX location for legitimate business reasons. Mere "the employee asked to relocate" doesn't qualify.  _(Section 8.1)_

### 8.2 NY-employer + nonresident commuter

- **NY employer NJ commuter example** — NJ-resident commutes daily to NYC office, starting 2023 works from NJ home 2 days/week, NYC office 3 days/week. NY: 100% NY-source under convenience rule (because the NJ home days are for employee's convenience). NJ: NJ-resident worldwide tax. Resident credit for the NY tax paid. The 2-day-home days are double-taxed for NJ purposes via the convenience rule, but the NJ resident credit kicks in. Note NJ in 2023 also adopted reciprocal convenience — but only against states that apply convenience to NJ residents. So NY-resident, NJ-employer commuter has the symmetric problem.  _(Section 8.2)_

### 8.3 CA-resident + NY-employer remote

- **CA resident NY employer remote worker example** — CA-resident works fully remotely from CA for NY-employer. NY: 100% NY-source under convenience rule (employer in NY). CA: 100% CA-resident worldwide tax. Resident credit: CA gives credit on its CA tax for the NY tax paid on the doubly-taxed income, BUT only up to the CA rate. If NY tax exceeds CA tax on that income, the excess is NOT refundable. Net effective rate: roughly max(CA rate, NY rate) on the wages. This is the worst outcome — full double tax. The CA-NY combination is the highest practical effective rate in the US (13.3%+ CA + ~10.9% NY = could approach 24% on top-bracket wages but resident credit caps at ~13.3%).  _(Section 8.3)_

### 8.4 NY-employer + employee works at remote conference for one day

- **NY employer one-day conference example** — A NJ-resident NY-employer-employee attends a 1-day conference in Chicago. NY: still 100% NY-source under convenience rule (one-off travel for the employee's job is not a bona fide employer office in Chicago). IL: arguably 1 day IL-source for nonresident if IL nonresident filing threshold is met; in practice, employer doesn't withhold for 1 day and most taxpayers don't file. Practical: NY tax 100%; ignore IL.  _(Section 8.4)_

## 9. §4 USC 114 — pension source tax preemption

Brief recap from §6.9 with practical application:

## 9. §4 USC 114 — pension source tax preemption

- **Federal law and retirement income definition** — Federal law: 4 U.S.C. §114(a): "No State may impose an income tax on any retirement income of an individual who is not a resident or domiciliary of such State." "Retirement income" defined in §114(b): 1. Distributions from qualified plans under §401(a) (pension, profit-sharing, 401(k)); 2. Distributions from §403(a) annuities; 3. Distributions from §403(b) plans; 4. Distributions from IRAs (Traditional and Roth); 5. Distributions from §408(p) SIMPLE IRA; 6. Distributions from §457(b) governmental plans; 7. Income from §3121(v)(2)(C) "non-qualified deferred compensation plans" IF either (a) such income is part of a series of substantially equal periodic payments over the life of the recipient OR over a period of not less than 10 years, OR (b) the income is a distribution after termination of employment and is paid as part of a plan that maintains an excess benefit plan.  _(4 U.S.C. §114(a); 4 U.S.C. §114(b))_

## 9. §4 USC 114 — pension source tax preemption

- **Items not covered by §4 USC 114 preemption** — Not covered (state can still tax if old-state-source): Lump-sum nonqualified deferred comp under §409A or §457(f) when paid in less than 10 years; Stock options exercised after move (those are NOT retirement income — sourced under Section 7); RSUs vested after move (NOT retirement income); Severance paid post-move (NOT retirement income — see §7.9); Bonuses paid post-move for pre-move work (NOT retirement income).  _(§409A; §457(f))_

## 9. §4 USC 114 — pension source tax preemption

- **Practical advice on relocation for retirement income** — For a high-earning executive nearing retirement who plans to move from NY to FL: Time the move BEFORE collecting any nonqualified deferred comp lump sum (NY taxes it because not §4 USC 114 protected) OR Restructure the deferred comp into a 10-year+ series of substantially equal periodic payments to bring within §4 USC 114 protection (requires plan amendment and §409A compliance). For a typical retiree who has only IRA and 401(k) distributions: §4 USC 114 protects everything. Old state cannot tax IRA RMDs after the move. New state taxes them at new-state's rates only.  _(4 U.S.C. §114; §409A)_

## 10. Resident credit for taxes paid to other states

### 10.1 Mechanics

- **Resident credit mechanics and formula** — When a taxpayer is resident in state A and earns income sourced to state B: State A: taxes worldwide income (100%); State B: taxes only the B-source income (nonresident return); State A: provides a CREDIT for the tax paid to State B on the doubly-taxed income. Formula (typical): Resident credit = lesser of: (a) tax actually paid to State B on the doubly-taxed income, OR (b) State A's tax on the doubly-taxed income at State A's rates. The "lesser of" rule means: if State B's rate exceeds State A's rate, the excess is NOT refundable. The taxpayer is in the position of being taxed at the higher of the two rates. Forms: CA: Schedule S (Other State Tax Credit). Limited to CA rate × CA AGI portion. Strict sourcing rules. NY: Form IT-112-R (Resident Credit). Limited to NY rate × NY AGI portion. NJ: Schedule NJ-COJ. Limited. Various other states: each has its own form.  _(Section 10.1)_

### 10.2 Limitations

- **Resident credit limitations** — Only for income, not other taxes: the credit is for the other state's income tax only. Not property tax, sales tax, license fees, franchise tax. Only for state tax, not local tax: NYC personal income tax (an NYC-only tax) may not be creditable in some states. CA does not credit NYC tax against CA tax (CA only credits NY State tax). Only for tax actually paid: estimated payments and withholding count if applied; refunded amounts do not. No "circular" credit: if both states are claiming you as resident, only one will give a resident credit (typically the state where you're a STATUTORY resident, not domiciliary resident, gives the credit — the credit follows the secondary residency).  _(Section 10.2)_

### 10.3 The §901 analogy

Resident credit is analogous to the foreign tax credit under §901 — same logic, same "highest-rate-wins" outcome. See us-foreign-tax-credit-1116.

### 10.4 Dual-residency credit allocation

- **Dual-residency credit allocation examples** — When a taxpayer is resident of state A (domiciliary) AND state B (statutory), which state gives the credit? NY rule (and most): the STATUTORY resident state gives the credit for income from other states. The domiciliary state taxes worldwide income with credit only for income earned in true source states. The interaction: a FL-domiciled / NY statutory resident with CA-source wages: CA: taxes the CA-source wages (nonresident). NY: taxes worldwide (statutory resident); credit for CA tax paid. FL: no PIT. A NY-domiciled / NJ statutory resident with CA-source wages: CA: taxes the CA-source wages. NJ: taxes worldwide (statutory resident); credit for CA tax. NY: taxes worldwide (domiciliary); credit for both CA tax AND NJ tax on the worldwide income. The mechanics are state-specific; consult each state's resident-credit form.  _(Section 10.4)_

### 10.5 Reciprocal-state interaction

- **Reciprocal-state credit interaction** — If two states have a reciprocal agreement, NO nonresident return in the work state, NO resident credit needed. The home state simply taxes 100%. See §6.3.  _(Section 10.5)_

## 11. Telework / remote work post-COVID

### 11.1 The COVID safe harbors expired

- **COVID safe harbor expiration** — During 2020-2021, many states (MA, NJ, GA, IN, MS, MD, NY in limited form) granted "temporary safe harbors" — remote workers who were normally working in state X but were working remotely from state Y due to COVID restrictions were treated as if still working in state X. By 2022-2023, most safe harbors expired. The current rule across most states: PHYSICAL PRESENCE GOVERNS. Where the work is actually performed (employee's keyboard) determines sourcing.  _(Section 11.1)_

### 11.2 Exception: convenience-rule states

NY, NJ, CT, PA, NE, AR, DE — the convenience rule continues to apply. See §6.2 and Section 8.

### 11.3 State income-tax nexus for employers

- **Employer nexus consequences of remote employees** — A remote employee working in state X (where the employer has no other presence) may create: Withholding obligation for state X on the employee's wages (state X is the work-state). Income tax nexus for the employer in state X (creating a corporate state tax filing obligation). Sales tax nexus in state X (if the remote employee solicits sales). UI tax obligation in state X. This is a HR / employer-level issue, not the employee's residency issue. Flag to the employer if the employee is the only employee in state X.  _(Section 11.3)_

### 11.4 Practical recommendations for clients

- **Practical recommendations for remote-work clients** — For a remote-work client moving across state lines: 1. Update employer HR with the new home address; 2. Employer should reissue W-4 and state withholding form; 3. Employer should adjust withholding to reflect the new work state (if no convenience rule); 4. Employee should also make quarterly estimated payments to the new state in case of under-withholding (see us-quarterly-estimated-tax); 5. Watch for old-state convenience rule — if old employer is NY/NJ/CT/PA/NE/AR/DE-based, the wages may still be source-state taxed.  _(Section 11.4)_

## 12. Aggressive-audit states

The states that audit residency aggressively, in rough order:

## 12. Aggressive-audit states

- **Ranked list of aggressive-audit states** — 1. New York — the gold standard for aggressive residency audits. Dedicated Residency Audit Unit. Subpoenas cell tower records, EZ-Pass, credit cards, doorman logs. Detailed published guidance (TSB-M, Audit Guidelines). Average audit takes 2-3 years. 2. California — pursues ex-residents for 5+ years post-move. Closest-connections test is open-ended. FTB does not concede easily. See Section 13. 3. New Jersey — Division of Taxation pursues both domicile and statutory residency. Convenience rule (reciprocal) bites NY commuters. 4. Massachusetts — DOR aggressive on Boston tech workers and Cape Cod retirees claiming FL domicile. 5. Minnesota — DOR aggressive (the "Wynne" line of cases — Comptroller v. Wynne). 6. Illinois — Department of Revenue aggressive in part because the 9-month statutory residency rule is unique. 7. Maryland — pursued the Wynne case to the Supreme Court; aggressive on resident credits. 8. Connecticut — DRS aggressive but smaller volume than NY. 9. DC — aggressive on DC commuters who claim DC residency but actually live in MD/VA. 10. Oregon — aggressive on resident credit limitations. Less aggressive (but still audit): GA, NC, VA, WI, OH, PA, MI. No PIT (no residency audit risk): TX, FL, TN, NH, WA, WY, SD, AK, NV — but the OLD state still pursues you.  _(Comptroller v. Wynne)_

## 12. Aggressive-audit states

- **Risk-stratification of state-to-state moves** — Risk-stratification: Moving FROM aggressive state (NY/CA/NJ/MA/MN) TO no-PIT state (FL/TX/etc.): HIGH audit risk. Plan and document the move thoroughly. Moving FROM no-PIT state TO any state: low risk (the no-PIT state doesn't care). Moving BETWEEN PIT states: medium risk, both states care.  _(Section 12)_

## 13. California "Sun West" / closest-connections traps

CA deserves a dedicated section because of its unique aggressiveness and the "9 months and a day" myth.

### 13.1 The 9-month presumption (R&TC §17014)

- **9-month presumption** — CA has a presumption that an individual who spends >9 months in CA during a tax year IS a CA resident. This is a presumption — rebuttable but the burden is on the taxpayer to overcome. This is NOT a "stay <9 months and you're a nonresident" rule. The closest-connections test still applies even if you spend <9 months. A CA-domiciled person who travels for 4 months but maintains the CA primary residence, family, business, etc., is STILL a CA resident — the 9-month rule does not bar that. The 9-month presumption is a one-way ratchet against the taxpayer, not a safe harbor.  _(R&TC §17014)_

### 13.2 The "Sun West" / "California-flavored" snowbird

A common pattern: high-earner sells CA business or vests significant equity, plans to take a "tax-free year" in NV or TX before the liquidity event, then return. CA FTB pursues these aggressively under the closest-connections test:
- Maintains CA family home → CA-resident.
- Maintains CA professional license, doctor, bank → CA-resident.
- Returns to CA after the event → presumption that you never left.

The "safe harbor" under R&TC §17014(d) — an absence of >546 days for employment-related reasons — gives some protection if the taxpayer leaves for at least 18 months for an employment-related purpose and has minimal CA contacts during the absence. But this is narrow.

### 13.3 CA "safe harbor" employment-related absence

- **CA employment-related absence safe harbor** — R&TC §17014(d): a CA-domiciled person is treated as a NONRESIDENT for the period of absence IF: (a) The absence is for an uninterrupted period of at least 546 consecutive days for employment-related purposes; (b) During the absence, the spouse and minor children also are absent for the same period (with limited exceptions); (c) Intangible income during the absence does not exceed $200,000/year (this is RIGOROUS — most equity-event clients exceed this); AND (d) The absence is not principally for the purpose of avoiding California tax. If ALL conditions are met → CA treats the person as nonresident during the absence. If any condition fails → CA resident throughout.  _(Cal. Rev. & Tax. Code §17014(d))_
- **CA safe harbor intangible income limit** — 200,000 USD/year (The $200,000 intangibles limit is the killer. Anyone with significant stock holdings will exceed this.)  _(Cal. Rev. & Tax. Code §17014(d))_

### 13.4 CA's pursuit of equity-comp deferral

CA aggressively sources stock-option and RSU income that vests AFTER a CA-to-other-state move under the workday allocation rule (see Section 7). FTB will request:
- Complete employment history with dates and locations;
- Grant statements for every equity grant;
- Vest schedules and exercise dates;
- Workday calendar for the entire grant-to-exercise (or grant-to-vest) period.

The FTB has special-purpose audit teams for equity-comp sourcing.

### 13.5 AUDIT FLASH POINT — CA tech equity-event audits

A CA-resident software engineer or executive who has a $5M+ vest, then moves to TX a year before vest, expecting the entire $5M to be TX-source: WRONG. CA will source by grant-to-vest workdays. Typically 60-90% remains CA-source. Plan years in advance — the move should happen as early in the vesting period as possible to minimize CA workdays in the allocation.

## 14. Famous cases — read these before signing a residency position

### 14.1 Matter of Gaied v. New York State Tax Appeals Tribunal, 22 N.Y.3d 592 (2014)

- **Gaied case** — Facts: John Gaied was a domiciliary of NJ. He purchased a building in NY where his elderly parents lived. He paid the utilities and helped his parents with rent. He had a key to the building. NY argued statutory residency: permanent place of abode in NY + 183+ days in NY (he was over because of NJ-NY commute). Holding: NOT a statutory resident. The NY Court of Appeals held that "permanent place of abode" requires that the taxpayer HIMSELF use the dwelling as his residence. Mere ownership or financial support of a relative's residence is not enough. The taxpayer must USE the abode personally. Implication: an apartment OWNED by the taxpayer but rented out, OR a relative's home where the taxpayer occasionally stays, may not be a "permanent place of abode" — but this is fact-intensive. Don't rely on Gaied without strong facts.  _(Matter of Gaied v. NY State Tax Appeals Tribunal, 22 N.Y.3d 592 (2014))_

### 14.2 Matter of Patrick (NY 2009)

- **Patrick case** — Day-count case. Taxpayer kept careful records but NY proved through credit card and toll records that the diary was wrong on multiple days. Result: statutory residency upheld. Implication: the diary defense is necessary but not sufficient. Contemporaneous corroborating evidence (credit cards, EZ-Pass) is essential.  _(Matter of Patrick, NY Div. of Tax App. (2009))_

### 14.3 Matter of Sobotka (NY 2014)

- **Sobotka case** — Day-count case + bona fide employer office. Held: a New York-based employer's NJ home office did not qualify as a bona fide employer office; convenience rule applied; all home-office wages were NY-source. Implication: the convenience rule is hard to escape.  _(Matter of Sobotka, NY Div. of Tax App. (2014))_

### 14.4 Matter of Reilly (NY 2010)

- **Reilly case** — Stock option sourcing case. Established the workday-allocation method for NQSO sourcing in NY.  _(Matter of Reilly, NY Div. of Tax App. (2010))_

### 14.5 Matter of Stuckless (NY 2015)

- **Stuckless case** — Held that a NY-domiciled employee's NQSO grant-to-exercise period must be sourced to NY for the period of NY work, even if exercised after move.  _(Matter of Stuckless, NY Div. of Tax App. (2015))_

### 14.6 Hellerstein v. Assessment Bd. (NJ)

- **Hellerstein case** — Established the NJ statutory residency test parallel to NY.

### 14.7 Comptroller v. Wynne, 575 U.S. 542 (2015)

- **Wynne case** — US Supreme Court held that Maryland's failure to grant a full resident credit for taxes paid to other states violated the dormant Commerce Clause. Effect: MD had to expand its resident credit. Broader implication: double taxation by states without resident credit may be unconstitutional, but courts have not extended Wynne broadly.  _(Comptroller v. Wynne, 575 U.S. 542 (2015))_

### 14.8 Bindley v. Franchise Tax Board (CA Court of Appeal, 2024)

- **Bindley case** — CA case. Held that intangible income (royalties received by an out-of-state resident from CA-source IP) can be sourced to CA. Aggressive CA position; not yet followed nationally.  _(Bindley v. Franchise Tax Board, Cal. Ct. App. (2024))_

### 14.9 Buehler v. Franchise Tax Board (CA, various)

- **Buehler case** — Closest-connections test applied; FTB prevailed on residency despite taxpayer's effort to relocate to NV.

### 14.10 In re Estate of Edith Windsor (federal, but residency relevant)

- **Windsor estate case** — Tangentially relevant for cross-state estate issues.

### 14.11 Matter of Zelinsky v. Tax Appeals Tribunal, 1 N.Y.3d 85 (2003)

- **Zelinsky case** — Cardozo Law professor (CT resident) challenged NY's convenience rule on Commerce Clause and Due Process grounds. NY Court of Appeals upheld the convenience rule. Cert. denied by US Supreme Court. Implication: the convenience rule has survived constitutional challenge in NY. Federal solution (Mobile Workforce Act) is the only way to abolish it, and it remains unpassed.  _(Matter of Zelinsky v. Tax Appeals Tribunal, 1 N.Y.3d 85 (2003))_

## 15. Moving-day planning checklist

When advising a client planning a state-to-state move, use this checklist:

### 15.1 Pre-move (60-180 days before)

- [ ] Identify aggressive-audit state risk profile (Section 12);
- [ ] Determine clean break vs. partial break feasibility;
- [ ] Make a list of all old-state ties to sever;
- [ ] Project tax impact of move year (part-year, statutory residency risk);
- [ ] Equity comp analysis: project vest dates, grant-to-vest sourcing if relevant (Section 7);
- [ ] Consider acceleration or deferral of recognition events:
   - Accelerate RSU vests (rarely possible) to old state if rate is lower;
   - Defer Roth conversion to new state if rate is lower;
   - Defer pension lump sums or restructure to §4 USC 114 covered form;
   - Defer real estate sale gains;
- [ ] Begin "intent" paper trail: declarations of domicile, lease/purchase in new state.

### 15.2 At move

- [ ] Move physical residence (truck on a date);
- [ ] Update federal W-4 and state withholding form with employer;
- [ ] Update mailing address for all financial accounts;
- [ ] Surrender old driver's license; obtain new state license within 30 days;
- [ ] Re-register vehicles;
- [ ] Re-register to vote;
- [ ] Begin daily location log;
- [ ] Open new-state primary bank account;
- [ ] Update will, trust, durable POA to reference new state;
- [ ] Update beneficiary designations and address on retirement accounts.

### 15.3 Within 90 days of move

- [ ] Resign / convert membership in old-state clubs, religious, professional organizations;
- [ ] Transfer doctors, dentists, attorneys, CPA;
- [ ] Transfer kids' school enrollment;
- [ ] Move "items near and dear" (heirlooms, art, important documents);
- [ ] Sell or rent out (preferably sell) the old primary residence;
- [ ] Update professional licenses;
- [ ] Update emergency contacts;
- [ ] File any state-specific declarations (e.g., FL Declaration of Domicile, recorded in county).

### 15.4 First year after move

- [ ] File old state part-year resident return (final);
- [ ] File new state part-year resident return;
- [ ] File federal 1040 with new-state address;
- [ ] Keep cell tower / credit card / EZ-Pass records for old state (3-7 years statute of limitations);
- [ ] Limit time in old state to <30 days if possible (no statutory-residency risk even with old abode);
- [ ] If old abode retained, ensure no >183 days and limit total to <11 months in the resident year if abode kept.

### 15.5 Years 2-5 after move

- [ ] Continue daily location log;
- [ ] Continue limiting old-state days;
- [ ] File new state full-year resident returns;
- [ ] No old-state filing needed unless old-state-source income (rental, partnership);
- [ ] Audit response: be ready to produce 5+ years of evidence.

## 16. Worked Example 1 — NY-to-FL move + statutory residency risk

### 16.1 Facts

- Taxpayer: Janet, age 58, NY State and NYC domiciliary through May 31, 2025.
- Employment: VP at NYC-based law firm. W-2 wages $400,000 (annual).
- Move: Bought FL home in February 2025. Moved permanently to FL on June 1, 2025. Sold NYC apartment? NO — kept it for "trips back" to see daughter at NYU.
- NY days post-move: Visited daughter 60 days July-Dec; weddings/work meetings 30 days; family events 15 days. Total post-move NY days = 105.
- Pre-move NY days: January-May = 152 days (she was there all the time except weekends in CT).
- Total 2025 NY days: 152 + 105 = 257 days.
- NY abode: kept the NYC co-op all year, used by Janet and family. "Maintained for substantially all the year" — YES.

### 16.2 Analysis

Domicile: Janet successfully changed domicile to FL on June 1, 2025 (assuming she did the checklist properly — license, voter registration, etc.). Confirmed.

BUT — statutory residency:
- Permanent place of abode in NY: YES (the NYC co-op, maintained substantially all year, used by Janet).
- More than 183 days in NY: YES (257 days).
- → Janet IS a NY statutory resident for 2025.

Filing result:
(a) Federal: Form 1040, FL address. All worldwide income reported. Single return.
(b) NY State and NYC: Form IT-201 (RESIDENT return) for full year 2025. Because Janet is a statutory resident, she files as if she were a NY resident all year. All worldwide income subject to NY tax.
(c) FL: no PIT. Janet's FL domicile saves her on intangible investment income that no state taxes (no FL PIT). But for 2025, NY taxes her wages, dividends, capital gains, EVERYTHING (statutory residency = full residency).

Tax bill 2025 (see table).

Compared to a successful escape from NY statutory residency (≤183 days), Janet would have paid roughly $0 in NY tax 2025 (FL domicile + non-resident with only ~152 NY workdays Jan-May for wage sourcing, but wages would be allocated by workdays performed in NY = full Jan-May wages roughly $170k × NY rates ≈ $14,000). Net difference: ~$29,000 in extra 2025 NY tax + lost NYC tax.

**Tax bill 2025**

| Item | Amount |
| --- | --- |
| NY State tax on $400k wages + dividends/cap gains | ~$30,000 (NY State only) |
| NYC tax on same (NYC residents file NYC tax) | ~$13,000 |
| Total NY tax 2025 | ~$43,000 |

### 16.3 What Janet should have done

(a) Sold the NYC co-op in June 2025 (or by September). The "substantially all year" test would have failed → no statutory residency → only part-year NY tax on wages earned Jan-May.
(b) Limited NY days post-move to ≤30 days. Even with the abode, if total NY days were 152 + 30 = 182, no statutory residency (assuming <183 days strict).
(c) Rented out the co-op to a non-family tenant. The abode would not be "available" to Janet — borderline whether it remains a permanent place of abode (depends on lease terms).

### 16.4 Outcome

Janet pays ~$43,000 NY tax 2025 + faces potential NY audit reviewing the 2025 day-count carefully. Reviewer recommends: sell or rent out the NYC co-op by mid-2026 and limit NY days going forward. Janet's 2026 should look very different.

AUDIT FLASH POINT: This is exactly the case NY DTF audits. The combo of "FL domicile + NYC kept + 257 NY days" is a guaranteed audit.

## 17. Worked Example 2 — NY-employer + remote in TX (convenience rule)

### 17.1 Facts

- Taxpayer: Carlos, age 35, software engineer.
- Employer: Tech Inc., based in NYC. Carlos works fully remote.
- Residence history: NY domicile through 12/31/2024. Moved to Austin, TX on 1/1/2025 as a "permanent" move (sold NYC apartment, bought TX home, registered to vote, transferred license, etc.) — clean break domicile.
- Wages 2025: $300,000 W-2 from Tech Inc.
- Tech Inc.'s NYC office: still operational. Tech Inc. allows Carlos to work remotely as an employee accommodation. No bona fide TX office of Tech Inc. (Carlos works from his TX home; Tech Inc. doesn't have business reason to require TX presence).
- TX days in 2025: 360 (full year minus 5 NYC visits).
- NY days in 2025: 5 (one-week visits to NYC for company offsites).

### 17.2 Analysis

- **Carlos convenience rule analysis** — Domicile: Carlos is TX domiciliary as of 1/1/2025 (clean break). TX is full-year domicile for 2025. Statutory residency in NY: Carlos has NO permanent place of abode in NY (sold the apartment). Even if he had abode, he was only 5 days in NY → far below 183. → NOT a statutory NY resident. Wage sourcing — CONVENIENCE RULE: Tech Inc. is a NY-based employer. Carlos works remotely from TX, but this is at his convenience, not Tech Inc.'s necessity. The NY convenience rule applies: 100% of Carlos's wages are NY-source. EXCEPT for the 5 NYC visit days — those are obviously NY-source (no escape). The remaining 355 TX days — also NY-source under convenience rule. Carlos's NY-source wages = 100% × $300,000 = $300,000. TX tax: $0 (no PIT). NY tax: - NY State nonresident return Form IT-203. - NY-source income: $300,000 wages. - NY State tax: ~$20,000 (at 6.85% effective rate after deductions for top brackets). - NYC tax: Carlos is NOT a NYC resident, so NO NYC tax. - Total NY tax: ~$20,000. Resident credit: TX has no PIT → no TX tax to credit. No relief from the NY tax. Federal: Carlos's federal Form 1040 reports $300,000 wages. SALT deduction limited to $10,000 (TCJA). Carlos can claim a state-tax deduction (limited) for the $20,000 paid to NY.  _(20 NYCRR §132.18)_

### 17.3 Net result

Carlos owes ~$20,000 NY tax on wages earned entirely from his TX home — the convenience rule effect. There's no escape unless:
- Tech Inc. designates the TX home as a "bona fide employer office" (unlikely without business reason);
- Carlos changes employer to a non-NY-based employer; or
- The Mobile Workforce Act is enacted federally (status: pending, not enacted).

AUDIT FLASH POINT: NY DTF in 2024-2025 increasingly audits this exact fact pattern — NY employer + remote worker who claims TX/FL move. Tech employees are a primary target.

### 17.4 Planning recommendation

If Carlos wants to escape NY tax:
- (a) Change employer to a non-NY-based employer (most effective);
- (b) Negotiate with Tech Inc. for a "bona fide TX office" (employer leases co-working space in Austin, Carlos meets clients/teammates there, employer reimburses, etc.); or
- (c) Accept the NY tax cost as a permanent feature of working for a NY employer.

## 18. Worked Example 3 — CA-to-TX move with $2M RSU vest

### 18.1 Facts

- Taxpayer: Priya, age 40, senior staff engineer at TechMega Inc.
- Equity: RSU grant 1/1/2022 of 50,000 shares, 4-year quarterly vest (4,167 shares per Q, Q1 2025 through Q4 2025 — last year of the grant). Grant date FMV $40/share; vest-by-vest FMVs vary.
- Residence history: CA full-year through 8/31/2024. Moved to Austin, TX on 9/1/2024 (clean break). Continuing employment with TechMega; CA office; works from TX remotely.
- Wages 2025 (non-equity portion): $300,000 base salary.
- RSU vests in 2025: all four quarterly vests. Total vest 2025 value (FMV × shares) = $2,000,000 ($500,000 per quarterly vest assumed flat for simplicity).
- TX days in 2025: 365 (full year).
- CA days in 2025: 0.
- Domicile 2025: TX (clean break in 2024).

### 18.2 Analysis — base wages

- **Base salary sourcing** — Base salary $300,000: CA wage convenience rule? NO — CA does NOT have a convenience-of-the-employer rule. CA sources wages strictly by where work is physically performed. Workdays in CA 2025: 0. → $0 CA-source wages. TX wages: $300,000. TX has no PIT → no tax. CA tax on base wages 2025: $0.

### 18.3 Analysis — RSU vests

- **RSU workday-allocation calculations** — RSU grant 1/1/2022, vest 3/31/2025 (Q1 2025 vest, $500,000 portion): Grant date 1/1/2022. Vest date 3/31/2025. Period = 1/1/2022 to 3/31/2025 = 39 months ≈ 850 workdays (assuming 5-day workweek, ~260 workdays per year × 3.25 years). CA workdays in period: 1/1/2022 to 8/31/2024 = 32 months ≈ 700 workdays. TX workdays in period: 9/1/2024 to 3/31/2025 = 7 months ≈ 150 workdays. CA-source = $500,000 × 700/850 = $411,765. TX-source = $500,000 × 150/850 = $88,235. RSU vest Q2 2025 (6/30/2025), $500,000: Grant 1/1/2022 to vest 6/30/2025 = 42 months ≈ 910 workdays. CA workdays: 700. TX workdays: 6/30/2025 minus 9/1/2024 = 10 months ≈ 210 workdays. CA-source = $500,000 × 700/910 = $384,615. TX-source = $500,000 × 210/910 = $115,385. RSU vest Q3 2025 (9/30/2025), $500,000: Grant 1/1/2022 to vest 9/30/2025 = 45 months ≈ 975 workdays. CA workdays: 700. TX workdays: 9/1/2024 to 9/30/2025 = 13 months ≈ 275 workdays. CA-source = $500,000 × 700/975 = $358,974. TX-source = $500,000 × 275/975 = $141,026. RSU vest Q4 2025 (12/31/2025), $500,000: Grant 1/1/2022 to vest 12/31/2025 = 48 months = 1,040 workdays. CA workdays: 700. TX workdays: 9/1/2024 to 12/31/2025 = 16 months ≈ 340 workdays. CA-source = $500,000 × 700/1,040 = $336,538. TX-source = $500,000 × 340/1,040 = $163,462. Total RSU CA-source 2025: = $411,765 + $384,615 + $358,974 + $336,538 = $1,491,892. Total RSU TX-source 2025: = $88,235 + $115,385 + $141,026 + $163,462 = $508,108. (Sanity check: $1,491,892 + $508,108 = $2,000,000 ✓)

### 18.4 CA tax computation 2025

- **CA tax computation** — CA-source income 2025: $1,491,892 (RSU only — base wages $0 CA-source). CA nonresident return Form 540-NR. CA tax computed as if 100% CA resident on the $1,491,892, then pro-rated by CA AGI / Total AGI. For simplification: top CA bracket 13.3% + Mental Health Services Tax 1% on income >$1M = 14.3% on income >$1M. Approximate CA tax: $1,491,892 × ~14.0% blended = ~$208,800. (Actual computation requires running the full CA Form 540-NR. The Mental Health Services Tax kicks in only on the portion >$1M; the 13.3% on $700,000+ etc. This is a simplification.) TX tax 2025: $0. Resident credit: TX has no PIT → no credit available. No relief. Federal: $2,300,000 (wages + RSU vest) on federal Form 1040. SALT deduction $10,000.

### 18.5 Net result

Priya pays approximately $208,800 in CA tax 2025 — entirely on the CA-allocated portion of the RSU vests. The base wages are 100% TX-source (no CA tax). The TX-source RSU $508,108 is taxed only federally.

Critical observation: had Priya delayed her move to TX until 1/1/2026 (last year of grant), ALL of the 2025 vests would have been 100% CA-source — adding ~$70,000 more in CA tax. Conversely, had she moved earlier (e.g., 1/1/2023, just one year into the grant), 75% of each vest would be TX-source — saving ~$150,000 in CA tax.

Planning lesson: for taxpayers with multi-year equity vesting and a planned move, MOVE AS EARLY IN THE VESTING PERIOD AS POSSIBLE. Each additional year in CA pulls more vest value into CA-source.

### 18.6 Audit risk

CA FTB will audit this return — $1.5M of CA-source RSU on a Form 540-NR for a 2024-mover from CA is exactly the FTB equity-comp audit profile. Workpapers required:
- Grant agreement and vesting schedule;
- Workday log Jan 1, 2022 through Dec 31, 2025 (4 years);
- Travel records (boarding passes, hotel receipts);
- Move evidence (truck receipt, lease/purchase docs, TX driver's license issuance date);
- Employer's stock plan administrator statements (Schwab Equity Award Center, E*TRADE, etc.).

Preparer should request all of the above before signing.

AUDIT FLASH POINT: CA-to-TX (or CA-to-NV, CA-to-WA) equity-comp moves are among the most-audited CA fact patterns. FTB has dedicated equity-comp audit teams. Workpapers must be airtight.

## 19. Self-checks before signing the return

Before a credentialed reviewer signs the return, confirm:

1. ☐ Domicile determination supported by 6-factor analysis. Documented in workpapers.
2. ☐ Statutory residency analysis run for every state where taxpayer has abode + significant days. Day-count documented.
3. ☐ Part-year resident dates match between federal address change, voter registration, license issuance, and lease/purchase.
4. ☐ Wage allocation: workday log for each state. Convenience-rule states (NY/NJ/CT/PA/NE/AR/DE) flagged.
5. ☐ Equity comp: workday-allocation method applied. Grant date, vest date, exercise date documented for every grant. Per-vest spreadsheet.
6. ☐ Capital gains: real estate sourced to property state; intangibles sourced to domicile (with exceptions for partnership-interest-as-real-estate).
7. ☐ Pension and IRA distributions: §4 USC 114 preemption confirmed. Lump-sum nonqualified deferred comp identified and old-state-sourced.
8. ☐ Resident credit form prepared for the resident state (CA Sch S, NY IT-112-R, etc.). Limited to lesser of source-state actual tax or resident-state tax on the doubly-taxed income.
9. ☐ Reciprocal-agreement states: nonresident return AVOIDED if reciprocity applies and employee filed the reciprocal exemption form.
10. ☐ K-1 income from pass-through entities: state-by-state apportionment from K-1 supplements documented.
11. ☐ Rental real estate: sourced to property state. Depreciation recapture also sourced to property state.
12. ☐ Local taxes (NYC, Philadelphia, Yonkers, SF, etc.) addressed separately — flagged to local-specialty preparer if applicable.
13. ☐ Old-state audit risk assessed; documentation prepared for response.
14. ☐ Estimated payments to new state in place; old-state withholding adjusted/refunded.
15. ☐ S-corp / LLC / partnership state-level filings (PTE tax election, composite return) handled separately under us-pte-state-matrix.

## 20. Provenance and citations

- 4 U.S.C. §114 (Pension Source Tax Act of 1996, P.L. 104-95).
- N.Y. Tax Law §605 (residency definition).
- 20 NYCRR §105.20 (NY DTF regulation on residency and day-counting).
- 20 NYCRR §132.18 (NY DTF regulation on convenience-of-the-employer).
- NY TSB-M-06(5)I (NY guidance on convenience rule).
- NY TSB-M-95(3)I (NY guidance on stock option sourcing).
- NY TSB-M-09(1)I (NY guidance on 5-factor domicile test).
- NY Audit Guidelines (Nonresident Audit Guidelines, current revision).
- N.J.S.A. 54A:1-2(m) (NJ residency definition).
- N.J.S.A. 54A:5-1 (NJ adoption of reciprocal convenience rule, 2023).
- Conn. Gen. Stat. §12-701, §12-711 (CT residency and convenience).
- M.G.L. ch. 62 §1(f) (MA residency).
- Cal. Rev. & Tax. Code §17014 (CA residency, including 9-month presumption and 546-day safe harbor).
- Cal. Rev. & Tax. Code §17041 (CA tax base for nonresidents).
- Cal. Rev. & Tax. Code §17952 (CA sourcing of intangibles).
- Cal. Rev. & Tax. Code §17952.5 (CA installment-sale look-back).
- CA FTB Publication 1031 (Guidelines for Determining Resident Status).
- CA FTB Publication 1004 (Stock Option Guidelines).
- Neb. Rev. Stat. §77-2733(2) (NE convenience rule).
- Ark. Code §26-51-202 (AR convenience rule).
- 24 PA Code §109.8 (PA convenience rule limited).
- Matter of Gaied v. NY State Tax Appeals Tribunal, 22 N.Y.3d 592 (2014).
- Matter of Zelinsky v. Tax Appeals Tribunal, 1 N.Y.3d 85 (2003).
- Matter of Patrick, NY Div. of Tax App. (2009).
- Matter of Sobotka, NY Div. of Tax App. (2014).
- Matter of Reilly, NY Div. of Tax App. (2010).
- Matter of Stuckless, NY Div. of Tax App. (2015).
- Comptroller v. Wynne, 575 U.S. 542 (2015).
- Bindley v. Franchise Tax Board, Cal. Ct. App. (2024).
- IRS Notice 2002-47 (federal framework for executive compensation source rules).
- Treasury Regulation §1.83-3 (restricted property under §83).
- IRC §83, §409A, §457(f), §3121(v)(2)(C).

State guidance referenced (non-exhaustive): CA FTB Pub. 1031, NJ GIT-6, MA TIR 95-7, IL Pub-100, MN Schedule M1NR instructions, MD Form 502 instructions.

## 21. Circular 230 disclosure

This skill provides general guidance only. It is not a covered opinion. The reviewer must independently verify each state-specific position under that state's law. Multi-state residency is among the most-litigated areas of state tax law; consult a state-licensed practitioner for every state in which a return is filed. The taxpayer's facts and the applicable state law as of the filing date control. Tax positions taken on returns must be supported by substantial authority (or higher) under federal §6662 standards and applicable state penalty rules.

A credentialed practitioner (CPA, EA, or attorney admitted under Circular 230) must review and sign every multi-state return covered by this skill. State-specific representation in audits requires state-specific licensing. The reviewer must hold appropriate credentials for the jurisdiction(s) involved.

## End of skill

End of skill — us-multi-state-residency-and-allocation v0.1.

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
