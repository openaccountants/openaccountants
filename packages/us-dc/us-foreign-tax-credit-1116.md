---
name: us-foreign-tax-credit-1116
description: Work out a US individual's 2026 foreign tax credit on Form 1116, or the no-Form-1116 election, for a citizen or resident alien who paid foreign income tax. Covers credit or deduction, creditable taxes and the Notice 2023-55 and 2023-80 relief, the separate categories, sourcing, the section 904(a) limit, the USD 300 or USD 600 de minimis election under section 904(j), the 1-year carryback and 10-year carryforward, cash or accrual and currency, the line 12 reduction for income excluded on Form 2555, the AMT credit, later changes in foreign tax, and the 2026 One Big Beautiful Bill Act changes for section 951A (net CFC tested income). Trigger on "foreign tax credit", "Form 1116", "FTC", "foreign taxes paid", "1099-DIV foreign tax", "FTC carryover", "excess foreign tax credit", "high-taxed income". Load us-foreign-earned-income-2555 when the person also excludes foreign earned income. Federal only.
version: "1.0"
jurisdiction: US
tax_year: 2026
last_updated: 2026-11-13
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: cross-border
type: computation
---

# US foreign tax credit for individuals (Form 1116), tax year 2026

> **Source-cited draft.** Built from the 2025 Instructions for Form 1116 (the 2026 form and instructions were not yet published), IRS Pub. 514 (for 2025 returns), the 2025 Instructions for Form 6251, Notices 2023-55 and 2023-80, 26 U.S.C. 904 and Public Law 119-21 sections 70311, 70312 and 70321, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** A US citizen or resident alien who paid or accrued foreign income tax can credit it against US tax, category by category, up to the US tax on the foreign-source share of taxable income: **limit = US tax x (foreign-source taxable income in the category / worldwide taxable income)** (section 904(a)). Unused credit carries **back 1 year, then forward 10 years**, in the same category. If all the foreign income is passive, reported on Forms 1099 or K-1 or K-3, and the creditable tax is **not more than USD 300 (USD 600 on a joint return)**, the credit can be claimed directly on Schedule 3, line 1 without Form 1116, but then nothing carries to or from that year. Tax on income excluded on Form 2555 can never be credited. For 2026 the 2025 form and instructions are the latest published; check line numbers against the 2026 versions when they appear.

## Scope and who this is for

In scope: a US citizen or resident alien filing Form 1040 for 2026 who paid or accrued foreign income tax on foreign-source income. The skill explains how to:

- choose between the credit and the itemized deduction;
- decide whether a foreign tax is creditable, including the 2022 regulations and the Notice relief;
- source the income and sort it into the separate categories ("baskets");
- work out the limit on each Form 1116, and summarise in Part IV;
- use the no-Form-1116 election;
- carry excess credit back and forward (Schedule B);
- convert currency on the cash or accrual basis;
- reduce the credit for income excluded on Form 2555;
- run the AMT credit, and report later changes in foreign tax (Schedule C).

Out of scope, and where it goes:

| Topic | Skill |
| --- | --- |
| The foreign earned income exclusion and housing, and the choice between exclusion and credit | `us-foreign-earned-income-2555` |
| The rest of Form 1040 and the 2026 tax brackets | `us-form-1040-individual-return` |
| CFCs, GILTI or net CFC tested income, section 962 elections and Form 1118 | `us-cfc-gilti`, `us-form-5471-cfc-information` |
| FBAR and Form 8938 | `us-fbar-and-fatca-8938` |
| Moving abroad, the wider checklist | `us-citizen-moving-abroad-tax` |
| Nonresident aliens | `us-form-1040-nr-nonresident-return` |
| Amending a return for a carryback | `us-amended-return-form-1040-including-capital` |
| Corporations, estates and trusts | not covered; see "When to refuse or refer" |

## Ask the client first

1. Which countries taxed you, on what income, and in which currency? Bring the foreign return or assessment, payslips, or the Form 1099-DIV, 1099-INT, Schedule K-1 or K-3 that shows the tax.
2. Was the tax **legally owed**, or could part of it be refunded (for example, the treaty rate is lower than the rate withheld)?
3. Is any foreign tax still under dispute, or has any been refunded or changed since an earlier US return?
4. Have you ever **deducted** foreign taxes on Schedule A instead of crediting them, and for which years?
5. Do you have a foreign tax credit carryover from earlier years? Bring the 2025 Schedule B (Form 1116).
6. Have you ever checked the "Accrued" box in Part II of Form 1116?
7. Are you claiming, or have you ever claimed or revoked, the foreign earned income exclusion (Form 2555)?
8. For foreign dividends: did you hold the shares long enough around each ex-dividend date?
9. Are you a US shareholder of a controlled foreign corporation, a partner in a partnership with foreign activity, or someone who has made a section 962 election?
10. Did any income come from a country on the section 901(j) list?
11. Are you subject to the alternative minimum tax?
12. Do you rely on a tax treaty to treat any income as foreign source or to claim a credit the Code does not allow?

## The method, step by step

### Rates, bands and thresholds

| Item | Amount | Source |
| --- | --- | --- |
| No-Form-1116 election: maximum creditable foreign tax, other than joint returns | USD 300 | [26 U.S.C. 904(j)(2)(B)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partIII-subpartA-sec904.htm) |
| No-Form-1116 election: maximum creditable foreign tax, joint return | USD 600 | [26 U.S.C. 904(j)(2)(B)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partIII-subpartA-sec904.htm) |
| Carryback of excess credit | 1 year | [26 U.S.C. 904(c)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partIII-subpartA-sec904.htm) |
| Carryforward of excess credit | 10 years | [26 U.S.C. 904(c)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partIII-subpartA-sec904.htm) |
| Time to switch from deduction to credit (from the unextended due date of the year the tax was paid or accrued) | 10 years | [IRS Pub. 514 (2025), Making or Changing Your Choice](https://www.irs.gov/pub/irs-pdf/p514.pdf) |
| Time to switch from credit to deduction | 3 years from filing or 2 years from paying, whichever is later | [IRS Pub. 514 (2025), Making or Changing Your Choice](https://www.irs.gov/pub/irs-pdf/p514.pdf) |
| Dividend holding period for the credit | 16 days within the 31-day period starting 15 days before the ex-dividend date | [IRS Pub. 514 (2025), Holding period](https://www.irs.gov/pub/irs-pdf/p514.pdf) |
| Accrued tax must be paid within | 24 months after the year it relates to | [Instructions for Form 1116 (2025)](https://www.irs.gov/pub/irs-pdf/i1116.pdf) |
| Qualified dividend and capital gain adjustment exception: foreign gains plus dividends must be less than | USD 20,000 | [Instructions for Form 1116 (2025), Qualified Dividends and Capital Gains](https://www.irs.gov/pub/irs-pdf/i1116.pdf) |
| Adjustment exception threshold, 2025 returns: single, head of household, married filing separately | USD 197,300 | [Instructions for Form 1116 (2025)](https://www.irs.gov/pub/irs-pdf/i1116.pdf) |
| Adjustment exception threshold, 2025 returns: married filing jointly, qualifying surviving spouse | USD 394,600 | [Instructions for Form 1116 (2025)](https://www.irs.gov/pub/irs-pdf/i1116.pdf) |
| Interest expense: may be allocated all to US source if gross foreign-source income (including excluded income) is not more than | USD 5,000 | [Instructions for Form 1116 (2025), lines 4a and 4b](https://www.irs.gov/pub/irs-pdf/i1116.pdf) |
| Sourcing exception: gain on nondepreciable personal property sold with a tax home abroad is foreign source if foreign tax on it is at least | 10% of the gain | [Instructions for Form 1116 (2025)](https://www.irs.gov/pub/irs-pdf/i1116.pdf) |
| Senior deduction added back on line 18 (per person aged 65 or over, 2025 to 2028) | USD 6,000 | [Public Law 119-21, section 70103](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| Penalty for not notifying a foreign tax redetermination, per month or part month | 5% of the tax due, up to 25% | [IRS Pub. 514 (2025)](https://www.irs.gov/pub/irs-pdf/p514.pdf) |
| Section 250 deduction for net CFC tested income, tax years beginning after 31 December 2025 | 40% | [Public Law 119-21, section 70321](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| Section 960(d) deemed-paid credit share, tax years beginning after 31 December 2025 | 90% | [Public Law 119-21, section 70312(a)](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| Credit disallowed for foreign tax on a section 959(a) distribution of previously taxed net CFC tested income (after 28 June 2025) | 10% | [Public Law 119-21, section 70312(b)](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |

None of these is indexed except the adjustment exception threshold, which follows the brackets; the 2026 thresholds will be in the 2026 instructions (see "Not yet confirmed"). The maximum foreign earned income exclusion for 2026 is owned by `us-foreign-earned-income-2555`.

### Step 1. Confirm the tax can be credited

It must be a foreign income tax (or a tax in place of one) that the person legally owes and actually paid or accrued. Taxes that could be refunded (for example withholding above the treaty rate, whether or not the refund is claimed), taxes offset by a subsidy, and interest or penalties do not count. Source: [Instructions for Form 1116 (2025), Foreign Taxes Not Eligible for a Credit](https://www.irs.gov/pub/irs-pdf/i1116.pdf).

**The 2022 regulations and the Notice relief** ([Notice 2023-55](https://www.irs.gov/pub/irs-drop/n-23-55.pdf); [Notice 2023-80](https://www.irs.gov/pub/irs-drop/n-23-80.pdf)):

- T.D. 9959 (published 4 January 2022, with correcting amendments on 27 July 2022) rewrote Reg. 1.901-2 and 1.903-1 on what counts as a creditable foreign income tax, adding a net gain requirement and attribution requirements.
- Notice 2023-55 lets taxpayers decide creditability under the pre-2022 rules instead (former Reg. 1.901-2(a) and (b), as revised on 1 April 2021 and modified by the Notice), and apply 1.903-1 without the jurisdiction-to-tax and source-based attribution requirements.
- Notice 2023-80 extended the relief to tax years ending before a notice or other guidance withdrawing or modifying it is issued. The 2025 Form 1116 instructions describe the relief as extended "until further notice".
- Conditions: apply it to **all** foreign taxes paid in the relief year, including taxes of others the person can claim (such as a CFC's taxes for a US shareholder). It cannot be used to credit a tax for which a deduction is allowed in that or any other year.
- **Digital services taxes stay non-creditable** even under the relief: Notice 2023-55 states that a gross-basis DST does not meet the net income requirement and is not a tax in lieu of an income tax.
- **Gross withholding on services or royalties** by a country that sources income by where the payer is: under the relief, test it as an in-lieu-of tax under 1.903-1 and document the analysis. Where unclear and material, refer.
- **Before filing a 2026 return,** check IRS.gov/Form1116 and the Internal Revenue Bulletin for any notice that withdraws or modifies Notice 2023-80, and apply its effective date.

**Holding period** ([IRS Pub. 514 (2025)](https://www.irs.gov/pub/irs-pdf/p514.pdf)):

- Tax withheld on a **dividend** is not creditable unless the shares were held at least 16 days within the 31-day period that begins 15 days before the ex-dividend date. A longer period applies to some preferred-stock dividends.
- A similar 16-day rule applies to other income or gain from property.
- Tax is also not creditable to the extent the person must make related payments on substantially similar or related positions.
- Tax that fails these tests may be **deducted** even in a year the credit is taken.

**Treaty-based credit.** A person relying on a treaty to credit a tax the Code does not allow, or to re-source income, discloses it on Form 8833. Source: [Instructions for Form 1116 (2025), category f](https://www.irs.gov/pub/irs-pdf/i1116.pdf).

**Contested tax.** A contested foreign income tax cannot be credited until the contest is resolved, unless the person elects a provisional credit, which needs Form 7204 and then Schedule C (Form 1116) for each later year until it is resolved. Source: [IRS Pub. 514 (2025)](https://www.irs.gov/pub/irs-pdf/p514.pdf).

### Step 2. Credit or deduction for the year

- The credit reduces US tax dollar for dollar, works with the standard deduction, and is the only one that carries back or forward. The IRS says the credit is better in most cases but tells you to work out both.
- In one year the person must credit **all** qualifying foreign income taxes or deduct **all** of them. A credit cannot be carried into a year in which foreign taxes were deducted, and the carryover is reduced by the amount that year could have absorbed.
- Change of choice: to the credit within 10 years from the unextended due date for the year the taxes were paid or accrued (for 2026 taxes, from 15 April 2027); to the deduction within 3 years from filing or 2 years from paying, whichever is later. Either period can be extended by agreement.
- A refund claim caused by foreign tax paid or accrued has a 10-year limitation period from the due date of the return for the year the taxes were actually paid or accrued.

Source: [IRS Pub. 514 (2025), Choosing To Take Credit or Deduction](https://www.irs.gov/pub/irs-pdf/p514.pdf).

### Step 3. Test the no-Form-1116 election

The credit may be claimed without Form 1116 only if **all** of these are true for the year ([26 U.S.C. 904(j)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partIII-subpartA-sec904.htm); [Instructions for Form 1116 (2025), Election To Claim the Foreign Tax Credit Without Filing Form 1116](https://www.irs.gov/pub/irs-pdf/i1116.pdf)):

1. **All** foreign-source gross income is passive category income (for this test, high-taxed income and export financing interest still count as passive).
2. All that income, and the foreign tax on it, was reported on a qualified payee statement: Form 1099-DIV or 1099-INT, Schedule K-1 (Form 1041), Schedule K-3 (Form 1065 or 1120-S), or a similar substitute statement.
3. Total creditable foreign taxes are **not more than USD 300**, or **not more than USD 600** on a joint return.
4. The person is an individual (estates and trusts cannot elect).
5. Elect by entering the smaller of total foreign tax or regular tax on Schedule 3 (Form 1040), line 1.

**What it costs:** the section 904 limit does not apply; **no carryover** to or from the election year (that year's taxes cannot be carried anywhere, and carryovers from other years cannot be used in it; their periods are not extended); for AMT the credit equals the regular credit and no AMT carryback or carryforward is allowed to or from that year. The normal creditability rules, the holding period and the line 12 reductions still apply.

**Traps:** any foreign-source wages, self-employment or business income in gross income blocks the election, even with no foreign tax on it, including wages above the exclusion limit. A client with carryovers or with more creditable tax than the election allows may do better filing Form 1116 (Case 2).

### Step 4. Source the income and sort it into categories

**Sourcing** ([Instructions for Form 1116 (2025), Income From Sources Outside the United States](https://www.irs.gov/pub/irs-pdf/i1116.pdf)):

- Pay for services performed abroad is foreign source. An employee's pay (other than fringe benefits) for work both in and outside the US is split on a time basis.
- Dividends from a corporation incorporated abroad and interest from a payer located abroad are foreign source.
- Gain on selling personal property by a US resident is generally US source. Exception: nondepreciable personal property sold while the person has a tax home abroad is foreign source if foreign tax of at least 10% of the gain was paid.

**One Form 1116 per category.** On the 2025 form the boxes are:

| Box | Category | Typical individual items |
| --- | --- | --- |
| a | Section 951A category income | A US shareholder's CFC inclusion under section 951A; from 2026 the statute calls it net CFC tested income (previously GILTI). No carryback or carryover |
| b | Foreign branch category income | Business profits of a qualified business unit in a foreign country |
| c | Passive category income | Dividends, interest, royalties, rents, annuities, investment gains, excluding high-taxed income and export financing interest |
| d | General category income | Wages, self-employment and active business income, and anything not in another category |
| e | Section 901(j) income | Income from a sanctioned country; one Form 1116 per country |
| f | Certain income re-sourced by treaty | US-source income treated as foreign under a treaty; one Form 1116 per treaty country; Form 8833 may be required |
| g | Lump-sum distributions | Foreign tax on a qualifying foreign-source lump-sum pension distribution |

Source: [Form 1116 (2025)](https://www.irs.gov/pub/irs-pdf/f1116.pdf); [26 U.S.C. 904(d)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partIII-subpartA-sec904.htm).

- **High-taxed income moves out of passive.** Passive income is high-taxed if the foreign tax on it, after expenses, exceeds the highest US tax that can be imposed on it (section 904(d)(2)(F)). This is a classification rule, not an election. Report the income as a negative amount on the passive Form 1116 and a positive amount on the general category form, and move the related tax on line 13 the same way. (The old version of this skill called this the section 904(j) "high-tax kick-out"; section 904(j) is the de minimis election.)
- **Look-through:** dividends, interest, rents or royalties from a CFC in which the person owns 10% or more of the vote or value may not be passive. Refer.
- **Section 901(j) countries.** Pub. 514 for 2025 lists Iran, Libya (a waiver has applied since 10 December 2004), North Korea, Sudan and Syria. Tax paid **to** a sanctioned country is not creditable; tax paid to a non-sanctioned residence country on that income can be (keep completing Form 1116 past line 17). The 2026 list will be in the 2026 Pub. 514; do not assume the 2025 list carries over. Source: [IRS Pub. 514 (2025)](https://www.irs.gov/pub/irs-pdf/p514.pdf).

### Step 5. Part I: income, deductions and the adjustments

- Put deductions **definitely related** to the foreign income (for example Schedule C expenses of the foreign work) on line 2.
- Apportion the standard deduction or other itemized deductions on lines 3a to 3g by gross income (line 3f is line 3d over line 3e, to at least four decimal places). Lines 3d and 3e **include** foreign earned income excluded on Form 2555, while line 1a includes only wages not excluded.
- Home mortgage interest goes on line 4a, other interest on line 4b, losses on line 5. If gross foreign-source income (including excluded income) is not more than USD 5,000, all interest expense may be allocated to US source.
- Partnerships and S corporations report their foreign allocations on Schedule K-3.
- **Senior deduction.** The section 151(d)(5)(C) deduction of USD 6,000 per person aged 65 or over (Schedule 1-A), for 2025 through 2028, is added back to taxable income on line 18, as the line 3b and line 18 instructions describe.
- **Qualified dividends and capital gains.** Foreign-source qualified dividends and capital gains taxed at preferential rates must usually be scaled down (Worksheet for Line 18 and Worksheets A and B). Skip this under the **adjustment exception** only if both are true: line 5 of the Qualified Dividends and Capital Gain Tax Worksheet is not more than the year's threshold (for 2025, USD 197,300 single, head of household or married filing separately; USD 394,600 joint or qualifying surviving spouse), and foreign-source net capital gain plus qualified dividends is **less than USD 20,000**.
- **Line 16 adjustments**, in the order the instructions set out: the section 461(l) loss, foreign losses, US losses, and recapture of overall foreign loss, separate limitation loss and overall domestic loss accounts. If line 15 is zero or a loss there is generally no credit for that category, but line 16 is still completed.
- **New from 2026 for section 951A category income:** only the section 250 deduction for net CFC tested income (and section 164(a)(3) taxes on it) and deductions directly allocable to that income are allocated to it; no interest expense or research costs are. What would otherwise have gone to it is allocated to US source income. Source: [Public Law 119-21, section 70311, new section 904(b)(5)](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm), tax years beginning after 31 December 2025.

Source: [Instructions for Form 1116 (2025), Part I](https://www.irs.gov/pub/irs-pdf/i1116.pdf).

### Step 6. Part II: the foreign taxes, cash or accrual, currency

**Cash basis (the default for most individuals):** credit in the year the tax is **paid**, converted at the rate on the date paid (withheld tax: the date withheld; foreign estimated payments: each payment date). Do **not** use the yearly average rate on a cash basis.

**Electing accrual:** a cash-basis individual can credit taxes in the year they accrue by checking the "Accrued" box in Part II on a **timely filed original return**, never on an amended return. The choice binds all later years and covers all foreign taxes. Foreign taxes generally accrue on the last day of the foreign tax year.

**Accrual conversion:** accrued taxes use the **average exchange rate** for the tax year they relate to, except when paid before that year starts, more than 24 months after it ends, or in an inflationary currency; then use the date-paid rate. The person can elect the date-paid rate for accrued taxes in a nonfunctional currency, by the due date including extensions, binding later years unless the IRS consents to revoke.

**Other Part II rules:**

- Tax already shown in dollars on a Form 1099 needs no conversion; enter "1099 taxes".
- **Accrued but unpaid tax** not paid within 24 months after the year it relates to reduces the credit until paid.

**Line 12 reductions** include:

- **Tax on income excluded on Form 2555.** Multiply the foreign tax on foreign earned income by: (excluded foreign earned income and housing amounts, minus otherwise deductible expenses allocable to them, not counting the housing deduction) / (total foreign earned income, minus deductible expenses allocable to it, including the housing deduction). If the foreign tax also covers other income and cannot be separated, the denominator is all income subject to that foreign tax, minus its expenses. If all the foreign earned income is excluded, none of its tax is creditable. Source: [Instructions for Form 1116 (2025), line 12](https://www.irs.gov/pub/irs-pdf/i1116.pdf); [26 U.S.C. 911(d)(6)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partIII-subpartB-sec911.htm).
- Tax on Puerto Rico income exempt from US tax, tax connected with a foreign tax credit splitting event, and the other items the line 12 instructions list.

Source: [Instructions for Form 1116 (2025), Part II](https://www.irs.gov/pub/irs-pdf/i1116.pdf); [IRS Pub. 514 (2025), Translating foreign currency](https://www.irs.gov/pub/irs-pdf/p514.pdf).

### Step 7. Part III: the limit

1. **Line 17:** foreign-source taxable income in the category, after the line 16 adjustments. **Line 18:** worldwide taxable income (with the senior deduction added back). **Line 19:** line 17 divided by line 18; enter 1 if line 17 is more than line 18.
2. **Line 20:** regular tax liability. On the 2025 form that is Form 1040, line 16, plus Schedule 2, Part I, line 1z, less any Form 4972 tax. It does **not** include the section 1411 net investment income tax, and the Form 1116 credit does not reduce that tax.
3. **Line 21:** line 20 x line 19. **Line 22:** any section 960(c) increase. **Line 23:** the limit.
4. **Line 24**, the credit for the category, is the smaller of the foreign tax available (line 14) and the limit (line 23).

Source: [26 U.S.C. 904(a)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partIII-subpartA-sec904.htm); [Instructions for Form 1116 (2025), Part III](https://www.irs.gov/pub/irs-pdf/i1116.pdf).

### Step 8. Part IV, carryovers and Schedule B

- **Part IV (lines 25 to 33)** must be completed even when only one Form 1116 is filed (new for 2025). Line 33 is the smaller of line 20 and line 32. The credit goes to Schedule 3 (Form 1040), line 1.
- **Excess foreign tax** in a category is carried **back 1 year**, then **forward 10 years**, in that order, and stays in the same category. The carryback is claimed on Form 1040-X with a revised Form 1116 for the earlier year. The period is not extended because a year could not absorb it. Current-year taxes are used first, then the oldest carryover.
- **No carryback or carryover** for section 951A category income; leave line 10 blank on that form.
- No credit can be carried into a year in which foreign taxes were **deducted**; the carryover is also reduced by what that year could have used.
- **Schedule B (Form 1116)** reconciles the carryover year to year. Attach one for each category whenever line 10 shows a carryover or the year creates one.

Source: [26 U.S.C. 904(c)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partIII-subpartA-sec904.htm); [Instructions for Form 1116 (2025), line 10 and Part IV](https://www.irs.gov/pub/irs-pdf/i1116.pdf).

### Step 9. The AMT foreign tax credit

- Work out the AMT foreign tax credit (AMTFTC) on Form 6251, line 8, when line 10 of Form 6251 (regular tax after the regular credit) is less than line 7.
- If the no-Form-1116 election was made, the AMTFTC equals the regular credit.
- Otherwise prepare a separate AMT Form 1116 for each category, with "AMT" and the category in the top margin, using AMT income and deductions, and testing for high-taxed income at the **AMT rate**.
- **Simplified limitation election:** use the regular-tax foreign-source income (line 17) on the AMT Form 1116. It must be made for the first tax year after 1997 for which an AMTFTC is claimed, or never; once made it binds later years unless the IRS consents to revoke.
- Unused AMTFTC carries back and forward under section 904(c), tracked separately from the regular carryover; none in a year the no-Form-1116 election applies.
- A person who also excludes income uses the Foreign Earned Income Tax Worksheet in the Form 6251 instructions.

Source: [Instructions for Form 6251 (2025), line 8](https://www.irs.gov/pub/irs-pdf/i6251.pdf).

### Step 10. When the person also excludes foreign earned income

- The exclusion, housing amounts and the decision between exclusion and credit are in `us-foreign-earned-income-2555`.
- No credit for foreign tax allocable to excluded income: reduce it on line 12 (Step 6).
- Pay above the exclusion stays in gross income, is general category income, and blocks the no-Form-1116 election.
- Tax on the income left is stacked: figured at the rates that would apply without the exclusion (section 911(f)), so line 20 is the stacked tax.
- Claiming the credit or deduction on the excluded pay in a later year, instead of the exclusion, is treated as revoking the exclusion, which then cannot be elected again before the 6th tax year after without IRS consent. Claiming the credit only on tax on pay above the exclusion is allowed.

### Step 11. Section 951A category (net CFC tested income) for individuals: flag only

- For tax years beginning after 31 December 2025, a US shareholder of a CFC includes **net CFC tested income** (the renamed GILTI) under section 951A.
- **Without a section 962 election** an individual gets no deemed-paid credit for the CFC's foreign taxes and no section 250 deduction; those apply to domestic corporations.
- **With a section 962 election** the credit is claimed on Form 1118, not Form 1116. For tax years beginning after 31 December 2025 the section 250 deduction for net CFC tested income is **40%** (was 50%) and the section 960(d) deemed-paid credit is **90%** (was 80%) of the inclusion percentage times tested foreign income taxes.
- **Previously taxed distributions:** no credit for **10%** of foreign taxes on an amount excluded under section 959(a) because of an earlier section 951A inclusion, for amounts after 28 June 2025. Withholding tax on such a distribution otherwise goes on Form 1116, with or without a section 962 election.
- This skill only flags these items; refer the computation (R-FTC-2).

Source: [Public Law 119-21, sections 70312 and 70321](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm).

## Boundary and exception table

| Situation | Rule | Source |
| --- | --- | --- |
| Tax exactly USD 300 (not a joint return), all passive, all on Forms 1099 | Election available ("not more than") | [26 U.S.C. 904(j)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partIII-subpartA-sec904.htm) |
| Tax one dollar over the cap, or any non-passive foreign income | Election not available; file Form 1116 | [26 U.S.C. 904(j)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partIII-subpartA-sec904.htm) |
| Foreign qualified dividends plus net capital gain of exactly USD 20,000 | Adjustment exception fails (needs "less than") | [Instructions for Form 1116 (2025)](https://www.irs.gov/pub/irs-pdf/i1116.pdf) |
| Tax withheld above the treaty rate | Only the treaty-rate amount is creditable, whether or not the refund is claimed | [Instructions for Form 1116 (2025)](https://www.irs.gov/pub/irs-pdf/i1116.pdf) |
| Digital services tax | Not creditable, even under the Notice relief | [Notice 2023-55](https://www.irs.gov/pub/irs-drop/n-23-55.pdf) |
| Tax on wages excluded on Form 2555 | Not creditable; reduce on line 12 | [Instructions for Form 1116 (2025)](https://www.irs.gov/pub/irs-pdf/i1116.pdf) |
| Section 951A category excess | No carryback or carryover | [Instructions for Form 1116 (2025)](https://www.irs.gov/pub/irs-pdf/i1116.pdf) |
| Accrued tax unpaid 24 months after year end | Reduce the credit until paid | [Instructions for Form 1116 (2025)](https://www.irs.gov/pub/irs-pdf/i1116.pdf) |
| "Accrued" box first checked on an amended return | Not allowed | [Instructions for Form 1116 (2025)](https://www.irs.gov/pub/irs-pdf/i1116.pdf) |
| Net investment income tax | The Form 1116 credit does not reduce it (not regular tax liability) | [Instructions for Form 1116 (2025)](https://www.irs.gov/pub/irs-pdf/i1116.pdf) |
| Dividend shares held 15 days or fewer in the 31-day window | Not creditable; may be deducted | [IRS Pub. 514 (2025)](https://www.irs.gov/pub/irs-pdf/p514.pdf) |
| Tax paid to a section 901(j) country | Not creditable; residence-country tax on the same income may be | [IRS Pub. 514 (2025)](https://www.irs.gov/pub/irs-pdf/p514.pdf) |
| Foreign taxes deducted in a year | No carryover can be used in that year | [IRS Pub. 514 (2025)](https://www.irs.gov/pub/irs-pdf/p514.pdf) |

### Defaults when a fact is missing

| Missing fact | Default, and flag it |
| --- | --- |
| Cash or accrual history | Cash basis, date-paid rates, until the earlier returns show the "Accrued" box |
| Prior-year carryover | Zero; ask for the 2025 Schedule B |
| Whether tax is refundable under a treaty | Credit only the treaty rate |
| Holding period on fund dividends | Assume met for long-held funds; ask where shares were bought or sold near the ex-dividend date |
| Category of a K-3 item | Follow the K-3; do not re-classify |
| Whether the Notice 2023-80 relief is still in force | Check IRS.gov/Form1116 before filing; if not checked, say so |
| Exchange rate for withheld tax | The rate on each withholding date |
| Whether the client excludes income on Form 2555 | Ask; never credit tax on excluded pay |

### Red flags to raise with the client

| Flag | Why it matters |
| --- | --- |
| Foreign tax far above US tax on the same income | Large carryover; check the exclusion is not also being claimed and plan its use |
| Withholding at a non-treaty rate | Part is refundable abroad and not creditable |
| A digital services tax or a gross-basis levy | Not creditable |
| Foreign tax refund or reassessment since the last return | Schedule C and possibly an amended return; penalty for not notifying |
| Foreign tax first claimed as a deduction in a past year | No carryover into that year; check the 10-year window to switch |
| CFC shares or a section 962 election | Section 951A category and Form 1118: refer |
| No-Form-1116 election used while a carryover exists | Carryover cannot be used that year and its clock keeps running |
| Income from a sanctioned country | Separate Form 1116, often no credit |

## Worked cases

The 2026 single and joint brackets used for line 20 are from Rev. Proc. 2025-32 and are owned by `us-form-1040-individual-return`. Taxpayers are invented.

**Case 1, the ordinary general category limit.** A single filer on the cash basis, no carryovers. Foreign-source general category taxable income (line 17) USD 60,000; worldwide taxable income (line 18) USD 150,000; regular tax (line 20) on USD 150,000 at the 2026 single rates is USD 28,598. Foreign income tax withheld USD 15,000, converted at the withholding-date rates.

Limit: USD 28,598 x 60,000 / 150,000 = USD 11,439.20. Credit: the smaller of USD 15,000 and USD 11,439.20. The excess of USD 3,560.80 is carried back to 2025 first (Form 1040-X with a revised 2025 Form 1116); any remainder carries forward up to 2036 in the general category. Attach Schedule B.

```oa-check
name: Form 1116 general category limit and carryover, single (2026)
inputs:
  foreign_taxable: 60000
  worldwide_taxable: 150000
  foreign_tax: 15000
steps:
  - line_20: 0.10 * min(worldwide_taxable, 12400) + 0.12 * clamp(worldwide_taxable - 12400, 0, 38000) + 0.22 * clamp(worldwide_taxable - 50400, 0, 55300) + 0.24 * clamp(worldwide_taxable - 105700, 0, 96075)
  - line_19: min(foreign_taxable / worldwide_taxable, 1)
  - line_21: line_20 * line_19
  - line_24: min(foreign_tax, line_21)
  - excess: foreign_tax - line_24
expected:
  line_20: 28598.00
  line_21: 11439.20
  line_24: 11439.20
  excess: 3560.80
```

**Case 2, a decision: the no-Form-1116 election or Form 1116?** A married couple filing jointly has only foreign fund dividends reported on Forms 1099-DIV, with foreign tax of USD 580 shown on the forms, all holding periods met, and a USD 1,200 passive category carryover from 2025. Foreign passive taxable income after allocated deductions (line 17) is USD 8,000; worldwide taxable income is USD 120,000; regular tax at the 2026 joint rates is USD 15,824.

The election is available (USD 580 is not more than USD 600), and the credit would be USD 580, with the carryover unusable this year and still ageing. Form 1116: limit USD 15,824 x 8,000 / 120,000 = USD 1,054.93; tax available USD 580 plus USD 1,200 carryover = USD 1,780; credit USD 1,054.93. **File Form 1116**: it gives USD 474.93 more credit this year and uses the oldest carryover, leaving USD 725.07 to carry forward. Without the carryover the election would give the same USD 580 with less paperwork. Had one spouse also had foreign consulting fees, even with no foreign tax, the election would fail outright because not all foreign income is passive.

```oa-check
name: No-Form-1116 election against Form 1116 with a carryover, joint (2026)
inputs:
  foreign_tax: 580
  carryover: 1200
  foreign_passive_taxable: 8000
  worldwide_taxable: 120000
  de_minimis_cap: 600
steps:
  - regular_tax: 0.10 * min(worldwide_taxable, 24800) + 0.12 * clamp(worldwide_taxable - 24800, 0, 76000) + 0.22 * clamp(worldwide_taxable - 100800, 0, 110600)
  - headroom_under_cap: de_minimis_cap - foreign_tax
  - election_credit: min(foreign_tax, regular_tax)
  - limit: regular_tax * foreign_passive_taxable / worldwide_taxable
  - form_1116_credit: min(foreign_tax + carryover, limit)
  - extra_credit: form_1116_credit - election_credit
  - carry_forward: foreign_tax + carryover - form_1116_credit
expected:
  regular_tax: 15824.00
  headroom_under_cap: 20.00
  election_credit: 580.00
  limit: 1054.93
  form_1116_credit: 1054.93
  extra_credit: 474.93
  carry_forward: 725.07
```

**Case 3, exclusion plus credit, by narrative.** A single filer abroad all year has foreign wages of USD 180,000, no housing amounts and no deductible expenses, foreign tax of USD 54,000, and excludes USD 132,900. Tax allocable to excluded income: USD 54,000 x 132,900 / 180,000 = USD 39,870, removed on line 12. Tax still available: USD 14,130. Wages left in income: USD 47,100, general category; line 1a shows USD 47,100 while lines 3d and 3e include the full USD 180,000. The election is not available. The comparison with the credit alone is Case 1 of `us-foreign-earned-income-2555`.

**Case 4, currency, by narrative.** A cash-basis client had euro tax withheld from each monthly salary payment. Convert each withholding at the rate for its date. The yearly average rate is only for accrual-basis taxes paid within the time limits; to use it the client checks "Accrued" on a timely original return, which then binds all later years.

**Case 5, a DST and a disputed tax, by narrative.** A freelancer paid a foreign digital services tax and is contesting a foreign income tax assessment. The DST is not creditable. The contested tax cannot be credited until the contest ends, unless the client elects a provisional credit on Form 7204 and files Schedule C (Form 1116) each year until it is resolved.

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-FTC-1 | Corporations, estates and trusts, or nonresident aliens | Refer: this skill is for individual US citizens and residents |
| R-FTC-2 | Section 962 elections, Form 1118, CFC look-through income, previously taxed earnings accounts, or Forms 5471, 8865, 8858 or 8621 | Refer: `us-cfc-gilti`, `us-form-5471-cfc-information` |
| R-FTC-3 | Treaty re-sourcing (box f), treaty-based credits needing Form 8833, or the additional credit for US citizens resident in treaty countries | Refer |
| R-FTC-4 | Section 901(m) covered asset acquisitions, foreign tax credit splitting events, foreign oil and gas income | Refer |
| R-FTC-5 | Recapture of overall foreign loss, separate limitation loss or overall domestic loss accounts beyond a single simple year | Refer |
| R-FTC-6 | A material withholding tax on services or royalties whose creditability depends on the Notice relief analysis | Refer |
| R-FTC-7 | Contested foreign taxes and the provisional-credit election (Form 7204) | Refer |
| R-FTC-8 | State returns | Do not assume any state gives a credit for foreign tax; use that state's skill |
| R-FTC-9 | A figure the 2026 instructions have not yet published | Give the 2025 figure, labelled as 2025, and say it must be checked |

## Filing and payment

Sources: [Instructions for Form 1116 (2025)](https://www.irs.gov/pub/irs-pdf/i1116.pdf); [IRS Pub. 514 (2025)](https://www.irs.gov/pub/irs-pdf/p514.pdf); [Instructions for Form 2555 (2026), When To File](https://www.irs.gov/pub/irs-pdf/i2555.pdf).

1. **Attachments:** each Form 1116, plus Schedule B and Schedule C where required, attached to Form 1040. The credit goes on Schedule 3 (Form 1040), line 1.
2. **Due date:** 15 April 2027 for a 2026 calendar-year return. Form 4868 extends the time **to file** to 15 October 2027, not the time to pay.
3. **People abroad:** citizens and residents who live outside the US and Puerto Rico with their tax home outside them on the due date get an automatic 2-month extension to 15 June 2027 to file and pay; interest still runs from 15 April. Details in `us-foreign-earned-income-2555`.
4. **Foreign tax redeterminations** (a foreign refund, extra foreign tax, accrued tax not paid within 24 months, a change from credit to deduction): if US tax changes, file an amended return with a revised Form 1116 and a statement, and file **Schedule C (Form 1116)** with the current-year return for each category; if US tax does not change, Schedule C with the original return is enough.
5. **Penalty for not notifying:** without reasonable cause, 5% of the resulting tax due for each month or part of a month, up to 25%. The IRS can also assess the extra tax outside the normal limitation period.
6. **Carryback:** Form 1040-X for 2025 with a revised 2025 Form 1116.

### 2025 returns still being filed on extension

Where 2025 differs from the 2026 text above: the foreign earned income exclusion limit is USD 130,000 (see `us-foreign-earned-income-2555`); the adjustment exception thresholds are USD 197,300 and USD 394,600 as in the rates table; Part IV must be completed even with one Form 1116 (new for 2025); for section 951A category income with a section 962 election the section 250 deduction was 50% and the section 960(d) credit 80%, with the 10% disallowance already applying to amounts after 28 June 2025; the section 901(j) list is Iran, Libya (waiver), North Korea, Sudan and Syria; and the Notice 2023-55 and 2023-80 relief applies.

## Completion checklist

- [ ] Every foreign tax is legally owed, not refundable, not offset by a subsidy; holding periods met.
- [ ] Notice 2023-55 and 2023-80 relief still in force for the year (IRS.gov/Form1116 checked); no DST claimed; reliance for any withholding tax documented.
- [ ] Credit or deduction consistent for all taxes of the year; any change within the 10-year (credit) or 3-year or 2-year (deduction) window.
- [ ] No-Form-1116 election tested against every condition, and its carryover and AMT costs weighed.
- [ ] One Form 1116 per category, right box; sanctioned-country income on its own form, per country.
- [ ] Income sourced correctly; wages split on a time basis.
- [ ] Deductions allocated; line 18 senior-deduction add-back; qualified dividend and capital gain adjustment or the exception.
- [ ] Currency at the right rate: date paid for cash basis, average rate for accrual within the limits; "Accrued" box history checked.
- [ ] Line 12 Form 2555 reduction and the high-tax reclassification (income in Part I, tax on line 13) done.
- [ ] Part IV completed; credit on Schedule 3, line 1.
- [ ] Schedule B attached where there is a carryover; the 1-year carryback claimed on Form 1040-X where useful.
- [ ] AMT Form 1116 done if AMT applies.
- [ ] Schedule C and amended returns filed for any foreign tax change.
- [ ] Items to refer out flagged to the client in writing.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Instructions for Form 1116 (2025). Read for the no-Form-1116 election, Foreign Taxes Not Eligible, sourcing, categories a to g, lines 3d to 4b (USD 5,000), the adjustment exception (USD 197,300, USD 394,600, USD 20,000), line 12, line 10 carryovers, Part III, Part IV and the Notice relief "until further notice". | https://www.irs.gov/pub/irs-pdf/i1116.pdf | 2026-11-13 |
| Form 1116 (2025). Read for the category boxes and Parts I to IV. | https://www.irs.gov/pub/irs-pdf/f1116.pdf | 2026-11-13 |
| IRS Pub. 514 (for 2025 returns). Read for Choosing To Take Credit or Deduction (10-year, 3-year and 2-year windows), the holding period (16 days), section 901(j) countries, Form 7204, and the redetermination penalty (5%, 25%). | https://www.irs.gov/pub/irs-pdf/p514.pdf | 2026-11-13 |
| Instructions for Form 6251 (2025). Read for line 8, the AMT Form 1116 steps, the simplified limitation election and AMTFTC carrybacks. | https://www.irs.gov/pub/irs-pdf/i6251.pdf | 2026-11-13 |
| Notice 2023-55. Read for the temporary relief and the DST statement. | https://www.irs.gov/pub/irs-drop/n-23-55.pdf | 2026-11-13 |
| Notice 2023-80. Read for the extension of the relief until withdrawn or modified. | https://www.irs.gov/pub/irs-drop/n-23-80.pdf | 2026-11-13 |
| 26 U.S.C. 904 (govinfo, 2024 edition). Read for (a), (c) (1 year back, 10 forward), (d) and (j) (USD 300, USD 600). | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partIII-subpartA-sec904.htm | 2026-11-13 |
| 26 U.S.C. 911 (govinfo). Read for (d)(6), no credit on excluded income. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partIII-subpartB-sec911.htm | 2026-11-13 |
| Public Law 119-21 (govinfo). Read for sections 70103 (USD 6,000 senior deduction), 70311 (new section 904(b)(5), from 2026), 70312 (90% deemed-paid credit, 10% disallowance after 28 June 2025) and 70321 (40% section 250 deduction). | https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm | 2026-11-13 |
| Instructions for Form 2555 (2026). Read for When To File (15 June 2027 extension). | https://www.irs.gov/pub/irs-pdf/i2555.pdf | 2026-11-13 |

Not yet confirmed: the 2026 Form 1116, its instructions, the 2026 Pub. 514 and the 2026 Instructions for Form 6251 were not yet published, so the line numbers above are from the 2025 editions and the 2026 adjustment exception thresholds and the 2026 section 901(j) list are not given; whether any notice has withdrawn or modified Notice 2023-80 after the 2025 instructions was not checked in the Internal Revenue Bulletin; the amount of the penalty for failing to file Form 8833 was not confirmed on an IRS page read for this rewrite, so it is not stated.
