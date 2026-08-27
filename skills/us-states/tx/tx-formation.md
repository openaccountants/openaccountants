---
name: tx-formation
description: Tier 2 Texas content skill for entity formation covering tax year 2025. Includes the TX LLC Certificate of Formation $300, no state PIT, no franchise/margin tax under $2.47M revenue threshold, mandatory annual Public Information Report (Form 05-102), Series LLC permitted (2009 legislation), foreign qualification Certificate of Authority $750, doing-business thresholds for out-of-state entities (post-Wayfair $500k sales/$50k payroll/$50k property), and the BOI/CTA stay status.
jurisdiction: US-TX
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# TX Formation

## Texas Entity Formation — Tax Year 2025

## 1. Scope

This skill provides guidance on forming a Texas business entity (LLC, C-Corp, S-Corp, Series LLC) and on qualifying a foreign (out-of-state) entity to do business in Texas. It is written for founders, freelance software developers transitioning from sole proprietorship, small-business owners relocating from California or New York, and tax professionals advising on Texas entity choice for tax year 2025.

**In scope:**

- Texas Limited Liability Company (LLC) formation under Texas Business Organizations Code (BOC) Chapter 101
- Texas For-Profit Corporation (C-Corp) formation under BOC Chapter 21
- Texas Series LLC formation under BOC §101.601 et seq.
- Foreign qualification of out-of-state LLCs and corporations under BOC Chapter 9
- Texas Secretary of State filing fees and ongoing compliance
- Annual Public Information Report (Form 05-102) filed with the Texas Comptroller
- Franchise/margin tax thresholds and their interaction with entity choice (computation deferred to `tx-margin-tax.md` and `tx-franchise-tax.md`)
- Economic-nexus thresholds for out-of-state entities post-Wayfair (South Dakota v. Wayfair, 138 S. Ct. 2080 (2018))
- The Corporate Transparency Act (CTA) / Beneficial Ownership Information (BOI) stay status as of the version date
- Texas vs Delaware entity-choice analysis for founders, especially for venture-backed startups and bootstrapped software businesses
- The "doing business in Texas" determination under Texas Tax Code §171.001 and the Texas Comptroller's economic-nexus standard

**Out of scope:**

- Texas franchise/margin tax computation itself (see `tx-margin-tax.md`)
- Texas sales-and-use tax registration and computation (see `tx-sales-tax.md`)
- Federal entity classification election (Form 8832) or S-corp election (Form 2553) — see `us-s-corp-election-decision`
- Federal income tax computation for the owner — see `us-tax-workflow-base` and downstream federal content skills
- Non-profit corporations, professional associations (PAs), professional limited liability companies (PLLCs) where Texas licensing-board approval is required (e.g. medical, legal, dental — separate licensing analysis required)
- Limited partnerships (LPs) and limited liability partnerships (LLPs) beyond brief mention
- Texas state employment tax (Texas Workforce Commission unemployment insurance)
- Local (city/county) business license and permit research

**Required companion skills:**

- `us-tax-workflow-base` v0.2 or later (workflow architecture, conservative defaults, refusal catalogue)
- `tx-franchise-tax` for the Public Information Report mechanics
- `tx-margin-tax` for the margin tax computation when revenue exceeds the No Tax Due threshold

## 2. Why Texas?

Texas has, over the past decade, become one of the most popular jurisdictions in the United States for entity formation, second only to Delaware in cumulative founder mindshare and ahead of Delaware in raw resident-business formation. The reasons fall into four categories: (a) the absence of a state personal income tax, (b) a generous franchise/margin tax No Tax Due threshold, (c) low overall operating costs, and (d) a deep and growing technology ecosystem.

### 2.1 No state personal income tax

- **Texas constitutional protection against personal income tax** — Texas is one of nine U.S. states with no individual personal income tax. This is constitutionally protected by Article 8, Section 24 of the Texas Constitution, which requires a statewide referendum to impose any personal income tax — making a future income tax practically impossible.  _(Texas Constitution Article 8, Section 24)_

For pass-through entity owners (sole proprietors filing Schedule C, single-member LLC owners disregarded for federal tax, multi-member LLC partners, S-corp shareholders), the pass-through income flows from the federal return to the owner with **zero additional state income tax**. This is a structural advantage over California (top rate 13.3% including the mental health services tax), New York (top rate 10.9%), Oregon (top rate 9.9%), and Hawaii (top rate 11%).

For a Texas-resident sole proprietor with $200,000 of Schedule C net profit, the federal tax bill might be $50,000–$55,000 depending on deductions, but the **state** tax bill is $0. The same taxpayer in California would owe roughly $15,000–$18,000 in additional state income tax. Over a decade, the cumulative state-tax savings on a high-six-figure-income business compound into seven-figure differences.

### 2.2 No franchise/margin tax under $2.47M revenue (2024 and 2025 report years)

- **No Tax Due threshold** — 2,470,000 USD annualized total revenue (raised from $1,230,000 by Senate Bill 3 (88th Legislature, 2nd Called Session, 2023), for report years 2024 and forward, with subsequent annual inflation indexing)  _(Senate Bill 3 (88th Legislature, 2nd Called Session, 2023))_
- **Franchise tax is entity-level tax** — The Texas franchise tax (also called the "margin tax") is an entity-level tax imposed on most taxable entities doing business in Texas. For freelance developers, consultants, and small-business owners with revenue under the No Tax Due threshold — which describes the overwhelming majority of single-member-LLC owners and small Texas C-Corps — the franchise tax owed is $0.  _(Senate Bill 3 (88th Legislature, 2nd Called Session, 2023))_
- **PIR still required regardless of revenue** — This does not mean the entity has no Texas filing obligation. Every taxable entity — including LLCs and corporations with $0 in revenue — must file an annual Public Information Report (Form 05-102) with the Texas Comptroller. Missing this filing carries severe penalties (covered in Section 7 and as an AUDIT FLASH POINT).  _(Form 05-102, Texas Comptroller)_

### 2.3 Low operating costs

Texas has no state-level personal income tax, no state-level capital gains tax, no state-level dividend tax, and (for most small entities) no entity-level income tax. State property tax in Texas is comparatively high, but it applies to real property rather than to business operating income. Texas commercial rents in major metros (Austin, Houston, Dallas-Fort Worth, San Antonio) are substantially lower than San Francisco, New York, or Boston. Salaries for technical talent run roughly 70–85% of San Francisco-equivalent roles in Austin.

The combined effect is that a Texas-based software business with $1M in revenue retains a meaningfully higher share of profit than the same business in California, even before considering personal income tax on the owner's salary or distributions.

### 2.4 Tech hub growth — Austin

Austin has, since roughly 2018, emerged as a serious alternative to the San Francisco Bay Area for technology company headquarters. Tesla relocated its corporate headquarters to Austin in 2021. Oracle moved its headquarters to Austin in 2020. Major venture capital firms (8VC, Multicoin Capital, Founders Fund partners) maintain Austin offices. The University of Texas at Austin produces a substantial pipeline of engineering and computer science graduates.

Houston remains the energy-industry capital with strong adjacent industries in healthcare (Texas Medical Center is the largest medical complex in the world) and aerospace (Johnson Space Center). Dallas-Fort Worth has emerged as a financial-services and logistics hub, hosting the headquarters of AT&T, Texas Instruments, and Frito-Lay. San Antonio hosts a growing cybersecurity cluster around the National Security Agency's Texas Cryptologic Center and the U.S. Air Force's 24th Air Force.

For a founder, the practical implication is that Texas now offers access to engineering talent, venture capital, customers, and professional services (lawyers, accountants, IP counsel) at a scale that did not exist a decade ago.

### 2.5 Strong "doing business" reach — post-Wayfair

- **Post-Wayfair economic nexus adoption** — The 2018 U.S. Supreme Court decision in South Dakota v. Wayfair, Inc., 138 S. Ct. 2080 (2018), eliminated the physical-presence requirement for state-tax nexus. Texas adopted economic-nexus standards across both its sales-tax regime and its franchise-tax regime. The franchise-tax economic-nexus threshold is $500,000 in Texas-sourced gross receipts under the Texas Comptroller's Rule §3.586. This means out-of-state entities with substantial Texas customers may owe Texas franchise tax even without any physical presence — covered in detail in Section 9.  _(South Dakota v. Wayfair, Inc., 138 S. Ct. 2080 (2018); Texas Comptroller Rule §3.586)_

## 3. Texas LLC Formation

The Texas Limited Liability Company is the workhorse entity for small businesses, freelancers transitioning out of sole proprietorship, real estate investors, and consultants. It combines pass-through federal tax treatment (by default) with limited liability protection.

### 3.1 Certificate of Formation (Form 205)

- **Certificate of Formation content requirements** — Formation is accomplished by filing a Certificate of Formation — Limited Liability Company (Texas Secretary of State Form 205) under BOC §3.001 et seq. and §101.001 et seq. The certificate must include: 1. Entity name ending in "Limited Liability Company," "Limited Company," "LLC," "L.L.C.," "LC," or "L.C." Must be distinguishable on the records of the Secretary of State (BOC §5.053). 2. Type of entity — LLC (Section 1 of the form). 3. Registered agent — name and Texas street address of the registered agent (cannot be a P.O. box). The registered agent must be a Texas resident or a Texas entity authorized to do business in Texas (BOC §5.201). 4. Governing authority — whether the LLC is member-managed or manager-managed, plus names and addresses of the initial members or managers. 5. Purpose — generally "any lawful purpose for which a limited liability company may be organized." Specific professional purposes (medical, legal) may require additional licensing-board approval and conversion to PLLC. 6. Organizer — the person filing the certificate (typically the founder, an attorney, or a formation service). 7. Effective date — either immediately on filing, on a delayed date up to 90 days after filing, or on the occurrence of a future event up to 90 days out (BOC §4.052).  _(BOC §3.001 et seq.; BOC §101.001 et seq.; BOC §5.053; BOC §5.201; BOC §4.052)_

### 3.2 Filing fee — $300

- **LLC Certificate of Formation filing fee** — 300 USD (one-time fee; paid at filing online via SOSDirect or by mail with check payment)
- **Expedited 24-hour processing fee** — 25 USD
- **No annual franchise-tax filing fee at SOS** — This $300 fee is a one-time charge. There is no annual franchise-tax filing fee at the Secretary of State (the Public Information Report is filed separately with the Texas Comptroller at no fee).

### 3.3 Registered agent in Texas

- **Registered agent requirement** — Texas requires every LLC (and corporation) to maintain a registered agent with a Texas physical street address (BOC §5.201). The registered agent's role is to receive service of process (lawsuits) and official state correspondence on behalf of the entity.  _(BOC §5.201)_

The registered agent may be:

- The owner themselves, if they reside in Texas and accept the public-record disclosure of their home or business address.
- A Texas resident other than the owner (e.g., a co-founder, an attorney).
- A Texas entity (typically a commercial registered-agent service such as Northwest Registered Agent, Texas Registered Agent LLC, or LegalZoom). Commercial registered-agent fees range from $100 to $300 per year.

A common founder mistake is listing a residential address that the founder later vacates without updating the Secretary of State, causing official notices (including franchise-tax delinquency notices) to bounce. Update Form 401 (Statement of Change of Registered Office/Agent) within 30 days of any change.

### 3.4 No annual Secretary of State filing fee or LLC tax until revenue exceeds $2.47M

- **No Tax Due threshold applicability** — 2,470,000 USD annualized total revenue (threshold for report years 2024 and 2025; Texas charges no annual fee at the Secretary of State level regardless of revenue, unlike California ($800 annual franchise tax under R&TC §17941), Delaware ($300 annual franchise tax), and New York)
- **Below-threshold obligations** — Below the threshold, the Texas LLC owes: $0 state-level entity tax; $0 Secretary of State annual fee; Form 05-102 Public Information Report must still be filed annually (no fee, but failure to file carries severe penalties — see AUDIT FLASH POINT).
- **Margin tax rate above threshold — retail/wholesale** — 0.375% (of the lesser of (a) 70% of total revenue or (b) total revenue minus cost of goods sold or minus compensation)
- **Margin tax rate above threshold — other** — 0.75% (of the lesser of (a) 70% of total revenue or (b) total revenue minus cost of goods sold or minus compensation)
- **EZ Computation rate** — 0.331% of revenue (available for entities between $2.47M and $20M annualized revenue; see tx-margin-tax.md)

### 3.5 Public Information Report (Form 05-102) — annual, mandatory regardless of revenue

- **AUDIT FLASH POINT 1 — Missed Public Information Report** — Every Texas LLC and corporation must file Form 05-102 annually by May 15 with the Texas Comptroller, regardless of whether the entity owes any franchise tax. The PIR discloses: Entity legal name and Texas Taxpayer Number; Federal Employer Identification Number (FEIN); Mailing address; Principal office and principal place of business addresses; Names, titles, and mailing addresses of all directors, officers, members, or managers; The owners of any subsidiary entity of the reporting entity (if any).
- **PIR late filing penalty** — 50 USD (for late filing, plus interest on any underlying franchise tax due)  _(Texas Tax Code §171.362)_
- **Forfeiture consequence for repeated PIR failure** — More damaging, repeated failure to file (typically two consecutive report years) triggers forfeiture of the entity's corporate privileges under Texas Tax Code §171.251–§171.252 and ultimately administrative dissolution of the entity by the Secretary of State on certification by the Comptroller.  _(Texas Tax Code §171.251–§171.252)_
- **Personal liability upon forfeiture** — The practical consequence of forfeiture is loss of limited liability protection — directors, officers, members, and managers may become personally liable for the entity's debts incurred during the forfeiture period under Texas Tax Code §171.255. This single risk justifies the cost of a competent registered agent or compliance vendor for any Texas entity.  _(Texas Tax Code §171.255)_

### 3.6 Operating agreement

- **Operating agreement not required but authorized** — Texas does not require an LLC to file or even adopt an operating agreement, but BOC §101.052 specifically authorizes one, and the default statutory provisions are generally unfavorable for asymmetric ownership or capital-call structures.  _(BOC §101.052)_

Best practice for any multi-member LLC is to adopt a written operating agreement covering:

- Capital contributions and capital accounts
- Profit/loss/distribution allocations (which need not track ownership percentages under §704(b) regulations)
- Management structure (member-managed vs manager-managed)
- Voting thresholds for major decisions
- Buy-sell provisions on death, disability, withdrawal, or expulsion
- Tax matters partner / partnership representative designation
- Dissolution and winding-up

For a single-member LLC, an operating agreement is still recommended to evidence the intent to operate as a separate entity (supporting the corporate-veil analysis under Texas piercing-the-veil doctrine, e.g., Castleberry v. Branscum, 721 S.W.2d 270 (Tex. 1986), and the legislative limitations on veil-piercing under BOC §21.223).

### 3.7 EIN and federal classification

- **EIN application and default classifications** — After SOS filing, the founder applies for a Federal Employer Identification Number (EIN) via IRS Form SS-4 (free, instant online). A single-member LLC defaults to disregarded entity status for federal tax (reported on the owner's Schedule C). A multi-member LLC defaults to partnership status (Form 1065). Either may elect to be taxed as a C-corp (Form 8832) or as an S-corp (Form 2553) — see us-s-corp-election-decision.

## 4. Texas C-Corp Formation

The Texas For-Profit Corporation is used primarily by venture-backed startups, businesses planning a public offering, and certain professional firms.

### 4.1 Certificate of Formation (Form 201)

- **C-Corp Certificate of Formation content requirements** — Formation is accomplished by filing a Certificate of Formation — For-Profit Corporation (SOS Form 201) under BOC §3.001 et seq. and §21.001 et seq. Required content: 1. Entity name ending in "Corporation," "Company," "Incorporated," "Limited," "Corp.," "Co.," "Inc.," or "Ltd." Must be distinguishable on SOS records. 2. Registered agent — Texas street address. 3. Number of authorized shares — typically 10,000,000 shares of common stock at $0.0001 par value for a venture-track startup, or 1,000–10,000 shares with no par value for a closely held corporation. 4. Initial directors — names and addresses (minimum one director under BOC §21.403). 5. Organizer — the incorporator. 6. Purpose — generally "any lawful purpose."  _(BOC §3.001 et seq.; BOC §21.001 et seq.; BOC §21.403)_

### 4.2 Filing fee — $300

- **C-Corp Certificate of Formation filing fee** — 300 USD (same as the LLC; expedited 24-hour processing adds $25)

### 4.3 Public Information Report — annual

- **C-Corp PIR requirement** — Same as the LLC (see §3.5). Form 05-102 is filed annually by May 15 regardless of revenue. C-Corps and LLCs use the same PIR form.

### 4.4 Franchise/margin tax

- **No Tax Due threshold for franchise/margin tax** — 2,470,000 USD annualized total revenue (for 2024 and 2025 report years)
- **Retail or wholesale rate** — 0.375% of taxable margin (for retail or wholesale businesses defined under Texas Tax Code §171.002(c))  _(Texas Tax Code §171.002(c))_
- **Other businesses rate** — 0.75% of taxable margin
- **EZ Computation rate** — 0.331% of revenue (available for entities between $2.47M and $20M annualized revenue; see tx-margin-tax.md)

A C-Corp engaged in software development, consulting, professional services, or SaaS would generally pay the 0.75% rate (or the 0.331% EZ rate if eligible and beneficial). A C-Corp engaged in retail e-commerce reselling tangible personal property may qualify for the 0.375% retail rate, subject to the qualification rules in §171.002(c) which require, among other things, that less than half of the entity's total revenue come from the sale of items produced or processed by the entity. See tx-margin-tax.md for detailed computation.

### 4.5 Federal C-Corp taxation

- **Federal corporate tax rate** — 21% (flat corporate rate established by the Tax Cuts and Jobs Act (TCJA, 2017) and made permanent at 21% by subsequent legislation)
- **Double taxation pattern and Texas advantage** — Distributions to shareholders are taxed at the shareholder level as qualified dividends (preferential rates) or as compensation (ordinary rates). The combined federal C-corp rate (21% corporate + 15–23.8% qualified dividend) creates the "double taxation" pattern. For a Texas-resident shareholder, however, the dividend-distribution leg owes no Texas tax, making the Texas C-corp meaningfully more attractive than the California C-corp for a closely held business that plans to distribute earnings to a Texas-resident shareholder.

### 4.6 S-corp election

- **S-corp election timing and Texas treatment** — A Texas C-Corp may elect S-corporation status by filing Form 2553 with the IRS within 2 months and 15 days of the start of the tax year for which the election is to be effective (or for the entity's first tax year). The S-corp election does not change Texas-level treatment — Texas treats both C-corps and S-corps identically as taxable entities for franchise-tax purposes (BOC and Tax Code do not recognize the S-corp election). The S-corp election affects only federal income tax and Texas self-employment tax exposure (Texas has no SE-tax equivalent). See us-s-corp-election-decision.

## 5. Texas Series LLC

- **Series LLC statutory basis** — Texas permits Series LLCs by statute under BOC §101.601–§101.621, added by Senate Bill 1442 (81st Legislature, 2009 Regular Session), effective September 1, 2009. The Series LLC is a single legal entity that may establish one or more internal "series," each of which can hold separate assets, conduct separate operations, have separate members, and — critically — be firewalled from the liabilities of the parent LLC and of every other series, provided certain statutory formalities are observed.  _(BOC §101.601–§101.621; Senate Bill 1442 (81st Legislature, 2009 Regular Session))_

### 5.1 What is a Series LLC?

- **Series LLC definition** — A Series LLC is a master LLC that creates internal protected series under its governing documents. Each series: May hold title to assets in its own name; May contract in its own name; May sue and be sued in its own name; Has its own members, managers, and economic rights; Has liabilities enforceable only against the assets of that series, not against the parent LLC or any other series (BOC §101.602(b)). The liability shield between series is sometimes called the "internal liability shield" or the "firewall." It is conceptually similar to having multiple separate LLCs but with a single SOS filing, a single registered agent, and potentially a single set of governing documents.  _(BOC §101.602(b))_

### 5.2 Statutory requirements for the liability shield (BOC §101.602(b))

- **Four requirements for effective firewall** — For the firewall to be effective, the master LLC must satisfy all of the following: 1. Notice in the Certificate of Formation — the certificate must contain notice that the LLC may establish protected series, and that the debts of any series are enforceable only against that series. 2. Notice in the operating agreement (company agreement) — the agreement must establish at least one series and provide for the limitations on liability. 3. Separate records — the records of each series must account for the assets of that series separately from the assets of the LLC generally and of any other series. This is the single most-litigated requirement and the most common source of firewall failures. 4. Name — each series typically operates under a name that includes the master LLC name and the series designation (e.g., "Smith Real Estate Holdings LLC – Series A").  _(BOC §101.602(b))_

A failure to maintain separate records — commingled bank accounts, commingled bookkeeping, commingled tax filings without proper allocation — risks a court collapsing the series and treating all series as a single pool of assets reachable by any creditor. The practical bookkeeping discipline required is significant and is the most common reason a Series LLC is not the right answer for a small operator.

### 5.3 When the Series LLC makes sense

- Real estate investors holding multiple rental properties, where each property is isolated from the others' tort and contract liabilities (slip-and-fall, tenant default, environmental).
- Multi-brand operators running several distinct product lines or DBAs that should not cross-contaminate liability.
- Family wealth structures where each branch or generation operates a separate series with its own beneficiaries.

### 5.4 When the Series LLC is overkill

- Single-business operators (a freelance software developer with one consulting practice does not need a Series LLC — a plain SMLLC suffices).
- Operators who will not maintain rigorous separate books for each series.
- Operators in states that do not recognize the Texas Series LLC firewall — interstate operation requires careful analysis because not every state recognizes series isolation.

### 5.5 Filing and fee

- **Series LLC filing fee** — 300 USD (A Series LLC is filed on the same Certificate of Formation (Form 205) as a regular LLC, with the series notice added under Section 5 ("Supplemental Provisions/Information").)

### 5.6 Federal tax treatment of Series LLCs

- **Federal vs Texas treatment of series** — The IRS treats each series as a separate entity for federal tax purposes under Proposed Treasury Regulation §301.7701-1(a)(5) (proposed in 2010 and not yet finalized but generally followed in practice). Each series files its own federal tax return as appropriate (Schedule C for a single-member series disregarded for federal tax; Form 1065 for a multi-member series; Form 1120 if a C-corp election is made). For Texas franchise-tax purposes, the Comptroller treats the master Series LLC and all its protected series as a single taxable entity filing one combined franchise tax return and one PIR — a notable divergence from federal treatment that simplifies state compliance.  _(Proposed Treasury Regulation §301.7701-1(a)(5))_

## 6. Texas Foreign Qualification (Certificate of Authority)

- **Foreign entity definition** — A "foreign" entity in Texas terminology is an entity formed in another state (e.g., a Delaware C-Corp, a California LLC, a Wyoming LLC) that does business in Texas. Foreign entities transacting business in Texas must register with the Texas Secretary of State by filing for a Certificate of Authority.

### 6.1 What constitutes "transacting business" in Texas?

- **Safe harbor activities and triggering activities** — BOC §9.251 lists activities that do not constitute transacting business, including: maintaining a bank account, holding meetings, conducting an isolated transaction completed within 30 days, and being a limited partner in a Texas partnership. Activities outside this safe harbor — having a physical office, employing Texas residents, owning Texas real property, conducting regular business with Texas customers — generally do constitute transacting business and trigger the registration requirement.  _(BOC §9.251)_
- **Franchise-tax nexus broader than SOS standard** — The Texas Comptroller's franchise-tax nexus standard (Texas Comptroller Rule §3.586) is broader than the Secretary of State's "transacting business" standard. An out-of-state entity may owe franchise tax even when it is below the SOS-registration threshold — see §9 below.  _(Texas Comptroller Rule §3.586)_

### 6.2 Application for Registration (Form 304 for LLC, Form 301 for corporation)

- **Required content for foreign qualification application** — Required content: 1. Entity legal name (and a fictitious name if the legal name is not available in Texas) 2. State of formation 3. Date of formation 4. Federal Employer Identification Number 5. Principal office address (home state) 6. Texas registered agent name and address 7. Statement that the entity is in existence and good standing in its home state (typically evidenced by a Certificate of Existence from the home-state Secretary of State, dated within 91 days of filing in Texas under BOC §9.005) 8. Names and addresses of governing persons (members/managers for LLC; directors/officers for corporation)  _(BOC §9.005)_

### 6.3 Filing fee — $750

- **Foreign qualification filing fee** — 750 USD (substantially higher than the $300 domestic-formation fee)
- **Practical implication of fee differential** — This differential is the principal reason a Texas-resident founder forming a new business should generally form directly as a Texas entity rather than forming in Delaware or Wyoming and qualifying back into Texas. For a venture-backed startup planning to raise from institutional VC investors, the $450 differential is trivial relative to the strategic value of Delaware formation (see §10). For a bootstrapped freelance developer, the $450 differential is meaningful — and the operational complexity of managing two states' compliance (Delaware annual franchise tax minimum $300, Delaware registered agent ~$100/year, Delaware Certificate of Good Standing for annual Texas confirmation) compounds the case for direct Texas formation.

### 6.4 Ongoing obligations of a qualified foreign entity

- **Ongoing obligations list** — Once qualified, the foreign entity must: Maintain its Texas registered agent; File annual Form 05-102 (Public Information Report) with the Texas Comptroller; File annual franchise tax (Form 05-158 Long Form or Form 05-169 EZ Computation), with $0 owed if under the No Tax Due threshold; Maintain good standing in its home state (and file annual reports there); File a withdrawal (Form 608 for LLC, Form 612 for corporation) when ceasing Texas operations, $15 fee.

## 7. Annual Public Information Report (Form 05-102) — Deep Dive

Because the PIR is the single most-missed Texas compliance item and the single greatest source of post-formation Texas legal trouble, this section provides additional detail beyond §3.5.

### 7.1 Who must file

- **Taxable entity list** — Every "taxable entity" under Texas Tax Code §171.0002 must file an annual franchise tax report, which includes Form 05-102 as a component. Taxable entities include: Texas LLCs; Texas corporations (C-corps and S-corps both); Texas Series LLCs (one filing covers all series); Foreign LLCs and corporations qualified to do business in Texas; Foreign LLCs and corporations with Texas nexus even if not formally qualified (Comptroller's economic-nexus rule); Texas limited partnerships (LPs) and limited liability partnerships (LLPs); Texas professional associations (PAs) and professional corporations (PCs); Texas business trusts. Sole proprietorships and general partnerships are not taxable entities and have no PIR obligation. Single-member LLCs disregarded for federal tax are nonetheless separate taxable entities for Texas franchise-tax purposes and must file the PIR.  _(Texas Tax Code §171.0002)_

### 7.2 Filing deadline

- **PIR annual filing deadline** — May 15 (covering the prior calendar year (the "report year"). An entity formed in 2025 first files in 2026 for the 2025 calendar year (or, more precisely, the period from formation through the prior December 31).)
- **Extension availability** — An automatic extension to November 15 is available by filing Form 05-164 by May 15 and paying any estimated tax due. For entities below the No Tax Due threshold, the extension form is generally unnecessary because no tax is owed, but the PIR still must be filed by May 15.  _(Form 05-164)_

### 7.3 No filing fee

- **PIR late filing penalty** — 50 USD (for late filing, plus interest on any underlying franchise tax due)  _(Texas Tax Code §171.362)_

### 7.4 Forfeiture of corporate privileges (AUDIT FLASH POINT 1, expanded)

- **Grounds for forfeiture** — Under Texas Tax Code §171.251, the Comptroller may forfeit an entity's "corporate privileges" if the entity: (a) does not file a required report (b) does not pay tax or penalty when due, or (c) does not permit an authorized examination of records. Forfeiture occurs by Comptroller certification to the Secretary of State after notice.  _(Texas Tax Code §171.251)_
- **Consequences of forfeiture** — Once forfeited, the entity: May not sue or defend in Texas court (Texas Tax Code §171.252); Loses its "right to do business" in Texas; Directors, officers, members, and managers become personally liable for debts created or incurred during the forfeiture period under Texas Tax Code §171.255.  _(Texas Tax Code §171.252; Texas Tax Code §171.255)_

The §171.255 personal liability is the single most dangerous consequence of a missed PIR. A founder who forms a Texas LLC for liability protection, then fails to file the PIR for two consecutive years, may discover during a lawsuit that the LLC has been forfeited and that they are personally liable for all debts incurred during the forfeiture window — exactly the outcome the LLC was meant to prevent.

Revival is available by filing all delinquent reports, paying all tax, penalty, and interest, and filing an Application for Reinstatement (Form 801) with the SOS along with a Tax Clearance Letter from the Comptroller. Total cost of revival can range from a few hundred dollars (small operator, one missed PIR) to many thousands of dollars (larger operator with multiple years of margin tax owed plus penalties and interest).

### 7.5 Information disclosed publicly

- **PIR is a public record** — The PIR is a public record. It discloses the names and mailing addresses of all directors, officers, members, or managers.

Owners concerned about privacy commonly:

- Use a commercial registered agent at a business address (not the home address)
- List a business mailing address rather than a home address
- Operate through a Texas LLC with a manager-managed structure, listing only a manager (potentially the founder's professional title) rather than all members

There is no legal mechanism to keep the PIR private — Texas has chosen public disclosure of ownership and governance for all taxable entities, which is a distinguishing feature of the Texas regime relative to states like Wyoming, New Mexico, or Nevada that permit substantial owner anonymity.

## 8. Doing Business in Texas — Economic Nexus Thresholds (Post-Wayfair)

- **Post-Wayfair adoption of economic nexus** — The Texas Comptroller adopted economic-nexus standards for both sales tax and franchise tax in the wake of the 2018 Supreme Court decision in South Dakota v. Wayfair, Inc., 138 S. Ct. 2080 (2018), which overturned the physical-presence requirement of Quill Corp. v. North Dakota, 504 U.S. 298 (1992).  _(South Dakota v. Wayfair, Inc., 138 S. Ct. 2080 (2018); Quill Corp. v. North Dakota, 504 U.S. 298 (1992))_

### 8.1 Sales tax economic nexus — $500,000 (Texas Tax Code §151.107)

- **Sales tax economic nexus threshold** — 500,000 USD in preceding 12 calendar months (total Texas revenue from sale of tangible personal property and taxable services into Texas; Texas does not have a transaction-count threshold (unlike some states with "$100,000 or 200 transactions"). See tx-sales-tax.md for sales-tax mechanics.)  _(Texas Tax Code §151.107)_

### 8.2 Franchise tax economic nexus (Texas Comptroller Rule §3.586)

- **Franchise tax nexus — gross receipts threshold** — 500,000 USD in Texas-sourced gross receipts (the most-cited threshold; during the federal income tax accounting period)  _(Texas Comptroller Rule §3.586)_
- **Franchise tax nexus — payroll threshold** — 50,000 USD in payroll (paid to Texas residents or for services performed in Texas)  _(Texas Comptroller Rule §3.586)_
- **Franchise tax nexus — payroll threshold** — 50,000 USD in payroll (paid to Texas residents or for services performed in Texas)  _(Texas Comptroller Rule §3.586)_
- **Physical presence nexus trigger** — Physical presence in Texas — owning or renting an office, store, or warehouse; having Texas employees; etc. If any one of these thresholds is met, the entity has Texas nexus and must file a Texas franchise tax report (Form 05-158 or 05-169) and a PIR (Form 05-102). The economic-nexus standard applies independently of the Secretary of State's "transacting business" registration standard — an entity may have economic nexus for Comptroller purposes without being registered for SOS purposes, in which case the entity may be both delinquent on franchise tax and operating in violation of BOC §9.051 (transacting business without registration).  _(Texas Comptroller Rule §3.586; BOC §9.051)_

### 8.3 The dual-compliance trap

An out-of-state founder selling SaaS into Texas may inadvertently trigger:

- Sales tax registration if SaaS is treated as a "data processing service" (see tx-sales-tax.md)
- Franchise tax filing if Texas-sourced gross receipts exceed $500,000
- Secretary of State foreign qualification (Certificate of Authority, $750)

The three obligations are administered by two different state agencies (Comptroller for tax; SOS for registration) and have overlapping but non-identical thresholds. A common practitioner approach is: once a non-Texas client crosses $500,000 in Texas revenue or hires a Texas-resident employee, evaluate all three compliance triggers together.

### 8.4 Sourcing of receipts to Texas

- **Sourcing rules by receipt type** — For franchise tax, Texas-sourced gross receipts are determined under Texas Tax Code §171.103 and Comptroller Rule §3.591. For services, receipts are sourced based on where the service is performed (cost-of-performance / market-based hybrid). For sales of tangible personal property, receipts are sourced to the destination of the shipment. For software and SaaS, sourcing follows the location of the user or customer, subject to the technical rules in Rule §3.591. For internet hosting receipts, sourcing follows the location of the customer (Texas Tax Code §171.106(g)).  _(Texas Tax Code §171.103; Comptroller Rule §3.591; Texas Tax Code §171.106(g))_

## 9. BOI / Corporate Transparency Act (CTA) Status

- **CTA overview** — The Corporate Transparency Act (CTA), enacted as part of the National Defense Authorization Act for Fiscal Year 2021 (P.L. 116-283, Title LXIV), required most U.S. entities to file a Beneficial Ownership Information (BOI) report with the Financial Crimes Enforcement Network (FinCEN) disclosing each beneficial owner (any individual owning 25% or more or exercising substantial control).  _(National Defense Authorization Act for Fiscal Year 2021 (P.L. 116-283, Title LXIV))_

### 9.1 Current status — stayed

- **CTA stay status as of November 2025** — As of the version date of this skill (November 2025), the CTA reporting requirement has been stayed by federal court injunction and by subsequent FinCEN regulatory action. In December 2024 the U.S. District Court for the Eastern District of Texas issued a nationwide preliminary injunction in Texas Top Cop Shop, Inc. v. Garland halting CTA enforcement. The Fifth Circuit, the Supreme Court, and FinCEN's interim final rule (March 2025) have further reshaped the landscape. The current operative position is that domestic U.S. entities are not required to file BOI reports, while foreign entities registered to do business in the U.S. remain subject to a modified reporting regime.  _(Texas Top Cop Shop, Inc. v. Garland; FinCEN interim final rule (March 2025))_

This area is fast-moving. Practitioners should verify the current FinCEN guidance and any pending litigation before advising a client on BOI filing — the guidance in this skill is current as of November 2025 only.

### 9.2 What entities should do now

- **Conservative approach pending stabilization** — 1. Collect the BOI information (names, dates of birth, addresses, identifying numbers, image of identifying document) for all 25%+ owners and substantial-control individuals even if not filing, so the filing can be completed quickly if requirements re-activate. 2. Document the file-or-no-file decision with citation to the current FinCEN guidance and any operative injunction. 3. Monitor FinCEN.gov and the docket in Texas Top Cop Shop and related cases for changes. 4. For entities formed in 2024 or 2025 that previously filed a BOI report under the original CTA timeline, no withdrawal is currently required — the prior filings remain on record.

### 9.3 Penalties (if reinstated)

- **CTA civil penalty** — 591 USD per day (inflation-adjusted civil penalty for willful failure to report; if the requirement is reinstated, these penalties may apply prospectively from the reinstatement date)
- **CTA criminal penalty** — up to $10,000 and 2 years imprisonment (for willful violations)

## 10. Texas vs Delaware for Startups

The Texas-versus-Delaware question is the single most-asked entity-formation question by sophisticated founders. The answer is highly context-dependent.

### 10.1 Where Delaware wins

- **VC expects Delaware C-corps** — Substantially all institutional venture capital term sheets assume — and many require — that the portfolio company be a Delaware C-Corp. Reasons include: Court of Chancery — Delaware's specialized business court, with no jury trials, with judges (Chancellors and Vice Chancellors) who are specialists in corporate law, and with a deep body of precedent on fiduciary duty, deal protection, takeover defense, and stockholder voting. Texas business courts (established 2024 under HB 19, 88th Legislature) are too new to have built equivalent precedent depth. DGCL flexibility — the Delaware General Corporation Law permits drag-along rights, preferred stock with negotiated rights, sophisticated anti-dilution mechanics, and other deal structures with well-established case-law support. Lawyer fluency — every venture-track lawyer in the U.S. knows Delaware corporate law; only Texas-track lawyers know Texas BOC §21 with equivalent depth.  _(HB 19 (88th Legislature); BOC §21)_
- **Delaware corporation filing fee** — 89 USD (substantially less than Texas's $300, though Delaware franchise tax can run $400+ per year for typical startup share counts using the authorized-shares method (and $400 minimum using the assumed-par-value-capital method))

For a startup planning to raise institutional VC, Delaware C-Corp is the default.

### 10.2 Where Texas wins

- **Texas advantages for bootstrapped or Texas-resident founders** — Texas wins on personal tax and ongoing cost for the bootstrapped founder or for the founder who will hold company stock long-term as a Texas resident. - No Texas personal income tax — a Texas-resident founder who eventually liquidates her Delaware C-Corp shares pays 0% Texas tax on the capital gain. (Federal capital gains tax still applies, of course, and §1202 QSBS exclusion may apply to qualified small business stock held more than 5 years.) - No Texas tax on dividends — Texas-resident shareholders of either a Texas or Delaware C-Corp pay 0% Texas tax on dividend distributions. - Lower formation cost for direct Texas formation — $300 vs Delaware's $89 SOS fee plus the Texas $750 foreign qualification fee (total $839) if forming Delaware and operating in Texas. - No Texas franchise tax under $2.47M revenue — a bootstrapped Texas LLC with $1M in revenue pays $0 Texas franchise tax; the same LLC formed in Delaware and operating in Texas would also pay $0 Texas franchise tax (foreign qualification triggers Texas filing but not tax under the threshold) but would owe Delaware annual franchise tax ($300 minimum for an LLC; variable for a corporation).

### 10.3 The hybrid pattern

A common pattern for sophisticated founders:

1. Form a Delaware C-Corp for the operating company that will raise VC.
2. Foreign-qualify the Delaware entity into Texas (Certificate of Authority, $750).
3. Maintain Texas residency for the founder personally so that all founder-level capital gains, dividends, and salary are state-tax-free.
4. Operate the company in Texas (Austin office, Texas employees) so that the Delaware entity has substantive Texas presence.

This pattern pays the Delaware corporate fees (formation, annual franchise tax, registered agent) for VC compatibility, while capturing the personal-tax benefit of Texas residency for the founder.

For a founder who is not raising institutional VC — a freelance developer forming an LLC, a real estate investor, a consultant, a small e-commerce operator — the analysis collapses to direct Texas formation: lower formation fee, no Delaware compliance overhead, full Texas personal-tax benefit.

### 10.4 Decision matrix

**Founder profile decision matrix**

| Founder profile | Recommended formation state |
| --- | --- |
| Venture-track startup raising Series A+ | Delaware C-Corp, qualify into Texas |
| Pre-seed startup with no VC plans yet | Texas LLC (convertible to Delaware C-Corp pre-financing) |
| Bootstrapped SaaS / consulting | Texas LLC |
| Freelance developer single-member | Texas LLC (or sole prop if revenue < $50K) |
| Real estate investor (multiple properties) | Texas Series LLC |
| Multi-state e-commerce with Texas operations | Texas LLC (or Delaware LLC if multi-state nexus already triggers many states) |
| Family wealth holding entity | Texas Series LLC or Texas LLC with subsidiaries |

## 11. Common Errors and Pitfalls

### 11.1 AUDIT FLASH POINT 1 — Forgetting the Public Information Report

- **Symptom, root cause, and mitigation** — Symptom: Founder forms a Texas LLC, never registers with the Texas Comptroller, never files Form 05-102, and is surprised when the LLC is forfeited two years later and they are personally sued for an LLC debt. Root cause: Texas Secretary of State filing is decoupled from Texas Comptroller franchise-tax registration. Filing the Certificate of Formation does not automatically register the entity with the Comptroller; the entity must independently register for a Texas Taxpayer Number with the Comptroller (Form AP-114 for foreign entities; Texas-formed entities receive a Taxpayer Number automatically but must still file annual reports). Mitigation: Calendar the May 15 PIR deadline annually. Use a commercial registered agent or compliance vendor that sends annual filing reminders. Verify Comptroller registration within 30 days of SOS formation. Confirm receipt of Comptroller welcome letter (typically mailed 30–60 days after SOS formation).  _(Form AP-114)_

### 11.2 AUDIT FLASH POINT 2 — Confusing "no franchise tax under $2.47M" with "no margin tax"

- **Symptom, root cause, worked example, and mitigation** — Symptom: Founder treats the No Tax Due threshold as a permanent exemption and is shocked to receive a $5,000+ margin tax bill the year revenue crosses $2.47M. Root cause: The No Tax Due threshold under Texas Tax Code §171.002(d) is a year-by-year threshold based on annualized total revenue. Crossing the threshold for a single report year triggers full margin tax for that report year. There is no phase-in, no smoothing, no de minimis credit above the threshold. A taxpayer with $2,500,000 in revenue is liable for margin tax computed on the full taxable margin — typically 0.331% EZ rate × $2,500,000 = $8,275 in margin tax, not 0.331% of the $30,000 excess. Mitigation: Monitor revenue against the threshold quarterly. Plan for the year-of-crossover margin tax bill. Consider whether deferring revenue into a subsequent year, or accelerating deductible expenses into the crossover year, reduces total tax (a margin-tax-aware year-end planning exercise).  _(Texas Tax Code §171.002(d))_

### 11.3 Mismatch between SOS registered agent and Comptroller mailing address

- **Symptom and mitigation** — Symptom: Comptroller notices (franchise tax delinquency, audit notices) are mailed to a stale address and never reach the owner. Mitigation: Update both the SOS registered agent address (Form 401) and the Comptroller mailing address (online via Texas Comptroller's Webfile portal) whenever the entity moves. Verify both addresses annually as part of the PIR filing.

### 11.4 Treating Series LLC bookkeeping casually

- **Symptom and mitigation for Series LLC bookkeeping** — Symptom: Founder forms a Series LLC with three series, deposits all rental income into one bank account, prepares one Schedule E, and is surprised when a tenant-injury judgment in Series A is satisfied out of Series B's property because a court collapses the series for failure to maintain separate records. Mitigation: Each series should have: - A separate bank account in the series's name - Separate bookkeeping (separate QuickBooks file or separate class/location coding) - Separate federal tax filings where required (separate Schedule E columns or separate disregarded entity treatment) - Series-specific contracts (lease agreements signed by "Series A," not by the master LLC) - Series-specific insurance policies

### 11.5 Forgetting to update the registered agent on a residential move

- **Symptom and mitigation for registered agent updates** — Symptom: Founder uses her home address as her LLC's registered agent address, moves to a new house, forgets to file Form 401, and never receives service of process in a lawsuit — leading to a default judgment. Mitigation: Use a commercial registered agent ($100–$300/year) to insulate the registered-agent function from personal moves. Calendar a quarterly check of the SOS public record to confirm registered agent and address are current.

### 11.6 Filing Delaware C-Corp without qualifying in Texas while operating from Texas

- **Symptom and mitigation for unqualified foreign operation** — Symptom: Texas-resident founder forms a Delaware C-Corp, operates the business from Texas (Texas employees, Texas office, Texas customers) but never foreign-qualifies. SOS later catches up, and the corporation faces back-fees, penalties, and a period of operating in unauthorized status under BOC §9.051 — including potential inability to enforce Texas contracts during the unqualified period. Mitigation: Foreign-qualify (Form 301 or 304, $750) within 90 days of commencing Texas operations.  _(BOC §9.051)_

## 12. Worked Examples

### 12.1 Example 1 — Austin tech startup raising seed financing

Two technical co-founders in Austin (one ex-Google, one ex-Meta) form a software company in February 2025 to build an AI-powered developer tool. They have $500,000 in friends-and-family funding committed and plan to raise a $3M seed round from institutional VC in Q3 2025. Projected revenue 2025: $0–$100,000 (closed alpha). 2026: $1–2M ARR.

The founders intend to raise institutional VC. Substantially all institutional VC term sheets require a Delaware C-Corp. **Recommended structure:**

- **Delaware C-Corp formation** — File Certificate of Incorporation with Delaware Division of Corporations, $89 fee. Authorize 10,000,000 shares of common stock at $0.0001 par value. Initial board: both co-founders. 5,000,000 shares issued to each co-founder, vesting over 4 years with 1-year cliff (per standard VC expectations).

- **Texas foreign qualification** — File Form 301 with Texas SOS, $750 fee, within 90 days of commencing Texas operations.
- **Texas Comptroller registration** — Register for Texas Taxpayer Number via Comptroller Webfile.
- **Texas registered agent** — Northwest Registered Agent (~$125/year) at Texas business address.
- **Texas employer registration** — Texas Workforce Commission unemployment insurance registration before first paycheck.
- **EIN** — IRS Form SS-4, free, instant online.
- **83(b) elections** — Both co-founders file 83(b) elections within 30 days of stock issuance to elect immediate income recognition on $0.0001 × 5,000,000 = $500 of restricted stock, eliminating future ordinary-income recognition on appreciation.

- Delaware annual report (March 1, 2026): $50 corporate report + Delaware franchise tax ($400 minimum assumed-par-value-capital method, or up to thousands using authorized-shares method on 10M shares — typically the founders' counsel switches to assumed-par-value-capital method to keep DE franchise tax minimal).
- Texas Form 05-102 PIR (May 15, 2026): $0 (revenue under No Tax Due threshold).
- Texas franchise tax Form 05-163 No Tax Due (May 15, 2026): $0 owed, filing required.
- Federal Form 1120 C-Corp return (April 15, 2026, extension available to October 15): minimal taxable income given pre-revenue stage.

- Delaware formation: $89 + ~$150 registered agent
- Delaware franchise tax: ~$450
- Texas foreign qualification: $750
- Texas registered agent: ~$125
- **Approximate total: $1,564**

A Texas C-Corp could be formed for $300 and operate in Austin without foreign qualification. However, when the seed-round term sheet arrives in Q3 2025, the company would need to **convert** from Texas to Delaware (typically via a Texas-to-Delaware conversion under BOC §10.101 or a merger), incurring legal fees of $5,000–$15,000 and triggering complex federal tax analysis under §368 reorganization rules. The $1,500 upfront cost of direct Delaware formation is materially cheaper than the eventual conversion cost.

### 12.2 Example 2 — Houston real estate investor with five rental properties

Texas-resident investor owns five rental single-family homes in Houston with combined annual rental income of $180,000 and combined net rental income (after mortgage interest, property tax, depreciation, repairs, property management) of $35,000. Currently holds all five properties personally; tenant on Property 3 sued for a slip-and-fall injury (~$50,000 claim). Investor wants liability isolation.

- **Form Texas Series LLC** — File Certificate of Formation (Form 205) with series notice in Section 5, $300 fee. Master entity name: 'Smith Family Real Estate Holdings, LLC.'
- **Establish five series** — By operating agreement amendment, establish Series A through Series E, one for each property.
- **Quit-claim deeds** — Deed each property from the investor (or current owner) into the appropriate series, e.g., 'Smith Family Real Estate Holdings, LLC – Series A.' File deeds in the county records. (Watch for due-on-sale clause in existing mortgages; lender consent may be required.)
- **Separate bank accounts** — One operating account per series.
- **Separate bookkeeping** — QuickBooks with class tracking by series, or separate QuickBooks files per series.
- **Operating agreement** — Single master agreement covering all five series, with appendices establishing each series.
- **Texas Taxpayer Number** — Single Taxpayer Number for the master LLC; all series report on a single combined Texas franchise tax return.
- **Federal tax treatment** — Each series is a separate entity for federal tax; for a single-owner investor, each series is a disregarded entity. All rental income flows to the investor's Schedule E with separate columns for each series.
- **Insurance** — Separate landlord insurance policy per series, naming the series as the named insured.

- Texas PIR Form 05-102: $0 fee, May 15.
- Texas franchise tax Form 05-163 No Tax Due: $0 owed, $180,000 combined revenue is well under $2.47M threshold.
- Federal Schedule E with five columns.
- Registered agent: ~$125/year.

- **Pitfall to avoid — separate records requirement** — Investor must rigorously maintain separate bookkeeping. The single most-litigated point in Texas Series LLC case law is the §101.602(b)(3) separate-records requirement. Sloppy bookkeeping risks collapsing the firewall, exposing all five properties to the slip-and-fall judgment on Property 3.  _(§101.602(b)(3))_

### 12.3 Example 3 — Dallas e-commerce sole proprietor crossing the $2.47M threshold

Dallas-resident e-commerce operator sells custom apparel via Shopify and Amazon FBA. 2024 revenue: $1,800,000. Projected 2025 revenue: $3,200,000. Operates as a sole proprietorship through 2024. Wants to formalize the business.

- **Form Texas LLC** — Certificate of Formation, $300, effective January 1, 2025 (if not already past). Default federal classification: disregarded entity (single-member LLC reports on Schedule C).
- **Evaluate S-corp election** — At $3.2M projected revenue with significant ordinary-income exposure to self-employment tax, an S-corp election under Form 2553 may save meaningful SE tax. Defer detailed analysis to `us-s-corp-election-decision`.  _(Form 2553)_
- **Texas franchise tax planning — retail rate qualification** — Revenue will exceed the $2,470,000 No Tax Due threshold in 2025. Margin tax for 2025: Retail rate available if entity qualifies under §171.002(c) (resale of items not produced by the entity) — for custom apparel that is produced by the entity (designs printed on demand by contracted print-on-demand vendors), the retail-rate qualification is fact-specific and depends on whether the entity is treated as the producer. Conservative position: 0.75% rate or 0.331% EZ rate, not 0.375% retail rate.  _(§171.002(c))_
- **Taxable margin computation** — Taxable margin: lesser of (a) 70% × $3,200,000 = $2,240,000 or (b) total revenue minus COGS, or (c) total revenue minus compensation, or (d) total revenue minus $1,000,000 (the 'compensation alternative').
- **Conservative margin tax estimate** — Conservative estimate using 70% method × 0.75% = $16,800 of margin tax, or EZ Computation at 0.331% × $3,200,000 = $10,592. EZ Computation likely beneficial — see `tx-margin-tax.md`.  _(tx-margin-tax.md)_
- **Texas sales tax** — Apparel is taxable tangible personal property in Texas. Operator should already be registered for Texas sales tax (Form AP-201) and collecting on Texas-destination sales. See `tx-sales-tax.md`.  _(tx-sales-tax.md)_
- **Quarterly federal estimated tax** — Form 1040-ES quarterly payments; see `us-quarterly-estimated-tax`.  _(us-quarterly-estimated-tax)_
- **Public Information Report** — Form 05-102 due May 15, 2026 covering 2025 report year. AUDIT FLASH POINT — operator must file this even though the LLC just formed.

Operator should not assume that the No Tax Due threshold protects them in 2025. Revenue projection of $3.2M crosses the $2.47M threshold by ~$730K, triggering full margin tax computed on the full taxable margin (no phase-in). Plan for the ~$10,000–$17,000 margin tax bill at year-end and reserve cash accordingly.

### 12.4 Example 4 — Foreign founder forming a Texas LLC

Founder is a Maltese citizen and Maltese tax resident operating a software consulting practice serving U.S. clients. Wants to form a U.S. entity for client billing, U.S. payment processing (Stripe, PayPal), and U.S. banking. Has no U.S. residence, no U.S. employees, no U.S. customers in any single state above any economic-nexus threshold. Projected U.S. revenue: $300,000/year.

- **Texas LLC formation** — Certificate of Formation, $300, registered agent in Texas (commercial registered agent required since founder has no Texas presence; ~$150/year).
- **EIN application** — IRS Form SS-4. Foreign founder without SSN/ITIN must apply by fax or mail (cannot use online application). Processing time: 4–6 weeks. EIN required for U.S. bank account opening.
- **U.S. bank account** — Wise Business, Mercury, or similar online business banking accepts foreign-owner Texas LLCs. Traditional banks (Chase, Bank of America) typically require U.S. presence.
- **W-8BEN-E or W-8BEN** — Provided to U.S. payors to claim treaty benefits (Malta-U.S. tax treaty) and avoid 30% withholding.
- **Federal tax classification** — Single-member LLC owned by foreign individual is a disregarded entity for federal tax. The foreign individual reports U.S.-effectively-connected income on Form 1040-NR. If the consulting work is performed entirely outside the U.S. (Malta), the income is generally not U.S.-source under the place-of-performance rule for personal services (§861(a)(3)), and the foreign individual may have no U.S. federal tax obligation despite billing through a U.S. entity.  _(§861(a)(3))_
- **Form 5472 requirement** — Foreign-owned single-member LLC must file Form 5472 (Information Return of a 25% Foreign-Owned U.S. Corporation or a Foreign Corporation Engaged in a U.S. Trade or Business) annually, attached to a pro forma Form 1120. This is mandatory under Treasury Reg §1.6038A-1 and §1.6038A-2 for any reportable transactions between the LLC and the foreign owner — including capital contributions, distributions, and loans. Penalty for failure to file: $25,000 per Form 5472 per year.  _(Treasury Reg §1.6038A-1 and §1.6038A-2)_
- **Texas Public Information Report** — Form 05-102 due May 15 annually. AUDIT FLASH POINT — the foreign founder is the most likely to miss the PIR because the Comptroller notices may be mailed to a Texas registered agent address that the founder does not actively monitor. Configure registered agent to scan and email all received notices.
- **Texas franchise tax** — $0 owed at $300,000 revenue (well under $2.47M threshold), but the Form 05-163 No Tax Due return must still be filed.

- Texas formation: $300
- Texas registered agent: ~$150
- **Approximate total: $450**

- Form 5472 + pro forma Form 1120 preparation: typically $1,000–$2,500 in professional fees.

The Form 5472 obligation is the single most-missed federal compliance item for foreign-owned Texas LLCs. The $25,000-per-form penalty is severe and is assessed mechanically by the IRS. Every foreign founder forming a U.S. LLC must understand this obligation before the first reportable transaction (typically the initial capital contribution at formation).

## 13. Cross-References

- `us-tax-workflow-base` — workflow architecture, conservative defaults, reviewer signoff protocol.
- `tx-franchise-tax` — Form 05-102 PIR mechanics, Form 05-163 No Tax Due return, Form 05-158 Long Form franchise tax return.
- `tx-margin-tax` — margin tax computation, taxable margin methods (70%, COGS, compensation, $1M alternative), EZ Computation, retail/wholesale rate qualification.
- `tx-sales-tax` — Texas sales-and-use tax registration, Form 01-114, taxable services including data processing services under §151.0035, 20% data-processing exemption under §151.351, economic nexus threshold of $500,000 under §151.107.
- `us-tx-freelance-intake` — Texas-resident freelance developer intake form, document collection, federal-plus-Texas workflow entry point.
- `us-tx-return-assembly` — final assembly of federal return plus Texas PIR/franchise tax plus optional Texas sales tax for Texas-resident sole proprietors and SMLLCs.
- `us-s-corp-election-decision` — break-even analysis for S-corp election; particularly relevant for Texas operators where no state-level S-corp tax negates the California-style penalty for electing.
- `us-sole-prop-bookkeeping` — Schedule C classification for federal income tax, which feeds the Texas franchise-tax total revenue computation.

## 14. Self-Checks (Reviewer Worksheet)

Before finalizing entity-formation advice, the reviewer should confirm:

1. [ ] Is the founder a Texas resident? If not, has out-of-state-founder analysis (foreign qualification, Form 5472, treaty benefits) been completed?
2. [ ] Has the founder confirmed entity name availability with SOS name search (sosdirect.sos.state.tx.us)?
3. [ ] Has a Texas-physical-address registered agent been identified and consent obtained?
4. [ ] Has the entity been registered with the Texas Comptroller (Texas Taxpayer Number assigned)?
5. [ ] Has the May 15 PIR filing been calendared and assigned to an owner?
6. [ ] If revenue is projected to exceed $2.47M, has the margin tax been estimated and reserved?
7. [ ] If the entity is a Series LLC, has the separate-records discipline been put in place (separate bank accounts, separate bookkeeping, separate contracts)?
8. [ ] If the entity is a foreign qualification, has the home-state Certificate of Existence been obtained and dated within 91 days of the Texas filing?
9. [ ] Has the federal classification election (Form 8832 or Form 2553) been considered and documented?
10. [ ] Has the BOI/CTA reporting decision been documented with citation to current FinCEN guidance?
11. [ ] Has the Texas sales-tax obligation been evaluated (if the entity sells taxable goods or services)?
12. [ ] Has the founder been advised that the $300 SOS fee is a one-time charge but the annual PIR and margin-tax-when-over-threshold are ongoing obligations?
13. [ ] If the founder is foreign, has the Form 5472 obligation been explained and a Form 5472 preparer engaged?
14. [ ] Has a Texas-licensed attorney reviewed the operating agreement (or corporate bylaws and stockholder agreement) for any multi-member or multi-stockholder entity?

## 15. Refusals

The following requests are outside this skill's scope and should be referred elsewhere:

- **R-TX-FORM-1** — Forming a Texas non-profit corporation under BOC Chapter 22 — separate skill required for 501(c) federal exemption analysis.  _(BOC Chapter 22)_
- **R-TX-FORM-2** — Forming a Texas professional entity (PLLC, PA, PC) where Texas licensing-board approval is required (medical, legal, dental, engineering, architecture) — refer to a Texas-licensed attorney for board-approval mechanics.
- **R-TX-FORM-3** — Texas-to-Delaware or Delaware-to-Texas conversions, mergers, or domestications — refer to specialized corporate counsel; federal §368 reorganization tax analysis required.  _(§368)_
- **R-TX-FORM-4** — Texas sales-tax registration and computation — see `tx-sales-tax.md`.  _(tx-sales-tax.md)_
- **R-TX-FORM-5** — Texas margin tax computation when revenue exceeds $2.47M — see `tx-margin-tax.md`.  _(tx-margin-tax.md)_
- **R-TX-FORM-6** — Federal S-corp election break-even analysis — see `us-s-corp-election-decision`.  _(us-s-corp-election-decision)_
- **R-TX-FORM-7** — BOI/CTA filing for periods when the requirement is reinstated — verify current FinCEN guidance; this skill captures only the November 2025 stay status.
- **R-TX-FORM-8** — Texas franchise-tax combined group reporting for affiliated entities — separate analysis under Texas Tax Code §171.1014.  _(Texas Tax Code §171.1014)_
- **R-TX-FORM-9** — Texas business courts venue and procedure (HB 19, 88th Legislature, 2023) — refer to litigation counsel.  _(HB 19, 88th Legislature, 2023)_
- **R-TX-FORM-10** — Texas community-property and pre-marital planning for entity ownership — refer to family-law and estate-planning counsel.

## 16. Version History

- **0.1 (2025-11-15)** — Initial version. Tax year 2025 under post-OBBBA federal framework and post-SB 3 (88th Legislature, 2nd C.S., 2023) Texas franchise-tax framework. CTA/BOI stayed as of November 2025.

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
