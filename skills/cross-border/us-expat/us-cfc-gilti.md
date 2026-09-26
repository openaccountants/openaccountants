---
name: us-cfc-gilti
description: "US anti-deferral rules for US persons owning foreign corporations: Controlled Foreign Corporation status (IRC §957/§951(b)), Subpart F income (§951/§952), GILTI (§951A) and the §250 deduction, the §962 election to be taxed at corporate rates with deemed-paid credits, the high-tax exception, and Form 5471 filing. Produces a working paper and a reviewer brief — not a filed return. MUST load alongside cross-border-tax-workflow-base."
version: 0.1
jurisdiction: US
tax_year: 2026
last_updated: 2026-09-25
authored_by: OpenAccountants team
review_status: pending_review
trust_label: By OpenAccountants
depends_on:
  - cross-border-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# US controlled foreign corporations: Subpart F and net CFC tested income (formerly GILTI)

## Scope and who this is for

This Guide covers a **US person** who owns stock in a **foreign corporation**. A US person here means a citizen, green-card holder, resident alien, domestic partnership, domestic corporation, or domestic estate or trust. The Guide sets out:

- when the owner is a **United States shareholder** and when the company is a **controlled foreign corporation (CFC)**
- the two current-year inclusions: **Subpart F income** (§951(a)(1)(A)) and **net CFC tested income** (§951A, called GILTI before 2026)
- the **§962 election** for individuals, the **high-tax exclusion**, and the **§250 deduction** and **§960 deemed-paid credit**
- **Form 5471** categories, deadlines and penalties

Figures are for tax year 2026: **tax years beginning after 31 December 2025** (2026 for calendar-year taxpayers and calendar-year CFCs). P.L. 119-21 (the One Big Beautiful Bill Act) changed several rules from 2026, so there is a dated section for **2025 returns** near the end.

It does not cover:

- passive foreign investment companies (PFICs)
- §965 transition tax computations
- §956 computations in detail
- foreign partnerships (Form 8865)
- the Form 1118 credit computation, line by line

The Form 1116 side of foreign tax credits is covered in the `us-foreign-tax-credit-1116` Guide.

A foreign entity is only in scope if it is classified as a **corporation** for US tax purposes. If it is a partnership or a disregarded entity (for example after a Form 8832 check-the-box election), the CFC rules do not apply to it and this Guide stops.

## Ask the client first

- Which foreign entities do you (or your family, trusts, partnerships or companies) own? What is each entity's US tax classification?
- For each one, what share of the **total combined voting power** do you own? What share of the **total value** of all classes of stock? Split each into stock you own **directly**, **indirectly through foreign entities**, and **constructively** (through family, partnerships, estates, trusts or corporations).
- Who else owns 10% or more by vote or value ([§951(b)](https://www.law.cornell.edu/uscode/text/26/951)), and are they US persons?
- On which days during the company's tax year did you own the stock? Were there any purchases, sales, redemptions or new issues during the year?
- What is the company's tax year? What are its income by type (dividends, interest, rents, royalties, related-party sales or services, active trading), its deductions, its foreign income taxes and its earnings and profits?
- Did the company pay you any distributions this year? Have earlier inclusions created previously taxed earnings?
- Are you an individual? If so, do you want to model the §962 election?
- Has Form 5471 been filed for every earlier year in which you had a filing obligation?

## The method, step by step

Work in this order. Each step is set out below.

1. Test each US owner for United States shareholder status (Step 1).
2. Test the company for CFC status (Step 2).
3. Build the §958(a) and §958(b) ownership maps, applying the 2026 attribution rules (Step 3).
4. Work out who includes and each pro rata share (Step 4).
5. Compute Subpart F income (Step 5).
6. Compute net CFC tested income (Step 6).
7. Apply the high-tax exception or exclusion where it is elected and the rate test is met (Step 7).
8. For corporate shareholders and §962 electors, apply the §250 deduction and the deemed-paid credit (Step 8).
9. For individuals, compare the outcomes with and without the §962 election (Step 9).
10. Determine the Form 5471 categories, the deadline and the penalty exposure (Step 10).

### Step 1: United States shareholder test ([§951(b)](https://www.law.cornell.edu/uscode/text/26/951))

A US person is a **United States shareholder** if it owns, or is treated as owning, **10% or more** of **either**:

- the total combined voting power of all classes of voting stock, **or**
- the total value of shares of all classes of stock.

The test is "10 percent or more", so exactly 10% qualifies. Ownership counts direct and indirect stock (§958(a)) and constructive stock (§958(b)).

### Step 2: CFC test ([§957(a)](https://www.law.cornell.edu/uscode/text/26/957))

The foreign corporation is a **CFC** if United States shareholders together own **more than 50%** of the voting power **or** of the value, on **any day** of the corporation's tax year.

- Exactly 50% is not enough.
- Owners below 10% are not United States shareholders, so their stock does not count toward the more-than-50% total.

### Step 3: build two ownership maps ([§958](https://www.law.cornell.edu/uscode/text/26/958))

- **§958(a) ownership** decides **who includes** income and **how much**. It is stock owned directly, plus stock held proportionately through foreign corporations, partnerships, trusts and estates.
- **§958(b) constructive ownership** decides **status** only: whether someone is a United States shareholder, and whether the company is a CFC. It uses the §318 attribution rules, with modifications.

Record both maps separately.

**Change from 2026: downward attribution from foreign persons is switched off again.**

- For tax years of foreign corporations beginning after 31 December 2025, §958(b)(4) says the §318(a)(3) rules "shall not be applied so as to consider a United States person as owning stock which is owned by a person who is not a United States person".
- So a US subsidiary of a foreign parent is no longer treated as owning its foreign sister companies' stock for CFC status.

**New §951B.**

- In its place, §951B applies the Subpart F and §951A rules to a **foreign controlled United States shareholder** of a **foreign controlled foreign corporation**.
- That is broadly a US person that would own more than 50% if downward attribution still applied.
- If the structure has a foreign parent above both US and foreign subsidiaries, refer it out.

### Step 4: who includes, and the pro rata share ([§951(a)](https://www.law.cornell.edu/uscode/text/26/951); [§951A(c)](https://www.law.cornell.edu/uscode/text/26/951A))

These rules apply for tax years of foreign corporations beginning after 31 December 2025.

**Subpart F income:**

- Each United States shareholder that owns §958(a) stock **on any day** during the CFC year includes its pro rata share.
- The pro rata share is the income attributable to the stock it owned **and** to the part of the year when all three of these were true at once:
  - it owned the stock
  - it was a United States shareholder
  - the company was a CFC
- The inclusion goes in the shareholder's tax year that includes the **last day it owned** §958(a) stock during that CFC year.

**Net CFC tested income:**

- The same pro rata rules apply.
- For §951A, a person counts as a United States shareholder only if it owns §958(a) stock on any day in the year.

Constructive-only owners count for status but include nothing.

**§956 investments in US property** (§951(a)(1)(B)) still use the owner on the **last day** of the CFC year on which the company is a CFC. Refer §956 computations out.

### Step 5: Subpart F income ([§952](https://www.law.cornell.edu/uscode/text/26/952); [§954](https://www.law.cornell.edu/uscode/text/26/954))

Classify the CFC's gross income. The main Subpart F categories are:

- **Foreign personal holding company income:** dividends, interest, rents, royalties, annuities, and certain property, currency and commodity gains.
- **Foreign base company sales income and services income:** mainly related-party sales and services that have little to do with the CFC's own country.
- **Insurance income.**

Then apply these rules:

- **De minimis rule (§954(b)(3)(A)):** if foreign base company income plus gross insurance income is **less than** the lesser of **5%** of gross income or **$1,000,000**, none of the gross income is treated as foreign base company or insurance income.
- **Full inclusion rule (§954(b)(3)(B)):** if that total **exceeds 70%** of gross income, all gross income is treated as foreign base company or insurance income. This is still subject to the high-tax exception and to deductions.
- **Related-CFC look-through (§954(c)(6)):** dividends, interest, rents and royalties from a related CFC are not foreign personal holding company income to the extent they come from the payer's income that is neither Subpart F income nor effectively connected income. P.L. 119-21 removed the rule's end date, for tax years of foreign corporations beginning after 31 December 2025.
- **Earnings and profits limit (§952(c)(1)(A)):** Subpart F income cannot exceed the CFC's current-year earnings and profits.
- **High-tax exception (§954(b)(4)):** see Step 7.

### Step 6: net CFC tested income ([§951A](https://www.law.cornell.edu/uscode/text/26/951A))

For tax years beginning after 31 December 2025, each United States shareholder includes its **net CFC tested income**:

- its pro rata share of the **tested income** of each CFC,
- **minus** its pro rata share of the **tested loss** of each CFC.

To find a CFC's **tested income**, start with its gross income and **exclude**:

- effectively connected income (§952(b))
- income taken into account in determining Subpart F income
- income excluded under the high-tax exception of §954(b)(4)
- dividends from related persons
- foreign oil and gas extraction income

Then subtract the deductions (including taxes) properly allocable to that gross income. If the deductions are larger, the result is a tested loss.

**What is gone from 2026:**

- The old GILTI formula subtracted a **net deemed tangible income return** (a return on qualified business asset investment, QBAI) from net tested income.
- P.L. 119-21 struck that out. For 2026 there is **no QBAI reduction**: the inclusion is the whole net tested income.

The §951A inclusion is treated as a §951(a)(1)(A) Subpart F inclusion for several purposes, including §§959, 961 and **962**.

### Step 7: high-tax exception and exclusion ([§954(b)(4)](https://www.law.cornell.edu/uscode/text/26/954); [Reg. §1.951A-2(c)(7)](https://www.law.cornell.edu/cfr/text/26/1.951A-2))

**Rate test:** the income must have been subject to a foreign effective rate **greater than 90%** of the maximum §11 rate. With a **21%** corporate rate, that means **greater than 18.9%**. Exactly 18.9% fails.

**Subpart F:** the §954(b)(4) exception removes qualifying items from foreign base company income and insurance income.

**Tested income (the "GILTI high-tax exclusion"):**

- It applies only if an **election** is in effect for the CFC for the year.
- The rate is tested for each **tested unit**, not for the CFC as a whole.
- The election is made by the CFC's **controlling domestic shareholders**. They file a statement with one of:
  - a timely filed original return, or
  - an amended return filed **within 24 months of the unextended due date** of the original return.
- If the election is made on an amended return, every United States shareholder that owns §958(a) stock at the end of the CFC's year must also file amended returns (or timely original returns, if none has been filed yet).
- All of those returns must be filed, and any resulting tax paid, within a **single period of no more than six months** inside the 24-month window.
- The election, or its revocation, is **valid only if every requirement is met**, including the notices to the other United States shareholders. A revocation is made the same way as an election on an amended return.
- For a CFC in a **CFC group**, the election, or its revocation, applies to **every member** of the group.

**Credit trade-off:** excluded income drops out of tested income, so the foreign taxes on it are not tested foreign income taxes and give no §960(d) credit. Model both outcomes before electing.

**Open point for 2026:** the regulations still cite the pre-2026 numbering of §951A. For example, they cite §951A(c)(2)(A)(i)(III), which is now §951A(b)(2)(A)(i)(III). Until Treasury updates them, confirm that the election mechanics have not changed before relying on them for 2026.

### Step 8: the §250 deduction and the deemed-paid credit, for corporate shareholders and §962 electors ([§250](https://www.law.cornell.edu/uscode/text/26/250); [§960](https://www.law.cornell.edu/uscode/text/26/960))

These rules apply for tax years beginning after 31 December 2025.

**§250 deduction ([§250(a)(1)(B)](https://www.law.cornell.edu/uscode/text/26/250)):**

- A domestic corporation deducts **40%** of its net CFC tested income, **plus** the §78 gross-up that relates to it.
- The deduction is limited by taxable income under §250(a)(2).

**Deemed-paid credit ([§960(d)](https://www.law.cornell.edu/uscode/text/26/960)):**

- The corporation is deemed to pay **90%** of:
  - its **inclusion percentage** (net CFC tested income divided by the total of its pro rata shares of tested income), **multiplied by**
  - the tested foreign income taxes of its CFCs.
- Taxes of a CFC with a tested loss are not tested foreign income taxes. Tested losses also lower the inclusion percentage.

**Gross-up ([§78](https://www.law.cornell.edu/uscode/text/26/78)):** the full deemed-paid amount, figured without the "90 percent of" haircut, is treated as a dividend.

**Taxes on distributed previously taxed income ([§960(d)(4)](https://www.law.cornell.edu/uscode/text/26/960)):**

- No credit is allowed for **10%** of the foreign taxes on a distribution that is excluded under §959(a) because of an earlier §951A inclusion.
- This applies to amounts **after 28 June 2025**. Check the exact scope for the client's facts.

**Foreign tax credit limitation ([§904(b)(5)](https://www.law.cornell.edu/uscode/text/26/904)):**

- For the Section 951A category, only two kinds of deduction are allocated to the income:
  - the §250 deduction (and taxes on the income deducted under §164(a)(3))
  - deductions **directly allocable** to it
- **No interest expense or research and experimental expenditure** is allocated to it.
- Excess credits in this category cannot be carried back or forward. This matches the `us-foreign-tax-credit-1116` Guide.

**Subpart F inclusions:** §960(a) deems a domestic corporation to have paid the foreign income taxes properly attributable to the Subpart F item, with no haircut.

### Step 9: individuals, and the §962 election ([§962](https://www.law.cornell.edu/uscode/text/26/962); [Reg. §1.962-1](https://www.law.cornell.edu/cfr/text/26/1.962-1); [Reg. §1.962-2](https://www.law.cornell.edu/cfr/text/26/1.962-2))

**Without the election**, an individual United States shareholder:

- includes Subpart F income and net CFC tested income at ordinary individual rates
- gets **no §250 deduction**, because it applies to domestic corporations
- gets **no deemed-paid credit** for the CFC's foreign taxes

**With the election:**

- **Rate:** the tax on the §951(a) amounts equals the §11 corporate tax on them, at **21%**.
- **Credit:** §960 applies as if the individual were a domestic corporation. For 2026 that means the §960(d) credit at 90%, claimed on **Form 1118**, not Form 1116.
- **§250:** the regulations give the individual the §250 deduction that a domestic corporation would get, on the net CFC tested income plus its §78 gross-up. The §962 computation allows only the deductions the regulation lists.
- **Who can elect:** only an individual (including a trust or estate) who is a United States shareholder.
- **Scope:** the election covers **all** CFCs for which the shareholder has a §951(a) inclusion that year. It cannot be made for some CFCs only.
- **How:** attach a statement to the return for the year. The statement lists:
  - each CFC and each entity in the ownership chain
  - the inclusions, company by company
  - the shareholder's share of each CFC's earnings and profits and foreign taxes
  - distributions, by type

  The Form 5471 instructions also contemplate making the election on an **amended return** in a later year.
- **Revocation:** only with IRS consent. Consent needs a material and substantial change in circumstances that could not have been anticipated.

**The second layer ([§962(d)](https://www.law.cornell.edu/uscode/text/26/962)):**

- When the CFC later distributes earnings that were included under the election, the distribution is taxable to the extent it **exceeds the US tax paid** under the election.
- The usual §959 exclusion does not shelter the rest.
- Model both the inclusion year and the expected distribution years before recommending the election.

### Step 10: Form 5471 ([Form 5471 instructions](https://www.irs.gov/instructions/i5471))

**When to file:** attach Form 5471 to the income tax return, and file both **by the due date (including extensions)** of that return.

**Several categories:** one person can fall into several categories. If so, complete every item that applies, without duplicating information.

| Category | Who (summary) |
| --- | --- |
| 1 (1a, 1b, 1c) | United States shareholder of a section 965 specified foreign corporation |
| 2 | US citizen or resident who is an officer or director of a foreign corporation in which a US person acquired stock that meets the 10% ownership requirement, or an additional 10% or more |
| 3 | US person who acquires stock that reaches the 10% ownership requirement, disposes of enough stock to fall below it, or becomes a US person while meeting it |
| 4 | US person who controlled the foreign corporation during its annual accounting period: **more than 50%** of total voting power or total value |
| 5 (5a, 5b, 5c) | United States shareholder of a CFC who owned the stock on the last day in the year on which the company was a CFC |

**Main exceptions:**

- A constructive-only owner, where the US person the ownership is attributed from files all the required information.
- A constructive-only owner whose ownership comes solely from a **nonresident alien**.
- A United States shareholder of a **foreign-controlled CFC** that owns no §958(a) stock in it **and** is not related to it under §954(d)(3).
- Any case where **no** United States shareholder owns §958(a) stock in a foreign-controlled CFC on the last day of its CFC year.

**Penalties ([§6038](https://www.law.cornell.edu/uscode/text/26/6038)):**

- **$10,000** for each annual accounting period of each foreign corporation, for failure to furnish the information on time.
- If the failure continues **more than 90 days** after the IRS mails a notice, a further **$10,000** for each 30-day period or part of one. This extra penalty is capped at **$50,000** per failure.
- **Foreign tax credit reduction:**
  - available foreign taxes under §§901 and 960 are cut by **10%**
  - a further **5%** is cut for each 3-month period the failure continues after the 90-day period
  - both are subject to the limits in §6038(c)(2)

**Statute of limitations ([§6501(c)(8)](https://www.law.cornell.edu/uscode/text/26/6501)):**

- The time to assess any tax on the return stays open until **3 years after** the information is furnished.
- If the failure was due to reasonable cause and not willful neglect, only the related items stay open.

**Corrections:** file a corrected Form 5471, marked "Corrected", with an amended return.

## Thresholds and figures with years

| Item | Tax years beginning after 31 Dec 2025 | 2025 (and earlier post-2017 years) | Source |
| --- | --- | --- | --- |
| United States shareholder | 10% or more, vote or value | same | [§951(b)](https://www.law.cornell.edu/uscode/text/26/951) |
| CFC | more than 50%, vote or value, any day | same | [§957(a)](https://www.law.cornell.edu/uscode/text/26/957) |
| Name of §951A inclusion | net CFC tested income | global intangible low-taxed income (GILTI) | [§951A](https://www.law.cornell.edu/uscode/text/26/951A) |
| QBAI return | none (repealed) | 10% of QBAI, reduced by specified interest expense | [Reg. §1.951A-1](https://www.law.cornell.edu/cfr/text/26/1.951A-1) |
| §250 deduction on the §951A amount | 40% | 50% | [§250](https://www.law.cornell.edu/uscode/text/26/250) |
| §960(d) deemed-paid share | 90% | 80% | [§960](https://www.law.cornell.edu/uscode/text/26/960) |
| Disallowed share of tax on distributed §951A earnings | 10% | 10%, for amounts after 28 June 2025 (check the exact scope) | [§960(d)(4)](https://www.law.cornell.edu/uscode/text/26/960) |
| Corporate rate (also used for §962) | 21% | 21% | [§11(b)](https://www.law.cornell.edu/uscode/text/26/11) |
| High-tax threshold | greater than 18.9% | greater than 18.9% | [Reg. §1.951A-2](https://www.law.cornell.edu/cfr/text/26/1.951A-2) |
| Subpart F de minimis | less than the lesser of 5% of gross income or $1,000,000 | same | [§954(b)(3)](https://www.law.cornell.edu/uscode/text/26/954) |
| Subpart F full inclusion | more than 70% of gross income | same | [§954(b)(3)](https://www.law.cornell.edu/uscode/text/26/954) |
| Form 5471 penalty | $10,000 plus up to $50,000 after notice | same | [§6038(b)](https://www.law.cornell.edu/uscode/text/26/6038) |

## Boundary and exception table

| Situation | Result | Source |
| --- | --- | --- |
| Owns exactly 10% of value but none of the vote | United States shareholder (vote **or** value, "10 percent or more") | [§951(b)](https://www.law.cornell.edu/uscode/text/26/951) |
| United States shareholders own exactly 50% | Not a CFC (needs more than 50%) | [§957(a)](https://www.law.cornell.edu/uscode/text/26/957) |
| Crosses more than 50% for one day only | CFC for that year; the pro rata share is still limited to the qualifying period | [§957(a)](https://www.law.cornell.edu/uscode/text/26/957); [§951(a)(2)](https://www.law.cornell.edu/uscode/text/26/951) |
| Owns only by attribution (§958(b)) | Counts for status; includes nothing | [§951(a)(1)](https://www.law.cornell.edu/uscode/text/26/951) |
| 2026: CFC status only through downward attribution from a foreign parent | Not a CFC under §957; check §951B | [§958(b)(4)](https://www.law.cornell.edu/uscode/text/26/958); [§951B](https://www.law.cornell.edu/uscode/text/26/951B) |
| Foreign effective rate exactly 18.9% | High-tax exception or exclusion not available (the rate must be greater) | [Reg. §1.951A-2](https://www.law.cornell.edu/cfr/text/26/1.951A-2) |
| Individual, no §962 election | No §250 deduction, no deemed-paid credit | [§250](https://www.law.cornell.edu/uscode/text/26/250); [§960](https://www.law.cornell.edu/uscode/text/26/960) |
| §962 election wanted for one CFC only | Not possible: it applies to all CFCs with inclusions that year | [Reg. §1.962-2](https://www.law.cornell.edu/cfr/text/26/1.962-2) |
| Excess Section 951A category credit | No carryback or carryover | [§904](https://www.law.cornell.edu/uscode/text/26/904) |

## Worked cases ([§951A](https://www.law.cornell.edu/uscode/text/26/951A); [§962](https://www.law.cornell.edu/uscode/text/26/962); [§6038](https://www.law.cornell.edu/uscode/text/26/6038))

All amounts are hypothetical. Each case assumes:

- a calendar-year US individual who owns 100% of a calendar-year CFC all year
- no Subpart F income and no other CFCs
- no other deductions in the §962 computation
- no binding §250(a)(2) limit

**Case A: 2026, no §962 election.** The CFC has tested income of $100,000 after deducting foreign income tax of $15,000.

- Net CFC tested income included: $100,000.
- It is taxed at ordinary individual rates.
- There is no §250 deduction and no deemed-paid credit for the $15,000.

**Case B: 2026, §962 election.** Same facts.

- **High-tax check:** the foreign effective rate is 15,000 ÷ 115,000 = 13.04%. That is not greater than 18.9%, so the high-tax exclusion is not available.
- **Gross-up:** deemed-paid taxes before the haircut are $15,000. The §78 gross-up is $15,000. Income is therefore $100,000 + $15,000 = $115,000.
- **§250 deduction:** 40% × $115,000 = $46,000. The taxable amount is $69,000.
- **Tax at 21%:** $14,490.
- **§960(d) credit:** 90% × $15,000 = $13,500. All the income is foreign source; assuming the Section 951A category limitation does not bind, the full $13,500 is allowed.
- **US tax under the election:** $14,490 − $13,500 = $990.
- **Later distribution (§962(d)):** if the CFC later distributes the $100,000 the taxable amount is $100,000 − $990 = $99,010. Whether it is a qualified dividend depends on the CFC's country and treaty status, so refer that point out.

**Case C: 2025 return, no §962 election, with QBAI.** Tested income is $100,000 and QBAI is $200,000. There is no specified interest expense.

- Net deemed tangible income return: 10% × $200,000 = $20,000.
- GILTI: $100,000 − $20,000 = $80,000. It is included at ordinary rates.
- With the same facts in 2026, the inclusion would be the full $100,000 because QBAI is repealed.

**Case D: late Form 5471.** One CFC, one year, not filed. The IRS mails a notice, and the failure continues well past 90 days.

- Dollar penalty: $10,000 plus the continuation penalty capped at $50,000. That is at most $60,000 for that CFC-year.
- Foreign taxes available for credit are also reduced.
- The assessment period for the whole return stays open until 3 years after the form is filed. If the failure was due to reasonable cause and not willful neglect, only the related items stay open.

## 2025 returns, tax years beginning before 1 January 2026 ([§250](https://www.law.cornell.edu/uscode/text/26/250); [§960](https://www.law.cornell.edu/uscode/text/26/960); [Reg. §1.951A-1](https://www.law.cornell.edu/cfr/text/26/1.951A-1))

Use these rules for a 2025 return, including one on extension. The Form 5471 goes with the return, by its extended due date.

- **Name and formula:** the inclusion is **GILTI**. It is net tested income minus the net deemed tangible income return. That return is **10% of QBAI**, reduced by specified interest expense.
- **§250 rate:** **50%** of GILTI plus the related §78 gross-up (for domestic corporations and §962 electors).
- **§960(d) rate:** the deemed-paid share is **80%**. The §78 gross-up ignores that haircut.
- **Distributions of previously taxed GILTI:** the 10% disallowance in §960(d)(4) already applies to taxes on such distributions **after 28 June 2025**. Check the exact scope for the client's facts.
- **Pro rata share:**
  - For **both** Subpart F (§951(a)(1)(A)) and the §951A inclusion, only a United States shareholder that owned §958(a) stock on the **last day** of the foreign corporation's year on which it was a CFC included anything.
  - A shareholder that sold before that day had no inclusion for that year.
  - The pre-2026 §951(a)(2)(B) reduction for dividends paid to other owners during the year still applies.
  - A transition rule excludes certain dividends from that reduction. Check it for any 2025 change of ownership.
- **Downward attribution:**
  - §958(b)(4) did not apply, so a US person could be treated as owning stock held by a foreign person.
  - This can make the foreign subsidiaries of a foreign-parented group into CFCs.
  - The Form 5471 Category 5b and 5c exceptions address some of these cases.
- **Expense allocation:** the new §904(b)(5) rule for the Section 951A category starts only in 2026. For 2025, use the prior allocation rules and refer the computation out.
- **Look-through:** the §954(c)(6) related-CFC look-through also applies in 2025.

## When to refuse or refer

Refer to a credentialed US international tax preparer when:

- the ownership chain involves a foreign parent, trusts, partnerships or several tiers (§951B, §958 attribution, §958(a) chains)
- a foreign trust holds the CFC stock: coordinate with the `us-foreign-trust-reporting` Guide (Forms 3520 and 3520-A), because the same earnings can trigger both regimes
- a fiscal-year CFC's tax year straddles 1 January 2026. Some changes apply to "taxable years beginning after" that date (QBAI repeal and the new §250 and §960(d) rates). Others apply to "taxable years of foreign corporations beginning after" it (the any-day owner rule, §958(b)(4) and §951B). The two can fall in different years.
- there are mid-year stock transfers, redemptions or new issues (the pro rata share and year-closing rules)
- there is Subpart F income beyond simple passive income, or there is insurance income or a §956 investment in US property
- a §962 election, the high-tax exclusion, a Form 1118 computation, or a previously taxed earnings account is needed
- prior-year Forms 5471 are missing (delinquent filing and reasonable-cause strategy)
- the CFC may also be a PFIC, or has US effectively connected income

Refuse to give a final figure when the client cannot provide the CFC's income by category, its foreign taxes, or its earnings and profits.

## Filing steps

1. Finish the CFC status table and the §958(a) and §958(b) maps (Steps 1 to 3).
2. Compute Subpart F income and net CFC tested income for each CFC (Steps 5 to 7), and each shareholder's pro rata share (Step 4).
3. Individuals: decide on the §962 election. If you make it, attach the statement to the return and compute the tax and credit on Form 1118.
4. Controlling domestic shareholders: decide on the high-tax election, and give the other shareholders any required notices.
5. Report the inclusions on the income tax return. Prepare Form 5471 with the schedules that its category chart requires for each filer category.
6. File the return and Form 5471 together, **by the return's due date including extensions**.
7. Keep the working papers, the ownership maps, the election statements and the previously taxed earnings records.

## Completion checklist ([§951](https://www.law.cornell.edu/uscode/text/26/951); [§957](https://www.law.cornell.edu/uscode/text/26/957); [Reg. §1.951A-2](https://www.law.cornell.edu/cfr/text/26/1.951A-2))

- [ ] Entity confirmed as a foreign **corporation** for US tax purposes.
- [ ] §958(a) and §958(b) maps built separately, applying the 2026 §958(b)(4) and §951B rules, or the 2025 rules for 2025.
- [ ] The 10%-or-more United States shareholder test and the more-than-50% CFC test done on both vote and value, for every day of the year.
- [ ] Pro rata shares computed with the ownership-period rule for the year in question.
- [ ] Subpart F income classified; de minimis, full-inclusion and earnings and profits limits applied.
- [ ] Net CFC tested income (2026) or GILTI with QBAI (2025) computed; tested losses reflected.
- [ ] High-tax exception or election tested at greater than 18.9%, with the credit trade-off modelled.
- [ ] Individuals: outcomes with and without §962 modelled, including the §962(d) second layer.
- [ ] The right year's §250 (40% or 50%) and §960(d) (90% or 80%) percentages used.
- [ ] Form 5471 categories, schedules and prior-year compliance checked; penalty exposure noted.
- [ ] Output labelled as a draft working paper for sign-off by a credentialed preparer.

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
