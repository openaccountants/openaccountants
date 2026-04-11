---
name: ny-llc-filing-fee-it-204-ll
description: Tier 2 New York content skill for preparing Form IT-204-LL (Partnership, Limited Liability Company, and Limited Liability Partnership Filing Fee Payment Form) for single-member LLCs disregarded for federal tax purposes whose sole member is a New York full-year resident individual. Covers the flat $25 disregarded-entity filing fee under NY Tax Law §658(c)(1), the "income, gain, loss, or deduction from New York sources" filing trigger, the dormancy exception, the March 15 due date with no extension available, late filing and late payment penalties, and the coordination with the owner's Form IT-201. Does NOT cover multi-member LLCs, LLCs taxed as partnerships or corporations, the gross-receipts-based sliding fee schedule for partnership-taxed LLCs, or LLCs doing business both inside and outside New York — see Section 7. MUST be loaded alongside us-tax-workflow-base v0.2 or later and ny-it-201-resident-return. New York full-year residents with disregarded SMLLCs only.
version: 0.2
---

# New York IT-204-LL SMLLC Filing Fee Skill v0.2

## What this file is, and what it is not

This is a Tier 2 content skill under `us-tax-workflow-base v0.2`. It conforms to the thirteen mandatory slots of the Section 7 content skill slot contract. It provides the position rules, figures, citations, refusals, defaults, reviewer attention thresholds, worked examples, intake additions, and self-check additions needed to prepare Form IT-204-LL for a single-member LLC disregarded for federal tax whose sole member is a New York State full-year resident individual.

This skill cannot produce any output on its own. It must be loaded alongside `us-tax-workflow-base` for the workflow runbook, output specification, global refusals, self-checks, and citation discipline. It is typically loaded alongside `ny-it-201-resident-return` as part of a full NY resident filing engagement, but it can be invoked standalone for a discrete IT-204-LL review.

---

## Section 1 — Scope statement

**In scope.** This skill covers the preparation of Form IT-204-LL for tax year 2025 for:

- A single-member LLC (SMLLC) that is treated as a disregarded entity for federal income tax purposes (default classification, or an affirmative Form 8832 disregarded election);
- Organized under New York law OR organized in another state and registered as a foreign LLC with the New York Department of State;
- Whose sole member is an individual who was a full-year New York State resident for 2025;
- That had any income, gain, loss, or deduction from New York sources in 2025.

The skill produces one deliverable: a completed Form IT-204-LL worksheet reporting the flat $25 disregarded-entity filing fee, with payment instructions, due date, and a reviewer brief section explaining the filing determination.

**Out of scope.** The following are refused under Section 7 of this skill:

- Multi-member LLCs (refused; treated as partnerships for federal tax and use a different fee schedule)
- LLCs electing corporate treatment via Form 8832 or S-corporation treatment via Form 2553
- LLCs whose sole member is a non-resident, part-year resident, trust, estate, or other entity
- LLCs with activity inside and outside New York requiring apportionment
- Tiered partnership structures
- Fiscal-year filers
- Short-period returns (first year with formation mid-year, final year with dissolution mid-year) with complex timing questions
- Amended IT-204-LL filings
- Pure-investment LLCs potentially exempt under nexus rules
- LLCs in liquidation or dissolution

The scope limitations align with `us-tax-workflow-base` Section 6 base refusals (R-US-PARTNERSHIP, R-US-S-CORP, R-US-C-CORP, R-US-MULTISTATE, R-US-ESTATE-TRUST, R-US-INVESTMENT-INCOME) and add NY-specific refusals in this skill's Section 7 (R-NY204-1 through R-NY204-10).

---

## Section 2 — Tax year coverage and currency

**Tax year covered:** 2025 (calendar year, returns due in 2026).

**Currency date:** The skill is current as of April 2026. Every figure, every form reference, every statutory citation in this skill is verified against primary sources as of that date.

**Legislation and guidance current as of the currency date:**

- NY Tax Law §658(c) as amended by Chapter 59 of the Laws of 2025 (the Executive Budget bill for FY 2025-26), effective for tax years beginning on or after January 1, 2025
- Form IT-204-LL (2025) released by NYSDTF in January 2026
- Instructions for Form IT-204-LL (2025), Publication IT-204-LL-I, released by NYSDTF in January 2026
- NY Publication 16, "New York Tax Status of Limited Liability Companies and Limited Liability Partnerships," most recent version

**Legislation monitored but not in force for 2025:**

- No pending NY legislation affects the flat $25 disregarded-entity filing fee for TY 2025. The OBBBA §174A uncertainty that affects the IT-201 skill does not affect this skill — the IT-204-LL filing fee is a flat amount independent of federal taxable income computation.

---

## Section 3 — Year-specific figures table for tax year 2025

### Filing fee amounts

| Figure | Value | Source |
|---|---|---|
| Disregarded-entity SMLLC filing fee | $25 (flat) | NY Tax Law §658(c)(1); Form IT-204-LL Instructions (2025), Line 7 |
| Minimum partnership LLC filing fee | $25 | NY Tax Law §658(c)(2); Form IT-204-LL Instructions (2025), filing fee table |
| Maximum partnership LLC filing fee | $4,500 | NY Tax Law §658(c)(2); Form IT-204-LL Instructions (2025), filing fee table (NOT relevant to this skill; shown for contrast) |
| Proration for short tax year | None (no proration allowed) | Form IT-204-LL Instructions (2025), "Period covered" |

### Filing trigger thresholds

| Figure | Value | Source |
|---|---|---|
| Disregarded SMLLC filing trigger | Any income, gain, loss, or deduction from NY sources | NY Tax Law §658(c)(1); Form IT-204-LL Instructions (2025), "Who must file" |
| Dormancy exception | Zero income, gain, loss, or deduction from NY sources | Form IT-204-LL Instructions (2025), "Who is not required to file"; NY Publication 16 |

### Due dates and extensions

| Figure | Value | Source |
|---|---|---|
| IT-204-LL due date (calendar year) | 15th day of 3rd month after year-end | NY Tax Law §658(c)(3); Form IT-204-LL Instructions (2025), "When to file" |
| 2025 calendar year due date | March 16, 2026 (March 15 falls on Sunday) | General rule: NY Tax Law §171; §658(c)(3) |
| 2026 calendar year due date | March 15, 2027 | NY Tax Law §658(c)(3) |
| Extension available | None | Form IT-204-LL Instructions (2025), "No extension of time" |

### Penalties and interest

| Figure | Value | Source |
|---|---|---|
| Late filing penalty | 5% per month of unpaid fee, max 25% | NY Tax Law §685(a)(1); applied to filing fee via §658(c)(3)(D) |
| Late payment penalty | 0.5% per month of unpaid fee, max 25% | NY Tax Law §685(a)(2); applied via §658(c)(3)(D) |
| Combined maximum penalty | 25% of fee | NY Tax Law §685(a)(1) proviso |
| Interest rate on underpayments | Variable, set quarterly by Commissioner | NY Tax Law §684; current rate approximately 9.5% annually as of the currency date |
| Minimum combined penalty on $25 fee | Trivial (≤ $6.25), but the non-filing record is the real risk | Computed from §685 figures above |

### Form line references

| Form line | Content | Source |
|---|---|---|
| IT-204-LL Part 1 | General information: legal name, address, EIN/SSN, DOS file number, formation date, business description, filer type checkbox | Form IT-204-LL (2025), Part 1 |
| IT-204-LL Part 1 Line 1 | "Did this entity have any income, gain, loss, or deduction from NY sources during the 2025 tax year?" (Yes required to file) | Form IT-204-LL (2025), Line 1 |
| IT-204-LL Part 1 Line 2 | Interest in NY real property in last three years | Form IT-204-LL (2025), Line 2 |
| IT-204-LL Part 1 Line 3 | Transfer or acquisition of controlling interest in last three years | Form IT-204-LL (2025), Line 3 |
| IT-204-LL Part 2 | Partnership / partnership-taxed LLC fee computation (SKIP for disregarded SMLLCs) | Form IT-204-LL (2025), Part 2 |
| IT-204-LL Part 3 Line 6a | Name of owner (for disregarded SMLLCs) | Form IT-204-LL (2025), Line 6a |
| IT-204-LL Part 3 Line 6b | SSN of owner | Form IT-204-LL (2025), Line 6b |
| IT-204-LL Part 3 Line 7 | LLC disregarded entity NYS filing fee (ENTER 25) | Form IT-204-LL (2025), Line 7 |
| IT-204-LL Part 4 | Payment amount and signature | Form IT-204-LL (2025), Part 4 |

---

## Section 4 — Primary source library

Every position in this skill cites from this list. New citations added to the skill must be verified against the primary source before use.

### New York statutory authority

| Citation | Governs |
|---|---|
| NY Tax Law §658(c)(1) | Imposes the flat $25 filing fee on disregarded SMLLCs with NY source income, gain, loss, or deduction |
| NY Tax Law §658(c)(2) | Imposes the sliding-scale filing fee on LLCs/LLPs treated as partnerships (out of scope for this skill; cited for contrast) |
| NY Tax Law §658(c)(3) | Sets the due date, the no-extension rule, and the collection and enforcement mechanics |
| NY Tax Law §658(c)(3)(D) | Provides that the fee is assessed, collected, and enforced "in the same manner as tax" and imposes penalties and interest on the same basis as a late tax return |
| NY Tax Law §631 | Defines New York source income for individuals; incorporated by reference for determining NY source activity of a disregarded SMLLC |
| NY Tax Law §612 | Defines NY adjusted gross income for residents (taxed on worldwide income); relevant to determining that a resident member's LLC activity is NY source regardless of client location |
| NY Tax Law §684 | Sets interest rates on underpayments |
| NY Tax Law §685(a)(1) | Sets the 5% per month late filing penalty |
| NY Tax Law §685(a)(2) | Sets the 0.5% per month late payment penalty |
| NY Tax Law §171 | General rule that due dates falling on a Saturday, Sunday, or legal holiday shift to the next business day |

### NYSDTF guidance

| Citation | Governs |
|---|---|
| Form IT-204-LL (2025) | The filing form itself, released January 2026 |
| Form IT-204-LL Instructions (2025) | Official line-by-line instructions; primary authority for filing trigger, due date, no-extension rule, and fee computation |
| NY Publication 16 | "New York Tax Status of Limited Liability Companies and Limited Liability Partnerships"; explains the dormancy exception, the disregarded entity treatment, and the NY source income rules for LLC fee purposes |
| NY Department of Taxation and Finance, "Partnership, LLC, and LLP annual filing fee" | Overview page at tax.ny.gov/pit/efile/annual_filing_fee.htm |

### Federal authority (for disregarded entity classification only)

| Citation | Governs |
|---|---|
| Treas. Reg. §301.7701-3(b)(1)(ii) | Default classification of a single-member LLC as disregarded for federal tax purposes |
| Treas. Reg. §301.7701-3(c) | Form 8832 classification election (used here only to identify LLCs that have elected out of disregarded treatment and are therefore out of scope) |

### URLs for verification (not authoritative, for skill maintenance)

- Form IT-204-LL (2025): https://www.tax.ny.gov/pdf/2025/inc/it204ll_2025_fill_in.pdf
- Instructions for Form IT-204-LL (2025): https://www.tax.ny.gov/forms/current-forms/it/it204lli.htm
- Instructions PDF (2025): https://www.tax.ny.gov/pdf/2025/inc/it204lli_2025.pdf
- Partnership, LLC, LLP annual filing fee overview: https://www.tax.ny.gov/pit/efile/annual_filing_fee.htm

---

## Section 5 — Position rules

Each position rule follows the slot 5 contract format: **trigger condition → rule → conservative default → source**. A worked example for each position appears in Section 9.

### Position 5.1 — Entity classification gate

**Trigger.** The intake identifies that the freelancer operates through an LLC.

**Rule.** Confirm that the LLC is single-member (the freelancer is the only owner) and that it has NOT filed Form 8832 electing corporate treatment or Form 2553 electing S-corp treatment. If both conditions are satisfied, the LLC is disregarded for federal purposes under Treas. Reg. §301.7701-3(b)(1)(ii) and is within this skill's scope. If the LLC has multiple members, fire R-NY204-1. If the LLC has elected corporate or S-corp treatment, fire R-NY204-2.

**Conservative default.** If classification is ambiguous and the user cannot confirm, refuse under R-US-CONTENT-MISMATCH (from the base) pending reviewer verification. Do not assume disregarded status without evidence.

**Source.** Treas. Reg. §301.7701-3(b)(1)(ii); Treas. Reg. §301.7701-3(c); Form IT-204-LL Instructions (2025), "Who must file" section, disregarded entity bullet.

### Position 5.2 — Owner residency gate

**Trigger.** Entity classification (Position 5.1) has cleared.

**Rule.** Confirm that the sole member is a New York State full-year resident for 2025. "Full-year resident" means domiciled in NY for the entire tax year OR (if not domiciled in NY) maintaining a permanent place of abode in NY and being physically present in NY for more than 183 days of the year (Tax Law §605(b)). If the member is a part-year resident, non-resident, trust, estate, or other entity, fire R-NY204-3.

**Conservative default.** If residency is ambiguous (e.g., the member moved late in the year but the move date is unclear), refuse under R-NY204-3 and route to the not-yet-built part-year resident skill.

**Source.** NY Tax Law §605(b); Form IT-204-LL Instructions (2025), "Who must file" (implicit; the form requires the owner's identifying information and the fee structure assumes resident ownership for disregarded entities in this skill's scope).

### Position 5.3 — NY source activity determination

**Trigger.** Owner residency has cleared.

**Rule.** For a disregarded SMLLC whose sole member is a NY full-year resident, the "NY source activity" test under NY Tax Law §658(c)(1) is satisfied if the LLC had **any** income, gain, loss, or deduction in the current tax year. This follows from the interaction of §658(c)(1) with §612 (residents are taxed on worldwide income) — activity performed by a NY resident member is NY source activity regardless of where the client or counterparty is located. Examples of qualifying activity:

- Client payments received by the LLC (any amount, any source)
- Bank interest earned on the LLC's operating account
- Any business expense paid by the LLC (software subscriptions, contractor payments, bank fees)
- LLC maintenance fees paid to the NY Department of State
- Depreciation on an asset owned by the LLC (even if no cash moved)

If the LLC had zero activity — no receipts, no disbursements, no assets generating deduction, no interest earned — the dormancy exception under Form IT-204-LL Instructions (2025), "Who is not required to file," applies and the LLC is not required to file Form IT-204-LL for 2025.

**Conservative default.** If the taxpayer cannot confirm whether any activity occurred (e.g., they are uncertain whether bank interest was credited or whether a state DOS fee was auto-debited), assume activity occurred and file. The cost of over-filing is $25 and a few minutes; the cost of under-filing is penalties and a compliance record flag. The default is always to file when in doubt.

**Source.** NY Tax Law §658(c)(1); NY Tax Law §612; Form IT-204-LL Instructions (2025), "Who must file" and "Who is not required to file" sections; NY Publication 16.

### Position 5.4 — Fee amount (flat $25, no computation)

**Trigger.** Positions 5.1, 5.2, and 5.3 have cleared — i.e., the SMLLC is in scope and has qualifying NY source activity.

**Rule.** The filing fee is **$25 flat**. There is no gross-receipts computation, no sliding scale, no proration for short tax years, no minimum or maximum above $25. On Form IT-204-LL, skip Part 2 entirely (that part is for partnership-taxed LLCs) and enter `25` on Line 7 in Part 3.

**Conservative default.** Not applicable — the fee is fixed. Any computation other than $25 indicates an error in the skill's logic.

**Source.** NY Tax Law §658(c)(1); Form IT-204-LL Instructions (2025), Line 7 ("LLC disregarded entity NYS filing fee — Enter 25 on this line").

### Position 5.5 — Due date determination

**Trigger.** Fee amount has been set.

**Rule.** The return is due on the 15th day of the 3rd month following the close of the LLC's tax year. For a calendar-year LLC, that is March 15 of the following year. For tax year 2025, March 15, 2026 falls on a Sunday, so the due date shifts to the next business day: **March 16, 2026** under NY Tax Law §171.

There is **no extension of time** to file Form IT-204-LL or to pay the fee. Filing Form IT-370 to extend the owner's Form IT-201 personal return does NOT extend Form IT-204-LL. This is stated explicitly in the Form IT-204-LL Instructions (2025) and is the single most common trap for freelance developers who assume all NY filings share the personal return's April 15 due date.

**Conservative default.** If the due date is ambiguous (e.g., the LLC is newly formed and the first tax year is uncertain), assume the earliest plausible due date and flag for reviewer.

**Source.** NY Tax Law §658(c)(3); NY Tax Law §171; Form IT-204-LL Instructions (2025), "When to file" and "No extension of time" sections.

### Position 5.6 — Penalty exposure for non-filing or late payment

**Trigger.** Not a preparation position, but a reviewer-brief and planning position. Applied when the taxpayer has missed a prior-year IT-204-LL filing or is at risk of missing the current due date.

**Rule.** Under NY Tax Law §658(c)(3)(D), the $25 fee is assessed, collected, and enforced "in the same manner as tax." Late filing triggers a 5% per month penalty (capped at 25%) under §685(a)(1). Late payment triggers a 0.5% per month penalty (capped at 25%) under §685(a)(2). Interest accrues at the statutory rate under §684.

On a $25 fee, the maximum combined penalty is approximately $6.25. The dollar amount is trivial. The reason to still file on time is the compliance record: unfiled returns are open items at NYSDTF, surface during cross-checks, and create findings in any future due diligence. The reviewer brief must state this plainly — the dollar cost of non-compliance is not the point; the record-keeping cost is.

**Conservative default.** Always file, always pay the $25 on time, even if the taxpayer questions whether it's "worth it." The answer is always yes.

**Source.** NY Tax Law §658(c)(3)(D); §685(a)(1); §685(a)(2); §684.

### Position 5.7 — Federal deductibility of the $25 fee (negative position)

**Trigger.** The taxpayer asks whether they can deduct the $25 on Schedule C, or the skill is asked to determine the federal tax effect of the fee.

**Rule.** The $25 is paid by the LLC, but because the LLC is disregarded for federal tax purposes, any LLC-level expense flows to the owner's Schedule C by operation of the disregarded entity rule. The question is whether it is deductible there.

The $25 IT-204-LL filing fee is a **state entity-level fee**, not a business tax in the §164 sense. It is arguably deductible on Schedule C as an ordinary and necessary business expense under IRC §162 (a cost of maintaining the legal entity through which the trade or business is conducted). Different tax professionals take different positions. Most commonly it is reported as a legal and professional fee (Schedule C Line 17) or as "taxes and licenses" (Schedule C Line 23) or as an "other expense" (Schedule C Line 27a).

However: because the amount is $25 and the tax effect is immaterial (at a 37% marginal rate, the deduction saves $9.25), this skill's position is to **flag the item but not push a position on Schedule C deductibility**. The reviewer can take any defensible position. The skill's reviewer brief notes the item and defers to reviewer judgment.

**Conservative default.** Do not claim the $25 as a Schedule C deduction unless the reviewer affirmatively elects to do so. The conservative position is non-deductible at the federal level.

**Source.** IRC §162(a); IRC §164; Schedule C Instructions (2025), Line 23 and Line 17; no direct primary source on IT-204-LL filing fee deductibility (this is a judgment area, correctly flagged as such).

---

## Section 6 — Conservative defaults table

| Ambiguity | Conservative default | Source |
|---|---|---|
| LLC exists but entity classification unclear | Refuse under R-US-CONTENT-MISMATCH; require reviewer to confirm disregarded status | Treas. Reg. §301.7701-3 |
| Owner residency unclear or mixed-year | Refuse under R-NY204-3; route to part-year resident skill | NY Tax Law §605(b) |
| Activity in 2025 unclear (dormancy ambiguous) | Assume activity occurred; file the return and pay $25 | Cost of over-filing is trivial; cost of under-filing is penalty record |
| LLC has bank account with only interest income | Treat as activity; file | NY Tax Law §612 (all income of resident is NY source) |
| LLC paid only state DOS maintenance fees | Treat as activity (deduction); file | Form IT-204-LL Instructions (2025), "income, gain, loss, or deduction" |
| LLC formed mid-year with activity | File for the full year; no proration | Form IT-204-LL Instructions (2025), "Period covered" |
| LLC dissolved mid-year with prior activity | File for the year of dissolution; no proration | Same |
| NY DOS file number not known | Flag for reviewer; do not invent; can often be looked up via NY DOS Corporation and Business Entity Database | Administrative |
| EIN not assigned to LLC | Use owner's SSN on Line 6b | Form IT-204-LL Instructions (2025), "Identifying number" |
| Prior-year IT-204-LL not filed | Flag as past-due compliance item; recommend current-year filing still proceeds on time; route prior-year catch-up to reviewer | NY Tax Law §658(c)(3)(D) |
| Owner asks if the $25 is Schedule C deductible | Do not claim as federal deduction without reviewer affirmative election | IRC §162; §164 (judgment area) |
| LLC has activity in NYC as well as NY state | File IT-204-LL AND flag for cross-reference to nyc-unincorporated-business-tax skill | Independent filings |
| LLC has a separate NY DOS biennial statement obligation | Flag as related compliance item (non-tax); do not compute | Non-tax obligation, out of skill scope |

---

## Section 7 — Topical refusal catalogue

These refusals extend the base global catalogue in `us-tax-workflow-base` Section 6. When any refusal fires, output the text in the "Output" field **verbatim** per base Check 16, then stop workflow and flag in the brief's refusal trace.

**R-NY204-1 — Multi-member LLC.**
Trigger: The LLC has two or more members (owners) as of any point during the 2025 tax year.
Output: "This skill covers only single-member LLCs disregarded for federal tax. A multi-member LLC is treated as a partnership for federal tax and files Form IT-204 (the full NY partnership return) together with Form IT-204-LL using the gross-receipts-based sliding fee schedule ($25 to $4,500). Partnership preparation is outside this skill's scope. Please consult a CPA or Enrolled Agent familiar with partnership returns."

**R-NY204-2 — LLC elected corporate or S-corporation treatment.**
Trigger: The LLC has filed Form 8832 electing corporate treatment OR Form 2553 electing S-corporation treatment and the election is effective for 2025.
Output: "An LLC that has elected to be treated as a corporation or an S-corporation is not subject to the IT-204-LL filing fee. Instead, the entity files a corporate return under NY Tax Law Article 9-A: Form CT-3 (C-corporation) or Form CT-3-S (S-corporation). Corporate return preparation is outside this skill's scope. Please consult a CPA or Enrolled Agent familiar with NY corporate returns."

**R-NY204-3 — Non-resident or part-year resident owner.**
Trigger: The sole member of the LLC was NOT a New York full-year resident for 2025. This includes part-year residents, non-residents with NY activity, and residents who moved into or out of NY mid-year.
Output: "This skill assumes the LLC's sole member is a New York full-year resident. Part-year and non-resident owners raise NY source allocation questions that require Form IT-203 coordination and potentially Form IT-203-A business allocation. Please consult an Enrolled Agent or CPA familiar with NY part-year and non-resident returns."

**R-NY204-4 — Multi-state LLC activity requiring apportionment.**
Trigger: The LLC has material business activity both inside and outside New York, such that NY source income must be determined by apportionment rather than by the resident's worldwide-income rule.
Output: "This skill assumes all LLC activity is New York source by virtue of the owner's NY residency. An LLC with material business activity inside and outside New York requires Form IT-203-A business allocation analysis, which is outside this skill's scope. Please consult a CPA familiar with multi-state apportionment. (This refusal also triggers R-US-MULTISTATE from the workflow base.)"

**R-NY204-5 — Tiered partnership structure.**
Trigger: The LLC is a partner in another partnership, or another partnership holds an interest in this LLC (tiered structure).
Output: "Tiered partnership structures have complex flow-through treatment under NY Tax Law §§617 and 631. This is outside this skill's scope. Please consult a CPA familiar with tiered partnership returns."

**R-NY204-6 — Fiscal-year LLC.**
Trigger: The LLC uses a fiscal year rather than a calendar year for federal income tax purposes.
Output: "This skill assumes a calendar year LLC. Fiscal-year LLCs have a different due date (15th day of 3rd month after fiscal year-end) and require coordination with the owner's calendar-year Form IT-201 that is beyond this skill's scope. Please consult a CPA familiar with fiscal-year entities."

**R-NY204-7 — Complex short-period return.**
Trigger: The LLC formed mid-year with ambiguous first-year activity OR dissolved mid-year with questions about activity attribution OR changed from multi-member to single-member during the year.
Output: "Complex short-period returns involving formation, dissolution, or member-count changes during the tax year require judgment beyond this skill's scope. Simple cases (LLC formed in the year with clear activity, or LLC dissolved with clear prior activity) can be handled. Ambiguous cases are routed to reviewer. Please consult an Enrolled Agent or CPA for resolution."

**R-NY204-8 — Amended IT-204-LL filing.**
Trigger: The taxpayer needs to amend a previously filed Form IT-204-LL.
Output: "Amending a $25 filing is rare and usually indicates an underlying classification or residency issue that requires human judgment. This skill does not prepare amended IT-204-LL filings. Please consult a CPA or Enrolled Agent."

**R-NY204-9 — Pure-investment LLC potentially exempt under nexus rules.**
Trigger: The LLC's only activity consists of holding investment property or receiving passive investment income, with no active trade or business.
Output: "An LLC whose only activity is holding investment property may qualify for exemption from the IT-204-LL filing fee under complex nexus rules in NY Tax Law §631 and related guidance. This skill assumes the LLC has active trade or business activity. Please consult a CPA familiar with NY investment LLC nexus analysis. (This refusal also triggers R-US-INVESTMENT-INCOME from the workflow base.)"

**R-NY204-10 — LLC is in liquidation or dissolution with open tax matters.**
Trigger: The LLC is winding down operations and has open tax matters (unfiled returns, outstanding liabilities, pending audits) that affect the final filing.
Output: "An LLC in liquidation or dissolution with open tax matters requires coordinated handling of the final return, any outstanding obligations, and the dissolution filings with NY DOS. This is outside this skill's scope. Please consult a CPA or Enrolled Agent familiar with LLC dissolution. (This refusal may also trigger R-US-AUDIT from the workflow base if open audits exist.)"

---

## Section 8 — Reviewer attention thresholds

This skill produces a $25 filing fee deliverable. Traditional dollar-threshold reviewer attention flags are not meaningful here. Instead, reviewer attention is triggered by any of the following conditions, regardless of the dollar amount at stake:

| Trigger | Flag reason |
|---|---|
| Prior-year IT-204-LL was not filed and the non-filing is still open | Compliance history gap; reviewer must decide whether to catch up prior years before the current filing |
| LLC formed in 2025 — first filing | First-year LLCs often have errors in DOS file number, formation date, or principal business activity description; verify all Part 1 fields |
| LLC has NYC nexus (any NYC activity at all) | Cross-reference to `nyc-unincorporated-business-tax` required; UBT filing may be required separately with a potentially material tax effect |
| LLC dissolved during 2025 | Verify that the current filing is the final IT-204-LL and that NY DOS dissolution steps are underway |
| Owner is considering S-corp election for 2026 | Flag for `us-s-corp-election-decision` skill; election changes entity classification for all purposes |
| Activity consists entirely of bank interest and state DOS fees (no active trade) | Verify that the LLC genuinely has active trade or business; flag potential R-NY204-9 concern if pure passive |
| LLC has any non-US owner exposure (owner is dual-resident, owner spouse is non-resident alien) | Flag for R-US-FOREIGN from base; potential FBAR and Form 5472 implications outside this skill |
| LLC's owner maintained the LLC through a registered agent in another state | Verify owner residency more carefully; sometimes indicates the LLC was formed in a different state primarily and NY registration is secondary |
| The taxpayer asks about deductibility of the $25 on Schedule C | Flag as judgment area; reviewer decides whether to claim |
| First IT-204-LL filing after a Form 8832 disregarded election | Verify the federal election was actually filed and accepted; reviewer should see the IRS confirmation letter |

---

## Section 9 — Worked examples

Five worked examples covering the common fact patterns the skill encounters. Each shows facts → reasoning → citations → output.

### Example 1 — Brooklyn-based freelance developer with active LLC

**Facts.** Sarah is a freelance software developer, single, age 32, full-year resident of Brooklyn. In 2024 she formed Sarah Code LLC in New York to run her consulting work. For 2025 she had $180,000 in client receipts flowing through the LLC's Chase business checking account, paid $8,000 in business expenses through the LLC (SaaS, AWS, conference travel), and earned $142 in interest on the LLC's savings sub-account. She uses the LLC's EIN. She has never filed Form 8832. No employees. Domestic US clients only. She plans to file Form IT-201 as a single NY full-year resident.

**Reasoning.**

Step 1 — Entity classification (Position 5.1). Single-member LLC, no Form 8832, default disregarded under Treas. Reg. §301.7701-3(b)(1)(ii). In scope.

Step 2 — Owner residency (Position 5.2). Full-year resident of NY under Tax Law §605(b). In scope.

Step 3 — NY source activity (Position 5.3). $180,000 in receipts, $8,000 in expenses, $142 in interest. All three are "income, gain, loss, or deduction from New York sources" because Sarah is a NY resident (worldwide-income rule under §612). Filing required.

Step 4 — Fee amount (Position 5.4). $25 flat. Skip Part 2. Enter 25 on Line 7.

Step 5 — Due date (Position 5.5). March 16, 2026 (March 15 falls on Sunday).

**Output.** File Form IT-204-LL by March 16, 2026 with a $25 payment. Reviewer brief notes that this filing is separate from Sarah's Form IT-201 and that her April 15 personal return extension, if any, does not extend this form.

**Primary source.** NY Tax Law §658(c)(1); §612; §171; Treas. Reg. §301.7701-3(b)(1)(ii); Form IT-204-LL Instructions (2025).

### Example 2 — Dormant LLC, no 2025 activity (dormancy exception applies)

**Facts.** Marcus formed Marcus Consulting LLC in NY in June 2023 intending to freelance, but then took a W-2 job in September 2023 and never used the LLC. The LLC has no bank account, no EIN, no clients, no contracts. It is still registered with NY DOS. For 2025 Marcus had zero activity in the LLC — no payments in, no payments out, no assets. He did file IT-204-LL and pay $25 for 2023 and 2024 out of caution. For 2025 he wants to know if he needs to file again.

**Reasoning.**

Step 1 — Entity classification. Single-member LLC, no Form 8832, disregarded. In scope.

Step 2 — Owner residency. Marcus is a NY full-year resident. In scope.

Step 3 — NY source activity (Position 5.3). Zero income, zero gain, zero loss, zero deduction. The dormancy exception under Form IT-204-LL Instructions (2025), "Who is not required to file," applies. Marcus is **not required** to file Form IT-204-LL for 2025.

Step 4 — Fee amount. N/A (not filing).

Step 5 — Due date. N/A.

**Output.** Marcus does not file Form IT-204-LL for 2025 and does not pay the $25. The reviewer brief notes:
- Prior-year filings (2023 and 2024) were correctly filed because the LLC was formed in 2023 and may have had trivial activity that year; if 2024 was truly dormant the $25 was technically unnecessary but non-refundable now
- Marcus should either (a) dissolve the LLC with NY DOS to end future compliance obligations permanently, or (b) keep it dormant and monitor annually; he must re-file IT-204-LL in any future year where he has even $1 of activity
- The skill strongly recommends dissolution if Marcus has no plans to use the LLC, because the ongoing non-tax compliance burden (NY DOS biennial statement, liability insurance if applicable, separate checking account maintenance fees) exceeds the benefit of keeping an inactive entity

**Primary source.** NY Tax Law §658(c)(1); Form IT-204-LL Instructions (2025), "Who is not required to file"; NY Publication 16.

### Example 3 — Ambiguous activity (auto-debited state maintenance fees only)

**Facts.** Priya formed Priya Labs LLC in NY in 2022. She used it heavily in 2022 and 2023 but pivoted to a W-2 job in early 2024. For 2025 she thought the LLC was dormant. On closer inspection: the LLC's Mercury business checking account was never closed, and in 2025 it had (a) $18 in interest credits across the year, (b) $9 in monthly bank fees across two months before the fees stopped when the account balance was depleted, and (c) a $9 auto-debit for the NY DOS biennial statement fee in March 2025. Net account balance went from $50 to $14. No client activity, no invoices, no contracts.

**Reasoning.**

Step 1 — Classification. Disregarded SMLLC. In scope.

Step 2 — Residency. NY full-year resident. In scope.

Step 3 — NY source activity (Position 5.3). This is the ambiguous case. Technical reading:
- $18 of interest income: YES, this is NY source income to a resident under §612
- $18 of bank fees: YES, this is NY source deduction (business expense)
- $9 DOS biennial fee: YES, this is NY source deduction (state entity maintenance expense)

Any one of these three triggers the filing obligation under §658(c)(1). The dormancy exception does NOT apply because there is positive income and positive deductions, even though they sum to a trivial net. Filing is required.

Step 4 — Fee amount. $25 flat regardless of how small the underlying activity is.

Step 5 — Due date. March 16, 2026.

**Output.** File IT-204-LL by March 16, 2026 with $25 payment. Reviewer brief notes:
- The dormancy exception was tested and does NOT apply because of bank interest and bank fees
- This is the conservative position per Section 6 defaults
- Priya should close the Mercury account immediately to stop the activity trail and qualify for the dormancy exception for 2026
- If Priya wants to dissolve the LLC, she should do so via NY DOS and the 2026 return would be the final short-period return

**Primary source.** NY Tax Law §658(c)(1); §612; Form IT-204-LL Instructions (2025), "Who must file."

### Example 4 — LLC with NYC activity (cross-reference trigger)

**Facts.** David is a freelance iOS developer, age 41, full-year NYC resident (lives in Manhattan), single. He formed DevShop NYC LLC in 2024 to run his consulting. For 2025 the LLC had $240,000 in gross receipts (all from two clients, both based outside NY state — one in San Francisco, one in Austin). He paid $11,000 in business expenses through the LLC. He works from his home office in Manhattan. He has never filed Form 8832. Plans to file Form IT-201 as NYC resident.

**Reasoning.**

Step 1 — Classification. Disregarded SMLLC. In scope.

Step 2 — Residency. NYC full-year resident, which is a subset of NY full-year resident. In scope.

Step 3 — NY source activity. $240,000 receipts plus $11,000 expenses, all NY source because David is a NY resident. Filing required.

Step 4 — Fee amount. $25 flat.

Step 5 — Due date. March 16, 2026.

**Cross-reference trigger (Section 8 reviewer attention).** David's LLC has NYC nexus (the Manhattan home office). His unincorporated business gross income exceeds $95,000. This triggers a separate obligation: NYC Unincorporated Business Tax (UBT) via Form NYC-202 or NYC-202S, filed with the NYC Department of Finance, computed at 4% of unincorporated business taxable income with a small-taxpayer credit phaseout between $3,401 and $5,400 of UBT liability. This skill handles only the state IT-204-LL filing. David's UBT obligation must be routed to `nyc-unincorporated-business-tax`.

**Output.** File IT-204-LL by March 16, 2026 with $25 payment. Reviewer brief includes a **prominent cross-reference flag** directing the reviewer to verify that the NYC UBT analysis has been completed by the `nyc-unincorporated-business-tax` skill. The IT-204-LL $25 and the NYC UBT liability are independent filings with independent due dates (UBT is due April 15).

**Primary source.** NY Tax Law §658(c)(1); §612; NYC Admin Code §11-502 and §11-514 (for the cross-reference).

### Example 5 — First-year LLC, formed mid-year, immediate activity

**Facts.** Elena is a freelance data engineer, married filing jointly with her spouse Luis (also a NY resident), full-year NY resident, living in Westchester County. She was a bare sole prop in 2024. On September 1, 2025, she registered Elena Data LLC with NY DOS. From September 1 through December 31, 2025, the LLC received $75,000 in client payments. Prior to September 1, the same client work was billed through her personal name (sole prop). She has an EIN for the LLC, assigned by the IRS in September 2025. She files IT-201 as MFJ.

**Reasoning.**

Step 1 — Classification. Disregarded SMLLC. In scope.

Step 2 — Residency. NY full-year resident. In scope.

Step 3 — NY source activity (Position 5.3). $75,000 in LLC receipts from September through December 2025. NY source activity clearly present. Filing required.

Step 4 — Fee amount (Position 5.4). **$25 flat. No proration** for the short first year. Even though the LLC only existed for four months, the full $25 applies. Per Form IT-204-LL Instructions (2025): "There is no proration of the filing fee if the LLC, LLP, or partnership has a short tax year for federal tax purposes."

Step 5 — Due date (Position 5.5). March 16, 2026.

**Reviewer attention triggers (Section 8).** First-year LLC. Verify all Part 1 fields carefully: legal name matches NY DOS records exactly, DOS file number is correct, formation date is correct, EIN is correct, principal business activity description is accurate (e.g., "computer systems design and related services," NAICS 541511).

**Schedule C coordination note for the brief.** Elena's 2025 federal Schedule C reports business activity for the full year. For the period January through August, the business was a bare sole prop (her personal name). From September through December, the business operated through the LLC (but is still reported on Schedule C because the LLC is disregarded). The Schedule C is one continuous report, not two; the LLC formation does not trigger any federal cut-off. This is a common source of confusion and should be noted in the reviewer brief.

**Output.** File Form IT-204-LL by March 16, 2026 with $25 payment. Reviewer brief includes the first-year attention flags, the short-period-no-proration note, and the Schedule C coordination note.

**Primary source.** NY Tax Law §658(c)(1); Form IT-204-LL Instructions (2025), Line 7 and "Period covered"; Treas. Reg. §301.7701-3(b)(1)(ii).

---

## Section 10 — Output format extensions

This skill extends the standard reviewer brief template from `us-tax-workflow-base` Section 3 with one additional section: **"NY LLC Filing Fee Determination."**

The section appears in the brief after "Bottom line" and before "High flags." It contains:

```markdown
## NY LLC Filing Fee Determination

**Entity:** [LLC legal name]
**NY DOS file number:** [number] (or "not yet provided — see reviewer flags")
**Entity classification:** Single-member LLC, disregarded for federal tax under Treas. Reg. §301.7701-3(b)(1)(ii)
**Member:** [owner name], New York State full-year resident for 2025
**NY source activity determination:** [one-sentence explanation of activity that triggered filing, OR dormancy exception rationale]

**Filing required:** [Yes / No]

**If Yes:**
- Fee amount: $25 (flat, NY Tax Law §658(c)(1))
- Due date: March 16, 2026 (March 15 falls on a Sunday; shifted under NY Tax Law §171)
- No extension available: Confirmed per Form IT-204-LL Instructions (2025), "No extension of time"
- Payment method: Check payable to "NYS filing fee" OR electronic filing via NYS-approved software
- Filed separately from Form IT-201: Yes — do not attach to personal return

**If No (dormancy exception):**
- Basis: [one-sentence rationale]
- Verified that LLC had zero income, zero gain, zero loss, zero deduction from NY sources in 2025
- Reviewer should confirm no bank interest, no state entity maintenance fees, no depreciation from dormant assets
- Recommendation: [dissolve the LLC via NY DOS / keep dormant and monitor annually]

**Cross-references:**
- [If NYC nexus present] NYC Unincorporated Business Tax: route to `nyc-unincorporated-business-tax` skill
- [If first-year LLC] Verify all Part 1 fields match NY DOS records
- [If dissolution planned] Flag current year as potential final return
```

The rest of the brief follows the base template (computation trail, conservative defaults applied, refusal trace, scope limitations, disclaimers).

**Working paper.** This skill does not produce an Excel working paper. The filing is too simple (one number, one form) to justify a workbook. The reviewer brief and the completed Form IT-204-LL worksheet are the complete deliverables.

**Chat response extension.** The chat response for this skill includes one additional element: the explicit March 16, 2026 due date with the "NO extension available" reminder, because this is the single most common trap for freelancers.

---

## Section 11 — Intake form additions

These questions extend the base intake. They are asked only if the base intake did not already capture the information. Use `ask_user_input_v0` where possible.

**NY204-1.** (Single-select, blocking) Does the freelancer operate through a single-member LLC?
- Options: "Yes — single-member LLC" / "No — bare sole prop" / "Multi-member LLC" / "S-corp or C-corp"
- Blocking: "Multi-member LLC" → R-NY204-1. "S-corp or C-corp" → R-NY204-2. "Bare sole prop" → skip this skill entirely.

**NY204-2.** (Single-select, blocking) Has the LLC filed Form 8832 (electing corporate treatment) or Form 2553 (electing S-corp treatment)?
- Options: "No" / "Yes — Form 8832" / "Yes — Form 2553" / "Not sure"
- Blocking: "Yes" to either → R-NY204-2. "Not sure" → ask follow-up: "Have you ever received a K-1, W-2 from your own LLC, or filed Form 1120 or 1120-S?"

**NY204-3.** (Free text) What is the LLC's legal name exactly as it appears in the NY DOS filing?

**NY204-4.** (Free text) What is the NY DOS file number for the LLC? (If unknown, flag for lookup via the NY DOS Corporation and Business Entity Database before filing.)

**NY204-5.** (Free text) What is the LLC's formation date? (Date on the Articles of Organization.)

**NY204-6.** (Single-select) Does the LLC have its own EIN?
- Options: "Yes" / "No — uses owner's SSN"
- If Yes, collect the EIN.

**NY204-7.** (Single-select, blocking) Was the LLC's sole member a New York State full-year resident for all of 2025?
- Options: "Yes, full year" / "Moved into NY during 2025" / "Moved out of NY during 2025" / "Never lived in NY in 2025"
- Blocking: Anything other than "Yes, full year" → R-NY204-3.

**NY204-8.** (Multi-select) In 2025, did the LLC have any of the following? (Check all that apply.)
- Options: "Client payments received" / "Business expenses paid through the LLC" / "Bank interest earned" / "State DOS fees paid from the LLC account" / "Depreciable assets owned by the LLC" / "None of the above"
- If "None of the above" is selected exclusively: dormancy exception applies, no filing required. Proceed to Example 2 path.
- If any other option is selected: filing required. Proceed to Example 1, 3, 4, or 5 path.

**NY204-9.** (Single-select) Was Form IT-204-LL filed for the 2024 tax year?
- Options: "Yes, filed and paid" / "No — I didn't know this was required" / "No — the LLC was dormant in 2024" / "LLC didn't exist in 2024"
- "No — I didn't know" triggers reviewer attention flag for prior-year compliance gap.

**NY204-10.** (Single-select) Does the LLC operate from or have any activity in New York City (the five boroughs)?
- Options: "Yes — NYC home office" / "Yes — NYC clients but home office outside NYC" / "No — no NYC activity"
- "Yes — NYC home office" → cross-reference flag to `nyc-unincorporated-business-tax`.

---

## Section 12 — Self-check additions

These self-checks extend the seventeen base checks in `us-tax-workflow-base` Section 5. They start at Check 18 to avoid collision with the base numbering.

**Check 18 — Entity classification gate cleared.** Position 5.1 executed; LLC confirmed as single-member disregarded; no Form 8832 or Form 2553 election. If ambiguous, R-NY204-1 or R-NY204-2 fired.

**Check 19 — Owner residency gate cleared.** Position 5.2 executed; owner confirmed as NY full-year resident. If ambiguous, R-NY204-3 fired.

**Check 20 — NY source activity determination documented.** Position 5.3 executed; the skill states explicitly whether the LLC had activity in 2025 and, if so, what kind. The dormancy exception was tested and the result is in the brief.

**Check 21 — Fee amount is exactly $25 or $0.** Position 5.4 allows no other value. Any computation returning anything else is an error. If $0 (dormancy), the brief states dormancy exception applies; if $25, the brief states Position 5.4 applies.

**Check 22 — Due date is March 16, 2026 for calendar-year 2025.** Not April 15. Not March 15. March 16. The Sunday shift under NY Tax Law §171 has been applied. If the brief states anything else, the check fails.

**Check 23 — "No extension available" stated verbatim in the brief.** The reviewer brief explicitly states that Form IT-204-LL has no extension of time to file, and that filing Form IT-370 to extend the owner's Form IT-201 does not extend this form. If the brief does not contain this verbatim warning, the check fails and the warning is added.

**Check 24 — Payment instruction includes "NYS filing fee" as payee.** Not "New York State" or "NYSDTF" or "NYS Income Tax." The correct payee is "NYS filing fee" per the Form IT-204-LL Instructions (2025). If the brief names a different payee, the check fails.

**Check 25 — Federal Schedule C deductibility is not claimed.** Position 5.7 default is non-deductible unless the reviewer affirmatively claims it. If the brief claims the $25 as a Schedule C deduction without reviewer affirmation, the check fails.

**Check 26 — NYC cross-reference fired if applicable.** If the intake indicates NYC activity (NY204-10 = "Yes — NYC home office"), the reviewer brief contains a prominent cross-reference flag to `nyc-unincorporated-business-tax`. If the flag is missing, the check fails.

**Check 27 — Refusal trace includes all 10 R-NY204 codes.** The refusal trace in the brief lists R-NY204-1 through R-NY204-10 with a one-sentence cleared-or-fired note for each. This is in addition to the 18 base R-US codes from `us-tax-workflow-base` Section 6.

---

## Section 13 — Cross-skill references

**Inputs from intake skill** (either `us-ca-freelance-intake` with NY extension, or a future `us-ny-freelance-intake`, or a future state-agnostic intake):
- Owner identifying information (name, SSN, address, filing status)
- Owner residency confirmation (must be NY full-year)
- Entity structure (must be disregarded SMLLC)
- LLC legal name, NY DOS file number, formation date, EIN if any
- 2024 IT-204-LL filing status (for prior-year compliance check)

**Inputs from `us-sole-prop-bookkeeping`:**
- Confirmation of whether the LLC had any 2025 activity (the dormancy test)
- Categorized transactions (for verifying bank interest, state fees, and other activity markers)

**Inputs from `ny-it-201-resident-return`:**
- Owner residency confirmation (must match this skill's Position 5.2)
- NYC vs. non-NYC residency within NY state (for the UBT cross-reference trigger)

**Outputs to `us-federal-ny-return-assembly` orchestrator:**
- Completed Form IT-204-LL worksheet (or "not required — dormancy" determination)
- $25 payment instruction (if required) with the March 16, 2026 due date
- Reviewer brief section per Section 10 above
- Taxpayer action list entry: "File IT-204-LL and pay $25 by March 16, 2026 — separate from personal return, cannot be extended"
- Any reviewer attention flags from Section 8

**Outputs to `nyc-unincorporated-business-tax` skill (cross-reference only, not data flow):**
- Trigger flag if LLC has NYC nexus
- This skill does NOT compute or estimate UBT; that is the UBT skill's job

**Does NOT interact with:**
- `us-self-employed-retirement` (retirement is at the owner level, not the LLC level)
- `us-self-employed-health-insurance` (health insurance is at the owner level)
- `us-qbi-deduction` (QBI is computed at the owner level; disregarded LLC is transparent)
- `us-quarterly-estimated-tax` (federal estimated tax is at the owner level)
- `ny-estimated-tax-it-2105` (NY estimated tax is at the owner level)

The LLC-level filing is genuinely isolated from all the owner-level tax mechanics. This is deliberate and reflects the disregarded entity's tax-transparent status for federal income tax while maintaining separate compliance obligations with NY state.

---

## Section 14 — Reference material and change log

### Why this skill exists

New York is one of a small number of states that impose a separate filing fee on disregarded SMLLCs even though federal tax treats them as transparent. Many freelance developers who form an LLC through LegalZoom, ZenBusiness, or similar services have no idea this obligation exists. The first they hear of it is when NYSDTF sends a notice for a missed filing, or when a diligence review of their business surfaces the non-filing. The skill exists to catch this trap early and handle it mechanically.

The $25 is trivial. The compliance record is not. A freelancer with three years of unfiled IT-204-LL is a reviewer's problem to untangle — not because of the dollar amount, but because of the pattern.

### What this skill does not do

- It does not advise on whether to form an LLC at all (entity-choice decision)
- It does not handle the NY LLC publication requirement (newly formed LLCs must publish in two newspapers in their county of organization within 120 days; that's a NY DOS obligation, not a tax obligation, and failure to publish can suspend the LLC's ability to bring lawsuits)
- It does not handle the NY DOS biennial statement (every two years, separate filing, separate small fee)
- It does not handle LLC dissolution filings with NY DOS
- It does not compute the NY state personal income tax flowing from the LLC's activity — that is `ny-it-201-resident-return`'s job
- It does not compute NYC UBT — that is `nyc-unincorporated-business-tax`'s job
- It does not handle partnership-taxed LLCs, corporate-taxed LLCs, or any entity classification other than disregarded single-member

### Design notes

This skill is the smallest file in the NY stack. It was built first (before `ny-it-201-resident-return`, which is the load-bearing file) to validate the Tier 2 content skill slot contract pattern cheaply. Lessons carried forward to the IT-201 skill:

1. The slot contract produces a longer file than the CA 568 pattern, but the resulting skill is materially more auditable, more maintainable, and easier for a reviewer to verify
2. Worked examples (slot 9) are the single highest-value section — they anchor all the prose rules to concrete fact patterns a reviewer can recognize
3. The year-specific figures table (slot 3) is valuable even for a skill with one figure — it gives updaters a single place to change values when tax law changes
4. The reviewer attention thresholds section (slot 8) does not have to use dollar thresholds; for flat-fee skills, condition-based triggers work just as well

### Change log

- **v0.1 (April 2026):** Initial draft matching the `ca-smllc-form-568` pattern. Approximately 368 lines. Non-conformant with `us-tax-workflow-base` Section 7 slot contract (missing year-specific figures table, missing primary source library structure, missing worked examples, missing reviewer attention thresholds, missing structured position rules).
- **v0.2 (April 2026):** Rewrite to strict slot contract conformance. Restructured into 14 sections mapping to the 13 mandatory slots and 1 optional slot (cross-skill references). Added structured year-specific figures table, primary source library with governance descriptions, seven structured position rules, thirteen-row conservative defaults table, ten topical refusals in trigger/output format, ten-row reviewer attention thresholds, five worked examples covering common fact patterns, output format extension for the brief, ten-question intake additions with blocking logic, ten self-check additions numbered 18-27 to avoid collision with base checks 1-17. Currency date: April 2026. All figures verified against tax.ny.gov primary sources during a deep research pass preceding this draft.

## End of NY IT-204-LL SMLLC Filing Fee Skill v0.2


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
