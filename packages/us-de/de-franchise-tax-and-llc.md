---
name: de-franchise-tax-and-llc
description: Delaware LLCs, LPs, and GPs owe a flat $300 annual tax due June 1, regardless of income or activity. Delaware corporations owe annual franchise tax due March 1 computed under two methods — the Authorized Shares Method (flat tiers from $175 up to a $200,000 cap) and the Assumed Par Value Capital Method ($400 floor to the same $200,000 cap, $250,000 for Large Corporate Filers). Taxpayers pay the lower of the two. Corporations also file an annual report with officer/director and gross asset information. No Delaware corporate income tax applies unless the entity has Delaware-source income. Tax year 2025.
jurisdiction: US-DE
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# DE Franchise Tax And LLC

## Delaware Franchise Tax & LLC Tax

Delaware LLCs, LPs, and GPs owe a flat $300 annual tax due June 1, regardless of income or activity. Delaware corporations owe annual franchise tax due March 1 computed under two methods — the Authorized Shares Method (flat tiers from $175 up to a $200,000 cap) and the Assumed Par Value Capital Method ($400 floor to the same $200,000 cap, $250,000 for Large Corporate Filers). Taxpayers pay the lower of the two. Corporations also file an annual report with officer/director and gross asset information. No Delaware corporate income tax applies unless the entity has Delaware-source income. Tax year 2025.

## 1. Scope

This skill covers:

- **Delaware LLCs, LPs, and GPs** (entities formed under Title 6 of the Delaware Code) — the flat $300 annual tax administered by the Delaware Division of Corporations.
- **Delaware for-profit corporations** (entities formed under Title 8, the Delaware General Corporation Law, "DGCL") — the annual franchise tax and accompanying annual report.
- **Large Corporate Filer** regime under 8 Del. C. §503(c) for very large public-style corporations.
- **Coordination with Delaware Corporate Income Tax** (CIT) under Title 30, which applies only when the entity has Delaware-source income.
- **Late filing penalties and interest** under 8 Del. C. §502(d) (corporations) and 6 Del. C. §18-1107(b) (LLCs).
- **Practical filing posture** for typical Delaware-incorporated startups whose only Delaware contact is the registered agent and certificate of incorporation.

Out of scope (handled by other skills or refused):

- **Delaware Gross Receipts Tax** under Title 30, Chapter 21 — see the `de-gross-receipts-tax` skill. Delaware has no general sales tax; GRT is the closest analogue and is separate from franchise tax.
- **Delaware corporate income tax preparation** when DE-source income exists — see `de-income-tax`. This skill confirms whether DE CIT applies and routes onward.
- **Nonprofit, religious, and exempt corporations** under 8 Del. C. §501(b). Exempt corporations file an annual report and pay only a $25 filing fee; this skill flags but does not compute their treatment.
- **Public benefit corporations (PBCs)** under DGCL §362 — same franchise tax mechanics as ordinary corporations but with additional benefit-report obligations; computation flows are identical.
- **Statutory trusts** under 12 Del. C. §3801 — flat $300 annual tax, mechanically similar to LLCs but with separate statutory citation.
- **Captive insurance, banks, regulated investment companies** — these have separate Title 5 / Title 18 franchise-tax-like assessments outside this skill.
- **Series LLC sub-series** — Delaware does not separately tax registered series for the $300 annual; the parent LLC pays one $300. Protected series have no separate franchise tax. This skill confirms but does not advise on series structuring.
- **Foreign entities qualified to do business in Delaware** under 8 Del. C. §371 — they pay a separate annual report fee, not franchise tax. Flagged but not computed.

This is a Tier 2 jurisdiction skill. It must be loaded alongside `us-tax-workflow-base v0.2+` for the workflow scaffolding. It does not assemble a federal return. It does not compute owner-level distributions, basis, or K-1 information.

### 2.1 Statutory basis

- **LLCs annual tax** — Every domestic limited liability company and every foreign limited liability company registered to do business in this State shall pay an annual tax for the use of the State in the amount of $300.  _(6 Del. C. §18-1107(b))_
- **LPs annual tax** — $300  _(6 Del. C. §17-1109(b))_
- **GPs annual tax** — $300  _(6 Del. C. §15-1208(c))_

The tax is administered by the Delaware Division of Corporations, not the Delaware Division of Revenue. This is important: a Delaware LLC that has never had a single dollar of revenue, no employees, no operations, and no Delaware connection beyond the certificate of formation still owes the $300 every year. It is the price of having an active Delaware legal entity.

### 2.2 Key characteristics

- **Flat amount** — $300 per entity, per year. No tiers, no ratios, no schedules.  _(6 Del. C. §18-1107(b))_
- **Not based on income/revenue/assets/activity** — The tax exists because the entity is on the Delaware register, not because of income, revenue, gross receipts, assets, or activity.
- **Not affected by federal classification** — A single-member LLC disregarded for federal tax, an LLC taxed as a partnership, an LLC that has elected S-corp status, and an LLC that has elected C-corp status all owe the same $300 — because the tax is on the Delaware juridical entity, not the federal tax classification.
- **No annual report for LLCs/LPs** — Unlike corporations, Delaware LLCs and LPs do NOT file an annual report with officer/manager information. They just pay the $300.
- **Due date** — Due June 1 each year for the preceding calendar year (i.e., the 2025 tax is due June 1, 2025 and covers the 2025 calendar year). The first $300 is due the June 1 following the year of formation; an LLC formed in December 2024 owes the $300 by June 1, 2025.
- **No proration for short years** — An LLC formed November 15, 2024 still owes the full $300 by June 1, 2025 for the 2024 stub period. An LLC dissolved in February still owes the full $300 if it was active on January 1.
- **Cancellation requires payment of all back tax** — A Delaware LLC cannot cancel its certificate of formation under 6 Del. C. §18-203 unless all franchise taxes and penalties are current. Founders who simply "stop filing" accumulate $300/year plus penalty plus interest indefinitely until they actively file a Certificate of Cancellation.  _(6 Del. C. §18-203)_

### 2.3 No Delaware income tax return required for most LLCs

- **What LLC does not need to file** — The flat $300 tax is the only recurring Delaware obligation for a typical LLC whose sole Delaware contact is being formed in Delaware. The LLC does not need to file: A Delaware corporate income tax return (CIT applies to corporations, not LLCs, unless the LLC has elected C-corp status — see §10). A Delaware personal income tax return (this is the owner's responsibility, only if the owner is a DE resident or earns DE-source income). A Delaware gross receipts tax return (only if the LLC has DE-source receipts — see de-gross-receipts-tax). A Delaware partnership return (Form 300) — required only if the LLC is a partnership for federal tax purposes AND has DE-source income.

Mantra: **Forming in Delaware ≠ doing business in Delaware.** A Delaware LLC operating entirely in California with no Delaware customers, no Delaware employees, and no Delaware property has zero Delaware income tax exposure. It owes $300 and nothing more to Delaware.

### 2.4 Practical filing mechanics

- **Filing mechanics** — File online through the Delaware Division of Corporations portal at corp.delaware.gov. Payment by ACH, credit card (with surcharge), or check. The filer must have the 7-digit Delaware File Number (sometimes called the SR&I number). This is on the original certificate of formation. Confirmation receipt is the proof of payment — the Division does not mail certificates of good standing automatically. The registered agent typically sends a reminder in April. Many founders mistakenly think the registered agent files for them — the agent does not. Payment is the entity's responsibility.

### 3.1 Statutory basis and concept

- **Authorized Shares Method** — 8 Del. C. §503(a) gives the corporation two methods for computing franchise tax. The default — and the method Delaware uses if the corporation does not actively choose otherwise — is the Authorized Shares Method. This method is based purely on the number of shares the corporation has authorized in its certificate of incorporation, with no regard to how many shares are actually issued, what par value they have, or what the corporation is worth.  _(8 Del. C. §503(a))_

### 3.2 The schedule (2025)

**Authorized Shares Method schedule (2025)**

| Authorized shares | Franchise tax |
| --- | --- |
| 1 — 5,000 | $175 |
| 5,001 — 10,000 | $250 |
| 10,001 — 20,000 | $250 + $85 = $335 |
| 20,001 — 30,000 | $250 + $170 = $420 |
| Each additional 10,000 shares or fraction thereof beyond 10,000 | + $85 |
| Maximum (regular filers) | $200,000 |
| Maximum (Large Corporate Filers, see §7) | $250,000 |

- **Authorized Shares tax formula (>10,000 shares)** — Tax = $250 + $85 × ceiling((authorized shares − 10,000) / 10,000)

The "ceiling" matters: 10,001 shares triggers the same $85 increment as 19,999 shares. Partial blocks round up.

### 3.3 Why this method punishes startups by default

A typical Delaware C-corp formed via Stripe Atlas, Clerky, or a similar service is incorporated with 10,000,000 authorized shares at $0.0001 par value. This is the standard "founder-friendly" cap table architecture and makes total economic sense — except for one thing.

Under Authorized Shares:

> Tax = $250 + $85 × (10,000,000 − 10,000) / 10,000
> Tax = $250 + $85 × 999
> Tax = $250 + $84,915
> **Tax = $85,165**

That is the bill Delaware sends, by default, every March 1, to a freshly minted unfunded startup with no revenue and no assets. The state mails an invoice that says "FRANCHISE TAX: $85,165.00" to founders who have not even raised a seed round. Many founders panic and pay. Many incorporation services, on autopilot, also pay it.

This is almost always the wrong amount. See §5.

### 3.4 When the Authorized Shares Method is actually optimal

- **When Authorized Shares is optimal** — Despite the horror story above, Authorized Shares is the right method for certain profiles: - Closely-held corporations with very few authorized shares. A 1,500-authorized-share family C-corp pays $175 under Authorized Shares and significantly more under Assumed Par if it has any real assets. - Corporations with low gross assets relative to authorized shares. If gross assets are zero and shares are few, $175 beats the $400 Assumed Par floor. - Recently-incorporated shells before any funding. With 1,500 authorized shares and no operations, Authorized Shares is $175 and Assumed Par is the $400 floor. Authorized Shares wins by $225. Rule of thumb: if authorized shares × $250 (or thereabouts) is below the Assumed Par result, use Authorized Shares.

### 4.1 Statutory basis and concept

- **Assumed Par Value Capital Method** — 8 Del. C. §503(b) provides an alternative computation: Assumed Par Value Capital Method. This method ties the tax to a hybrid measure of the corporation's economic size, blending issued shares, par value, and gross assets. For most startups and growth-stage companies, it produces a vastly lower bill than Authorized Shares.  _(8 Del. C. §503(b))_

### 4.2 The five-step computation

- **Step 1 — Total gross assets** — Total gross assets per 8 Del. C. §503(b) = the amount reported on U.S. federal Form 1120, Schedule L, Line 15(d), "Total assets," as of the end of the taxable year. This is book value, not market value, and it is the same number the corporation reports to the IRS. (For first-year corporations that have not yet filed Form 1120, use the closest available balance sheet number; the Division accepts good-faith estimates with documentation.)  _(8 Del. C. §503(b))_
- **Step 2 — Total issued shares** — The total number of issued and outstanding shares (all classes, including treasury — but treasury usually does not move the math). This is not authorized shares. Issued shares are the ones actually outstanding on the corporation's books.
- **Step 3 — Assumed Par Value** — Assumed Par Value = Total Gross Assets / Total Issued Shares
- **Step 4 — Assumed Par Value Capital** — For each class of stock: If the actual par value > Assumed Par Value: use actual par value × authorized shares of that class. If the actual par value ≤ Assumed Par Value: use Assumed Par Value × authorized shares of that class. Plus, for no-par stock: Assumed Par Value × authorized no-par shares. Sum across all classes = Assumed Par Value Capital.
- **Step 5 — Tax computation** — Tax = ceiling(Assumed Par Value Capital / $1,000,000) × $400, with a $400 minimum and the same $200,000 / $250,000 cap as the Authorized Shares Method.

### 4.3 Why this method rescues startups

The Assumed Par calculation has a structural feature that favors small companies with high authorized-share counts: when a corporation has very few real assets, the Assumed Par Value is tiny, which means each authorized share contributes very little to Assumed Par Value Capital.

Example: a startup with $50,000 gross assets, 6,000,000 issued shares, and 10,000,000 authorized shares at $0.0001 par.

- Assumed Par = $50,000 / 6,000,000 = $0.00833
- Actual par ($0.0001) < Assumed Par ($0.00833), so use Assumed Par.
- Assumed Par Value Capital = $0.00833 × 10,000,000 = $83,333
- Tax = ceiling($83,333 / $1,000,000) × $400 = 1 × $400 = $400 (the floor)

The same corporation that owed $85,165 under Authorized Shares owes the $400 floor under Assumed Par. The savings are 99.5%.

### 4.4 When Assumed Par is *worse*

Assumed Par produces a higher number than Authorized Shares when the company has a lot of gross assets but relatively few authorized shares.

Example: $500M in gross assets, 100M issued, 100M authorized at $0.001 par.

- Assumed Par = $500M / 100M = $5.00
- Actual par ($0.001) < Assumed Par ($5.00), so use Assumed Par.
- APV Capital = $5.00 × 100M = $500M
- Tax = ceiling($500M / $1M) × $400 = 500 × $400 = $200,000 (capped)

Under Authorized Shares with 100M authorized:

- Tax = $250 + $85 × (100M − 10,000) / 10,000 ≈ $850,165, capped at $200,000.

Both methods cap at $200,000 here, so it does not matter — pick either. But increase gross assets or issued shares further and Assumed Par stays at $200,000 while Authorized Shares would too. At the cap, the methods tie.

### 4.5 Documenting the Assumed Par election

- **How to elect Assumed Par** — The corporation chooses Assumed Par by filling in the additional fields on the annual franchise tax filing portal (total gross assets, total issued shares, par values per class). The portal automatically computes both methods and bills the lower of the two — but only if the taxpayer enters the Assumed Par data. If the taxpayer leaves those fields blank, Delaware bills the Authorized Shares amount. This is the single most important practical fact in this skill: failing to enter the issued shares and gross assets fields means accepting the Authorized Shares bill.

### 5.1 The legal rule

- **Lower of two methods** — 8 Del. C. §503(c) provides that "the amount of tax under §503(a) [Authorized Shares] or §503(b) [Assumed Par Value Capital], whichever is lower, shall be paid by every corporation, as the franchise tax for the year." The taxpayer is statutorily entitled to the lower of the two methods. There is no election, no Form, no advance notice — it is automatic if the taxpayer enters the data.  _(8 Del. C. §503(c))_

### 5.2 Quick decision rule

- **Decision heuristics** — 1. If authorized shares ≤ 5,000 → almost always Authorized Shares ($175 vs. $400 floor under Assumed Par). 2. If authorized shares are 5,001–10,000 and gross assets are zero/minimal → Authorized Shares ($250 vs. $400 floor). 3. If authorized shares are above 10,000 and gross assets are modest (< $10M) → Assumed Par almost always wins. Compute both to confirm. 4. If gross assets per issued share exceed approximately $25 → re-check Authorized Shares; it may now win because Assumed Par scales with assets. 5. At the cap ($200,000), the two methods tie. Don't agonize.

### 5.3 The reviewer's responsibility

- **Reviewer checklist** — Before signing off any Delaware corporation client's franchise tax filing, the reviewer must: - Confirm authorized shares from the most recent certificate of incorporation (including any amendments). - Confirm issued shares from the corporation's stock ledger or cap table (Carta, Pulley, AngelList, or the secretary's records). Not estimates. - Confirm gross assets from the corporation's Form 1120 Schedule L Line 15(d) for the same fiscal year. If Form 1120 is not yet filed, use the closest book balance sheet. - Run both calculations. - Pay the lower. - Document the choice with workpapers showing both methods.

### 6.1 Corporations must file an annual report

- **Annual report requirement** — Under 8 Del. C. §502(a), every domestic corporation must file an annual report at the time it pays franchise tax. The report includes: The location of its registered office in Delaware and the name of its registered agent (usually the same as the formation document — confirm it has not changed). The location of its principal place of business outside Delaware (if any). The names and addresses of all directors as of the filing date. The names and addresses of all officers as of the filing date (typically including at least a president, treasurer, and secretary). Total gross assets as of the close of the corporation's fiscal year (this is the same number used in the Assumed Par Value calculation). The total number of issued shares as of the close of the fiscal year (used in Assumed Par).  _(8 Del. C. §502(a))_
- **Annual report filing fee — regular corporation** — $50  _(8 Del. C. §502(a))_
- **Annual report filing fee — exempt corporation** — $25  _(8 Del. C. §501(b))_

The annual report is filed and paid concurrently through the Division of Corporations online portal. There is a $50 annual report filing fee for regular corporations (and $25 for exempt corporations under §501(b)) that is in addition to the franchise tax. The portal totals it for you, but for budgeting: a small startup using Assumed Par pays $400 franchise + $50 annual report = $450 total to Delaware annually.

### 6.2 LLCs do NOT file an annual report

- **LLC no annual report** — This is a key contrast. Delaware LLCs, LPs, and GPs file no annual report. They pay $300 and that is the entire transaction. No officer/manager information goes on file with the state. This is one of the structural reasons Delaware LLC tax is simpler than Delaware corporate tax.

### 6.3 Foreign corporations qualified in Delaware

- **Foreign corporation annual report** — A corporation incorporated in another state but registered to do business in Delaware under 8 Del. C. §371 files a separate annual report (Form 200) with a $125 fee and no franchise tax. This skill flags but does not compute Form 200.  _(8 Del. C. §371)_

### 7.1 The threshold

- **Large Corporate Filer criteria** — 8 Del. C. §503(c) and accompanying Division of Corporations regulations classify a corporation as a Large Corporate Filer (LCF) if it meets ALL of the following: 1. It is listed on a national securities exchange (or its stock is publicly traded). 2. Its total gross assets OR total gross revenues equal or exceed $750 million. (As of 2025; the prior threshold was $250M, raised by 81 Del. Laws c. 348 effective 2018. Always confirm the threshold against current Division guidance — the $750M figure governs 2025 filings.) 3. It reports total consolidated gross assets or gross revenues on its federal financial statements.  _(8 Del. C. §503(c))_

### 7.2 Consequence — higher cap

- **LCF maximum franchise tax** — $250,000  _(8 Del. C. §503(c))_

LCFs are subject to a $250,000 maximum franchise tax (instead of $200,000). The Authorized Shares formula and the Assumed Par formula both apply normally; only the cap is raised. Most LCFs hit the cap regardless of method.

### 7.3 Practical posture

For 99% of startups, LCFs are not a concern. The skill flags it because reviewers handling Delaware-incorporated public companies need to know the cap differs. For a Series A through pre-IPO private corporation, the regular $200,000 cap applies.

### 8.1 Corporate franchise tax — due March 1

- **Corporate franchise tax due date** — 8 Del. C. §502(a). Annual report and franchise tax payment are due March 1 each year for the preceding calendar year. There is no extension available for franchise tax — even if the corporation is on a fiscal year and has not yet closed its books for Schedule L purposes, the tax is due March 1. Practical workaround: use best-available gross assets data and amend later if needed (rare).  _(8 Del. C. §502(a))_

### 8.2 LLC / LP / GP annual tax — due June 1

- **LLC/LP/GP due date** — 6 Del. C. §18-1107(b) and parallel provisions. June 1 each year. Like the corporate deadline, this is statutory and not extendable.  _(6 Del. C. §18-1107(b))_

### 8.3 Late filing penalty — corporations

- **Corporate late penalty** — 8 Del. C. §502(d): a penalty of $200 plus interest of 1.5% per month (compounded monthly) on the unpaid franchise tax and on the unpaid penalty. The corporation also loses good standing — meaning it cannot obtain a Certificate of Good Standing, cannot file documents with the Division (mergers, amendments, dissolutions) until current, and after extended delinquency may have its charter declared void under §510 (typically after 1 year of nonpayment, recoverable through reinstatement under §312 with payment of all back taxes, penalties, and interest).  _(8 Del. C. §502(d))_

### 8.4 Late filing penalty — LLCs / LPs / GPs

- **LLC/LP/GP late penalty** — 6 Del. C. §18-1107(g) (and parallel for LPs/GPs): a penalty of $200 plus interest of 1.5% per month on the unpaid $300 tax. The entity loses good standing and, after 3 years of nonpayment, the certificate of formation may be cancelled administratively under §18-1108. Reinstatement requires payment of all back taxes plus penalties plus interest plus a reinstatement fee.  _(6 Del. C. §18-1107(g))_

### 8.5 The math of long-term delinquency

A $300 LLC tax left unpaid for one full year accumulates: $300 + $200 penalty + 1.5% × 12 = 18% interest on the $300 + 18% interest on the penalty (roughly) ≈ $590 at year end. Five years of nonpayment can easily reach $3,000+ on what started as a $300 obligation, plus loss of good standing and potential administrative cancellation.

### 8.6 Refund / amendment

- **Refund window** — If a taxpayer overpaid (commonly: paid Authorized Shares when Assumed Par was lower), the corporation can file an amended franchise tax report within 3 years of the original due date and request a refund. The Division processes refunds via ACH or check; processing time runs 60–120 days. For LLCs, there is rarely cause to amend because the tax is flat — but if an LLC paid franchise tax in error after cancellation, refund is similarly available within 3 years.

### 9.1 Statutory basis

- **Delaware Corporate Income Tax rate** — 8.7%  _(30 Del. C. §1902)_
- **DE CIT imposition** — 30 Del. C. §1902 imposes a Delaware Corporate Income Tax (CIT) on every corporation deriving income from sources within Delaware. The rate is 8.7% of Delaware-apportioned taxable income (federal taxable income with state modifications, then apportioned).  _(30 Del. C. §1902)_

### 9.2 The "Delaware-source income" trigger

- **DE-source income triggers** — CIT applies only when the corporation has Delaware-source income. Delaware-source income includes: Sales of tangible personal property delivered to Delaware customers (apportionment via single-factor sales). Services performed in Delaware (i.e., the service is delivered in Delaware) — under Delaware's market-based sourcing rules. Rental income from Delaware real property. Royalties from Delaware-based intellectual property use (rare in practice). Gain on sale of Delaware real estate.
- **What does NOT create DE-source income** — Critically, the following do NOT create DE-source income on their own: Being incorporated in Delaware. This is the holy grail of "no DE CIT for DE-formed corps." A Delaware C-corp operating entirely in California with all customers outside Delaware has zero DE-source income. Having a registered agent in Delaware. Registered agent address is not nexus. Holding intangible assets through a Delaware entity (the classic "Delaware holding company" — see §1902(b)(8) Delaware Holding Company exemption for investment companies). Having board meetings in Delaware (telephonic, hybrid, or even one annual in-person — minimal contact does not create nexus).  _(30 Del. C. §1902(b)(8))_

### 9.3 The Delaware Holding Company exemption

- **Holding Company exemption** — 30 Del. C. §1902(b)(8) exempts certain investment-only Delaware corporations from CIT — historically a major reason corporations formed Delaware "passive investment companies" (PICs) to hold IP and trademarks. The exemption requires the entity to maintain only intangible investments and not actively conduct business. Post-2016 federal and multistate developments have eroded the practical benefit (most states now disregard PICs for income-shifting purposes), but the Delaware exemption itself remains on the books. This skill flags but does not advise on PIC strategy — that is a multistate planning matter requiring credentialed counsel.  _(30 Del. C. §1902(b)(8))_

### 9.4 Returns and forms

- **Form 1100 and due date** — When DE CIT applies, the corporation files Form 1100 (Delaware Corporate Income Tax Return) with Delaware Division of Revenue. Due date: 15th day of the 4th month after fiscal year end (April 15 for calendar-year corporations), with a 6-month extension available via Form 1100-EXT. This skill does not prepare Form 1100 — route to de-income-tax if DE-source income exists.

### 9.5 The most common posture for a Delaware-formed corporation

Most Delaware-incorporated startups, scaleups, and even mature private companies have: $0 of Delaware-source income. No CIT obligation. Annual franchise tax + annual report (Title 8) only. That is the entire Delaware tax relationship. Reviewers should confirm this affirmatively each year (i.e., ask: "Any Delaware customers, employees, property?") rather than assuming.

## 10. Why Delaware for Incorporation

This is brief context for advising founders, not tax content per se. Delaware is the dominant U.S. incorporation jurisdiction (over 67% of Fortune 500, over 80% of U.S. IPOs) for reasons that include:

- **The Court of Chancery.** A specialized equity court with no juries, judges chosen for corporate law expertise, and over a century of corporate-law jurisprudence. Outcomes are predictable and well-reasoned. Investors and acquirors prefer this venue.
- **The DGCL itself.** Title 8 is updated annually by the Delaware Bar Association's Corporation Law Section and ratified by the legislature. The statute is precise, flexible, and revised in light of practitioner experience.
- **Case law depth.** Tens of thousands of published decisions on fiduciary duty, M&A, fiduciary standards (Revlon, Unocal, Caremark, Aronson, MFW), and minority shareholder rights.
- **The Delaware LLC Act (Title 6, Chapter 18).** Among the most flexible LLC statutes in the U.S. — permits waiver of fiduciary duties (except the implied covenant of good faith and fair dealing), permits series LLCs, permits divisions, permits all manner of contractual flexibility.
- **Speed.** Same-day and 24-hour filing services available; expedited dissolution and merger.
- **Predictability of franchise tax.** Despite the horror stories, the tax is bounded ($200,000 cap, with rare $250,000 LCF cap). Investors model around it.

The trade-off: every Delaware entity owes Delaware money every year, even when there is no Delaware activity. For a single-owner LLC operating in California, this is $300 to Delaware + $800 California minimum tax + $70 statement of information = ~$1,170/year just to exist. Founders should weigh this against the cost of forming in their home state.

### 11.1 Paying Authorized Shares when Assumed Par would be lower

Already covered in §3 and §4. The single largest dollar error in Delaware franchise tax practice. Reviewer rule: never sign off without running both methods.

### 11.2 Confusing the LLC $300 with the corporate franchise tax

A Delaware LLC will never owe more than $300 (plus penalty/interest if late). Anyone quoting a Delaware "franchise tax" bill of more than $300 for an LLC is wrong — they have either:

- Mistakenly applied the corporate rules to an LLC.
- Confused another state's LLC tax with Delaware's (e.g., California's $800 minimum franchise tax on LLCs).
- Counted gross receipts tax or another assessment alongside.

### 11.3 Assuming the registered agent files

Registered agents (CSC, NRAI, Harvard Business Services, Northwest, Cogency Global, etc.) accept service of process and forward mail. They typically send a reminder email in February/April. They do not file or pay franchise tax on your behalf unless you have separately retained them for that service (often $50–$150 extra). Founders consistently misunderstand this.

### 11.4 Believing "we have no DE-source income, so we owe no DE tax"

Wrong. Even with zero DE-source income, the corporation owes franchise tax (minimum $400 under Assumed Par, $175 under Authorized Shares with ≤5,000 shares) plus the $50 annual report fee. An LLC owes $300. These are not income taxes — they are entity-existence taxes.

### 11.5 Believing dissolution stops the meter automatically

Wrong. Dissolution requires filing a Certificate of Dissolution (corporations) under 8 Del. C. §275 or a Certificate of Cancellation (LLCs) under 6 Del. C. §18-203. Until the filing is accepted and all back taxes paid, the entity remains on the register and accrues annual tax.

### 11.6 Believing the Authorized Shares horror bill is real

Many founders see the March pre-bill from Delaware, see "$85,165 DUE", and either panic-pay or panic-call the formation service. The Authorized Shares amount is the default amount until the corporation enters Assumed Par data. It is the price of inaction, not the correct bill. Calmly enter the issued share and gross asset figures, and the portal recomputes to the correct lower number.

### 11.7 Treating "gross assets" as market value or fundraised capital

Wrong. "Total gross assets" for Assumed Par is book value (Form 1120 Schedule L Line 15(d)). A startup that has raised $50M but spent down to $30M cash + $5M other assets has $35M gross assets, not $50M. Reporting $50M needlessly inflates the Assumed Par bill.

### 11.8 Forgetting to update issued shares after a stock split or financing

After a Series A, the cap table grows — preferred shares are issued. The corporation must use the year-end issued share count, not the prior year. After a forward stock split, the issued share count multiplies. Reviewers should pull the cap table as of December 31 (or fiscal year end) before computing.

### 11.9 Filing Form 1100 unnecessarily

A Delaware corporation with no DE-source income is not required to file Form 1100. Filing a zero-income Form 1100 every year is a common over-cautious practice that costs preparation hours and creates open-tax-year audit exposure to no benefit. The franchise tax filing alone satisfies Delaware. (When in doubt, confirm DE-source income status affirmatively and document.)

### 11.10 Series LLCs paying $300 per series

Delaware Series LLCs (under 6 Del. C. §18-215) registered or protected series do not pay a separate $300 per series — the parent LLC pays one $300. Some founders have been mistakenly billed by formation services for multiple $300 payments; only the parent owes.

### 12.1 Example A — Small DE LLC, single-member, operating in California

Pearl Street Ventures LLC, formed in Delaware June 2023. Single member: Sarah, a California resident. LLC is disregarded for federal tax — Sarah reports on Schedule C. 2025 revenue: $180,000, all from California clients delivered in California. No Delaware customers, no DE employees, no DE property. Registered agent: Harvard Business Services in Lewes, DE.

**Example A computation table**

| Item | Amount |
| --- | --- |
| Delaware annual tax (6 Del. C. §18-1107(b)) | $300 |
| Annual report fee | $0 (LLCs do not file) |
| Late penalty if missed | $200 + 1.5%/mo interest |
| DE corporate income tax | $0 (no DE-source income; LLC is not a corporation) |
| DE personal income tax for Sarah | $0 (Sarah is a CA resident; her income is not DE-source) |
| **Total to Delaware in 2025** | **$300** |

Due June 1, 2025. Payment via Delaware Division of Corporations portal. Sarah also owes California — $800 minimum LLC franchise tax + LLC fee on revenue + $20 SOI biennial — but that is a CA matter, not DE.

### 12.2 Example B — Early-stage startup, 10M authorized, $0.0001 par, pre-funding

Facts:
- Acme AI, Inc., a Delaware C-corp formed January 2025.
- Authorized shares: 10,000,000 common, $0.0001 par value.
- Issued shares as of December 31, 2025: 8,000,000 (founders only, no funding yet).
- Gross assets (Form 1120 Schedule L Line 15(d)) at year end: $25,000.

Authorized Shares Method:

> Tax = $250 + $85 × (10,000,000 − 10,000) / 10,000
> Tax = $250 + $85 × 999
> Tax = $250 + $84,915
> **= $85,165**

Assumed Par Value Method:

> Assumed Par = $25,000 / 8,000,000 = $0.003125
> Actual par ($0.0001) < Assumed Par ($0.003125) → use Assumed Par
> Assumed Par Value Capital = $0.003125 × 10,000,000 = $31,250
> Tax = ceiling($31,250 / $1,000,000) × $400 = 1 × $400
> **= $400** (the floor)

Plus annual report fee: $50.

**Lower method: Assumed Par. Total franchise tax + report = $450, due March 1, 2026.**

Note: had the founders accepted the default Authorized Shares pre-bill, they would have paid $85,165 + $50 = $85,215. The savings from entering the Assumed Par data: $84,765. This single entry of two numbers in the portal is worth ~$85K to the company.

### 12.3 Example C — Mature private corp with real assets and Series B funding

Facts:
- Beta Robotics, Inc., a Delaware C-corp founded 2020.
- Series B completed March 2025; valuation $400M.
- Authorized shares: 25,000,000 common + 10,000,000 preferred = 35,000,000 total. Par value $0.00001 on all classes.
- Issued shares as of December 31, 2025: 14,000,000 common (founders, employees, ESOP) + 8,000,000 preferred = 22,000,000 total.
- Gross assets (Form 1120 Schedule L Line 15(d)) at year end: $108,000,000 (cash from Series B + R&D capitalized + equipment).

Authorized Shares Method:

> Tax = $250 + $85 × (35,000,000 − 10,000) / 10,000
> Tax = $250 + $85 × 3,499
> Tax = $250 + $297,415
> Tax = **$297,665**, capped at $200,000

Assumed Par Value Method:

> Assumed Par = $108,000,000 / 22,000,000 = $4.909 per share
> Actual par ($0.00001) < Assumed Par ($4.909) → use Assumed Par
> Assumed Par Value Capital = $4.909 × 35,000,000 = $171,818,182
> Tax = ceiling($171,818,182 / $1,000,000) × $400 = 172 × $400
> **= $68,800**

Plus annual report fee: $50.

**Lower method: Assumed Par. Total = $68,850, due March 1, 2026.** Savings vs. Authorized Shares cap: $131,150.

### 12.4 Example D — Large Corporate Filer at the cap

Facts:
- Gamma Networks, Inc., a Delaware C-corp, publicly traded on NASDAQ.
- Authorized shares: 500,000,000 common, $0.001 par value.
- Issued shares: 220,000,000 common.
- Gross assets per Form 1120 Schedule L Line 15(d): $4.2 billion.
- Gross revenues per consolidated 10-K: $1.8 billion.
- Listed on a national securities exchange.

LCF determination: gross assets ($4.2B) > $750M and publicly listed → Large Corporate Filer. Cap: $250,000.

Authorized Shares Method:

> Tax = $250 + $85 × (500,000,000 − 10,000) / 10,000
> Tax = $250 + $85 × 49,999
> Tax = $250 + $4,249,915 = $4,250,165 → capped at $250,000

Assumed Par Value Method:

> Assumed Par = $4,200,000,000 / 220,000,000 = $19.09
> Actual par ($0.001) < Assumed Par ($19.09) → use Assumed Par
> APV Capital = $19.09 × 500,000,000 = $9,545,000,000
> Tax = ceiling($9,545M / $1M) × $400 = 9,545 × $400 = $3,818,000 → capped at $250,000

Both methods hit the $250,000 LCF cap. **Tax = $250,000** plus $50 annual report = $250,050, due March 1, 2026. The choice of method is irrelevant once both methods cap.

### 12.5 Example E — Delaware LLC with Delaware-source income

Wilmington Logistics LLC, a Delaware LLC operating a warehouse in New Castle County, DE. LLC taxed as a partnership for federal purposes. 2025 revenue: $2.4M, of which $1.8M from Delaware customers, $600K from Pennsylvania.

**Example E computation table**

| Item | Amount |
| --- | --- |
| Delaware annual tax | $300 |
| Annual report fee | $0 (LLCs do not file) |
| DE Partnership Return (Form 300) | Required — has DE-source income |
| DE Gross Receipts Tax | Required — see `de-gross-receipts-tax` |
| **Franchise tax obligation to DE** | **$300** |

The LLC's $300 franchise obligation is unchanged. But because it has DE-source income, it also files Form 300 (partnership return) reporting Delaware-apportioned income, the partners receive K-1s showing DE-source income, and the LLC is liable for DE gross receipts tax on warehouse services revenue. Routed to `de-income-tax` and `de-gross-receipts-tax` for the substantive computations.

### 13.1 Primary statutory sources

- 8 Del. C. §501–§518 — Delaware General Corporation Law, franchise tax provisions, including §502 (annual report and tax payment), §503 (computation methods), §510 (forfeiture for non-payment), §312 (renewal/revival).
- 6 Del. C. §18-1107 — Delaware Limited Liability Company Act, annual tax provisions.
- 6 Del. C. §17-1109 — Delaware Revised Uniform Limited Partnership Act, annual tax provisions.
- 6 Del. C. §15-1208 — Delaware Revised Uniform Partnership Act, annual tax provisions.
- 6 Del. C. §18-203, §18-1108 — LLC cancellation and forfeiture provisions.
- 12 Del. C. §3801–§3812 — Delaware Statutory Trust Act, including annual tax.
- 30 Del. C. §1902 — Delaware Corporate Income Tax imposition and exemptions.

### 13.2 Regulatory and administrative sources

- Delaware Division of Corporations — annual franchise tax instructions, available at corp.delaware.gov.
- Delaware Division of Corporations FAQ — practical guidance on Authorized Shares vs. Assumed Par.
- Title 8 Annual Report instructions — Division of Corporations, current as of 2025 filing year.
- Delaware Code Online (delcode.delaware.gov) — authoritative current text of all cited statutes.

### 13.3 Legislative updates relevant to 2025

- 81 Del. Laws c. 348 (2017) — raised the Large Corporate Filer cap from $180,000 to $250,000 and adjusted the LCF threshold; subsequent amendments refined the threshold to the current $750M figure.
- Annual technical-amendments bills — Delaware Bar Association Corporation Law Section sponsors annual amendments to Title 8; the 2024 amendments package (84 Del. Laws c. ___, signed July 2024) made conforming changes to several DGCL sections, none of which alter the franchise tax computation for 2025.

### 13.4 Cross-references within this skillset

- `us-tax-workflow-base` — workflow scaffolding for Tier 2 skills.
- `de-gross-receipts-tax` — separate Delaware obligation, triggered by DE-source receipts.
- `de-income-tax` — Delaware corporate and personal income tax, triggered by DE-source income.
- `us-s-corp-election-decision` — S-corp election analysis for DE-formed entities.
- `global-router` — routing logic for multi-state taxpayers including DE-formed entities.
- `no-sales-tax-states` — Delaware's lack of a general sales tax (NEXUS-free for sales tax purposes; GRT is separate).

### 13.5 Verification status

This skill is marked verified_by: pending. It awaits sign-off by a Delaware-licensed CPA or attorney with active Title 8 / Title 6 practice. The skill must not be used to file or to advise on Delaware franchise tax without that sign-off. The author has based all figures on the 2025 Delaware Division of Corporations published rate schedules and the current text of the cited statutes; users should re-confirm rate-schedule figures before each filing season since Delaware periodically adjusts thresholds and caps.

### 13.6 Last updated

2025-11-15. Next scheduled review: by February 1, 2026, in advance of the March 1 corporate filing deadline.

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
