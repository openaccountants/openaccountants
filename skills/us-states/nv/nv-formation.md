---
name: nv-formation
description: Tier 2 Nevada content skill for entity formation covering tax year 2025. Includes the NV LLC $75 filing fee + $150 Initial List of Managers + $200 State Business License (first-year total $425), no state PIT, no corporate income tax (only Commerce Tax over $4M), charging-order asset protection, Domestic Asset Protection Trust (DAPT) availability, Series LLC permitted, and authorized-shares structure for NV C-Corp franchise calculation.
jurisdiction: US-NV
domain: state-tax
tax_year: 2025
tier: 2
last_updated: 2026-07-06
---

# nv-formation

## Nevada Entity Formation Skill

## 1. Scope

This skill covers the formation of Nevada (NV) domestic entities — LLCs, C-corporations, and to a lesser extent limited partnerships — for tax year 2025. It is a Tier 2 content skill and assumes the orchestrating workflow has already determined that Nevada is the jurisdiction of formation (typically because the founder is a Nevada resident, holds Nevada situs assets, or has affirmatively chosen Nevada for its asset-protection statutes or its absence of a state-level personal income tax).

The skill covers:

- The mechanics of filing Articles of Organization (LLC) and Articles of Incorporation (corporation) with the Nevada Secretary of State under NRS Chapters 86 and 78 respectively.
- The Initial List of Managers/Members/Officers required under NRS 86.263 (LLCs) and NRS 78.150 (corporations) at the time of formation and again annually thereafter.
- The Nevada State Business License required under NRS 76.100 (the $200-per-year license that catches almost every accountant by surprise the first time).
- The authorized-shares structure used by Nevada to size the C-corporation filing and annual fees (NRS 78.760).
- Nevada's charging-order protection regime for LLC members (NRS 86.401) and the statutory exclusivity of the charging order as a remedy.
- The Nevada Domestic Asset Protection Trust (DAPT) regime under NRS Chapter 166 (the Nevada Spendthrift Trust Act), including the two-year seasoning period and Nevada's position as one of the strongest DAPT jurisdictions in the United States.
- Series LLC permission under NRS 86.1255 and the practical drafting considerations.
- The comparison between Nevada, Wyoming (WY), and Delaware (DE) for founder choice-of-state purposes.
- Foreign qualification when the Nevada entity will operate outside Nevada.
- Worked examples covering high-net-worth asset protection, real-estate holding, and crypto / digital asset structures.

The skill does NOT cover:

- The Nevada Commerce Tax itself (see `nv-commerce-tax.md` and `nv-commerce-and-mbt.md` for the $4,000,000 gross-receipts-threshold tax).
- The Nevada Modified Business Tax (payroll-based — see `nv-commerce-and-mbt.md`).
- Nevada sales and use tax (see `nv-sales-tax.md`).
- Federal tax classification (check-the-box, S-election, partnership). Federal classification is handled by `us-s-corp-election-decision.md`, `us-sole-prop-bookkeeping.md`, and the federal return assembly skill.
- Estate tax planning beyond the DAPT overview. Estate-tax-driven structures should be referred to qualified estate counsel.
- Securities-law issues for capital raises, employee equity, or VC financings. For VC-backed structures Delaware is almost always the right answer regardless of founder residency — this skill notes that consistently.
- Gaming, marijuana, mining, banking, insurance, or other regulated-industry licensing. Nevada's gaming regime in particular has bespoke entity rules well outside scope.

This skill MUST be loaded alongside `us-tax-workflow-base v0.2` or later for the structured intake form, conservative-defaults principle, and reviewer-oriented output spec.

## 2. Why Nevada

Nevada is one of the three "founder states" routinely considered by sole proprietors, single-member LLC owners, and small C-corp founders when they decide where to incorporate. The other two are Wyoming and Delaware. Nevada's value proposition has three pillars:

### 2.1 No state personal income tax

- **No state personal income tax** — Nevada imposes no state-level personal income tax on individuals; the state has no PIT statute. For a sole proprietor or single-member LLC owner whose LLC is disregarded for federal purposes, the income flows to the federal Form 1040 and there is no state return to file.  _(Nevada Constitution Article 10 §1)_
- **No-PIT peer states** — Nevada shares the no-PIT posture with Wyoming, Texas, Florida, South Dakota, Tennessee, Washington (with some narrow exceptions for capital gains in WA), and a handful of other no-PIT states.
- **NV formation does not relocate CA tax residency** — This only benefits a NV-resident owner. If the owner is a California resident who forms a Nevada LLC, California will tax the LLC's income on the owner's California return under R&TC §17041 (resident worldwide income) and will also assert nexus over the Nevada LLC if it does business in California, triggering the $800 California franchise tax and CA Form 568. Forming in Nevada does NOT relocate the owner's personal tax residence. This is a routine error and AUDIT FLASH POINT — see Section 11.  _(R&TC §17041)_

### 2.2 No state corporate income tax

- **No corporate net-income tax; components of NV C-corp cost** — Nevada imposes no corporate net-income tax. A Nevada C-corporation pays: Federal corporate income tax under IRC §11 (currently 21% flat); Nevada Commerce Tax — but ONLY if Nevada gross receipts exceed $4,000,000 (NRS 363C.200), below which the entity files a zero-Commerce-Tax return and owes nothing; Nevada Modified Business Tax (MBT) on wages above the quarterly threshold — irrelevant if the entity has no Nevada employees; the annual State Business License ($200/year — Section 3.3); the annual list fee ($150/year — Section 3.2). There is no franchise tax in the Delaware sense (Delaware corporations pay a franchise tax tied to authorized shares or assumed par value — Nevada's annual list fee is a flat $150 regardless of share count, which is materially friendlier for capitalized startups).  _(NRS 363C.200; IRC §11)_

### 2.3 Asset protection

- **Three pillars of NV asset protection** — Nevada has positioned itself, alongside South Dakota and Alaska, as one of the strongest asset-protection jurisdictions in the United States. The three pillars of NV asset protection are: 1) Charging-order exclusivity for LLC members (NRS 86.401) — a judgment creditor of a Nevada LLC member can obtain a charging order against the member's distributional interest but cannot foreclose on the membership interest, cannot force a sale, cannot vote the interest, and cannot reach LLC assets. Nevada amended NRS 86.401 to clarify that the charging order is the sole and exclusive remedy, meaningfully stronger than the default RULLCA position. 2) Domestic Asset Protection Trust (DAPT) availability under NRS Chapter 166 — Nevada allows a settlor to establish a self-settled spendthrift trust (settlor also a discretionary beneficiary), and after a two-year seasoning period, future creditors are barred from reaching trust assets — one of the most favorable DAPT statutes in the country. 3) No exception creditors — unlike some DAPT states (e.g., Delaware, exceptions for alimony, child support, and pre-existing tort creditors), Nevada has NO statutory exception creditor categories. Once the two-year period has run, the only attack vector is a fraudulent-transfer claim under the Uniform Voidable Transactions Act as adopted by Nevada (NRS Chapter 112). The combination of charging-order exclusivity, DAPT availability, and the absence of exception creditors makes Nevada the preferred jurisdiction for high-net-worth asset protection planning — particularly for clients whose primary concerns are professional liability (physicians, executives, real-estate operators) or contingent litigation exposure rather than spousal/family creditor exposure.  _(NRS 86.401; NRS Chapter 166; NRS Chapter 112)_

### 2.4 Privacy

- **Privacy of LLC members** — Nevada does not require the public disclosure of LLC members on the Articles of Organization. The Initial List and Annual List do require the disclosure of managers (or member-managers), but if the LLC is manager-managed and the manager is a separate Nevada entity or a non-member individual, the underlying members remain off the public record. This is comparable to Wyoming and stronger than Delaware (where the registered agent must maintain a record but the state itself collects very little). Privacy is NOT confidentiality from the IRS, from a litigation subpoena, or from a properly issued discovery request. Privacy is a public-records protection, not a litigation shield.

## 3. Nevada LLC Formation

### 3.1 Articles of Organization — $75

- **Articles of Organization filing fee** — $75  _(NRS 86.151)_
- **Articles of Organization required contents** — The Articles must include: the name of the LLC, which must contain "Limited-Liability Company," "Limited Company," "Limited," "LLC," "L.L.C.," "LC," or "L.C." and be distinguishable on the records of the Secretary of State (NRS 86.171); the name and street address of the Nevada registered agent, who must be a Nevada resident individual or a commercial registered agent authorized to do business in Nevada (NRS 77.310) — a P.O. Box is not sufficient; a statement of whether the LLC is member-managed or manager-managed; the name and address of each manager (if manager-managed) or each managing member (if member-managed), which duplicates information also on the Initial List (Section 3.2); the duration of the LLC (perpetual by default); the name and address of each organizer; an optional statement of professional purpose if the LLC is a Professional LLC under NRS 89.  _(NRS 86.171; NRS 77.310; NRS 89)_
- **Filing method and expedited service** — Filing is done online via SilverFlume (the Nevada Business Portal at nvsilverflume.gov) or by mail. Online filings are typically processed within 1–2 business days; expedited service is available for additional fees ($125 for 24-hour, $500 for 2-hour, $1,000 for 1-hour).

### 3.2 Initial List of Managers/Members — $150

- **Initial List of Managers or Managing Members filing fee** — $150  _(NRS 86.263)_
- **Initial List due date and content** — The Initial List is due by the last day of the month following the month in which the Articles were filed. For example, Articles filed on March 15 require the Initial List by April 30. In practice, Nevada SilverFlume bundles the Articles and the Initial List together so the founder pays both fees at the same time at formation. The Initial List must disclose, for each manager (or managing member), the name and street address. The registered agent's address is generally not acceptable for the manager's address — Nevada wants the actual manager's address. A P.O. Box is not acceptable.  _(NRS 86.263)_
- **AUDIT FLASH POINT — Initial List deadline** — Missing the Initial List deadline results in the LLC being marked "Default" on the Secretary of State's records. Continued default for one year triggers administrative revocation under NRS 86.272. Reinstatement requires payment of all delinquent fees, penalties of $75 per default year (NRS 86.276), and a reinstatement fee. The cleanest path is to file the Initial List concurrently with the Articles at formation, eliminating the deadline-tracking risk.  _(NRS 86.272; NRS 86.276)_

### 3.3 State Business License — $200/year

- **Nevada State Business License fee for LLCs and corporations** — $200/year  _(NRS Chapter 76)_
- **State Business License applicability and other entity fees** — Under NRS Chapter 76, every entity doing business in Nevada — including a Nevada LLC, even one with no Nevada operations — must hold a Nevada State Business License. The fee is $200/year for LLCs (and corporations); sole proprietors pay $200 and the few entities organized as nonprofits pay $0.  _(NRS Chapter 76)_
- **Renewal bundling and local license distinction** — The State Business License is renewed annually at the same time as the Annual List. SilverFlume bundles the renewal so the founder pays $150 (Annual List) + $200 (State Business License) = $350/year going forward. The State Business License is NOT the same as a local business license. Las Vegas, Reno, Henderson, Sparks, Carson City, and Clark/Washoe counties each have their own local business license regimes for businesses with physical presence in those jurisdictions. A Nevada LLC formed for asset-protection purposes that has no Nevada business activity still owes the State Business License but typically does not owe any local license.
- **AUDIT FLASH POINT — Forgetting the State Business License** — This is the single most common Nevada formation mistake. Founders pay the $75 Articles fee, pay the $150 Initial List fee, see their LLC marked active on the state's records, and assume they are done. The $200 State Business License is a separate line item that must be paid AT FORMATION (not as part of the Articles or Initial List) and again annually. Failure to obtain the State Business License is a misdemeanor under NRS 76.150 and triggers a $100 per-month late fee (capped at $100 — but the $200 base license still accrues each year). On reinstatement Nevada will demand the back license fees, the $100 late penalty, and a reinstatement fee.  _(NRS 76.150)_

### 3.4 First-year cost summary

**First-year cost summary (LLC)**  _(NRS 86.151; NRS 86.263; NRS 76.100)_

| Item | Statute | Fee |
| --- | --- | --- |
| Articles of Organization | NRS 86.151 | $75 |
| Initial List of Managers/Members | NRS 86.263 | $150 |
| Nevada State Business License | NRS 76.100 | $200 |
| **First-year total (Nevada-only)** |  | **$425** |

Items not included in the table that often add to the real first-year cost: registered agent fee — commercial registered agents charge $50–$300/year, required if no Nevada-resident individual is willing to serve; formation attorney or service company — $0 to $2,000+ depending on whether the founder DIYs via SilverFlume or hires counsel; operating agreement drafting — $0 (template) to $5,000+ (multi-member with capital and distribution waterfalls); EIN application — $0 if filed via IRS Form SS-4 online by an individual with an SSN; otherwise foreign-individual applications take 4–6 weeks by fax; foreign qualification in the state where the LLC actually operates (if not Nevada) — see Section 9; the first-year cost of the foreign qualification's home-state filing — often higher than the Nevada fees themselves.

### 3.5 Subsequent annual cost

**Subsequent annual cost (LLC)**

| Item | Fee |
| --- | --- |
| Annual List of Managers/Members | $150 |
| State Business License renewal | $200 |
| **Annual total (Nevada-only)** | **$350** |

- **Annual due date and late penalties** — The Annual List and State Business License are due by the last day of the anniversary month of formation. Late filing triggers a $75 penalty on the Annual List (NRS 86.272) plus a $100 penalty on the License (NRS 76.130).  _(NRS 86.272; NRS 76.130)_

## 4. Nevada C-Corporation Formation

### 4.1 Articles of Incorporation — $75 base + authorized-shares premium

- **Articles of Incorporation base filing fee** — $75  _(NRS 78.030)_

**Nevada authorized-shares fee schedule (NRS 78.760, tax year 2025)**  _(NRS 78.760)_

| Authorized shares (or aggregate par value $) | Filing fee |
| --- | --- |
| Up to 75,000 shares (or par value up to $75,000) | $75 |
| 75,001 – 200,000 shares | $175 |
| 200,001 – 500,000 shares | $275 |
| 500,001 – 1,000,000 shares | $375 |
| Each additional 1,000,000 shares (or fraction thereof) above 1,000,000 | +$375 |
| Maximum filing fee | $35,000 |

The simplest founder structure — a single-class corporation with 10,000,000 authorized shares of common stock at $0.0001 par value (typical for a startup intended to receive seed financing) — would owe approximately $375 + ($375 × 9) = $3,750 at filing under the additional-million-share tier. That is a meaningful number compared to Wyoming's flat $100 filing or Delaware's franchise-tax-based regime.

**Heuristic:** if the founder is forming a single-shareholder C-corp purely for personal-services income (rare — almost always an S-election or sole prop is better — see `us-s-corp-election-decision.md`), authorize 75,000 shares and pay the $75 fee. If the founder anticipates outside investment, the right answer is almost always Delaware (see Section 8), not Nevada.

- **Articles of Incorporation required contents** — The Articles of Incorporation must include: corporate name with "Incorporated," "Corporation," "Company," "Limited," "Corp.," "Inc.," "Co.," or "Ltd." (NRS 78.035); registered agent name and Nevada street address; authorized capital structure — classes of stock, number of shares per class, par value (or "no par"), preferences/rights/limitations; name and address of each director (NRS 78.030(1)(d)) and each incorporator; optional purpose clause (general "any lawful business" is the default and usually sufficient); indemnification and limitation-of-liability provisions are optional but routine.  _(NRS 78.035; NRS 78.030(1)(d))_

### 4.2 Initial List of Officers and Directors — $150

- **Initial List of Officers/Directors** — $150
- **Initial List content and sole-officer structure** — Under NRS 78.150 the corporation must file an Initial List of Officers, Directors, and the Registered Agent at the time of incorporation. The Initial List must identify the President, Secretary, Treasurer, and all directors by name and street address. A Nevada corporation can be formed with a single person serving as the sole officer and sole director (NRS 78.115). This is the standard solo-founder structure.  _(NRS 78.150; NRS 78.115)_

### 4.3 State Business License — $200/year

- **State Business License for corporations** — $200/year

Same $200/year State Business License applies as for an LLC (Section 3.3). No corporation-specific carve-out.

### 4.4 First-year C-corp cost summary (75,000-share founder structure)

**First-year C-corp cost summary**

| Item | Fee |
| --- | --- |
| Articles of Incorporation (≤75,000 shares) | $75 |
| Initial List of Officers/Directors | $150 |
| State Business License | $200 |
| **First-year total** | **$425** |

For a higher-share-count structure (e.g., 10,000,000 shares for a future-fundraising entity), the Articles fee climbs to $3,750 and the first-year total to $4,100 — at which point Delaware's flat $109 incorporation fee plus $400-ish annual franchise tax under the Assumed Par Value method starts to look very attractive.

### 4.5 Subsequent annual cost

- **Subsequent annual cost (C-corp)** — Annual List of Officers/Directors: $150 (flat, regardless of share count). State Business License renewal: $200. Annual total: $350. Note: Nevada's annual list fee does NOT scale with authorized shares — the share count only matters at formation and at amendment (e.g., a recapitalization that increases authorized shares triggers a fresh look at the Section 78.760 schedule and a fee for the increment). This is a meaningful structural difference from Delaware, where the franchise tax can range from $400 to $200,000+ per year depending on share count and the chosen calculation method.  _(NRS 78.760)_

## 5. Charging-Order Protection (NRS 86.401)

### 5.1 The statutory rule

- **Charging order mechanics and exclusivity** — Under NRS 86.401(1), a judgment creditor of a member of a Nevada LLC may apply to a court of competent jurisdiction for a charging order against the member's interest. Subsections (2) and (3) make clear: the charging order constitutes a lien on the judgment debtor's transferable interest in the LLC; the charging order only entitles the creditor to receive distributions that would otherwise have been made to the debtor-member; the charging order does NOT entitle the creditor to participate in management, to vote the interest, to inspect books and records, or to force a dissolution of the LLC. NRS 86.401(2)(a) explicitly states that the charging order is the sole and exclusive remedy of the judgment creditor against the member's interest. This statutory exclusivity was clarified by the Nevada Legislature to forestall judicial creativity — in some other states courts have allowed creditors to "foreclose" on the charging order and effectively force a sale of the membership interest. Nevada has closed that door by statute.  _(NRS 86.401)_

### 5.2 Practical effect

- **Single-member LLC protection vs Olmstead** — For a single-member LLC the charging-order protection has historically been thinner — the leading case is Olmstead v. FTC, 44 So.3d 76 (Fla. 2010), in which the Florida Supreme Court allowed a creditor to seize a Florida single-member LLC interest because the policy rationale for charging-order protection (protecting non-debtor members from being saddled with an unwanted business partner) does not apply where there are no non-debtor members. Nevada responded by statutorily preserving charging-order exclusivity even for single-member LLCs — NRS 86.401(2)(a) makes no distinction between single-member and multi-member LLCs. This is one of Nevada's edges over Florida and a few other states for single-member-LLC asset protection. It is comparable to Wyoming (Wyo. Stat. §17-29-503) and stronger than Delaware (which protects the charging order as an exclusive remedy but has more open issues around single-member treatment).  _(NRS 86.401(2)(a); Olmstead v. FTC, 44 So.3d 76 (Fla. 2010); Wyo. Stat. §17-29-503)_

### 5.3 What charging-order protection does NOT do

- **Limits of charging-order protection** — It does NOT protect the LLC's assets from the LLC's own creditors. A judgment against the LLC itself can be enforced against LLC assets. It does NOT protect from veil-piercing — a court can disregard the LLC's separateness if the member has used the LLC as an alter ego, has commingled funds, has failed to observe formalities, or has used the LLC to commit fraud. It does NOT protect from fraudulent-transfer claims — a transfer of personal assets into the LLC after a creditor's claim has arisen — or in anticipation of a foreseeable claim — can be unwound under NRS 112.180 (UVTA). It does NOT protect from federal tax liens — the IRS can levy on an LLC interest regardless of state-law charging-order rules.  _(NRS 112.180)_

### 5.4 Drafting considerations

- **Maximizing charging-order protection** — To maximize charging-order protection: the operating agreement should expressly invoke NRS 86.401 and recite the charging-order remedy as exclusive; the operating agreement should give the manager (or a non-debtor majority of members) discretion over whether to make distributions — a creditor with a charging order who cannot force distributions has, in practice, a worthless lien, often called the "K-1 problem" because the creditor may be allocated phantom income on a Schedule K-1 without receiving cash to pay tax on it (though the Tax Court's position in Rev. Rul. 77-137 on charging-order phantom income is debated); the operating agreement should include transfer restrictions and a right of first refusal to prevent the membership interest from passing freely to a creditor or assignee; capital contributions and distributions should follow the operating agreement strictly — sloppy execution invites veil-piercing.  _(NRS 86.401; Rev. Rul. 77-137)_

## 6. Nevada Domestic Asset Protection Trust (DAPT) — NRS Chapter 166

### 6.1 The Nevada Spendthrift Trust Act

- **Nevada Spendthrift Trust Act and two-year bar** — Nevada was an early adopter of the self-settled spendthrift trust (the technical term for what marketing materials call a "Domestic Asset Protection Trust" or DAPT). The Nevada Spendthrift Trust Act, codified at NRS Chapter 166, permits a settlor to establish an irrevocable trust naming himself or herself as a discretionary beneficiary, and — after a two-year seasoning period — to defeat future creditor claims against the trust assets. The cornerstone provision is NRS 166.170(1): a creditor's claim against trust assets is barred unless the action is brought within two years after the transfer to the trust (or six months after the creditor discovered or reasonably should have discovered the transfer, whichever is later, but in no event later than two years from the transfer).  _(NRS 166.170(1))_

### 6.2 Statutory requirements

- **NV spendthrift trust qualification requirements** — To qualify as a Nevada spendthrift trust under NRS 166.015 the trust must: be irrevocable — the settlor cannot retain the power to revoke the trust or to amend it in a way that defeats the spendthrift protection (limited powers, e.g., to remove and replace a non-settlor trustee, to change administrative provisions, are permitted); have at least one Nevada trustee — either a Nevada-resident individual, a Nevada-chartered trust company, or a federally chartered institution with a Nevada office authorized to act as trustee; include an express spendthrift clause restraining voluntary and involuntary alienation of the beneficiary's interest; the Nevada trustee must maintain custody of at least some of the trust's records in Nevada and must conduct at least part of the trust's administration in Nevada.  _(NRS 166.015)_

### 6.3 Settlor's permitted retained powers

- **Permitted retained powers under NRS 166.040** — Under NRS 166.040 the settlor may retain (without defeating the asset-protection structure): the power to direct trust investments; the power to veto trust distributions; a testamentary special power of appointment; the right to receive distributions of income, principal, or both, but only in the trustee's discretion (mandatory distributions are not permitted — distributions must be at the trustee's sole, absolute, and uncontrolled discretion or pursuant to an ascertainable standard); the right to use real estate held by the trust (e.g., a personal residence) as long as the use is consistent with the trust's terms; the right to remove the trustee and appoint a successor (subject to limits — the successor cannot be the settlor or someone related/subordinate within the meaning of IRC §672(c) if the settlor wants to avoid grantor-trust traps that would also gut the asset protection).  _(NRS 166.040; IRC §672(c))_

### 6.4 No exception creditors

- **Nevada has no statutory exception creditor categories** — Nevada has no statutory exception creditor categories. This is the single feature that distinguishes Nevada from most other DAPT states: Delaware has exceptions for child support, alimony, and pre-existing tort creditors (12 Del. C. §3573); Alaska has exceptions for child support arrearages and any creditor whose claim arose from the settlor's commission of an intentional tort; South Dakota has exceptions for pre-DAPT child support. Nevada has none. After the two-year seasoning period, even a spouse pursuing alimony or child support must satisfy a fraudulent-transfer analysis under NRS 112 — Nevada provides no automatic carve-out. This is one reason Nevada DAPTs are popular with executives and physicians whose primary exposure is professional or commercial liability rather than family-law obligations. It is also why Nevada DAPTs draw heightened scrutiny in cases where a settlor's true motive is divorce planning — a court considering a Nevada DAPT funded shortly before a divorce filing will look hard for fraudulent-transfer indicia.  _(12 Del. C. §3573; NRS 112)_

### 6.5 The two-year seasoning period

- **Two-year clock per transfer** — The two-year period under NRS 166.170 begins to run on the date of each transfer to the trust. Each contribution has its own two-year clock. This is critical: if a settlor funds the trust over time, only the portions held for at least two years enjoy the statutory bar. Practical implication: a DAPT should be funded in a single large transfer at the outset (to start a single clock for the bulk of the assets) rather than dripped in over years (which creates a rolling sequence of clocks and complicates any future creditor analysis).  _(NRS 166.170)_

### 6.6 Fraudulent-transfer analysis

- **UVTA badges of fraud and best practices** — Even after the two-year period, a creditor can attempt to unwind a transfer under the Uniform Voidable Transactions Act (Nevada has adopted the UVTA at NRS Chapter 112). The relevant badges of fraud under NRS 112.180(2): transfer to an insider (the trust may qualify if the settlor is a beneficiary); settlor retained possession or control of the asset after transfer; transfer was concealed; transfer occurred after, or shortly before, a substantial debt was incurred; settlor was insolvent at the time of, or as a result of, the transfer; transfer was for less than reasonably equivalent value; substantially all of the settlor's assets were transferred.  _(NRS 112.180(2))_
- **AUDIT FLASH POINT — DAPT structuring for fraudulent-transfer challenges** — A DAPT funded at a time when the settlor faces foreseeable creditor exposure is exposed to fraudulent-transfer challenge regardless of the two-year period. The two-year period of NRS 166.170 only protects against actions brought more than two years after the transfer — it does NOT cure a transfer that was fraudulent in its inception under NRS 112. Best practice: fund the DAPT when the settlor has no known creditors, no pending litigation, and no foreseeable claims; retain a solvency analysis at the time of funding, prepared by an independent CPA or financial advisor, documenting that the settlor was solvent both before and after the transfer; do not transfer "substantially all" of the settlor's assets — leave meaningful liquid net worth outside the trust to satisfy ordinary creditors; do not treat trust assets as personal pocket money — distributions should be requested in writing and considered by the trustee on the record; document the trust's business purposes (estate planning, generational wealth transfer, professional liability protection in general) as the rationale — not "I'm worried about X creditor."  _(NRS 166.170; NRS 112)_

### 6.7 Federal tax treatment

- **Grantor vs non-grantor DAPT and CA ING/NING attack** — A Nevada DAPT can be structured as either a grantor trust or a non-grantor trust for federal income tax purposes. Most planning is done as a grantor trust — meaning the settlor continues to be taxed on trust income at the individual level (IRC §§671–679), which avoids the compressed trust tax brackets and preserves the ability to use the settlor's personal capital-loss limits, qualified dividends, and §121 home-sale exclusion if a personal residence is in the trust. For a Nevada-resident settlor, grantor trust treatment is the default planning choice. For a high-income California-resident settlor considering a Nevada DAPT to escape California's 13.3% top rate via non-grantor trust treatment, the planning gets significantly more complex and is subject to California's "throwback" and "incomplete gift non-grantor trust" (ING/NING) rules — which California has consistently attacked and which the FTB has issued multiple legal rulings against. ING/NING planning is out of scope here and should be referred to qualified estate counsel familiar with FTB Legal Ruling 2023-02 (the FTB's position that NING trusts are typically disregarded).  _(IRC §§671–679; FTB Legal Ruling 2023-02)_

## 7. Series LLC — NRS 86.1255

Nevada permits the formation of a Series LLC under NRS 86.1255. A Series LLC is a single LLC under which multiple "series" (or "cells") can be established, each with its own: members and managers; assets and liabilities (segregated from other series under NRS 86.1255(2)); business purpose; distribution and allocation rules. The key statutory feature is the inter-series liability shield: if the LLC's operating agreement and records properly segregate the series, the debts and obligations of one series are not enforceable against the assets of another series or against the master LLC.

### 7.1 Practical use

- **Common Series LLC use cases** — The Series LLC is popular in three contexts: 1) Real estate holding — each rental property held in a separate series; a slip-and-fall lawsuit at Property A cannot reach Property B's assets (see Section 10.2). 2) Multi-line investment vehicles — different asset classes (real estate, crypto, private equity, art) held in separate series for liability segregation without the cost of forming a separate LLC per asset class. 3) Family wealth structures — different family members hold beneficial interests in different series of a single master LLC for governance and segregation purposes.

### 7.2 Statutory mechanics

- **Series LLC statutory requirements** — Under NRS 86.1255(1) the master LLC's Articles of Organization must expressly authorize the formation of series and must give notice of the inter-series liability limitations. The operating agreement must: identify each series by name or designation; specify the members, managers, and asset of each series; maintain separate records and accounts for each series; adhere to the segregation strictly — commingling between series destroys the shield.  _(NRS 86.1255(1))_

### 7.3 Caveats

- **Series LLC federal/multistate uncertainties** — Federal tax treatment is unsettled — the IRS has proposed regulations (Prop. Reg. §301.7701-1(a)(5), 2010) treating each series as a separate entity for federal tax purposes, but the regulations have never been finalized; current practice is to treat each series as a separate entity and to file accordingly (separate EINs, separate Schedule Cs or partnership returns, etc.). State recognition outside Nevada is patchy — some states (e.g., California — see California's Form 568 Schedule IW treatment) require each series to register separately, pay the $800 franchise tax separately, and file separate Form 568s; the cost savings of using a Series LLC over separate LLCs can evaporate when the entity operates in multiple states. Foreign qualification is uncertain — some states will not foreign-qualify a single series of an out-of-state Series LLC; the entire master LLC must qualify, which exposes all series to that state's jurisdiction. Bankruptcy treatment is unclear — it is unsettled whether a single series can file bankruptcy without dragging in the master LLC or other series. For the foregoing reasons, the Series LLC is a meaningful planning tool for an asset-protection-focused Nevada-resident holding Nevada-situs assets, but it should be deployed cautiously and only with counsel familiar with the limits of inter-series segregation across state lines.  _(Prop. Reg. §301.7701-1(a)(5))_

## 8. Nevada vs Wyoming vs Delaware

The three founder-state options are frequently compared. The honest answer is that the right state depends on what the founder needs the entity to do.

### 8.1 Comparison table

**Nevada vs Wyoming vs Delaware comparison table**  _(NRS 86.401; Wyo. Stat. §17-29-503; 6 Del. C. §18-703; NRS Ch. 166; 12 Del. C. §3573; NRS 86.1255)_

| Feature | Nevada | Wyoming | Delaware |
| --- | --- | --- | --- |
| State PIT | None | None | Yes (up to 6.6%) |
| Corporate income tax | None (Commerce Tax >$4M only) | None | 8.7% |
| Franchise tax | None for small entities | $60/year minimum | $400+/year (scales w/ shares) |
| LLC filing fee | $75 | $100 | $110 |
| LLC annual fee | $350 (List $150 + License $200) | $60 | $300 |
| C-Corp filing fee | $75 base + share-based | $100 | $109 |
| C-Corp annual cost | $350 | $60 | $400 – $200,000 |
| Charging-order exclusivity | Yes (NRS 86.401) | Yes (Wyo. Stat. §17-29-503) | Yes (6 Del. C. §18-703) |
| Single-member LLC protection | Strong (statute clarifies) | Strong | Less clear (no statute) |
| DAPT permitted | Yes (NRS Ch. 166) | No (until WY 2025 — limited) | Yes (12 Del. C. §3573) |
| DAPT exception creditors | None | N/A | Child support, alimony, tort |
| DAPT seasoning | 2 years | N/A | 4 years |
| Series LLC | Yes (NRS 86.1255) | Yes | Yes |
| Privacy of member identity | High | Highest | Moderate |
| Court system | Generalist | Generalist | Court of Chancery (specialist) |
| Case law depth | Moderate | Limited | Vast |
| VC / institutional acceptance | Low | Very low | Universal |

### 8.2 Choice-of-state heuristics

**Choose Nevada if:**
- The founder is a Nevada resident.
- The primary objective is asset protection, particularly via DAPT.
- The structure involves Nevada-situs assets (Nevada real estate, Nevada-headquartered operations).
- The founder values the absence of DAPT exception creditors.

**Choose Wyoming if:**
- Cost minimization is paramount ($60/year vs Nevada's $350/year matters at the margin).
- The founder values privacy above all else.
- The founder does not need DAPT functionality.
- The entity is a passive holding company with no anticipated litigation exposure.

**Choose Delaware if:**
- The founder anticipates institutional investment (seed, Series A, etc.).
- The entity will be a C-corporation. **DE is the universal VC standard.** A Nevada C-corporation will, at the time of the first institutional financing, be required to redomicile to Delaware — and that redomestication will cost $5,000–$15,000 in legal fees and create taxable boot if not handled carefully. Form in Delaware from day one.
- The entity will have multiple share classes, preferred-stock financings, or complex governance.
- The transaction lawyers and investors are familiar with Delaware General Corporation Law and want the predictability of the Court of Chancery.

**Choose home state (not NV/WY/DE) if:**
- The entity will operate primarily in the founder's home state.
- The founder is in California, New York, Massachusetts, or another high-tax/high-regulation state and the entity will trigger nexus there anyway.
- Foreign qualification fees in the home state will exceed the savings from out-of-state formation.

### 8.3 The "Nevada for a California resident" trap

- **NV formation does not escape CA tax; cost breakdown** — A frequent pattern: a California-resident founder is told (often by a Nevada-based formation service company) that forming in Nevada will let them "escape" California taxes. This is wrong in two ways: 1) California taxes its residents on worldwide income (R&TC §17041) — a California resident who owns a Nevada LLC pays California PIT on the LLC's income regardless of the LLC's state of formation. 2) California asserts nexus over any LLC "doing business" in California — and the bar is low under R&TC §23101 — a Nevada LLC managed from California, holding California-situs assets, or earning California-source income will be required to register as a foreign LLC in California, pay the $800 annual franchise tax, and file Form 568. The Nevada entity ends up paying: Nevada State Business License ($200/year); Nevada Annual List ($150/year); California foreign-qualification filing ($70); California $800 annual franchise tax; California LLC fee on gross receipts (if applicable); California Form 568 filing. A net cost of $1,220+/year and TWO sets of compliance obligations, in exchange for zero tax savings. Forming in California from the start would have been cheaper and simpler.  _(R&TC §17041; R&TC §23101)_
- **AUDIT FLASH POINT — confusing NV residency with NV formation** — Forming a Nevada LLC does not change the owner's personal tax residency. The Nevada formation is meaningful only if the owner is actually a Nevada resident (physical presence, domicile intent, NV driver's license, NV voter registration, NV homestead) — or if the LLC's activities are genuinely Nevada-situs and out-of-state nexus is avoided.

## 9. Foreign Qualification

A Nevada LLC or corporation that "transacts business" outside Nevada must register as a foreign entity in each state where it transacts business. The trigger for foreign qualification varies by state but generally includes: maintaining an office, warehouse, or physical presence; employing residents of the state; holding real property in the state; engaging in regular, repeated transactions with customers in the state.

What does NOT trigger foreign qualification in most states (under "doing business" safe harbors derived from Model Business Corporation Act §15.01(b)): maintaining bank accounts in the state; holding directors' or managers' meetings in the state; engaging in isolated transactions completed within 30 days; owning a passive investment in a foreign entity; defending or settling a lawsuit in the state.

### 9.1 Mechanics

- **Foreign qualification process steps** — To foreign-qualify in another state, the Nevada entity must: 1) Obtain a Certificate of Good Standing (sometimes called a Certificate of Existence) from the Nevada Secretary of State — typically $50 and 1–2 days online via SilverFlume. 2) File an Application for Authority (or equivalent — terminology varies) with the foreign state's Secretary of State, attaching the Nevada Certificate of Good Standing. 3) Designate a registered agent in the foreign state. 4) Pay the foreign-qualification filing fee (ranges from $50 to $750+ depending on state). 5) Comply with annual report / annual franchise tax obligations in the foreign state.

### 9.2 The compounding cost

A Nevada LLC foreign-qualified in California, Texas, and New York pays: Nevada: $350/year (List + License). California: $800/year franchise tax + LLC fee if gross receipts >$250,000. Texas: $0 franchise tax if revenue <$2.47M, but $0–$25 Public Information Report filing. New York: $9 biennial statement + publication requirement of $1,000–$2,000 one-time at qualification. Total annual cost: $1,150 – $5,000+ per year before any tax. For an entity with only modest operations in each state, this is a meaningful overhead. Many founders consolidate to a single home-state formation once they realize the multi-state cost.

### 9.3 Penalties for non-qualification

- **Penalties for transacting business without authority** — Most states impose penalties for transacting business without authority: California: $20/day per day of non-qualification (R&TC §23304), plus inability to maintain a lawsuit in California state court while unqualified. Texas: $750 minimum penalty plus loss of access to Texas courts. New York: $500/year penalty plus loss of access to NY courts. The litigation-access bar is particularly painful: an unqualified foreign LLC cannot file or maintain an action in the state's courts. The LLC can be sued, but cannot sue, until it qualifies and pays back fees and penalties.  _(R&TC §23304)_

## 10. Worked Examples

### 10.1 Example — High-net-worth Nevada-resident asset protection

**Facts.** Dr. Sarah Chen is a Nevada-resident orthopedic surgeon, age 52, married, with two adult children. Her practice generates $1.2 million/year of net income. She owns a primary residence in Henderson (NV) worth $2.5 million, an investment portfolio of $4 million in liquid securities, a small commercial building in Reno worth $800,000 leased to a tenant unrelated to her practice, and $500,000 of crypto held in a hardware wallet. She has no debts other than a $400,000 mortgage on the residence and no current litigation. She is concerned about future medical-malpractice exposure that could exceed her $3 million umbrella + $1 million malpractice policy coverage.

**Structure.**

1. **Personal residence:** Transfer to a Nevada DAPT under NRS 166. The residence is not a high-claim-risk asset on its own, but placing it in the DAPT removes it from the personal balance sheet visible to a future medical-malpractice plaintiff. Two-year clock starts on the date of transfer.
2. **Investment portfolio:** Form a Nevada single-member LLC ("Chen Family Holdings LLC") and contribute the $4 million in securities. Retain Sarah as the sole managing member. Then transfer the membership interest in Chen Family Holdings LLC to the Nevada DAPT. This stacks two layers of protection: charging-order protection on the LLC interest, plus DAPT protection on the underlying interest.
3. **Reno commercial property:** Form a separate Nevada single-member LLC ("Chen Reno Commercial LLC") because the rental activity carries its own tort exposure (tenant slip-and-fall, premises liability). Keep this LLC outside the DAPT — the commercial building's exposure could create exception-creditor pressure on the DAPT if the building's liabilities ever exceeded its assets. Inside-out protection: the LLC shields Sarah personally from claims arising at the property. Outside-in protection: if Sarah is sued personally for malpractice, a charging order on her LLC interest is the only remedy and cannot reach the building.
4. **Crypto:** Form a separate Nevada single-member LLC ("Chen Digital Asset LLC"). Move the hardware wallet to the LLC's custody (this is operationally tricky — see Example 10.3). Then transfer the LLC interest to the DAPT.
5. **Medical practice:** Restructure the practice as a Nevada Professional LLC (under NRS 89). Sarah personally remains liable for her own malpractice (that's a non-waivable feature of professional practice), but the practice entity shields her from co-employee acts, contractual exposure, and general business torts. The practice entity itself is not transferred to the DAPT — operating professional revenue should remain in the operating-entity layer.

**Cost.**

- DAPT formation: $5,000 – $15,000 attorney's fees + Nevada trustee setup fee.
- 4 Nevada LLCs (Family Holdings, Reno Commercial, Digital Asset, Professional LLC): 4 × $425 first year = $1,700.
- Recurring: 4 × $350/year = $1,400/year LLC compliance + Nevada trustee fee (typically $3,000–$10,000/year).

**Timeline.** The two-year clock under NRS 166.170 begins running on the date of each contribution. Sarah should fund the DAPT in a single large transfer to start one clock for the bulk of the assets. Any subsequent transfers (e.g., topping up with annual savings) start their own two-year clocks.

**Audit flash points.**
- Solvency at the time of DAPT funding must be documented by an independent CPA.
- The Reno commercial property should NOT be in the DAPT — its operating exposure is incompatible with DAPT protection.
- The professional practice entity should NOT be in the DAPT — Sarah cannot insulate herself from her own malpractice via a self-settled trust, and putting practice operations inside the trust creates IRC §677 grantor-trust issues and licensing problems.

### 10.2 Example — Real-estate holding via Series LLC

**Facts.** Marcus Rivera, Nevada resident, owns five rental single-family homes in the Las Vegas metro area. Combined fair market value $3.2 million, combined annual rental income $200,000. He currently holds all five in his personal name. He is concerned about tort liability (tenant injury) at any one property cascading into a claim against the other four.

**Structure.**

1. **Form a Nevada Series LLC** ("Rivera Real Estate Holdings, LLC") under NRS 86.1255. Articles of Organization expressly authorize series and recite the inter-series liability limitations.
2. **Establish five series** within the master LLC: Series A, B, C, D, E — one per property.
3. **Transfer each property** by quitclaim deed (or warranty deed if a title-insurance requirement) to the applicable series. Recording the deed must reference the specific series, e.g., "Rivera Real Estate Holdings, LLC – Series A."
4. **Maintain separate books** for each series: separate bank account, separate accounting, separate tenant agreements, separate insurance policies (each property's policy should name the applicable series as named insured).
5. **Single federal EIN** at the master-LLC level, or separate EINs per series. Under current IRS guidance the safer position is separate EINs per series since the proposed regulations would treat each series as a separate entity.

**Tax treatment.** Each series is a single-member disregarded entity for federal tax purposes (because Marcus is the sole member of each series). Rental income and expenses flow to Marcus's Schedule E on Form 1040. No separate entity-level federal return.

**Nevada compliance.** One filing: one set of Articles, one Initial List, one State Business License. The master LLC pays $425 at formation and $350/year. The series themselves do not file separate Articles or pay separate fees in Nevada. This is the cost-saving point of the Series LLC structure.

**Limitations.** If any property is sold to a buyer in another state, or if Marcus expands into Arizona, California, or Utah, the Series LLC's inter-series segregation may not be recognized in that other state. Foreign qualification in California, for example, requires registering EACH SERIES as a separate foreign LLC and paying $800/year per series — eliminating the cost savings.

**Audit flash point.** Strict segregation of series accounts is essential. If Marcus deposits rent from Property C into the Series A bank account, even once, a court could find that the inter-series shield has been pierced as to that transaction or as to all transactions. Series segregation is more demanding than ordinary corporate formality — it is the price of the inter-series protection.

### 10.3 Example — Crypto / digital-asset holding

**Facts.** Jordan Park, Nevada resident, has accumulated approximately $4.5 million in cryptocurrency over the past eight years, held primarily in two hardware wallets (Ledger and Trezor) and one Coinbase Custody account. Jordan is a software engineer at a Nevada-based tech company, has no current creditors, and is concerned about (a) liability from a future failed startup he plans to launch, (b) hacking / loss of the private keys, and (c) estate-planning concerns about transferring the assets to children at death.

**Structure.**

1. **Form a Nevada single-member LLC** ("Park Digital Assets LLC") — $425 first-year cost. Manager-managed, with Jordan as the sole manager and sole member.
2. **Transfer the crypto to the LLC.** This is the operationally tricky step. Mechanically the transfer occurs by:
   - Generating new wallet addresses owned by the LLC (typically a new Ledger or Trezor device titled in the LLC's name and held in a safe-deposit box rented by the LLC).
   - Sending the crypto from Jordan's personal wallets to the LLC's wallets in a single recorded transaction.
   - Documenting the transfer in a written capital contribution agreement that values the crypto at its FMV on the date of transfer.
   - Filing an LLC operating-agreement amendment recording the contribution.
   - For the Coinbase Custody account, opening a new LLC-titled account and transferring the holdings (Coinbase will require LLC formation documents, EIN letter, and operating agreement).
3. **Establish the LLC's books and records.** Each year's gain/loss on disposition of crypto is reported on the LLC's books and flows to Jordan's Schedule D (because the LLC is disregarded for federal tax). The LLC structure does NOT change the federal tax treatment of the crypto — disposals still produce capital gain/loss. But the LLC structure creates a separate legal owner for asset-protection purposes.
4. **Optionally, transfer the LLC interest to a Nevada DAPT** under NRS 166. This stacks charging-order protection (against the LLC interest) with DAPT protection (against the trust interest). For Jordan's facts — no current creditors, foreseeable future startup liability — the DAPT layer is worth considering. Two-year clock starts on the date of the LLC-interest transfer to the trust.

**Operational issues unique to crypto.**

- **Private key custody.** The LLC's wallets must be held by the LLC, not by Jordan personally. If Jordan keeps the seed phrase in his personal safe, a creditor can argue alter-ego — that the LLC's "ownership" is a fiction because Jordan retains practical custody. Best practice: store seed phrases in a safe-deposit box rented by the LLC, with the LLC's records reflecting the rental.
- **Reporting on Form 8938 and FBAR.** Even though the LLC is disregarded, Jordan may have foreign-account reporting obligations on the underlying exchanges (if any are foreign). Crypto-specific reporting under Form 1099-DA (effective 2025) and the broker reporting rules under IRC §6045 apply to dispositions regardless of LLC structure.
- **State sales tax.** Nevada does not impose sales tax on cryptocurrency transactions. Some states do (e.g., on the conversion of crypto to a stablecoin or to fiat). Nevada formation gives Jordan a clean home-state position.
- **Federal tax on the contribution.** Contribution of appreciated crypto to a single-member LLC is not a taxable event (the LLC is disregarded). Contribution to a multi-member LLC may be a taxable event if §721 does not apply (e.g., investment-company restrictions). For a single-member LLC, this is not an issue.
- **Federal tax on contribution to DAPT.** Contribution to a Nevada DAPT structured as a grantor trust is not a taxable event for income-tax purposes (grantor is still the owner under IRC §671). It MAY be a taxable gift for gift-tax purposes if the DAPT is not properly structured as an "incomplete gift" trust. Most asset-protection-focused DAPTs are structured as completed-gift trusts (to use the lifetime gift exclusion) or as incomplete-gift trusts (to avoid using exclusion) depending on the settlor's estate-tax posture. Crypto contributions can rapidly exhaust the lifetime exclusion ($13.99 million for 2025) if the structure is completed-gift — handle with care.

**Cost.** LLC: $425 first year, $350/year thereafter. DAPT: $5,000–$15,000 attorney fees + ongoing Nevada trustee fee of $3,000–$10,000/year. The DAPT cost generally only makes sense for crypto holdings >$2 million.

**Audit flash points.**
- Jordan must NOT use LLC-held crypto for personal expenditures. If he wants to spend crypto on a personal purchase, he must first distribute crypto (or the fiat proceeds of a sale) from the LLC to himself as a member distribution, document the distribution, and only then spend.
- Seed-phrase custody is the most common veil-piercing risk in crypto LLC structures. Documentation that the LLC, not Jordan personally, has custody of the seed phrase is essential.
- Two-year DAPT clock starts only when the LLC interest is transferred to the trust — not when the crypto was originally acquired or when the LLC was originally formed. Time the transfer carefully.

## 11. Common Errors and Audit Flash Points

This section consolidates the audit flash points scattered through the skill into a single checklist. A reviewer signing off on a Nevada formation should verify each of the following:

### 11.1 Formation mechanics

- **State Business License obtained at formation** — Most common omission. NRS 76.100 requires the license for every entity. $200 first year, $200 annual renewal. Late: $100 penalty plus reinstatement.  _(NRS 76.100)_
- **Initial List filed on time** — Due by the last day of the month after formation. NRS 86.263 (LLC) or NRS 78.150 (corporation). Late: $75 penalty plus reinstatement.  _(NRS 86.263; NRS 78.150)_
- **Registered agent is a Nevada resident or commercial registered agent** — NRS 77.310. A P.O. Box, an out-of-state address, or a non-resident individual is not sufficient.  _(NRS 77.310)_
- **Entity name is distinguishable** — Pre-check via SilverFlume name-search before filing.
- **Articles capture authorized capital correctly for C-corps** — The NRS 78.760 share-based fee schedule applies at formation. Authorize only what is needed; share count can be amended later (with a separate fee).  _(NRS 78.760)_

### 11.2 Charging-order protection

- **Operating agreement expressly invokes NRS 86.401** — The default charging-order rule applies whether or not the operating agreement says so, but a clear recital strengthens the position in litigation.  _(NRS 86.401)_
- **Operating agreement gives manager discretion over distributions** — Mandatory distributions undermine charging-order protection.
- **Operating agreement includes transfer restrictions** — Right of first refusal, drag-along provisions, restrictions on assignment of economic interests.
- **Capital contributions and distributions are documented** — Each contribution and distribution must be on the LLC's books with appropriate journal entries.
- **No commingling** — LLC bank account is separate from personal accounts; LLC credit cards are not used for personal purchases.
- **Annual maintenance** — Annual List and State Business License paid on time. Operating-agreement reviews annually. Member/manager certifications updated.

### 11.3 DAPT

- **At least one Nevada trustee** — NRS 166.015(1). The settlor cannot serve as sole trustee — there must be a Nevada-resident individual, Nevada-chartered trust company, or federally chartered institution with a Nevada office.  _(NRS 166.015(1))_
- **Trust is irrevocable** — NRS 166.015(2). Limited powers to amend administrative provisions are permitted; power to revoke is not.  _(NRS 166.015(2))_
- **Spendthrift clause is present** — NRS 166.020. Both voluntary and involuntary alienation restricted.  _(NRS 166.020)_
- **Settlor's permitted powers do not exceed NRS 166.040** — Power to direct investments, veto distributions, testamentary power of appointment — yes. Power to compel distribution to settlor — no.  _(NRS 166.040)_
- **Solvency at time of funding documented** — Independent CPA solvency analysis at the date of each contribution. Critical for fraudulent-transfer defense.
- **No substantially all assets transferred** — Meaningful liquid net worth retained outside the trust.
- **Two-year seasoning clock on each contribution tracked** — A schedule of contributions and seasoning maturity dates maintained.
- **No retreats** — Settlor does not treat trust assets as personal pocket money. Distributions are requested in writing and considered by the trustee on the record.

### 11.4 Series LLC

- **Articles of Organization expressly authorize series** — NRS 86.1255(1).  _(NRS 86.1255(1))_
- **Operating agreement identifies each series and its members, managers, assets, business purpose** — 
- **Separate bank accounts and accounting per series** — Inter-series transfers documented as intercompany loans or capital movements.
- **Separate insurance per series** — Each series should be a named insured on policies relating to its assets.
- **Deeds, contracts, and tenant agreements reference the specific series, not the master LLC** — 
- **Separate EINs per series** — Safer position pending finalization of Prop. Reg. §301.7701-1(a)(5).  _(Prop. Reg. §301.7701-1(a)(5))_
- **Out-of-state recognition checked** — Before assuming inter-series protection in another state, verify that state's recognition (or non-recognition) of Series LLCs.

### 11.5 Choice-of-state and residency

- **Owner's residency confirmed** — Nevada formation only provides PIT savings to a Nevada-resident owner. CA/NY/MA residents who form in NV still owe home-state PIT on worldwide income.
- **Nexus analysis performed** — A Nevada LLC operating in another state must foreign-qualify. Failure exposes the LLC to penalties and litigation-access bars.
- **VC fundraising contemplated?** — If yes, Delaware is the right choice. Forming in Nevada now and redomesticating to Delaware later is expensive and tax-complex.
- **Operating reality matches structure** — A Nevada LLC managed entirely from California is doing business in California regardless of its formation state.

### 11.6 Federal coordination

- **EIN obtained** — Required for opening bank accounts and for federal filings even for single-member LLCs that don't have a separate-entity filing obligation.
- **Check-the-box election considered** — Default classification (disregarded for single-member, partnership for multi-member) is usually correct, but an S-election (Form 2553) or C-election (Form 8832) may be advisable depending on facts. See `us-s-corp-election-decision.md`.  _(Form 2553; Form 8832)_
- **Schedule C / Schedule E / partnership return aligned** — The federal filing must reflect the LLC's actual federal classification. See `us-sole-prop-bookkeeping.md` and `us-schedule-c-and-se-computation.md`.

## 12. Defaults, Limits, and Output Spec

Per `us-tax-workflow-base v0.2`, this skill emits a reviewer-oriented output package containing:
1. **Entity recommendation memo** — one to two pages summarizing the recommended entity type, jurisdiction, and rationale, with explicit calls to alternative jurisdictions and the reasons not to choose them.
2. **Formation checklist** — step-by-step list of filings, deadlines, fees, and required information, with the deadlines for the Initial List and the State Business License highlighted.
3. **First-year cost estimate** — itemized cost breakdown.
4. **Annual recurring cost estimate** — itemized.
5. **Operating agreement / bylaw drafting notes** — flagging the charging-order recital, transfer restrictions, manager discretion over distributions, and (for series LLCs) the inter-series segregation requirements.
6. **DAPT supplement (if applicable)** — separate package covering the trust structure, contribution timing, solvency documentation, and seasoning-clock schedule.
7. **Foreign qualification supplement (if applicable)** — list of states requiring qualification and the cost/timeline for each.
8. **Self-check** — the checklist in Section 11 with each item marked complete, deferred, or not-applicable.
9. **Credentialed-reviewer signoff block** — under Circular 230, every output must be reviewed by an EA, CPA, or attorney before delivery.

### 12.1 Refusal catalogue

- **No business purpose / sham formation** — The owner is not a Nevada resident AND has no Nevada-situs activity AND has no asset-protection rationale — the formation has no business purpose and may be a sham.
- **Named creditor / fraudulent transfer** — The owner discloses a specific named creditor whose claim has accrued or is reasonably foreseeable — DAPT structuring under these facts is a fraudulent transfer and the firm should not facilitate it.
- **Tax evasion intent** — The owner discloses intent to use the Nevada structure to evade taxes legally owed to the IRS or to another state — this exceeds professional ethical boundaries under Circular 230 §10.51.  _(Circular 230 §10.51)_
- **Regulated industry without specialist counsel** — The structure involves a regulated industry (gaming, marijuana, banking, insurance) and the firm does not have specialist counsel involved.
- **No credentialed counsel for DAPT drafting** — The owner has not engaged credentialed counsel for the DAPT trust drafting (the Nevada DAPT requires attorney-drafted instruments — the firm should not provide trust documents).
- **VC fundraising contemplated** — The owner contemplates VC fundraising — refer to specialist startup counsel and recommend Delaware C-corporation formation.

### 12.2 Citation discipline

- **Citation format standards** — When citing Nevada statutes, use the format "NRS §" followed by the chapter and section (e.g., "NRS 86.401(2)(a)"). For Delaware comparisons use "Del. Code Ann. tit. X" or the equivalent. For federal Internal Revenue Code citations use "IRC §" (e.g., "IRC §671"). For Treasury Regulations use "Treas. Reg. §" or "Prop. Reg. §" as appropriate. Do not cite secondary sources or formation-service-company marketing materials.

### 12.3 Conservative defaults

- **Default manager-managed LLC** — Default to a manager-managed LLC structure (gives more flexibility for inserting a non-debtor manager later, and is friendlier to charging-order discretion).
- **Default C-corp authorized shares** — Default to authorizing only 75,000 shares for a C-corporation (minimum filing-fee tier — easy to amend upward later).
- **Default registered agent** — Default to a single Nevada commercial registered agent (avoids the cost and risk of designating an individual).
- **Default Initial List timing** — Default to filing the Initial List concurrently with the Articles (eliminates deadline-tracking risk).
- **Default Wyoming recommendation for non-asset-protection founders** — Default to recommending a non-VC-track founder use Wyoming over Nevada IF asset protection is not a stated objective — Wyoming is cheaper for pure no-PIT, no-corporate-tax benefits.
- **Default Delaware recommendation for VC-track founders** — Default to recommending Delaware for any founder who has mentioned VC, institutional investment, multiple share classes, or stock-based compensation.
- **Default credentialed reviewer signoff** — Default to requesting the credentialed reviewer's signoff before delivery — never deliver formation documents directly to the client without EA/CPA/attorney review.

## 13. Cross-references

- `nv-commerce-tax.md` — Nevada Commerce Tax ($4M gross-receipts threshold), filed annually via the Nevada Department of Taxation.
- `nv-commerce-and-mbt.md` — Combined Nevada Commerce Tax and Modified Business Tax (MBT) on payroll.
- `nv-sales-tax.md` — Nevada sales and use tax compliance.
- `no-sales-tax-states.md` — Cross-state reference for states with no general sales tax (Nevada has sales tax — this is the cross-reference for entities forming in Nevada but operating in NH, MT, OR, AK, or DE).
- `global-router.md` — Top-level state-selection routing.
- `us-s-corp-election-decision.md` — Federal S-election analysis for a newly formed Nevada LLC or corporation.
- `us-sole-prop-bookkeeping.md` — Schedule C classification for a single-member Nevada LLC disregarded for federal tax.
- `us-schedule-c-and-se-computation.md` — SE tax computation for the Nevada-LLC sole-prop owner.
- `us-federal-return-assembly.md` — Final assembly of the federal return where a Nevada formation is involved.

## 14. Version notes

- 0.1 (2025-11-15): Initial draft covering LLC formation, C-corp formation, charging-order protection, DAPT, Series LLC, NV vs WY vs DE comparison, foreign qualification, and three worked examples. Awaiting verification by Nevada-credentialed reviewer.

End of nv-formation.md.

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is
different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your
jurisdiction — **no liability on either side until you and the accountant sign
a formal engagement letter** — book a free 30-minute call:

**→ [Book a call](https://calendly.com/openaccountants-info/30min)**

We'll route you to the named verifier covering your country or state. You can
also see the full list of verified accountants at
[openaccountants.com/network](https://openaccountants.com/network).
