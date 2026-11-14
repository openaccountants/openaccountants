---
name: nj-cbt-and-bait
description: New Jersey Corporation Business Tax (CBT) and the elective Pass-Through Business Alternative Income Tax (BAIT, also called PTE) for tax year 2026. Covers nexus (more than 100,000 dollars of receipts or 200 transactions), mandatory unitary combined reporting, entire net income and the dividend exclusion, single sales factor allocation, PNOL and NOL with the 80% limit, the 6.5%, 7.5% and 9% rates on the whole base, the minimum tax tables, the 2.5% Corporate Transit Fee above 10 million dollars (periods beginning 2024 to 2028), CBT-150 estimates and extensions, and the BAIT election, brackets (5.675%, 6.52%, 10.9%), estimates and the owner's refundable credit. Trigger on "New Jersey corporate tax", "NJ CBT", "CBT-100", "CBT-100U", "CBT-100S", "Corporate Transit Fee", "NJ BAIT", "NJ PTE", "PTE-100", "New Jersey pass-through entity tax".
version: "1.0"
jurisdiction: US-NJ
tax_year: 2026
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: corporate-tax
type: computation
---

# New Jersey Corporation Business Tax (CBT) and Pass-Through Business Alternative Income Tax (BAIT), tax year 2026

> **Source-cited draft.** Built from the 2025 CBT-100, CBT-100U and CBT-100S instructions, the 2026 CBT-150 instructions, the 2026 PTE-100 and 2027 PTE-150 instructions, Technical Bulletins TB-86(R), TB-108(R), TB-109 and TB-110(R) and the Division of Taxation's CBT and BAIT pages, read on 2026-11-14. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** CBT is 9% of the whole tax base above USD 100,000 (7.5% above USD 50,000, 6.5% at or below), never less than the minimum tax (USD 500 to USD 2,000 by New Jersey receipts). For privilege periods beginning 1 January 2024 through 31 December 2028, a 2.5% Corporate Transit Fee applies to all taxable net income when it is over USD 10 million ([CBT-100 instructions (2025)](https://www.nj.gov/treasury/taxation/pdf/current/cbt/cbt100ins.pdf)). BAIT is elected each year by the original PTE-100 due date (15 March 2027 for calendar 2026), at 5.675% on the first USD 250,000 of aggregate distributive proceeds, 6.52% to USD 1,000,000 and 10.9% above ([2026 PTE-100 instructions](https://www.nj.gov/treasury/taxation/pdf/current/pte-bait/pte100instr.pdf)); owners get a refundable credit.

## Scope and who this is for

This skill covers two New Jersey taxes that are often planned together:

- the **Corporation Business Tax (CBT)** on C corporations and combined groups (Forms CBT-100 and CBT-100U), including the rates, the minimum tax, the Corporate Transit Fee, mandatory unitary combined reporting, single sales factor apportionment, economic nexus, the NOL and PNOL rules, estimated tax, extensions and penalties;
- the elective **Pass-Through Business Alternative Income Tax (BAIT, also called PTE)** paid by partnerships, New Jersey S corporations and LLCs taxed as either (Form PTE-100), and the owner's refundable credit.

Figures are for **tax year 2026** where published. The latest CBT instructions are the 2025 set, used for accounting periods ending 31 July 2025 through 30 June 2026. The 2026 CBT-150 estimated tax instructions and the 2026 PTE-100 instructions are published. Each figure carries its year. A dated section covers **2025 returns**.

Not covered: the individual NJ-1040 and NJ-1040NR themselves (see the **nj-income-tax** skill, which shows where the BAIT credit goes on the return), banking and financial corporations' special rules, insurance premiums tax, public utility taxes, tax credit programs, and New Jersey sales tax.

## Ask the client first

- What is the entity for federal tax purposes (C corporation, S corporation, partnership, disregarded entity)? If a federal S corporation, does it file as a **New Jersey S corporation** (Form CBT-100S) or as a New Jersey C corporation?
- What does it have or do in New Jersey: office, employees, property, inventory (including in a marketplace warehouse), and New Jersey receipts? How many separate transactions are delivered to New Jersey customers?
- Does it sell only tangible goods, and is soliciting orders its only New Jersey activity? What does its website or app do after the sale?
- Is it more than 50% commonly owned with other corporations, and are they in a unitary business? Which filing method is the group using (water's-edge, world-wide or affiliated group), and when was it elected? ([CBT-100U instructions (2025)](https://www.nj.gov/treasury/taxation/pdf/current/cbt/cbt100uins.pdf))
- What is the allocated taxable net income (after allocation and NOLs)? Is it near $50,000, $100,000 or $10 million? ([CBT-100 instructions (2025)](https://www.nj.gov/treasury/taxation/pdf/current/cbt/cbt100ins.pdf))
- New Jersey gross receipts, and the **total payroll of the whole affiliated or controlled group** (is it $5,000,000 or more)? ([CBT-100 instructions (2025)](https://www.nj.gov/treasury/taxation/pdf/current/cbt/cbt100ins.pdf))
- Loss history: PNOLs from periods ending before 31 July 2019, post-allocation NOLs, and which of those arose in periods beginning after 31 July 2023?
- Last year's total CBT liability and the prior year's gross receipts (for estimated tax).
- For a pass-through entity: who the owners are (resident or nonresident individuals, estates, trusts, corporations, partnerships, tax-exempt owners), each owner's share of distributive proceeds, whether it files NJ-1065 or CBT-100S, whether BAIT has been elected for the year, and whether it files a composite return (NJ-1080-C).
- For owners: do they also pay another state's pass-through entity tax, and do they have other income that BAIT will not cover?

## The method, step by step

### Step 1: does the corporation have nexus? ([CBT-100 instructions (2025)](https://www.nj.gov/treasury/taxation/pdf/current/cbt/cbt100ins.pdf); [TB-108(R)](https://www.nj.gov/treasury/taxation/pdf/pubs/tb/tb108.pdf))

- Every domestic (New Jersey) corporation files. A foreign corporation files if it holds New Jersey authority to do business, does business, employs or owns capital or property, maintains an office, derives receipts, engages in contacts, or keeps a stock of goods in New Jersey.
- **Bright-line economic nexus** (privilege periods ending on and after 31 July 2023): a corporation has nexus if, in its tax year, New Jersey receipts are **more than $100,000**, or **200 or more** separate transactions are delivered to New Jersey customers. For a service, "delivered" means where the benefit is received. A corporation meeting neither threshold, with no other nexus, does not have nexus on receipts alone.
- **Public Law 86-272** protects only the solicitation of orders for tangible goods. TB-108(R) lists internet activities that go beyond it, for example post-sale chat or email support through the website, placing cookies to gather data that is sold, and warranty or upgrade services delivered over the internet. A corporation claiming P.L. 86-272 checks the box on page 1, still pays the minimum tax, and is not subject to the Corporate Transit Fee.
- Inventory held in a New Jersey marketplace warehouse is property in New Jersey, so it creates nexus ([Division nexus page](https://www.nj.gov/treasury/taxation/organization/audit-taxtype-nexus.shtml)).

### Step 2: separate return or combined return? ([CBT-100U instructions (2025)](https://www.nj.gov/treasury/taxation/pdf/current/cbt/cbt100uins.pdf); [TB-109](https://www.nj.gov/treasury/taxation/pdf/pubs/tb/tb109.pdf); [TB-86(R)](https://www.nj.gov/treasury/taxation/pdf/pubs/tb/tb86r.pdf))

- **Mandatory combined reporting** applies for group privilege periods ending on and after 31 July 2019. A combined group is all companies with **common ownership** (more than 50% of voting control owned directly or indirectly by a common owner) that are engaged in a **unitary business**, where at least one is subject to CBT. Combined returns are mandatory, not elective. The group files one Form CBT-100U through its **managerial member**.
- **Filing methods:** the default is **water's-edge** (entities with significant business operations in the United States, with inclusions and exceptions). The group may instead elect **world-wide** or **affiliated group** on a timely filed original return. The election binds the year of election plus five later years (usually six tax years). It can be revoked early only prospectively, for reasonable cause, by written request to the Director. It cannot be made by amending a filed return.
- **Who is in and out:** New Jersey S corporations only if they elect in. Partnerships and disregarded entities are not members; their income flows to the corporate owner. REITs, RICs and investment companies file separately unless captive.
- **Allocation:** for privilege periods ending on and after 31 July 2023 the group uses the **Finnigan method**. All members' New Jersey receipts go into the numerator, and the tax rate is set at group level.
- **P.L. 86-272 in a group:** for privilege periods ending on and after 31 July 2023 the group is one taxpayer. A member's own P.L. 86-272 protection does not protect the group if another member exceeds P.L. 86-272 or has New Jersey activity it does not protect ([CBT-100U instructions (2025)](https://www.nj.gov/treasury/taxation/pdf/current/cbt/cbt100uins.pdf)). The member-by-member test applied only to periods ending before 31 July 2023 ([Division notice](https://www.nj.gov/treasury/taxation/cbt/combinedgroupsrevision.shtml)).

### Step 3: entire net income ([CBT-100 instructions (2025)](https://www.nj.gov/treasury/taxation/pdf/current/cbt/cbt100ins.pdf); [TB-110(R)](https://www.nj.gov/treasury/taxation/pdf/pubs/tb/tb110.pdf); [OBBBA renaming notice](https://www.nj.gov/treasury/taxation/cbt/obbba-gilti-fdii-renaming.shtml))

- Start from federal taxable income (the federal return is attached) and make New Jersey modifications on Schedule A.
- **NCTI (formerly GILTI)** is treated as a dividend. The dividend exclusion is **100%** for dividends from qualified subsidiaries (at least **80%** owned by vote and by shares) and **50%** for other dividends where at least **50%** is owned; nothing below that. (TB-110(R) says "more than 50%" for the 50% band, while the CBT-100 instructions say "at least 50%"; at exactly 50% ownership, check with the Division.) The whole exclusion is then reduced by a clawback of **5%** of all dividends and deemed dividends. The clawback does not apply to intercompany dividends eliminated in a combined group; those are not eligible for the exclusion either. The federal section 250 deductions are not allowed, and FDDEI is included gross.
- For tax years beginning after 31 December 2025 the federal law renamed GILTI as NCTI and FDII as FDDEI. New Jersey's treatment is unchanged.

### Step 4: allocate with the single sales factor ([CBT-100 instructions (2025)](https://www.nj.gov/treasury/taxation/pdf/current/cbt/cbt100ins.pdf); [CBT-100U instructions (2025)](https://www.nj.gov/treasury/taxation/pdf/current/cbt/cbt100uins.pdf); [TB-108(R)](https://www.nj.gov/treasury/taxation/pdf/pubs/tb/tb108.pdf))

- Business income is allocated by a **single sales (receipts) factor** on Schedule J: New Jersey receipts over receipts everywhere, carried to six decimal places. Goods are New Jersey receipts if shipped to points in New Jersey, or if possession passes to the customer in New Jersey. Services are sourced where the benefit is received.
- Exclusions and adjustments come before the factor is computed. Nonoperational income is dealt with on Schedule O and nonunitary partnership income separately.
- The result (allocated entire net income before NOLs) is Schedule A, Part II, line 19.

### Step 5: NOLs, and the PNOL conversion ([CBT-100 instructions (2025)](https://www.nj.gov/treasury/taxation/pdf/current/cbt/cbt100ins.pdf); [Worksheet 500-P](https://www.nj.gov/treasury/taxation/pdf/current/cbt/500-p.pdf))

- **PNOLs** are losses from tax years ending **before 31 July 2019**. To use them, convert the unused, unexpired amounts to a post-allocation basis on Worksheet 500-P: multiply each carryover by the allocation factor from the **last tax period ending before 31 July 2019**. PNOLs are deducted before any NOL.
- **Post-allocation NOLs** are losses from tax years ending on or after 31 July 2019, already on an allocated basis.
- Both carry forward **20 privilege periods** after the loss period. There is **no carryback**.
- **80% limit:** for tax years ending on or after 31 July 2023, NOLs are limited to **80%** of taxable net income (the federal section 172(a)(2) limit, with New Jersey dates). On Form 500 the limit applies to NOLs from periods beginning after 31 July 2023; NOLs from periods ending on or after 31 July 2019 and beginning before 1 August 2023 are not limited.
- Federal rules on consolidated NOLs, ownership changes and reorganisations generally apply where consistent with the CBT Act. Losses excluded from income under section 108 reduce PNOLs first, then NOLs, after allocation.
- In a combined group, NOLs are also limited to **80%** of the group's taxable net income ([CBT-100U instructions (2025)](https://www.nj.gov/treasury/taxation/pdf/current/cbt/cbt100uins.pdf); see TB-95(R) for members joining or leaving).
- Allocated entire net income minus the PNOL and NOL deductions is **taxable net income** (Schedule A, Part II, line 21).

### Step 6: tax at the graduated rate, compare with the minimum tax ([CBT-100 instructions (2025)](https://www.nj.gov/treasury/taxation/pdf/current/cbt/cbt100ins.pdf); [CBT-100U instructions (2025)](https://www.nj.gov/treasury/taxation/pdf/current/cbt/cbt100uins.pdf))

- One rate (6.5%, 7.5% or 9%, table below) applies to the **whole** tax base (page 1, line 1), not in slices.
- Short periods: the 7.5% rate applies only if prorated net income is not more than **$8,333** a month, and the 6.5% rate only if it is not more than **$4,166** a month.
- For a combined group the rate is imposed at group level on the group's base.
- The tax is the **greater** of the rate tax and the minimum tax (table below), less credits. Most credits cannot take the tax below the minimum tax (there are rare exceptions); follow each credit form. In a combined group the minimum is $2,000 times the number of taxable members.

### Step 7: add the Corporate Transit Fee ([Division notice](https://www.nj.gov/treasury/taxation/cbt/corporatetransitfee.shtml); [CBT-100 instructions (2025)](https://www.nj.gov/treasury/taxation/pdf/current/cbt/cbt100ins.pdf))

- **Who:** any taxpayer whose taxable net income (Schedule A, Part III, line 2a, 2b or 2c) is **over $10 million**, for privilege periods **beginning on and after 1 January 2024 through 31 December 2028** (P.L. 2024, c.20). So it applies to 2025 and 2026, and to periods beginning up to 31 December 2028.
- **How much:** **2.5%** of the whole line 2 amount, not only the excess over $10 million. The base is taxable net income, so it is measured **after** allocation and after the PNOL and NOL deductions.
- **Credits:** tax credits cannot be used against the fee. Only payments (installments, extension payments, prior overpayments) reduce it ([New laws summary](https://www.nj.gov/treasury/taxation/newlegislation.shtml)).
- **Exempt:** public utilities, New Jersey S corporations filing CBT-100S, and P.L. 86-272 filers.
- **Combined groups:** the group is the taxpayer and the fee is imposed at group level on the group's taxable net income. Income of a member that is a public utility or S corporation is not excluded when testing or computing it.
- **Extension beyond 2028:** the Division's list of new laws shows no change to the end date as of 14 November 2026. Check the list and the Division notice before relying on a year after 2028.

### Step 8: BAIT for a pass-through entity ([Division BAIT page](https://www.nj.gov/treasury/taxation/baitpte/index.shtml); [BAIT FAQ](https://www.nj.gov/treasury/taxation/baitpte/baitpte-faq.shtml); [2026 PTE-100 instructions](https://www.nj.gov/treasury/taxation/pdf/current/pte-bait/pte100instr.pdf))

1. **Eligibility.** Partnerships, **New Jersey** S corporations, and LLCs classified as a partnership or S corporation, with **at least one member who is an individual, estate or trust** liable for New Jersey gross income tax on their share. Single-member LLCs and sole proprietorships cannot elect. A federal S corporation filing in New Jersey as a C corporation is not a New Jersey S corporation.
2. **Election.** Register with the Division of Revenue and Enterprise Services, then elect **electronically, every year**, by the **original due date** of Form PTE-100 (15 March for a calendar year) and before filing the return. An extension of the return does not extend the election; if it is not made by the original due date, the PTE-100 will not be accepted. It cannot be made retroactively, and it must be in place **before any payment**, including estimated payments, is accepted. Elections do not carry forward. The entity can revoke electronically by the same original due date.
3. **Base.** Tax is on the **sum of every member's share of distributive proceeds**, including tax-exempt members:
   - partnership: resident individual, estate and trust members on **all** their income; all other members (nonresidents, corporations, other entities) on New Jersey source income only;
   - S corporation: shareholders on New Jersey source income only.
   - Shares follow the entity's NJ-1065 or CBT-100S, including the add-back of the BAIT deducted federally. If the entity has an overall loss, no BAIT is due, but the PTE-100 is still filed.
4. **Rate.** Apply the brackets (table below) to the **aggregate** base, not member by member. No credits reduce BAIT.
5. **Share out.** Each member with a positive share gets tax in proportion to their share of the total (negative shares are added back first for this step). Report it on Schedule PTE-K-1.

### Step 9: the owner's side ([Division BAIT page](https://www.nj.gov/treasury/taxation/baitpte/index.shtml); [BAIT FAQ](https://www.nj.gov/treasury/taxation/baitpte/baitpte-faq.shtml); [2025 NJ-1040 instructions](https://www.nj.gov/treasury/taxation/pdf/current/1040i.pdf))

- **Individuals, estates, trusts:** the share of BAIT is a **refundable** credit on NJ-1040, NJ-1040NR or NJ-1041. On the 2025 NJ-1040 it goes on line 63 through Schedule NJ-BUS-1, with Schedule PTE-K-1 enclosed. Residents of an S corporation still owe tax on its non-New Jersey income, and owners may still need NJ-1040-ES payments for other income.
- **Nonresident owners** still file a nonresident return if they meet the gross income tax filing threshold. From 2022 a partnership need not remit nonresident partner tax for a partner who reasonably expects a full refund of it from their BAIT credit.
- **Composite returns:** electing BAIT **does not prevent** a composite return (NJ-1080-C) for qualifying nonresident members who elect in. The composite return has a line for their share of BAIT. Composite payments cannot be moved to the BAIT account, or the reverse.
- **C corporation members:** the share stays in entire net income. The BAIT credit (N.J.S.A. 54:10A-5.43) is refundable from 2022 but cannot reduce CBT below the minimum tax; tax credits cannot be used against the Corporate Transit Fee.
- **S corporation members:** refundable credit against regular and minimum tax. **Exempt corporations** (N.J.S.A. 54:10A-3) claim a refund on Form A-3730.
- **Tiered entities:** an upper-tier partnership or S corporation can claim the credit on its own return, pass it to its individual, estate or trust owners, or use it on its own PTE-100. The Division's BAIT page allows a partnership to pass it through only if its partners are all individuals, estates or trusts. Tax remitted for it by a lower tier that did **not** elect BAIT cannot be credited against its BAIT.
- **Resident credit for another state's PTET:** a resident may take the Schedule NJ-COJ credit for a pass-through entity tax paid by a partnership or New Jersey S corporation to another state, D.C. or a political subdivision, if it is **substantially similar** to BAIT and is on income derived there that New Jersey also taxes. The credit cannot exceed what would have been allowed had the income been taxed to the individual. The Division's list includes New York's (Tax Law §862) and New York City's. Keep the entity's statement of the owner's share of income and tax.
- **Federal effect:** a state income tax imposed on and paid by the partnership or S corporation is deducted at entity level, outside the owner's SALT cap ([IRS Notice 2020-75](https://www.irs.gov/pub/irs-drop/n-20-75.pdf)). The **us-pte-state-matrix** skill has the cap figures.

### Rates, bands and thresholds

#### CBT ([CBT-100 instructions (2025)](https://www.nj.gov/treasury/taxation/pdf/current/cbt/cbt100ins.pdf); [CBT-100S instructions (2025)](https://www.nj.gov/treasury/taxation/pdf/current/cbt/cbt100sins.pdf); [Corporate Transit Fee notice](https://www.nj.gov/treasury/taxation/cbt/corporatetransitfee.shtml))

The 2025 instructions are the latest published. The statutory rates, the minimum tax and the fee have no change announced for 2026 ([New laws summary](https://www.nj.gov/treasury/taxation/newlegislation.shtml)), so the same figures apply to 2026 unless the 2026 instructions say otherwise.

| Item | Rate, 2025 and 2026 | Source |
|---|---|---|
| Tax base $50,000 or less | 6.5% of the whole base | [CBT-100 instructions (2025), page 1 line 2a](https://www.nj.gov/treasury/taxation/pdf/current/cbt/cbt100ins.pdf) |
| More than $50,000, not more than $100,000 | 7.5% of the whole base | same |
| More than $100,000 | 9% of the whole base | same |
| Corporate Transit Fee (periods beginning 2024 through 2028) | 2.5% of all taxable net income, if it is over $10 million | [CBT-100 instructions (2025), line 5](https://www.nj.gov/treasury/taxation/pdf/current/cbt/cbt100ins.pdf) |

**Minimum tax, separate filers (C corporations)**

| New Jersey gross receipts | Minimum tax amount | Source |
|---|---|---|
| Less than $100,000 | $500 | [CBT-100 instructions (2025), line 2b](https://www.nj.gov/treasury/taxation/pdf/current/cbt/cbt100ins.pdf) |
| $100,000 or more but less than $250,000 | $750 | same |
| $250,000 or more but less than $500,000 | $1,000 | same |
| $500,000 or more but less than $1,000,000 | $1,500 | same |
| $1,000,000 or more | $2,000 | same |
| Member of an affiliated or controlled group (IRC §1504 or §1563) with total group payroll of $5,000,000 or more | $2,000, whatever its receipts | same |

**Minimum tax, New Jersey S corporations (CBT-100S)**

| New Jersey gross receipts | Minimum tax amount | Source |
|---|---|---|
| Less than $100,000 | $375 | [CBT-100S instructions (2025)](https://www.nj.gov/treasury/taxation/pdf/current/cbt/cbt100sins.pdf) |
| $100,000 or more but less than $250,000 | $562 | same |
| $250,000 or more but less than $500,000 | $750 | same |
| $500,000 or more but less than $1,000,000 | $1,125 | same |
| $1,000,000 or more | $1,500 | same |
| Member of an affiliated or controlled group with total payroll of $5,000,000 or more | $2,000 | same |

- Payroll means the whole affiliated or controlled group's payroll, not New Jersey payroll. For a period shorter than 12 months, the higher minimum applies if prorated payroll exceeds **$416,667** a month. The minimum tax itself is not prorated.
- **Combined groups:** each member **with nexus** pays a **$2,000** minimum tax, whatever its receipts. Members without nexus, disregarded entities and partnerships pay none as members ([TB-86(R)](https://www.nj.gov/treasury/taxation/pdf/pubs/tb/tb86r.pdf); [CBT-100U instructions (2025)](https://www.nj.gov/treasury/taxation/pdf/current/cbt/cbt100uins.pdf)).
- **New Jersey S corporations** pay tax at the CBT rates only on income subject to federal corporate income tax; otherwise only the minimum tax applies. For privilege periods beginning on or after 22 December 2022 a federal S corporation can file as a New Jersey S corporation without a prior New Jersey election, by submitting the shareholder jurisdictional consent and proof of federal S status ([CBT-100S instructions (2025)](https://www.nj.gov/treasury/taxation/pdf/current/cbt/cbt100sins.pdf)).

#### BAIT ([2026 PTE-100 instructions](https://www.nj.gov/treasury/taxation/pdf/current/pte-bait/pte100instr.pdf); [2025 PTE-100 instructions](https://www.nj.gov/treasury/taxation/pdf/other_forms/pte/2025/pte100instr.pdf); [2021 PTE-100 instructions](https://www.nj.gov/treasury/taxation/pdf/other_forms/pte/2021/pte100instr.pdf))

The brackets are the same for 2025 and 2026. Tax = distributive proceeds × rate − subtraction.

| Distributive proceeds (line 1) | Rate | Subtract | Source |
|---|---|---|---|
| Over $0, not over $250,000 | 5.675% | $0 | [2026 PTE-100 instructions, tax computation](https://www.nj.gov/treasury/taxation/pdf/current/pte-bait/pte100instr.pdf) |
| Over $250,000, not over $1,000,000 | 6.52% | $2,112.50 | same |
| $1,000,000 and over | 10.9% | $45,912.50 | same |

- The subtraction amounts make the table work like marginal brackets: 5.675% on the first $250,000, 6.52% on the next $750,000, and 10.9% above $1,000,000.
- **Before 2022** (2020 and 2021) there were four bands: 9.12% from $1,000,000 to $5,000,000 and 10.9% only above $5,000,000. Do not use the 9.12% band for 2022 or later.
- **Estimated BAIT** is required if the entity expects to owe more than **$400**. Four payments of **25%** each ([PTE-150 instructions (2025 and 2027 editions)](https://www.nj.gov/treasury/taxation/pdf/current/pte-bait/pte150instr.pdf); [Division BAIT page](https://www.nj.gov/treasury/taxation/baitpte/index.shtml)).

## Boundary and exception table

| Situation | Rule | Source |
|---|---|---|
| Tax base exactly $100,000 | 7.5% on all of it; 9% needs **more than** $100,000 | [CBT-100 instructions](https://www.nj.gov/treasury/taxation/pdf/current/cbt/cbt100ins.pdf) |
| Tax base $100,001 | 9% on the whole base: the rates are not marginal | same |
| Taxable net income exactly $10,000,000 | No Corporate Transit Fee: it must be **over** $10 million | [Transit Fee notice](https://www.nj.gov/treasury/taxation/cbt/corporatetransitfee.shtml) |
| Taxable net income $10,000,001 | Fee is 2.5% of the whole amount | [CBT-100 instructions](https://www.nj.gov/treasury/taxation/pdf/current/cbt/cbt100ins.pdf) |
| Allocated income $14,000,000, NOLs bring taxable net income to $8,000,000 | No fee: the test is after NOLs | same |
| Remote seller with $100,000 of New Jersey receipts and 150 transactions | No bright-line nexus: neither test is met (receipts must be **more than** $100,000, **or** transactions 200 or more) | [TB-108(R)](https://www.nj.gov/treasury/taxation/pdf/pubs/tb/tb108.pdf) |
| Prior-year CBT liability exactly $1,500 | Installments not required; may instead pay 50% of that liability with the prior-year return | [CBT-100 instructions](https://www.nj.gov/treasury/taxation/pdf/current/cbt/cbt100ins.pdf) |
| Extension paid at 85% of the final tax | Extension denied retroactively; penalties and interest from the original due date | [CBT-200-T instructions](https://www.nj.gov/treasury/taxation/pdf/current/cbt/cbt-200-t.pdf) |
| BAIT election attempted with the extended PTE-100 | Too late: the original due date is the deadline | [2026 PTE-100 instructions](https://www.nj.gov/treasury/taxation/pdf/current/pte-bait/pte100instr.pdf) |
| Estimated BAIT paid before the election is filed | Not accepted: elect first | [Division BAIT page](https://www.nj.gov/treasury/taxation/baitpte/index.shtml) |
| Partnership with an overall loss but some profitable partners | No BAIT; cannot pay for some partners only; still file PTE-100 | [BAIT FAQ](https://www.nj.gov/treasury/taxation/baitpte/baitpte-faq.shtml) |
| Nonresident member in the composite return | Allowed; BAIT credited on the composite return | [Division BAIT page](https://www.nj.gov/treasury/taxation/baitpte/index.shtml) |
| First year of BAIT, all tax paid with the PTE-100 | No estimated tax penalty under the safe harbor; members get credit as if paid evenly | [BAIT FAQ](https://www.nj.gov/treasury/taxation/baitpte/baitpte-faq.shtml) |
| Group elected world-wide in 2023, wants water's-edge for 2026 | Bound through 2028 unless the Director allows a prospective revocation for reasonable cause | [TB-109](https://www.nj.gov/treasury/taxation/pdf/pubs/tb/tb109.pdf) |

## Worked cases

All amounts are hypothetical. Rates and thresholds come from the tables above.

### Case 1: a small New Jersey-only C corporation, 2026 ([CBT-100 instructions (2025)](https://www.nj.gov/treasury/taxation/pdf/current/cbt/cbt100ins.pdf); [CBT-150 instructions (2026)](https://www.nj.gov/treasury/taxation/pdf/current/cbt/cbt150ins.pdf))

- Facts: calendar 2026, all receipts in New Jersey, tax base $80,000, New Jersey gross receipts $1,200,000, not in an affiliated or controlled group. Its 2025 total liability was $5,000.
- Rate: $80,000 is more than $50,000 and not more than $100,000, so 7.5% × $80,000 = **$6,000**.
- Minimum tax: receipts of $1,000,000 or more give $2,000. The tax is the greater: **$6,000**. No fee (far below $10 million).
- Estimated tax for 2026: the 2025 liability of $5,000 is more than $1,500, so four 25% installments were due 15 April, 15 June, 15 September and 15 December 2026. Paying $1,250 each (100% of the 2025 liability) avoids underpayment interest, because a taxpayer is underpaid only if payments are less than 90% of the current year's liability **and** less than 100% of the prior year's.
- Return: 15 May 2027 falls on a Saturday, so it is due Monday 17 May 2027.

```oa-check
name: NJ CBT 2026, small separate filer, rate tax against minimum tax
inputs:
  tax_base: 80000
  minimum_tax: 2000
  prior_year_liability: 5000
steps:
  - rate_tax: tax_base * 0.075
  - cbt: max(rate_tax, minimum_tax)
  - installment: prior_year_liability * 0.25
expected:
  rate_tax: 6000.00
  cbt: 6000.00
  installment: 1250.00
```

### Case 2: the $100,000 line ([CBT-100 instructions (2025)](https://www.nj.gov/treasury/taxation/pdf/current/cbt/cbt100ins.pdf))

- Tax base $100,000: 7.5% × $100,000 = $7,500.
- Tax base $100,001: 9% × $100,001 = $9,000.09. One more dollar of income adds $1,500.09 of tax. Check year-end accruals near the line.

### Case 3: a combined group over $10 million, 2026 ([CBT-100U instructions (2025)](https://www.nj.gov/treasury/taxation/pdf/current/cbt/cbt100uins.pdf); [Transit Fee notice](https://www.nj.gov/treasury/taxation/cbt/corporatetransitfee.shtml))

- Facts: water's-edge group, three members with New Jersey nexus. Group taxable net income (after allocation and NOLs) $12,000,000. A $100,000 tax credit is available.
- CBT: 9% × $12,000,000 = $1,080,000. Minimum tax: 3 × $2,000 = $6,000, which is lower. CBT after the credit: $1,080,000 − $100,000 = $980,000.
- Fee: $12,000,000 is over $10 million, so 2.5% × $12,000,000 = **$300,000**, on the whole amount. The credit cannot be used against it.
- Total: $980,000 + $300,000 = **$1,280,000**.
- If NOLs had brought taxable net income down to $10,000,000, there would be no fee.

```oa-check
name: NJ combined group 2026, CBT plus Corporate Transit Fee
inputs:
  taxable_net_income: 12000000
  members_with_nexus: 3
  credits: 100000
steps:
  - rate_tax: taxable_net_income * 0.09
  - minimum: members_with_nexus * 2000
  - cbt_after_credits: max(rate_tax, minimum) - credits
  - transit_fee: taxable_net_income * 0.025
  - total: cbt_after_credits + transit_fee
expected:
  cbt_after_credits: 980000.00
  transit_fee: 300000.00
  total: 1280000.00
```

### Case 4: PNOLs, NOLs and the 80% limit, 2026 ([CBT-100 instructions (2025)](https://www.nj.gov/treasury/taxation/pdf/current/cbt/cbt100ins.pdf); [Worksheet 500-P](https://www.nj.gov/treasury/taxation/pdf/current/cbt/500-p.pdf))

- Facts: separate filer. Allocated entire net income before NOLs (line 19) $5,000,000. Converted PNOL $1,000,000 (a pre-2019 carryover of $4,000,000 × a 2018 allocation factor of 25%). Post-allocation NOL of $6,000,000 from a period beginning after 31 July 2023.
- PNOL first: $5,000,000 − $1,000,000 = $4,000,000.
- NOL limited to 80% × $4,000,000 = $3,200,000.
- Taxable net income: $4,000,000 − $3,200,000 = **$800,000**; tax at 9% × $800,000 = **$72,000**. NOL carried forward: $6,000,000 − $3,200,000 = $2,800,000.

### Case 5: a BAIT partnership with mixed owners, 2026 ([2026 PTE-100 instructions](https://www.nj.gov/treasury/taxation/pdf/current/pte-bait/pte100instr.pdf); [BAIT FAQ](https://www.nj.gov/treasury/taxation/baitpte/baitpte-faq.shtml))

- Facts: calendar 2026 partnership, elected BAIT before its first 2026 estimated payment (15 April 2026), and in any case no later than 15 March 2027. Partner A, a New Jersey resident individual: share of all income $700,000. Partner B, a New York resident individual: New Jersey source share $400,000. Partner C, a corporation: New Jersey source share $100,000.
- Base: $700,000 + $400,000 + $100,000 = $1,200,000.
- Tax: $1,000,000 and over, so 10.9% × $1,200,000 − $45,912.50 = $130,800 − $45,912.50 = **$84,887.50**.
- Shares: A 7/12 = $49,517.71; B 1/3 = $28,295.83; C 1/12 = $7,073.96.
- A claims $49,517.71 as a refundable credit on the NJ-1040. B files an NJ-1040NR (or joins a composite return) and claims $28,295.83; the partnership need not remit nonresident tax for B if B reasonably expects a full refund of it. C claims $7,073.96 against CBT, but not below its minimum tax.
- Estimated BAIT: 25% of $84,887.50 = $21,221.88 (rounded) on 15 April, 15 June and 15 September 2026 and 15 January 2027. Return PTE-100 due 15 March 2027.

```oa-check
name: NJ BAIT 2026, partnership with mixed owners
inputs:
  share_a: 700000
  share_b: 400000
  share_c: 100000
steps:
  - base: share_a + share_b + share_c
  - bait: base * 0.109 - 45912.50
  - credit_a: round(bait * share_a / base, 2)
  - credit_b: round(bait * share_b / base, 2)
  - credit_c: round(bait * share_c / base, 2)
  - quarterly: round(bait * 0.25, 2)
expected:
  bait: 84887.50
  credit_a: 49517.71
  credit_b: 28295.83
  credit_c: 7073.96
  quarterly: 21221.88
```

### Case 6: a New Jersey resident in a New York PTET partnership ([BAIT FAQ](https://www.nj.gov/treasury/taxation/baitpte/baitpte-faq.shtml); [2025 NJ-1040 instructions](https://www.nj.gov/treasury/taxation/pdf/current/1040i.pdf))

- A New Jersey resident's New York partnership elects the New York pass-through entity tax (Tax Law §862), which is on the Division's list of taxes substantially similar to BAIT.
- The resident claims the Schedule NJ-COJ credit for their share of that tax on New York-derived income that New Jersey also taxes, capped at what would have been allowed had the income been taxed to them, with the usual NJ-COJ limit. Keep the partnership's statement of their share of the income and the tax.

### Case 7: election timing ([2026 PTE-100 instructions](https://www.nj.gov/treasury/taxation/pdf/current/pte-bait/pte100instr.pdf); [2025 PTE-100 instructions](https://www.nj.gov/treasury/taxation/pdf/other_forms/pte/2025/pte100instr.pdf))

- In September 2026 a calendar-year S corporation asks to elect BAIT for 2025. It is too late: the 2025 election had to be made electronically before the original due date of the 2025 PTE-100 (16 March 2026). It cannot be made retroactively or with an extension.
- It can still elect for 2026 (by 15 March 2027), and must elect before making any 2026 estimated payment. It must be a New Jersey S corporation (files CBT-100S), and the base is New Jersey source income only.

## When to refuse or refer

- Banking or financial business corporations, insurers, public utilities, REITs, RICs, investment companies, casino licensees (TB-117) and cannabis licensees.
- Group composition (unitary status, foreign members, captives, members joining or leaving; TB-95(R), TB-102(R)), and choosing or revoking a world-wide or affiliated group election.
- Rebuilding a PNOL pool or disputing a 500-P conversion; ownership changes and section 382; debt cancellation adjustments.
- P.L. 86-272 positions resting on website or app activity; nexus questionnaires and voluntary disclosure.
- Multi-tier NCTI and dividend exclusion computations.
- BAIT for tiered structures, part-year residents, hedge fund status or consolidated PTE returns (N.J.S.A. 54A:12-3(c)), and whether to elect when many owners are tax-exempt or corporate.
- The Corporate Transit Fee for any period beginning after 31 December 2028, until the law is confirmed.

## Filing and payment

### CBT ([CBT-100 instructions (2025)](https://www.nj.gov/treasury/taxation/pdf/current/cbt/cbt100ins.pdf); [CBT-150 instructions (2026)](https://www.nj.gov/treasury/taxation/pdf/current/cbt/cbt150ins.pdf); [CBT-200-T instructions](https://www.nj.gov/treasury/taxation/pdf/current/cbt/cbt-200-t.pdf))

- **Electronic filing and payment are mandatory** for all CBT returns, estimated payments, extensions and vouchers.
- **Return due date:** the 15th day of the month **after** the month the federal corporate return is originally due. For a calendar year, 15 May. If that is a weekend or legal holiday, the next business day. Combined groups file one CBT-100U through the managerial member.
- **Extension (CBT-200-T):** six months to file, not to pay. File it by the original due date and pay at least **90%** of the tax shown on the return when filed. If either test fails, or the return is not filed by the extended date, the extension is retroactively denied and penalties and interest run from the original due date.
- **Estimated tax (CBT-150), 2026:**
  - Required if the prior year's total tax liability is **more than $1,500**. For a combined group the test is $1,500 multiplied by the number of members on the combined return, and the managerial member pays. Total tax liability includes the Corporate Transit Fee (CBT-100 line 6 is line 4 plus line 5). Four installments of **25%** on the 15th day of the 4th, 6th, 9th and 12th months (for a calendar year: 15 April, 15 June, 15 September, 15 December).
  - Taxpayers with prior-period gross receipts of **$50,000,000 or more** pay **25%** in the 4th month, **50%** in the 6th month and **25%** in the 12th month.
  - Prior year liability of **$1,500 or less** (for a group, not more than $1,500 per member): installments, or instead one payment of **50%** of the prior year's liability, made with the prior year's return by its original due date (entered on the return's installment line).
  - Underpaid if total estimates are less than **90%** of the current year's liability **and** less than **100%** of the prior year's. Interest on the underpayment is computed on Form CBT-160-A or CBT-160-B.
- **Penalties and interest:**
  - Late filing: **5%** a month or part month, up to **25%** of the underpayment; if no return is filed within 30 days of the first delinquency notice, 5% a month of the total liability up to 25%. A **$100** penalty for each month the return is late may also apply.
  - Late payment: **5%** of the balance paid after the due date.
  - Extension insufficiency: 5% a month up to 25% of the shortfall.
  - Interest: **3%** above the average predominant prime rate, for each month or part month, compounded annually.
- **Federal changes** to taxable income must be reported to the Division within 90 days.

### BAIT ([2026 PTE-100 instructions](https://www.nj.gov/treasury/taxation/pdf/current/pte-bait/pte100instr.pdf); [Division BAIT page](https://www.nj.gov/treasury/taxation/baitpte/index.shtml))

- **Election:** electronic, annual, by the original due date of the PTE-100 and before any payment. Revocation by the same date.
- **Estimated payments (PTE-150):** required if the entity expects to owe more than **$400**. Four payments of **25%** on the 15th day of the 4th, 6th and 9th months of the year and the 1st month of the next year (calendar year: 15 April, 15 June, 15 September, 15 January). Underpaid if estimates are less than **80%** of the current year's tax or less than **100%** of the prior year's; interest on Form PTE-160 ([2025 PTE-150 instructions](https://www.nj.gov/treasury/taxation/pdf/other_forms/pte/2025/pte150instr.pdf)). That is the PTE-150 wording ("or"). The CBT test uses "and", and the BAIT FAQ points to the safe harbor in N.J.S.A. 54A:9-6, which the **nj-income-tax** skill describes as the lesser of the two amounts. Until the Division confirms which applies, pay at least the larger of **80%** of this year's BAIT and **100%** of last year's ([BAIT FAQ](https://www.nj.gov/treasury/taxation/baitpte/baitpte-faq.shtml)). BAIT estimates cannot be moved to another tax account.
- **Return:** Form PTE-100 with Schedule PTE-K-1 for every member, due the 15th day of the 3rd month after year end (calendar 2026: 15 March 2027). All filings and payments are electronic; paper is not accepted.
- **Extension (PTE-200-T):** six months to file, if filed by the original due date and at least **80%** of the tax is paid by then. No extension to pay.
- **Penalties:** late filing **5%** a month up to **25%**, and a penalty of **$100** for each month or part month may be imposed; late payment **5%**; interest **3%** above prime, compounded annually. The Division has three years from the later of filing and the original due date to assess, with no limit if no return or a fraudulent one was filed.
- **Members** must be given Schedule PTE-K-1. An amended PTE-K-1 cannot report less than the original.

### 2025 returns, dated section ([CBT-100 instructions (2025)](https://www.nj.gov/treasury/taxation/pdf/current/cbt/cbt100ins.pdf); [2025 PTE-100 instructions](https://www.nj.gov/treasury/taxation/pdf/other_forms/pte/2025/pte100instr.pdf))

- **CBT:** use the 2025 forms for accounting periods ending 31 July 2025 through 30 June 2026. A calendar 2025 return was due **15 May 2026**. With a valid CBT-200-T (filed on time with at least 90% of the tax paid), it is due six months later: 15 November 2026 is a Sunday, so file by Monday 16 November 2026. The rates, minimum tax and fee are as in the tables; the fee applies because 2025 periods begin on or after 1 January 2024.
- **Estimated tax for 2026** depended on the 2025 total liability (more than $1,500: installments; $1,500 or less: installments or 50% of the 2025 liability with the 2025 return).
- **BAIT:** the calendar 2025 PTE-100 was due **16 March 2026**. With a timely PTE-200-T (at least 80% of the tax paid) the return may be filed within six months. The 2025 election window has closed.

## Completion checklist

Sources: [CBT-100 instructions (2025)](https://www.nj.gov/treasury/taxation/pdf/current/cbt/cbt100ins.pdf); [2026 PTE-100 instructions](https://www.nj.gov/treasury/taxation/pdf/current/pte-bait/pte100instr.pdf).

- [ ] Nexus tested: physical presence, receipts more than $100,000 or 200 or more transactions, and P.L. 86-272 (box checked if claimed).
- [ ] Combined group decided: more than 50% common ownership, unitary, filing method and binding period recorded, managerial member registered.
- [ ] Entire net income built; NCTI and dividend exclusion with the 5% clawback; single sales factor to six decimals.
- [ ] PNOLs converted on 500-P and used before NOLs; 80% limit applied to post-July 2023 NOLs; 20-period expiry tracked.
- [ ] Rate set on the whole base (6.5% / 7.5% / 9%); short-period proration checked; minimum tax compared (per member with nexus in a group).
- [ ] Corporate Transit Fee: taxable net income over $10 million tested after NOLs, 2.5% on the whole amount, no credits against it.
- [ ] Estimated tax pattern chosen ($1,500 test, per member for a group, fee included; $50,000,000 receipts test); extension with 90% paid; return by the 15th of the month after the federal due date; all electronic.
- [ ] BAIT: eligibility (at least one individual, estate or trust member; New Jersey S status), election made by the original due date before any payment, base built by member type, brackets applied to the aggregate, estimates if more than $400, PTE-K-1s issued.
- [ ] Owners: BAIT credit on NJ-BUS-1 and line 63; nonresident filing and composite decided; Schedule NJ-COJ for substantially similar other-state PTET with the entity's statement.

## Sources

| Source | URL | Read on |
|---|---|---|
| CBT-100 instructions (2025, periods ending 31 July 2025 to 30 June 2026); read for nexus, rates on line 2a, short-period proration, minimum tax on line 2b, Corporate Transit Fee on line 5, NOL and PNOL, dividend exclusion, filing and penalties | https://www.nj.gov/treasury/taxation/pdf/current/cbt/cbt100ins.pdf | 2026-11-14 |
| CBT-100U instructions (2025); read for combined groups, filing methods, Finnigan, group P.L. 86-272 and NOL rules | https://www.nj.gov/treasury/taxation/pdf/current/cbt/cbt100uins.pdf | 2026-11-14 |
| CBT-100S instructions (2025); read for the S corporation minimum tax table and New Jersey S status | https://www.nj.gov/treasury/taxation/pdf/current/cbt/cbt100sins.pdf | 2026-11-14 |
| CBT-150 instructions (2026); read for the USD 1,500 test, 25% installments, the USD 50 million pattern, 90% and 100% tests | https://www.nj.gov/treasury/taxation/pdf/current/cbt/cbt150ins.pdf | 2026-11-14 |
| CBT-200-T instructions; read for the 90% extension rule | https://www.nj.gov/treasury/taxation/pdf/current/cbt/cbt-200-t.pdf | 2026-11-14 |
| Worksheet 500-P; read for the PNOL conversion | https://www.nj.gov/treasury/taxation/pdf/current/cbt/500-p.pdf | 2026-11-14 |
| TB-108(R); read for bright-line nexus and P.L. 86-272 internet activities | https://www.nj.gov/treasury/taxation/pdf/pubs/tb/tb108.pdf | 2026-11-14 |
| TB-110(R); read for the dividend exclusion and 5% clawback | https://www.nj.gov/treasury/taxation/pdf/pubs/tb/tb110.pdf | 2026-11-14 |
| TB-109; read for the binding period of the world-wide and affiliated group elections | https://www.nj.gov/treasury/taxation/pdf/pubs/tb/tb109.pdf | 2026-11-14 |
| TB-86(R); read for the per-member minimum tax in combined groups | https://www.nj.gov/treasury/taxation/pdf/pubs/tb/tb86r.pdf | 2026-11-14 |
| Division Corporate Transit Fee notice; read for P.L. 2024, c.20, periods and exclusions | https://www.nj.gov/treasury/taxation/cbt/corporatetransitfee.shtml | 2026-11-14 |
| Division notice on combined group P.L. 86-272 revision; read for the pre-July 2023 member test | https://www.nj.gov/treasury/taxation/cbt/combinedgroupsrevision.shtml | 2026-11-14 |
| Division notice on federal renaming of GILTI and FDII; read for NCTI and FDDEI treatment | https://www.nj.gov/treasury/taxation/cbt/obbba-gilti-fdii-renaming.shtml | 2026-11-14 |
| Division nexus page; read for marketplace warehouse inventory | https://www.nj.gov/treasury/taxation/organization/audit-taxtype-nexus.shtml | 2026-11-14 |
| Division new laws page; read for the Corporate Transit Fee summary and 2025 to 2026 law changes | https://www.nj.gov/treasury/taxation/newlegislation.shtml | 2026-11-14 |
| 2026 PTE-100 instructions; read for eligibility, election timing, the 15 March 2027 due date, brackets and the 80% extension rule | https://www.nj.gov/treasury/taxation/pdf/current/pte-bait/pte100instr.pdf | 2026-11-14 |
| 2025 PTE-100 instructions; read for the 2025 election window and 16 March 2026 due date | https://www.nj.gov/treasury/taxation/pdf/other_forms/pte/2025/pte100instr.pdf | 2026-11-14 |
| 2021 PTE-100 instructions; read for the pre-2022 four-band table | https://www.nj.gov/treasury/taxation/pdf/other_forms/pte/2021/pte100instr.pdf | 2026-11-14 |
| PTE-150 instructions (current edition headed 2027; 2025 edition); read for the USD 400 test, 25% installments and the 80% or 100% wording | https://www.nj.gov/treasury/taxation/pdf/current/pte-bait/pte150instr.pdf | 2026-11-14 |
| Division BAIT page; read for eligibility, the rate table, sourcing and the election before payments | https://www.nj.gov/treasury/taxation/baitpte/index.shtml | 2026-11-14 |
| Division BAIT FAQ; read for losses, tiered entities, the first-year safe harbor and other-state PTET credits | https://www.nj.gov/treasury/taxation/baitpte/baitpte-faq.shtml | 2026-11-14 |
| 2025 Form NJ-1040 instructions; read for line 63 and Schedule NJ-COJ | https://www.nj.gov/treasury/taxation/pdf/current/1040i.pdf | 2026-11-14 |
| IRS Notice 2020-75; read for entity-level deduction of state pass-through taxes | https://www.irs.gov/pub/irs-drop/n-20-75.pdf | 2026-11-14 |

Not yet confirmed: the 2026 CBT-100, CBT-100U and CBT-100S instructions (not published on 2026-11-14; the 2025 set is used, and the rates, minimum tax and fee are statutory and unchanged on the Division's new laws page); any extension of the Corporate Transit Fee past privilege periods beginning 31 December 2028; whether the 50% dividend exclusion needs "at least 50%" (CBT-100 instructions) or "more than 50%" (TB-110(R)) ownership; which BAIT estimated tax safe harbor applies (PTE-150 says 80% of this year or 100% of last year with "or"; the BAIT FAQ points to N.J.S.A. 54A:9-6); the 2026 prime rate for interest.
