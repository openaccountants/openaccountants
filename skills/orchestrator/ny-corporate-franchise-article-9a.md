---
name: ny-corporate-franchise-article-9a
description: Tier 2 content skill for New York State Corporate Franchise Tax under Tax Law Article 9-A. Covers C-corporations and S-corporations electing federal status (NY GBC), the three alternative tax bases (business income, capital, fixed dollar minimum), the 6.5% standard rate and the 7.25% rate on business income over $5M, single-sales-factor apportionment with market-based sourcing, MTA surcharge for MCTD activity, mandatory first installment (MFI) rules, and CT-3 / CT-3-A combined filing. Tax year 2025.
jurisdiction: US-NY
tax_year: 2026
last_updated: 2026-09-25
authored_by: OpenAccountants team
review_status: pending_review
trust_label: By OpenAccountants
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# New York corporation franchise tax (Article 9-A, Form CT-3)

## Scope and who this is for

This Guide covers the New York State franchise tax on general business corporations under Tax Law Article 9-A. That means C corporations, and federal S corporations that have not elected (and are not mandated) to be New York S corporations. It covers nexus (including P.L. 86-272), the three tax bases and rates, apportionment, NOLs and the PNOLC subtraction, combined reporting, the MTA surcharge, and payments, extensions and penalties.

Figures are for **tax year 2026** where published; the latest instructions are for 2025 ([CT-3-I (2025)](https://www.tax.ny.gov/pdf/current_forms/ct/ct3i.pdf)), so each figure carries its year. A dated section covers **2025 returns** (due 15 October 2026 on extension).

Banking corporations have been taxed under Article 9-A since the 2015 merger of the bank tax ([corporate tax reform](https://www.tax.ny.gov/bus/ct/corp_tax_reform.htm)). Not covered: New York S corporations (Form CT-3-S), insurance corporations (Article 33), Article 9 corporations, REITs and RICs, tax credits, and the pass-through entity tax.

- **New York City** business corporation tax is a separate tax and return, outside this Guide; an NYC corporation usually owes the state tax, the MTA surcharge and the city tax.

## Ask the client first

- Where is it incorporated, which federal return does it file, and has it made a New York S election (Form CT-6)?
- What does it have or do in New York (employees, office, property, inventory, partnership interests, sales)? Is its only activity soliciting orders for **tangible goods**?
- What are its New York and everywhere receipts by type (goods, services, digital products, rents, royalties, financial instruments), and where are its customers?
- Does it own **more than 50% of the voting stock** of another corporation, or is it owned more than 50% by one, or are both owned by the same interests? Are those corporations unitary with it? ([CT-3-A-I](https://www.tax.ny.gov/pdf/current_forms/ct/ct3ai.pdf))
- What are its federal taxable income, New York modifications, investment income, GILTI and Subpart F income, total capital, and stocks held for investment over a year?
- Does it qualify as a **qualified New York manufacturer**, a **qualified emerging technology company (QETC)** or a **small business taxpayer**?
- Does it have post-2014 NOLs or a PNOLC balance? Does it do business in the 12-county Metropolitan Commuter Transportation District (MCTD)?
- What was its franchise tax after credits in each of the last two years? Was its business income **$1 million or more** in any of the last three years? ([CT-400-I](https://www.tax.ny.gov/pdf/current_forms/ct/ct400i.pdf))

## The method, step by step

### Step 1: is the corporation taxable in New York? ([CT-3-I](https://www.tax.ny.gov/pdf/current_forms/ct/ct3i.pdf); [deriving receipts](https://www.tax.ny.gov/bus/ct/article9a_deriving_receipts.htm))

- A **domestic corporation** (one incorporated in New York) is taxable for each year until it is formally dissolved. There is an exception: a domestic corporation that no longer does business, employs capital, owns or leases property, or derives receipts from activity in New York, and meets § 209.8, is exempt from the fixed dollar minimum after its final tax year.
- A **foreign corporation** is taxable in any period in which it does business, employs capital, owns or leases property, maintains an office, or derives receipts from activity in New York State.
- **Economic nexus.** A corporation is deriving receipts if its New York receipts are **$1,283,000 or more** in the tax year. This threshold applies to tax years beginning on or after 1 January 2024 and before 1 January 2027. For earlier years it was $1,000,000 (2015 to 2021) and $1,138,000 (2022 and 2023). The Commissioner reviews it every year and adjusts it when the Consumer Price Index has changed by 10% or more. **For 2027, check the deriving receipts page.**
- **Unitary groups.** A group has nexus if the combined New York receipts of its members meet the threshold. Only members that are unitary, meet the § 210-C ownership test, and have at least **$12,000** of New York receipts (2024 to 2026) count toward it. Leave out any member excluded by § 210-C.2(c): Article 9 or 33 taxpayers, non-captive REITs and RICs, New York S corporations, and alien corporations with no effectively connected income. Once the group meets the threshold, every member at or above the $12,000 floor is taxable. A member protected by P.L. 86-272 may still be included in the combined report, and its receipts count toward the group threshold (20 NYCRR 1-2.10(h)).
- **Corporate partners.** A general partner is taxable if the partnership is doing business in New York; a limited partner (other than of a portfolio investment partnership) only if it takes part in or controls the business. Some corporate partners and LLC members add the partnership's New York receipts to their own for the nexus test.
- **Public Law 86-272.** A foreign corporation is exempt if its only New York activity is soliciting orders for **sales of tangible personal property**, and the orders are approved outside New York and filled by shipment from outside New York. Soliciting over the internet counts ([20 NYCRR 1-2.10](https://www.tax.ny.gov/pdf/rulemaking/dec1123/corpreform/text.pdf)). The protection:
  - does **not** cover services or intangibles
  - is lost by any activity beyond solicitation that is more than de minimis. This includes internet activity such as interacting with customers through the website or an app. Presenting static text or images on a website is not enough to lose it.
  - is lost by maintaining an office, a warehouse or a stock of goods in New York.
  - A corporation that relies on P.L. 86-272 but still files marks box C on page 1 of Form CT-3, completes the whole return, and enters 0 on Part 2, line 4. A corporation taxable **only** because it derives receipts, and not protected by P.L. 86-272, marks Part 1, Section B, line 6.

### Step 2: entire net income ([CT-3-I](https://www.tax.ny.gov/pdf/current_forms/ct/ct3i.pdf), Part 3; [Notice N-26-1](https://www.tax.ny.gov/forms/n-notices/n-26-1.htm))

- Start with **federal taxable income before NOL and special deductions** (Form 1120, line 28). A federal S corporation taxed as a New York C corporation uses a pro forma federal figure. A member of a federal consolidated group uses a pro forma separate return.
- Add and subtract the New York modifications on Form CT-225. This gives **entire net income (ENI)** (Part 3, line 7). Common items:
  - **Related-member royalty addback.** A corporation not in a combined return with the related member adds back royalties paid to it, unless one of the four exceptions applies.
  - **P.L. 119-21 decoupling.** From tax years beginning on or after 1 January 2025, New York does not follow the federal law on:
    - **§ 168(n) qualified production property.** Add back the federal deduction, and subtract depreciation computed as if the election had not been made. Compute this on Form CT-399 and report it with codes A-507 and S-507.
    - **§§ 174 and 174A research and experimental expenditures.** Add back the federal deduction (code A-225). Subtract amortization over 60 months for amounts paid or incurred on or after 1 January 2025 (S-221). For earlier amounts, subtract amortization under the rules in effect on 1 January 2022 (S-222).

### Step 3: business income ([CT-3.1-I](https://www.tax.ny.gov/pdf/current_forms/ct/ct3_1i.pdf))

**Business income = ENI − investment income − other exempt income**, plus any excess interest attributed to those items (Part 3, lines 8-11).

- **Investment capital** means stock in **non-unitary** corporations that:
  - is a capital asset under IRC § 1221 at all times the corporation owned it during the year
  - is held for investment for **more than one year**
  - would produce long-term capital gain or loss when disposed of
  - Investment capital also includes debt New York cannot constitutionally tax; only corporations domiciled outside New York can claim this.
  - For stock acquired on or after 1 January 2015, it must never have been held for sale to customers after the close of the day it was acquired, and it must be identified as held for investment, generally before the close of the day it was acquired.
  - Stock held at year end for under a year may be presumed to meet the holding period; if it then fails, the income and capital are added back (CT-3.1, Schedule F).
- **Investment income** is limited to the greater of **8% of ENI** or the income New York cannot constitutionally tax.
- **Other exempt income** is exempt CFC income plus exempt unitary corporation dividends. Both count only where the payer is **not** in the combined return.
  - Exempt CFC income is 95% of GILTI (before the § 250 deduction) plus Subpart F income from a unitary corporation.
  - **§ 78 gross-up is not exempt.**
- **Interest attribution.** You can make a revocable election to reduce gross investment income and gross other exempt income by **40%**, instead of tracing the interest deductions attributable to them. The election covers both types, and every member of a combined group.

### Step 4: the three bases ([CT-3-I](https://www.tax.ny.gov/pdf/current_forms/ct/ct3i.pdf), Tax rates schedule; [Form CT-3](https://www.tax.ny.gov/pdf/current_forms/ct/ct3.pdf))

Compute all three bases. The tax is the **largest** of them (for a combined group, see Step 7: other members' fixed dollar minimums are added on top).

1. **Business income base (Part 3).**
   - Business income after addback × business apportionment factor = apportioned business income (line 15).
   - Subtract the PNOLC subtraction (line 16) and then the NOL deduction (line 18). The result is the **business income base** (line 19).
   - Multiply the base by the rate for the taxpayer's type (see the figures table).
   - The **7.25%** rate applies when the **business income base itself** (line 19, which is after apportionment and NOLs) is **more than $5,000,000**. It then applies to the whole base, not only the part above $5 million.
2. **Capital base (Part 4).**
   - Business capital is all assets other than investment capital and the taxpayer's own stock, less liabilities not deducted from investment capital.
   - Value real property and marketable securities at fair market value, and other assets at book value. Use the average for the year, quarterly if your accounting allows it.
   - Apportion using the same factor.
   - Multiply by 0.1875% (2021-2029), or 0% for preferred taxpayers. The capital base tax is **capped at $5,000,000**.
   - REITs and RICs enter 0.
3. **Fixed dollar minimum (Part 2, line 1c).** Look up New York receipts (Part 6, line 57, column A) in the table below. For a short year, annualize the receipts. Then reduce the fixed dollar minimum by **50%** for a period of not more than six months, or **25%** for more than six but not more than nine months.

**Preferred taxpayers:**

- **Qualified New York manufacturer.** It gets a 0% business income rate and the lower fixed dollar minimum. It qualifies by either of two tests:
  - **Principally engaged test.** More than 50% of gross receipts come from selling goods it produces by manufacturing, processing, assembling, refining, mining, extracting, farming, agriculture, horticulture, floriculture, viticulture or commercial fishing. **And** either its New York property used in production has an adjusted basis of **at least $1 million** at the close of the year, **or** all its real and personal property is in New York. GILTI is disregarded for this test. Generating or distributing electricity, distributing natural gas, and producing steam associated with generating electricity do not count.
  - **Significant employment and property test.** At least 2,500 manufacturing employees in New York, and New York manufacturing property with an adjusted basis of at least $100 million.
  - The 0% capital base rate has its own box (CT-3, Part 1, line 3). Check that box's test separately.
- **QETC.** It gets a **4.875%** business income rate, a 0% capital base and the lower fixed dollar minimum. It must meet Public Authorities Law § 3102-e(1)(c) **without regard to the $10 million limitation** on product sales.
- **Small business taxpayer.** It gets a 0% capital base, and its business income rate is 6.5%. **All four** conditions must be met:
  1. ENI is **not more than $390,000**. Annualize for a short year.
  2. Money and property received for stock, as capital contributions and as paid-in surplus total **not more than $1 million** at the end of the year.
  3. An average of **100 or fewer** full-time employees in New York, not counting general executive officers. Average the headcount on 31 March, 30 June, 30 September and 31 December.
  4. The corporation is **not in an affiliated group** (IRC § 1504), unless the group itself would meet these tests on a combined basis.
- **Cooperative housing corporation.** 0% capital base.

### Step 5: apportionment, a single receipts factor ([CT-3-I](https://www.tax.ny.gov/pdf/current_forms/ct/ct3i.pdf), Part 6)

- **Business apportionment factor = New York receipts ÷ everywhere receipts.** There is no property or payroll factor for the state tax. If Part 6 is not completed properly, the Department may impose a 100% factor.
- **Tangible goods:** New York if shipped to, or the destination is, a point in the state.
- **Rents** of real and tangible personal property: New York if the property is located in the state. **Royalties** from patents, copyrights, trademarks and similar intangibles: New York to the extent the intangible is used in the state.
- **Digital products and services** (sales, rentals, licences, remote access): apply 20 NYCRR 4-3 **in this order**:
  1. special rules
  2. the business address presumption
  3. a hierarchy of methods that begins with the **primary use location**.
- **Other services:** apply 20 NYCRR 4-4 in the same order: special rules, then the business address presumption, then a hierarchy that begins **where the benefit is received**.
- **Financial instruments.** Use customer-based sourcing. An individual is located at the billing address. A business is located at its commercial domicile: the seat of management and control, or failing that the billing address. Alternatively, you can elect the **8% fixed percentage method** for qualified financial instruments. That election is made each year on the original, timely filed return and is irrevocable for the year.

### Step 6: PNOLC subtraction and NOL deduction ([CT-3.3-I](https://www.tax.ny.gov/pdf/current_forms/ct/ct3_3i.pdf); [Form CT-3.3](https://www.tax.ny.gov/pdf/current_forms/ct/ct3_3.pdf); [CT-3.4-I](https://www.tax.ny.gov/pdf/current_forms/ct/ct3_4i.pdf))

1. **PNOLC subtraction first.** This is the conversion of NOLs from before 2015.
   - Use the carried-forward balance on Form CT-3.3, Schedule C.
   - The subtraction cannot reduce the tax below the **higher of the capital base tax or the fixed dollar minimum**.
   - Unused amounts cannot be carried forward more than 20 tax years after 2015, or into any tax year beginning on or after **1 January 2036**, whichever comes first.
   - File Form CT-3.3 every year you carry a balance, even if you cannot use any of it.
2. **Then the NOL deduction.** An NOL here is the business loss **multiplied by that year's apportionment factor**. It covers only losses from years beginning on or after 1 January 2015, in which the corporation was subject to Article 9-A. Losses from New York S years are excluded.
   - **Carryback:** 3 years, applied to the earliest year first. Claim it on an amended return for each year it is carried to, within three years of the loss year's due date (including extensions), and attach Form CT-3.4.
   - **Election to waive the carryback:** the entire carryback period, made on the **original, timely filed return** for the loss year (including extensions). It is irrevocable for that year, and binds every member of a combined group.
   - **Carryforward:** up to 20 years, earliest loss first.
   - **Limit:** the NOL deduction cannot reduce the tax below the higher of the capital base tax or the fixed dollar minimum.
   - New York has **no 80%-of-income limit** like § 172. The NOL deduction is not limited to the amount federal law would allow.
   - For a combined group, the NOL deduction is computed as if the group were one corporation filing a federal consolidated return, subject to §§ 381-384 and the SRLY rules.
   - File Form CT-3.4 every year.

### Step 7: combined reporting ([CT-3-A-I](https://www.tax.ny.gov/pdf/current_forms/ct/ct3ai.pdf); [CT-3-A/BC-I](https://www.tax.ny.gov/pdf/current_forms/ct/ct3a_bci.pdf))

- **Mandatory combination.** Corporations must file one combined return (Form CT-3-A) if **both** of these hold:
  - There is **more than 50%** voting-power ownership: one owns the other, it is owned by the other, or both are owned by the same interests.
  - They are **engaged in a unitary business**.
  - A captive REIT or RIC and a combinable captive insurance company are included.
  - Excluded are Article 9 and 33 taxpayers, non-captive REITs and RICs, New York S corporations, and **alien corporations** with no effectively connected income.
- **Commonly owned group election.** This combines every corporation meeting the ownership test, unitary or not.
  - It is made on an original, timely filed return, including extensions.
  - It is **irrevocable** for that year and the next six (short years do not count), and it **renews automatically** for further seven-year periods.
  - It can be revoked only on the original, timely filed return for the first year after a seven-year period. After a revocation, no member may make a new election in the next three years.
- **Mechanics.**
  - The designated agent files Form CT-3-A. Every other member files Form CT-3-A/BC.
  - Intercompany transactions are eliminated.
  - **Combined tax** = the largest of the combined business income base tax, the combined capital base tax and the **designated agent's own** fixed dollar minimum (CT-3-A, Part 2, line 1c), **plus** the sum of every other taxable member's own fixed dollar minimum (line 4b), whichever base is largest. Each member's fixed dollar minimum uses its own New York receipts. Nontaxpayer members pay none. The designated agent must be a taxpayer.
  - A group gets the QETC rate only if **all** members are QETCs.

### Step 8: MTA surcharge ([CT-3-M-I](https://www.tax.ny.gov/pdf/current_forms/ct/ct3mi.pdf); [Form CT-3-M](https://www.tax.ny.gov/pdf/current_forms/ct/ct3m.pdf))

- **Who.** An Article 9-A taxpayer that does business, employs capital, owns or leases property, maintains an office, or derives receipts in the **MCTD**. The MCTD is New York, Bronx, Kings, Queens, Richmond, Dutchess, Nassau, Orange, Putnam, Rockland, Suffolk and Westchester counties.
  - MCTD economic nexus is **$1,283,000 or more** of MCTD receipts.
  - A unitary member with at least $12,000 of MCTD receipts counts toward the group total.
- **Tax base.** The franchise tax under § 209 **before credits** (CT-3, Part 2, line 2). On a combined return, add each member's fixed dollar minimum.
- **MCTD apportionment percentage.** Add three single-weighted factors (property, receipts and payroll: MCTD amounts over New York State amounts) and divide by three. A factor is missing, and you divide by the number present, **only if both** its MCTD numerator and its New York denominator are zero. A 0% factor still counts. Payroll excludes general executive officers.
  - The New York receipts numerator is the MCTD receipts denominator.
  - Property is at federal adjusted basis. You can make a one-time, revocable election to use fair market value. Rented property is valued at eight times the gross rent.
  - **Surcharge = tax × MCTD percentage × 30%.**
- The surcharge has its own estimated payments and MFI. Pay it with the franchise tax payments.

## Figures with years

| Item | 2025 | 2026 | Source |
|---|---|---|---|
| Economic nexus (New York or MCTD receipts) | $1,283,000 or more | $1,283,000 or more | [deriving receipts](https://www.tax.ny.gov/bus/ct/article9a_deriving_receipts.htm) |
| Unitary member receipts counted toward nexus | at least $12,000 | at least $12,000 | same |
| Business income rate, general | 6.5% | 6.5% | [CT-3-I](https://www.tax.ny.gov/pdf/current_forms/ct/ct3i.pdf); [rate history](https://www.tax.ny.gov/data/stats/ter/fiscal-year27/corporate-franchise-tax.htm) |
| Business income rate, base more than $5,000,000 | 7.25% | 7.25% (tax years 2021-2029; 6.5% from 2030) | Tax Law § 210.1(a); [Financial Plan](https://www.budget.ny.gov/pubs/archive/fy27/en/fy27fp-en.pdf) |
| Business income rate, QETC | 4.875% | 4.875% | CT-3-I |
| Business income rate, qualified NY manufacturer | 0% | 0% | CT-3-I |
| Capital base rate, general | 0.1875% | 0.1875% (tax years 2021-2029; 0% from 2030) | Tax Law § 210.1(b)(1); [rate history](https://www.tax.ny.gov/data/stats/ter/fiscal-year27/corporate-franchise-tax.htm) |
| Capital base rate, manufacturers, QETCs, co-ops, small business taxpayers | 0% | 0% | CT-3-I |
| Capital base tax cap | $5,000,000 | $5,000,000 | [Article 9-A definitions](https://www.tax.ny.gov/bus/ct/def_art9a.htm) |
| MTA surcharge rate | 30% | 30% | [Form CT-3-M](https://www.tax.ny.gov/pdf/current_forms/ct/ct3m.pdf); [tax facts](https://www.tax.ny.gov/data/stats/taxfacts/corporation-tax.htm) |
| MFI threshold (second preceding year's tax after credits) | more than $5,000 | more than $5,000 | [CT-300-I (2026)](https://www.tax.ny.gov/pdf/current_forms/ct/ct300i.pdf) |
| Large corporation (estimated tax) | business income of at least $1 million in any of the 3 preceding years | same | [CT-400-I (2026)](https://www.tax.ny.gov/pdf/current_forms/ct/ct400i.pdf) |

**2027 to 2029.** Tax Law § 210.1(a) and (b)(1), as amended by the FY 2027 enacted budget (revision dated 5 June 2026), sets the 7.25% rate and the 0.1875% capital base for tax years beginning before 1 January 2030, and a 0% capital base from 2030. Supporting documents: the Division of the Budget [Financial Plan](https://www.budget.ny.gov/pubs/archive/fy27/en/fy27fp-en.pdf) (rate extension enacted) and the [FY 2027 Executive Budget memorandum](https://www.budget.ny.gov/pubs/archive/fy27/ex/artvii/revenue-memo.pdf) (Part E, as proposed). Our fetcher could not capture the statute page on nysenate.gov, so read § 210 there before filing. For 2027, also check the 2027 instructions for any change to the fixed dollar minimum or the nexus threshold.

**Fixed dollar minimum, based on New York receipts** ([CT-3-I](https://www.tax.ny.gov/pdf/current_forms/ct/ct3i.pdf), 2025):

| New York receipts ([CT-3-I](https://www.tax.ny.gov/pdf/current_forms/ct/ct3i.pdf)) | General | Qualified NY manufacturer or QETC |
|---|---|---|
| Not more than $100,000 | $25 | $19 |
| More than $100,000, not over $250,000 | $75 | $56 |
| More than $250,000, not over $500,000 | $175 | $131 |
| More than $500,000, not over $1,000,000 | $500 | $375 |
| More than $1,000,000, not over $5,000,000 | $1,500 | $1,125 |
| More than $5,000,000, not over $25,000,000 | $3,500 | $2,625 |
| More than $25,000,000, not over $50,000,000 | $5,000 | $3,750 (for all receipts over $25,000,000) |
| More than $50,000,000, not over $100,000,000 | $10,000 | $3,750 |
| More than $100,000,000, not over $250,000,000 | $20,000 | $3,750 |
| More than $250,000,000, not over $500,000,000 | $50,000 | $3,750 |
| More than $500,000,000, not over $1,000,000,000 | $100,000 | $3,750 |
| Over $1,000,000,000 | $200,000 | $3,750 |

Non-captive REITs and RICs use a separate table that stops at $500 ([CT-3-I](https://www.tax.ny.gov/pdf/current_forms/ct/ct3i.pdf)). The 2026 table had not been published when this was written; the 2025 amounts are shown.

## Boundary and exception table

| Situation | Rule | Source |
|---|---|---|
| New York receipts exactly $1,283,000 (2026) | Taxable: the test is "or more" | [deriving receipts](https://www.tax.ny.gov/bus/ct/article9a_deriving_receipts.htm) |
| Business income base exactly $5,000,000 | 6.5%: 7.25% applies only if the base is **more than** $5,000,000 | [CT-3-I](https://www.tax.ny.gov/pdf/current_forms/ct/ct3i.pdf) |
| Business income over $5,000,000 before apportionment, base below it after | 6.5%: the test uses line 19 | [Form CT-3](https://www.tax.ny.gov/pdf/current_forms/ct/ct3.pdf) |
| Seller of goods whose only New York activity is soliciting orders, including static website content | Protected by P.L. 86-272; mark box C and enter 0 tax | [20 NYCRR 1-2.10](https://www.tax.ny.gov/pdf/rulemaking/dec1123/corpreform/text.pdf) |
| The same seller, with website chat support or post-sale technical advice | Not protected: interaction beyond static content, or advice after delivery, goes beyond solicitation | same |
| Services or SaaS seller with $1,283,000 or more of New York receipts | Taxable; P.L. 86-272 never covers services or intangibles | same |
| Second preceding year's tax exactly $5,000 | No MFI: it must **exceed** $5,000 | [CT-300-I](https://www.tax.ny.gov/pdf/current_forms/ct/ct300i.pdf) |
| Second preceding year's tax exactly $100,000 | 25% MFI; 40% only if it **exceeds** $100,000 | same |
| No second preceding year return | No MFI, but declare and pay the remaining installments on Form CT-400 | same |
| ENI $390,000 but $1,200,000 of paid-in capital | Not a small business taxpayer; capital base at 0.1875% | [CT-3-I](https://www.tax.ny.gov/pdf/current_forms/ct/ct3i.pdf) |
| QETC with product sales over $10 million | Still eligible for 4.875%: the $10 million limit is disregarded | same |
| Extension paid at 85% of the final tax, when the prior year's tax was higher | Extension invalid, so the late filing penalty runs from the original due date. Pay at least the prior year's tax (for a 12-month year), or 90% of the final tax | [CT-5-I](https://www.tax.ny.gov/pdf/current_forms/ct/ct5i.pdf) |
| Loss year, waiver election left off the original return | The carryback applies; the waiver cannot be made on an amended return | [CT-3.4-I](https://www.tax.ny.gov/pdf/current_forms/ct/ct3_4i.pdf) |
| Unitary sister corporation with $11,000 of New York receipts (2026) | Left out of the group's nexus total and not taxable on that basis | [deriving receipts](https://www.tax.ny.gov/bus/ct/article9a_deriving_receipts.htm) |

## Worked cases

All cases are for calendar 2026. Amounts are hypothetical, and rates are taken from the figures table.

### Case 1: a New York-only software company ([CT-3-I](https://www.tax.ny.gov/pdf/current_forms/ct/ct3i.pdf); [CT-300-I](https://www.tax.ny.gov/pdf/current_forms/ct/ct300i.pdf))

- Business income is $850,000 and the apportionment factor is 100%. There are no NOLs.
- **Business income base tax:** $850,000 × 6.5% = **$55,250**.
- **Capital base:** ENI is more than $390,000, so it is not a small business taxpayer. Business capital of $1,500,000 × 0.1875% = $2,812.50.
- **Fixed dollar minimum:** New York receipts are $4,200,000, so $1,500.
- **Tax** is the largest of the three: **$55,250**.
- **MTA surcharge:** all property, payroll and receipts are in Manhattan, so the MCTD percentage is 100%. $55,250 × 30% = **$16,575**. The state-level total is **$71,825**.
- **MFI:** the 2024 tax was $30,000, so the 2026 MFI was 25% of it, **$7,500**, due 16 March 2026. The MTA MFI was 25% of the 2024 surcharge.

### Case 2: an engineering firm near the $5 million line ([Form CT-3](https://www.tax.ny.gov/pdf/current_forms/ct/ct3.pdf); [CT-3-M-I](https://www.tax.ny.gov/pdf/current_forms/ct/ct3mi.pdf))

- Business income is $5,200,000 and the apportionment factor is 80%, so the business income base is **$4,160,000**. That is not more than $5,000,000, so the rate is 6.5%: **$270,400**.
  - If the factor had been 100%, the base would be $5,200,000 and the whole base would be taxed at 7.25%: $377,000.
- **Capital base:** $8,000,000 × 80% = $6,400,000 × 0.1875% = $12,000.
- **Fixed dollar minimum:** receipts are $24,000,000, so $3,500. **Tax: $270,400.**
- **MCTD percentage:** property 50%, receipts 62.5%, payroll 60%. Sum 172.5% ÷ 3 = **57.5%**.
- **Surcharge:** $270,400 × 57.5% = $155,480 × 30% = **$46,644**.
- **MFI:** the 2024 tax was $150,000, which is more than $100,000, so the 2026 MFI was 40% = **$60,000**.

### Case 3: a combined group that is a qualified manufacturer ([CT-3-A/BC-I](https://www.tax.ny.gov/pdf/current_forms/ct/ct3a_bci.pdf))

- HoldCo (the designated agent) has a New York office, so it is a taxpayer, but $0 of New York receipts. OpCo1 makes medical devices, with $40,000,000 of New York receipts and $5,000,000 of New York production property. OpCo2 provides services, with $5,000,000 of New York receipts. There is 100% ownership and a unitary business.
- **Combined return** (Form CT-3-A). Device sales are more than 50% of receipts and the property is at least $1 million, so the group is a qualified manufacturer.
- **Business income base:** combined business income of $7,000,000 at 0% = $0. **Capital base:** 0% = $0.
- **Fixed dollar minimum:** each taxable member uses the manufacturer table on its own receipts. HoldCo $19 + OpCo1 $3,750 + OpCo2 $1,125 = **$4,894**.
- **Tax: $4,894.**
- **MTA surcharge:** with 100% in the MCTD, $4,894 × 30% = **$1,468.20**.

### Case 4: a QETC ([CT-3-I](https://www.tax.ny.gov/pdf/current_forms/ct/ct3i.pdf))

- Business income base $400,000 × 4.875% = **$19,500**. Capital base 0%.
- **Fixed dollar minimum:** New York receipts of $7,000,000, on the QETC table = $2,625. **Tax: $19,500.**
- If it were not a QETC, the tax would be $400,000 × 6.5% = $26,000.

### Case 5: nexus ([deriving receipts](https://www.tax.ny.gov/bus/ct/article9a_deriving_receipts.htm); [20 NYCRR 1-2.10](https://www.tax.ny.gov/pdf/rulemaking/dec1123/corpreform/text.pdf))

- A Delaware SaaS company has no New York property or employees, and $1,300,000 of New York receipts in 2026. That is at or above $1,283,000, so it is **taxable**. P.L. 86-272 does not protect services. It files Form CT-3 and marks Part 1, Section B, line 6.
- An Ohio furniture seller has one New York sales representative, a static website, $2,000,000 of New York receipts, and orders approved and shipped from Ohio. It is **protected**, and may file with box C marked and 0 tax.
  - If the representative also installs the furniture, the protection is lost.

### Case 6: an NOL ([CT-3.4-I](https://www.tax.ny.gov/pdf/current_forms/ct/ct3_4i.pdf))

- In 2026 there is an apportioned business loss of $600,000.
- **No waiver made on the timely 2026 return:** the loss is carried back to 2023 first, then 2024, then 2025. Amend each year within three years of the 2026 return's due date (including extensions), and attach Form CT-3.4.
- **Waiver made:** the loss is carried forward up to 20 years. In each later year, the deduction cannot reduce the tax below the higher of the capital base tax or the fixed dollar minimum.

## 2025 returns, tax years beginning in 2025 ([Notice N-26-1](https://www.tax.ny.gov/forms/n-notices/n-26-1.htm); [CT-3-I](https://www.tax.ny.gov/pdf/current_forms/ct/ct3i.pdf))

- Use the **2025** forms (CT-3, CT-3-A, CT-3-M). A calendar-year return on a valid extension is due **15 October 2026**.
- The rates and fixed dollar minimum are as in the figures table, and the nexus threshold is $1,283,000.
- **Notice N-26-1.** The 2026-2027 budget decoupled from § 168(n) and from §§ 174/174A with effect from 2025.
  - If a 2025 return has **already been filed**, an **amended return must be filed** reporting the modifications.
  - Penalty and interest relief is available if you timely file or amend reporting them.
- The 2025 MFI (due 17 March 2025) was based on the 2023 tax.

## When to refuse or refer

- The taxpayer is a New York S corporation, an insurer, an Article 9 corporation, a REIT or RIC, or needs **NYC** business corporation tax figures.
- **Rebuilding a PNOLC pool** from pre-2015 returns, or disputes over an existing balance.
- **Unitary or commonly owned group questions** with foreign affiliates, captives, or members joining or leaving the group. NOL limits under §§ 381-384 and SRLY.
- **Contested sourcing**, borderline **manufacturer** tests, or **investment capital** disputes (holding period, identification).
- **P.L. 86-272 positions** that rely on web activity beyond static content.
- **Voluntary disclosure**, or years with no returns filed.

## Filing and payment ([CT-3-I](https://www.tax.ny.gov/pdf/current_forms/ct/ct3i.pdf); [CT-300-I](https://www.tax.ny.gov/pdf/current_forms/ct/ct300i.pdf); [CT-400-I](https://www.tax.ny.gov/pdf/current_forms/ct/ct400i.pdf))

- **Return:** file Form CT-3 (or CT-3-A for a combined group) and Form CT-3-M if subject to the surcharge. The return is due **3½ months after the end of the year**, which is 15 April for a calendar year (the next business day if that falls on a Saturday, Sunday or legal holiday). Most general business corporations are mandated to e-file ([Article 9-A](https://www.tax.ny.gov/bus/ct/article9a.htm)).
- **Extension:** file Form CT-5 (CT-5.3 for a combined group) by the original due date for **six months**. You must pay the properly estimated franchise tax and surcharge with it. That amount must be at least the prior year's tax (if that was a 12-month year) or at least **90%** of the final tax. Interest runs from the original due date on anything unpaid. Up to two further extensions are available on Form CT-5.1 ([CT-5-I](https://www.tax.ny.gov/pdf/current_forms/ct/ct5i.pdf); [CT-3-I](https://www.tax.ny.gov/pdf/current_forms/ct/ct3i.pdf)). Each taxpayer member of a new combined group, and each taxpayer member newly added to an existing group, also files its own CT-5 for its first combined period.
- **MFI (Form CT-300):**
  - **When required:** only if the **second preceding** year's tax after credits **exceeds $5,000**.
  - **Amount:** **25%** of that tax if it is not more than $100,000, or **40%** if it exceeds $100,000. The MTA surcharge MFI uses the same percentage.
  - **Due** on the 15th day of the 3rd month of the tax year (**16 March 2026** for calendar 2026).
  - If there is no second preceding year return, no MFI is due ([CT-300-I](https://www.tax.ny.gov/pdf/current_forms/ct/ct300i.pdf)).
- **Declaration and installments (Form CT-400):** required if the franchise tax can reasonably be expected to **exceed $5,000**.
  - The declaration is due on the 15th day of the 6th month.
  - The 2nd, 3rd and 4th installments are each (estimated tax − MFI) ÷ 3. For a calendar year they are due 15 June, 15 September and 15 December ([CT-400-I](https://www.tax.ny.gov/pdf/current_forms/ct/ct400i.pdf)).
- **Underpayment penalty exceptions** ([CT-222-I](https://www.tax.ny.gov/pdf/current_forms/ct/ct222i.pdf)):
  1. recurring seasonal income
  2. annualized income installments of at least **91%**, or 100% for a large corporation
  3. at least the prior year's tax, where that year was 12 months and showed a liability
  4. the prior year's facts and law at current rates.
  - A shortfall from using the annualized or seasonal method must be made up in the next installment.
  - Exceptions 3 and 4 are **not available to large corporations**: those with business income of at least $1 million in any of the 3 preceding years.
- **Penalties** ([CT-3-I](https://www.tax.ny.gov/pdf/current_forms/ct/ct3i.pdf)):

| Failure | Addition |
|---|---|
| Late filing (or an invalid extension) | 5% a month, up to 25% |
| Filing more than 60 days late | At least the smaller of $100 or 100% of the tax due |
| Late payment | ½% a month, up to 25%. Combined with late filing, not more than 5% for any month |
| Substantial understatement | 10% of the understatement, when tax is understated by 10% or $5,000, whichever is greater. Reduced for substantial authority or adequate disclosure |
| Interest | Always runs from the original due date, and an extension does not stop it |

- **Amended returns:** file within 90 days of filing an amended federal return, or of a final federal determination.

## Completion checklist ([CT-3-I](https://www.tax.ny.gov/pdf/current_forms/ct/ct3i.pdf))

- [ ] Nexus tested: physical presence, $1,283,000 receipts (with the $12,000 unitary floor) and P.L. 86-272, with the correct CT-3 boxes marked.
- [ ] ENI built with CT-225 modifications (including N-26-1); CT-3.1 completed and 40% safe harbor decided; receipts sourced by type.
- [ ] PNOLC (CT-3.3) and NOL deduction (CT-3.4) applied, with the floor limits; carryback waiver decided on the original return.
- [ ] Preferred status checked; all three bases computed; 7.25% tested on line 19; capital base capped at $5,000,000.
- [ ] Combined group composition, designated agent and each member's fixed dollar minimum settled; commonly owned group election status recorded.
- [ ] MCTD three-factor percentage computed; surcharge at 30% on tax before credits.
- [ ] MFI tier from the second preceding year; CT-400 installments; penalty exception documented (large corporation status checked).
- [ ] Extension payment meets the prior-year or 90% test; returns e-filed; NYC tax referred out.

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
