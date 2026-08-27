---
name: ca-formation
description: Tier 2 California content skill for entity formation covering tax year 2025. Includes the CA LLC Form LLC-1 $70 filing fee, $800 annual minimum franchise tax under R&TC §17941 (first-year exemption AB 85/SB 818 expired 2024), tiered LLC fee on gross receipts under §17942 (Form 3536), 15-day rule for short first year, Statement of Information LLC-12, the "doing business in CA" threshold of $711,538 receipts / $71,154 payroll / $71,154 property triggering registration obligations for out-of-state entities, foreign qualification mechanics, and the C-corp formation overlay with $800 + 8.84% income tax.
jurisdiction: US-CA
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# CA Formation

## Scope (frontmatter blockquote)

**Scope.** This skill covers the mechanics of forming or registering a business entity in California for tax year 2025. It is opinionated toward freelancers, founders, and small-business owners who are either (a) physically located in California and forming a domestic entity, or (b) located out-of-state but conducting business in California in a way that triggers the foreign-qualification or "doing business in California" tests. The skill produces reviewer-ready filings and a structured fee-and-deadline schedule. It MUST be loaded alongside `us-tax-workflow-base v0.2` or later and, where relevant, `ca-540-individual-return`, `ca-smllc-form-568`, and `ca-llc-fee-and-tax`. **Federal entity classification (default disregarded SMLLC versus federal corporation versus federal S election) is delegated to `us-s-corp-election-decision`; this skill addresses the California overlay only.** All citations are to the California Revenue and Taxation Code (R&TC), the California Corporations Code (Corp. Code), the California Secretary of State (SOS) filing requirements, and the Franchise Tax Board (FTB) instructions current as of the `last_updated` date above. Statutes change. A credentialed reviewer (Enrolled Agent, CPA, or attorney) must sign off before any output is delivered.

## 1. Why California is Different

California is the most aggressive state in the United States with respect to (a) defining what constitutes "doing business" within its borders, (b) imposing an $800 minimum annual franchise tax that applies regardless of profit or activity level, and (c) imposing a separate gross-receipts-based LLC fee that is independent of net income. The combination of these three rules creates a structural fee floor that is unique among US states and is the single largest source of compliance failure for out-of-state founders who do business with California customers.

The practical reality is this: if you have any meaningful nexus to California — a customer base, an employee, a physical presence, an organizing partner, or a domicile — you almost certainly need to register an entity in California or qualify your out-of-state entity to do business in California. The "doing business" threshold under R&TC §23101 is so low ($757,070 in California-sourced receipts for 2025, or just $75,707 in California payroll or property) that any startup with a handful of California customers or a single California-based employee is over the line.

- **Unregistered foreign entity doing business in CA - consequences** — Under Corp. Code §17708.07 (LLCs) and §2203 (corporations), an unregistered foreign entity (1) cannot maintain or defend a civil action in California courts until it has registered and paid all back taxes, fees, and penalties; (2) is subject to a $250-per-year penalty under Corp. Code §17708.07(d); (3) is subject to a $20-per-day penalty under R&TC §19141 capped at $10,000 for failure to file FTB returns; and (4) the FTB will retroactively assess the $800 annual minimum franchise tax for every year the entity was doing business in California, plus interest, plus the LLC fee on gross receipts if applicable.  _(Corp. Code §17708.07; Corp. Code §2203; R&TC §19141)_

**AUDIT FLASH POINT — DE entity not qualifying in CA.** The lost-suit consequence is the most expensive in practice — founders routinely discover the failure when they try to enforce a contract against a California counterparty and find the courthouse door closed until they have written a six-figure cure check to the FTB. **Catch this in intake. Always ask: "Are you registered with the California Secretary of State?" and cross-check against the bizfileOnline search.**

## 2. California LLC Formation Mechanics

### 2.1 Articles of Organization — Form LLC-1

- **Form LLC-1 filing fee (online and paper)** — $70
- **Form LLC-1RES name reservation fee** — $10 USD (reserves name for 60 days)
- **LLC-1 required elements** — 1. Entity name must contain 'Limited Liability Company,' 'LLC,' 'L.L.C.,' or an acceptable abbreviation under Corp. Code §17701.08; must be distinguishable and not contain restricted words without approval. 2. Business address: street address (not P.O. box) preferred in California; foreign-state address permitted if principal place of business is outside California. 3. Agent for service of process: either an individual residing in California with a California street address, or a registered corporate agent that filed Form 1505; a P.O. box is not acceptable under Corp. Code §17701.13. 4. Management structure: member-managed (default) or manager-managed if elected in Articles. 5. Organizer signature: any individual may sign; need not be a member/manager or CA resident.  _(Corp. Code §17701.08; Corp. Code §17701.13)_
- **LLC-1 non-disclosure and federal classification** — The LLC-1 does not require disclosure of the members, the federal tax classification election, or the operating agreement. Federal classification (default disregarded SMLLC, partnership, or C-corporation under the check-the-box regulations) is established through Form 8832 with the IRS and is invisible at the California SOS layer.
- **Filing processing time and expedite fees** — Filing typically processes within 1–5 business days online. Expedited 24-hour ($350 additional) and same-day ($750 additional) processing is available under Government Code §12231.  _(Government Code §12231)_

### 2.2 Statement of Information — Form LLC-12

- **Initial LLC-12 due date** — 90 days after SOS file date of LLC-1
- **LLC-12 filing fee** — $20
- **LLC-12 recurring cadence** — Thereafter the LLC-12 is due biennially (every two years) on or before the end of the calendar month of original formation. (Note: this differs from the corporate Statement of Information, which is annual.)
- **LLC-12 required disclosures** — 1. Names and addresses of all managers (if manager-managed) or all members (if member-managed and LLC has fewer than the threshold number of members triggering full member disclosure under Corp. Code §17702.09). 2. The agent for service of process — name and California street address. 3. The principal office address and the California office address (if different). 4. The chief executive officer (if any). 5. The type of business — a brief description.  _(Corp. Code §17702.09)_
- **Penalty for missed LLC-12** — Failure to file the LLC-12 within 90 days of formation, or failure to file the biennial update, triggers a $250 penalty under R&TC §19141, plus eventual suspension of the LLC's powers, rights, and privileges by the FTB under R&TC §23301.  _(R&TC §19141; R&TC §23301)_

**AUDIT FLASH POINT — Missed Statement of Information.** A suspended LLC cannot enter into contracts, maintain or defend lawsuits, or use its name in California. Reviving a suspended LLC requires filing all delinquent Statements of Information, paying the penalties, paying any unpaid franchise taxes and LLC fees plus interest, and filing Form FTB 3557 to request revivor. The LLC-12 fee is the single cheapest compliance item in the California entity calendar and the most commonly missed.

### 2.3 Registered Agent

- **Registered agent requirement** — California requires every LLC to maintain an agent for service of process within California at all times. The agent is the entity or individual designated to receive lawsuits, subpoenas, FTB notices, and SOS correspondence on behalf of the LLC.
- **Agent options** — 1. Individual agent: any individual aged 18 or older residing in California with a California street address, available during normal business hours to accept service; using a resident member is cheapest but not advised for litigation-sensitive businesses because the home address becomes public record. 2. Commercial registered agent: a corporation that has filed a Form 1505 with the SOS; annual fees range from approximately $100 to $300. Common providers include Northwest Registered Agent, CT Corporation, Cogency Global, and InCorp.
- **Change of agent** — A change of agent requires filing Form LLC-12 (or the standalone Form LLC-12NC, no charge) within the timing requirements.

### 2.4 Operating Agreement

- **Operating agreement requirement** — Under Corp. Code §17701.10, every California LLC is required to have an operating agreement governing its internal affairs. The operating agreement is not filed with the SOS and is not publicly disclosed, but it is legally required to exist.  _(Corp. Code §17701.10)_
- **Operating agreement contents** — The operating agreement governs: member capital contributions, distributions, and allocations; voting rights and decision-making procedures; transfer restrictions on membership interests; dissolution and winding-up procedures; indemnification of members and managers; resolution of disputes among members.
- **SMLLC operating agreement requirement** — A single-member LLC must still have an operating agreement, even though the document effectively binds only the sole member. The federal tax treatment of an SMLLC as a disregarded entity does not eliminate the California operating agreement requirement, because the operating agreement is a corporate-law document, not a tax document. For SMLLCs, a 5–10 page template is sufficient; for multi-member LLCs, the operating agreement is typically 30–60 pages and should be drafted by counsel.

### 2.5 The $800 Minimum Franchise Tax — R&TC §17941

- **$800 minimum franchise tax requirement** — Under R&TC §17941, every LLC organized, registered, or doing business in California must pay an annual minimum franchise tax of $800. The $800 is a fixed amount that applies regardless of whether the LLC has any income, any activity, any employees, or any operations. It is owed in addition to any income tax, the gross-receipts LLC fee under R&TC §17942, and any other California tax.  _(R&TC §17941)_
- **Payment mechanics and due date** — The $800 is paid using Form FTB 3522, LLC Tax Voucher, and is due on or before the 15th day of the 4th month of the LLC's tax year — for calendar-year LLCs, this is April 15 of the current year (i.e., the $800 for 2025 is due April 15, 2025, paid in advance of the year's activity).

#### 2.5.1 The First-Year Exemption (AB 85 / SB 818) — EXPIRED

- **First-year exemption history** — For LLCs formed during the calendar years 2021, 2022, and 2023, California temporarily waived the $800 minimum franchise tax for the entity's first taxable year under Assembly Bill 85 (2020) and Senate Bill 818 (2021). This exemption was codified at R&TC §17941(g)(3).  _(R&TC §17941(g)(3))_
- **Exemption expiration** — This exemption expired on December 31, 2023. LLCs formed on or after January 1, 2024 owe the full $800 in their first taxable year. There is no statutory replacement and no transitional relief. Founders who relied on the first-year exemption in 2023 and have not updated their planning for the 2024+ era are routinely blindsided by the bill.

**AUDIT FLASH POINT — Pre-2024 founders unaware AB 85 expired.** The most common form of this error: a founder formed an LLC in 2023 and paid no $800 for 2023 (correctly, under AB 85). They then form a second LLC in 2024 or 2025 and assume the same first-year waiver applies. It does not. The 2024 LLC owes $800 by April 15, 2024 (or 2025 for a 2025-formed LLC); failure to pay generates interest under R&TC §19101 and a late-payment penalty under R&TC §19132 of 5% per month up to 25% of the unpaid tax. **Confirm the formation year in intake and the year-by-year payment status.**

#### 2.5.2 The 15-Day Rule

- **15-day rule mechanics** — Under R&TC §17946 and §23153(d), an LLC (or corporation) that (a) is formed in the last 15 days of its taxable year and (b) conducts no business during those 15 days owes $0 for that short taxable year. The $800 is owed for the following year as the first full year.  _(R&TC §17946; R&TC §23153(d))_
- **Calendar-year definition of last 15 days** — For a calendar-year entity, "the last 15 days" means December 17 through December 31 inclusive. An LLC organized on December 16 or earlier does not qualify; an LLC organized on December 17 or later does qualify provided it conducts no business in the residual days.
- **'Conducts no business' interpretation** — "Conducts no business" is interpreted strictly. Opening a bank account in the entity name, signing a contract in the entity name, receiving any payment, paying any expense (other than the SOS formation fee), or any other revenue-generating or operational activity disqualifies the entity from the 15-day rule. The safest interpretation: file the LLC-1 on or after December 17 and do absolutely nothing else in the entity until January 2 of the following year.
- **15-day rule scope** — The 15-day rule is purely a question of timing; it is not affected by AB 85 expiration. It is the only remaining mechanism by which a California LLC can avoid the $800 for its formation year.

**AUDIT FLASH POINT — Missing the 15-day rule.** If a founder intends to form an LLC in late December but files on December 14 or December 15, they have crossed back into the regular first-year regime and owe $800 for that year (and another $800 by April 15 of the following year, only 4 months later). For clients forming entities near year-end, **always confirm the SOS file date and recommend deferring to December 17 or later if December 16 or earlier was the original plan**.

### 2.6 The LLC Fee on Gross Receipts — R&TC §17942 (Form FTB 3536)

**LLC Fee on Gross Receipts schedule (2025)**  _(R&TC §17942)_

| Total California Income | LLC Fee |
| --- | --- |
| Less than $250,000 | $0 |
| $250,000 – $499,999 | $900 |
| $500,000 – $999,999 | $2,500 |
| $1,000,000 – $4,999,999 | $6,000 |
| $5,000,000 or more | $11,790 |

- **Nature of the fee** — The fee is not a tax on net income; it is a tax on gross California-sourced total income (broadly, gross receipts less returns and allowances, but before deduction of cost of goods sold or any operating expenses except for certain pass-through allocations). It is therefore possible — and common — for a low-margin LLC to owe a substantial fee while reporting a net loss.
- **Estimated fee - Form FTB 3536 due date and penalty** — Due on or before the 15th day of the 6th month of the taxable year (June 15 for calendar-year LLCs). The estimated fee must be at least the amount of the prior year's fee, and the underpayment penalty under R&TC §17942(d) is 10% of the underpayment unless the estimate equals or exceeds the prior year's fee.  _(R&TC §17942(d))_
- **Final fee true-up - Form 568** — The final fee is reconciled on Form 568, due on or before the 15th day of the 3rd month after year-end (March 15 for calendar-year LLCs). The Form 568 mechanics, including the income-sourcing rules for the LLC fee, are covered in detail in `ca-smllc-form-568` and `ca-llc-fee-and-tax`; this skill addresses only the formation-year planning implications.

Because the LLC fee is a gross-receipts tax, it disproportionately affects e-commerce, agency, and pass-through service businesses with substantial California revenue but thin margins. A California-located freelance developer billing $260,000 of California-sourced revenue will owe the $800 minimum franchise tax PLUS the $900 LLC fee — a combined $1,700 floor before any income tax — even if the developer's net profit is much lower.

## 3. California C-Corporation Formation Mechanics

### 3.1 Articles of Incorporation — Form ARTS-GS

- **Form ARTS-GS filing fee** — $100
- **Articles of Incorporation required elements** — 1. Entity name must contain 'Corporation,' 'Incorporated,' 'Limited,' or an acceptable abbreviation under Corp. Code §202(a), unless the name is sufficiently distinct to make the corporate status apparent. Name distinguishability rules apply. 2. Business purpose: a short general-purpose clause is sufficient — California default is 'to engage in any lawful act or activity for which a corporation may be organized under the General Corporation Law of California.' 3. Agent for service of process: same rules as for LLCs (Section 2.3). 4. Authorized shares: total number of shares authorized; most California small-business corporations authorize 1,000,000 to 10,000,000 shares of common stock for flexibility for option grants and future financing. 5. Incorporator signature: any individual may sign.  _(Corp. Code §202(a))_
- **Expedited processing** — Expedited processing options mirror the LLC schedule.

### 3.2 Corporate Statement of Information — Form SI-550

- **Form SI-550 filing fee** — $25
- **SI-550 due date and cadence** — Within 90 days of formation, and annually thereafter (note: annual, not biennial as for LLCs), the corporation must file Form SI-550.
- **SI-550 required disclosures and penalty** — The SI-550 discloses officers, directors, the agent for service of process, the principal office, and the corporation's California office. The penalty for failure to file is $250 under R&TC §19141, with the same suspension consequences described in Section 2.2.  _(R&TC §19141)_

### 3.3 Annual $800 Minimum Franchise Tax — R&TC §23153

- **$800 franchise tax floor / 8.84% rate for corporations** — Every California corporation owes the same $800 minimum franchise tax as an LLC. For corporations, the $800 is the floor; the actual franchise tax is the greater of $800 or 8.84% of net income (R&TC §23151(a)). The first-year minimum franchise tax for corporations was historically waived (R&TC §23153(f)(1)), but that waiver was eliminated effective January 1, 2024, parallel to the AB 85 LLC sunset.  _(R&TC §23153; R&TC §23151(a); R&TC §23153(f)(1))_
- **Apportionment and 15-day rule for corporations** — The 8.84% rate applies to net income apportioned to California using the single-sales-factor apportionment formula under R&TC §25128.7 (mandatory for most non-financial business activities). The 15-day rule under R&TC §23153(d) applies to corporations on the same terms as to LLCs (see Section 2.5.2).  _(R&TC §25128.7; R&TC §23153(d))_
- **Estimated corporate franchise tax and annual return due dates** — Estimated corporate franchise tax is paid quarterly on Form FTB 100-ES (due April 15, June 15, September 15, and December 15 for calendar-year corporations). The annual return, Form 100, is due on or before the 15th day of the 4th month after year-end (April 15 for calendar-year corporations).

### 3.4 The C-Corporation Double-Tax Reality

- **Double taxation description** — Forming a California C-corporation creates the classic federal-level double taxation: the C-corp pays 21% federal corporate income tax (IRC §11) plus 8.84% California corporate income tax on its net income, and then shareholders pay additional individual tax on any dividends or share redemptions distributed to them.  _(IRC §11)_
- **When C-corp is attractive** — For most freelance and small-business owners, the C-corp is not the right vehicle; the LLC (taxed as disregarded SMLLC or as partnership) is far more common. The C-corp becomes attractive only when: the business plans to raise venture capital (most institutional investors require a C-corp, typically Delaware-incorporated); the business has substantial qualified small business stock (QSBS) planning under IRC §1202; the business has a strategic reason to retain earnings inside the entity for reinvestment at the corporate rate.  _(IRC §1202)_
- **Decision delegation** — Decision logic between SMLLC and C-corp is delegated to `us-s-corp-election-decision` and to credentialed counsel.

## 4. California S-Corporation Election

- **California S-corp tax rate** — 1.5% percent of net income (in addition to $800 minimum franchise tax)  _(R&TC §23802)_
- **S-corp election honored by California** — A federal S-corporation election (IRS Form 2553) is honored by California, but California imposes a 1.5% S-corp tax on net income under R&TC §23802 (in addition to the $800 minimum franchise tax). The S-corp tax is a true entity-level tax that effectively erodes part of the federal SE-tax savings that motivate the S-corp election in the first place.  _(R&TC §23802)_

The California S-corp arithmetic for a freelance developer earning $200,000 of net profit:
- Federal SE tax savings from S-corp (versus SMLLC): approximately 15.3% on the difference between net profit and reasonable salary, partially offset by payroll tax on the salary.
- California S-corp tax cost: 1.5% × $200,000 = $3,000 per year.
- Plus the $800 minimum franchise tax.
- Plus payroll service costs (typically $600–$1,500/year).
- Plus additional federal and California return preparation costs (typically $1,500–$3,000 more than an SMLLC return).

The break-even for a California freelance developer between SMLLC and S-corp is typically between $80,000 and $120,000 of net profit, but the spread is much narrower than in non-California states because of the 1.5% S-corp tax. Decision logic is delegated to `us-s-corp-election-decision`; this skill flags only the California overlay.

## 5. The "Doing Business in California" Threshold — R&TC §23101

- **Doing business in California standard** — This is the most important compliance question for any out-of-state entity with California connections. The standard for "doing business in California" is codified at R&TC §23101 and is interpreted by FTB Notices and the California Court of Appeals.  _(R&TC §23101)_

### 5.1 The §23101(a) Active-Conduct Test

- **Active-conduct test definition** — An entity is doing business in California if it is actively engaging in any transaction for the purpose of financial or pecuniary gain or profit in California. This is a facts-and-circumstances test and the FTB applies it broadly.  _(R&TC §23101(a))_
- **Examples of active conduct in California** — Examples that have been held to constitute doing business under §23101(a) include: maintaining an office, store, or warehouse in California; having employees, agents, or independent contractors physically working in California on behalf of the entity; owning or leasing tangible personal property located in California; manufacturing or producing goods in California; soliciting sales in California through traveling employees or agents.  _(R&TC §23101(a))_

### 5.2 The §23101(b) Bright-Line Test — 2025 Thresholds

- **Bright-line economic-nexus test overview** — Effective for tax years beginning on or after January 1, 2011, R&TC §23101(b) provides a bright-line economic-nexus test that operates in addition to the §23101(a) active-conduct test. An entity is doing business in California if it meets any one of the following four conditions in the taxable year.  _(R&TC §23101(b))_
- **Condition 1 - organized or commercially domiciled** — The entity is organized or commercially domiciled in California.  _(R&TC §23101(b)(1))_
- **California-sourced sales threshold (2025)** — $757,070 USD (lesser of $757,070 or 25% of the entity's total sales worldwide, under sourcing rules of R&TC §25135 and §25136)  _([R&TC §23101(b)(2)](https://www.ftb.ca.gov/file/business/doing-business-in-california.html))_
- **California real property and tangible personal property threshold (2025)** — $75,707 USD (lesser of $75,707 or 25% of the entity's total property worldwide)  _([R&TC §23101(b)(3)](https://www.ftb.ca.gov/file/business/doing-business-in-california.html))_
- **California-paid compensation threshold (2025)** — $75,707 USD (lesser of $75,707 or 25% of the entity's total compensation worldwide; paid to employees, members, or partners attributable to California services)  _([R&TC §23101(b)(4)](https://www.ftb.ca.gov/file/business/doing-business-in-california.html))_
- **Annual inflation indexing** — The dollar thresholds are indexed annually for inflation under R&TC §23101(c) using the California Consumer Price Index. The figures above are the 2025 thresholds; the FTB publishes updated thresholds each year in early winter for the following tax year.  _(R&TC §23101(c))_

**AUDIT FLASH POINT — The "doing business in California" threshold is extremely low.** A Delaware LLC with a single California-based employee earning $80,000 per year is doing business in California and must register as a foreign LLC, pay the $800, file Form 568, and pay the gross-receipts LLC fee on its California-sourced revenue. A Wyoming corporation with $760,000 in sales to California customers (out of $3,000,000 total) is doing business in California — the $760,000 exceeds the lesser of the $757,070 absolute threshold and 25% of total sales ($750,000). **Treat any out-of-state entity with California operations or California-resident employees as a presumptive "doing business" candidate and confirm explicitly in intake.**

### 5.3 California-Sourced Sales: Single-Sales-Factor and Market-Based Sourcing

- **Sourcing rules for sales** — Under R&TC §25128.7 (mandatory single-sales-factor apportionment) and §25136 (market-based sourcing), sales of tangible personal property are sourced to California if the property is delivered or shipped to a California purchaser, and sales of services and intangibles are sourced to California based on where the customer received the benefit of the service or intangible. This is a market-based rule, not a cost-of-performance rule.  _(R&TC §25128.7; R&TC §25136)_

The practical consequence: a Texas freelance developer with no California presence who provides software development services to a California-headquartered client is generating California-sourced sales for purposes of §23101(b). If the developer's California-sourced sales exceed the lesser of $757,070 or 25% of total sales in 2025, the developer is doing business in California and must register a foreign entity (or, if operating as a sole proprietor without an entity, must at minimum file a California nonresident return — but this skill is concerned with the entity registration question).

For most California-services freelancers and small agencies, the §23101(b) bright-line is the binding constraint, not the §23101(a) active-conduct test. A California customer that generates $50,000 of revenue does not trigger the bright-line by itself, but a portfolio of California customers that totals $760,000 does; a lower California total can also trigger if it exceeds 25% of worldwide sales.

## 6. Statement of Information — Filing Cadence

**Statement of Information filing cadence by entity type**

| Entity Type | First SI Due | Recurring SI Cadence | Form | Fee |
| --- | --- | --- | --- | --- |
| California LLC | 90 days after SOS file date | Biennially (every 2 years) | LLC-12 | $20 |
| California C-corp | 90 days after SOS file date | Annually | SI-550 | $25 |
| California S-corp (federal election; California corp) | 90 days after SOS file date | Annually | SI-550 | $25 |
| California nonprofit | 90 days after SOS file date | Biennially | SI-100 | $20 |
| Foreign LLC (registered in CA) | 90 days after foreign-qual file date | Biennially | LLC-12 | $20 |
| Foreign corporation (registered in CA) | 90 days after foreign-qual file date | Annually | SI-550 | $25 |

The Statement of Information cadence is the most commonly missed compliance item because it is decoupled from the annual tax filing schedule. The LLC-12 for a biennial-cadence LLC formed in March 2023 is due in March 2025 — two years after the previous filing — and the FTB's tax-due reminders do not cover the SOS filing. **Build the SI due date into the entity calendar at formation and use a recurring reminder.**

## 7. Foreign Qualification — Registering an Out-of-State Entity in California

An out-of-state entity that meets the §23101 "doing business" test must register with the California Secretary of State as a foreign entity. The mechanics follow.

### 7.1 Foreign LLC — Form LLC-5

- **Form LLC-5 filing fee** — $70
- **LLC-5 required elements** — 1. The entity's name as registered in its home state. If the name is not available in California (e.g., another California entity already uses it), the foreign LLC must adopt a fictitious name for California purposes. 2. The state or country of organization and the date of organization. 3. A current Certificate of Good Standing (or equivalent) from the home state, dated no more than 6 months before the LLC-5 filing. 4. The agent for service of process in California — same rules as for domestic LLCs. 5. The principal office address.
- **Post-LLC-5 obligations** — After the LLC-5 is accepted, the foreign LLC must file the Statement of Information (Form LLC-12) within 90 days for $20, and biennially thereafter. The foreign LLC is then subject to the same $800 annual minimum franchise tax and the same gross-receipts LLC fee as a domestic California LLC.

### 7.2 Foreign Corporation — Form S&DC-S/N

- **Form S&DC-S/N filing fee** — $100
- **S&DC-S/N requirements and post-filing obligations** — The S&DC-S/N requires similar information to the LLC-5, plus a Certificate of Good Standing from the home jurisdiction. The corporation then files Form SI-550 within 90 days for $25 and annually thereafter, and is subject to the $800 minimum franchise tax (and 8.84% income tax on California-apportioned income).

### 7.3 The Delaware + California Double-Fee Trap

This is the canonical compliance failure pattern for venture-backed startups.

A founder forms a Delaware LLC (Delaware franchise tax: $300/year flat fee) because Delaware is "easy" or "the standard for startups." The founder is based in San Francisco and conducts the business from California, with California customers, a California office, and California employees. The founder believes that incorporating in Delaware insulates them from California fees. **This is wrong.**

The Delaware LLC is doing business in California under §23101 and must register as a foreign LLC. The total annual California-related fees are:
- Delaware annual LLC tax: $300 (paid to Delaware Division of Corporations).
- California foreign qualification one-time filing: $70 for LLC-5, plus $20 for the initial LLC-12 (one-time at registration).
- California annual minimum franchise tax: $800 (paid to FTB).
- California LLC gross-receipts fee: $0 to $11,790 depending on California-sourced gross receipts (paid to FTB).
- California biennial Statement of Information: $20 (paid to SOS, every 2 years).
- Delaware registered agent fee: $50–$300/year.
- California registered agent fee: $100–$300/year.

The "Delaware advantage" for an early-stage California-operating LLC is therefore negative. The founder pays Delaware $300 plus registered-agent fees, AND pays California $800 plus the gross-receipts fee, AND files in both states, AND maintains two registered agents. The combined annual carrying cost typically exceeds $1,400 of fixed fees before any income tax, versus approximately $900 of fixed fees ($800 + ~$100 registered agent) for a California-domestic LLC.

The Delaware advantage is real for C-corporations seeking institutional venture capital (Delaware corporate law is the U.S. de facto standard for VC-backed companies and most VCs require Delaware C-corp form factor), but it is rarely justified for LLCs. **Counsel founders against Delaware LLCs unless there is a specific institutional or contractual reason for Delaware law to apply.**

## 8. BOI / Corporate Transparency Act Status

The Corporate Transparency Act (CTA), 31 U.S.C. §5336, would require most newly-formed and existing entities to file a Beneficial Ownership Information (BOI) report with the Financial Crimes Enforcement Network (FinCEN). Following litigation in 2024 (*National Small Business United v. Yellen*, N.D. Ala.; *Texas Top Cop Shop, Inc. v. Garland*, E.D. Tex.) and the resulting injunctions, enforcement of the CTA against domestic reporting companies has been stayed. As of the `last_updated` date above, FinCEN is not requiring domestic reporting companies to file BOI reports.

This situation is fluid. Foreign reporting companies (entities formed outside the United States and registered to do business in a U.S. state) are subject to a narrower revised rule. Domestic reporting companies should monitor FinCEN announcements and prepare to file within 30 days if the stay is lifted. **Add a recurring reminder to check FinCEN CTA status every 90 days for any entity formed after January 1, 2024.**

The California state-level beneficial-ownership disclosure regime (SB 113, R&TC §17943) is independent of the federal CTA and has its own (limited) requirements, addressed in `ca-smllc-form-568` and `ca-llc-fee-and-tax`.

## 9. Common Errors and Audit Flash Points

**Common Errors and Audit Flash Points table**

| # | Error | Consequence | Remediation |
| --- | --- | --- | --- |
| 1 | DE LLC operating in CA without foreign qualification | Lost suit rights, $250+ Corp. Code penalty, back $800 × years, plus LLC fee + interest + 5%/month late-payment penalty | File LLC-5 with current DE Certificate of Good Standing, file all back-year Form 568 returns, pay all back taxes and fees with FTB Form 3557 revivor if suspended |
| 2 | Pre-2024 founder unaware AB 85 expired | Late-payment penalty of 5%/month up to 25%, plus interest under §19101 | Pay back $800 immediately with FTB 3522 and request first-time abatement under FTB Notice 2022-02 (rarely granted for franchise tax) |
| 3 | LLC formed December 16 instead of December 17 → loses 15-day rule | $800 owed for the formation year despite no activity | None — the rule is a strict calendar test. Document the timing clearly in formation memos so future founders avoid the trap |
| 4 | Missed Form LLC-12 within 90 days of formation | $250 penalty + eventual FTB suspension | File LLC-12 immediately + pay penalty + monitor revivor status |
| 5 | Underpayment of estimated LLC fee on Form 3536 (paid less than prior-year fee by June 15) | 10% underpayment penalty under §17942(d) | Pay the missed amount with Form 3536 plus a penalty waiver request — rarely granted absent reasonable cause |
| 6 | Foreign C-corp doing business in CA without S&DC-S/N | Same lost-suit consequences as #1, plus 8.84% income tax on apportioned CA income with no statute-of-limitations protection (the SOL doesn't start until a return is filed) | File S&DC-S/N + all back Form 100s + pay back $800 + 8.84% tax + interest + penalties |
| 7 | Reliance on home-state operating agreement for California LLC | Operating agreement may not address California-specific manager fiduciary duties under Corp. Code §17704.09 | Adopt a California-form operating agreement or add a California rider |
| 8 | Failure to recognize that a remote California-resident employee creates §23101 nexus | Foreign-qualification failure (#1 above) | Foreign-qualify; reassess whether to bring the employee into a different state or convert to contractor (with caution under AB 5 / Dynamex worker classification rules) |

**AUDIT FLASH POINT — Combined Delaware + California double-fee trap.** If you encounter a client with a Delaware LLC and California operations, the audit triage sequence is: (1) Has the entity registered with the California SOS via LLC-5? (2) Has it filed Form 568 for every year of California operations? (3) Has it paid the $800 for every year? (4) Has it filed the biennial LLC-12? If any answer is "no" or "unsure," the client needs to engage the FTB voluntary disclosure program (VDP) under R&TC §19191 to limit the look-back period to 6 years and waive most penalties (interest is not waivable). The VDP is only available to entities that have not been contacted by the FTB; the window closes as soon as the FTB sends a nexus questionnaire.

## 10. Worked Examples

### Example 10.1 — San Francisco Tech Startup Forming Delaware C-Corp + Qualifying in California

**Facts.** Two co-founders in San Francisco are launching a software-as-a-service product. They plan to raise venture capital. Their lead investor requires a Delaware C-corporation structure. The company will be operated entirely from San Francisco (initially from a co-working space; later from a leased office). The co-founders will be W-2 employees of the new company from day one.

**California analysis.**

The company forms a Delaware C-corporation via the Delaware Division of Corporations Online Filing for $89 (Certificate of Incorporation) plus the Delaware annual franchise tax (minimum $175 + $50 annual report = $225/year under the authorized-shares method; or $400 minimum under the assumed-par-value capital method — the lower of the two applies). Delaware registered agent: ~$100/year.

The Delaware C-corp is doing business in California under §23101(a) (active conduct from the SF office) and under §23101(b)(1) (commercially domiciled in California — the principal place of business is in CA). It must register as a foreign corporation with the California SOS by filing Form S&DC-S/N for $100, attaching a Delaware Certificate of Good Standing. It then files Form SI-550 within 90 days for $25, and annually thereafter.

The Delaware C-corp owes:
- Federal corporate income tax: 21% of taxable income.
- California corporate franchise tax: greater of $800 minimum or 8.84% of California-apportioned net income, paid quarterly via FTB 100-ES.
- California Statement of Information: $25/year.
- Delaware franchise tax: $225–$400/year depending on calculation method.
- Registered agents in both states: $200–$600/year combined.

**Total annual fixed compliance cost before income tax:** approximately $1,250–$1,800.

The Delaware structure is justified here by the institutional-investor requirement, not by tax efficiency. The founders should understand that the Delaware formation does not reduce California tax exposure — it adds Delaware filings on top.

**Formation calendar (assuming formation on March 10, 2025):**
- March 10, 2025: File DE Certificate of Incorporation ($89).
- March 11, 2025: Apply for federal EIN (free, online IRS).
- March 12, 2025: File CA Form S&DC-S/N ($100), attaching DE Certificate of Good Standing (obtained by paying DE $50 for certificate).
- April 15, 2025: First California estimated franchise tax via FTB 100-ES — $200 (25% of $800 minimum) or 25% of full estimated tax if greater.
- June 8, 2025: File first CA Form SI-550 ($25).
- June 15, 2025: Second FTB 100-ES installment.
- September 15, 2025: Third FTB 100-ES installment.
- December 15, 2025: Fourth FTB 100-ES installment.
- March 1, 2026: Delaware annual report and franchise tax due ($225–$400).
- April 15, 2026: California Form 100 due (full-year 2025 return + true-up).
- April 15, 2026: 2026 Q1 California estimated franchise tax ($200 minimum).
- June 8, 2026: Annual SI-550 due ($25).

### Example 10.2 — Los Angeles Real Estate LLC

**Facts.** An LA-based real-estate investor wants to hold a single rental property — a duplex in Pasadena — in a limited-liability entity to insulate the rest of her personal assets from tenant-liability exposure. The property generates $48,000/year of gross rents and approximately $8,000/year of net rental income after expenses, mortgage interest, and depreciation.

**California analysis.**

A single-member California LLC is the appropriate form. Form LLC-1 with the CA SOS, $70 online. Form LLC-12 within 90 days, $20. Federal classification defaults to disregarded entity (no Form 8832 needed); rental income flows to the owner's Schedule E (not Schedule C — rentals are generally not Schedule C unless services are provided beyond those typical of a landlord).

The LLC owes:
- $800 minimum franchise tax via FTB 3522 by April 15 each year.
- LLC gross-receipts fee on Form 3536/Form 568: $48,000 gross rents is below the $250,000 threshold, so the fee is $0.
- Form 568 by April 15 each year (rentals are sourced based on the location of the rental property — California-located property generates California-sourced income).
- LLC-12 biennially: $20 every two years.

**Total annual fixed California cost:** $800 + ~$10 average annual LLC-12 (~$20 every 2 years).

The total annual carrying cost is $800 + ~$10 = ~$810, which is large relative to the $8,000 of net rental income (10% drag). Many LA real-estate investors decide that a single duplex does not justify the $800 — they instead use an umbrella liability insurance policy ($300–$600/year for $1M–$2M of coverage) for liability protection. For a portfolio of three or more properties, the LLC becomes more cost-effective per property.

If the investor wants to defer the $800 to the next year, she can use the 15-day rule: file the LLC-1 on December 17, 2025 or later, conduct no business in 2025, and the first $800 is owed by April 15, 2026 for the 2026 year. This buys 12 months of liability protection planning at no California cost for 2025.

### Example 10.3 — Texas Freelance Developer SMLLC With California Clients

**Facts.** A Texas-resident freelance software developer operates as a Texas single-member LLC. In 2025 the developer billed $625,000 of total revenue, of which $190,000 came from three California-headquartered clients (the rest from clients in Texas, Florida, and New York). The developer works exclusively from his home office in Austin.

**California analysis.**

Under §23101(b)(2), the developer's California-sourced sales are $190,000. That is below the absolute $757,070 threshold, but the test uses the lesser of $757,070 or 25% of total sales. 25% of $625,000 is $156,250, and $190,000 exceeds that lesser threshold. The bright-line sales test is therefore met.

The developer is doing business in California. He must register his Texas LLC as a foreign LLC with the California SOS by filing Form LLC-5 ($70) plus current Texas Certificate of Good Standing, file Form LLC-12 within 90 days ($20), pay the $800 minimum franchise tax for 2025, and file Form 568 for 2025 to true up the gross-receipts LLC fee. The California-sourced gross receipts of $190,000 are below the $250,000 fee threshold, so the LLC fee on Form 3536 is $0.

**Total California cost for 2025:** $70 (LLC-5) + $20 (LLC-12) + $800 (3522/568) + $0 (LLC fee) = $890 of California compliance cost for the first year, plus $800/year thereafter until California sales drop below the §23101 thresholds.

The developer should also file a California nonresident individual income tax return (Form 540NR) reporting the California-sourced pass-through income from the Texas LLC. The California-sourced share of his self-employment income is taxable on the 540NR even though he is a Texas resident with no California physical presence. This skill addresses only the entity-formation overlay; the 540NR mechanics are covered by `ca-540-individual-return` (resident variant) and any nonresident return skill.

**AUDIT FLASH POINT — The 25% relative threshold catches more taxpayers than the $757,070 absolute threshold.** Many out-of-state freelancers and consultants believe they are safe from California "doing business" status because their California sales are well under $757,070. They overlook the 25%-of-total-sales prong. Always compute both: California sales as a dollar amount AND California sales as a percentage of worldwide sales. If either prong is met, the entity is doing business in California.

### Example 10.4 — California Retailer SMLLC Selling Physical Goods

**Facts.** A California-resident entrepreneur opens an online retail store selling handmade ceramic goods. The store launches January 15, 2025. In 2025 it generates $320,000 of gross sales, of which $180,000 comes from California customers and $140,000 from out-of-state customers. The entrepreneur operates from a home studio in Oakland. Cost of goods sold is approximately 40% ($128,000); net income before taxes is approximately $90,000.

**California analysis.**

The entrepreneur forms a California SMLLC by filing Form LLC-1 ($70) on January 15, 2025, and Form LLC-12 within 90 days ($20). The LLC is commercially domiciled in California and is therefore doing business in California under §23101(b)(1) — no thresholds analysis needed.

For 2025:
- Form FTB 3522 by April 15, 2025: $800 (no first-year exemption — AB 85 expired). The entrepreneur should pay this on or shortly after formation in January 2025.
- Form FTB 3536 by June 15, 2025: estimated LLC fee. California-sourced total income is the worldwide gross receipts because the LLC is commercially domiciled in California, subject to apportionment. With single-sales-factor apportionment, the California sourcing percentage is California sales / total sales = $180,000 / $320,000 = 56.25%. California-apportioned total income for the LLC fee = $320,000 × 56.25% = $180,000. This is below the $250,000 fee threshold. The estimated LLC fee is $0. (Important: the fee is on California-apportioned gross income, not net income — the COGS deduction does not apply.)
- Form 568 by April 15, 2026: full-year return, true-up of the LLC fee (still $0 if California-apportioned total income remains at $180,000).
- Form LLC-12 by mid-April 2025 (within 90 days of January 15 formation): $20.
- Form 568 for 2025 will report all California-related activity and reconcile.

**Plus California sales tax:** as a California retailer selling tangible personal property, the entrepreneur must register with the CDTFA for a seller's permit (free), collect California sales tax on California-destination sales (statewide 7.25% plus local district taxes — combined ~9.0%–10.5% in most metro areas), and file CDTFA-401 quarterly or annually depending on volume. Sales tax mechanics are covered in `california-sales-use-tax`. The entrepreneur should also register for sales tax in other states where economic-nexus thresholds (Wayfair) are met based on the $140,000 of out-of-state sales — most states' economic-nexus thresholds are $100,000 of sales or 200 transactions.

**Plus federal:** the $90,000 of net SMLLC profit flows to the entrepreneur's Schedule C. Self-employment tax under IRC §1401 applies; QBI deduction under §199A may apply (retail is non-SSTB). See `us-sole-prop-bookkeeping`, `us-schedule-c-and-se-computation`, and `us-qbi-deduction`.

**Total 2025 California entity-level cost:** $70 + $20 + $800 + $0 = $890.

### Example 10.5 — Wyoming LLC With Single California Remote Employee

**Facts.** A Wyoming LLC (formed because the founder read that Wyoming is "tax-friendly") has total 2025 revenue of $1,400,000, of which only $40,000 comes from California customers. However, the LLC has one fully remote employee living in San Diego who earns $95,000/year as a customer-success manager and works from her home in San Diego.

**California analysis.**

California-sourced sales: $40,000. Below both the $757,070 absolute threshold and 25% of $1,400,000 = $350,000. §23101(b)(2) is not met.

California property: assume $0 (no California-owned tangible property).

California compensation: $95,000 paid to the San Diego employee, attributable to California services. Compare against the lesser of $75,707 (the 2025 threshold) and 25% of total compensation. Assume total entity compensation is $400,000; 25% of that is $100,000. The lesser of $75,707 and $100,000 is $75,707. $95,000 > $75,707 — §23101(b)(4) IS met. The Wyoming LLC is doing business in California.

The Wyoming LLC must:
1. Register as a foreign LLC in California (Form LLC-5, $70).
2. File initial Form LLC-12 within 90 days ($20).
3. Pay $800 annual minimum franchise tax via FTB 3522 by April 15, 2025 (the formation in California for purposes of doing-business measurement is essentially retroactive to when the §23101 thresholds were first met; in practice, the LLC should treat 2025 as its first California year).
4. File Form 568 for 2025, reporting California-apportioned income. With single-sales-factor apportionment, California sales are $40,000 / $1,400,000 = 2.857% — so California-apportioned income is small. The LLC fee on gross receipts will be applied to California-apportioned total income; $1,400,000 × 2.857% = $40,000, which is well below the $250,000 fee threshold. LLC fee: $0.
5. Comply with California payroll tax obligations for the San Diego employee — California Employment Development Department (EDD) registration, SDI withholding, California PIT withholding, and quarterly DE 9 / DE 9C filings. This is a separate payroll-tax compliance domain not addressed by this skill but is triggered by the same fact pattern.
6. Withhold California income tax from the San Diego employee's wages and remit via Form DE 88.

The Wyoming "tax advantage" turns out to be illusory for this LLC. Wyoming's $60 annual report fee is dwarfed by the $800 California minimum franchise tax that California will assess every year that the San Diego employee remains in California (or that California-sourced sales exceed thresholds).

**Strategic option:** if the LLC wants to eliminate California exposure, it would need to (a) move the San Diego employee out of California, (b) convert the employee to a contractor based in California (but California AB 5 makes this difficult for employee-like roles), or (c) reduce California sales below the §23101(b)(2) threshold AND reduce California payroll below the §23101(b)(4) threshold. The path of least resistance is usually to register and comply.

## 11. Filing Schedule and Calendar Summary

**California-domestic LLC formed January 1, 2025 — filing schedule**  _(Corp. Code §17702.01; Corp. Code §17702.09; R&TC §17941; R&TC §17942(d); R&TC §18601, §18633.5; Corp. Code §17702.09)_

| Date | Filing | Form | Fee | Authority |
| --- | --- | --- | --- | --- |
| Jan 1, 2025 | LLC organized | LLC-1 | $70 | Corp. Code §17702.01 |
| Apr 1, 2025 | First Statement of Information (within 90 days) | LLC-12 | $20 | Corp. Code §17702.09 |
| Apr 15, 2025 | First annual minimum franchise tax | FTB 3522 | $800 | R&TC §17941 |
| Jun 15, 2025 | Estimated LLC fee (if expected California gross receipts ≥ $250K) | FTB 3536 | Variable | R&TC §17942(d) |
| Mar 15, 2026 | Annual LLC return + LLC fee true-up | Form 568 | Variable | R&TC §18601, §18633.5 |
| Apr 15, 2026 | Second annual minimum franchise tax | FTB 3522 | $800 | R&TC §17941 |
| Apr 30, 2027 | Biennial Statement of Information (every 2 years from formation month) | LLC-12 | $20 | Corp. Code §17702.09 |

**California-domestic C-corporation formed January 1, 2025 — filing schedule**  _(Corp. Code §202; Corp. Code §1502; R&TC §19023; R&TC §18601; Corp. Code §1502)_

| Date | Filing | Form | Fee | Authority |
| --- | --- | --- | --- | --- |
| Jan 1, 2025 | Corp incorporated | ARTS-GS | $100 | Corp. Code §202 |
| Apr 1, 2025 | First Statement of Information | SI-550 | $25 | Corp. Code §1502 |
| Apr 15, 2025 | Q1 estimated franchise tax | FTB 100-ES | $200+ | R&TC §19023 |
| Jun 15, 2025 | Q2 estimated franchise tax | FTB 100-ES | $200+ | R&TC §19023 |
| Sep 15, 2025 | Q3 estimated franchise tax | FTB 100-ES | $200+ | R&TC §19023 |
| Dec 15, 2025 | Q4 estimated franchise tax | FTB 100-ES | $200+ | R&TC §19023 |
| Apr 15, 2026 | Annual corporate return | Form 100 | Variable | R&TC §18601 |
| Apr 15, 2026 | Annual Statement of Information | SI-550 | $25 | Corp. Code §1502 |

## 12. Output Specification

When invoked, this skill produces:

1. **Entity-type recommendation memo** — 1–2 pages summarizing the entity-type decision (SMLLC vs. partnership LLC vs. C-corp vs. S-corp election) given the founder's facts. Defers federal classification mechanics to `us-s-corp-election-decision`.
2. **California filing roadmap** — a Gantt-style or table-format calendar of every California SOS and FTB filing required in the first 24 months, with dates, forms, fees, and statutory authority.
3. **Fee budget** — a 3-year projected California compliance cost summary, including: SOS filings, FTB minimum franchise tax, FTB LLC fee, Statement of Information cadence, registered-agent fees, and federal EIN/Form 8832 costs (if applicable).
4. **"Doing business in California" determination** — for out-of-state entities, an explicit §23101 analysis showing California sales, California property, and California compensation against the 2025 thresholds, with a clear yes/no on foreign-qualification obligation.
5. **Reviewer brief** — a 1-page summary of the recommendation, the statutory authorities cited, the assumptions made, and the open questions for credentialed reviewer signoff.

All outputs include the standard reviewer disclaimer: this is a draft for review by a credentialed California-licensed CPA, Enrolled Agent, or attorney; it is not legal or tax advice and should not be acted upon without independent review.

## 13. Self-Checks (must pass before output is released)

1. ☐ Is the entity type (LLC vs. C-corp vs. S-corp election) explicitly identified and matched to the founder's stated objectives?
2. ☐ Has the §23101 "doing business in California" analysis been performed, with explicit comparison against the 2025 thresholds ($757,070 sales / $75,707 payroll / $75,707 property, plus the 25%-of-total prongs)?
3. ☐ For out-of-state entities, has the foreign-qualification cost (LLC-5 $70 + LLC-12 $20, or S&DC-S/N $100 + SI-550 $25) been added to the budget?
4. ☐ Has the AB 85 / SB 818 expiration been flagged to any client who formed in 2021–2023 OR who is considering formation in 2024+?
5. ☐ Has the 15-day rule been considered if the formation date is in November or December?
6. ☐ Has the Statement of Information filing cadence (90-day initial + biennial-for-LLC / annual-for-corp) been included in the calendar?
7. ☐ Has the gross-receipts LLC fee under R&TC §17942 been computed or explicitly noted as $0 because California-apportioned gross income is below $250,000?
8. ☐ For Delaware-LLC clients with California operations, has the double-fee trap been raised explicitly?
9. ☐ Has the CTA / BOI status been noted with a "monitor FinCEN" reminder?
10. ☐ Has the output been flagged as requiring credentialed reviewer signoff before being acted upon?

- **§23101 doing-business-in-California 2025 thresholds** — $757,070 sales / $75,707 payroll / $75,707 property, plus the 25%-of-total prongs  _([R&TC §23101](https://www.ftb.ca.gov/file/business/doing-business-in-california.html))_

## 14. Refusals and Out-of-Scope

- **Federal entity classification mechanics out of scope** — Delegated to `us-s-corp-election-decision` and to federal entity-election skills.  _(14. Refusals and Out-of-Scope)_
- **California sales and use tax out of scope** — Delegated to `california-sales-use-tax`.  _(14. Refusals and Out-of-Scope)_
- **California payroll tax (EDD) out of scope** — Out of scope. A separate payroll-tax skill is required.  _(14. Refusals and Out-of-Scope)_
- **Nonresident individual returns (Form 540NR) out of scope** — Out of scope. Use a 540NR-specific skill.  _(14. Refusals and Out-of-Scope)_
- **Series LLCs not recognized** — California does not recognize series LLCs as separate taxable entities. Any series LLC formed in another state and doing business in California is treated as a single LLC for California purposes, with one $800 minimum franchise tax for the master series.  _(14. Refusals and Out-of-Scope)_
- **Professional LLCs (PLLCs) not permitted** — California does not permit LLCs to render licensed professional services (medicine, law, accounting, architecture, etc.). Licensed professionals must form a California Professional Corporation under the Moscone-Knox Professional Corporation Act (Corp. Code §13400 et seq.) — separate skill required.  _(Corp. Code §13400 et seq.)_
- **Nonprofit formation out of scope** — Out of scope.  _(14. Refusals and Out-of-Scope)_
- **Multi-state apportionment beyond California sourcing out of scope** — For entities operating in multiple states with complex apportionment, additional state-specific skills are required.  _(14. Refusals and Out-of-Scope)_
- **Standard refusal message** — "This task is out of scope for ca-formation. Please load [appropriate skill name] or engage credentialed counsel directly."  _(14. Refusals and Out-of-Scope)_

## 15. Statutory and Regulatory Authorities (Selected)

- **LLC minimum franchise tax** — $800  _(California Revenue and Taxation Code §17941)_
- **LLC gross-receipts fee** — LLC gross-receipts fee.  _(California Revenue and Taxation Code §17942)_
- **15-day rule for LLCs** — 15-day rule for LLCs.  _(California Revenue and Taxation Code §17946)_
- **"Doing business in California" definition and bright-line thresholds** — "Doing business in California" definition and bright-line thresholds.  _(California Revenue and Taxation Code §23101)_
- **Corporate franchise tax rate** — 8.84%  _(California Revenue and Taxation Code §23151)_
- **Corporate minimum franchise tax and 15-day rule** — Corporate minimum franchise tax and 15-day rule.  _(California Revenue and Taxation Code §23153)_
- **S-corporation tax rate** — 1.5%  _(California Revenue and Taxation Code §23802)_
- **Single-sales-factor apportionment** — Single-sales-factor apportionment.  _(California Revenue and Taxation Code §25128.7)_
- **Market-based sourcing of services and intangibles** — Market-based sourcing of services and intangibles.  _(California Revenue and Taxation Code §25136)_
- **California Revised Uniform Limited Liability Company Act** — California Revised Uniform Limited Liability Company Act.  _(California Corporations Code §17701.01 et seq.)_
- **Consequences of foreign LLC failure to register** — Consequences of foreign LLC failure to register.  _(California Corporations Code §17708.07)_
- **Corporation Articles of Incorporation requirements** — Corporation Articles of Incorporation requirements.  _(California Corporations Code §202)_
- **Corporate Statement of Information** — Corporate Statement of Information.  _(California Corporations Code §1502)_
- **Consequences of foreign corporation failure to qualify** — Consequences of foreign corporation failure to qualify.  _(California Corporations Code §2203)_
- **First-year minimum franchise tax waiver (now expired)** — First-year minimum franchise tax waiver (now expired).  _(Assembly Bill 85 (2020))_
- **Extension of AB 85 waiver through 2023 (now expired)** — Extension of AB 85 waiver through 2023 (now expired).  _(Senate Bill 818 (2021))_
- **Corporate Transparency Act (federal BOI rule, currently stayed for domestic reporting companies)** — Corporate Transparency Act (federal BOI rule, currently stayed for domestic reporting companies).  _(31 U.S.C. §5336)_

## *End of ca-formation skill, version 0.1, last updated 2025-11-15. Federal-overlay, California-state only. Reviewer signoff required.*

*End of ca-formation skill, version 0.1, last updated 2025-11-15. Federal-overlay, California-state only. Reviewer signoff required.*

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
