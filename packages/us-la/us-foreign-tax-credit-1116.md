---
name: us-foreign-tax-credit-1116
description: Tier 2 US federal content skill for §901 Foreign Tax Credit (Form 1116) covering tax year 2025. Includes the basket separation under §904 (passive, general, GILTI, foreign branch, §901(j) sanctioned countries), the §904(a) limitation formula, the $300/$600 de minimis no-Form-1116 election, §904(j) high-tax kick-out for passive income, the 2022 T.D. 9959 attribution/nexus/cost-recovery requirements with Notice 2023-55/2024-44 (and successor) relief, the FEIE-vs-FTC strategic choice for US expats, 1-year back / 10-year forward credit carries, and the AMT FTC computation. Schedule A itemized deduction alternative when credit isn't useful.
jurisdiction: US
tax_year: 2026
last_updated: 2026-09-25
authored_by: OpenAccountants team
review_status: pending_review
trust_label: By OpenAccountants
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# US Foreign Tax Credit (Form 1116) for individuals

This Guide is written for **tax year 2026** (returns filed in 2027). A short dated section near the end covers **2025 returns**, which are still being filed on extension until 15 October 2026. The 2026 Form 1116 and its instructions were not yet published when this was written (25 September 2026). Where this Guide describes form lines, it uses the 2025 form, so check the line numbers against the 2026 instructions before filing.

## Scope and who this is for

It covers a US citizen or resident alien who files Form 1040 and paid or accrued foreign income tax on foreign-source income. It explains how to:

- choose between the credit and the itemized deduction
- sort income into the separate categories ("baskets")
- work out the limit on each Form 1116
- use the no-Form-1116 election
- carry excess credit back and forward
- deal with the foreign earned income exclusion (FEIE)
- apply the AMT credit, currency conversion and later changes in the foreign tax (Schedules B and C)

It does **not** cover corporations, estates and trusts, nonresident aliens, the §962 computation itself (Form 1118), or state returns. See "When to refuse or refer".

## Ask the client first

- Which countries taxed you, on what income, and in which currency? Get the foreign return or assessment, payslips, or the Form 1099-DIV / 1099-INT / Schedule K-1 / K-3 that shows the tax.
- Was the tax **legally owed**, or could part of it be refunded (for example, the treaty rate is lower than the rate withheld)?
- Is any foreign tax still under dispute with the foreign authority, or has any been refunded or changed since an earlier US return?
- Have you ever **deducted** foreign taxes on Schedule A instead of crediting them, and for which years?
- Do you have a foreign tax credit carryover from earlier years? Bring last year's Schedule B (Form 1116).
- Have you ever checked the "Accrued" box in Part II of Form 1116?
- Are you claiming, or have you ever claimed or revoked, the foreign earned income exclusion (Form 2555)?
- Did you hold the foreign shares for long enough around each dividend date? (See the holding-period rule below.)
- Are you a US shareholder of a controlled foreign corporation (CFC), a partner in a partnership with foreign activity, or someone who has made a §962 election?
- Did any income come from Iran, North Korea, Sudan, Syria, or another country on the §901(j) list?
- Are you subject to alternative minimum tax (AMT)?

## The method, step by step

1. **Confirm the tax can be credited.** It must be a foreign income tax (or a tax in place of one) that you legally owe and actually paid or accrued. Taxes you could get refunded, taxes offset by a subsidy, and interest or penalties do not count ([Form 1116 instructions](https://www.irs.gov/instructions/i1116), "Foreign Taxes Not Eligible for a Credit"). See the creditability section below for the 2022 regulations and the Notice relief.
2. **Choose credit or deduction for the year.** The choice covers all qualifying foreign income taxes of the year ([Pub. 514](https://www.irs.gov/publications/p514)).
3. **Test the no-Form-1116 election.** If every condition is met, claim the credit on Schedule 3 (Form 1040), line 1, and stop.
4. **Source the income and sort it into categories.** Use one Form 1116 per category.
5. **Allocate deductions and apply the qualified dividend and capital gain adjustment** in Part I.
6. **Enter the foreign taxes in Part II** on the right basis (paid or accrued), converted to dollars at the right exchange rate. Then make the line 12 reductions, such as tax on income excluded on Form 2555.
7. **Work out the limit in Part III.** The credit on line 24 is the smaller of the foreign tax available (line 14) and the limit on line 23. Line 23 is the US tax multiplied by the foreign share of taxable income (line 21), plus any §960(c) increase (line 22).
8. **Summarise in Part IV.** This is required even when you file only one Form 1116. The credit goes to Schedule 3 (Form 1040), line 1. Attach Schedule B if any carryover is used or created.
9. **Repeat for AMT** if Form 6251 applies.
10. **File, and record later changes.** Report foreign refunds and adjustments on Schedule C (Form 1116) and, where US tax changes, on an amended return.

## Step 2: credit or deduction ([Pub. 514](https://www.irs.gov/publications/p514))

- The credit reduces US tax dollar for dollar. You can take it and still claim the standard deduction. Only the credit can be carried back or forward. The IRS says the credit is better in most cases, but tells you to work out both.
- In a given year you must either credit **all** qualifying foreign income taxes or deduct **all** of them. You cannot carry a credit into a year in which you deducted.
- **Time to change the choice:**
  - You can switch **to the credit** within 10 years from the regular due date (without extensions) of the return for the year the taxes were paid or accrued.
  - You can switch **to the deduction** within 3 years from filing, or 2 years from paying the tax, whichever is later ([Pub. 514](https://www.irs.gov/publications/p514), "Making or Changing Your Choice").
  - For 2026 foreign taxes, the credit window runs 10 years from 15 April 2027.
- **Refund claims:** a refund claim caused by foreign tax you paid or accrued has a 10-year limitation period. It runs from the date the return was due for the year the taxes were actually paid or accrued ([26 U.S.C. §6511(d)(3)(A)](https://www.law.cornell.edu/uscode/text/26/6511)).

## Step 3: the no-Form-1116 election ([§904(j)](https://www.law.cornell.edu/uscode/text/26/904); [Form 1116 instructions](https://www.irs.gov/instructions/i1116))

You may claim the credit without Form 1116 only if **all** of these are true for the year:

1. **All** your foreign-source gross income is passive category income. For this test, high-taxed income and export financing interest still count as passive.
2. **All** that income, and the foreign tax on it, was reported to you on a qualified payee statement, such as:
   - Form 1099-DIV or 1099-INT
   - Schedule K-1 (Form 1041)
   - Schedule K-3 (Form 1065 or 1120-S)
   - a similar substitute statement
3. Total creditable foreign taxes are **not more than $300**, or **not more than $600** on a married-filing-jointly return. The tax is counted only if it appears on a payee statement.
4. You are an individual. Estates and trusts cannot make this election.
5. You elect it by entering the smaller of total foreign tax or regular tax on Schedule 3 (Form 1040), line 1.

**What the election costs:**

- The §904 limitation does not apply for the year.
- **No carryover** is possible to or from an election year. Foreign taxes of that year cannot be carried anywhere. Carryovers from other years cannot be used in it, and their carry period is not extended.
- For AMT, the credit equals the regular credit, and **no AMT carryback or carryforward** is allowed to or from that year ([Form 6251 instructions](https://www.irs.gov/instructions/i6251)).
- You still apply the normal creditability rules, including the holding period, and the line 12 reductions.

**Traps:**

- Any foreign-source wages, self-employment income or business income that stays in gross income blocks the election. This is true even if no foreign tax was paid on it.
- This includes wages above the FEIE limit.
- A client with carryovers may do better filing Form 1116 even when the election is available.

## Step 4: sourcing and the separate categories ([Form 1116 instructions](https://www.irs.gov/instructions/i1116); [§904(d)](https://www.law.cornell.edu/uscode/text/26/904))

**Sourcing basics** (Form 1116 instructions, "Income From Sources Outside the United States"):

- Pay for services performed abroad is foreign-source. An employee's pay (other than fringe benefits) for work both in and outside the US is split on a time basis.
- Dividends from a corporation incorporated abroad and interest from a payer located abroad are foreign-source.
- Gain on selling personal property by a US resident is generally not foreign-source. One exception applies to nondepreciable personal property sold while you have a tax home abroad: the gain is foreign-source if you paid foreign tax of at least 10% of the gain.

Use a separate Form 1116 for each category. On the 2025 form the boxes are:

| Box | Category | Typical individual items |
| --- | --- | --- |
| a | Section 951A category income | A US shareholder's CFC inclusion under §951A. From 2026 the statute calls this inclusion "net CFC tested income" (previously GILTI). No carryback or carryover. |
| b | Foreign branch category income | Business profits of a qualified business unit (QBU) in a foreign country |
| c | Passive category income | Dividends, interest, royalties, rents, annuities, investment gains. This excludes high-taxed income and export financing interest. |
| d | General category income | Wages, self-employment and active business income, and anything not in another category |
| e | Section 901(j) income | Income from a sanctioned country. Use one Form 1116 per country. |
| f | Certain income re-sourced by treaty | US-source income treated as foreign-source under a treaty. Use one Form 1116 per treaty country. |
| g | Lump-sum distributions | Foreign tax on a qualifying lump-sum distribution |

- **High-taxed income moves out of passive.** Passive income is "high-taxed" if the foreign tax on it, after expenses, exceeds the highest US tax that can be imposed on it. This is a classification rule, not an election.
  - Report the income as a negative amount on the passive Form 1116 and a positive amount on the other category's form.
  - Move the related tax on line 13 in the same way.
- **Look-through:** dividends, interest, rents or royalties from a CFC in which you own 10% or more of the vote or value may not be passive. Refer out.
- **§901(j) countries:** Pub. 514 lists Iran, Libya, North Korea, Sudan and Syria for 2025. A waiver has applied to Libya since 10 December 2004.
  - Taxes paid **to** a sanctioned country are not creditable. Tax paid to a non-sanctioned residence country on that income can be.
  - The 2026 list will be in the 2026 Pub. 514. Check it, and do not assume the 2025 list carries over.

## Creditability: the 2022 regulations and the Notice relief ([Notice 2023-55](https://www.irs.gov/pub/irs-drop/n-23-55.pdf); [Notice 2023-80](https://www.irs.gov/pub/irs-drop/n-23-80.pdf))

- **The 2022 regulations.** T.D. 9959 (published 4 January 2022, with correcting amendments on 27 July 2022) rewrote the rules in Reg. §1.901-2 and §1.903-1 on what counts as a creditable "foreign income tax". They added a net gain requirement and attribution requirements.
- **The relief.** Notice 2023-55 lets taxpayers decide creditability under the pre-2022 rules instead: former Reg. §1.901-2(a) and (b), as revised on 1 April 2021 and modified by the Notice. It also lets them apply §1.903-1 without the jurisdiction-to-tax and source-based attribution requirements.
  - Notice 2023-80 extended the relief to tax years ending before a notice or other guidance withdrawing or modifying it is issued.
  - The 2025 Form 1116 instructions still describe the relief as extended "until further notice".
- **Conditions of the relief:**
  - Apply it to **all** foreign taxes you paid in the relief year. Also apply it to all taxes paid by others that you could claim, such as taxes of a CFC in which you are a US shareholder.
  - You cannot use it to credit any tax for which a deduction is allowed in that year or any other year.
- **Digital services taxes stay non-creditable even under the relief.** Notice 2023-55 states that a gross-basis DST does not meet the net income requirement and does not qualify as a tax in lieu of an income tax. Do not claim a DST on Form 1116.
- **Gross withholding taxes on services or royalties** from a country that sources income by where the payer is: under the relief, test them as in-lieu-of taxes under §1.903-1. Document the analysis in the workpapers. Where the answer is not clear and the amount matters, refer.
- **Treaty-based credit.** If you rely on a treaty to credit a tax the Code does not allow, disclose it on Form 8833. Failing to disclose can bring a $1,000 penalty ([Pub. 514](https://www.irs.gov/publications/p514), "Tax Treaties").
- **Before filing a 2026 return, check** IRS.gov/Form1116 and the Internal Revenue Bulletin for any notice that withdraws or modifies Notice 2023-80. If one has been issued, apply its effective date.

## Holding period for dividends and other income ([Form 1116 instructions](https://www.irs.gov/instructions/i1116))

- Foreign tax withheld on a **dividend** is not creditable unless you held the stock for at least 16 days within the 31-day period that begins 15 days before the ex-dividend date. A longer period applies to some preferred-stock dividends.
- A similar 16-day rule applies to other income or gain from property.
- Tax is also not creditable to the extent you must make related payments on substantially similar or related positions.
- Tax that fails these tests may be **deducted** even in a year you take the credit.

## Step 5: Part I and the limitation formula ([Form 1116 instructions](https://www.irs.gov/instructions/i1116))

**The formula:** the limit for each category is US tax × (foreign-source taxable income in the category ÷ total taxable income) ([§904(a)](https://www.law.cornell.edu/uscode/text/26/904)). On the form:

- Line 17 is foreign-source taxable income, after the line 16 adjustments.
- Line 18 is worldwide taxable income.
- Line 19 is line 17 ÷ line 18. If line 17 is more than line 18, enter 1.
- Line 20 is regular tax liability. For 2025 that is Form 1040, line 16, plus Schedule 2, Part I, line 1z, less any Form 4972 tax. It does **not** include the §1411 net investment income tax, and the Form 1116 credit does not reduce that tax.
- Line 21 is line 20 × line 19.

**Deductions:**

- Put deductions **definitely related** to the foreign income (for example, Schedule C expenses of the foreign work) on line 2.
- Apportion the standard deduction or other itemized deductions on lines 3a to 3g.
- Home mortgage interest goes on line 4a, other interest on line 4b, and losses on line 5.
- Partnerships and S corporations report their own foreign allocations on Schedule K-3.

**Senior deduction:** the §151(d)(5)(C) deduction of $6,000 for each person aged 65 or over, reported on Schedule 1-A, line 37, applies for 2025 through 2028. For the limitation, it must be **added back** to taxable income on line 18, as the line 3b and line 18 instructions describe.

**Qualified dividends and capital gains:** foreign-source qualified dividends and capital gains taxed at preferential rates must usually be scaled down (the Worksheet for Line 18 and Worksheets A and B). You can skip this under the **adjustment exception** only if both of these are true:

- line 5 of the Qualified Dividends and Capital Gain Tax Worksheet is not more than the threshold for the year (2025 thresholds are below)
- foreign-source net capital gain plus foreign-source qualified dividends is **less than $20,000**

The 2026 thresholds will be in the 2026 instructions.

**Line 16 adjustments** are made in the order the instructions set out: the §461(l) loss, foreign losses, US losses, and recapture of overall foreign loss, separate limitation loss and overall domestic loss accounts. If line 15 is zero or a loss there is generally no credit for that category, but you still complete line 16.

**New from 2026 for Section 951A category income (net CFC tested income):** only the §250 deduction and deductions directly allocable to this income are allocated to it. No interest expense or research costs are allocated to it ([§904(b)(5)](https://www.law.cornell.edu/uscode/text/26/904), for tax years beginning after 31 December 2025).

## Step 6: Part II, cash or accrual, and currency ([Form 1116 instructions](https://www.irs.gov/instructions/i1116); [Pub. 514](https://www.irs.gov/publications/p514))

**Cash basis (the default for most individuals):**

- You claim the credit in the year you **pay** the tax.
- Convert at the exchange rate **on the date paid**. For withheld tax, use the rate on the date it was withheld. For foreign estimated payments, use the date of each payment.
- Do **not** use the yearly average rate on a cash basis.

**Electing accrual:**

- A cash-basis individual can choose to credit taxes in the year they accrue by checking the "Accrued" box in Part II on a **timely filed original return**. You cannot make this choice on an amended return.
- The choice binds all later years and covers all foreign taxes.
- Foreign taxes generally accrue on the last day of the foreign tax year.

**Accrual-basis conversion:**

- Accrued taxes use the **average exchange rate** for the tax year they relate to.
- That rule does not apply if the tax is paid before that year starts, more than 24 months after it ends, or in an inflationary currency. In those cases use the rate on the date paid.
- You can elect to use the date-paid rate for accrued taxes in a nonfunctional currency. The election is made by the due date, including extensions, and binds later years unless the IRS consents to revoke it.

**Other Part II rules:**

- Tax already shown in dollars on a Form 1099 needs no conversion. Enter "1099 taxes".
- **Accrued but unpaid tax** must be paid within 24 months after the year it relates to. If it is not, reduce the credit until it is paid.
- **Line 12 reductions** include tax allocable to income excluded on Form 2555 (see below), and tax connected with a foreign tax credit splitting event.

## Steps 7 and 8: Part III, Part IV and carryovers ([§904(c)](https://www.law.cornell.edu/uscode/text/26/904); [Form 1116 instructions](https://www.irs.gov/instructions/i1116); [Schedule B instructions](https://www.irs.gov/instructions/i1116sb))

- **Line 24** is the smaller of the foreign tax available (line 14) and the limit (line 23).
- **Part IV:** lines 25 to 32 must be completed even when you file only one Form 1116. Line 33 is the smaller of line 20 or line 32. The credit then goes to Schedule 3 (Form 1040), line 1.
- **Excess foreign tax** in a category is carried **back 1 year**, then **forward 10 years**, in that order, and stays in the same category.
  - The carryback is claimed on Form 1040-X with a revised Form 1116 for the earlier year.
  - The period is not extended because a year could not absorb the carryover.
  - Current-year taxes are used first, then the oldest carryover.
- **No carryback or carryover** is allowed for Section 951A category income. Leave line 10 blank on that form.
- You cannot carry a credit into a year in which you **deducted** foreign taxes. You also reduce the carryover by the amount that year could have used.
- **Schedule B (Form 1116)** reconciles the carryover from year to year. Attach one for each category whenever line 10 shows a carryover from a prior year or the current year creates one.

## Step 9: AMT foreign tax credit ([Form 6251 instructions](https://www.irs.gov/instructions/i6251); [§59(a)](https://www.law.cornell.edu/uscode/text/26/59))

- Work out the AMT foreign tax credit on Form 6251, line 8. You need it when line 10 of Form 6251 (regular tax after the regular credit) is less than line 7.
- Prepare a separate AMT Form 1116 for each category. Write "AMT" and the category in the top margin.
  - Use AMT income and deductions.
  - Test for high-taxed income using the **AMT rate**, not the regular rate.
- The **simplified limitation election** uses regular-tax foreign-source income in the AMT limitation. It can be made only for the first year after 1997 in which you claim an AMT credit. It binds later years unless the IRS consents to revoke it.
- Unused AMT credit is carried back and forward under §904(c), tracked separately from the regular carryover. There is none in a year the no-Form-1116 election applies.

## FEIE and the credit ([§911](https://www.law.cornell.edu/uscode/text/26/911); [Rev. Proc. 2025-32](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf); [Form 1116 instructions](https://www.irs.gov/instructions/i1116))

- The 2026 FEIE limit is **$132,900** per qualifying person.
- **No double benefit:**
  - No credit is allowed for foreign tax allocable to excluded income (§911(d)(6)).
  - On line 12, reduce foreign tax on foreign earned income by the fraction: (excluded earned income and housing amounts, minus deductible expenses allocable to them) ÷ (total foreign earned income, minus deductible expenses allocable to it, including the housing deduction).
  - If the foreign tax also covers other income and cannot be separated, the denominator is all income subject to that foreign tax.
- Income above the exclusion stays in gross income. It is general category income on Form 1116, and it blocks the no-Form-1116 election.
- **Stacking:** if you exclude income, tax on the rest is figured at the rates that would apply without the exclusion (§911(f)).
- **Revoking the FEIE:** the election continues until revoked. After revoking, you cannot elect again before the 6th tax year after the year of revocation without IRS consent (§911(e)).
  - Weigh this before claiming the FEIE in a year you may later want the credit instead.
- **Rule of thumb, which must be tested for each client:**
  - Where there is no foreign income tax, only the FEIE helps.
  - Where the foreign tax on earned income is higher than the US tax on it, the credit alone often removes US tax on that income and creates a carryover.
  - In other cases, work out the credit alone, the FEIE alone, and the FEIE with the credit on the remainder, and document the choice.

## Section 951A category (NCTI, formerly GILTI) for individuals ([§951A](https://www.law.cornell.edu/uscode/text/26/951A); [§960](https://www.law.cornell.edu/uscode/text/26/960); [§250](https://www.law.cornell.edu/uscode/text/26/250))

- For tax years beginning after 31 December 2025, §951A requires a US shareholder of a CFC to include **net CFC tested income**, the renamed GILTI.
- **Without a §962 election**, an individual gets no deemed-paid credit for the CFC's foreign taxes. The §960(d) deemed-paid credit and the §250 deduction apply to domestic corporations.
- **With a §962 election**, you claim the credit on **Form 1118**, not Form 1116. For tax years beginning after 31 December 2025:
  - the §250 deduction for the net CFC tested income amount is **40%**
  - the §960(d) deemed-paid credit is **90%** of the inclusion percentage × tested foreign income taxes
- **Previously taxed earnings:** §960(d)(4) disallows the credit for **10%** of foreign taxes on a distribution that is excluded under §959(a) because of an earlier §951A inclusion. The 2025 Form 1116 instructions say it applies to such amounts "after June 28, 2025"; check the exact scope for the client's facts.
  - Withholding tax on such a distribution otherwise goes on Form 1116, whether or not you made a §962 election.
- This Guide only flags these items. See "When to refuse or refer".

## Boundaries and exceptions

| Situation | Rule | Source |
| --- | --- | --- |
| Tax exactly $300 (not a joint return), all passive, all on Forms 1099 | Election available ("not more than") | [Form 1116 instructions](https://www.irs.gov/instructions/i1116) |
| Tax one dollar over the cap, or any non-passive foreign income | Election not available; file Form 1116 | [§904(j)](https://www.law.cornell.edu/uscode/text/26/904) |
| Foreign qualified dividends plus net capital gain of exactly $20,000 | Adjustment exception fails (needs "less than") | [Form 1116 instructions](https://www.irs.gov/instructions/i1116) |
| Tax withheld above the treaty rate | Only the treaty-rate amount is creditable, whether or not you claim the refund | [Form 1116 instructions](https://www.irs.gov/instructions/i1116) |
| Digital services tax | Not creditable, even under the Notice relief | [Notice 2023-55](https://www.irs.gov/pub/irs-drop/n-23-55.pdf) |
| Tax on FEIE-excluded wages | Not creditable; reduce on line 12 | [Form 1116 instructions](https://www.irs.gov/instructions/i1116) |
| Section 951A category excess | No carryback or carryover | [Form 1116 instructions](https://www.irs.gov/instructions/i1116) |
| Accrued tax unpaid 24 months after year end | Reduce credit until paid | [Form 1116 instructions](https://www.irs.gov/instructions/i1116) |
| "Accrued" box first checked on an amended return | Not allowed | [Form 1116 instructions](https://www.irs.gov/instructions/i1116) |
| Net investment income tax | Form 1116 credit does not reduce it (not regular tax liability) | [Form 1116 instructions](https://www.irs.gov/instructions/i1116) |

## Worked cases ([Form 1116 instructions](https://www.irs.gov/instructions/i1116))

All amounts are in dollars and are illustrations, not real clients.

**Case 1: ordinary general-category limit (2026).** A single filer is on the cash basis, with no carryovers.

- Foreign-source general-category taxable income (line 17) is $60,000.
- Worldwide taxable income (line 18) is $150,000.
- Regular tax (line 20) is $27,000.
- Foreign income tax withheld is $15,000, converted at the rates on the withholding dates.
- Limit: $27,000 × 60,000 ÷ 150,000 = $10,800.
- Credit: the smaller of $15,000 and $10,800, so $10,800.
- The excess of $4,200 is carried back to 2025 first, on Form 1040-X with a revised 2025 Form 1116. Any remainder carries forward up to 2036 in the general category. Attach Schedule B.

**Case 2: the no-Form-1116 boundary (2026).** A married couple filing jointly has only Form 1099-DIV income from foreign funds, with foreign tax of $600 shown on the forms. Every holding period is met.

- The election is available, because the cap is "not more than $600".
- Enter the smaller of $600 and regular tax on Schedule 3, line 1.
- There is no carryover to or from 2026, and no AMT carryover for 2026.
- Suppose one spouse also had foreign consulting fees, even with no foreign tax withheld. The election would then fail, because not all foreign-source income is passive. The couple would file separate Forms 1116 for passive and general income.

**Case 3: FEIE plus credit (2026).** A single filer abroad for the whole year has foreign wages of $180,000. There are no housing amounts and no deductible expenses. The foreign tax on the wages is $54,000, and the client excludes $132,900.

- Tax allocable to excluded income: $54,000 × 132,900 ÷ 180,000 = $39,870. Reduce this on line 12.
- Tax still available for credit: $54,000 − $39,870 = $14,130.
- Wages left in gross income: $180,000 − $132,900 = $47,100. This is general category.
- The no-Form-1116 election is not available.

**Case 4: currency (fix of the old guidance).** A cash-basis client had euro tax withheld from each monthly salary payment.

- Convert each withholding at the rate for its date.
- The yearly average rate is only for accrual-basis taxes paid within the time limits.
- If the client wants to use accrual and the average rate, check the "Accrued" box on the timely original return. The choice then binds all later years.

**Case 5: DST and a disputed tax.** A freelancer paid a foreign digital services tax and is contesting a foreign income tax assessment.

- The DST is not creditable.
- The contested income tax cannot be credited until the contest is resolved. The exception is an election for a provisional credit, which needs Form 7204 and then Schedule C (Form 1116) each year until the contest is resolved.

## When to refuse or refer

- Corporations, estates and trusts, and nonresident aliens. This Guide covers individual US citizens and residents only.
- §962 elections, Form 1118, CFC look-through income, previously taxed earnings accounts, and preparing Forms 5471, 8865, 8858 or 8621.
- Treaty re-sourcing (box f), treaty-based credits needing Form 8833, and the additional credit for US citizens resident in treaty countries.
- §901(m) covered asset acquisitions, foreign tax credit splitting events, and foreign oil and gas income.
- Recapture of overall foreign loss, separate limitation loss or overall domestic loss accounts, beyond a single simple year.
- A material withholding tax on services or royalties whose creditability depends on the Notice relief analysis.
- Contested foreign taxes and the provisional-credit election (Form 7204).
- State returns. Do not assume any state gives a credit for foreign tax. Check that state's own rules.
- Anyone asking for a figure the 2026 instructions have not yet published. Give the 2025 figure, labelled as 2025, and say it must be checked.

## Filing, payment and later changes ([extension of time to file](https://www.irs.gov/forms-pubs/extension-of-time-to-file-your-tax-return); [Pub. 54](https://www.irs.gov/publications/p54); [Schedule C instructions](https://www.irs.gov/instructions/i1116sc); [Pub. 514](https://www.irs.gov/publications/p514))

- **Attachments:** attach each Form 1116, plus Schedule B and Schedule C where required, to Form 1040. The credit goes on Schedule 3 (Form 1040), line 1.
- **2026 returns** are due 15 April 2027 for calendar-year filers ([§6072(a)](https://www.law.cornell.edu/uscode/text/26/6072)).
  - Form 4868 extends the time **to file** to 15 October. It does not extend the time to pay.
  - Citizens and residents living abroad whose main place of business or post of duty is outside the US get an automatic 2-month extension to file and pay. Interest still runs from the regular due date.
- **Foreign tax redeterminations** include a foreign refund, extra foreign tax, accrued tax not paid within 24 months, and a change of credit or deduction.
  - If US tax changes, file an amended return with a revised Form 1116 and a statement.
  - Also file **Schedule C (Form 1116)** with the current-year return for each category.
  - If US tax does not change, Schedule C with the original return is enough.
- **Penalty for not notifying:** failing to notify the IRS of a redetermination without reasonable cause costs 5% of the resulting tax due for each month or part of a month, up to 25%. The IRS can also assess the extra tax outside the normal limitation period.

## 2025 returns (extended returns due 15 October 2026) ([Form 1116 instructions](https://www.irs.gov/instructions/i1116); [Form 2555 instructions](https://www.irs.gov/instructions/i2555))

Where 2025 differs from the 2026 text above:

- **FEIE limit:** $130,000.
- **Adjustment exception thresholds** (line 5 of the Qualified Dividends and Capital Gain Tax Worksheet): $197,300 for single, head of household and married filing separately; $394,600 for married filing jointly and qualifying surviving spouse. The foreign gains and dividends must also be less than $20,000.
- **Line 18** adds back the $6,000 senior deduction from Schedule 1-A, line 37.
- **Part IV** lines 25 to 32 must be completed even with one Form 1116. This is new for 2025.
- **Section 951A category** (GILTI) for 2025 with a §962 election: §250 deduction of 50% ([§250](https://www.law.cornell.edu/uscode/text/26/250) amendment note) and deemed-paid credit of 80% ([§960](https://www.law.cornell.edu/uscode/text/26/960) amendment note). The 10% disallowance for tax on previously taxed distributions already applies to amounts after 28 June 2025.
- **§901(j) list for 2025:** Iran, Libya (waiver), North Korea, Sudan, Syria.
- **Notice 2023-55/2023-80 relief** applies to 2025.

## Completion checklist

- [ ] Every foreign tax is legally owed, not refundable, and not offset by a subsidy. The holding periods are met.
- [ ] The Notice 2023-55/2023-80 relief is still in force for the year (check IRS.gov/Form1116). No DST is claimed. Reliance for any withholding tax is documented.
- [ ] The credit or deduction choice is consistent for all taxes of the year. Any change is made within the 10-year (credit) or 3-year/2-year (deduction) window.
- [ ] The no-Form-1116 election has been tested against all of its conditions, and its carryover and AMT costs have been weighed.
- [ ] There is one Form 1116 per category, with the right box. Sanctioned-country income is on its own form, per country.
- [ ] Income is sourced correctly, with wages split on a time basis.
- [ ] Deductions are allocated. The line 18 senior-deduction add-back and the qualified dividend and capital gain adjustment (or the exception) are applied.
- [ ] Tax is converted at the correct rate: date paid for cash basis, average rate for accrual within the limits. The "Accrued" box history has been checked.
- [ ] The line 12 FEIE reduction and the high-tax adjustments (income in Part I, tax on line 13) are done.
- [ ] Part IV is completed, and the credit goes to Schedule 3, line 1.
- [ ] Schedule B is attached where there is a carryover. The 1-year carryback is claimed on Form 1040-X where useful.
- [ ] The AMT Form 1116 is done if AMT applies.
- [ ] Schedule C and amended returns are filed for any foreign tax change.
- [ ] Items to refer out have been flagged to the client in writing.

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
