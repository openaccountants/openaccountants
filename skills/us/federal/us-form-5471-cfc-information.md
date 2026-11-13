---
name: us-form-5471-cfc-information
description: Decide whether a US person must file Form 5471 for a foreign corporation in tax year 2026, which filer category or categories apply (1a to 1c, 2, 3, 4, 5a to 5c), and which schedules follow, using the December 2025 Form 5471 and its instructions. Covers the 10% US shareholder and more-than-50% CFC tests with family and entity attribution, the filing exceptions (constructive owners, joint filers, foreign-controlled CFCs under Rev. Proc. 2019-40, dormant corporations under Rev. Proc. 92-70), the $10,000 penalties under sections 6038 and 6679 with the $50,000 continuing-failure cap, the foreign tax credit reduction, the open statute under section 6501(c)(8), and the routes to fix missed years. Explains the One Big Beautiful Bill Act changes that reach Form 5471 from 2026 (GILTI renamed net CFC tested income, the one-month deferral election repealed, section 958(b)(4) restored with new section 951B, the new pro rata share rule). Trigger on "Form 5471", "CFC", "controlled foreign corporation", "foreign company owner", "5471 penalty", "Category 4", "Category 5", "US shareholder of a foreign corporation". The NCTI (GILTI) computation itself is in us-gilti-fdii-beat. Federal only.
version: "2.1"
jurisdiction: US
tax_year: 2026
last_updated: 2026-11-13
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: formation
type: situation-rules
---

# US Form 5471: who files, which category, which schedules, tax year 2026

> **Source-cited draft.** Built from Form 5471 (Rev. December 2025) and its instructions (Rev. December 2025), Public Law 119-21 (the One Big Beautiful Bill Act), 26 U.S.C. 11, 318, 951, 954, 957, 958, 6038, 6046, 6072, 6501 and 6679 on govinfo.gov, and the IRS pages on the streamlined filing compliance procedures and delinquent international information returns, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** A US person files Form 5471 for a foreign corporation when they fall into at least one of five filer categories. The two that catch most people: **Category 5**, a US shareholder (10% or more of vote or value, counting family and entity attribution) of a controlled foreign corporation (more than 50% owned by US shareholders), and **Category 4**, a US person who controlled the corporation (more than 50% of vote or value) at any time in their tax year. Form 5471 is attached to the filer's own income tax return and is due with it, extensions included. Missing it costs **$10,000** per foreign corporation per year under section 6038(b), plus up to **$50,000** more after an IRS notice, a cut in foreign tax credits, and an assessment period that stays open. For 2026 the form still reports the same categories, but the law under it changed: GILTI becomes "net CFC tested income" (computed in `us-gilti-fdii-beat`), the one-month deferral year for foreign subsidiaries is gone, and downward attribution from foreign persons is switched off again for foreign corporations' tax years beginning after 31 December 2025.

## Scope and who this is for

In scope: deciding, for one US person and one foreign corporation, whether Form 5471 is required for a 2026 tax year, which category boxes to check on item B, which schedules to attach, the exceptions that remove or reduce the filing, the deadline, the penalties, and how to fix missed years. US persons include citizens, residents, domestic partnerships, domestic corporations and domestic estates and trusts.

Out of scope, and where it goes:

| Topic | Skill |
| --- | --- |
| Computing net CFC tested income (formerly GILTI), the section 250 deduction, the section 962 election and the section 960 deemed-paid credit | `us-gilti-fdii-beat` |
| Subpart F income categories (foreign personal holding company income, base company sales and services income, insurance income) and the CFC working paper | `us-gilti-fdii-beat` |
| Foreign tax credit on Form 1116 for an individual | `us-foreign-tax-credit-1116` |
| Form 5472, foreign-owned US corporations and disregarded entities | `us-form-5472-foreign-owned-us` |
| FBAR (FinCEN 114) and Form 8938 | `us-fbar-and-fatca-8938` |
| Forms 3520 and 3520-A, foreign trusts and gifts | `us-foreign-trust-reporting` |
| The corporate return the form attaches to, including fiscal-year due dates | `us-form-1120-c-corp` |
| The partnership return the form attaches to | `us-form-1065-partnership` |
| Penalty abatement requests, appeals and collection after an assessment | `us-irs-collections-and-controversy` |
| Form 8865 (foreign partnerships) and Form 8621 (PFICs) | no skill yet: refer |

## Ask the client first

1. **The ownership chart on every day of the foreign corporation's 2026 tax year.** For each shareholder: name, US or foreign person, class of stock, number of shares, votes and value, and dates of every purchase, sale, issue or redemption. Category 4 is tested at any time in the filer's tax year; Category 5 looks at who owned stock on the last day the corporation was a CFC; Category 3 is triggered by the transaction itself.
2. **Family.** Shares owned by the client's spouse, children, grandchildren and parents (section 318(a)(1)), and whether each of them is a US citizen or resident. Stock of a nonresident alien relative is not attributed to a US citizen or resident for the CFC tests (section 958(b)(1)). Siblings are never attributed.
3. **Entities and estates in between.** Any partnership, corporation, trust or estate that owns shares, whether it is US or foreign, and the client's share of it. Foreign entities pass ownership up proportionately (section 958(a)(2)); US entities count only through constructive ownership (section 958(b)).
4. **Roles.** Is the client (or a US person related to them) an officer or director of the foreign corporation? That alone can create Category 2.
5. **The foreign corporation's tax year**, and whether it used the one-month deferral election under former section 898(c)(2). For a year beginning after 30 November 2025 that election is gone and the first year under the new rule may be short.
6. **Is anyone else filing?** Another US shareholder, the parent company or an estate executor may file a Form 5471 that covers the client (joint filers and constructive-owner exceptions).
7. **History.** Earlier Forms 5471 filed, any IRS notices (and their dates), section 965 balances still on Schedule J or P, and whether the client's returns for 2022 to 2025 omitted any foreign income.
8. **Accounts.** Functional currency, local financial statements, local tax paid, and any distributions, loans or payments between the corporation and its US shareholders.
9. **Deaths and inheritances.** At any intake where a parent or grandparent owned a foreign business, ask whether anyone died or an estate now holds the shares (Worked case 3).

## The method, step by step

### Rates, bands and thresholds

| Item | Amount or date | Source |
| --- | --- | --- |
| US shareholder: share of total combined voting power or of total value, directly, indirectly or constructively | 10% or more | [26 U.S.C. 951(b)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partIII-subpartF-sec951.htm) |
| Controlled foreign corporation: share of vote or value owned by US shareholders on any day of the foreign corporation's tax year | more than 50% | [26 U.S.C. 957(a)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partIII-subpartF-sec957.htm) |
| Category 4 control: share of vote or value owned at any time during the filer's tax year | more than 50% | [26 U.S.C. 6038(e)(2)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap61-subchapA-partIII-subpartA-sec6038.htm) |
| Category 2 and 3 stock ownership requirement (vote or value) | 10% or more | [Instructions for Form 5471 (Rev. December 2025)](https://www.irs.gov/pub/irs-pdf/i5471.pdf) |
| Category 2 exception: three or fewer US persons own this much of value after the acquisition | 95% or more | [Instructions for Form 5471 (Rev. December 2025)](https://www.irs.gov/pub/irs-pdf/i5471.pdf) |
| Foreign controlled US shareholder under new section 951B (section 958(b) applied without paragraph (4)) | more than 50 percent | [Public Law 119-21, section 70353](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| Section 958(b)(4) restored (no downward attribution from foreign persons) and section 951B in force: taxable years of foreign corporations beginning after | 31 December 2025 | [Public Law 119-21, section 70353(d)](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| One-month deferral election (former section 898(c)(2)) repealed: taxable years of specified foreign corporations beginning after | 30 November 2025 | [Public Law 119-21, section 70352(b)](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| GILTI renamed net CFC tested income, deemed tangible return (QBAI) repealed: taxable years beginning after | 31 December 2025 | [Public Law 119-21, section 70323](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| New section 951(a) pro rata share rule (any day of ownership): taxable years of foreign corporations beginning after | 31 December 2025 | [Public Law 119-21, section 70354(c)(1)](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| Section 954(c)(6) look-through made permanent: taxable years of foreign corporations beginning after | 31 December 2025 | [Public Law 119-21, section 70351](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| Penalty for failing to furnish section 6038 information, per annual accounting period of each foreign corporation | USD 10,000 | [26 U.S.C. 6038(b)(1)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap61-subchapA-partIII-subpartA-sec6038.htm) |
| Continuing failure: added for each 30-day period (or fraction) after 90 days from the IRS notice | USD 10,000 | [26 U.S.C. 6038(b)(2)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap61-subchapA-partIII-subpartA-sec6038.htm) |
| Cap on the continuing-failure addition, per failure | USD 50,000 | [26 U.S.C. 6038(b)(2)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap61-subchapA-partIII-subpartA-sec6038.htm) |
| Foreign tax credit reduction for a section 6038 failure | 10 percent | [26 U.S.C. 6038(c)(1)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap61-subchapA-partIII-subpartA-sec6038.htm) |
| Further reduction for each 3-month period (or fraction) after 90 days from notice | 5 percent | [26 U.S.C. 6038(c)(1)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap61-subchapA-partIII-subpartA-sec6038.htm) |
| Floor of the cap on the credit reduction (the cap is the greater of this or the corporation's income for the period) | USD 10,000 | [26 U.S.C. 6038(c)(2)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap61-subchapA-partIII-subpartA-sec6038.htm) |
| Penalty for failing to file section 6046 information (Category 2 and 3, Schedule O) | USD 10,000 | [26 U.S.C. 6679(a)(1)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapB-partI-sec6679.htm) |
| Section 6046 continuing failure: per 30-day period after 90 days from notice, capped at USD 50,000 | USD 10,000 | [26 U.S.C. 6679(a)(2)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapB-partI-sec6679.htm) |
| Assessment period stays open until this long after the missing information is furnished | 3 years | [26 U.S.C. 6501(c)(8)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap66-subchapA-sec6501.htm) |
| High-tax exception: foreign effective rate must be greater than this share of the top section 11 rate | 90 percent | [26 U.S.C. 954(b)(4)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partIII-subpartF-sec954.htm) |
| Corporate income tax rate (section 11), so the high-tax line is 90% x 21% = 18.9% | 21 percent | [26 U.S.C. 11(b)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partII-sec11.htm) |
| Form 8833 treaty-position disclosure penalty (C corporation: USD 10,000) | USD 1,000 | [Instructions for Form 5471 (Rev. December 2025)](https://www.irs.gov/pub/irs-pdf/i5471.pdf) |
| Streamlined foreign offshore procedures: days physically outside the US, with no US abode, in one of the last 3 years | 330 full days | [IRS, U.S. taxpayers residing outside the United States](https://www.irs.gov/individuals/international-taxpayers/u-s-taxpayers-residing-outside-the-united-states) |
| Streamlined domestic offshore procedures: miscellaneous offshore penalty on the highest aggregate year-end balance | 5 percent | [IRS, U.S. taxpayers residing in the United States](https://www.irs.gov/individuals/international-taxpayers/us-taxpayers-residing-in-the-united-states) |

None of these amounts is indexed for inflation. The section 250 deduction rates and the section 960 deemed-paid percentage that apply to 2026 inclusions are owned by `us-gilti-fdii-beat` and are not restated here.

### Step 1: is the foreign corporation a CFC for its 2026 tax year?

1. List every US person who owns stock directly, indirectly through foreign entities (section 958(a)(2), proportionately) or constructively (section 958(b), which applies section 318(a) with changes).
2. For each, add up vote and value separately. Family attribution: spouse, children, grandchildren and parents (section 318(a)(1)); not siblings; not from a nonresident alien relative (section 958(b)(1)). Entity attribution: up from partnerships, estates, trusts and corporations to their owners (section 318(a)(2); for corporations the 50% threshold is read as 10% (section 958(b)(3)), and an entity owning more than 50% of the vote is treated as owning all of it (section 958(b)(2))). Down from owners to entities (section 318(a)(3)).
3. **Downward attribution from foreign persons, 2026 change.** For taxable years of foreign corporations beginning after 31 December 2025, section 958(b)(4) is back: stock owned by a foreign person is not attributed down to a US person under section 318(a)(3)(A) to (C). A foreign corporation that was a CFC only because a foreign parent's shares were attributed to its US subsidiary (the "sister CFC" of 2018 to 2025) stops being a CFC for those years. Source: [Public Law 119-21, section 70353](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm).
4. A US person with 10% or more of vote or value is a **US shareholder**. The value prong was added for foreign corporation years beginning after 31 December 2017; before that only votes counted, so no-vote stock no longer avoids the test. Add the stock (counted once, not once per person) owned by all US shareholders. More than 50% of vote or of value on any day of the foreign corporation's tax year makes it a **CFC**.
5. **Section 951B check (new).** If the corporation is not a CFC under step 4 but a single US person would own more than 50% if downward attribution still applied, that person is a "foreign controlled United States shareholder" and the corporation a "foreign controlled foreign corporation". Subpart F and net CFC tested income then apply to that person as if they were a US shareholder of a CFC. Treasury may extend the US shareholder and CFC treatment to "any reporting requirement" (section 951B(d)(1)). The December 2025 instructions do not yet say how such a person reports on Form 5471: see "Not yet confirmed" under Sources, and refer.

### Step 2: which category boxes on item B

Work through all five; one person can be in several. Source for every row: [Instructions for Form 5471 (Rev. December 2025)](https://www.irs.gov/pub/irs-pdf/i5471.pdf).

| Category | Who | Notes |
| --- | --- | --- |
| 1a, 1b, 1c | A US shareholder of a section 965 specified foreign corporation, who owned the stock on the last day it was one | Continues only while the corporation has section 965 E&P on Schedule J or the filer has section 965 PTEP on Schedule P. 1b: unrelated section 958(a) US shareholder of a foreign-controlled section 965 SFC; 1c: related constructive US shareholder of one; 1a: everyone else. Rule it out consciously; most small filers are not Category 1 |
| 2 | A US citizen or resident who is an officer or director of a foreign corporation in which a US person acquired stock meeting the 10% requirement, or an additional 10% | The officer or director needs no shares. The acquirer can be anyone US, including a relative who inherits |
| 3 | A US person who acquires stock reaching 10% (with or without stock already owned), becomes a US person while holding 10%, disposes of enough to fall below 10%, or is treated as a US shareholder under section 953(c) | Section 6046. Includes the immigrant who held 10% before becoming resident. Attach the statement of indebtedness to related persons and of subscribers |
| 4 | A US person who controlled the foreign corporation (more than 50% of vote or value) at any time during the filer's tax year | Control passes down a chain of more-than-50% holdings. There is no 30-day minimum |
| 5a, 5b, 5c | A US shareholder of a CFC who owned the stock on the last day in the year it was a CFC | 5b: unrelated section 958(a) US shareholder of a foreign-controlled CFC; 5c: related constructive US shareholder of a foreign-controlled CFC; 5a: everyone else |

A filer who is both Category 4 and Category 5a checks **only the Category 4 box** and leaves 5a blank, but completes everything both categories require. A joint filer checks only the boxes that apply to itself.

**Categories 1b, 1c, 5b and 5c in 2026.** These categories exist because downward attribution made foreign-controlled corporations CFCs. With section 958(b)(4) restored for foreign corporation years beginning after 31 December 2025, most of those corporations are no longer CFCs and the 5b and 5c filings fall away for those years. They still apply to the foreign corporation's last tax year that began on or before 31 December 2025 (for a calendar-year corporation, 2025, reported on the 2025 return filed in 2026).

### Step 3: which schedules

Separate Form 5471 for each foreign corporation. When a required schedule has nothing to report, file it with zero amounts. If more than one category applies, do not duplicate information but complete every item that any category requires. Source: the chart "Filing Requirements for Categories of Filers", [Instructions for Form 5471 (Rev. December 2025)](https://www.irs.gov/pub/irs-pdf/i5471.pdf), page 8.

| Category | Page 1 identifying information plus |
| --- | --- |
| 1a | Schedule B Part II, E, E-1, J, P |
| 1b | E and E-1 (only if claiming deemed-paid taxes under section 960), P |
| 1c | Schedule B Part II, E (E-1 may be left blank), G, G-1 |
| 2 | Schedule O Part I |
| 3 | Schedule A, B Part I, B Part II, C, F, G, G-1, O Part II |
| 4 | Schedule A, B Part I, B Part II, C, F, E, E-1, G, G-1, H, H-1 (applicable CAMT corporations only), I, I-1, J, M, P, Q, R |
| 5a | Schedule B Part II, E, E-1, G, G-1, H, H-1 (CAMT only), I, I-1, J, P, Q, R |
| 5b | E and E-1 (only if claiming section 960 deemed-paid taxes), H-1 (CAMT only), I, I-1, P, Q |
| 5c | Schedule B Part II, E (E-1 may be left blank), G, G-1, I-1 |

A sole owner of a CFC (Categories 4 and 5a) completes all six pages of Form 5471 and separate Schedules E, G-1, H, H-1 (if a CAMT applicable corporation), I-1, J, M, P, Q and R. Schedule O is added in any year with a Category 2 or 3 event.

What each schedule holds, in short:

| Schedule | Content | Revision in use |
| --- | --- | --- |
| A | Classes of stock and shares outstanding at the start and end of the year; each class listed separately | Form 5471, Dec 2025 |
| B | Part I: US shareholders of the corporation (section 951(b), direct, indirect or constructive); Part II: direct shareholders of the corporation | Form 5471, Dec 2025 |
| C | Income statement in functional currency and US dollars; the starting point for subpart F and tested income and for E&P on Schedule H | Form 5471, Dec 2025 |
| E, E-1 | Foreign income taxes paid, accrued or deemed paid, by separate category; E-1 is included with E. Feeds the section 901 and 960 credits | Dec 2021 |
| F | Balance sheet, start and end of year, on US tax principles, not local GAAP | Form 5471, Dec 2025 |
| G | Other information: yes/no questions on hybrids, elections, disregarded entities, section 304 transactions (new line 21) and the pro rata share transition rule (line 22a and new 22b); new question 3b on qualified business units with a different functional currency (Form 8964-TRA). The main source of audit questions: answer each one | Form 5471, Dec 2025 |
| G-1 | Cost sharing arrangements | Dec 2023 |
| H | Current earnings and profits under section 964, from book income with tax adjustments | Dec 2021 |
| H-1 | Pro rata share of CFC adjusted net income for the corporate alternative minimum tax | Dec 2024 |
| I | The shareholder's subpart F inclusion and related amounts, with Worksheet A | Form 5471, Dec 2025 |
| I-1 | CFC-level inputs for the tested income inclusion (still titled "Global Intangible Low-Taxed Income") | Dec 2021 |
| J | Accumulated E&P, by PTEP group | Dec 2020 |
| M | Transactions between the CFC and its shareholders or related persons (sales, rents, royalties, services, interest, loans, dividends); the main transfer-pricing data source | Dec 2021 |
| O | Part I: Category 2 acquisitions; Part II: Category 3 acquisitions, dispositions and reorganizations | Dec 2012 |
| P | The shareholder's previously taxed E&P (PTEP), by group, year and foreign tax credit basket | Dec 2020 |
| Q | CFC income by CFC income group; the bridge to the section 960 credit | Dec 2024 |
| R | Distributions from the foreign corporation, with the PTEP group they come from | Dec 2020 |

Translate amounts as each schedule's instructions say (income and taxes generally at the average rate under section 986(a); balance sheet at spot), and report every exchange rate as units of foreign currency per one US dollar, to at least four decimal places.

### Step 4: apply the exceptions

| Exception | Conditions | Applies to |
| --- | --- | --- |
| Constructive owner, another US person files | No direct interest; filer only because of constructive ownership from another US person; that person's Form 5471 reports everything required of the filer. No statement needed | Categories 1, 3, 4, 5 |
| Constructive owner, from a nonresident alien | No direct or indirect interest; required only because of constructive ownership from a nonresident alien | Categories 1, 4, 5 |
| No section 958(a) US shareholder | The corporation is foreign-controlled and no US shareholder owns stock within section 958(a) on the last day it was a CFC (Notice 2018-13, section 5.02) | Categories 1, 5 |
| Unrelated constructive US shareholder | Foreign-controlled corporation; filer owns no section 958(a) stock and is not related under section 954(d)(3) (Rev. Proc. 2019-40, section 8.04) | Categories 1, 5 |
| Category 2 | Immediately after the acquisition three or fewer US persons own 95% or more of value and the acquirer files as Category 3; or the person is a constructive owner and the person whose stock is attributed files | Category 2 |
| Multiple filers (joint return) | One person with the same or greater filing requirements files for the others and completes item H; each person named in item H attaches a statement to their own return, plus their own Schedule P if Category 1a, 1b, 4, 5a or 5b. 5b and 5c cannot file jointly. For Category 3, only a person with an equal or greater interest can file for another. Missing statements lose the exception | All categories |
| Section 953(d) insurance company | The foreign insurer elected to be treated as domestic and filed a US return | All categories |
| Dormant foreign corporation (Rev. Proc. 92-70) | Summary filing: page 1 only, labeled "Filed Pursuant to Rev. Proc. 92-70 for Dormant Foreign Corporation", with filer information, items A to C, tax year, the accounting period and items 1a to 1d. Satisfies sections 6038 and 6046 | All categories |
| Alternative information (Rev. Proc. 2019-40) | Items F and G on page 1: a code shows which safe-harbour alternative information was used for a foreign-controlled CFC | Mainly 5b |

### Step 5: what 2026 changes on the form and the inclusions

1. **Net CFC tested income replaces GILTI.** For taxable years beginning after 31 December 2025 the section 951A inclusion is "net CFC tested income", and the deemed tangible income return built on QBAI is repealed. Schedule I-1 still supplies the CFC-level inputs; the computation, the section 250 deduction rate and the section 960 credit share are in `us-gilti-fdii-beat`. Source: [Public Law 119-21, sections 70321 to 70323](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm).
2. **One-month deferral year repealed.** A specified foreign corporation (a CFC more than 50% owned by one US shareholder) must use its majority US shareholder's year. The election to use a year beginning one month earlier ends for years beginning after 30 November 2025. A corporation that was a specified foreign corporation on 30 November 2025 has a first year after that date that ends with the first required year, which can be short; the change is treated as made with consent. File a Form 5471 for that first required year; foreign taxes split between the short year and the next follow Notice 2025-72, with a statement under Schedule E column (j). Sources: [Public Law 119-21, section 70352](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm); [Instructions for Form 5471 (Rev. December 2025)](https://www.irs.gov/pub/irs-pdf/i5471.pdf).
3. **Pro rata share.** For CFC years beginning after 31 December 2025, each US shareholder that owns section 958(a) stock on any day of the CFC year includes the subpart F income attributable to the period it owned the stock while it was a US shareholder and the corporation a CFC. The inclusion goes in the shareholder's year that contains the last day it owned the stock in that CFC year. A seller during the year therefore has an inclusion it did not have before. For dividends paid before the first such year, the transition rule (Notice 2025-75) is reported on Schedule G line 22b and Schedule I Worksheet A line 46. Source: [Public Law 119-21, section 70354](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm).
4. **Downward attribution restored and section 951B added** (step 1, items 3 and 5).
5. **Section 954(c)(6) look-through made permanent** for foreign corporation years beginning after 31 December 2025: payments between related CFCs out of non-subpart F income stay out of foreign personal holding company income.

### Step 6: penalties and exposure

- **Section 6038(b):** USD 10,000 for each annual accounting period of each foreign corporation for which the information is not furnished on time (Form 5471 and Schedule M). If still missing 90 days after the IRS mails a notice, USD 10,000 more for each 30-day period or part, up to USD 50,000 per failure. Most a single corporation-year can cost under this section: USD 60,000.
- **Section 6038(c):** foreign taxes available for credit under sections 901 and 960 are cut by 10%, plus 5% for each 3-month period or part after the 90 days, capped at the greater of USD 10,000 or the corporation's income for the period, and reduced by any section 6038(b) penalty for the same period. For a shareholder relying on deemed-paid credits, this can cost more than the USD 10,000.
- **Section 6679 (Categories 2 and 3, Schedule O):** USD 10,000 per failure for each reportable transaction, plus USD 10,000 per 30-day period after 90 days from notice, capped at USD 50,000; not imposed where the failure is due to reasonable cause.
- **Section 6501(c)(8):** the time to assess any tax on the return to which the information relates does not run out until 3 years after the information is furnished. With reasonable cause, only the items related to the failure stay open.
- **Criminal:** sections 7203, 7206 and 7207 can apply to the information required by sections 6038 and 6046.
- **Accuracy:** section 6662(j) can add a penalty on undisclosed foreign financial asset understatements.
- **A late return makes the form late.** Form 5471 is on time only if the return it is attached to is filed by its due date, extensions included.
- **Who is liable when someone else files.** A person who agrees to let another person file the form and Schedules J, M or O for them can still be penalized if that filing is wrong or missing.
- **Rev. Proc. 2019-40, section 7** waives certain section 6038 and 6662 penalties for certain persons in foreign-controlled structures.

Reasonable cause works by moving the start of the time limits: the deadline and the 90-day period are treated as not earlier than the last day reasonable cause existed (section 6038(c)(4)(B)). It needs ordinary business care and prudence, shown in writing with evidence (for example, documented reliance on a competent adviser who was given all the facts, serious illness, disaster, or records that could not be obtained).

### Step 7: fixing missed years

| Situation | Route | What it costs |
| --- | --- | --- |
| All income was reported and tax paid; only Form 5471 is missing; no IRS contact, exam or investigation | Delinquent international information return submission procedures: attach the late Form 5471 to an amended return, with a reasonable cause statement | Penalties may still be assessed in the normal way and the statement may only be considered later; be ready to answer IRS letters |
| Unreported foreign income as well, non-willful, client lives abroad (no US abode and 330 full days outside the US in one of the last 3 years) | Streamlined foreign offshore procedures: 3 years of returns with all information returns, 6 years of FBARs, Form 14653, tax and interest | No information return, accuracy, failure-to-file or FBAR penalties if all instructions are followed |
| Same, but client lives in the US and filed returns for the last 3 years | Streamlined domestic offshore procedures: 3 years of amended returns with information returns, 6 years of FBARs, Form 14654 | 5% miscellaneous offshore penalty on the highest aggregate year-end balance of the assets it covers, instead of information return penalties |
| Willful failure, or under exam or investigation | Refer: IRS Criminal Investigation Voluntary Disclosure Practice or counsel | Outside this skill |

Streamlined procedures are for failures to report income from foreign financial assets. A client whose only failure is the information return, with all income reported, goes through the delinquent information return route, not streamlined. Neither streamlined route is open to a taxpayer under civil exam or criminal investigation, and a non-willfulness certification is signed under penalty of perjury. Sources: [IRS streamlined filing compliance procedures](https://www.irs.gov/individuals/international-taxpayers/streamlined-filing-compliance-procedures); [IRS delinquent international information return submission procedures](https://www.irs.gov/individuals/international-taxpayers/delinquent-international-information-return-submission-procedures).

### Step 8: related items reported elsewhere (pointers only)

- The shareholder's inclusions flow to Form 1040 Schedule 1, line 8n (section 951(a) inclusion) and line 8o (section 951A(a) inclusion) on the 2025 Schedule 1; check the 2026 line numbers when the 2026 schedule is out. Inclusions are ordinary income, not qualified dividends. Corporate filers: Form 1120 Schedule C (see `us-form-1120-c-corp`).
- Previously taxed E&P (section 959): inclusions create PTEP; distributions come out of PTEP first in section 959(c) order and are excluded from income; inclusions raise and PTEP distributions lower stock basis (section 961). Keep Schedules J and P by year, group and foreign tax credit basket every year. Currency gain or loss on PTEP distributions is ordinary (section 986(c)).
- Assets already reported on Form 5471 are not reported again on Form 8938.
- A treaty-based return position needs Form 8833 (USD 1,000 penalty, USD 10,000 for a C corporation).
- A section 338 election on a foreign target, a reportable transaction (Form 8886) or a foreign disregarded entity or branch (Form 8858) adds attachments; follow the instructions' "Additional Filing Requirements".

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Client owns 8% directly, spouse 4% | 12% by family attribution: a US shareholder. Siblings' stock would not count |
| Parent is a nonresident alien holding 40% | Not attributed to the US child for the CFC and US shareholder tests (section 958(b)(1)) |
| 51% of value, 30% of vote (preferred stock) | Category 4 and CFC tests are vote or value: still control |
| Officer or director with no shares, a US investor buys 10% | Category 2 for the officer or director, with Schedule O Part I |
| Client became a US resident in 2026 holding 15% of a foreign company | Category 3 (becomes a US person while meeting 10%); Category 5 too if it is a CFC |
| First purchase reaching 10% in the year | Category 3 with Schedule O Part II, on top of the Category 5 schedules |
| Corporation had no income, no staff, no activity | Still a filing; the Rev. Proc. 92-70 summary filing may be used if it meets that procedure's definition of dormant |
| US partnership owns the CFC | The partnership files; each US partner that is itself a US shareholder through it files too, unless an exception (joint filer or constructive owner) applies |
| Foreign parent, US subsidiary, foreign sister company: tax year of the sister beginning in 2025 | Downward attribution applies: sister may be a CFC; US subsidiary is 5c, a 10% indirect US owner of the parent is 5b; check the Notice 2018-13 and Rev. Proc. 2019-40 exceptions |
| Same structure, sister's tax year beginning on or after 1 January 2026 | Section 958(b)(4) applies: no downward attribution; sister is not a CFC on that basis. Check section 951B for any US person over 50% without the restriction, and refer |
| Category 4 and 5a filer | Check only the 4 box; complete all six pages and the separate schedules for both |
| Same corporation reported by two consenting shareholders with different high-tax elections | Not allowed: the high-tax exception election is made by the controlling domestic shareholders and binds the group; the forms must agree |
| Return filed late without extension | Form 5471 is late too, even if ready on time |
| Inherited shares through a US estate | The estate is the section 958(a) owner; beneficiaries own constructively under section 318(a)(2)(A) (Worked case 3) |
| Section 245A dividend from the CFC to a US corporation | Not PTEP; report on Schedule R and flag on Schedule G; the deduction is on Form 1120 |
| CFC tax year ends 30 June 2026, shareholder on the calendar year | Reported on the shareholder's 2026 return (the year in which the CFC year ends) |

### Red flags at review

| Red flag | Why it matters |
| --- | --- |
| Spouse, parent or child holds shares and the intake did not ask | Family attribution is the most missed route to US shareholder status |
| A US board member with no shares, and a relative or investor crossed 10% | Category 2 filing the board member rarely knows about |
| "Dormant" company with no Form 5471 at all | Still required; at least the Rev. Proc. 92-70 summary filing |
| Partnership files and the partners assume they are covered | Partners who are US shareholders through it file unless an exception is met and documented |
| Schedule I inclusion with no supporting working paper (subpart F categories, E&P limit, pro rata share) | Weak support at exam; keep the working paper from `us-gilti-fdii-beat` |
| Schedule P with PTEP lumped in one column, no basket or year | Credit and exclusion on later distributions can be lost; reconcile every year |
| Average and spot rates mixed between Schedules C and F | Reconciliation failure that draws attention |
| First year over 10% filed with Category 5 schedules only | Schedule O Part II missing: incomplete form |
| Section 965 PTEP balances never reconciled | Category 1 continues and later deemed-paid credits may be lost |
| Penalty notice for a form that was in fact filed | Automated notices misfire (form not imaged, return late but form on time); answer by the notice's deadline with proof of filing |
| High-tax CFC (above 18.9%) with no documented high-tax election analysis | The election choice changes the inclusion; run it in `us-gilti-fdii-beat` |

### Defaults when a fact is missing

| Missing fact | Default |
| --- | --- |
| Whether a relative owns shares | Do not assume zero: ask, and hold the category decision |
| The foreign corporation's tax year | Ask; do not assume calendar year, especially for a former one-month deferral company |
| Whether another US person files for the client | Assume the client files their own Form 5471 until a copy of the other filing is in hand |
| Dates of share changes during the year | Ask; the CFC test is met on any one day and Category 4 at any time |
| Whether earlier years were filed | Assume not, and check the transcripts before choosing a Step 7 route |

## Worked cases

**Case 1, a decision: which category, which schedules?** Dana, a US citizen, has owned 8% of the only class of stock of a Portuguese company since 2023. Her husband, also a US citizen, owns 4%. Dana's US-citizen brother owns 40%. Foreign individuals own the remaining 48%. Nothing was bought or sold in 2026; Dana is not an officer or director.

Dana counts her own 8% plus her husband's 4% (section 318(a)(1)(A)(i)): 12%, so she is a US shareholder. The brother's 40% is not attributed to her (no sibling attribution), but he is a US shareholder on his own. Stock owned by US shareholders: 8% + 4% + 40% = 52%, more than 50%, so the company is a CFC. Dana's 12% is far from control, so not Category 4. No acquisition in 2026, so not Category 3. Dana is **Category 5a**: page 1 plus Schedule B Part II, E, E-1, G, G-1, H, I, I-1, J, P, Q and R. Her husband (also 12%, with a direct interest) is Category 5a as well; the constructive-owner exception does not apply to either of them because each owns shares directly, but they may file one joint Form 5471 with item H completed and a statement plus Schedule P attached to the other return.

The other way: if the brother owned 35% (foreigners 53%), US shareholders would own 47%. The company is not a CFC, so no Category 5, and with no acquisition and no control, **no Form 5471** for 2026. The 3-point difference decides the whole filing; confirm the share register on every day of the year, since the CFC test is met on any one day.

```oa-check
name: Category decision, Dana, 2026 (CFC at 52%, not at 47%)
inputs:
  dana_direct: 0.08
  spouse_direct: 0.04
  brother_direct: 0.40
  brother_alternative: 0.35
steps:
  - dana_counted: dana_direct + spouse_direct
  - us_shareholder_flag: 1 - ceil(clamp(0.10 - dana_counted, 0, 1))
  - us_shareholder_stock: dana_direct + spouse_direct + brother_direct
  - cfc_flag: ceil(clamp(us_shareholder_stock - 0.50, 0, 1))
  - category_4_flag: ceil(clamp(dana_counted - 0.50, 0, 1))
  - us_shareholder_stock_alternative: dana_direct + spouse_direct + brother_alternative
  - cfc_flag_alternative: ceil(clamp(us_shareholder_stock_alternative - 0.50, 0, 1))
expected:
  dana_counted: 0.12
  us_shareholder_flag: 1
  us_shareholder_stock: 0.52
  cfc_flag: 1
  category_4_flag: 0
  us_shareholder_stock_alternative: 0.47
  cfc_flag_alternative: 0
```

The flags read 1 for yes and 0 for no. The CFC test is "more than 50%", so exactly 50% gives 0; the US shareholder test is "10% or more", so exactly 10% gives 1.

**Case 2, penalty exposure for missed years.** Leo, a US citizen in Texas, wholly owns two foreign companies and filed no Form 5471 for 2023, 2024 or 2025 (six failures, each a section 6038(b) failure as Category 4). One IRS notice covers all six. He files everything 150 days after the notice was mailed, with no reasonable cause accepted.

Base penalty: 2 companies x 3 years x USD 10,000 = USD 60,000. After the notice, 150 - 90 = 60 days remain, which is 2 periods of 30 days, so USD 20,000 more per failure (below the USD 50,000 cap), USD 120,000 in all. Total USD 180,000, before any foreign tax credit reduction under section 6038(c) (which is itself reduced by these penalties). The returns for 2023 to 2025 also stay open for assessment until 3 years after the forms are furnished (section 6501(c)(8)). If his income was all reported, the next step is the delinquent information return route with a reasonable cause statement for each form.

```oa-check
name: Section 6038(b) penalties, 2 corporations x 3 years, filed 150 days after notice
inputs:
  corporations: 2
  years: 3
  base_penalty: 10000
  days_after_notice: 150
  grace_days: 90
  period_days: 30
  continuing_cap: 50000
steps:
  - failures: corporations * years
  - base_total: failures * base_penalty
  - periods: ceil(max(days_after_notice - grace_days, 0) / period_days)
  - continuing_per_failure: min(periods * base_penalty, continuing_cap)
  - continuing_total: failures * continuing_per_failure
  - total: base_total + continuing_total
expected:
  failures: 6
  base_total: 60000
  periods: 2
  continuing_per_failure: 20000
  continuing_total: 120000
  total: 180000
```

**Case 3, inheritance through a US estate.** Joseph, a US citizen, owned 60% of a Mexican manufacturing company and filed Form 5471 every year. He died in April 2026; his US estate holds the 60% through the end of 2026, and his will splits the estate equally between his US-citizen children Mark and Anna. Mark owns no shares himself.

The estate is a US person and the section 958(a) owner of 60%: Category 4 (control) and 5a, so the executor files, checking box 4. Mark and Anna each constructively own 30% (section 318(a)(2)(A), estate to beneficiaries); as US shareholders they are Category 5 filers, but because they have no direct interest and are filers only through constructive ownership from another US person (the estate), the **constructive-owner exception** applies if the estate's Form 5471 reports everything required of them. Their preparer should get a copy of the estate's filing. Because they own nothing within section 958(a), Mark and Anna have no subpart F or tested income inclusion from the company for 2026; that falls on the estate. When the shares are distributed to them, each acquisition of 30% is a Category 3 event for that year.

**Case 4, a sole owner after the 2026 changes.** Sarah, a US citizen, owns 100% of a Singapore company with a calendar tax year. For 2026 she is Category 4 and 5a: she checks box 4 only and files all six pages plus Schedules E, G-1, H, I-1, J, M, P, Q and R (not H-1, which is only for corporate alternative minimum tax corporations). The company's services income is not subpart F income on these facts, so her inclusion is net CFC tested income, computed in `us-gilti-fdii-beat` (no deduction for QBAI from 2026). Singapore's rate on her company is below 18.9%, so the high-tax exception cannot help. Whether a section 962 election is worth making is decided in `us-gilti-fdii-beat`. Her Singapore bank account also needs an FBAR (`us-fbar-and-fatca-8938`).

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-5471-951B | A US person would be over 50% only with downward attribution from a foreign person, for a foreign corporation year beginning after 31 December 2025 | Refer: section 951B inclusions apply, and the Form 5471 reporting for it is not yet set out in IRS guidance |
| R-5471-WILLFUL | Signs of willful non-filing, or the client is under exam or criminal investigation | Refer to counsel; do not prepare a streamlined certification |
| R-5471-NOTICE | IRS penalty notice already received | Prepare the late form if asked, but refer the penalty response to `us-irs-collections-and-controversy` |
| R-5471-965 | Section 965 balances, Category 1 PTEP or transition tax installments | Refer: specialist PTEP reconstruction |
| R-5471-INSURANCE | Section 953(c) related person insurance income, captives, section 953(d) elections | Refer |
| R-5471-FSC | A foreign sales corporation | Refer: special Category 2 to 5 rules |
| R-5471-CAMT | The filer is an applicable corporation for the corporate alternative minimum tax (Schedule H-1) | Refer |
| R-5471-REORG | Section 338 election, section 304 transaction, reorganization or liquidation of the foreign corporation | Refer: added attachments and Schedule G line 21 |
| R-5471-PFIC | The foreign corporation may also be a PFIC for a shareholder that is not a US shareholder | Refer: Form 8621 rules, no skill yet |
| R-5471-SHORT | First required year after the one-month deferral repeal, with foreign taxes to split under Notice 2025-72 | Prepare the categories and schedules; refer the tax allocation |

## Filing and payment

Form 5471 is not filed on its own: it is attached to the filer's income tax return (or partnership or exempt organization return) and filed by that return's due date, including extensions. For a 2026 calendar year:

| Filer | Return | Due | Extension |
| --- | --- | --- | --- |
| Individual | Form 1040 | 15 April 2027 (26 U.S.C. 6072(a)) | Form 4868: 6 more months, to 15 October 2027. A citizen or resident "out of the country" on the due date gets 2 extra months without asking (to 15 June 2027) and can then request 4 more |
| C corporation, calendar year | Form 1120 | 15 April 2027 (26 U.S.C. 6072(a)) | Form 7004; see `us-form-1120-c-corp` for fiscal years |
| Partnership or S corporation, calendar year | Form 1065 or 1120-S | 15 March 2027 (26 U.S.C. 6072(b)) | Form 7004 |

The foreign corporation's tax year that ends with or within the filer's tax year is the one reported (Schedule O instead reports events during the filer's tax year). There is no separate extension for Form 5471: the return's extension covers it. A corrected Form 5471 goes with an amended return, marked "Corrected", with a statement of the changes. No tax is paid with Form 5471 itself; tax on inclusions is paid with the shareholder's return and through estimated tax (`us-quarterly-estimated-tax`). Sources: [Instructions for Form 5471 (Rev. December 2025)](https://www.irs.gov/pub/irs-pdf/i5471.pdf); [26 U.S.C. 6072](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap61-subchapA-partV-sec6072.htm); [Form 4868 (2025)](https://www.irs.gov/pub/irs-pdf/f4868.pdf).

## Completion checklist

- Ownership chart covers every day of the foreign corporation's year, vote and value separately, with family and entity attribution and the 2026 section 958(b)(4) rule applied.
- Every category tested; item B checked (4 only when 4 and 5a both apply); item C voting percentage at year end.
- Schedules match the chart for every category; zero-amount schedules still included.
- Exceptions claimed only where every condition is met; item H and the attached statements for joint filers; Schedule P attached by each joint filer in 1a, 1b, 4, 5a or 5b.
- Schedule O added for any acquisition, disposition or new US person status in the year.
- First required year after the one-month deferral repeal identified, with the Notice 2025-72 statement if foreign taxes were split.
- Schedule G line 22b answered for dividends under the pro rata share transition rule.
- Exchange rates as units of foreign currency per dollar, four decimals or more.
- Inclusions computed in `us-gilti-fdii-beat` and carried to the return; Schedules J and P roll forward from last year.
- High-tax election (or its absence) documented with the effective rate, consistent across all shareholders' forms.
- Return filed on time with extension; late years routed through Step 7.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Instructions for Form 5471 (Rev. December 2025). Read for What's New (section 70352 repeal, pro rata share transition rule, Schedule G 3b, 21, 22b), Categories of Filers and their exceptions, Additional Filing Exceptions, the filing requirements chart (page 8), item B, penalties, dormant corporations, exchange rates, corrections. | https://www.irs.gov/pub/irs-pdf/i5471.pdf | 2026-11-13 |
| Form 5471 (Rev. December 2025). Read for item B category boxes, items F to H, and the section 898 tax year line. | https://www.irs.gov/pub/irs-pdf/f5471.pdf | 2026-11-13 |
| IRS, About Form 5471. Read for the current revision and the schedule list (Schedule I-1 still titled for GILTI). | https://www.irs.gov/forms-pubs/about-form-5471 | 2026-11-13 |
| Public Law 119-21 (One Big Beautiful Bill Act). Read for sections 70321 to 70323 (net CFC tested income, QBAI repeal, effective dates), 70351 (section 954(c)(6)), 70352 (section 898(c)(2) repeal and transition), 70353 (section 958(b)(4) and new section 951B, effective date), 70354 (section 951(a) pro rata share, transition rule for dividends). | https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm | 2026-11-13 |
| 26 U.S.C. 6038 (govinfo, 2024 edition, not amended by Public Law 119-21). Read for (b) USD 10,000 and USD 50,000, (c) 10 and 5 percent reductions and the USD 10,000 limit, (c)(4)(B) reasonable cause timing, (e)(2) control. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap61-subchapA-partIII-subpartA-sec6038.htm | 2026-11-13 |
| 26 U.S.C. 6679 (govinfo). Read for the section 6046 penalty, USD 10,000 and USD 50,000. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapB-partI-sec6679.htm | 2026-11-13 |
| 26 U.S.C. 6046 (govinfo). Read for the acquisition and disposition returns behind Categories 2 and 3. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap61-subchapA-partIII-subpartA-sec6046.htm | 2026-11-13 |
| 26 U.S.C. 6501 (govinfo). Read for (c)(8), 3 years after the information is furnished, and the reasonable cause limit. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap66-subchapA-sec6501.htm | 2026-11-13 |
| 26 U.S.C. 951 (govinfo, 2024 edition). Read for (b) US shareholder, 10 percent of vote or value, and the 2017 value-prong note; (a) as replaced by Public Law 119-21 is read from the Public Law. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partIII-subpartF-sec951.htm | 2026-11-13 |
| 26 U.S.C. 957 (govinfo). Read for (a) more than 50 percent on any day. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partIII-subpartF-sec957.htm | 2026-11-13 |
| 26 U.S.C. 958 (govinfo, 2024 edition). Read for (a)(2) proportionate ownership through foreign entities, (b)(1) to (3), and the note on the 2017 repeal of (b)(4) that Public Law 119-21 reverses. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partIII-subpartF-sec958.htm | 2026-11-13 |
| 26 U.S.C. 318 (govinfo). Read for (a)(1) family attribution (spouse, children, grandchildren, parents). | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapC-partI-subpartC-sec318.htm | 2026-11-13 |
| 26 U.S.C. 954 (govinfo). Read for (b)(4), greater than 90 percent of the maximum section 11 rate. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partIII-subpartF-sec954.htm | 2026-11-13 |
| 26 U.S.C. 11 (govinfo). Read for (b), 21 percent. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partII-sec11.htm | 2026-11-13 |
| 26 U.S.C. 6072 (govinfo). Read for (a) 15 April and (b) 15 March due dates. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap61-subchapA-partV-sec6072.htm | 2026-11-13 |
| Form 4868 (2025). Read for the 6-month extension and the 2 extra months for taxpayers out of the country. | https://www.irs.gov/pub/irs-pdf/f4868.pdf | 2026-11-13 |
| Schedule 1 (Form 1040) 2025. Read for lines 8n and 8o. | https://www.irs.gov/pub/irs-pdf/f1040s1.pdf | 2026-11-13 |
| IRS, U.S. taxpayers residing outside the United States (streamlined foreign offshore procedures). Read for 330 full days, the non-willful definition and the penalty relief. | https://www.irs.gov/individuals/international-taxpayers/u-s-taxpayers-residing-outside-the-united-states | 2026-11-13 |
| IRS, U.S. taxpayers residing in the United States (streamlined domestic offshore procedures). Read for the 3-year and 6-year periods and the 5 percent miscellaneous offshore penalty. | https://www.irs.gov/individuals/international-taxpayers/us-taxpayers-residing-in-the-united-states | 2026-11-13 |
| IRS, Delinquent international information return submission procedures. Read for amended-return filing and reasonable cause statements. | https://www.irs.gov/individuals/international-taxpayers/delinquent-international-information-return-submission-procedures | 2026-11-13 |

Not yet confirmed: the 2026 revisions of Form 5471, its schedules and instructions were not published when read; the December 2025 revisions are used, and the Category 5 definition (stock owned on the last day the corporation was a CFC) may change to follow the new any-day pro rata share rule. How a foreign controlled United States shareholder under section 951B reports on Form 5471 is not in the December 2025 instructions. The 2026 Schedule 1 (Form 1040) and Form 4868 were not yet published; line numbers and extension rules are from the 2025 editions. Notices 2018-13, 2025-72 and 2025-75, Rev. Procs. 92-70 and 2019-40, and the high-tax exception regulations (Treas. Reg. 1.951A-2(c)(7) and 1.954-1(d)) are described as the instructions summarize them and were not opened separately. The litigation over whether section 6038(b) penalties can be assessed without a deficiency procedure (Farhy, Tax Court 2023, reversed by the D.C. Circuit in 2024) was not re-read; treat the penalty as assessable.
