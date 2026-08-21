---
name: de-formation
description: Tier 2 Delaware content skill for entity formation covering tax year 2025. Includes the Court of Chancery and DGCL advantages making Delaware the standard for VC-backed startups, $90 LLC Certificate of Formation, $89 C-Corp Certificate of Incorporation, $300 annual LLC tax (June 1 deadline), the "startup standard" 10M-share / $0.0001 par value structure that optimizes franchise tax under the Assumed Par Value method, Series LLC firewalling, Statutory Trusts, Public Benefit Corporations, foreign qualification requirements in operating states, and the §83(b) 30-day election trap for founder restricted stock.
jurisdiction: US-DE
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# DE Formation

## 0. Scope

This skill covers the mechanics, statutory basis, fee schedule, and strategic considerations for forming a Delaware entity in tax year 2025. It is the "front-door" skill that engagement leads, founder clients, and VC counsel reach for first when planning the legal vehicle for a new business or restructuring an existing one.

In scope:

- Delaware LLC (formed under the Delaware Limited Liability Company Act, 6 Del. C. Ch. 18)
- Delaware C-Corporation (formed under the Delaware General Corporation Law, 8 Del. C. Ch. 1, commonly "DGCL")
- Delaware Series LLC (6 Del. C. § 18-215)
- Delaware Statutory Trust (12 Del. C. Ch. 38)
- Delaware Public Benefit Corporation (8 Del. C. §§ 361-368)
- Foreign qualification of a Delaware entity in the operating state
- §83(b) election mechanics for founder restricted stock
- Beneficial Ownership Information (BOI) status as of mid-2025

Out of scope (deferred to companion skills):

- Franchise tax computation for both corps and LLCs → `de-franchise-tax-and-llc.md`
- Delaware corporate income tax for entities doing business inside Delaware
- Delaware Division of Revenue business licenses and gross receipts tax
- S-corp election analysis → `us-s-corp-election-decision.md`
- Federal Schedule C / SE / 1040 mechanics → federal content skills
- State income tax in the founder's home/operating state
- Securities law compliance (Reg D, Rule 506(b)/(c), state blue sky) — flagged but not computed

This skill assumes a human reviewer credentialed under the laws of the operating state signs off on every entity formation engagement. It does not substitute for legal advice; entity choice is a mixed legal-and-tax question and the legal half belongs to a licensed attorney.

## 1. Why Delaware — the founder-choice gold standard

More than 68% of Fortune 500 companies and roughly 80% of US-IPO companies in the last decade are incorporated in Delaware. The pattern is not regulatory arbitrage — Delaware has a higher franchise tax than most states. Founders, lawyers, and venture capitalists pick Delaware because of three durable advantages.

### 1.1 The Court of Chancery — specialized business court

Delaware's Court of Chancery sits in Wilmington and Georgetown and hears business disputes under equity jurisdiction. It is the oldest continuously operating equity court in the United States and has three structural advantages:

1. No juries. Chancery cases are heard by Chancellors and Vice Chancellors — judges who are themselves former corporate lawyers, typically with 15-25 years of M&A or fund litigation practice before appointment. A breach-of-fiduciary-duty case in front of a Vice Chancellor is decided by a single expert; a state court in California would put the same dispute in front of twelve jurors who have never read a stock purchase agreement.
2. Speed. A typical preliminary injunction motion on a deal break-up is decided in weeks, not years. The court routinely sits on weekends for time-sensitive merger litigation.
3. Body of precedent. Roughly 150 years of accumulated case law on duty of care, duty of loyalty, entire-fairness review, the Revlon duties, Unocal enhanced scrutiny, Caremark monitoring obligations, MFW cleansing, appraisal rights under § 262, books-and-records demands under § 220, derivative standing under Court of Chancery Rule 23.1, and dozens of other doctrines. Sophisticated transactional lawyers can predict outcomes within a narrow band.

This predictability is worth real money. Director-and-officer insurance premiums are lower for Delaware corporations because the risk of an outlier jury verdict is essentially zero.

### 1.2 The DGCL — the most-developed corporate law in the US

The Delaware General Corporation Law is updated annually by the Corporation Law Section of the Delaware State Bar Association. Recent amendments include:

- 2022: Permitting officer exculpation under § 102(b)(7)
- 2023: Clarifying the validity of board acts where minor defects existed (the "ratification" amendments under §§ 204 and 205)
- 2024: Statutory authorization for lost stock certificate procedures and updates to franchise tax computation
- 2025: Codification of the "MFW" cleansing framework for controller transactions under amended § 144 (signed June 2025, effective for all controller transactions after that date)

This continuous statutory updating is unique. Most states copy the Model Business Corporation Act with a multi-year lag; Delaware reacts to litigation outcomes within one or two sessions.

### 1.3 The VC standard — and the "Delaware flip"

Every major venture capital firm — Sequoia, a16z, Benchmark, Founders Fund, Accel, Greylock, Khosla, and the Y Combinator standard SAFE — uses Delaware C-Corp documents as the default term sheet. The National Venture Capital Association model documents (NVCA forms) are written for a Delaware Delaware C-Corporation.

If a startup is incorporated elsewhere — say, a California LLC — and then raises an institutional Series A, the first thing the investor's counsel will demand is a Delaware flip: convert the entity into a Delaware C-Corp before the term sheet is countersigned. This costs $15,000-$40,000 in legal fees and creates a tax event on built-in gain if the converting entity has appreciated assets. The cheaper path is to incorporate Delaware on day one.

### 1.4 Banking and counterparty friendliness

A Delaware Certificate of Incorporation or Certificate of Formation is recognized by every commercial bank, SaaS vendor, and large enterprise customer in the US. Bank of America, JPMorgan Chase, Mercury, Brex, Silicon Valley Bank (now First Citizens), and Stripe Atlas all have streamlined onboarding flows for Delaware entities. Forming in some other states (e.g., New Mexico, which is anonymous but obscure) can cause friction with vendor onboarding and KYC reviews that costs more time than the Delaware fees ever would.

## 2. Delaware LLC formation mechanics

The Delaware LLC is the most popular vehicle for bootstrapped small businesses, freelancer single-member LLCs, real estate investment vehicles, and joint ventures. It is not the right vehicle for a venture-backed company (which needs a C-Corp — see § 3).

### 2.1 Statutory basis

- **Delaware LLC statutory basis** — Delaware LLCs are governed by the Delaware Limited Liability Company Act, codified at 6 Del. C. §§ 18-101 through 18-1208. The Act is the most permissive LLC statute in the United States: § 18-1101(b) explicitly states that the policy of the chapter is to give "maximum effect to the principle of freedom of contract" and the enforceability of LLC agreements.  _(6 Del. C. §§ 18-101 through 18-1208; § 18-1101(b))_

### 2.2 Certificate of Formation — $90 filing fee

Formation is triggered by filing a Certificate of Formation with the Delaware Division of Corporations under 6 Del. C. § 18-201. The Certificate is short — typically one page — and must include the required elements listed in the table below.

**Certificate of Formation required elements**  _(6 Del. C. § 18-201)_

| Required element | Source |
| --- | --- |
| Name of the LLC, ending in "Limited Liability Company," "L.L.C.," or "LLC" | § 18-102 |
| Address of registered office in Delaware | § 18-104 |
| Name of registered agent in Delaware | § 18-104 |
| Any other matters the members elect to include | § 18-201(a)(3) |

- **LLC Certificate of Formation filing fee** — $90 USD (2025 schedule)  _(6 Del. C. § 18-201)_
- **Mandatory county filing fee** — $9 USD  _(Division of Corporations fee schedule)_
- **Expedited fees (one-hour, two-hour, same-day, next-day)** — $200 for one-hour, $100 for two-hour, $50 for same-day, $30 for next-day USD  _(Division of Corporations fee schedule)_
- **Common filing practice** — Most formations are filed for same-day expedited service at $50 so the filer can open a business bank account that week. The Certificate is not required to disclose members, managers, capital contributions, profit-sharing percentages, or any operating details. This is by design — Delaware LLCs are private.

### 2.3 Registered agent — required

- **Registered agent requirement** — Under § 18-104, every Delaware LLC must maintain a registered agent with a Delaware street address at all times. The registered agent receives service of process (lawsuit papers), tax notices from the Division of Corporations, and annual report reminders.  _(§ 18-104)_

**Common registered agent providers and 2025 annual fees**

| Provider | 2025 annual fee | Notes |
| --- | --- | --- |
| Harvard Business Services | $50 | The cheap-and-cheerful default for solo founders |
| Northwest Registered Agent | $125 | Strong privacy posture; will list its own address as principal address on filings |
| Cogency Global / CSC | $250-$300 | Used by VC-backed companies; tighter SLA, integrated annual report filing |
| Stripe Atlas (uses Capitol Services) | Included in $500 setup | Bundled with EIN and bank account |

- **Self as registered agent restriction** — Commercial registered agents charge $50-$300 per year. The founder cannot be her own registered agent unless she personally maintains a Delaware street address (not a P.O. Box). For founders living outside Delaware, the commercial provider is mandatory.

### 2.4 Operating Agreement — required, but not filed

- **LLC Agreement requirement** — Under § 18-101(9) and § 18-201(d), every Delaware LLC has an LLC Agreement (the "operating agreement"). The agreement is not filed with the state and is not public. It can be: Written (standard, strongly recommended); Oral (legally valid but a malpractice trap); Implied (legally valid but a litigation disaster).  _(§ 18-101(9); § 18-201(d))_
- **Single-member LLC operating agreement provisions** — For single-member LLCs, the operating agreement establishes: Single-member ownership and capital contribution; Manager-managed vs member-managed (single-member LLCs are almost always member-managed); Authority of the sole member to bind the LLC; Distribution waterfall (typically: all distributions to sole member); Dissolution events; Disregarded entity for federal tax election language (default treatment, no Form 8832 needed).  _(§ 18-101(9); § 18-201(d))_
- **Multi-member LLC operating agreement provisions** — For multi-member LLCs, additional provisions matter: Profit-and-loss allocations (must comply with IRC § 704(b) substantial economic effect rules if not pro rata); Capital account maintenance; Buy-sell provisions (drag-along, tag-along, right of first refusal); Manager appointment and removal; Voting thresholds; Deadlock-resolution mechanisms; Restrictions on transfer to preserve closely-held status.  _(IRC § 704(b))_

Practitioner note: The single biggest malpractice risk in DE LLC formations is the off-the-shelf single-page template used for what was supposed to be a simple single-member LLC, but then a second member joins informally. Without proper amendments, the partners are operating under default DGCL rules (which favor equal distributions and equal voting regardless of capital contributions) and have created a de facto general partnership. Always paper amendments contemporaneously.

### 2.5 Annual LLC tax — $300 due June 1

- **Annual LLC tax vs annual report** — Delaware does not impose an annual report requirement on LLCs (unlike corporations — see § 3.4), but it does impose a flat $300 annual LLC tax under 6 Del. C. § 18-1107.  _(6 Del. C. § 18-1107)_

**Annual LLC tax 2025 figures**  _(6 Del. C. § 18-1107)_

| Item | 2025 figure | Source |
| --- | --- | --- |
| Annual LLC tax (flat) | **$300** | 6 Del. C. § 18-1107(b) |
| Due date | **June 1** | § 18-1107(c) |
| Late penalty | **$200** + 1.5% per month interest | § 18-1107(g) |
| Form | Online via Division of Corporations portal | No paper form |

- **LLC tax owed regardless of activity** — The $300 is owed regardless of revenue, profit, activity, or whether the LLC has ever transacted business. A dormant LLC formed three years ago and forgotten still owes $300 every June 1, plus the cumulative $200 late penalties.  _(6 Del. C. § 18-1107)_

AUDIT FLASH POINT: The single most common Delaware LLC error in client portfolios is the dormant LLC the client forgot they formed. Each year of non-payment accumulates: Year 1 = $300 + $200 = $500. Year 2 = $300 + $200 + $300 + $200 = $1,000. After five years of non-payment and the LLC is administratively dissolved by the state, reinstatement costs $200 + all back-taxes + all penalties + accrued interest — easily $3,000-$5,000. Reviewer must surface every Delaware LLC in the client's history and confirm $300 has been paid every June 1.

### 2.6 Expedited service

**Expedited service tiers**

| Service level | Fee | Use case |
| --- | --- | --- |
| 30-day standard | $0 | Never used in practice |
| 24-hour | $50 | Default for founders who want to open a bank account this week |
| Same-day | $100 | Time-sensitive bank account or contract execution |
| 2-hour | $500 | M&A transaction with a same-day signing |
| 1-hour | $1,000 | M&A closing |

- **Recommended expedited tier for startup formation** — For a startup formation, 24-hour at $50 is the right answer. Same-day is occasionally needed when the founder has a Stripe Atlas-style packaged deadline.

### 2.7 EIN

- **EIN application process** — After the Certificate of Formation is filed, the LLC needs an Employer Identification Number from the IRS. For US founders, Form SS-4 online at IRS.gov produces an EIN immediately. For non-US founders without an SSN or ITIN, the SS-4 must be faxed to the IRS Philadelphia office with a 4-8 week processing time, or filed via Form W-7 ITIN + SS-4 in the same envelope.
- **EIN required for** — The EIN is required for: Opening a business bank account; Filing federal tax returns; Hiring employees; Applying for state tax IDs; Most vendor onboarding.

## 3. Delaware C-Corporation formation mechanics

The Delaware C-Corporation is the default vehicle for venture-backed startups. If the company has any intention of raising institutional capital, an IPO, or being acquired by a public buyer, the C-Corp is the answer.

### 3.1 Statutory basis

- **Delaware C-Corp statutory basis** — Delaware C-Corps are governed by the Delaware General Corporation Law (DGCL), codified at 8 Del. C. §§ 101-398. The DGCL is referenced and copied around the world — Cayman Islands corporate law, BVI, Bermuda, and even some emerging-market jurisdictions have explicit DGCL-tracking statutes.  _(8 Del. C. §§ 101-398)_

### 3.2 Certificate of Incorporation — $89 filing fee

Formation is triggered by filing a Certificate of Incorporation with the Delaware Division of Corporations under 8 Del. C. § 102. The Certificate must include the required elements listed in the table below.

**Certificate of Incorporation required elements**  _(8 Del. C. § 102)_

| Required element | Source |
| --- | --- |
| Name of the corporation, ending in "Corporation," "Incorporated," "Limited," "Corp.," "Inc.," "Co.," "Ltd." | § 102(a)(1) |
| Address of registered office in Delaware | § 102(a)(2) |
| Name of registered agent in Delaware | § 102(a)(2) |
| Nature of business or purposes ("to engage in any lawful act or activity" is standard) | § 102(a)(3) |
| **Authorized share structure** | § 102(a)(4) |
| Name and mailing address of the incorporator | § 102(a)(5) |

- **C-Corp Certificate of Incorporation filing fee** — $89 USD (a $9 mandatory county fee plus $80 base, for a basic single-class corporation with up to 1,500 shares of no-par stock (2025 schedule))  _(8 Del. C. § 102)_
- **Expedited fees same as LLCs; higher share counts increase fee** — Expedited fees are the same as for LLCs (§ 2.6). For higher share counts and par-value structures, the filing fee increases — see § 4 for the startup-standard 10M-share structure.

### 3.3 Authorized share structure — affects franchise tax forever

- **Authorized share structure decision** — This is the single most consequential decision in the Certificate of Incorporation. The Certificate must specify: 1. Total number of authorized shares; 2. Par value per share (or "no par value"); 3. Number of classes (single class of common is the default; multi-class with preferred is structured at the Series A, not at formation). The choice between default Authorized Shares method and the Assumed Par Value method for franchise tax computation is driven by the par value and share count chosen here. A mistake at the Certificate stage cannot be undone without a board resolution and amendment — and the corporation will pay franchise tax at the wrong rate for as long as the mistake persists. See § 4 below.

### 3.4 Registered agent + annual report

- **Registered agent requirement for corporations** — Like LLCs, Delaware corporations need a registered agent under 8 Del. C. § 132. Same providers, same price range.  _(8 Del. C. § 132)_

**Corporation annual report 2025 figures**  _(8 Del. C. § 502)_

| Item | 2025 figure |
| --- | --- |
| Annual report filing fee | **$50** (minimum, applies to all domestic corps) |
| Franchise tax (separate computation) | Variable — see § 4 and `de-franchise-tax-and-llc.md` |
| Due date | **March 1** |
| Late penalty | **$200** + 1.5% per month interest |
| Information required | Officer names and addresses, director names and addresses, total assets, gross assets |
| Filing portal | Division of Corporations online |

Critical date difference: C-Corps file by March 1. LLCs pay by June 1. Practitioners commonly conflate these. Set calendar reminders for both. A C-Corp client who hears "Delaware annual tax is June 1" will be three months late.

### 3.5 Officers, directors, bylaws, organizational consents

- **Post-filing organizational steps** — The Certificate of Incorporation does not by itself create a functioning corporation. After filing, the incorporator must execute: 1. Action by Sole Incorporator — appoints the initial board of directors 2. Bylaws adopted by the board (8 Del. C. § 109) 3. Initial board consent — appoints officers (CEO, Secretary, Treasurer at minimum), approves stock issuances, ratifies pre-incorporation acts, opens the bank account, authorizes the corporate seal, sets the fiscal year 4. Stock subscription agreements with the founders 5. Stock purchase agreements with vesting and §83(b) election forms (see § 9) 6. Indemnification agreements with directors and officers (8 Del. C. § 145) 7. Form SS-4 for EIN 8. Form 2553 only if electing S-corp status (rare for VC-track companies — see `us-s-corp-election-decision.md`) 9. State qualification in the operating state (see § 8) This package — bylaws, board consents, stock paperwork, indemnification, founder vesting — is what NVCA and YC standardize. Counsel typically charges $3,000-$10,000 for a full formation package, or it is bundled into Stripe Atlas / Clerky / Carta Launch at $500-$2,000.  _(8 Del. C. § 109; 8 Del. C. § 145)_

### 3.6 EIN, state tax IDs, registered office

Same as for LLCs (§ 2.7).

## 4. The "startup standard" 10M-share structure

This section is the single most-asked question Delaware formation lawyers get from founders, and the single most-common error in non-specialist filings. Get this right at formation and the company saves thousands of dollars in annual franchise tax for the life of the company.

### 4.1 The two franchise tax methods

- **Two franchise tax methods, corporation pays lesser** — Under 8 Del. C. § 503, every Delaware corporation owes annual franchise tax, computed under either of two methods — the corporation pays the lesser of the two: 1. Authorized Shares method (default — the Division of Corporations defaults the invoice to this method); 2. Assumed Par Value Capital method (must be affirmatively elected on the annual report). The two methods produce wildly different numbers for the same corporation.  _(8 Del. C. § 503)_

### 4.2 Authorized Shares method — the default trap

- **Authorized Shares method basis** — Under § 503(1), franchise tax under the Authorized Shares method is computed per the table below.  _(§ 503(1))_

**Authorized Shares method franchise tax table (2025)**  _(§ 503(1))_

| Authorized share count | Franchise tax (2025) |
| --- | --- |
| 1 - 5,000 | **$175** minimum |
| 5,001 - 10,000 | **$250** |
| Each additional 10,000 (or fraction thereof) above 10,000 | **+ $85** |
| Maximum (cap) | **$200,000** (large corporate filer cap is $250,000 for certain filers) |

- **Authorized Shares method worked example — 10,000,000 no-par shares** — $250 + (10,000,000 - 10,000) / 10,000 × $85 = $250 + 999 × $85 = $250 + $84,915 = $85,165  _(§ 503(1))_

That is $85,165 per year in franchise tax, billed in March, for a corporation that may have zero revenue and three founders working out of a garage. This is the bill that lands in every unprepared founder's inbox in mid-March and triggers a panic call to counsel.

### 4.3 Assumed Par Value Capital method — the right answer

- **Assumed Par Value Capital method rate** — $400 per $1,000,000 of "Assumed Par Value Capital," with a $400 minimum and the same $200,000 cap  _(§ 503(2))_
- **Assumed Par Value Capital computation steps** — "Assumed Par Value Capital" is computed (simplified) as: 1. Take total gross assets from the corporation's federal Form 1120 Schedule L (typically reported as of the last day of the fiscal year); 2. Divide gross assets by total issued shares to get an "Assumed Par"; 3. If Assumed Par exceeds the stated par value, multiply Assumed Par by total authorized shares; 4. Result is Assumed Par Value Capital; 5. Tax = $400 × (Assumed Par Value Capital ÷ $1,000,000)  _(§ 503(2))_
- **Assumed Par Value Capital worked example** — For an early-stage corporation with $100,000 of gross assets, 10,000,000 authorized shares, 8,000,000 issued, and $0.0001 par: Assumed Par = $100,000 / 8,000,000 = $0.0125; Assumed Par exceeds stated par ($0.0001), so use $0.0125; Assumed Par Value Capital = $0.0125 × 10,000,000 = $125,000; Tax = $400 × (125,000 / 1,000,000) = $50 → floored at $400 minimum.  _(§ 503(2))_
- **Annual savings comparison** — The Assumed Par Value method is therefore $400 per year — vs $85,165 under Authorized Shares. The annual savings are $84,765.  _(§ 503(2))_

### 4.4 The startup-standard recipe

**Startup-standard configuration parameters**

| Parameter | Standard value | Why |
| --- | --- | --- |
| Authorized common shares | **10,000,000** | Enough to issue founders 8M, reserve 2M for option pool, with room for early stock splits |
| Par value | **$0.0001 per share** | Low par keeps Assumed Par Value Capital low |
| Initial issuance | 8,000,000 to founders | Leaves 2M in treasury for ESOP and SAFE conversions |
| Initial classes | Single class of common | Preferred is created at Series A |
| Option pool | 10%-20% of post-money | Created at Series A on a fully-diluted basis |

- **Filing fee at startup-standard structure** — Filing fee at $0.0001 par × 10M authorized = a Certificate filing fee in the $220-$250 range (the filing fee scales with the par value × share count for corporations with par-value stock under § 391(a)(5)), still cheaper over the corporation's life than any other configuration.  _(§ 391(a)(5))_

AUDIT FLASH POINT: Authorized Shares method default vs Assumed Par Value method. When a Delaware C-Corp client receives a franchise tax bill above $1,000, first action is to recompute under the Assumed Par Value method before paying. The Division of Corporations defaults invoices to the higher of the two methods. The corporation has the statutory right to recompute and pay the lower under § 503. Many founders pay the default invoice without checking — and donate $10,000-$80,000 per year to the State of Delaware for no reason.

### 4.5 Founder common with vesting

- **Standard founder vesting terms** — Founder shares are almost always issued subject to vesting to protect against the "co-founder who quits in month two and keeps 50% of the company" problem. The standard vesting: 4-year vesting with a 1-year cliff; Repurchase right at the lower of cost or fair market value if the founder leaves before fully vested; Acceleration on change of control (single-trigger or double-trigger; double is more common). This is implemented via a Restricted Stock Purchase Agreement between the founder and the corporation. Founder pays cash at the closing (typically $0.0001 × 2,000,000 = $200 — yes, founders write a $200 personal check at formation) and receives 2,000,000 shares of common stock subject to repurchase that lapses on the vesting schedule.

### 4.6 Vehicle for outside investment via SAFE / preferred

- **Preferred stock creation and SAFEs** — At formation, the corporation issues only common stock. Preferred stock is created when an institutional investor cuts a check at the Seed or Series A round. The preferred stock is created via a Certificate of Amendment (or, for a complete Series A, a Restated Certificate of Incorporation) authorizing the new class with its specific economic and control terms (liquidation preference, dividend, anti-dilution, board seats, protective provisions, conversion rights). Pre-Series-A bridge financing is typically via SAFE (Simple Agreement for Future Equity) — the Y Combinator standard. SAFEs are not debt and not equity at issuance; they convert to preferred at the next priced round at a discount or valuation cap. SAFEs are not filed with the state and do not affect the authorized share count until conversion.

## 5. Series LLC — firewalled liability

Delaware was the first state to enact a Series LLC statute (1996), and it remains the gold standard. Series LLCs are codified at 6 Del. C. § 18-215.

### 5.1 Concept

- **Series LLC concept** — A Series LLC is a single "master" LLC under which the operating agreement creates an arbitrary number of internal series. Each series: Has separate members, managers, assets, and liabilities from every other series and from the master; Is firewalled for liability purposes — a creditor of Series A cannot reach the assets of Series B or of the master (provided strict statutory formalities are met); Can have its own EIN, bank account, and tax classification (each series can be separately disregarded, partnership, S-corp, or C-corp for federal tax); Is not separately filed with the Delaware Division of Corporations — only the master LLC is filed.  _(6 Del. C. § 18-215)_

### 5.2 Statutory firewall requirements

- **Requirements for inter-series firewall** — For the inter-series firewall to hold under § 18-215(b), the LLC must: 1. Master operating agreement explicitly authorizes series with the statutory language; 2. Master Certificate of Formation gives notice that the LLC may establish series with limited liability (the "notice provision," 6 Del. C. § 18-215(b)(3)); 3. Each series maintains separate records identifying which assets belong to which series; 4. Each series is operated separately — separate bank accounts, separate bookkeeping, separate contracts in the name of "[Master LLC], Series A," not just "[Master LLC]". A series that commingles funds or signs contracts in the master's name loses the firewall and a creditor can pierce to other series.  _(§ 18-215(b); § 18-215(b)(3))_

### 5.3 Use cases

Real estate: One series per property. A tenant slip-and-fall claim against Series A (the Atlanta duplex) cannot reach Series B (the Phoenix triplex); Investment funds: One series per fund or strategy; Family offices: One series per asset class; Holding company structures: Each subsidiary line of business in its own series.

### 5.4 Tax treatment

- **Series LLC federal and state tax treatment** — The IRS issued Proposed Treasury Regulation § 301.7701-1(a)(5) in 2010 (still proposed as of 2025) treating each series as a separate entity for federal tax purposes. Most practitioners follow the proposed regs and treat each series separately. Each series files its own federal return (or is a separate disregarded entity reporting on its owner's return). State income tax treatment is inconsistent — some states (e.g., Illinois) recognize the firewall; others (e.g., California) do not, and a California foreign-qualifying Series LLC pays an $800 minimum franchise tax per series, defeating the cost savings.  _(Proposed Treasury Regulation § 301.7701-1(a)(5))_

### 5.5 Franchise tax

- **Series LLC franchise tax treatment** — Delaware treats the Series LLC as a single LLC for franchise tax purposes — $300 annually, total, regardless of how many series. This is the cost advantage that makes Series LLCs attractive over forming dozens of separate LLCs.

## 6. Statutory Trust — special-purpose vehicles

- **Delaware Statutory Trust definition** — The Delaware Statutory Trust (DST) is governed by the Delaware Statutory Trust Act, 12 Del. C. §§ 3801-3863. It is a separate legal entity, not a common-law trust, and offers limited liability to beneficial owners.  _(12 Del. C. §§ 3801-3863)_

### 6.1 Use cases

Asset-backed securitizations — mortgage-backed securities and auto loan-backed securities frequently use DSTs as the issuing entity; Mutual funds and ETFs — the Vanguard fund family is structured as a series of Delaware Statutory Trusts; 1031 exchange replacement property — fractional real estate investments offered to retail investors as 1031 exchange targets are typically DSTs (because §1031 like-kind exchange treatment requires the investor to receive a direct interest in real estate, and DST interests qualify under Revenue Ruling 2004-86); Pension and ERISA structures.

### 6.2 Formation mechanics

- **DST formation, filing fee, annual tax** — Formation is by filing a Certificate of Trust under 12 Del. C. § 3810. Filing fee is $500 (higher than LLC or corp). Annual tax is $300 under § 3812. The DST must have: At least one Delaware-resident trustee (or a trustee with a Delaware office), or a trustee that is a Delaware bank or trust company; A governing instrument (the trust agreement) — not filed publicly; Beneficial owners (analogous to LLC members or trust beneficiaries). DSTs are rarely formed for typical small-business clients. This skill flags the structure but does not provide formation worked examples — a DST engagement requires specialist trust and securities counsel.  _(12 Del. C. § 3810; § 3812)_

## 7. Public Benefit Corporation — DGCL §§ 361-368

- **Delaware Public Benefit Corporation definition** — The Delaware Public Benefit Corporation (PBC) is a for-profit corporation that explicitly identifies one or more "public benefit" purposes in its Certificate of Incorporation, alongside the goal of generating returns for shareholders.  _(8 Del. C. §§ 361-368)_

### 7.1 Statutory framework

- **PBC statutory framework history** — PBCs are codified at 8 Del. C. §§ 361-368, added to the DGCL in 2013 and significantly revised in 2020 to make PBC formation easier (the 2020 amendments removed the supermajority shareholder vote requirement for converting an existing corp into a PBC).  _(8 Del. C. §§ 361-368)_

### 7.2 Key differences from a standard C-Corp

**Standard C-Corp vs Public Benefit Corp feature comparison**  _(8 Del. C. §§ 362, 366)_

| Feature | Standard C-Corp | Public Benefit Corp |
| --- | --- | --- |
| Director fiduciary duties | To shareholders (maximize value) | **Tripartite** — shareholders, the specific public benefit, and stakeholders affected by the business |
| Required statement in Certificate of Incorporation | None | Must state the specific public benefit (§ 362) |
| Required public reporting | None at state level | **Biennial benefit report** to shareholders (§ 366) — measuring against a third-party standard |
| Conversion requirement | N/A | Standard C → PBC requires majority shareholder vote (post-2020) |

### 7.3 PBC vs B Corp Certification — they are NOT the same thing

This is a persistent client confusion point:

- Delaware PBC is a legal entity type — a state-law construct created by filing a particular Certificate of Incorporation
- B Corp Certification is a private third-party certification issued by B Lab, a nonprofit, based on an assessment of social and environmental performance

A Delaware PBC is not automatically a Certified B Corp, and a Certified B Corp does not have to be a PBC (though B Lab requires PBC conversion within a defined window for corporations in states that have PBC statutes). The two often co-exist but are doctrinally distinct.

### 7.4 Use cases

PBCs are attractive for: Mission-driven for-profit companies (Allbirds, Warby Parker pre-IPO, Kickstarter); ESG-focused VC portfolio companies; Founders who want to bake mission into the charter to constrain future activist shareholder challenges.

PBCs are not appropriate for: Pure-play financial-return startups (most VCs prefer standard C-Corps); Founders who want flexibility to pivot.

### 7.5 Tax treatment

- **PBC tax treatment identical to C-Corp** — PBCs are taxed identically to standard C-Corporations for federal and Delaware franchise tax purposes. There is no special tax treatment. The "benefit" purpose is a fiduciary-duty and disclosure construct, not a tax construct.

## 8. Foreign qualification — registering the DE entity in the operating state

This is the second most-common Delaware formation error (after the Authorized Shares franchise tax trap). It costs companies the ability to sue in the operating state's courts, generates per-day fines, and surfaces in due diligence as a deal-killing remediation item.

### 8.1 The rule

- **Foreign qualification requirement** — Every US state requires a foreign entity (i.e., an entity formed in another state, including Delaware) that is "doing business" in the state to register with that state's Secretary of State and obtain a Certificate of Authority (sometimes called Foreign Qualification, Foreign Registration, Statement and Designation by Foreign Corporation, or similar — terminology varies by state). For a Delaware entity with its principal place of business in California, the founder must: 1. Form the Delaware LLC or corp (Delaware Division of Corporations) 2. Foreign qualify in California with the California Secretary of State (Form LLC-5 for an LLC, or Form S&DC-S/N for a corporation) 3. Pay the California $800 minimum franchise tax annually to the California Franchise Tax Board (and the LLC fee under R&TC § 17942 — see `ca-smllc-form-568.md`) 4. Register for any required California state tax accounts (employment, sales tax)

### 8.2 "Doing business" — the trigger

- **Doing business triggers and safe harbors** — "Doing business" is defined differently in every state, but common triggers include: Having employees in the state; Maintaining an office or warehouse; Holding inventory; Active solicitation of customers (passive web traffic generally does not count); Holding real estate; Maintaining a bank account (sometimes — varies); Performing services on-site. Some safe-harbors are common across states (Uniform Foreign Corporation Act-style): Defending a lawsuit; Holding director or shareholder meetings; Maintaining a bank account (in some states, not all); Soliciting orders via mail or the internet that are accepted out of state; Owning real or personal property.

### 8.3 Consequences of failure to qualify

- **Consequences of failure to foreign qualify** — Failure to foreign qualify in the operating state typically produces: 1. Loss of access to that state's courts — the entity cannot file a lawsuit (e.g., to sue a non-paying customer) until it qualifies and pays back-taxes and penalties. This is the most painful consequence — a non-qualified Delaware entity that gets stiffed on a $200,000 invoice cannot enforce the contract. 2. Per-day fines — California, for example, charges up to $20/day plus a $250 penalty under R&TC § 19135. 3. Back franchise tax — every year the entity should have been qualified. 4. Personal liability — some states permit creditors to reach the directors and officers personally for unpaid taxes during the period of non-qualification.  _(California R&TC § 19135)_

AUDIT FLASH POINT: Foreign-qualification failure. When a Delaware client is identified, immediately determine the operating state(s). For each operating state, confirm: 1. Date of qualification with that state's Secretary of State; 2. Current good-standing status; 3. All annual reports and franchise tax obligations paid current; 4. State tax registrations (income, employment, sales) in place. A "Delaware LLC operating out of San Francisco for three years that never qualified in California" is a $5,000-$15,000 remediation engagement before any other tax work can be done.

### 8.4 California — the most-common operating state

- **California foreign qualification requirements for Delaware LLC** — For a Delaware LLC foreign-qualified in California: California Form LLC-5 — initial registration, $70 filing fee; California $800 minimum franchise tax — paid by the 15th day of the 4th month after qualification, then annually; California LLC fee (under R&TC § 17942) — based on California-source income, scales from $0 to $11,790; California Form 568 — annual return, due 3.5 months after fiscal year-end; California Statement of Information (Form LLC-12) — every 2 years for LLCs, $20 filing fee.  _(California R&TC § 17942)_
- **California foreign qualification requirements for Delaware C-Corp** — For a Delaware C-Corp foreign-qualified in California: California Form S&DC-S/N — initial registration; California $800 minimum franchise tax — annual; California corporate income tax at 8.84% of California-source income (or 6.65% for S-corps, plus 1.5% S-corp tax); California Form 100 (C) or 100S (S) — annual return; California Statement of Information — annually.

## 9. §83(b) election — the 30-day trap

- **§83(b) election significance** — The §83(b) election is the single most consequential 30-day deadline in startup law and is missed in roughly 10-15% of founder formations based on practitioner surveys. A missed §83(b) election can cost a successful founder millions in incremental ordinary-income tax versus capital-gain tax.

### 9.1 What §83(b) does

- **IRC § 83(a) default treatment and worked example** — Under IRC § 83(a), when an employee or service-provider receives property (including stock) in exchange for services that is subject to a substantial risk of forfeiture (i.e., vesting), the recipient does not recognize income at grant. Instead, income is recognized each time a portion vests, equal to the then-current fair market value minus the amount paid. For a founder who buys 2,000,000 shares at $0.0001 (cost $200) subject to 4-year vesting: - Year 0 (grant): No income recognition. - Year 1 (1/4 vests): 500,000 shares vest. Assume by then the Series A priced common at $1.00/share. Founder recognizes $1.00 × 500,000 − $0.0001 × 500,000 = $499,950 of ordinary income in Year 1. Founder owes ordinary income tax on $499,950 with no cash from the company to pay it. This is sometimes called the "phantom income" problem. - Year 2, 3, 4: Same pattern, at whatever the then-current FMV is. By the time the company is acquired in Year 4 at $10/share, the founder has recognized millions of ordinary income along the way. Under IRC § 83(b), the founder can elect to be taxed at the grant date instead. At the grant date, FMV of common stock = purchase price ($0.0001) because the stock was just sold for that price in an arm's-length transaction. Income at the grant date = $0. No tax. All future appreciation is taxed as capital gain at sale — long-term if held > 1 year (likely the case at exit).  _(IRC § 83(a); IRC § 83(b))_

### 9.2 The 30-day deadline

- **§83(b) election filing deadline and process** — The §83(b) election must be filed with the IRS within 30 days of the property transfer date — not 30 days from formation, not 30 days from signing, but 30 days from the founder writing the check and receiving the stock certificate. The election is filed by: 1. Drafting the §83(b) election statement (one-page document with specific required content under Treas. Reg. § 1.83-2(e)) 2. Mailing by certified mail with return receipt to the IRS service center where the founder files her individual return 3. Keeping the green return-receipt card as proof of timely filing 4. Providing a copy to the corporation 5. Attaching a copy to the founder's individual return for that year (no longer required for tax years after 2015, but still considered best practice)  _(Treas. Reg. § 1.83-2(e))_

### 9.3 Why the 30-day deadline is hard

- **Reasons the §83(b) deadline is difficult to meet** — - The 30 days runs from stock issuance, not formation. Founders who form the corp on day 1 and don't get around to executing the stock purchase agreement until day 45 have already created a §83(b) trap they don't realize exists. - The IRS does not accept e-filed §83(b) elections as of 2025. The election must be paper-filed by mail. (The IRS announced in 2024 an intent to develop an electronic process; as of mid-2025 it is not yet live.) - There is no relief for late filing. Treas. Reg. § 1.83-2(f) does not permit relief under § 9100. The Tax Court and IRS have rejected late filings even when the founder's lawyer made the mistake. - Founders sometimes confuse §83(b) with the §83(i) deferral election for private company stock, which is a different (and rarely-used) election.  _(Treas. Reg. § 1.83-2(f))_

### 9.4 When to file §83(b) — decision rule

- **§83(b) decision rule — when to file and not file** — Always file §83(b) when: Founder is purchasing restricted stock at formation; FMV at grant ≈ purchase price (early-stage, no priced round yet); Founder reasonably expects the stock to appreciate. Do NOT file §83(b) when: Founder is receiving an option (§83(b) does not apply to options — it applies to actual stock; options are governed by §§ 421-422 ISO or §§ 83 NSO rules and the analysis is different); The stock is already fully vested (no risk of forfeiture means §83(a) doesn't apply, so §83(b) is unnecessary); The founder is unlikely to remain through the cliff (because filing §83(b) and then leaving means paying tax on stock the founder doesn't get to keep); FMV at grant is substantially higher than purchase price (the election triggers immediate tax — possibly a large amount — which the founder may not be able to fund).  _(IRC §§ 421-422; IRC § 83)_

AUDIT FLASH POINT: §83(b) 30-day deadline. When onboarding a founder client, the FIRST question after entity confirmation is "when did you sign your stock purchase agreement and write the check, and did you file your §83(b) election within 30 days, and do you have the certified-mail green card?" If the answer to any of those three is unclear, request the formation closing binder and confirm the election was filed timely. A founder who missed the window has lost the election forever — no relief is available.

## 10. US LLC for non-US founders

This section flags the complexity of non-US founder fact patterns but defers the detailed analysis to specialist cross-border skills. Many of the trickiest engagements in any practice are non-US founders forming Delaware LLCs.

### 10.1 The headline issue

- **Non-US founder US tax obligations, Form 5472 requirement** — A non-US person forming a single-member US LLC that is disregarded for federal tax may believe (and may be told by Stripe Atlas or a generalist agent) that the LLC produces no US tax obligation because the LLC is disregarded. This is partly true and partly wrong: - For US federal income tax: the LLC is disregarded; the non-US owner is taxed on US-source income personally - For Form 5472 + Form 1120: the LLC must file Form 5472 with a pro forma Form 1120 every year, regardless of whether there is any US-source income, because of Treas. Reg. § 1.6038A-1 (extended to disregarded entities in 2017). Penalty for non-filing: $25,000 per year per missed filing. This is by far the biggest trap. - For state tax: depends on the state where the LLC has any nexus - For US estate tax: a non-US person holding a US LLC interest may be subject to US estate tax (with only the $60,000 NRA exemption) on death  _(Treas. Reg. § 1.6038A-1)_

### 10.2 Why founders form anyway

Non-US founders use US LLCs because: US banking (Stripe, Mercury, Wise Business); US customer trust (B2B contracts with US enterprises); US payment processing (Stripe and PayPal both prefer US entities); Access to US-denominated revenue without the cost of a full US corporate footprint; IP holding structures (for non-US founders deferring conversion to corp).

### 10.3 Better structures for non-US founders

In many cases, a non-US holding company that owns a US LLC is better than a direct non-US-individual ownership, because the holding company is treated as a corporation for US tax (with possible withholding tax on US-source ECI) and avoids the Form 5472 individual-level issues. This is highly fact-specific and out of scope for this skill.

Cross-reference: For non-US founders forming US LLCs, see also `us-federal-non-resident-llc.md` and `us-form-5472-disregarded-smllc.md` (if those skills exist in the practice library) plus the relevant home-country skill.

## 11. Beneficial Ownership Information (BOI) — current status

- **Corporate Transparency Act BOI requirement** — The Corporate Transparency Act ("CTA"), enacted as part of the National Defense Authorization Act for FY 2021, required most US entities (including Delaware LLCs and Corps) to file a Beneficial Ownership Information (BOI) report with the Financial Crimes Enforcement Network (FinCEN).

### 11.1 Status as of mid-2025

- **BOI litigation timeline and current status** — The CTA's BOI requirements are subject to ongoing constitutional litigation: - December 3, 2024: The US District Court for the Eastern District of Texas issued a nationwide preliminary injunction in Texas Top Cop Shop, Inc. v. Garland, halting BOI enforcement - January 2025: The Supreme Court stayed the injunction in part, allowing FinCEN to continue accepting (but not requiring) BOI filings while litigation proceeds - March 2025: Treasury issued a "non-enforcement statement" suspending BOI penalties for domestic reporting companies - As of November 2025: BOI reporting is effectively suspended for domestic entities but FinCEN continues to accept voluntary filings. The picture remains fluid; the rule may be reinstated, narrowed (to foreign-owned entities only), or struck down entirely.  _(Texas Top Cop Shop, Inc. v. Garland)_

### 11.2 Practitioner guidance

- Do not advise clients that BOI is mandatory in mid-to-late 2025 without checking the current FinCEN guidance page
- Do advise clients to be prepared to file if the injunction is lifted — track beneficial owners' driving licenses, passports, and ownership percentages now
- Foreign entities qualifying to do business in the US may still be subject to BOI under the post-March 2025 carve-out — fact-pattern dependent

## 12. Common errors — the practitioner's checklist

These are the errors that show up repeatedly in client portfolios when a Delaware entity is reviewed for the first time. The skill flags them as the top remediation priorities.

### 12.1 Startup uses the Authorized Shares method by default

- **Error: Authorized Shares method default** — Symptom: Client receives a Delaware franchise tax invoice for $5,000-$85,000 in March, panics, calls the practitioner. Cause: The Division of Corporations defaults the franchise tax invoice to the Authorized Shares method. For any corporation with 10M+ authorized shares and low gross assets, this method dramatically over-states the tax. Fix: Recompute under the Assumed Par Value method on the annual report (§ 4 of this skill). Pay the lower amount. If the client has already paid the higher invoice in a prior year, request a refund from the Division of Corporations — refunds are available within the statute of limitations.

### 12.2 Entity doesn't qualify in the operating state

- **Error: failure to foreign qualify** — Symptom: Client sues a non-paying customer in operating-state court. Defendant's lawyer moves to dismiss because the plaintiff (the Delaware entity) is not foreign-qualified. Cause: Founder formed in Delaware following internet advice but never registered in the operating state. Fix: Foreign-qualify immediately. Pay all back franchise tax, penalties, and interest in the operating state. The court will typically stay the litigation for 30-60 days to permit cure, but the entity has already paid for emergency-track filings.

### 12.3 Forgets §83(b) within 30 days

- **Error: missed §83(b) election** — Symptom: Three years after formation, the company is acquired in a $50M stock-for-stock deal. The founder discovers she has been recognizing ordinary income on each tranche of vesting at the then-current FMV, owes ordinary income tax on $4M of cumulative recognized income, and only realizes long-term capital gain treatment on the portion that vested more than 12 months before sale. Cause: Founder didn't know about §83(b), or knew but forgot, or filed late, or filed without certified mail and can't prove timeliness. Fix: None. The 30-day window cannot be reopened. The only remediation is forward-looking — if any additional restricted stock grants occur (e.g., a follow-on founder grant), file §83(b) timely for those.

### 12.4 LLC vs C-Corp confusion

- **Error: LLC formed instead of C-Corp for VC-track startup** — Symptom: Founder pitches a VC. VC reads the pitch deck, sees "Acme Innovations LLC," declines the meeting. Cause: Founder formed an LLC for simplicity and tax pass-through but is now seeking institutional capital. VCs cannot invest in LLCs because (a) LLC interests are treated as partnership interests, generating unrelated business taxable income (UBTI) for tax-exempt LPs in the VC fund; (b) LLC operating agreements require negotiation of profit-and-loss allocations under §704(b); (c) no standardized NVCA equivalent exists. Fix: Delaware flip — convert the LLC to a Delaware C-Corp. Two main techniques: 1. Statutory conversion under DGCL § 265 (LLC converts directly to corp); 2. F-reorganization structure with a holding C-Corp. Both have tax consequences and should be planned before the term sheet. Cost: $15,000-$40,000 in legal fees, possibly tax cost on built-in gain.  _(DGCL § 265; IRC § 704(b))_

### 12.5 Dormant LLC accruing $500/year

See § 2.5 of this skill. Surface all Delaware LLCs in the client's history. Pay or formally dissolve.

### 12.6 Operating agreement on the back of a napkin

Symptom: Founders fall out. Litigation. The "operating agreement" is a Google Doc nobody signed with placeholder bracketed text.

Fix: Draft a real operating agreement at formation. If the entity is already in dispute, refer to litigation counsel — the practitioner does not paper over an active dispute.

### 12.7 Personal liability via piercing

Symptom: Sole member uses the LLC bank account to pay personal credit cards. Creditor sues, prevails on a veil-piercing claim.

Cause: Commingling. The LLC is treated as the alter ego of the member.

Fix: Strict separation of LLC funds from personal funds. Use a real business bank account. Pay yourself via an "owner's draw" transfer, not by swiping the LLC debit card at Whole Foods.

### Example 1 — YC startup forming a Delaware C-Corp

Two co-founders, Maya and Devon, building a B2B SaaS product. Accepted into the YC W26 batch. Plan to raise a $5M seed in March 2026 and a Series A in early 2027. Currently bootstrapping out of Maya's apartment in San Francisco.

**Recommended structure**

| Element | Choice |
| --- | --- |
| Entity type | **Delaware C-Corporation** (VC-track, will raise institutional capital) |
| Authorized shares | **10,000,000** |
| Par value | **$0.0001** |
| Initial issuance to founders | **8,000,000 split per founder agreement** (e.g., 50/50 = 4M each, or 60/40 = 4.8M / 3.2M) |
| Treasury reserve | 2,000,000 shares (will become part of option pool at Series A) |
| Founder vesting | 4-year monthly vesting with 1-year cliff |
| Founder purchase price | $0.0001 × shares issued (e.g., 4,000,000 × $0.0001 = $400 personal check) |
| §83(b) election | **MANDATORY** — filed within 30 days, certified mail with green card |
| Bylaws | YC SAFE-compatible default bylaws |
| Initial board | Two founders (institutional board seats added at seed and Series A) |
| Initial officers | Maya = CEO + Secretary; Devon = CTO + Treasurer |
| Registered agent | Cogency Global (premium provider — investors will check) |
| Foreign qualification | **California Form S&DC-S/N** filed immediately because the office is in SF |
| EIN | Filed via SS-4 online same week as formation |
| Bank account | Mercury or SVB (now First Citizens) opened in week 2 |
| Franchise tax method | Assumed Par Value method — must be elected on first annual report by March 1, 2027 |

- DE annual report + franchise tax: ~$450 (assuming gross assets stay modest)
- DE registered agent: $250
- CA $800 minimum franchise tax: $800
- CA Statement of Information: ~$25/year amortized
- **Total ~$1,525/year** while bootstrapping; rises after Series A as gross assets grow

- **30 days from stock purchase:** §83(b) filing for each founder
- **March 1 each year:** DE annual report + franchise tax (use Assumed Par Value method)
- **April 15 each year:** California Form 100 + federal Form 1120 (or extensions)
- **15th day of 4th month after formation:** California first $800 minimum franchise tax

### Example 2 — E-commerce LLC

Solo founder Priya, dropshipping a single-product Shopify store from her Austin, TX apartment. Expected first-year revenue $100,000-$300,000. No outside investment planned. Wants liability protection and an EIN for vendor onboarding.

**Recommended structure**

| Element | Choice |
| --- | --- |
| Entity type | **Delaware LLC, single-member, disregarded** |
| Why DE? | Honestly, **why not Texas LLC?** Texas is her operating state. Forming TX-only avoids foreign qualification. Delaware is overkill for a single-member solo e-commerce business with no investor or sale plans. |
| Recommendation | **Form Texas LLC instead.** Save the Delaware $300/year, save the foreign qualification step, save the second registered agent fee. Use Delaware only if there is a real reason (multi-state operations, future investor expectation, IP licensing structure). |

**If client insists on Delaware** (e.g., privacy preference, future relocation plans):

- DE Certificate of Formation: $90 + $50 expedited
- DE registered agent: $50/year (Harvard Business Services)
- DE annual LLC tax: $300/year
- **Foreign qualify in Texas** (Texas Form 304 — Application for Registration of a Foreign LLC, $750 filing fee)
- Texas no income tax, but **Texas Franchise Tax** applies via Form 05-102 PIR (see `tx-franchise-tax.md`)
- §83(b) **N/A** — single-member LLC, member capital interest not subject to vesting unless the operating agreement explicitly creates vesting (unusual)

- DE registered agent: $50
- DE $300 annual tax: $300
- Texas franchise tax: $0 (under no-tax-due threshold)
- Texas PIR: $0 filing fee
- **Total ~$350/year** + $750 one-time TX foreign qualification

- TX registered agent: $50-$125 (or self if founder maintains TX address)
- TX franchise tax: $0
- TX PIR: $0
- **Total ~$50-$125/year**

The Texas-formed structure saves **~$300/year**. The Delaware-formed structure costs more for zero functional benefit in this fact pattern. The practitioner's job is to **redirect** the client to the cheaper, better choice.

### Example 3 — Real estate Series LLC

Sarah and Marcus, married, own three rental properties: a duplex in Atlanta, a triplex in Phoenix, and a single-family rental in Nashville. Each property generates $15,000-$30,000 of net rental income annually. They want firewall liability between properties so a tenant lawsuit against one cannot reach the others.

1. **Three separate LLCs** (one per property)
   - Cost: $300/year × 3 = $900/year in DE annual tax, plus three registered agents ($150-$450), plus three foreign qualifications ($600-$1,500 across GA, AZ, TN), plus three separate bookkeeping streams
   - Pro: Clean separation, no Series LLC complexity, recognized in every state
2. **One LLC owning all three properties**
   - Cost: $300/year in DE, plus foreign qualification in all three states
   - Con: **No firewall** — a lawsuit against the LLC reaches all three properties
3. **Delaware Series LLC with one series per property**
   - Cost: $300/year in DE (single LLC fee covers all series), plus registered agent, plus foreign qualifications
   - Pro: Firewall between series, single annual filing
   - Con: Some operating states may not respect the firewall

- **Georgia Series LLC firewall recognition** — Georgia recognizes Series LLC firewall  _(Georgia Code § 14-11-1107)_
- **Arizona Series LLC firewall recognition** — Arizona recognizes Series LLC firewall  _(A.R.S. § 29-3401)_
- **Tennessee Series LLC firewall recognition** — Tennessee recognizes Series LLC firewall  _(Tenn. Code Ann. § 48-249-309)_

Delaware Series LLC if all operating states recognize the firewall. As of 2025:

- **Georgia:** Recognizes Series LLC firewall (Georgia Code § 14-11-1107)
- **Arizona:** Recognizes (A.R.S. § 29-3401)
- **Tennessee:** Recognizes (Tenn. Code Ann. § 48-249-309)

All three states recognize the firewall, so Series LLC works for this fact pattern.

**Structure mechanics**

| Element | Detail |
| --- | --- |
| Master entity | Delaware Series LLC with explicit Series authorization in the Certificate and operating agreement |
| Master Certificate of Formation | Includes the § 18-215(b)(3) notice provision |
| Series A | Atlanta duplex — separate bank account, separate books, separate insurance |
| Series B | Phoenix triplex |
| Series C | Nashville SFR |
| Federal tax treatment | Each series files its own federal return as a partnership (since Sarah and Marcus jointly own each series) — or, if structured carefully under Rev. Proc. 2002-69, as a disregarded entity wholly owned by a community-property couple |
| Operating agreement | Series-LLC-specific master agreement plus Series Designation documents for each series |
| Foreign qualifications | The **master LLC** foreign-qualifies in GA, AZ, TN — not each series separately (most states do not require series-level qualification, but some do; check state-by-state) |

### Example 4 — Foreign founder with US LLC

Klaus, a German tax resident, runs an online consulting business serving US-based clients. Wants to bill US clients in USD via Stripe, hold the funds in a US bank account, and avoid the Germany-side hassle of receiving USD wire transfers.

"Form a single-member Delaware LLC, disregarded for US federal tax. Since you're a non-US person and the LLC is disregarded and the income is German-source consulting income (you perform the services in Germany), there's no US tax."

- The federal income tax conclusion is **mostly correct** (assuming no US permanent establishment, which is a fact-specific analysis)
- The **Form 5472 filing requirement is absolute**: every year, the LLC must file Form 5472 with a pro forma Form 1120, disclosing the foreign owner and all "reportable transactions" between the foreign owner and the LLC. Penalty for non-filing: **$25,000 per year per missed form** under § 6038A(d). This is enforced.
- The LLC needs an **EIN** — Klaus must file Form SS-4 (paper, because he has no SSN/ITIN), wait 4-8 weeks for processing
- **US estate tax exposure**: a non-US person's US-situs assets (including a US LLC interest, arguably) are subject to US estate tax above a $60,000 exemption. This is a long-term planning issue.
- **Germany-side analysis**: Klaus must report the US LLC and its income to the German tax authorities. Germany's controlled foreign company rules may apply. **This is out of scope of this US-DE skill — refer Klaus to a German tax advisor.**

**Recommended structure**

| Element | Detail |
| --- | --- |
| Entity | Delaware single-member LLC, disregarded |
| Registered agent | Northwest Registered Agent ($125/year — strong privacy posture, will not list Klaus's German address on filings) |
| EIN | Filed via paper Form SS-4 (Klaus has no SSN/ITIN); allow 8 weeks |
| Bank | Mercury (accepts non-US founders); Stripe Atlas-bundled option also available |
| Annual federal filings | **Form 5472 + pro forma Form 1120, by April 15 each year** — NEVER MISS |
| Annual DE filings | $300 LLC tax by June 1 |
| Foreign qualification | None — Klaus has no US operating state, just a Delaware LLC with no US activity |
| §83(b) | N/A — single-member LLC, no stock |
| German tax | Out of scope — refer to German advisor |

- DE registered agent: $125
- DE annual tax: $300
- US federal filing prep (Form 5472 + 1120 pro forma): $500-$1,500 from a specialist preparer
- **Total ~$925-$1,925/year**

- **Critical risk — Form 5472 late filing penalty** — If Klaus fails to file Form 5472 by April 15 of any year, $25,000 penalty. This is the dominant compliance risk in non-US founder Delaware LLC engagements and the skill flags it as the highest-priority recurring task.  _(§ 6038A(d))_

## 14. Reviewer checklist

Before signing off on a Delaware entity formation engagement, the credentialed reviewer should confirm:

- [ ] Entity type (LLC vs C-Corp vs Series LLC vs DST vs PBC) matches the client's actual business plan and investor expectations
- [ ] Authorized share structure (for C-Corps) is 10M / $0.0001 par or another structure that minimizes Assumed Par Value franchise tax
- [ ] Certificate of Formation / Certificate of Incorporation filed and stamped by the Delaware Division of Corporations
- [ ] Registered agent engaged and first-year fee paid
- [ ] Operating Agreement (LLC) or Bylaws + organizational consents (C-Corp) executed
- [ ] EIN obtained (or in process for non-US founders)
- [ ] §83(b) election filed within 30 days for every founder receiving restricted stock — **certified mail green cards collected and filed in the corporate minute book**
- [ ] Foreign qualification filed in the operating state (or documented determination that no operating-state nexus exists)
- [ ] Operating-state franchise tax / minimum tax / annual report / statement of information schedule documented and entered into the client's tax calendar
- [ ] Delaware March 1 (corp) / June 1 (LLC) deadlines entered into the practice's calendar system
- [ ] BOI status determined (likely suspended as of 2025, but document the determination)
- [ ] For non-US founders: Form 5472 + pro forma 1120 obligation flagged and entered into the calendar; German/UK/Indian/etc. home-country advisor identified
- [ ] Franchise tax computation method (Authorized Shares vs Assumed Par Value) determined for the first March 1 filing

## 15. Authority and citations

**Authority and citations**

| Source | Citation |
| --- | --- |
| Delaware LLC Act | 6 Del. C. §§ 18-101 — 18-1208 |
| Delaware General Corporation Law | 8 Del. C. §§ 101 — 398 |
| Series LLC provision | 6 Del. C. § 18-215 |
| Delaware Statutory Trust Act | 12 Del. C. §§ 3801 — 3863 |
| Public Benefit Corporations | 8 Del. C. §§ 361 — 368 |
| Annual LLC tax | 6 Del. C. § 18-1107 |
| Annual report (corps) | 8 Del. C. § 502 |
| Franchise tax (corps) | 8 Del. C. § 503 |
| IRC §83 (restricted stock) | 26 U.S.C. § 83 |
| §83(b) regulations | Treas. Reg. § 1.83-2 |
| Form 5472 disregarded entity reporting | Treas. Reg. § 1.6038A-1 |
| Corporate Transparency Act | 31 U.S.C. § 5336; 31 CFR § 1010.380 |
| Texas Top Cop Shop injunction | Civil Action No. 4:24-CV-478 (E.D. Tex. Dec. 3, 2024) |
| Revenue Ruling on DST 1031 eligibility | Rev. Rul. 2004-86, 2004-2 C.B. 191 |
| Treasury proposed regs on Series LLCs | Prop. Treas. Reg. § 301.7701-1(a)(5) (2010) |

- **6 Del. C. §§ 18-101 — 18-1208** — 6 Del. C. §§ 18-101 — 18-1208  _(Delaware LLC Act)_
- **8 Del. C. §§ 101 — 398** — 8 Del. C. §§ 101 — 398  _(Delaware General Corporation Law)_
- **6 Del. C. § 18-215** — 6 Del. C. § 18-215  _(Series LLC provision)_
- **12 Del. C. §§ 3801 — 3863** — 12 Del. C. §§ 3801 — 3863  _(Delaware Statutory Trust Act)_
- **8 Del. C. §§ 361 — 368** — 8 Del. C. §§ 361 — 368  _(Public Benefit Corporations)_
- **6 Del. C. § 18-1107** — 6 Del. C. § 18-1107  _(Annual LLC tax)_
- **8 Del. C. § 502** — 8 Del. C. § 502  _(Annual report (corps))_
- **8 Del. C. § 503** — 8 Del. C. § 503  _(Franchise tax (corps))_
- **26 U.S.C. § 83** — 26 U.S.C. § 83  _(IRC §83 (restricted stock))_
- **§83(b) regulations** — Treas. Reg. § 1.83-2
- **Treas. Reg. § 1.6038A-1** — Treas. Reg. § 1.6038A-1  _(Form 5472 disregarded entity reporting)_
- **31 U.S.C. § 5336; 31 CFR § 1010.380** — 31 U.S.C. § 5336; 31 CFR § 1010.380  _(Corporate Transparency Act)_
- **Civil Action No. 4:24-CV-478 (E.D. Tex. Dec. 3, 2024)** — Civil Action No. 4:24-CV-478 (E.D. Tex. Dec. 3, 2024)  _(Texas Top Cop Shop injunction)_
- **Rev. Rul. 2004-86, 2004-2 C.B. 191** — Rev. Rul. 2004-86, 2004-2 C.B. 191  _(Revenue Ruling on DST 1031 eligibility)_
- **Prop. Treas. Reg. § 301.7701-1(a)(5) (2010)** — Prop. Treas. Reg. § 301.7701-1(a)(5) (2010)  _(Treasury proposed regs on Series LLCs)_

## 16. Version history

**Version history**

| Version | Date | Author | Changes |
| --- | --- | --- | --- |
| 0.1 | 2025-11-15 | OpenAccountants engineering | Initial draft — Tier 2 content for tax year 2025 |

- **0.1** — 2025-11-15  _(Initial draft — Tier 2 content for tax year 2025)_

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
