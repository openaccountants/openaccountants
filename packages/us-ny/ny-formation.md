---
name: ny-formation
description: Tier 2 New York content skill for entity formation covering tax year 2025. Includes the NY LLC $200 Articles of Organization, the unique LLC publication requirement under LLC Law §206 (2 newspapers, 6 consecutive weeks, costing $1,000-$2,000+ in NYC vs $50-$200 outside), $50 biennial Statement, NY C-Corp $125 Certificate of Incorporation with no publication requirement, NYC Unincorporated Business Tax 4%, biennial DOS-1357 ($9), and the NY-specific S-Corp election separate from federal §1362.
jurisdiction: US-NY
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# NY Formation

## 1. Scope

This skill is a **Tier 2 content layer** covering the procedural and tax mechanics of forming a business entity in the State of New York. It is intended to be loaded alongside:

- `us-tax-workflow-base` (Tier 1 workflow scaffolding)
- `ny-corporate-franchise-article-9a.md` (for C-Corp franchise tax computation)
- `nyc-ubt.md` (for NYC Unincorporated Business Tax computation)
- `ny-llc-filing-fee.md` (for the annual NY-LLC fee)
- `us-s-corp-election-decision.md` (for federal S-corp election analysis)

**In scope:**

- Formation of NY domestic Limited Liability Companies (LLCs) under N.Y. Limited Liability Company Law
- Formation of NY domestic business corporations under N.Y. Business Corporation Law
- The LLC publication requirement under LLC Law §206
- The NY S-corporation election under N.Y. Tax Law §660(a) (separate from federal §1362)
- Biennial Statement filing under BCL §408 and LLCL §301-A
- NYC-specific overlays: Unincorporated Business Tax, General Corporation Tax (legacy), Business Corporation Tax (post-2015 reform)
- NY Wage Theft Prevention Act notice obligations on formation
- Beneficial Ownership Information (BOI) / Corporate Transparency Act status as of tax year 2025

**Out of scope:**

- Foreign (out-of-state) entities qualifying to do business in NY — handled in a separate skill
- Not-for-profit corporations under N-PCL
- Professional Service Corporations (PCs) and Professional LLCs (PLLCs) — partially covered; refer to NY Education Law for licensing overlays
- Partnerships and Limited Partnerships under Partnership Law (only briefly referenced)
- Federal entity classification election (Form 8832) and federal S-corp election (Form 2553) — those are federal-skill territory
- New York State estimated tax, withholding, and unemployment insurance registration — see `ny-estimated-tax.md`, `ny-mctmt.md`

**Authorities relied on:**

- N.Y. Limited Liability Company Law (LLCL), in particular §§203, 206, 301-A, 1102
- N.Y. Business Corporation Law (BCL), in particular §§402, 408
- N.Y. Tax Law §§208 (corporation franchise tax), 660 (S-corp election), 1330 (NYC GCT), 1306 (NYC UBT)
- N.Y. Labor Law §195 (Wage Theft Prevention Act)
- NYC Administrative Code Title 11, Chapters 5 and 6 (UBT and GCT)
- N.Y. Department of State filing fee schedules effective for 2025
- Corporate Transparency Act, 31 U.S.C. §5336, and Treasury enforcement notices through November 2025

## 2. Why New York

New York is a **high-cost, high-value formation jurisdiction**. It is not a "tax-haven" state like Delaware, Nevada, or Wyoming, and small operators sometimes recoil at the LLC publication cost. Despite this, many founders — especially in technology, financial services, real estate, hospitality, and media — choose to form directly in New York rather than form in Delaware and qualify as a foreign LLC. The reasons reviewers should understand:

1. **Local presence economics.** If the entity is going to have a New York City office, hire New York employees, sign a New York lease, or sell to New York customers, it is going to be subject to New York taxation regardless of the state of formation. Forming out-of-state and then qualifying as a foreign entity doubles the compliance work: you pay the home-state biennial/annual fee **plus** you pay the New York foreign-qualification fee, plus you trigger the publication requirement anyway (LLC Law §802(b)(v) applies the publication requirement to foreign LLCs that obtain authority to do business in NY). So the typical "Delaware LLC" play does **not** avoid the New York publication cost if the entity actually operates in New York.

2. **Investor familiarity.** Venture investors, banks, and institutional landlords are comfortable with NY-formed entities. NY's corporate jurisprudence is well-developed and predictable.

3. **Access to NY courts and judgment enforcement.** A NY-formed entity defaults to NY personal jurisdiction. For New York-centric businesses, this is a feature, not a bug.

4. **Wall Street, Hudson Yards, Brooklyn tech corridor, Long Island manufacturing, Hudson Valley life-sciences clusters** — all of these create natural reasons to form in NY rather than ship the formation to Delaware.

5. **Brand signaling.** "Inc., New York, New York" carries marketing weight in finance, fashion, hospitality, and media that "Inc., Wilmington, Delaware" does not.

The corollary is that **forming in NY is not free**. A reviewer counseling a founder should always confirm the founder understands the publication cost up front, especially if the operating address is in Manhattan, where the publication invoice can exceed the entire rest of the first-year formation budget.

## 3. NY LLC Formation Mechanics

### 3.1 Articles of Organization

- **Articles of Organization filing fee** — $200  _(LLCL §203, Form DOS-1336)_
- **Articles must state** — Name of the LLC (must contain "Limited Liability Company", "L.L.C.", or "LLC" — LLCL §204); County within New York State in which the office of the LLC is to be located (dictates which newspapers will be designated for publication — see §3.3); Designation of the Secretary of State as agent for service of process, with an address to which process should be forwarded; Signature of the organizer. Optional but common provisions include the registered agent (in addition to the Secretary of State), a specified dissolution date, the duration, and any limitations on liability of members.  _(LLCL §203, §204)_
- **Filing channels** — Online via the NY DOS Business Express system (preferred — typically processed within a few business days); By mail to NY Department of State, Division of Corporations; 24-hour expedited service: additional $25; Same-day expedited service: additional $75; 2-hour expedited service: additional $150

### 3.2 Operating Agreement

- **Operating Agreement requirement** — LLCL §417 requires every NY LLC to adopt a written Operating Agreement within 90 days of filing the Articles of Organization. The Operating Agreement does not get filed with the Department of State; it is an internal document. Reviewers should confirm one exists. The statute is largely toothless in that there is no fine for failing to adopt one, but its absence can create real problems in disputes between members and in due-diligence reviews by counterparties. Single-member LLCs still must adopt an Operating Agreement. Many founders skip this because there is no one else to sign it; a sole-member agreement is still legally appropriate and recommended.  _(LLCL §417)_

### 3.3 The Publication Requirement (LLCL §206) — AUDIT FLASH POINT

**This is the most-missed and most-misunderstood NY formation step.** It is also the single item that most commonly results in legal disability of the entity. Treat it as an AUDIT FLASH POINT every time you encounter a NY LLC.

- **The rule** — Within 120 days after the Articles of Organization become effective, the LLC must publish a copy of the Articles (or a notice containing the substance of the Articles) once each week for six successive weeks in two newspapers — one daily and one weekly — designated by the county clerk of the county in which the office of the LLC is located (as stated in the Articles).  _(LLCL §206)_
- **Certificate of Publication filing** — After publication, the LLC must file a Certificate of Publication (Form DOS-1708) with the Department of State, accompanied by the affidavits of publication from the two newspapers. The DOS filing fee for the Certificate of Publication is $50.  _(Form DOS-1708)_
- **Consequence of failure** — Under LLCL §206(a), an LLC that fails to publish within the 120-day window has its authority to carry on, conduct, or transact any business in New York suspended. The suspension is not automatic dissolution in the strict statutory sense, but the practical effect is severe: The LLC cannot maintain an action or special proceeding in any New York court while suspended (LLCL §206(a)); Members may face personal liability exposure on contracts entered into while the LLC was non-compliant; Many counterparties (banks, landlords, payment processors) will refuse to do business with an LLC that cannot produce a current Certificate of Status from the Department of State. The suspension can be cured by completing publication late and filing the Certificate of Publication. The cure is retroactive in effect (the LLC's existence is treated as continuous), but contracts entered into during the suspension period may remain vulnerable to challenge.  _(LLCL §206(a))_

**Cost ranges by location of LLC office**

| Location of LLC office | Typical publication cost |
| --- | --- |
| New York County (Manhattan) | $1,200 – $2,000+ |
| Kings County (Brooklyn) | $1,000 – $1,800 |
| Queens County | $700 – $1,200 |
| Bronx County | $600 – $1,000 |
| Richmond County (Staten Island) | $400 – $800 |
| Nassau County | $400 – $700 |
| Westchester County | $350 – $600 |
| Most upstate counties (Albany, Buffalo, Rochester, Syracuse) | $50 – $200 |
| Rural upstate (Allegany, Schoharie, Lewis, Hamilton) | $50 – $150 |

The cost differential is driven by the rate cards of the newspapers the county clerk designates. In Manhattan, the designated daily is invariably one of the New York Law Journal or The Daily News or The New York Post; their per-line rates are an order of magnitude higher than the small upstate weeklies.

- **The "Albany County dodge"** — A widely-circulated piece of advice is to list Albany County (or another low-cost county) as the LLC's office in the Articles of Organization, complete publication cheaply there, then operate the business from Manhattan. This is legally valid in the sense that LLCL §203 only requires the Articles to name a county within New York State; it does not require that county to be the principal place of business. However, reviewers should flag three concerns: 1. NYC tax nexus is not avoided — NYC will tax the business based on where the activity actually occurs, not where the Articles say the office is; 2. Service of process address — some practitioners conflate "county of office" with "registered agent address" — they are distinct; 3. Bank, landlord, and investor scrutiny — sophisticated counterparties review the Articles and an Albany County filing for a Manhattan-operating LLC sometimes draws questions. That said, the Albany County (or similar low-cost county) strategy is widely used and is, in our experience, accepted by the DOS. Many practitioners advise it routinely for budget-conscious clients. The skill should not steer the user toward or away from it — just disclose the trade-offs.  _(LLCL §203)_

### 3.4 Biennial Statement (LLCL §301-A)

- **Biennial Statement requirement and fee** — Every NY LLC must file a Biennial Statement with the Department of State during the calendar month every two years that contains the anniversary of the LLC's formation. The fee is $9.  _(LLCL §301-A)_
- **Form updates** — The form (Form DOS-1290) updates: The address to which the Secretary of State should forward service of process; The name and street address of the registered agent (if any); The principal business location of the LLC.  _(Form DOS-1290)_
- **Consequence of failure to file** — The LLC is marked "past due" in the DOS database. The DOS does not administratively dissolve LLCs for failure to file the Biennial Statement (unlike many other states), but past-due status causes the Certificate of Status to indicate non-compliance, which can interfere with bank and counterparty due diligence. The fix is simply to file the late Biennial Statement and pay the $9 fee.

### 3.5 Annual NY-LLC Filing Fee (Tax Law §658(c)(3))

- **IT-204-LL annual filing fee range** — $25 to $4,500 USD per year  _(Tax Law §658(c)(3), Form IT-204-LL)_
- **Applicability** — Separate from the biennial DOS filing, every NY LLC that is treated as a partnership or disregarded entity for federal tax purposes and that has any income, gain, loss, or deduction from New York sources, must pay an annual filing fee based on New York-sourced gross income. This fee is filed on Form IT-204-LL. See `ny-llc-filing-fee.md` for the bracket schedule. This fee is separate from, and on top of, the biennial $9 DOS Statement. Both are required.  _(Tax Law §658(c)(3))_

### 3.6 Federal Form 1065 (Informational)

- **Federal 1065 / NY IT-204 pass-through treatment** — If the LLC has more than one member, it files a federal Form 1065 partnership return. New York piggybacks via Form IT-204. There is no NY entity-level income tax on the LLC itself (the income flows through to members), but the IT-204-LL filing fee in §3.5 above is a separate and unavoidable cost. If the LLC has one member and is treated as a disregarded entity, no Form 1065 is filed federally, but IT-204-LL is still owed at the NY level if there is any NY-source gross income.

## 4. NY C-Corporation Formation Mechanics

### 4.1 Certificate of Incorporation

- **Certificate of Incorporation filing fee** — $125 USD  _(BCL §402, Form DOS-1239)_
- **Share tax and total example cost** — Plus a tax on shares: $0.05 per share for the first 20,000 shares, then graduating downward. For a typical 200-share startup at par value, the total filing cost is $135.  _(BCL §402)_
- **Certificate must state** — Name (must contain "Corporation", "Incorporated", "Limited", or a recognized abbreviation — BCL §301); Purpose (a general business purpose clause is acceptable — "to engage in any lawful business activity"); Aggregate number of shares the corporation is authorized to issue, with par value or "no par"; County in NY where the office is to be located; Designation of the Secretary of State as agent for service of process; Names and addresses of the incorporators.  _(BCL §301, §402)_

### 4.2 No Publication Requirement

- **No publication requirement for corporations** — Critical contrast with LLCs: NY business corporations are not subject to the publication requirement under BCL or under LLCL §206. Many founders, when comparing LLC vs C-corp formation costs, fail to appreciate that the publication requirement is the swing item. A bare comparison of $200 (LLC filing fee) vs $125 (C-corp filing fee) understates the LLC cost by an order of magnitude in NYC. This is one of the legitimate reasons why some Manhattan-based founders default to C-corp form even when LLC would otherwise be the preferred federal tax structure for their situation.  _(LLCL §206)_

### 4.3 Biennial Statement (BCL §408)

- **Corporation Biennial Statement fee** — $9 USD  _(BCL §408, Form DOS-1357)_
- **Form updates** — The form updates the same information as the LLC Biennial Statement (service of process address, registered agent, principal business location), plus: Names and business addresses of the corporation's chief executive officer; Principal business address of the corporation.  _(BCL §408)_

### 4.4 NY Corporate Franchise Tax

- **Franchise tax scope and minimum tax range** — NY C-corporations are subject to corporate franchise tax under Article 9-A of the Tax Law. This skill does not attempt to compute the franchise tax — refer to `ny-corporate-franchise-article-9a.md`. The minimum tax (the floor tax that applies even with no business income) is graduated by NY receipts and ranges from $25 (for a corporation with NY receipts of $100,000 or less) up to $200,000 (for a corporation with NY receipts over $1 billion). For most freelance-developer-sized clients forming a NY C-corp, the minimum tax is $25 or $75 per year.  _(Tax Law Article 9-A)_

## 5. NY S-Corporation Election

The federal Subchapter S election (Form 2553) made under IRC §1362 does not automatically flow through to New York. NY requires a separate state-level S-corp election under N.Y. Tax Law §660(a), made on Form CT-6 ("Election by a Federal S Corporation to be Treated as a New York S Corporation").

- **Eligibility** — The corporation must already have a valid federal S-corporation election in effect; The corporation must be a NY-resident corporation (formed in NY) or a foreign corporation doing business in NY that is subject to franchise tax under Article 9-A; All shareholders who are NY residents on the date the election is made (or, for a new corporation, on the first day of the first taxable year) must consent.  _(N.Y. Tax Law §660(a))_
- **Timing** — For the election to be effective for a tax year, Form CT-6 must be filed within 2½ months of the first day of the tax year, or at any time during the preceding tax year. This is parallel to the federal §1362(b) timing rule.  _(N.Y. Tax Law §660(a); IRC §1362(b))_
- **Effect of the election** — The S-corp's income, losses, deductions, and credits flow through to NY-resident shareholders on Form CT-34-SH and on the shareholders' Form IT-201 (NY personal income tax return); The corporation itself still pays NY franchise tax, but at the fixed-dollar minimum tax schedule (the same minimum as for C-corps, ranging from $25 to $4,500 based on NY receipts) rather than the higher business-income tax; The corporation also potentially owes the MTA Surcharge if it operates in the Metropolitan Commuter Transportation District (NYC + Nassau, Suffolk, Westchester, Rockland, Orange, Putnam, Dutchess counties).
- **Mandatory NY S-corp treatment** — Under N.Y. Tax Law §660(i), a federal S-corporation that has investment income exceeding 50% of its federal gross income is mandatorily treated as a NY S-corporation, regardless of whether Form CT-6 has been filed. This is a trap for founders who do not realize they triggered automatic NY S treatment.  _(N.Y. Tax Law §660(i))_
- **Failure to file Form CT-6** — If the federal S-election is in effect but the founder did not file Form CT-6, the entity is taxed as a NY C-corporation. This generally produces a worse tax outcome (the corporation pays full Article 9-A tax on its business income, and the shareholders receive distributions taxed as dividends rather than pass-through income). Reviewers should check Form CT-6 filing status for every federal S-corp client they encounter.

## 6. NYC-Specific Requirements

New York City has its own tax regime that overlays the NY State regime. The NYC system is administered by the NYC Department of Finance, not the NY State Department of Taxation and Finance. This produces real compliance complexity.

### 6.1 NYC Unincorporated Business Tax (UBT) — AUDIT FLASH POINT

- **UBT tax rate** — 4% (of taxable income after exemption)  _(Section 7 — NY-specific tax framework > NYC Unincorporated Business Tax (UBT) — Form NYC-202)_
- **Who UBT applies to** — Sole proprietors carrying on a trade, business, profession, or occupation wholly or partly within NYC; Partnerships (including LLCs taxed as partnerships) carrying on a trade, business, profession, or occupation wholly or partly within NYC; Single-member LLCs that are disregarded for federal tax purposes are treated as the activity of the member (so if the member is an individual sole proprietor, UBT applies to the individual).  _(NYC Administrative Code Title 11, Chapter 5)_
- **UBT exemption/credit thresholds** — A credit eliminates UBT for businesses with UBT taxable income of $95,000 or less; a partial credit phases out the credit between $95,000 and $150,000 of UBT taxable income; above $150,000, full UBT applies.  _(NYC Administrative Code Title 11, Chapter 5)_
- **Form** — NYC-202 (individual sole props) or NYC-204 (partnerships/LLCs). See `nyc-ubt.md` for the full computation.

New NYC-based freelance software developers (the prototypical sole-prop or single-member-LLC client) frequently fail to file Form NYC-202. They file federal Schedule C, NY State IT-201, and stop there. The UBT is invisible to them until the NYC DOF sends a notice. By that point, late-filing penalties and interest may have accrued. Reviewers should always verify UBT filing status for any NYC-resident individual carrying on a trade or business. A common defensive argument is that the freelancer is "performing services as an employee" rather than as an independent business — but if the freelancer files Schedule C federally, that argument is foreclosed at the city level too.

### 6.2 NYC General Corporation Tax (GCT) — Legacy

- **GCT history and applicability** — Prior to 2015, NYC corporations paid the NYC General Corporation Tax (GCT) under Title 11, Chapter 6, Subchapter 2. The 2015 NYC corporate tax reform (NYC Local Law 60 of 2015) repealed the GCT for most corporations and replaced it with the NYC Business Corporation Tax (BCT) under Subchapter 3-A, which is aligned with the post-2015 NY State Article 9-A. GCT is still in effect for: S corporations (NYC does not recognize the federal or NY state S election for purposes of the NYC corporate tax — S corps are taxed at the entity level under GCT); Insurance corporations and certain other excluded categories.  _(NYC Administrative Code Title 11, Chapter 6, Subchapter 2; NYC Local Law 60 of 2015)_
- **GCT rate** — 8.85% percent of entire net income allocated to NYC  _(NYC Administrative Code Title 11, Chapter 6, Subchapter 2)_

So a federal S-corporation operating in NYC will pay NYC GCT at the entity level despite its pass-through status for federal and NY State purposes. This is a significant trap for S-corp founders moving to or operating in NYC — the NYC-level entity tax can eliminate much of the federal SE-tax savings that motivated the S-corp election in the first place. Always model NYC GCT before recommending an S-corp election to a NYC-resident client. See `us-s-corp-election-decision.md`.

### 6.3 NYC Business Corporation Tax (BCT)

- **BCT base rate** — 8.85% percent of entire net income allocated to NYC
- **BCT structure** — For C-corporations operating in NYC, the BCT applies. There is also a capital base and a fixed-dollar minimum, analogous to the NY State Article 9-A structure.

### 6.4 NYC Commercial Rent Tax (CRT)

- **CRT rate** — 6% (effectively 3.9% after credits and the 35% reduction)
- **CRT applicability threshold** — Applies to commercial tenants in Manhattan south of 96th Street paying more than $250,000 in base rent per year.

This is not formation-relevant but reviewers should be aware that a new NYC entity signing a Manhattan lease may walk into a CRT obligation.

### 6.5 BID Assessments

- **BID assessment rate and applicability** — Many NYC neighborhoods are within a Business Improvement District (BID), and properties within the BID pay an annual BID assessment of approximately 1% of assessed property value. This is technically a property assessment, not an entity tax, but is sometimes characterized colloquially as a "BID tax." For most freelance-developer-sized clients, BID assessments are paid by the landlord (and may be passed through in the lease's additional-rent provisions) rather than directly by the tenant entity. Reviewers do not typically file BID-related forms.

### 6.6 NYC Personal Property — Important Distinction

- **No NYC tax on tangible personal property** — There is no NYC tax on a business's tangible personal property (no inventory tax, no equipment tax). This contrasts with several other states (e.g., Texas, parts of California) that do tax business personal property. New York's real estate tax does apply to real property only.

## 7. NY Wage Theft Prevention Act Notice

- **Notice requirement on hiring** — Under N.Y. Labor Law §195(1), every employer must provide each new employee, at the time of hiring, with a written notice in English and in the employee's primary language containing: Rate of pay; Allowances claimed as part of the minimum wage; The regular pay day designated by the employer; The name of the employer (including any "doing business as" names); The physical address of the employer's main office or principal place of business; The telephone number of the employer. The notice must be signed by the employee and retained for six years.  _(N.Y. Labor Law §195(1))_
- **Penalty for failure** — Failure to provide the notice exposes the employer to civil penalties of up to $50 per workday, with a cap of $5,000 per employee. This is not a formation filing in the DOS sense, but it is the first thing that comes due the moment a newly-formed NY entity hires its first employee, and reviewers should put it on the formation checklist.  _(N.Y. Labor Law §195(1))_

## 8. Beneficial Ownership Information (BOI) / Corporate Transparency Act

The federal Corporate Transparency Act (31 U.S.C. §5336) imposes Beneficial Ownership Information reporting obligations on most LLCs and small corporations formed in any U.S. state, including New York.

**Status as of tax year 2025:** A series of federal court injunctions, FinCEN enforcement notices, and Treasury policy statements during 2024 and 2025 have repeatedly stayed, narrowed, and re-imposed the BOI filing obligation for U.S.-formed entities. As of the date of this skill (2025-11-15), the operative posture is:

- The Treasury / FinCEN interim final rule issued March 2025 limits BOI reporting to foreign reporting companies (i.e., entities formed under the laws of a foreign country that registered to do business in the United States).
- U.S.-formed entities (including NY LLCs and NY corporations) are not currently required to file BOI reports.
- Existing BOI filings submitted before the stay remain on file with FinCEN.

This posture is unstable. Reviewers must check current FinCEN guidance and any subsequent court orders before advising a client that no BOI filing is needed. The default conservative posture in this skill is to flag BOI as a pending item that the reviewer must verify is not currently required at the time of advice.

## 9. Common Errors

### 9.1 Forming an LLC and missing the publication requirement — AUDIT FLASH POINT

- **Common error scenario and cure** — By far the most common NY formation error. A founder files Articles of Organization, gets a confirmation from the DOS, opens a bank account, signs a lease, hires a freelancer — and never publishes. After 120 days, the LLC's authority to transact business is suspended under LLCL §206(a). The founder typically discovers this only when: A counterparty requests a Certificate of Status and the DOS returns a "not in good standing" certificate; The LLC tries to sue someone and the defendant raises §206 as a defense; A bank conducts a periodic KYC review and notices the gap. Cure: complete publication late, file Form DOS-1708 with the affidavits, pay the $50 fee. The cure is treated as restoring the LLC's authority retroactively. Contracts signed during the suspension period are not automatically void but may be subject to challenge. Reviewers seeing a new NY LLC engagement should always ask: "Have you completed publication and filed the Certificate of Publication?" Do not assume.  _(LLCL §206(a))_

### 9.2 NYC vs upstate publication cost mismatch

- **County designation mismatch error** — A founder forms an LLC with a Manhattan address listed in the Articles, then discovers the publication will cost $1,500+. Cannot retroactively change the county of office without amending the Articles (which has its own fee and re-triggers the publication clock). Reviewers should always discuss the county designation before the Articles are filed — once filed, the cheap-option ship has sailed for that formation.

### 9.3 Forgetting the biennial DOS Statement

- **Biennial statement forgotten error** — The $9 biennial Statement is the easiest filing in the entire NY system, but because it only comes around every two years, founders forget. The DOS does not send paper reminders to anyone except the registered agent on file, so if the agent address is stale, the founder never sees the reminder. Past-due status accumulates silently. Reviewers should add the biennial Statement to a recurring calendar reminder.

### 9.4 Confusing the biennial DOS Statement with the annual IT-204-LL

**Biennial Statement vs IT-204-LL comparison**

| Filing | Agency | Frequency | Fee |
| --- | --- | --- | --- |
| Biennial Statement (DOS-1290 / DOS-1357) | NY Department of State | Every 2 years | $9 |
| IT-204-LL Annual Filing Fee | NY Department of Taxation and Finance | Every year | $25 – $4,500 |

Both are required. Filing one does not satisfy the other.

### 9.5 Skipping Form CT-6 for a federal S-corp

- **CT-6 skipped error** — A founder files Form 2553 federally, assumes NY follows, and never files Form CT-6. The entity is then taxed as a NY C-corp at the State level — typically a worse outcome. The CT-6 must be filed within 2½ months of the start of the tax year for which the election is to be effective.

### 9.6 Missing NYC UBT for sole proprietors

- **Missing UBT filing error** — NYC-resident freelancers who file Schedule C frequently miss the NYC-202 filing obligation. UBT is the single most-missed NYC filing for individual operators. See `nyc-ubt.md`.

### 9.7 Picking S-corp form in NYC without modeling NYC GCT

- **S-corp without GCT modeling error** — A founder hears that S-corp saves on self-employment tax, elects S-corp federally, and then discovers that NYC GCT (8.85% at the entity level) wipes out most of the savings. Always model the NYC-level entity tax before recommending an S-corp to a NYC-resident client.

### 9.8 BOI confusion

- **BOI confusion error** — A founder reads a 2024-vintage source that says BOI is required, panics, and either files unnecessarily or pays a service to file. Reviewers should explain the current (as of late 2025) stayed posture and not push the client into unnecessary filings.

## 10. Worked Examples

### Example 1: NYC SaaS Startup ("Ridgeway Labs LLC")

**Facts:** Two technical co-founders form a new SaaS company in Manhattan. Each contributes $50,000 of seed capital. They expect to raise institutional capital in 12 months and have been told by potential investors that a Delaware C-corp is preferred for the priced round, but they need to operate now under some entity.

**Recommendation:**

The textbook investor-track answer is Delaware C-corp from day one so that the founders do not have to pay to convert the entity later. But the cost-benefit of forming in NY first and re-domesticating later is sometimes attractive for budget reasons. Walk through both paths with the founders.

If the founders nevertheless decide to form a NY LLC initially:

**NY LLC path cost table**

| Item | Cost |
| --- | --- |
| Articles of Organization filing fee | $200 |
| Manhattan publication (2 newspapers, 6 weeks) | ~$1,500 |
| Certificate of Publication filing fee | $50 |
| Operating Agreement (in-house draft) | $0 |
| Biennial Statement (filed in year 2) | $9 |
| IT-204-LL filing fee (year 1, assuming NY gross income $0 – $100,000) | $25 |
| **Year 1 NY formation cost** | **~$1,775** |

The LLC is taxed as a partnership federally and is subject to NYC UBT at 4% if NYC-allocated income exceeds the credit threshold. With early-stage SaaS revenue typically under the $95,000 threshold, UBT is fully credited away in year 1. NYC Commercial Rent Tax: if they sign a Manhattan office lease at a rent above $250,000/year, CRT applies. Most early-stage SaaS clients sublease or co-work below the threshold.

If they instead form a Delaware C-corp that qualifies in NY:

**Delaware C-corp path cost table**

| Item | Cost |
| --- | --- |
| Delaware Certificate of Incorporation | $89 |
| Delaware Annual Franchise Tax (minimum, assumed-par method) | $175 |
| NY Application for Authority (BCL §1304) | $225 |
| NY Biennial Statement (filed in year 2) | $9 |
| NYC BCT minimum (year 1) | $25 |
| Federal Form 1120 prep (assuming a CPA) | engagement-dependent |
| **Year 1 NY formation cost (Delaware path)** | **~$500 + DE annual** |

The Delaware path is dramatically cheaper because the LLC publication requirement does not apply to a NY foreign C-corp (only to NY-domestic LLCs and NY-foreign LLCs — note that NY domestic C-corps and foreign C-corps both escape it). This is one of the legitimate reasons NYC tech founders default to Delaware C-corp formation.

**Reviewer's flash points for this client:**

- LLC publication requirement — mark calendar for 120-day deadline
- Confirm Form CT-6 will not be needed (LLC will not elect S unless converted later)
- Confirm NYC UBT filing for year 1 even if at credit threshold (filing is required)
- Discuss Delaware C-corp conversion path before institutional round

### Example 2: Manhattan Real Estate LLC ("215 East 73rd Holdings LLC")

**Facts:** An individual investor forms a single-member LLC to hold one Manhattan rental brownstone. The property generates ~$180,000 of gross rents and $40,000 of net operating income after debt service. The LLC will hold no other assets.

**Recommendation:**

Single-member LLC is appropriate. Real estate holding LLCs are the classic use case. The LLC is disregarded for federal tax purposes; rental activity flows to the individual's Schedule E.

**NY-specific items cost table**

| Item | Cost |
| --- | --- |
| Articles of Organization | $200 |
| Manhattan publication | ~$1,500 |
| Certificate of Publication | $50 |
| Biennial Statement | $9 |
| IT-204-LL (NY-source gross income ~$180,000, bracket fee) | $50 |

- **Real estate UBT exclusion** — Rental income is generally not subject to NYC UBT under NYC Admin Code §11-502(b) because the operation of real property is excluded from UBT if the property is the sole or principal income source of the unincorporated entity. Always confirm this exclusion still applies to the specific facts. If the LLC's activity rises to a "real estate brokerage" or active dealer-in-real-property level, UBT is no longer excluded.  _(NYC Admin Code §11-502(b))_

The LLC will receive NYC real property tax bills as the legal owner — these are not entity formation items but should be on the client's radar. No federal entity-level tax because disregarded. The individual reports on Schedule E.

**Reviewer's flash points:**

- Confirm the UBT real estate exclusion applies on the specific facts
- Confirm a NY Transfer Tax was paid on acquisition (TP-584) — this is an acquisition-time item but reviewers often inherit clients post-acquisition and need to confirm
- Confirm publication was completed — many real estate LLCs are formed by transactional counsel and the publication is sometimes outsourced separately

### Example 3: Brooklyn Restaurant ("Greenpoint Pierogi LLC")

**Facts:** A restaurateur forms a single-member LLC to own and operate a sit-down restaurant in Greenpoint, Brooklyn. The LLC will have an actual storefront, will hire 8 employees, will hold a liquor license, and will gross ~$1.2M in year 1.

**Recommendation:**

Single-member LLC is appropriate; could also consider C-corp form for liability and equity-raise reasons, but LLC is the default for owner-operated restaurants of this scale.

**NY-specific items cost table**

| Item | Cost |
| --- | --- |
| Articles of Organization | $200 |
| Kings County publication | ~$1,200 |
| Certificate of Publication | $50 |
| Biennial Statement | $9 |
| IT-204-LL (NY-source gross income ~$1.2M, bracket fee) | $1,500 |
| **Year 1 NY formation cost** | **~$2,959** |

**NYC overlays:**

- NYC UBT applies — restaurant operations are not subject to the real estate exclusion. With $1.2M of gross revenue and likely UBT taxable income above $150,000, the 4% UBT is fully applicable. Plan for material UBT liability.
- NY Sales Tax registration is mandatory before opening (food and beverages are taxable). See `ny-sales-tax.md`.
- Workers' Compensation insurance is required from the first employee. NY is a strict state — coverage gaps trigger steep penalties.
- NY Wage Theft Prevention Act notice must be issued to each of the 8 employees on hiring.
- NYC Liquor License is administered by the NY State Liquor Authority for on-premises consumption; expect a 4-6 month review.

**Reviewer's flash points:**

- Publication deadline — Kings County rates are not as bad as Manhattan but still material
- UBT will be a real number every year — plan for quarterly estimated UBT payments
- IT-204-LL filing fee is at the high bracket — confirm the client understands this is owed even with zero net profit
- Sales tax registration before opening

### Example 4: Multi-State Company with NY Presence ("Halberd Software Inc.")

**Facts:** A Delaware C-corp software company is headquartered in Austin, Texas, with engineering in Bangalore, and is opening a 5-person sales office in Midtown Manhattan. The company is not forming a new NY entity but is "doing business" in NY.

**Recommendation:**

The Delaware C-corp does not form a new NY entity. Instead it files an Application for Authority under BCL §1304, paying $225 to the NY DOS. This qualifies it as a "foreign corporation" authorized to do business in NY.

**Foreign C-corps escape publication.** This is critical. Foreign LLCs must publish under LLCL §802; foreign corporations do not. So a Delaware C-corp qualifying in NY pays $225 and is done with the DOS side.

**NY tax overlays once doing business in NY:**

- NY State Article 9-A franchise tax (apportioned to NY)
- NYC Business Corporation Tax (apportioned to NYC)
- NY State and NYC employer registration for the 5 sales employees
- NY State and NYC withholding for the 5 sales employees
- NYC Commercial Rent Tax if the Manhattan lease base rent exceeds $250,000/year
- Sales tax registration if it sells taxable products into NY (most pure SaaS sales to business customers are non-taxable; consumer SaaS may be taxable — see `ny-sales-tax.md`)

**Reviewer's flash points:**

- Foreign qualification often missed by out-of-state companies that "just open an office" without paperwork. NY can assess back franchise tax and impose penalties for the gap period.
- NYC BCT applies to the Manhattan presence regardless of headquarters location
- Article 9-A apportionment for software companies uses single-receipts-factor apportionment under post-2015 reform — most software receipts from NY-located customers will apportion to NY
- Federal Form 1120 and Form 1120 supporting state schedules will need NY add-back / decoupling adjustments (e.g., NY does not allow the full federal deduction for state and local taxes in computing NY entire net income)

## 11. Reviewer Checklist

Before finalizing any NY formation engagement, confirm:

1. ☐ Entity type (LLC vs C-corp vs S-corp) modeled against NYC overlays where applicable
2. ☐ County of office selected with publication-cost awareness
3. ☐ Articles of Organization or Certificate of Incorporation filed and confirmation in client file
4. ☐ Operating Agreement (LLC) or Bylaws and initial board consent (corp) executed and dated within 90 days
5. ☐ Publication completed (LLC only) within 120 days and Certificate of Publication filed
6. ☐ Form CT-6 filed if NY S-corp treatment is desired (within 2½ months)
7. ☐ IT-204-LL filing fee budgeted and tracked annually
8. ☐ Biennial Statement calendared for 24-month anniversary
9. ☐ NYC UBT filing status confirmed for individual operators and partnership/LLC operators in NYC
10. ☐ NY Wage Theft Prevention Act notices issued to all new hires
11. ☐ Workers' Compensation, NY State Unemployment Insurance, NY State Disability Benefits registrations completed before first hire
12. ☐ BOI / CTA status checked against current FinCEN posture at the date of advice
13. ☐ Sales tax registration (if applicable) completed before first taxable sale
14. ☐ MTA Surcharge applicability assessed if entity operates in the Metropolitan Commuter Transportation District

## 12. Citation Discipline

Statutory citations in this skill should be presented to reviewers in their full form on first use within the deliverable, then abbreviated. Always include the section, not just the chapter. Example:

- First use: "N.Y. Limited Liability Company Law §206(a)"
- Subsequent: "LLCL §206(a)"

Do not cite secondary sources (treatises, blog posts, online formation services) as authority in deliverables; if a secondary source clarifies a procedural point, the underlying statute or DOS guidance should be cited directly. Cross-references to companion skills (`ny-llc-filing-fee.md`, `nyc-ubt.md`, etc.) are appropriate as workflow pointers but should not substitute for statutory citation when stating a legal rule.

## 13. Refusal Catalogue

- **R-NY-FORM-1** — Forming or qualifying an entity for the purpose of evading NY State or NYC tax with no bona fide business activity at the formation address  _(R-NY-FORM-1)_
- **R-NY-FORM-2** — Advice on whether a specific business activity does or does not constitute "doing business" in NY for nexus purposes without a fact-specific analysis by a credentialed reviewer  _(R-NY-FORM-2)_
- **R-NY-FORM-3** — Advice on professional licensing requirements for PCs, PLLCs, and licensed professionals (this requires NY Education Law expertise outside the scope of this skill)  _(R-NY-FORM-3)_
- **R-NY-FORM-4** — Advice on whether a specific revenue stream is or is not subject to NYC UBT without a fact-specific UBT analysis (defer to `nyc-ubt.md` and a credentialed reviewer)  _(R-NY-FORM-4)_
- **R-NY-FORM-5** — Re-domestication, conversion, and merger transactions (LLC-to-corp conversion, NY-to-DE re-domestication) — these are transactional matters requiring legal counsel  _(R-NY-FORM-5)_
- **R-NY-FORM-6** — Securities-law and Blue Sky advice incident to issuing equity in a newly-formed NY entity  _(R-NY-FORM-6)_
- **R-NY-FORM-7** — Advice that recommends ignoring the LLC publication requirement on the theory that "no one enforces it"  _(R-NY-FORM-7)_

Every output produced under this skill must be reviewed and signed off by a credentialed reviewer (NY-admitted attorney, CPA, or Enrolled Agent operating within Circular 230 scope where federal items intersect) before reaching the client or being acted upon.

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
