---
name: us-form-5471-cfc-information
description: US federal content skill for Form 5471 — US Information Return for Controlled Foreign Corporations and other foreign corps requiring US-shareholder reporting under §§6038 and 6046. Covers tax year 2025 including the five filing categories (Cat 1 SFC, Cat 2 officer/director, Cat 3 acquisition/disposition, Cat 4 controller >50%, Cat 5 CFC shareholder), the §958(b)(4) repeal expanding the CFC universe through downward attribution, the eleven schedules (A through Q), §951 Subpart F + §951A GILTI inclusion mechanics, §959 PTEP tracking, §954(b)(4) high-tax exception, the $10,000 per-failure-per-year §6038 penalty, and reasonable-cause defense paths including Streamlined Foreign Offshore Procedures.
jurisdiction: US
domain: federal-tax
tax_year: 2025
reviewed_by: Christopher Aryee
review_status: accountant-reviewed
tier: 1
last_updated: 2026-07-06
---

# us-form-5471-cfc-information

## US Form 5471 — Information Return of US Persons With Respect to Certain Foreign Corporations

## 1. Scope and orientation

Form 5471 is an information return — not a tax return that itself produces a liability. It is the primary vehicle by which the United States enforces the global anti-deferral regime built into Subchapter N of the Internal Revenue Code. The form discloses ownership, financial position, earnings, and intercompany dealings of foreign corporations in which US persons have meaningful equity. It is also the substrate on which Subpart F inclusions under §951, GILTI inclusions under §951A, foreign tax credits under §§901 and 960, and previously taxed earnings and profits (PTEP) under §959 are computed, supported, and audited.

This skill covers tax year 2025. The post-TCJA architecture (effective for foreign-corp tax years beginning after December 31, 2017) remains in force: the repeal of §958(b)(4), the introduction of §951A GILTI, the §965 transition tax (now historical for ongoing filings but still relevant for PTEP tracking), the expansion of the §954(b)(4) high-tax exception, and the addition of Schedules I-1, J, P, and Q. The form itself was revised in December 2024 with refinements to Schedules J and P for tax years beginning on or after December 1, 2024; tax year 2025 filings use the most recent revision.

The form is mandatory for five distinct categories of US filers, each with a different triggering event and a different subset of schedules. A single filer can fall into more than one category for a single foreign corporation; in that case, the filer files one Form 5471 and checks every applicable category box on page 1. The five-category framework derives from two statutes — §6038 (annual information reporting by US persons controlling or owning interests in foreign corporations) and §6046 (reporting of acquisitions, dispositions, and organizational changes).

This skill is the entry point for any Schedule C, Form 1040, or Form 1120 file that reaches into a foreign corporate structure. Out of scope and referred elsewhere:

- Form 5472 — reverse direction: foreign-owned 25%+ US corporations and foreign-owned disregarded entities. Covered in the separate `us-form-5472-foreign-owned-us` skill.
- Form 8865 — interests in foreign partnerships. Separate skill.
- Form 8938 — specified foreign financial assets at the individual level under §6038D. Separate skill.
- Form 3520 / 3520-A — foreign trusts and foreign gifts above $100,000. Separate skill.
- FBAR / FinCEN 114 — Bank Secrecy Act reporting, not an IRS form. Separate skill.
- §962 election mechanics — the individual-level election to be taxed at corporate rates on §951(a) inclusions. Cross-referenced here, fully covered in the `us-section-962-election` skill.
- PFICs (Form 8621) — passive foreign investment companies. Often overlapping with CFCs; covered in separate skill.

## 2. Who must file — the five categories

### 2.1 Category 1 — US shareholder of a Specified Foreign Corporation (SFC)

- **Category 1 (SFC) definition and history** — Category 1 was originally added by the Tax Cuts and Jobs Act of 2017 to capture US shareholders of 'specified foreign corporations' under §965 — that is, CFCs plus any foreign corporation in which at least one US corporation was a US shareholder. It was the principal reporting category for the one-time §965 transition tax on accumulated deferred foreign income. With the §965 inclusion now historical, Category 1 has narrowed substantially in practical relevance, but the IRS has kept it on the form and has subdivided it into Cat 1a (controlling Section 245A shareholder), Cat 1b (non-controlling), and Cat 1c (related constructive owner). The category continues to apply to certain Section 245A reporting under the dividends-received deduction regime and to ongoing PTEP attributable to the §965 inclusion. A taxpayer should not assume Category 1 is dead. If the corporate structure includes a foreign corporation that was an SFC for tax year 2017 and that still has §965 PTEP balances flowing through Schedule P, the §245A reporting obligation continues. For most freelance and small-business filers this skill targets, Category 1 will be inapplicable, but the categorization analysis must consciously rule it out.  _(§965; TCJA 2017)_

### 2.2 Category 2 — US officer or director on an acquisition

- **Category 2 trigger and scope** — Category 2 is triggered when a US citizen or resident is an officer or director of a foreign corporation and any US person acquires (1) stock that, when added to stock already owned, meets the 10% threshold by vote or value, or (2) an additional 10% or more by vote or value. The triggering acquisition need not be by the officer or director themselves — it is enough that the officer or director sits on the foreign corporation's board or executive when some other US person crosses the threshold. This category catches an under-appreciated population. A US person who agrees to serve on the board of a friend's foreign startup as a favor — owning no equity at all — becomes a Cat 2 filer the moment any US investor acquires 10% of the company. Penalties under §6038 apply notwithstanding the zero economic interest. The schedules required for Cat 2 are limited (essentially Schedules A, B, and O), but the filing obligation is real.  _(§6038)_

### 2.3 Category 3 — Acquisition, disposition, or change of status

- **Category 3 four triggering events** — Category 3 is the §6046 transactional category. Four distinct events trigger it: 1. A US person acquires stock that, in the aggregate, meets the 10% threshold (by vote or value) of a foreign corporation. 2. A US person acquires additional stock that, when added to prior holdings, increases the holding by 10% or more. 3. A US person disposes of stock that drops them below 10%. 4. A person becomes a US person while owning at least 10% of a foreign corporation (the 'expatriation in reverse' trigger — e.g., a green card holder finally becoming a US tax resident). Category 3 requires a substantive filing including Schedule O (Part II) documenting the transaction, the seller, the consideration, and the resulting ownership. Many practitioners forget the 'becomes a US person' trigger; it bites immigrants who held foreign-corp equity before relocation.  _(§6046)_

### 2.4 Category 4 — Control for 30 days

- **Category 4 control test** — Category 4 is the §6038 'control' category. A US person who at any time during the foreign corporation's annual accounting period had more than 50% ownership by vote OR value, for an uninterrupted period of at least 30 days, is a Category 4 filer. 'Control' is determined by §6038(e)(2) and uses constructive ownership rules under §318(a) with certain modifications. Category 4 requires the full schedule set: Schedules A, B, C, F, G, H, I, M, and — depending on whether the corporation is also a CFC — Schedules E, E-1, I-1, J, P, Q, and R. Category 4 is the heaviest filing burden on the form. Note carefully: Category 4 control is 'vote OR value.' A US person holding 51% by value but only 30% by vote (a common preferred-stock arrangement) is still a Cat 4 filer. The vote-or-value test was harmonized post-TCJA across the CFC and Cat 4 definitions; pre-TCJA, control for CFC purposes was vote-only, which created traps the 2017 changes were designed to close.  _(§6038(e)(2); §318(a))_

### 2.5 Category 5 — US shareholder of a CFC

- **Category 5 definition and subdivisions** — Category 5 is by far the most common filing trigger and the workhorse of the Form 5471 universe. A US shareholder (defined at §951(b) as a US person owning 10% or more of a foreign corporation by vote or value) of a CFC (defined at §957 — see §3 below) who owns stock in the CFC on the last day of the CFC's tax year on which it qualifies as a CFC is a Category 5 filer. Category 5 is subdivided: - Cat 5a — controlling US shareholder: a US shareholder who is also a Cat 4 controller, or who is a 'specified Section 958(a) US shareholder' in a partnership/S corporation structure that controls. - Cat 5b — non-controlling US shareholder: any other 10%+ US shareholder who is not within Cat 5a or 5c. - Cat 5c — related constructive owner: a US shareholder whose 10%+ position arises solely through constructive ownership (e.g., §318 family attribution) and who is related to a controlling Section 958(a) shareholder. Cat 5c filers may rely on a multiple-filer exception if the controlling shareholder files a complete Form 5471 covering all required schedules — but the exception must be claimed and documented, not assumed. The schedule load for Cat 5 mirrors Cat 4 plus the post-TCJA additions (I-1, J, P, Q) tied to GILTI and PTEP.  _(§951(b); §957)_
- **AUDIT FLASH POINT — §958(b)(4) and Cat 5 expansion** — The TCJA's repeal of §958(b)(4) opened the floodgates: foreign-to-US 'downward attribution' now applies for purposes of determining CFC status (though not for purposes of determining who is a 'US shareholder' with an inclusion). The result is that a foreign parent with a US subsidiary and a non-US subsidiary will cause the non-US sub to be a CFC even though no US person has any direct or indirect economic interest in it. The 10% US shareholder of that 'sister CFC' then has a Cat 5 filing obligation even though they are an arm's-length party with no inside information. Notice 2018-13 and Rev. Proc. 2019-40 provide partial safe-harbor relief — narrow, and conditional on the absence of a US-shareholder relationship of more than minimal economic interest — but the filing obligation is broad and routinely missed. The IRS has been issuing automated Letter 6291 / 6292 penalty notices to filers caught by this expansion who had no reason to suspect they were CFC shareholders.  _(§958(b)(4); Notice 2018-13; Rev. Proc. 2019-40)_

## 3. CFC definition — §957 and §958(b)(4) repeal

- **Controlled foreign corporation (CFC)** — A controlled foreign corporation is defined at §957(a) as any foreign corporation in which more than 50% of the total combined voting power of all classes of voting stock, or more than 50% of the total value of all stock, is owned (within the meaning of §958(a)) or considered owned (by applying the constructive ownership rules of §958(b)) by US shareholders on any day during the foreign corporation's tax year.  _(§957(a))_
- **US shareholder** — A US shareholder is defined at §951(b) as a US person who owns (within §958(a)) or is considered to own (within §958(b)) 10% or more of the total combined voting power of all classes of stock entitled to vote or 10% or more of the total value of all classes of stock of the foreign corporation.  _(§951(b))_
- **Vote-or-value disjunction post-TCJA** — The vote-or-value disjunction in both tests was introduced by TCJA effective for tax years beginning after December 31, 2017. Pre-TCJA, only vote counted; this enabled common-stock-with-no-vote structures to escape CFC status. Post-TCJA, those structures are squarely caught.  _(TCJA, effective for tax years beginning after December 31, 2017)_
- **Constructive ownership and §958(b)(4) repeal** — Constructive ownership under §958(b) imports the §318 rules with several modifications. §318 attributes ownership among family members (spouse, children, grandchildren, parents — note: no attribution between siblings), among entities and their owners, and among partnerships, estates, and trusts. The TCJA repealed §958(b)(4), which had previously turned off 'downward attribution' — attribution from a foreign person to a US person. With §958(b)(4) gone, a foreign parent's stock in a foreign subsidiary is attributed downward to the foreign parent's US subsidiary, with the result that the foreign subsidiary may be a CFC vis-à-vis the US sub even when no US person has any direct or indirect economic interest.  _(§958(b); §318)_
- **Rev. Proc. 2019-40 safe harbor for unrelated §958(a) US shareholders** — The Treasury issued Notice 2018-13 (October 2018), Proposed Regulations under §958 (October 2019), and Rev. Proc. 2019-40 (October 2019) to provide partial relief through a safe harbor for 'unrelated Section 958(a) US shareholders.' Under Rev. Proc. 2019-40, a US person who owns less than 10% by vote and value and who is unrelated to the controlling shareholder may rely on the safe harbor and be excused from Form 5471 filing. The safe harbor's scope is narrow: it does not relieve a 10%+ shareholder, and it requires the US person to have no current or former officer or director relationship with the foreign corp, no actual knowledge of the relevant CFC status, and to have made reasonable inquiry. Documentation of the inquiry is essential — without it the safe harbor cannot be invoked at audit.  _(Notice 2018-13; Rev. Proc. 2019-40)_

## 4. The eleven schedules — what each one does

Form 5471 is a multi-page mothership with schedules that are themselves multi-page returns. Filing requirements vary by category; not every filer files every schedule. The skill organises the schedules in the order they appear on the form, then maps them to categories at the end of this section.

### 4.1 Schedule A — Stock of the foreign corporation

- **Schedule A** — Schedule A is the disclosure of the foreign corporation's capital structure. It lists each class of stock issued, the number of shares outstanding at the beginning and end of the year, and the par or stated value. For multiple classes (voting, non-voting, common, preferred), each class is listed separately. Required for Categories 1, 2, 3, 4, and 5.

### 4.2 Schedule B — US shareholders of foreign corporation

- **Schedule B** — Schedule B is split into two parts. Part I lists all 'US shareholders' within the §951(b) meaning — that is, every US person owning 10% or more directly, indirectly (through §958(a) ownership through foreign entities), or constructively (through §958(b)). For each shareholder, the schedule discloses name, address, taxpayer identification number, class of stock held, number of shares at year-start and year-end, and pro rata share of Subpart F income and GILTI inclusion. Part II lists direct shareholders owning 5% or more by vote or value — a broader population than Part I, capturing economic interests that may not meet the US shareholder threshold but that the IRS wants visibility into. Required for Categories 4 and 5.  _(§951(b); §958)_

### 4.3 Schedule C — Income statement

- **Schedule C** — Schedule C presents the foreign corporation's income statement, organised by line items that broadly parallel a US GAAP/tax format. The statement must be prepared in functional currency (the currency of the corp's primary economic environment, generally local currency) and then translated to US dollars at the weighted-average exchange rate for income statement items. Schedule C is the input for the §954 Subpart F categorisation and the §951A tested income computation. It must reconcile to Schedule H (current E&P) through the book-to-tax adjustments specified in §964 and Treas. Reg. §1.964-1. Required for Categories 4 and 5.  _(§954; §951A; §964; Treas. Reg. §1.964-1)_

### 4.4 Schedule E and E-1 — Foreign income taxes paid and deemed paid

- **Schedule E** — Schedule E reports the foreign corporation's income, war profits, and excess profits taxes paid or accrued during the tax year, by separate-category basket (§904(d)) and by §959(c) PTEP group. Schedule E is the input for the foreign tax credit under §§901 (direct credit on Subpart F inclusion) and 960 (deemed-paid credit on GILTI and Subpart F inclusions by domestic corporations).  _(§904(d); §959(c); §901; §960)_
- **Schedule E-1** — Schedule E-1 tracks taxes 'deemed paid' — the §960 mechanism by which a domestic corporate US shareholder is treated as having paid the foreign taxes attributable to its §951(a) or §951A inclusion. The schedule is organised by §904(d) basket and tracks current-year taxes deemed paid, distributions of PTEP, and reductions. The Treasury final regulations under §960 (T.D. 9882, December 2019) prescribe a 'properly attributable' tracing methodology that requires precise basket-by-basket tracking. Required for Categories 4 and 5 (and historically Category 1 for §965 PTEP). Individual US shareholders not making the §962 election do not get the deemed-paid credit and may treat Schedule E-1 as informational for them, but it must still be completed where the schedule is otherwise required.  _(§960; T.D. 9882)_

### 4.5 Schedule F — Balance sheet

- **Schedule F** — Schedule F is the foreign corporation's balance sheet at the beginning and end of the tax year, in functional currency and translated to US dollars at the spot rate as of each balance sheet date. The schedule must conform to US tax principles, not local-GAAP principles; differences (deferred tax assets, revaluation reserves, equity-method investments) must be adjusted to US tax positions. Required for Categories 4 and 5.

### 4.6 Schedule G — Other information

- **Schedule G** — Schedule G is the disclosures section. It is a multi-page yes/no questionnaire covering related-party transactions, hybrid instruments, base-erosion arrangements (BEPS-related), §267A disallowed deductions, §59A BEAT relevance, the §954(b)(4) high-tax election, the §954(c)(6) look-through election, §1411 net investment income, ownership of foreign disregarded entities (linking to Form 8858), and dozens of other items. Schedule G has expanded significantly post-TCJA and is the principal source of audit triggers — answer it carefully. Required for Categories 4 and 5.  _(§267A; §59A; §954(b)(4); §954(c)(6); §1411)_

### 4.7 Schedule H — Current earnings and profits

- **Schedule H** — Schedule H computes the current-year E&P of the foreign corporation under §964 and Treas. Reg. §1.964-1. E&P is the principal measure of the corporation's distributable income for US tax purposes and is the cap on §951(a) Subpart F inclusions (under §952(c)) and the foundation for §959 PTEP tracking. The schedule begins with current-year net income per Schedule C, then makes book-to-tax adjustments (depreciation conformity to US methods, capitalised costs, accruals, foreign currency gain/loss recognition, etc.). Required for Categories 4 and 5.  _(§964; Treas. Reg. §1.964-1; §951(a); §952(c); §959)_

### 4.8 Schedule I — Shareholder's pro rata share of Subpart F income

- **Schedule I** — Schedule I is the shareholder-level summary: for each US shareholder, it reports their pro rata share of the foreign corp's Subpart F income by §954 category (foreign personal holding company income, foreign base company sales income, foreign base company services income, insurance income, §952(a)(3) international boycott income, §952(a)(4) illegal payments, etc.), plus the GILTI inclusion amount (from Schedule I-1), plus §965 inclusions for historical years. The pro rata share is determined under §951(a)(2) with reference to the shareholder's ownership at the close of the foreign corp's tax year, reduced by §245A dividends and earlier-year PTEP. The amount on Schedule I flows to Form 1040 Schedule 1 (for individual filers without a §962 election) or Form 1120 Schedule C (for corporate filers). Required for Categories 4 and 5.  _(§954; §952(a)(3); §952(a)(4); §951(a)(2); §245A)_

### 4.9 Schedule I-1 — Information for GILTI computation

- **Schedule I-1** — Schedule I-1 is the per-CFC computation of the inputs to GILTI under §951A. It reports: tested income or tested loss, qualified business asset investment (QBAI — average adjusted basis in tangible business assets generating tested income), tested interest expense, and tested interest income. These per-CFC amounts aggregate at the US-shareholder level on the shareholder's Form 8992 (GILTI calculation) and then to the shareholder's return. Required for Categories 4 and 5 (CFC only).  _(§951A)_
- **AUDIT FLASH POINT — §954(b)(4) high-tax exclusion election timing** — The §954(b)(4) high-tax exception, originally available only for Subpart F income, was extended to GILTI tested income by the Treasury's final regulations under §951A (T.D. 9902, July 2020). The election is made on Schedule I-1 (and on the controlling shareholder's Form 5471 covers all CFC members of a CFC group; once made, applies to all CFCs in the group). The election excludes from tested income any item that was subject to an effective foreign tax rate exceeding 90% of the maximum US corporate rate — for 2025 with a 21% US rate, the threshold is 18.9%. The election is annual and irrevocable for the year once made; it must be made by the controlling shareholder, which under Treas. Reg. §1.951A-2(c)(7) is the §958(a) controlling shareholder, and all consenting US shareholders' Forms 5471 must reflect the consistent election. Missing the consistency requirement is a common error and a frequent audit point.  _(§954(b)(4); T.D. 9902; Treas. Reg. §1.951A-2(c)(7))_

### 4.10 Schedule J — Accumulated earnings and profits

- **Schedule J** — Schedule J is the cumulative E&P tracking schedule. It opens with the prior-year ending balance, adds current-year E&P from Schedule H, and tracks distributions and §959(c) PTEP movements. Schedule J post-TCJA is organised by PTEP 'group' — a fine-grained classification that distinguishes §965(a) PTEP, §965(b) PTEP, §951(a)(1)(A) Subpart F PTEP, §951A GILTI PTEP (including the §250 deduction adjustments), §245A(d) hybrid dividend PTEP, and various others. The Schedule J columns total to 15+ separate PTEP groups, each tracked separately because each carries different foreign tax credit and §959 distribution-ordering consequences. Schedule J was significantly redesigned in the December 2024 form revision to add three new PTEP groups reflecting the IRS's evolving §959 distribution-ordering guidance. The new revision applies to tax years beginning on or after December 1, 2024 — so the typical calendar-year CFC for 2025 uses the new layout. Required for Categories 4 and 5.  _(§959(c); §965; §951(a)(1)(A); §951A; §250; §245A(d))_

### 4.11 Schedule M — Transactions between CFC and shareholders or related persons

- **Schedule M** — Schedule M discloses every related-party transaction during the tax year between the foreign corporation and: its US shareholders, persons related to those shareholders under §267(b), and various other related-party categories. The transactions are reported by counterparty and by type — sales of goods, sales of property, rents and royalties, services, commissions, interest, dividends, loans, capital contributions, distributions, and 'other.' Amounts are reported in US dollars. The schedule is the principal data source for transfer-pricing audits under §482 and for §367 outbound transfer review. Required for Categories 4 and 5.  _(§267(b); §482; §367)_

### 4.12 Schedule O — Organization or reorganization of foreign corporation, and acquisitions and dispositions of its stock

- **Schedule O** — Schedule O is the §6046 transactional schedule. Part I reports the foreign corporation's organisation or reorganisation events during the tax year — incorporation, dissolution, merger, division, recapitalisation. Part II reports each US person's acquisition or disposition of 10%+ of the foreign corp during the year — name, address, date, consideration, and resulting ownership. Required for Categories 2 and 3.  _(§6046)_

### 4.13 Schedule P — Previously taxed earnings and profits

- **Schedule P** — Schedule P is the US-shareholder-level PTEP tracking schedule, complementary to the entity-level Schedule J. PTEP under §959 is income that has already been included in a US shareholder's income under §951(a) (Subpart F) or §951A (GILTI), and which, when subsequently distributed, is excluded from gross income to prevent double taxation. PTEP must be tracked by year, by §959(c) group, and by §904(d) foreign tax credit basket. Distributions are sourced from PTEP under §959(c) before they touch §959(c)(3) non-previously-taxed E&P, in a strict ordering rule that the December 2024 revision clarified. Required for Categories 4 and 5.  _(§959; §951(a); §951A; §959(c); §904(d))_
- **AUDIT FLASH POINT — PTEP cliff at distribution** — When PTEP is distributed, the foreign tax associated with that PTEP (tracked on Schedule E-1) may be claimed as a deemed-paid credit by a domestic corporate shareholder — but only if Schedule P shows the PTEP balance and the basket assignment correctly. PTEP balances inherited from §965 (the 2017 transition tax) often went unreconciled in the years immediately after TCJA, leaving shareholders unable to claim the deemed-paid credit when distribution finally happened. Penalty assertions in this area focus less on the §6038 information-return penalty and more on the substantive disallowance of FTCs — which can be far more costly than the $10,000 form-filing penalty. Reconcile Schedule P every year, with year-by-year layers preserved and basket assignments documented.  _(§965; §6038)_

### 4.14 Schedule Q — CFC income by CFC income groups

- **Schedule Q** — Schedule Q reports the foreign corporation's income broken into 'CFC income groups' under Treas. Reg. §1.960-1: tested income or loss, residual income, Subpart F categories, §951A(c)(2)(A)(i)(II) high-tax exclusion income, etc. The schedule serves as the bridge between Schedule H (entity E&P) and Schedule I-1 (GILTI inputs), and is the input to the §960 deemed-paid foreign tax credit computation on Schedule E-1. Schedule Q is dense and unforgiving — it requires a detailed mapping of every E&P item to a basket and a group. The December 2024 revision refined the column headings to align with the §951A high-tax exception election and the §250 deduction interactions. Required for Categories 4 and 5 (CFC only).  _(Treas. Reg. §1.960-1; §951A(c)(2)(A)(i)(II); §960; §250)_

### 4.15 Schedule R — Distributions from foreign corporation

- **Schedule R** — Schedule R reports each distribution from the foreign corporation to its shareholders during the year — date, amount in functional currency, US-dollar-translated amount, character of the distribution (PTEP versus non-PTEP), PTEP group from which sourced, and recipient. The schedule supports the §959 distribution-ordering analysis on Schedule J and Schedule P. Required for Categories 4 and 5.  _(§959)_

### 4.16 Schedule-to-category map

**Schedule-to-category map**

| Category | Schedules required |
| --- | --- |
| Cat 1 (SFC) | A, B, C, F, G, H, I, E, E-1, J, P (historical §965 focus) |
| Cat 2 (officer/director on acquisition) | A, B (Part I), O |
| Cat 3 (acquisition/disposition) | A, B, C, F, G, H, I, O |
| Cat 4 (controller >50%) | A, B, C, E, E-1, F, G, H, I, M; if CFC: I-1, J, P, Q, R |
| Cat 5a (controlling CFC shareholder) | A, B, C, E, E-1, F, G, H, I, I-1, J, M, P, Q, R |
| Cat 5b (non-controlling) | A, B, C, F, G, H, I, I-1, J, P, Q, R (reduced M) |
| Cat 5c (related constructive owner) | Reduced; may rely on multiple-filer exception if controlling Cat 5a files complete return |

- **Cat 5c multiple-filer exception cross-statement requirement** — The reduced-Cat-5c exception requires the controlling shareholder to attach a statement listing the Cat 5c filers who are relying on the exception, and each Cat 5c filer attaches a corresponding statement to their own return identifying the Cat 5a filer. Failure to attach the cross-statements voids the exception and reinstates the full Cat 5c filing obligation, with §6038 penalty exposure.  _(§6038)_

## 5. §951 Subpart F inclusion — mechanics

- **§951(a) inclusion requirement** — §951(a) requires each US shareholder of a CFC to include in gross income their pro rata share of the CFC's Subpart F income for the CFC's tax year ending within or with the shareholder's tax year. The inclusion is current — not deferred until distribution — and is the original anti-deferral mechanism of the IRC (predating GILTI by 55 years; Subpart F was enacted in 1962).  _(§951(a))_
- **Pro rata share determination** — Pro rata share is determined under §951(a)(2): the shareholder's share of Subpart F income equals the amount that would be distributed to the shareholder if the CFC had distributed all of its current-year E&P, reduced by amounts distributed during the year to other persons. The denominator is total stock outstanding; the numerator is the shareholder's stock held on the last day of the CFC's tax year on which it qualifies as a CFC.  _(§951(a)(2))_
- **Subpart F income definition and E&P cap** — Subpart F income is defined at §952 and built up from the §954 categories described in §7 below. It is capped at current-year E&P under §952(c)(1) — a CFC cannot generate Subpart F income in excess of its current E&P, even if §954 categories independently would imply more. Excess Subpart F is 'recaptured' in later years to the extent of later E&P (§952(c)(2)).  _(§952; §952(c)(1); §952(c)(2))_
- **Reporting of Subpart F inclusion** — The inclusion is reported on the US shareholder's return. For individuals, on Form 1040 Schedule 1 Line 8 (Other Income) with a '§951(a)' descriptor. For C corporations, on Form 1120 Schedule C Line 14. The amount is sourced from Schedule I of the Form 5471.  _(§951(a))_
- **Character of Subpart F inclusion and §962 mitigation** — Character: ordinary income, not qualifying for §1(h)(11) qualified dividend rates. This is a major disadvantage for individual shareholders — they are taxed at ordinary rates (up to 37%) on income that, if received as a true dividend from a treaty-country corporation, might have qualified for the 20% qualified-dividend rate. The §962 election is the principal mitigation: it allows the individual to elect corporate-rate taxation (21%) plus the §250 deduction on GILTI, with the trade-off that subsequent distribution is taxed again at individual rates to the extent of the post-§962 PTEP excess.  _(§1(h)(11); §962; §250)_

## 6. §951A GILTI inclusion — mechanics

§951A was added by TCJA and is effective for tax years beginning after December 31, 2017. GILTI ('Global Intangible Low-Taxed Income') is a parallel anti-deferral regime that catches the residual income of CFCs not already caught by Subpart F. The intended target was the high-return intellectual-property-driven income of multinationals' offshore operations; the actual mechanical reach is much broader.

- **GILTI computation steps** — Computation at the US shareholder level (not at the CFC level, in contrast to Subpart F): 1. Tested income or loss per CFC = gross income, less the gross income items that fall outside the tested-income net (Subpart F income, §954(b)(4) high-tax excluded income, ECI, related-party dividends from same-country CFCs), less deductions properly allocable. 2. Net tested income = sum of tested income amounts minus sum of tested loss amounts across all CFCs the US shareholder owns. 3. Qualified business asset investment (QBAI) per CFC = average aggregate adjusted basis (using the alternative depreciation system) of specified tangible property held by the CFC and used in producing tested income. QBAI excludes intangibles, inventory, and property producing non-tested income. 4. Deemed tangible income return (DTIR) = 10% × aggregate QBAI of CFCs producing tested income. 5. Specified interest expense = net interest expense of CFCs to the extent allocable to tested income. 6. GILTI inclusion = net tested income minus (DTIR minus specified interest expense). If DTIR exceeds specified interest expense, the excess reduces GILTI; otherwise GILTI equals net tested income. The computation is at the shareholder level, but the per-CFC inputs come from Schedule I-1 of each CFC's Form 5471. The shareholder's Form 8992 aggregates the I-1 inputs and computes the GILTI inclusion.  _(§951A)_
- **§250 deduction rate for domestic C corporations** — §250 deduction: a domestic C corporation gets a 50% deduction against GILTI (37.5% effective rate on the GILTI portion of FDII, but on the GILTI side the deduction is 50% for tax years beginning before 2026, dropping to 37.5% for tax years beginning after 2025 under TCJA's original sunset). The OBBBA (P.L. 119-21, July 2025) preserved the §250 deduction at 50% — confirming the sunset cliff did not occur and the 50% rate continues for 2025 and beyond. Combined with the 21% corporate rate, the effective rate on GILTI for a domestic C corp is 10.5% before foreign tax credits.  _(§250; OBBBA P.L. 119-21 (July 2025))_
- **Individual shareholders GILTI treatment without §962** — Individual shareholders without a §962 election get no §250 deduction and pay ordinary rates (up to 37%) plus net investment income tax considerations on GILTI inclusions. The §962 election is therefore particularly powerful for individuals with material GILTI exposure: it provides corporate-rate taxation and access to the §250 deduction at the cost of a second layer of tax on distribution.  _(§962; §250)_
- **§954(b)(4) high-tax exclusion election for GILTI** — §954(b)(4) high-tax exclusion election: as noted in §4.9, the election extends to GILTI tested income for tax years of CFCs beginning on or after July 23, 2020. When made, items of tested income subject to an effective foreign tax rate exceeding 90% of the US corporate rate (>18.9% for 2025) are excluded from GILTI. The election is made by the controlling Section 958(a) shareholder, applies on a tested-unit-by-tested-unit basis, and binds all consenting US shareholders. Once made for a year, irrevocable for that year.  _(§954(b)(4))_

## 7. §954 categories of Subpart F income

§954 defines the principal categories of Subpart F income. Each category is computed separately and aggregated into the §952 Subpart F total.

### 7.1 Foreign personal holding company income (FPHCI) — §954(c)

- **FPHCI definition** — FPHCI is the passive-income basket. It includes dividends, interest, royalties, rents, annuities, net gains from sales of property producing the foregoing or that does not give rise to active income, commodity transactions (with active-trade exceptions), foreign currency gains (other than from §988 transactions in the ordinary course of the active business), and gains from notional principal contracts.  _(§954(c))_
- **§954(c)(2)(A) — active rent and royalty exception** — Rents and royalties from the active conduct of a trade or business and received from an unrelated person are excluded.  _(§954(c)(2)(A))_
- **§954(c)(3) — same-country exception** — Dividends and interest from a related corporation organised under the laws of the CFC's country, where that corporation has a substantial part of its assets used in a trade or business in that country, are excluded.  _(§954(c)(3))_
- **§954(c)(6) — CFC look-through made permanent** — Dividends, interest, rents, and royalties received from a related CFC are excluded if attributable to income of the payor that is neither Subpart F nor ECI. Originally a temporary provision, repeatedly extended; the OBBBA (2025) made §954(c)(6) permanent for tax years beginning after December 31, 2024. This is a major structural simplification for multinationals operating through CFC subgroups.  _(§954(c)(6); OBBBA (2025))_

### 7.2 Foreign base company sales income (FBCSI) — §954(d)

- **FBCSI definition** — FBCSI is income from a CFC's purchase of personal property from a related person and sale to any person (or purchase from any person and sale to a related person), where the property is both manufactured and sold for use outside the CFC's country of incorporation. The intent is to catch 'drop-shipping' structures where a CFC is interposed between a related supplier and a customer in a third country without performing substantive activity.  _(§954(d))_
- **Manufacturing exception** — If the CFC manufactures the property (under either the substantial-transformation test of Treas. Reg. §1.954-3(a)(4)(ii) or the substantial-contribution test of §1.954-3(a)(4)(iv)), the income is not FBCSI even if the purchase and sale parties are related.  _(Treas. Reg. §1.954-3(a)(4)(ii); §1.954-3(a)(4)(iv))_
- **Branch rule** — A branch of the CFC in a country other than the CFC's country of incorporation may be treated as a separate corporation for FBCSI purposes if the branch's effective tax rate is materially lower than the CFC's home-country rate, triggering FBCSI on income that flows through the branch.  _(§954(d))_

### 7.3 Foreign base company services income (FBCSI-svc) — §954(e)

- **FBCSI-svc definition** — FBCSI-svc is income from services performed by a CFC for or on behalf of a related person, where the services are performed outside the CFC's country of incorporation. Same intent as FBCSI: catching cross-border services arrangements that interpose a low-tax CFC for transfer-pricing optimisation without substantive functions.  _(§954(e))_

### 7.4 Insurance income — §953

- **Insurance income** — Insurance income of a CFC (insuring risks outside the CFC's home country) is Subpart F income. The category was substantially expanded by TCJA and the PATH Act amendments and now reaches captive insurance arrangements that previously escaped through the Bermuda and Cayman structures.  _(§953)_

### 7.5 §952(a)(3), (4), (5) — boycott income, illegal payments, foreign country sanctions

- **Boycott/illegal payments/sanctions income** — Less commonly relevant but on the books: income attributable to international boycotts (§999), illegal bribes and kickbacks (§162(c)), and income derived from countries subject to §901(j) sanctions. Schedule G asks about each.  _(§952(a)(3); §952(a)(4); §952(a)(5); §999; §162(c); §901(j))_

### 7.6 §954(b)(4) high-tax exception

- **§954(b)(4) high-tax exception threshold for 2025** — Already discussed at §4.9 and §6. For 2025 with the 21% US corporate rate, the threshold is 18.9% (90% × 21%). The election is made on Schedule I-1 by the controlling Section 958(a) shareholder, applies tested-unit-by-tested-unit, and excludes the high-taxed items from both Subpart F and GILTI. Documentation of the foreign effective tax rate on a tested-unit basis is essential and is the single most common audit issue under the high-tax election.  _(§954(b)(4))_

## 8. §959 PTEP — previously taxed earnings and profits

- **§959 double-taxation prevention mechanism** — §959 prevents double taxation of income that has already been included under §951(a) Subpart F or §951A GILTI. When such pre-taxed E&P is later distributed, §959(a) excludes it from the recipient's gross income. The mechanic is straightforward in principle and excruciating in operation.  _(§959(a); §951(a); §951A)_
- **PTEP groups** — Post-TCJA, PTEP is tracked in approximately 16 separate groups, distinguished by their source (Subpart F vs GILTI vs §965 transition tax vs §245A hybrid dividend), by their year of origin, and by their §904(d) foreign tax credit basket assignment. The December 2024 form revision refined the groupings to align with the §960 final regulations and added three new groups for §245A(d) and §951A high-tax-elected amounts.  _(§904(d); §960; §245A(d); §951A)_
- **Distribution ordering under §959(c)** — §959(c) prescribes that distributions are sourced first from §959(c)(1) PTEP (the §956 investment-in-US-property PTEP — rare post-TCJA but still occurs), then from §959(c)(2) PTEP (the §951(a)(1)(A) and §951A inclusions), then from §959(c)(3) non-previously-taxed E&P. Within §959(c)(2), the IRS's guidance (Notice 2019-01 and the proposed §959 regulations) prescribes a 'last-in, first-out' ordering by year and a within-year ordering by group.  _(§959(c); §959(c)(1); §959(c)(2); §959(c)(3); §956; §951(a)(1)(A); §951A; Notice 2019-01)_
- **Foreign currency translation of PTEP** — PTEP balances are tracked in US dollars at the spot rate on the date the underlying inclusion was made. Subsequent distribution at a different spot rate produces §986(c) foreign currency gain or loss — ordinary, not capital, and a routine source of small but persistent adjustments.  _(§986(c))_
- **Basis adjustment on inclusion and distribution** — A §951(a) or §951A inclusion increases the US shareholder's basis in the CFC stock under §961(a). A subsequent distribution of PTEP reduces basis under §961(b). If PTEP is distributed in excess of basis (rare, but possible after multiple years of basis erosion), the excess is treated as gain from sale or exchange.  _(§961(a); §961(b))_

## 9. Due dates and extensions

- **Form 5471 filing mechanics** — Form 5471 is filed as an attachment to the US person's income tax return for the tax year in which the foreign corp's tax year ends. The due date and extension date are the filer's, not the CFC's.
- **Individuals (Form 1040) due date** — April 15 of the year following the tax year; with extension, October 15.
- **Calendar-year C corporations (Form 1120) due date** — April 15 (15th day of 4th month after year-end); with extension, October 15.
- **Calendar-year partnerships (Form 1065) and S corporations (Form 1120-S) due date** — March 15; with extension, September 15. Form 5471 attaches to the entity return when the entity is the US shareholder.
- **June fiscal-year filers due date** — 15th day of the 4th month after fiscal year-end.
- **Extension mechanics via Form 4868/7004** — Form 4868 (individual extension) or Form 7004 (entity extension) extends Form 5471. There is no separate extension for the 5471 standing alone; if the underlying return is on extension, the 5471 is too.  _(Form 4868; Form 7004)_

A CFC with a non-calendar tax year reports on the US shareholder's tax year that contains the close of the CFC's tax year. For a US-calendar-year shareholder of a CFC with a June 30, 2025 fiscal year end, the Form 5471 attaches to the shareholder's 2025 Form 1040 (filed April 15, 2026) and reports the CFC's July 2024 – June 2025 fiscal year.

## 10. §6038 penalties

- **§6038(b) base penalty per Form 5471 per year** — $10,000 penalty per Form 5471 not filed, per year. The penalty is automatic — the IRS asserts it on the assumption of non-compliance and shifts the burden to the taxpayer to demonstrate reasonable cause. For a US person with multiple CFCs, the penalty is $10,000 per CFC per year — a six-CFC structure that has missed three years of filings carries a starting penalty exposure of $180,000 before any continuing-failure additions. USD  _(§6038(b))_
- **Continuing failure penalty** — If the failure continues 90 days after IRS notice of the failure, an additional $10,000 per 30-day period accrues, capped at $50,000 per Form 5471 per year. Combined with the initial $10,000, the per-CFC-per-year maximum is $60,000.  _(§6038(b))_
- **§6038(c) foreign tax credit reduction** — §6038(c) reduces the foreign tax credit otherwise allowable to the filer by 10% for each Form 5471 not timely filed. After 90 days of continuing failure, an additional 5% reduction applies per 3-month period, capped at the lesser of (a) the FTC otherwise allowable or (b) the greater of $10,000 or the income of the foreign corp for the year. For a US shareholder relying on the §960 deemed-paid credit to substantially zero out US tax on a GILTI inclusion, the §6038(c) reduction can be devastating — it can convert a tax-neutral GILTI position into a substantial cash tax liability independent of the $10,000 information-return penalty.  _(§6038(c))_
- **Criminal penalty for wilful failure** — §7203 imposes a misdemeanor (up to 1 year in prison, $25,000 fine) for wilful failure to file. Rarely asserted for Form 5471 alone but available where the IRS demonstrates wilfulness.  _(§7203)_
- **§6501(c)(8) statute of limitations extension** — §6501(c)(8) keeps the assessment statute of limitations open on the entire return until 3 years after the missing Form 5471 is filed. This is severe — a missing 5471 effectively eliminates the SoL on the entire 1040 or 1120, exposing all items on the return to indefinite audit. The Tax Court and several Courts of Appeals have repeatedly confirmed the §6501(c)(8) opening, most recently in the District Court litigation surrounding the Farhy decision and its aftermath.  _(§6501(c)(8))_
- **AUDIT FLASH POINT — §6038 automated penalties and Farhy** — The IRS implements §6038 penalties through automated Letter 6291 (initial penalty notice) and Letter 6292 (continuing failure). The notices are computer-generated based on AIR — the international information reporting database — and frequently misfire: filings made but not properly imaged, late-filed returns where the 5471 was on time but the 1040 was late, returns where the 5471 was attached but the cover sheet did not show it. The taxpayer must respond within 30 days with documentation. In Farhy v. Commissioner (160 T.C. No. 6, April 2023) the Tax Court held that the IRS lacks statutory authority to assess §6038(b) penalties — a major taxpayer win. The Court of Appeals for the DC Circuit reversed in May 2024 (Farhy v. Commissioner, No. 23-1179, D.C. Cir. May 3, 2024) and the Supreme Court declined certiorari, restoring the IRS's automated-assessment regime. As of 2025, the IRS resumed automated §6038 penalty assessment and is aggressively pursuing collection. Reasonable cause remains the primary defense.  _(Farhy v. Commissioner, 160 T.C. No. 6 (April 2023); Farhy v. Commissioner, No. 23-1179, D.C. Cir. (May 3, 2024))_

## 11. Reasonable cause and amnesty paths

A taxpayer with a missing Form 5471 has several avenues, each with different procedural rules and outcomes.

### 11.1 §6038(c)(4) reasonable cause

- **Reasonable cause defense elements** — The general reasonable-cause defense applies to §6038(b) penalties. The taxpayer must demonstrate (a) ordinary business care and prudence, (b) good faith, and (c) facts and circumstances supporting the failure. Common reasonable-cause grounds include reliance on competent tax advisor (with documentation of the engagement, the advisor's qualifications, and the specific advice given), serious illness or family emergency, casualty or natural disaster, and inability to obtain records (subject to limitations under Treas. Reg. §301.6038-2(k)). Reasonable cause is asserted by responding to the §6038 notice with a written statement and supporting documentation, and by filing the delinquent Form 5471 simultaneously. There is no specific form; a cover letter with the delinquent return and the reasonable-cause statement is sufficient.  _(§6038(c)(4); §6038(b); Treas. Reg. §301.6038-2(k))_

### 11.2 Streamlined Foreign Offshore Procedures (SFOP)

- **SFOP requirements and effect** — SFOP is for US persons resident outside the United States who failed to file Form 5471 (and/or FBAR, and/or report foreign income) for non-wilful reasons. The procedure requires: - A non-residency certification — physical presence outside the US for at least 330 full days in any one of the most recent three tax years. - Filing of the three most recent delinquent or amended income tax returns including all required international information returns. - A non-wilfulness certification under penalty of perjury — a detailed written statement explaining the failures. - Filing of the six most recent years of delinquent FBARs. - Payment of all unpaid tax and interest for the three years. In exchange, SFOP waives all penalties including §6038 penalties. The non-wilfulness certification is the gating item; the IRS scrutinises certifications closely and rejected certifications result in full penalty exposure plus potential criminal referral. SFOP is unavailable to taxpayers under IRS examination or criminal investigation.  _(§6038)_

### 11.3 Streamlined Domestic Offshore Procedures (SDOP)

- **SDOP requirements and penalty** — SDOP is for US persons resident in the United States with the same non-wilfulness profile. Same procedure as SFOP except the residency facts differ and the penalty waiver is partial: SDOP imposes a 5% miscellaneous offshore penalty computed on the highest year-end aggregate balance of unreported foreign financial assets over the six-year FBAR look-back. The 5% penalty replaces all §6038 and other information-return penalties. SDOP is unavailable under examination or criminal investigation. percent of highest year-end aggregate balance  _(§6038)_

### 11.4 Delinquent International Information Return Submission Procedures (DIIRSP) — historical

- **DIIRSP history and current status** — DIIRSP was the IRS's standalone amnesty for delinquent Forms 5471, 5472, 8865, 8938, 3520, and similar, where the taxpayer's tax position was correct (no unreported income or tax). The procedure was modified in November 2020 to eliminate the explicit penalty waiver and to require a reasonable-cause statement, effectively folding DIIRSP into the general §6038(c)(4) reasonable-cause framework. As of 2025, DIIRSP is no longer a separate identifiable amnesty — taxpayers in the DIIRSP profile simply file delinquent under reasonable cause.  _(§6038(c)(4))_

### 11.5 Voluntary Disclosure Practice (IRM 9.5.11.9)

- **Voluntary Disclosure Practice outcomes** — For wilful failures with material unreported income or tax, the IRS Voluntary Disclosure Practice is the path. It is administered by Criminal Investigation, requires a pre-clearance, and produces a closing agreement that typically imposes a 75% civil fraud penalty on the highest tax year and full §6038 penalties — but eliminates criminal exposure. The Voluntary Disclosure Practice is unavailable once an audit or criminal investigation is underway. Most Form 5471 failures do not require this path; reasonable cause and SFOP/SDOP cover the vast majority of cases. percent  _(IRM 9.5.11.9; §6038)_

## 12. Common errors

The following errors are the most frequent at audit and on review:

1. Missing constructive ownership under §318 family attribution. A taxpayer holds 8% of a foreign corp directly but their spouse holds another 4%. Spousal attribution under §318(a)(1) makes the taxpayer a 12% owner — a US shareholder — and triggers Cat 5 filing. Frequently missed at intake.

2. Failure to file Cat 2 when a relative inherits stock and crosses 10%. A US person serves on the foreign corp's board with zero equity. The founder's child (a US person) inherits stock and crosses 10%. The board member becomes a Cat 2 filer. The board member typically has no idea.

3. Not filing for a dormant CFC. A CFC with no income, no employees, and no activity is still a CFC if the ownership tests are met. Cat 5 filing remains required, with limited schedules. Rev. Proc. 92-70 provides a 'summary filing' for dormant CFCs — Schedule A, the identification section, and a statement of dormancy — but the filing must be made.

4. Cat 5 filer assuming a pass-through partnership absorbs the obligation. A US partnership owns a CFC; the partnership files Form 5471 at the partnership level. Each US partner that is itself a 10% indirect US shareholder under §958(a) attribution through the partnership must also file their own Form 5471 (unless they qualify for the multiple-filer exception with cross-statements). The partnership filing does not automatically discharge the partners.

5. Failure to attach Subpart F and GILTI worksheets. Schedule I reports the inclusion amount but the IRS expects a detailed worksheet showing the §954 categorisation, the §952(c) E&P cap, and the §951(a)(2) pro rata share allocation. Omission of the worksheet is a frequent inadequate-disclosure finding.

6. Inconsistent §954(b)(4) high-tax elections across consenting shareholders. The election must be uniformly made or not made across all controlling-shareholder-group filings. A discrepancy between two Forms 5471 covering the same CFC voids the election.

7. Missing PTEP basket assignments on Schedule P. Schedule P columns must show §904(d) basket. Taxpayers who lump all PTEP into a single column lose the foreign-tax-credit traceability and may face FTC disallowance at distribution.

8. Incorrect functional-currency conventions on Schedule C and Schedule F. Income statement uses weighted-average rate; balance sheet uses spot rate. Mixing the two is a common reconciliation failure that flags an audit-priority discrepancy.

9. Forgetting Schedule O when ownership crosses 10% for the first time. The initial acquisition is a Cat 3 event with Schedule O Part II required. Year-1 filers who only complete the Cat 5 schedules and skip Schedule O have an incomplete return and may be subject to §6038 penalty notwithstanding the substantive Cat 5 completion.

10. §958(b)(4)-driven 'sister CFC' Cat 5 filings ignored. Discussed at §2.5 and §3 above. The most under-recognised filing trigger post-TCJA.

11. Treating §245A dividends as PTEP. §245A dividends-received deduction operates differently from PTEP; the §245A treatment does not transit Schedule P (except for §245A(d) hybrid dividends which have their own PTEP group post-2024 revision).

12. Late filing of the 1040 voids on-time 5471. If the 1040 is late and on extension that was missed, the 5471 attached to it is also late notwithstanding that the 5471 itself was prepared on time. The 5471 due date is the 1040 due date.

### Example A — Small US individual owning 100% of Singapore Pte Ltd

**Facts.** Sarah is a US citizen resident in Texas. In March 2024 she incorporated a Singapore private limited company, Acora Pte Ltd, to provide software consulting services to Asian clients. She owns 100% of the share capital. For Singapore tax year 2025 (calendar year matching her US tax year), Acora Pte Ltd had:
- Revenue: SGD 480,000 (services to unrelated Asian clients)
- Operating expenses: SGD 180,000 (salaries to two Singapore employees, rent, software)
- Net income: SGD 300,000 (≈ USD 222,000 at average rate)
- Singapore corporate tax: SGD 24,300 (8.1% effective rate after partial exemption)
- Net after-tax: SGD 275,700 (≈ USD 203,500)
- Distributions to Sarah: SGD 100,000 (≈ USD 73,500) paid in November 2025
- Tangible business assets: laptops and office equipment, average adjusted basis USD 12,000

**Filing analysis.**

1. **CFC status**: Sarah owns 100% by both vote and value. She is a US shareholder under §951(b) (10%+). US shareholders own 100% of vote and value, exceeding the 50% threshold. Acora Pte Ltd is a CFC under §957(a).

2. **Filing category**: Sarah is a Cat 5a filer (controlling US shareholder, owns stock on last day of CFC's tax year). She also met Cat 4 control (>50% for 30+ days) and Cat 3 acquisition (initial 2024 acquisition crossed 10% — but Cat 3 was 2024's filing event; for 2025 she is Cat 5a unless other Cat 3 events occurred). The November 2025 distribution is not a Cat 3 event (she did not drop below 10%).

3. **Subpart F analysis**: services revenue from unrelated Asian clients is not FBCSI-svc (services for related parties only); not FPHCI (active services income); not FBCSI (no purchase/sale of property). Subpart F income = $0.

4. **GILTI analysis**:
 - Tested income = $222,000 (net income before US tax; less the $0 Subpart F; less Singapore tax of $18,000 if deductible — but tested income is computed before US tax and includes foreign tax as a deduction in computing net tested income).
 - Net tested income = ~$222,000 less Singapore tax = ~$204,000.
 - QBAI = $12,000; DTIR = 10% × $12,000 = $1,200.
 - Specified interest expense = $0.
 - GILTI inclusion = $204,000 - $1,200 = $202,800.

5. **§954(b)(4) high-tax election**: Singapore effective rate is 8.1%. Threshold is 18.9%. Sarah does NOT qualify for the high-tax exclusion. GILTI inclusion stands.

6. **§962 election analysis**: As an individual at the 37% rate, Sarah's GILTI would tax at $202,800 × 37% = $75,036, less her share of Singapore tax (zero individual-level FTC available without §962). With §962 election: GILTI of $202,800, §250 deduction of $101,400 (50%), taxable GILTI of $101,400, US corporate tax at 21% = $21,294, deemed-paid FTC of $18,000 (with §960 mechanics and §78 gross-up) — net US tax in the range of $4,000-$6,000. The §962 election saves ~$70,000 in current US tax for Sarah, at the cost of a second layer of tax when she distributes the post-§962 PTEP. For her facts, the §962 election is strongly indicated; she should sign the election statement and attach it to her 1040.

7. **Distribution treatment**: The $73,500 distribution in November 2025 is sourced first from §959(c)(2) PTEP (the GILTI inclusion). The GILTI inclusion of $202,800 (without §962) or post-§962 PTEP creates ample PTEP cover, so the distribution is excluded from gross income under §959(a). §986(c) foreign currency gain/loss may apply if the distribution rate differs from the inclusion rate.

8. **Form 5471 schedules required**: A, B, C, E, E-1, F, G, H, I, I-1, J, M, P, Q, R. Schedule M reports the distribution. Schedule O is not required (no organisation event in 2025).

9. **Other forms**: Form 8992 for the GILTI computation; Form 1116 for the foreign tax credit (if §962); §962 election statement; Form 1040 Schedule 1 for the GILTI inclusion. FBAR (FinCEN 114) for the Singapore corporate bank account if balance exceeded $10,000 (almost certainly yes). Form 8938 if specified foreign financial asset thresholds met.

### Example B — US C corporation with German GmbH subsidiary

**Facts.** Cutajar Software Inc., a Delaware C corporation, owns 100% of Cutajar Deutschland GmbH, a German limited liability company that develops software for European customers. For 2025:
- GmbH revenue: EUR 4,200,000 (services and license fees from unrelated EU customers)
- GmbH expenses: EUR 3,100,000 (salaries, rent, R&D, German depreciation under §168 ADS-conformed)
- GmbH net income: EUR 1,100,000 (≈ USD 1,210,000 at average rate)
- GmbH German tax (Körperschaftsteuer + Gewerbesteuer + Solidaritätszuschlag): EUR 330,000 (30% effective rate)
- GmbH after-tax: EUR 770,000 (≈ USD 847,000)
- QBAI: GmbH owns office equipment and servers, average adjusted basis EUR 240,000 (USD 264,000)
- Intercompany license payment from GmbH to Cutajar Software Inc. for use of US-developed IP: EUR 80,000 (royalty)
- Intercompany dividend from GmbH to parent: EUR 500,000 (November 2025)

**Filing analysis.**

1. **CFC status**: Cutajar Software Inc. owns 100%. GmbH is a CFC.

2. **Filing category**: Cat 4 (control >50%) and Cat 5a (controlling US shareholder). Single Form 5471 with both boxes checked.

3. **Subpart F**:
 - Services revenue: not FBCSI-svc (services to unrelated customers); not FPHCI.
 - License fees to unrelated EU customers: not FPHCI (active business, §954(c)(2)(A) active royalty exception likely applies given the substantial R&D operation in Germany).
 - The intercompany royalty paid BY GmbH to the US parent reduces GmbH's net income but is not GmbH's Subpart F (it is the parent's US-source income).
 - The intercompany dividend received by Cutajar Software Inc. is a §245A "Section 245A dividend" eligible for the 100% dividends-received deduction (German corp, more than one-year holding, etc.) — separate analysis, reported on Form 1120 Schedule C and flagged on Schedule G of the 5471.
 - Subpart F = $0.

4. **GILTI**:
 - Tested income = $1,210,000 - German tax of $363,000 ≈ $847,000.
 - QBAI = $264,000; DTIR = $26,400.
 - GILTI inclusion = $847,000 - $26,400 = $820,600.

5. **§954(b)(4) high-tax election**: German effective rate is 30%, well above the 18.9% threshold. The election is available and would exclude the GmbH's tested income from GILTI. The election is made on Schedule I-1 by Cutajar Software Inc. as the controlling shareholder. With the election: GILTI inclusion = $0. This is the obvious choice for high-tax CFCs and is the principal post-2020-regulations planning point.

6. **§245A dividend**: the EUR 500,000 distribution, to the extent not sourced from PTEP, is a Section 245A dividend with 100% DRD. Schedule R reports it; Form 1120 Schedule C Line 14 reports the gross dividend; Form 1120 Schedule C Line 28 reports the DRD.

7. **Schedule J PTEP**: with the high-tax election made, the GmbH has no GILTI PTEP. The dividend is sourced from §959(c)(3) E&P (not PTEP) and qualifies for §245A.

8. **§960 deemed-paid FTC**: with no GILTI inclusion (high-tax election), no §960 credit. The German tax of $363,000 reduces GmbH's E&P but does not flow to the US parent through the FTC mechanism — a cost of the high-tax election. Run the math both ways: GILTI inclusion + §250 + §960 vs. high-tax exclusion + §245A. For a high-tax CFC, the §245A path typically wins because the §250 deduction is only 50% (not 100%) and the §960 credit is haircut at 80% under §960(d)(1).

9. **Schedules required**: A, B, C, E, E-1, F, G, H, I, I-1 (with high-tax election line), J, M, P, Q, R. Schedule M reports the intercompany royalty payment from GmbH to parent.

10. **Other forms**: Form 8992 reflecting the elected-out income; Form 1118 (corporate FTC) if §960 credit is used elsewhere; Form 8975 country-by-country report if Cutajar Software Inc. is part of a multinational group exceeding $850M revenue (likely not for this size).

### Example C — Family attribution catching an unaware Cat 5 filer

**Facts.** Mark is a US citizen living in California. Mark's father, Joseph, is a US citizen living in Florida and has, for 20 years, owned 60% of an active manufacturing corporation in Mexico, Industrias Joseph S.A. de C.V. Joseph has filed Form 5471 every year. Mark has never been involved in the business, has never received a distribution, and owns no shares directly. In April 2025 Joseph dies and his estate (a US estate) inherits the 60%. The estate is in administration through end of 2025. Joseph's will divides his estate 50/50 between Mark and Mark's sister Anna (also a US citizen).

**Filing analysis.**

1. **Mark's direct ownership of Industrias Joseph S.A.**: 0%.

2. **Mark's §958(a) indirect ownership through the estate**: An estate is treated as owned by its beneficiaries under §958(a)(2) only if and to the extent of the beneficiaries' interests. Mark is a 50% beneficiary; the estate's 60% × Mark's 50% = 30% indirect §958(a) ownership.

3. **§958(b) constructive ownership**: Under §318(a)(2)(A) (estate-to-beneficiary attribution), the estate's stock is attributed to its beneficiaries to the extent of their interest. This duplicates the §958(a) result for Mark (30%).

4. **US shareholder status**: Mark owns 30% indirectly. He is a US shareholder under §951(b).

5. **CFC status**: US shareholders (Mark 30%, Anna 30% — same analysis — and the estate which holds 60% but is itself a US person owning through Joseph's residual estate interests; or alternatively the estate is the §958(a) owner with Mark and Anna as beneficiaries) collectively own well over 50%. Industrias Joseph S.A. is a CFC.

6. **Filing requirement**: Mark is a Cat 5 filer for 2025 (and Cat 3 for the inheritance event in April 2025 which crossed Mark's ownership above 10%). Mark must file his own Form 5471 attached to his 2025 Form 1040, due April 15, 2026 (October 15 with extension), with Schedules A, B, C, E, E-1, F, G, H, I, I-1, J, P, Q, R, and Schedule O for the inheritance event.

7. **Mark's likely state of awareness**: zero. Mark has never thought about his father's Mexican business and has no relationship with the company management. Mark and his preparer must coordinate with the estate executor, who has the books and records of Industrias Joseph S.A. The estate executor is a Cat 4 filer in their own right (control of the foreign corp through the estate).

8. **Possible relief**: Mark may qualify as a Cat 5c filer (related constructive owner of a Cat 5a controlling shareholder) if the estate (or a sibling) is a Cat 5a filer who files a complete Form 5471 covering all schedules. If so, Mark may rely on the multiple-filer exception and file a reduced return. The Cat 5a filer must attach a statement listing Mark as a Cat 5c filer relying on the exception, and Mark must attach a corresponding statement to his return.

9. **Penalty exposure if missed**: $10,000 §6038 penalty for 2025; if Mark continues to miss in 2026 and 2027 before discovery, $30,000+ exposure. §6501(c)(8) keeps Mark's 2025, 2026, 2027 1040s open indefinitely for assessment until the 5471s are filed.

10. **Practitioner action**: at any 1040 intake where a parent owned a foreign business, ask about death events and inheritances. Family attribution catches this scenario.

## 14. Closing notes

Form 5471 is the most administratively burdensome and most penalty-exposed information return in the US international tax system. The five-category framework, the eleven schedules, the §951/§951A inclusion mechanics, the §959 PTEP tracking, the §954 categorisation, and the §954(b)(4) high-tax election form a tightly interlocking system that demands year-round attention, not just April-15 attention.

Three practitioner disciplines reduce penalty exposure to near-zero:

1. **Year-end ownership review** — every 1040 and 1120 intake includes a deliberate question about direct, indirect, and constructive ownership of any foreign corporation. The §958(b)(4) "sister CFC" trap and the §318 family attribution trap require explicit inquiry.

2. **PTEP discipline** — maintain Schedule J and Schedule P with year-by-year layers, basket assignments, and currency translation rates from year of inclusion. PTEP balances are decade-spanning records and lose value rapidly when not maintained.

3. **High-tax election analysis** — every CFC with effective foreign tax above 18.9% should have a documented analysis of the §954(b)(4) election, with the run-the-math comparison of (a) GILTI + §250 + §960 vs. (b) high-tax exclusion + §245A. The wrong choice — silently defaulting to "no election" because no one ran the analysis — costs real money on high-tax-jurisdiction CFCs.

A reviewer Circular 230 sign-off on a Form 5471 should confirm: filing category correctly identified, all required schedules present, Schedule I reconciles to Schedule J PTEP movements, Schedule E-1 deemed-paid FTC ties to Schedule Q income groups, Schedule M intercompany transactions reconcile to the underlying intercompany agreements, the §954(b)(4) election (or its absence) is documented with the effective rate computation, and any §962 election by an individual shareholder is signed and attached. The skill defers all amount computations to the underlying corporate accounting records and the reviewer's substantive review; this skill provides the structural map.

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is
different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your
jurisdiction — **no liability on either side until you and the accountant sign
a formal engagement letter** — book a free 30-minute call:

**→ [Book a call](https://calendly.com/openaccountants-info/30min)**

We'll route you to the named verifier covering your country or state. You can
also see the full list of verified accountants at
[openaccountants.com/network](https://openaccountants.com/network).
