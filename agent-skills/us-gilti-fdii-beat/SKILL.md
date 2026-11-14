---
name: us-gilti-fdii-beat
description: "Work out the 2026 US federal tax on a US person's controlled foreign corporations and a large US corporation's foreign-facing income, under the rules Public Law 119-21 (the One Big Beautiful Bill Act) set for taxable years beginning after 31 December 2025. Covers the United States shareholder and CFC tests, the subpart F income categories with the de minimis, full-inclusion and earnings limits, net CFC tested income (formerly GILTI, now with no QBAI return), the high-tax exception and exclusion at greater than 18.9 percent, the section 250 deduction of 40 percent on net CFC tested income and 33.34 percent on foreign-derived deduction eligible income (formerly FDII), the 90 percent section 960(d) deemed-paid credit and the section 78 gross-up, the section 904(b)(5) expense rule, the section 962 election for individuals with the section 962(d) second layer, and the base erosion minimum tax at 10.5 percent. Trigger on \"GILTI\", \"NCTI\", \"net CFC tested income\", \"subpart F\", \"section 962 ele"
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/us-gilti-fdii-beat"
  jurisdiction: "US"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# US controlled foreign corporations, FDDEI and BEAT: subpart F, net CFC tested income, section 962, tax year 2026

> **Source-cited draft.** Built from Public Law 119-21 (sections 70311, 70312, 70321 to 70323, 70331 and 70351 to 70354), 26 U.S.C. 11, 59A, 250, 951, 951A, 952, 954, 957, 958 and 962 (2024 edition, read with the 2025 amendments), Treas. Reg. 1.951A-2 and 1.962-2, and the Instructions for Forms 5471, 8992, 8993 and 8991, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** For taxable years beginning after 31 December 2025, a United States shareholder of a controlled foreign corporation (CFC) includes two amounts each year: its share of the CFC's **subpart F income**, and its share of **net CFC tested income** (the inclusion called GILTI before 2026). The old 10% return on tangible assets (QBAI) is gone, so the whole net tested income is included. A US C corporation deducts **40%** of it (plus the section 78 gross-up) and is deemed to pay **90%** of the related foreign tax, so the US rate before credits is 12.6% and foreign tax of about 14% or more covers it, before expense allocation. An individual gets neither unless they make the **section 962 election**. A US C corporation's foreign-derived deduction eligible income (FDDEI, formerly FDII) gets a **33.34%** deduction. A corporation with average gross receipts of at least **USD 500,000,000** and a base erosion percentage of 3% or more pays the **base erosion minimum tax at 10.5%** of modified taxable income, to the extent it exceeds regular tax.

## Scope and who this is for

In scope: a US person (citizen, green card holder, resident alien, domestic corporation, partnership, estate or trust) that owns stock in a foreign corporation, for tax years beginning in 2026; and a domestic C corporation computing its section 250 deduction or the base erosion minimum tax. This skill holds the arithmetic for subpart F income, net CFC tested income, the section 250 deduction, the section 960 deemed-paid credit, the section 962 election and BEAT. `us-form-5471-cfc-information` decides who files Form 5471, in which category, and which schedules, and points here for these computations.

A foreign entity is in scope only if it is a **corporation** for US tax purposes. If it is a partnership or a disregarded entity (for example after a Form 8832 election), the CFC rules do not apply to it and this skill stops.

Out of scope, and where it goes:

| Topic | Skill |
| --- | --- |
| Who files Form 5471, the categories, the schedules, the penalties, fixing missed years | `us-form-5471-cfc-information` |
| The corporate return that carries the inclusions (Form 1120, Schedule C dividends, Schedule J) | `us-form-1120-c-corp` |
| The individual return that carries them (Schedule 1, Form 1040) | `us-form-1040-individual-return` |
| Individual foreign tax credits on Form 1116 | `us-foreign-tax-credit-1116` |
| Foreign partnerships (Form 8865) and foreign-owned US corporations (Form 5472) | `us-form-8865-foreign-partnership`, `us-form-5472-foreign-owned-us` |
| Foreign trusts that hold CFC stock (Forms 3520 and 3520-A) | `us-foreign-trust-reporting` |
| Foreign bank and asset reporting (FBAR, Form 8938) | `us-fbar-and-fatca-8938` |
| Passive foreign investment companies (PFICs), section 965 transition tax, section 956 computations, transfer pricing, Pillar Two computations abroad, state conformity | Refer (see When to refuse or refer) |

## Ask the client first

1. **Every foreign entity** owned by the client, their family, their trusts, partnerships and companies, and each entity's US tax classification (corporation, partnership, disregarded).
2. **Ownership by vote and by value** for each foreign corporation, split into stock owned directly, indirectly through foreign entities (section 958(a)), and constructively through family, partnerships, estates, trusts or corporations (section 958(b)).
3. **Who else owns 10% or more** by vote or value, and whether they are US persons. Is there a foreign parent above the client's companies?
4. **Dates:** each corporation's tax year, and every purchase, sale, redemption or new issue of stock during the year (the 2026 any-day pro rata rule depends on them).
5. **The CFC's income by type** (dividends, interest, rents, royalties, related-party sales and services, active trading), its deductions, its **foreign income taxes** paid or accrued, and its earnings and profits, in US dollars.
6. **Distributions** paid to the client this year, and the previously taxed earnings (PTEP) accounts from earlier inclusions.
7. **Who the client is:** an individual (then model the section 962 election), a C corporation (then also ask for export sales and services for FDDEI), or a pass-through.
8. **For a corporation:** average annual gross receipts for the three prior years (with its controlled group), and deductible payments to foreign related parties (for BEAT).
9. **Prior Forms 5471, 8992, 8993 and 8991**, and any high-tax or section 962 elections made in earlier years.

## The method, step by step

### Rates, bands and thresholds

| Item | Amount, 2026 | Source |
| --- | --- | --- |
| United States shareholder: owns this share of vote or value, or more | 10% | [26 U.S.C. 951(b)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partIII-subpartF-sec951.htm) |
| CFC: United States shareholders own more than this share of vote or value | 50% | [26 U.S.C. 957(a)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partIII-subpartF-sec957.htm) |
| Corporate tax rate (also the section 962 rate) | 21% | [26 U.S.C. 11(b)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partII-sec11.htm) |
| High-tax exception and exclusion: foreign effective rate must be greater than 90% of the section 11 rate | 18.9% (derived: 90% of 21%) | [26 U.S.C. 954(b)(4)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partIII-subpartF-sec954.htm) |
| Subpart F de minimis: base company and insurance income less than the lesser of this share of gross income | 5% | [26 U.S.C. 954(b)(3)(A)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partIII-subpartF-sec954.htm) |
| Subpart F de minimis: or this amount | USD 1,000,000 | [26 U.S.C. 954(b)(3)(A)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partIII-subpartF-sec954.htm) |
| Subpart F full inclusion: base company and insurance income more than this share of gross income | 70% | [26 U.S.C. 954(b)(3)(B)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partIII-subpartF-sec954.htm) |
| QBAI return (net deemed tangible income return) subtracted from net tested income | None (repealed) | [Public Law 119-21, section 70323(a)(2)](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| Section 250 deduction on net CFC tested income plus its section 78 gross-up | 40% | [Public Law 119-21, section 70321(a)(2)](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| Section 250 deduction on foreign-derived deduction eligible income | 33.34% | [Public Law 119-21, section 70321(a)(1)](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| Section 960(d) deemed-paid share of tested foreign income taxes | 90% | [Public Law 119-21, section 70312(a)(1)](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| Credit denied on foreign taxes on distributed previously taxed net CFC tested income (amounts after 28 June 2025) | 10% | [Public Law 119-21, section 70312(b)](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| BEAT rate on modified taxable income | 10.5% | [Public Law 119-21, section 70331(a)(1)](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| BEAT rate increase for an affiliated group with a bank or registered securities dealer | 1 percentage point | [26 U.S.C. 59A(b)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partVII-sec59A.htm) |
| BEAT gross receipts test: 3-year average at least | USD 500,000,000 | [26 U.S.C. 59A(e)(1)(B)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partVII-sec59A.htm) |
| BEAT base erosion percentage, at least | 3% (2% for banks and securities dealers) | [26 U.S.C. 59A(e)(1)(C)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partVII-sec59A.htm) |
| BEAT protected share of applicable section 38 credits | 80% | [26 U.S.C. 59A(b)(1)(B)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partVII-sec59A.htm) |

None of these is indexed for inflation. The Form 5471 penalty amounts are owned by `us-form-5471-cfc-information` and are not restated here.

**Which rules apply when.** Most changes start with **taxable years beginning after 31 December 2025** of the US taxpayer: the 40% and 33.34% section 250 rates, the 90% credit, the QBAI repeal, the section 904(b)(5) expense rule and the 10.5% BEAT rate. The ownership changes start with **taxable years of foreign corporations beginning after 31 December 2025**: the any-day pro rata rule, the restored section 958(b)(4), the new section 951B and the permanent section 954(c)(6) look-through. For a calendar-year shareholder and a calendar-year CFC both sets start in 2026. Source: [Public Law 119-21](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm).

### Step 1: United States shareholder and CFC status

1. A US person is a **United States shareholder** if it owns, or is treated as owning, **10% or more** of the total combined voting power of all classes of voting stock, **or** 10% or more of the total value of all classes of stock. Exactly 10% qualifies. Source: [26 U.S.C. 951(b)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partIII-subpartF-sec951.htm).
2. The foreign corporation is a **CFC** if United States shareholders together own **more than 50%** of the vote or of the value on **any day** of its tax year. Exactly 50% is not enough. Owners below 10% are not United States shareholders, so their stock does not count toward the total. Source: [26 U.S.C. 957(a)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partIII-subpartF-sec957.htm).
3. Build **two ownership maps** and keep them separate. Section 958(a) ownership (direct, plus proportionate ownership through foreign entities) decides **who includes** and **how much**. Section 958(b) constructive ownership (section 318 attribution, modified) decides **status** only. A constructive-only owner counts for status but includes nothing. Source: [26 U.S.C. 958](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partIII-subpartF-sec958.htm).
4. **Downward attribution from foreign persons is switched off again from 2026.** For taxable years of foreign corporations beginning after 31 December 2025, section 958(b)(4) provides that section 318(a)(3)(A) to (C) "shall not be applied so as to consider a United States person as owning stock which is owned by a person who is not a United States person". A US subsidiary of a foreign parent is no longer treated as owning its foreign sister companies, so those sisters are no longer CFCs on that ground (the "sister CFC" problem of 2018 to 2025, for which Notice 2018-13 and Rev. Proc. 2019-40 gave partial relief). Source: [Public Law 119-21, section 70353(a)](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm).
5. **New section 951B** replaces it for one case: a **foreign controlled United States shareholder** (a US person that would own more than 50% if downward attribution still applied) of a **foreign controlled foreign corporation** still includes subpart F income and net CFC tested income, under a separate parallel application of subpart F. If a foreign parent sits above both US and foreign subsidiaries, refer (R-INTL-951B). Source: [Public Law 119-21, section 70353(b)](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm).
6. If the client is not a United States shareholder of a CFC, neither subpart F nor net CFC tested income applies. Form 5471 may still be required (officers, directors, 10% acquisitions): see `us-form-5471-cfc-information`. A US C corporation owning 10% of a foreign corporation may also have the section 245A dividends received deduction, which is outside this skill.

### Step 2: who includes, and the pro rata share (2026 any-day rule)

7. For taxable years of foreign corporations beginning after 31 December 2025, **each United States shareholder that owns section 958(a) stock on any day of the CFC year** includes its pro rata share of subpart F income. The share is the income attributable to its stock **and** to the part of the year in which, at once, it owned the stock, it was a United States shareholder, and the company was a CFC. Source: [Public Law 119-21, section 70354(a)](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm).
8. The inclusion goes in the shareholder's taxable year that includes **the last day it owned** section 958(a) stock in that CFC year. A seller in mid-year now includes its share for the days it held the stock; under the 2025 rule only the last-day owner included anything, reduced under the old section 951(a)(2)(B) for dividends paid to other owners (with a transition rule for dividends paid after 28 June 2025).
9. Net CFC tested income uses the same pro rata and timing rules: section 951A(c) now looks to stock owned "on any day" in the year, and to the taxable year determined under section 951(a)(3). Source: [Public Law 119-21, section 70354(b)](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm).
10. **Section 956** (investment in US property) still uses the owner on the **last day** of the CFC year on which the company is a CFC. Refer the computation (R-INTL-956).
11. **One-month deferral repealed.** The section 898(c)(2) election that let a specified foreign corporation use a year ending one month before its majority shareholder's year is repealed for years beginning after 30 November 2025; a CFC that used it has a short first year ending with the required year. Source: [Public Law 119-21, section 70352](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm).

### Step 3: subpart F income, by category

12. Classify the CFC's gross income. Subpart F income is mainly **insurance income** (section 953) and **foreign base company income** (section 954), in these categories. Subpart F applies first: income in these categories is excluded from tested income in Step 4. Source: [26 U.S.C. 952](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partIII-subpartF-sec952.htm); [26 U.S.C. 954](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partIII-subpartF-sec954.htm).

| Category | What it catches | Main carve-outs |
| --- | --- | --- |
| Foreign personal holding company income, section 954(c) | Dividends, interest, rents, royalties, annuities; net gains on property producing passive income or no income; certain commodity and foreign currency gains; notional principal contract income | Active rents and royalties from unrelated persons; same-country dividends and interest and certain rents and royalties from related persons (954(c)(3)); related-CFC look-through (954(c)(6)); active financing exception (954(h), permanent since 2015) |
| Foreign base company sales income, section 954(d) | Profit on buying from or selling to a related person, where the goods are made outside, and sold for use outside, the CFC's country | Goods made or substantially transformed by the CFC itself; the branch rule in 954(d)(2) can create this income from a manufacturing branch (Whirlpool Financial Corp. v. Commissioner, 19 F.4th 944, 6th Cir. 2021) |
| Foreign base company services income, section 954(e) | Services performed for or on behalf of a related person outside the CFC's country | Services performed in the CFC's own country |
| Insurance income, section 953 | Premiums and investment income from insuring risks outside the CFC's country | Active insurance under 954(i) |

13. **De minimis rule:** if foreign base company income plus gross insurance income is **less than** the lesser of **5%** of gross income or **USD 1,000,000**, none of the gross income is treated as either. Source: [26 U.S.C. 954(b)(3)(A)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partIII-subpartF-sec954.htm).
14. **Full inclusion rule:** if that total is **more than 70%** of gross income, all gross income is treated as foreign base company or insurance income, still subject to the high-tax exception and deductions. Source: [26 U.S.C. 954(b)(3)(B)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partIII-subpartF-sec954.htm).
15. **Related-CFC look-through is permanent.** Dividends, interest, rents and royalties from a related CFC are not foreign personal holding company income to the extent they come out of the payer's income that is neither subpart F income nor effectively connected income. Public Law 119-21 struck the end date for taxable years of foreign corporations beginning after 31 December 2025. Source: [Public Law 119-21, section 70351](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm).
16. **Earnings limit:** subpart F income cannot exceed the CFC's current-year earnings and profits (section 952(c)(1)(A)); a recapture account carries the excess to later years. Source: [26 U.S.C. 952(c)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partIII-subpartF-sec952.htm).
17. **High-tax exception (Step 5)** removes qualifying items from foreign base company and insurance income.
18. Reduce the gross subpart F items by the deductions (including foreign taxes) properly allocable to them. The result, times the pro rata share, is the section 951(a)(1)(A) inclusion. Subpart F income goes in the general or passive foreign tax credit category, not the section 951A category.

### Step 4: net CFC tested income

19. For each CFC, **tested income** is gross income **excluding** (a) effectively connected income, (b) gross income taken into account in determining subpart F income, (c) gross income excluded from foreign base company or insurance income by the high-tax exception, (d) dividends received from related persons (section 954(d)(3)), and (e) foreign oil and gas extraction income; **less** the deductions, **including taxes**, properly allocable to that gross income. If deductions exceed the gross income, the CFC has a **tested loss**. Source: [26 U.S.C. 951A](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partIII-subpartF-sec951A.htm) (the 2024 text; the paragraph is now section 951A(b)(2) after the 2025 redesignation).
20. **Net CFC tested income** = the shareholder's pro rata shares of every CFC's tested income, minus its pro rata shares of every CFC's tested loss. Source: [Public Law 119-21, section 70323(a)](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm).
21. **No QBAI return from 2026.** Before 2026 the shareholder subtracted a net deemed tangible income return (10% of qualified business asset investment measured on ADS basis, less specified interest expense). Section 70323(a)(2) struck that subsection, so the whole net CFC tested income is included and QBAI is no longer needed for 2026 inclusions.
22. The section 951A inclusion is treated as a section 951(a)(1)(A) amount for several purposes, including sections 959 (previously taxed earnings), 961 (basis) and 962.

### Step 5: the high-tax exception and the high-tax exclusion

23. **Rate test:** the item must have borne a foreign effective rate **greater than 90%** of the section 11 rate, that is, **greater than 18.9%**. Exactly 18.9% fails. Source: [26 U.S.C. 954(b)(4)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partIII-subpartF-sec954.htm).
24. **Subpart F:** the section 954(b)(4) exception removes the qualifying items from foreign base company income and insurance income.
25. **Tested income (the high-tax exclusion):** it applies only if an election is in effect for the CFC for the year. The rate is tested for each **tested unit**, not the CFC as a whole. The CFC's controlling domestic shareholders make it with a timely filed original return, or with an amended return filed **within 24 months of the unextended due date** of the original return; on an amended return every United States shareholder owning section 958(a) stock at year end must also file within a single period of no more than six months inside that window. An election or revocation is valid only if every requirement, including notice to the other United States shareholders, is met. For a CFC group it binds every member. Source: [Treas. Reg. 1.951A-2(c)(7)](https://www.ecfr.gov/current/title-26/chapter-I/subchapter-A/part-1/section-1.951A-2).
26. **Credit trade-off:** excluded income leaves tested income, so its foreign taxes give no section 960(d) credit. Model both outcomes (see Case 1).
27. **Open point for 2026:** the regulation still cites pre-2026 numbering (for example section 951A(c)(2)(A)(i)(III), now 951A(b)(2)(A)(i)(III)). Until Treasury updates it, confirm the election mechanics before relying on them for 2026.

### Step 6: the corporate shareholder: section 78, section 250 and section 960

28. **Inclusion percentage** = net CFC tested income divided by the total of the shareholder's pro rata shares of tested income (tested losses lower it). **Tested foreign income taxes** are the taxes properly attributable to tested income of CFCs with tested income; a tested-loss CFC's taxes do not count.
29. **Deemed-paid credit:** a domestic corporation is deemed to pay **90%** of the inclusion percentage times its tested foreign income taxes. Source: [Public Law 119-21, section 70312(a)(1)](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm).
30. **Gross-up:** the deemed-paid amount, figured without the "90 percent of" haircut, is treated as a dividend under section 78 and added to income. Source: [Public Law 119-21, section 70312(a)(2)](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm).
31. **Section 250 deduction:** 40% of net CFC tested income plus the section 78 amount attributable to it. Source: [Public Law 119-21, section 70321](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm).
32. **Taxable income limit:** if net CFC tested income plus FDDEI exceeds taxable income (figured without section 250), the excess reduces each in proportion before the percentages apply. A loss-year corporation gets no section 250 deduction. The old section 250(a)(3) step-down for years after 2025 is struck. Source: [26 U.S.C. 250(a)(2)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVIII-sec250.htm).
33. **Foreign tax credit limitation, section 951A category:** for 2026, only the section 250(a)(1)(B) deduction (and any section 164(a)(3) deduction for taxes on that income) and deductions **directly allocable** to the income are allocated to it. **No interest expense and no research and experimental expenditure** is allocated to it; what would have been is allocated to US-source income. Excess credits in this category cannot be carried back or forward. Source: [Public Law 119-21, section 70311](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm). This removes most of the pre-2026 "expense allocation trap" in which US interest shrank the GILTI limitation; directly allocable expenses can still bite.
34. **Rough break-even foreign rate:** US tax before credits is 21% x (1 - 40%) = 12.6% of the grossed-up inclusion; the credit is 90% of the foreign rate; 12.6% / 90% = **14%**. Below about 14%, residual US tax remains even with no allocated expenses. (For 2025 the same arithmetic gave 10.5% / 80% = 13.125%.)
35. **Subpart F items:** section 960(a) deems a domestic corporation to pay the foreign taxes properly attributable to the subpart F item, with no haircut; the section 78 gross-up applies.
36. **Distributions of previously taxed net CFC tested income:** no credit is allowed for **10%** of the foreign taxes (including withholding) on a distribution excluded under section 959(a) because of an earlier section 951A inclusion. This applies to such amounts after 28 June 2025. Source: [Public Law 119-21, section 70312(b)](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm).
37. Report on Form 8992 (net CFC tested income, fed by Form 5471 Schedule I-1), Form 8993 (section 250), Form 1118 (credit) and Form 1120 (the section 78 amount on Schedule C, the section 250 deduction on line 29b per the current form). In a consolidated group, net CFC tested income is figured at the group level and allocated to members (Treas. Reg. 1.1502-51).

### Step 7: the individual shareholder, and the section 962 election

38. **Without the election** an individual includes subpart F income and net CFC tested income as ordinary income at the section 1 rates (up to 37%), gets **no section 250 deduction** (it is for domestic corporations) and **no deemed-paid credit** for the CFC's foreign taxes. A later distribution of the included earnings is excluded under section 959.
39. **With the election** (section 962), the tax on the section 951(a) amounts equals the section 11 tax a domestic corporation would pay: **21%**, with the section 960 credit as if the individual were a domestic corporation (for 2026, 90% for tested income), and, under the regulations, the section 250 deduction on net CFC tested income and its gross-up, claimed on Form 8993. The credit is claimed on Form 1118, not Form 1116. Source: [26 U.S.C. 962](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partIII-subpartF-sec962.htm).
40. **The second layer, section 962(d):** when the CFC later distributes earnings that were included under the election, the distribution is included in gross income "to the extent that such earnings and profits so distributed exceed the amount of tax paid" under the election. The usual section 959 exclusion does not shelter it. Whether that dividend is a **qualified dividend** depends on the CFC: a company resident in a country with a comprehensive US income tax treaty (or with stock readily tradable on a US market) can pay qualified dividends; one in a non-treaty country (for example Singapore or Hong Kong) generally pays ordinary dividends (the Tax Court reached that result for a Hong Kong company in Smith v. Commissioner, 2018). Source: [26 U.S.C. 962(d)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partIII-subpartF-sec962.htm).
41. **Who and how:** only an individual (including a trust or estate) who is a United States shareholder may elect. The election covers **all** CFCs for which the shareholder has a section 951(a) inclusion that year; it cannot be made for some only. It is made by filing a statement "with his return for the taxable year", listing each CFC and each entity in the ownership chain, the inclusions company by company, the shareholder's share of each CFC's earnings and profits and foreign taxes, and distributions by type. Revocation needs IRS consent (a material and substantial change in circumstances). Source: [Treas. Reg. 1.962-2](https://www.ecfr.gov/current/title-26/chapter-I/subchapter-A/part-1/section-1.962-2). The old version of this skill said the election cannot be made on an amended return; the regulation does not say so, and the Form 5471 instructions contemplate a later election. Keep a separate PTEP account for section 962 earnings (Form 5471 Schedules J and P).
42. **Net investment income tax:** under the default rules of Treas. Reg. 1.1411-10 a CFC inclusion is not net investment income when included, but the later distribution of the earnings is. CCA 202118008 discusses section 962 electors. Treat the NIIT effect as a reviewer point (R-INTL-NIIT).
43. **When the election helps:** the CFC pays meaningful foreign tax (the 90% credit offsets most of the 12.6%), the CFC is in a treaty country (the later dividend can be qualified, at 20%), and distributions are not imminent. **When it hurts or barely helps:** the CFC pays little foreign tax, is in a non-treaty country (the later dividend is ordinary and the election mostly defers), or distributions come soon. Always model the inclusion year and the expected distribution years together (Case 2).

### Step 8: FDDEI, the export deduction for a US C corporation

44. Only a **domestic C corporation** qualifies (not S corporations, partnerships, individuals, RICs or REITs). A section 962 elector gets the section 250 deduction for net CFC tested income only, not for FDDEI. A corporation with CFCs can claim both.
45. **Deduction eligible income (DEI)** is gross income excluding subpart F inclusions, net CFC tested income, financial services income, dividends from CFCs, domestic oil and gas extraction income, foreign branch income, and (for sales or other dispositions after 16 June 2025) income and gain from disposing of intangible property (as defined in section 367(d)(4)) and of other depreciable, amortizable or depletable property; **less** the deductions, including taxes, properly allocable to it **other than interest expense and research or experimental expenditures** (for years beginning after 31 December 2025). Source: [Public Law 119-21, section 70322](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm).
46. **No routine-return step from 2026.** The old formula reduced DEI by 10% of domestic QBAI to get "deemed intangible income" and then took the foreign-derived share. Section 70323(b) struck those paragraphs. FDDEI is the part of DEI derived from sales of property to foreign persons for foreign use and from services to persons, or for property, located outside the US. Source: [Public Law 119-21, section 70323(b)](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm).
47. **Deduction:** 33.34% of FDDEI, subject to the section 250(a)(2) taxable income limit (Step 6). Effective rate on FDDEI: 21% x (1 - 33.34%) = about 14.0%.
48. **Foreign use and documentation:** the regulations (Treas. Reg. 1.250(b)-3 to 1.250(b)-6) require evidence, kept at the time, that the buyer is a foreign person and that the use is foreign. Common positions:

| Transaction | Foreign use? | What to keep |
| --- | --- | --- |
| Goods sold to a foreign distributor for resale abroad | Yes | Evidence the buyer is foreign and the goods leave the US |
| Goods sold to a foreign affiliate that sells them back into the US | No | Trace the end use |
| Cloud or digital services used by customers abroad | Yes, for users located abroad | Location records, contracts, billing addresses |
| Licence of intangibles used in several countries | In proportion | Allocation by territory of use |
| Services to a business | Where the business operates | The recipient's operating locations |

   Sales to a foreign related party qualify only if the related party resells to unrelated foreign persons for foreign use. Small businesses have lighter documentation rules. Those regulations were written for FDII; check each one still fits the 2026 statute (see Not yet confirmed).
49. **Research expenditures:** for 2026, research and experimental expenditures are not apportioned to DEI at all (step 45), so domestic research expensing no longer depresses FDDEI the way it did before. The research expensing rules themselves are outside this skill.

### Step 9: BEAT, the base erosion minimum tax

50. **Who:** a corporation (not a RIC, REIT or S corporation) whose average annual gross receipts for the 3 prior years are at least **USD 500,000,000** (aggregated across the controlled group) and whose **base erosion percentage** is **3%** or more (2% for an affiliated group with a bank or registered securities dealer). Below USD 500,000,000 BEAT does not apply; most small and mid-sized engagements stop here. Source: [26 U.S.C. 59A(e)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partVII-sec59A.htm).
51. **Base erosion payments:** amounts paid or accrued to a foreign related person (generally 25% common ownership) that are deductible (interest, royalties, service fees, rent), that buy depreciable or amortizable property, that are reinsurance premiums, or that go to certain expatriated entities. Not included: cost of goods sold (it is not a deduction), services eligible for the services cost method charged at cost (only the markup counts), qualified derivative payments, and amounts on which US gross-basis tax was withheld, to the extent withheld.
52. **Base erosion percentage** = base erosion tax benefits (the deductions, depreciation and amortization from base erosion payments) divided by total deductions (with statutory exclusions). Source: [26 U.S.C. 59A(c)(4)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partVII-sec59A.htm).
53. **Modified taxable income** = taxable income + base erosion tax benefits + the base erosion percentage of any net operating loss deduction (pre-2018 NOLs are not affected).
54. **BEAT** = 10.5% of modified taxable income (11.5% for bank and securities dealer groups), minus regular tax liability **reduced by** the credits other than the research credit and the protected part (80%) of the applicable section 38 credits (low-income housing, renewable electricity production, and certain energy credits). Credits outside those two groups (for example the foreign tax credit) are subtracted from the regular tax, which raises BEAT. Public Law 119-21 struck the post-2025 rule that would have subtracted all credits and used 12.5%. Source: [Public Law 119-21, section 70331](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm); [26 U.S.C. 59A(b)(1)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partVII-sec59A.htm).
55. **Report on Form 8991** (Schedule A base erosion payments, then the modified taxable income and tax), filed with Form 1120 by every corporation that meets the gross receipts test, even if its base erosion percentage is below the threshold.

### Step 10: order of operations for a return with all of this

56. CFC status for each foreign corporation (Step 1); United States shareholders; both ownership maps.
57. Subpart F income per CFC (Step 3), then tested income or loss per CFC (Step 4); high-tax elections run both ways (Step 5).
58. Aggregate to net CFC tested income (Form 8992); pro rata shares under the any-day rule (Step 2).
59. Corporations: deemed-paid taxes, gross-up, section 250 together with FDDEI and the taxable income limit, then the section 951A category limitation (Forms 8993 and 1118). Individuals: with and without section 962.
60. Corporations over USD 500,000,000: BEAT last, because it compares against regular tax after credits (Form 8991).
61. Form 5471 filings and schedules: `us-form-5471-cfc-information`.

### Pillar Two, briefly

The United States has not adopted the OECD Pillar Two rules (a 15% minimum for groups with revenue of EUR 750 million or more), and Public Law 119-21 did not adopt them. Other countries' domestic top-up taxes, income inclusion rules and undertaxed profits rules can still charge a US-parented group abroad; those taxes are not computed here and their US creditability is unsettled (R-INTL-3).

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Owns exactly 10% of value and none of the vote | United States shareholder (vote or value, "10 percent or more") |
| United States shareholders own exactly 50% | Not a CFC: more than 50% is needed |
| Crosses more than 50% for one day | CFC for that year; the pro rata share is limited to the qualifying period |
| Owns only by section 958(b) attribution | Counts for status; includes nothing |
| 2026: CFC only through downward attribution from a foreign parent | Not a CFC under section 957; test section 951B |
| Seller of CFC stock in mid-2026 | Includes its share for the days it owned the stock (any-day rule); in 2025 only the last-day owner included |
| Foreign effective rate exactly 18.9% | High-tax exception and exclusion not available: the rate must be greater |
| Foreign effective rate 30%, high-tax exclusion elected | No tested income from that tested unit and no credit for its taxes; usually better than a large credit that is lost (Case 1) |
| Tested-loss CFC | Its loss offsets other CFCs' tested income; its foreign taxes are not tested foreign income taxes |
| Individual with no section 962 election | No section 250 deduction, no deemed-paid credit |
| Section 962 wanted for one CFC only | Not possible: it covers all CFCs with inclusions that year |
| Excess credit in the section 951A category | Lost: no carryback or carryover |
| US C corporation in a loss year | No section 250 deduction for net CFC tested income or FDDEI |
| Gain on selling intangible property after 16 June 2025 | Not DEI, so no FDDEI deduction on it |
| Group gross receipts USD 499,000,000 | Outside BEAT; Form 8991 not required |
| Fiscal-year CFC whose year straddles 1 January 2026 | Shareholder-year rules and foreign-corporation-year rules can start in different years: refer (R-INTL-FY) |

### Defaults when a fact is missing

| Missing fact | Default, and flag it |
| --- | --- |
| Whether a foreign affiliate is a CFC | Assume CFC and ask for ownership by vote and value; a missed Form 5471 carries automatic penalties |
| Whether the high-tax exclusion would be better | Run both; do not elect without showing the client |
| Whether the section 962 election would help | Run with and without, including the distribution years |
| Character of a related-party payment for BEAT | Treat as a base erosion payment until documented otherwise |
| Foreign-use documentation for FDDEI | Exclude the income from FDDEI until documented |
| The CFC's foreign taxes in dollars | No credit until translated at the right rate with the foreign tax return |
| The CFC's earnings and profits | Stop: subpart F is capped by them (R-INTL-EP) |

### Red flags to raise with the client

| Flag | Why it matters |
| --- | --- |
| A US individual owns a company in a zero or low-tax jurisdiction | Net CFC tested income at up to 37% with no credit, or section 962 with little credit |
| Foreign rate between about 14% and 18.9% | No high-tax exclusion, and close to the 14% break-even: check the expense allocation |
| Foreign rate below about 14% | Residual US tax under the 12.6% / 90% arithmetic |
| Large distributions planned from section 962 earnings | Section 962(d) second layer, possibly ordinary dividends |
| Foreign withholding tax on distributions of previously taxed tested income | 10% of it is not creditable (after 28 June 2025) |
| Interest or royalties paid by a large US group to foreign affiliates | BEAT exposure |
| FDDEI claimed from customer addresses alone | Disallowed without foreign-use documentation |
| A foreign trust or partnership in the chain | Other regimes run alongside: `us-foreign-trust-reporting`, `us-form-8865-foreign-partnership` |

### Common errors at review

| Error | Fix |
| --- | --- |
| Tested income figured before the CFC's foreign tax | Tested income is after allocable deductions, including taxes; the tax comes back in through the section 78 gross-up (the old version of this skill's German example made this error) |
| A QBAI return subtracted for 2026 | Repealed: include the whole net CFC tested income |
| 50% section 250 or 80% credit used for 2026 | 40% and 90% for taxable years beginning after 31 December 2025 |
| Section 250 or the deemed-paid credit given to an individual with no section 962 statement | Check the statement is attached |
| Excess section 951A category credit carried forward | Not allowed: it is lost |
| US interest expense allocated to the section 951A category in 2026 | Not allowed under section 904(b)(5) |
| Cost of goods sold treated as a base erosion payment | It is not a deduction; exclude it from the numerator and the denominator |
| All credits subtracted from regular tax in the 2026 BEAT computation | Only credits other than the research credit and 80% of applicable section 38 credits |
| Section 250 taxable income limit skipped | Compute taxable income before section 250 first |
| Subpart F and net CFC tested income mixed up | Different credit categories and credit percentages |

## Worked cases

All amounts are invented and in US dollars. Each case assumes calendar years, one CFC owned 100% all year, no subpart F income, no allocated expenses in the section 951A category and no binding taxable income limit.

**Case 1, a decision: a US C corporation with a high-tax German CFC, high-tax exclusion or not.** The CFC earns USD 1,320,000 before German tax and pays USD 396,000 (30%). Tested income is after taxes: USD 924,000.

Without the exclusion: gross-up USD 396,000, income USD 1,320,000; section 250 deduction 40% = USD 528,000; taxable USD 792,000; tax at 21% = USD 166,320. The credit is 90% x 396,000 = USD 356,400, but the section 951A category limitation is USD 166,320, so the US tax is nil and USD 190,080 of credit is lost for good. With the high-tax exclusion (30% is greater than 18.9%): no tested income, no gross-up, no credit, and the same nil US tax, with nothing lost and a simpler return. Recommend the exclusion, made by the controlling domestic shareholder with the return; check the other CFCs in the group first, because the election binds all of them.

```oa-check
name: Corporate net CFC tested income, high-tax German CFC (2026)
inputs:
  pretax_income: 1320000
  foreign_tax: 396000
steps:
  - tested_income: pretax_income - foreign_tax
  - effective_rate: foreign_tax / pretax_income
  - grossed_up: tested_income + foreign_tax
  - deduction_250: grossed_up * 0.40
  - us_tax_before_credit: (grossed_up - deduction_250) * 0.21
  - deemed_paid: foreign_tax * 0.90
  - credit_allowed: min(deemed_paid, us_tax_before_credit)
  - net_us_tax: us_tax_before_credit - credit_allowed
  - credit_lost: deemed_paid - credit_allowed
expected:
  tested_income: 924000.00
  effective_rate: 0.30
  grossed_up: 1320000.00
  deduction_250: 528000.00
  us_tax_before_credit: 166320.00
  deemed_paid: 356400.00
  net_us_tax: 0.00
  credit_lost: 190080.00
```

**Case 2, a decision: an individual with an Irish CFC, section 962 or not.** A US citizen in the 37% bracket owns an Irish trading company that earns USD 300,000 and pays Irish tax of USD 37,500 (12.5%, below 18.9%, so no high-tax exclusion). Tested income is USD 262,500. All earnings will be paid out in a later year, as qualified dividends (Ireland has a comprehensive US treaty). Figures are federal income tax only, before the net investment income tax.

No election: USD 262,500 x 37% = USD 97,125 now; the later distribution is previously taxed and excluded. With the election: gross-up to USD 300,000; section 250 deduction USD 120,000; taxable USD 180,000; 21% = USD 37,800; credit 90% x 37,500 = USD 33,750; US tax now USD 4,050. Later, section 962(d) taxes the distribution to the extent it exceeds the tax paid: USD 262,500 - 4,050 = USD 258,450 at 20% = USD 51,690. Total USD 55,740, which is USD 41,385 less. Recommend the election. If the company were in Singapore (no treaty), the later dividend would be ordinary and most of the saving would become deferral only.

```oa-check
name: Individual section 962 election, Irish CFC (2026)
inputs:
  pretax_income: 300000
  foreign_tax: 37500
  individual_rate: 0.37
  qualified_dividend_rate: 0.20
steps:
  - tested_income: pretax_income - foreign_tax
  - tax_without_election: tested_income * individual_rate
  - grossed_up: tested_income + foreign_tax
  - tax_at_21: (grossed_up - grossed_up * 0.40) * 0.21
  - credit: foreign_tax * 0.90
  - tax_now_with_election: max(tax_at_21 - credit, 0)
  - tax_on_distribution: (tested_income - tax_now_with_election) * qualified_dividend_rate
  - total_with_election: tax_now_with_election + tax_on_distribution
  - saving: tax_without_election - total_with_election
expected:
  tested_income: 262500.00
  tax_without_election: 97125.00
  tax_at_21: 37800.00
  credit: 33750.00
  tax_now_with_election: 4050.00
  tax_on_distribution: 51690.00
  total_with_election: 55740.00
  saving: 41385.00
```

**Case 3: FDDEI.** A US C corporation has deduction eligible income of USD 10,000,000, of which USD 4,000,000 is from documented sales to foreign customers for foreign use. Taxable income is well above USD 4,000,000. Deduction: 33.34% x 4,000,000 = USD 1,333,600. Tax on the FDDEI: (4,000,000 - 1,333,600) x 21% = USD 559,944, an effective rate of 13.9986%.

```oa-check
name: FDDEI deduction (2026)
inputs:
  fddei: 4000000
steps:
  - deduction: fddei * 0.3334
  - tax_on_fddei: (fddei - deduction) * 0.21
  - effective_rate: tax_on_fddei / fddei
expected:
  deduction: 1333600.00
  tax_on_fddei: 559944.00
  effective_rate: 0.139986
```

**Case 4: BEAT.** A US corporation in a group with average gross receipts of USD 2.4 billion has taxable income of USD 300,000,000 after USD 1,000,000,000 of deductions, of which USD 235,100,000 are base erosion tax benefits (a royalty to a Bermuda affiliate of USD 150,000,000, a Swiss management fee of USD 80,000,000 priced at cost plus 8% and not under the services cost method, and USD 5,100,000 of depreciation on a building bought from an affiliate). Regular tax is USD 63,000,000; credits are a research credit of USD 20,000,000 and foreign tax credits of USD 15,000,000.

Base erosion percentage: 235.1 / 1,000 = 23.51%, above 3%. Modified taxable income: USD 535,100,000; times 10.5% = USD 56,185,500. Regular tax for the comparison: 63,000,000 reduced by the credits other than the research credit (USD 15,000,000) = USD 48,000,000. BEAT = USD 8,185,500, on top of regular tax after credits of USD 28,000,000. (The old version of this example showed BEAT of nil in one step and USD 22,510,000 in the next; both were wrong.) Check whether the royalty bore US withholding (Bermuda has no income tax treaty with the US), which would take it out of the base erosion payments to the extent withheld.

```oa-check
name: Base erosion minimum tax (2026)
inputs:
  taxable_income: 300000000
  base_erosion_benefits: 235100000
  total_deductions: 1000000000
  regular_tax: 63000000
  research_credit: 20000000
  other_credits: 15000000
steps:
  - base_erosion_percentage: base_erosion_benefits / total_deductions
  - mti: taxable_income + base_erosion_benefits
  - tentative: mti * 0.105
  - regular_for_beat: regular_tax - other_credits
  - beat: max(tentative - regular_for_beat, 0)
expected:
  base_erosion_percentage: 0.2351
  mti: 535100000.00
  tentative: 56185500.00
  regular_for_beat: 48000000.00
  beat: 8185500.00
```

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-INTL-951B | A foreign parent above US and foreign subsidiaries; section 951B or attribution chains | Refer to a US international tax preparer |
| R-INTL-FY | A fiscal-year CFC or shareholder whose year straddles 1 January 2026 | Refer: the two sets of effective dates can fall in different years |
| R-INTL-PRS | Mid-year transfers, redemptions or new issues | Refer: pro rata share and year-closing rules |
| R-INTL-956 | A section 956 investment in US property | Refer |
| R-INTL-EP | The client cannot give income by category, foreign taxes or earnings and profits | Refuse a final figure |
| R-INTL-7 | Previously taxed earnings accounts over more than two tiers, or section 962 PTEP | Refer |
| R-INTL-NIIT | Net investment income tax on section 962 inclusions or distributions | Flag for the reviewer (CCA 202118008) |
| R-INTL-1 | Transfer pricing studies (section 482) | Refer to a transfer pricing economist |
| R-INTL-2 | Foreign tax credit optimisation beyond the section 951A category | Refer; `us-foreign-tax-credit-1116` for individuals |
| R-INTL-3 | Pillar Two top-up taxes computed abroad (QDMTT, IIR, UTPR) | Refer to the foreign jurisdiction's adviser |
| R-INTL-4 | Treaty positions and limitation on benefits | Refer |
| R-INTL-5 | Inversion planning (section 7874) | Refuse |
| R-INTL-6 | Hybrid instruments and entities (sections 245A(e), 267A) | Refer |
| R-INTL-8 | Foreign trusts holding CFC stock | Coordinate with `us-foreign-trust-reporting` |
| R-INTL-9 | The CFC may also be a PFIC, or the client holds PFICs | Refer |
| R-INTL-10 | Cross-border mergers and acquisitions | Refer |
| R-INTL-965 | Section 965 transition tax installments or a section 965(i) S corporation deferral triggered by a sale | Refer |
| R-INTL-STATE | State conformity to net CFC tested income or FDDEI (for example California) | Refer to the state skill |

## Filing and payment

- **Individuals:** inclusions on Schedule 1 of the 2026 Form 1040, due **15 April 2027** (15 June 2027 automatic extension for a citizen living abroad; 15 October 2027 with Form 4868), with Form 8992, Forms 5471 and, if elected, the section 962 statement, Form 8993 and Form 1118.
- **C corporations:** Form 1120 for a calendar 2026 year is due **15 April 2027** (extension to 15 October 2027), with Forms 8992, 8993, 1118, 5471 and, if the gross receipts test is met, 8991.
- Form 5471 is filed with the return by its due date including extensions: see `us-form-5471-cfc-information`.
- The tax on the inclusions is paid through 2026 estimated tax: `us-quarterly-estimated-tax` for individuals, `us-form-1120-c-corp` for corporations.

## Completion checklist

- [ ] Entity confirmed as a foreign corporation for US tax purposes.
- [ ] Section 958(a) and 958(b) maps built separately, with the 2026 section 958(b)(4) and 951B rules.
- [ ] 10%-or-more and more-than-50% tests run on vote and value for every day of the year.
- [ ] Pro rata shares under the 2026 any-day rule.
- [ ] Subpart F income by category; de minimis, full inclusion, look-through and earnings limit applied.
- [ ] Tested income after foreign taxes; no QBAI return for 2026.
- [ ] High-tax exception and exclusion tested at greater than 18.9%, both outcomes modelled.
- [ ] Corporations: 40% section 250, 90% credit with the full gross-up, section 904(b)(5) allocation.
- [ ] Individuals: with and without section 962, including section 962(d) and the dividend's character.
- [ ] FDDEI: 33.34%, intangible sale gains after 16 June 2025 excluded, foreign-use documents on file.
- [ ] BEAT: gross receipts test, base erosion percentage, 10.5% against regular tax less unprotected credits.
- [ ] Output labelled as a draft working paper for sign-off by a credentialed preparer.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Public Law 119-21. Read for sections 70311 (section 904(b)(5)), 70312 (90%, section 78, 10% PTEP disallowance after 28 June 2025), 70321 (33.34% and 40%, 250(a)(3) struck), 70322 (DEI, intangible sales after 16 June 2025, no interest or research expense), 70323 (net CFC tested income, QBAI repeal, FDDEI), 70331 (10.5% BEAT), 70351 (954(c)(6) permanent), 70352 (898 repeal), 70353 (958(b)(4), 951B) and 70354 (any-day pro rata). | https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm | 2026-11-13 |
| 26 U.S.C. 951 (govinfo). Read for (b) "10 percent or more" of vote or value. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partIII-subpartF-sec951.htm | 2026-11-13 |
| 26 U.S.C. 951A (govinfo, 2024 edition). Read for the tested income exclusions and the inclusion's treatment under 959, 961 and 962. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partIII-subpartF-sec951A.htm | 2026-11-13 |
| 26 U.S.C. 952 (govinfo). Read for subpart F income and the (c) earnings limit. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partIII-subpartF-sec952.htm | 2026-11-13 |
| 26 U.S.C. 954 (govinfo). Read for the categories, (b)(3) de minimis ($1,000,000, 5%) and 70% rules, and (b)(4) "greater than 90 percent of the maximum rate". | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partIII-subpartF-sec954.htm | 2026-11-13 |
| 26 U.S.C. 957 (govinfo). Read for "more than 50 percent". | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partIII-subpartF-sec957.htm | 2026-11-13 |
| 26 U.S.C. 958 (govinfo). Read for (a) and (b) ownership and the 2017 repeal of (b)(4) that the 2025 law reverses. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partIII-subpartF-sec958.htm | 2026-11-13 |
| 26 U.S.C. 962 (govinfo). Read for the election and (d) distributions. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partIII-subpartF-sec962.htm | 2026-11-13 |
| 26 U.S.C. 11 (govinfo). Read for the 21% rate. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partII-sec11.htm | 2026-11-13 |
| 26 U.S.C. 250 (govinfo, 2024 edition). Read for the (a)(2) taxable income limit. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVIII-sec250.htm | 2026-11-13 |
| 26 U.S.C. 59A (govinfo, 2024 edition). Read for (b)(1)(B) protected credits and 80%, (b)(3) bank increase, (c)(4) and (e) ($500,000,000, 3%, 2%). | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partVII-sec59A.htm | 2026-11-13 |
| Treas. Reg. 1.951A-2 (eCFR). Read for (c)(7) high-tax election, 24 months, tested units. | https://www.ecfr.gov/current/title-26/chapter-I/subchapter-A/part-1/section-1.951A-2 | 2026-11-13 |
| Treas. Reg. 1.962-2 (eCFR). Read for who may elect and the statement "with his return". | https://www.ecfr.gov/current/title-26/chapter-I/subchapter-A/part-1/section-1.962-2 | 2026-11-13 |
| Instructions for Form 8993 (2025). Read for the note that the deductions fall to 33.34% and 40% after 2025. | https://www.irs.gov/pub/irs-pdf/i8993.pdf | 2026-11-13 |
| Instructions for Form 8992 (Rev. December 2024). Read for Schedules A and B and consolidated groups. | https://www.irs.gov/pub/irs-pdf/i8992.pdf | 2026-11-13 |
| Instructions for Form 8991 (2025). Read for who files and the schedules. | https://www.irs.gov/pub/irs-pdf/i8991.pdf | 2026-11-13 |
| Instructions for Form 5471 (2025). Read for section 962 electing shareholders on Schedules J and P. | https://www.irs.gov/pub/irs-pdf/i5471.pdf | 2026-11-13 |

Not yet confirmed: 2026 revisions of Forms 8992, 8993 and 8991 and their instructions were not published when read, so line numbers are not quoted; Treasury has not yet updated Treas. Reg. 1.951A-2, 1.250(b)-1 to 1.250(b)-6 or 1.59A-1 to 1.59A-10 for the 2025 law, so the high-tax election mechanics, the FDDEI documentation rules and BEAT regulatory details are carried forward from the pre-2026 regulations and must be checked when new guidance appears; the qualified-dividend character of section 962(d) distributions rests on the treaty status of the CFC's country and is a reviewer point.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `us-gilti-fdii-beat` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/us-gilti-fdii-beat. If neither is available, confirm every figure against the official source pages cited above before relying on it.
