---
name: au-objections
description: >
  Use this guide to prepare an objection to an ATO assessment or decision under
  Part IVC of the Taxation Administration Act 1953, on the law at 2 November 2026
  (2026-27), for individuals, sole traders, companies, trusts, partnerships and
  super funds. Covers the objection right, section 14ZW periods by decision and
  taxpayer type, amended assessments, late objection requests under sections 14ZW
  and 14ZX, grounds and the burden of proof, disputed debts, and review by the
  Administrative Review Tribunal or appeal to the Federal Court. Trigger on
  'objection', 'late objection', 'extension of time to object', 'Part IVC',
  'ART review' or 'disputed debt'.
jurisdiction: AU
category: international
tax_year: 2026
tax_year_notes: "2026-27 (law as at 2 November 2026)"
tier: 2
last_updated: 2026-11-11
version: 0.1
review_status: pending_review
depends_on:
  - workflow-base
verified_by: pending
license: FSL-1.1-ALv2
---

# Australian Objections to ATO Decisions v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

This guide prepares a federal taxation objection under Part IVC of the *Taxation Administration Act 1953* (TAA) for a registered tax agent to review, sign and lodge. Part IVC applies only where another provision says that a dissatisfied person may object in the manner it sets out (TAA s 14ZL). The law is TAA compilation 227 (C2026C00468, in force from 1 October 2026), read on 2 November 2026.

**Covered:** whether a decision can be objected to; the objection period under s 14ZW for the common decision types, including amended assessments, penalty assessments and private rulings; limits on grounds (ss 14ZV, 14ZVA); the request to treat a late objection as lodged in time (ss 14ZW(2)-(3), 14ZX, PS LA 2003/7); grounds, evidence and the burden of proof (ss 14ZU, 14ZZK, 14ZZO); payment whilst the dispute runs (ss 14ZZM, 14ZZR, PS LA 2011/4); and the objection decision, deemed disallowance, review by the Administrative Review Tribunal (ART) and appeal to the Federal Court (ss 14ZY to 14ZZN). The taxpayer can be an individual, sole trader, company, trust, partnership or super fund.

**Not covered, and where it goes:**

- Correcting the taxpayer's own mistake by amendment request, and the section 170 amendment periods: `au-amending-individual-income-tax-return-period` for individuals; business routes in `au-lodgment-deadlines-penalties` Section 10.
- Penalty and interest amounts, GIC and SIC rates, penalty units and remission requests: `au-lodgment-deadlines-penalties`.
- Applying for a private ruling and its 60-day delay notice: `au-private-rulings`. This guide holds the period for objecting against a ruling.
- Director penalty notices: `au-director-penalties` (Division 269 of Schedule 1 contains no objection provision; the ATO describes a defence route instead).
- State and territory taxes, which follow each jurisdiction's own Act and revenue office: `au-land-tax` (Section 8 objection table) and `au-stamp-duty`.
- Division 7A assessments raised on the pre-*Bendel* view of unpaid present entitlements: `au-div7a` Rule 11. R&D amendment and objection windows: `au-rd-incentive`. Transfer pricing determinations: `australia-transfer-pricing`. The super guarantee charge computation: `au-super-guarantee`.
- Conducting ART or court proceedings, settlement and litigation strategy (refusal R-AU-OBJ-1).

## Ask the client first

1. Every notice for the period and matter in dispute: original assessment or decision, each amended notice, penalty assessments and the objection decision if one exists. For each: the issue date, how it was sent (online services, email, post) and any evidence of when it was received.
2. The taxpayer's type and, for income tax, the facts that decide which item of the s 170(1) table applies: individual, company or trustee; whether a business was carried on; small or medium business entity status for the year; any partnership or trust interests.
3. The result the taxpayer contends for, item by item, with the documents behind each point.
4. Earlier amendments, objections, private rulings, audit or review correspondence for the same matter (these can limit grounds).
5. The ATO account statement for the liability, payments made, any payment plan and any recovery action already taken.
6. If the period may have ended: when the taxpayer first disagreed, whether and how it told the ATO, what caused the delay and whether an adviser was involved.
7. The agent's authority to act for the taxpayer.

## The method, step by step

### Key figures

Every figure below was read on 2 November 2026. 'TAA' means TAA compilation 227; full URLs are in Sources.

| Item | Value | Source |
| --- | --- | --- |
| Income tax assessment, where s 170(1) item 1, 2, 3 or 3A applies | 2 years after notice of the assessment is given | TAA s 14ZW(1)(aa)(i) |
| Income tax assessment, otherwise | 4 years after notice of the assessment is given | TAA s 14ZW(1)(aa)(ii) |
| Who is in the 2-year group (ATO summary) | Most individuals, small businesses and medium businesses; medium business means aggregated turnover of at least $10 million but less than $50 million, for income years starting on or after 1 July 2021 | ATO, What you can object to, and the time limits (last updated 3 July 2026); ITAA 1936 s 170(1) items 1 to 3A and the 'medium business entity' definition in s 170(14) |
| FBT assessment (FBTAA s 78A) | 4 years after notice of the decision is given | TAA s 14ZW(1)(aaa) |
| Amended assessment where the 2-year rule would apply | Whichever ends last: 2 years after notice of the assessment that was amended was served, or 60 days after notice of the amended assessment was served | TAA s 14ZW(1BA) |
| Amended assessment where a 4-year rule would apply | Whichever ends last: 4 years after notice of the assessment that was amended was served (the first assessment for the year if amended more than once), or 60 days after notice of the amended assessment was served | TAA s 14ZW(1B), (1C) |
| Penalty assessment under Division 284 relating to an assessment of the person | 60 days, or the longer period for objecting to that assessment if there is one | TAA s 14ZW(1BB), (1)(c) |
| GST and other indirect tax assessment under Subdivision 155-C | The period in Sch 1 s 155-35(2)(a); the ATO states it as 4 years and one day from the date the assessment was given | TAA s 14ZW(1)(bg); ATO time limits page |
| Private ruling relating to an income year (not indirect tax or excise) | Whichever ends last: 60 days after the ruling was made, or 2 years (2-year group) or 4 years (otherwise) after the last day allowed for lodging the return for that year | TAA s 14ZW(1A) |
| Private indirect tax ruling | Whichever ends last: 60 days after the ruling was made, or 4 years after the last day allowed for lodging the return for the assessment to which it relates | TAA s 14ZW(1AAC) |
| Any other case | 60 days after notice of the decision is served | TAA s 14ZW(1)(c) |
| When a posted notice counts as given (ATO practice) | Currently 7 business days from the date it was issued through Australia Post | ATO time limits page; *Acts Interpretation Act 1901* s 29 (posted service is taken to occur when the letter would be delivered in the ordinary course of post, unless the contrary is proved) |
| Commissioner's decision period before the taxpayer can require one | 60 days after lodgment (or after the s 14ZX agreement), extended to 60 days after receipt of information requested within that period | TAA s 14ZYA(1) |
| Deemed disallowance | 60 days after the taxpayer gives notice requiring a decision | TAA s 14ZYA(3) |
| Applying to the ART for review of an objection decision | Within 60 days after being served with notice of the decision | TAA s 14ZZC(1) |
| Appeal to the Federal Court | Within 60 days after being served with notice of the decision | TAA s 14ZZN |
| Counting 'after' a day; weekend or holiday last day | The day named is excluded; a last day on a Saturday, Sunday or holiday moves to the next day that is none of those | *Acts Interpretation Act 1901* s 36(1) item 6, s 36(2) |
| Disputed-debt 50:50 arrangement | Pay all undisputed debts and at least 50% of the disputed principal tax debt; the ATO defers recovery of the balance and remits 50% of the GIC on it (75% for a Test Case Litigation Program dispute). Subject to a risk assessment; not available for an SGC debt, a diverted profits tax assessment, an objection the decision-maker considers frivolous or without merit, or where it would disadvantage the revenue | PS LA 2011/4 paras 25, 27, 28, 33, 38 |

The ATO page lists further decisions with other periods, including 21 days for some superannuation regulatory decisions and 6 months for disputed excise liabilities. Read that page and the enabling provision for any decision not in this table.

### Step 1: Confirm the decision can be objected to

Record the decision's type, date, period, amount and the provision under which it was made. Find the provision that gives the objection right: for an income tax assessment it is ITAA 1936 s 175A(1). Under s 175A(2) a taxpayer cannot object against an assessment of no taxable income, or of taxable income with no tax payable, unless it seeks an increase in its liability or its tax offset refunds (s 175A(3)). For any other decision, find the objection provision in the Act under which it was made. If none is found, record the decision as not shown to be objectable and list the alternatives for the agent (refusal R-AU-OBJ-3).

Separate a correction from a dispute. Where a late objection is lodged without a written request but within the amendment period, and the claim is reasonable and likely to be allowed in full, the ATO treats it as an amendment request (PS LA 2003/7 para 8). Route a simple correction to the amendment guides.

### Step 2: Build the notice chain

List every notice with its issue date, channel and the evidence of when it was given or served. Section 14ZW uses 'given' for some periods and 'served' for others; record which applies. Where the date of giving is unsupported, show the period end under each date the evidence allows and mark the timing `UNVERIFIED`. Do not label the objection in time or late: the registered tax agent decides.

### Step 3: Work out the period

Select the row in Key figures from the provision found in Step 1 and the s 170(1) item facts from intake. For an amended assessment, apply s 14ZV first: the right is limited to the alterations or additions and the matters relating to them. An earlier objection against a private ruling or a listed determination on the same matter limits later grounds to those that were not, and could not have been, grounds for that objection (s 14ZVA). Count with the *Acts Interpretation Act 1901* s 36 rules and show the arithmetic.

### Step 4: Draft the late objection request if needed

If the period may have passed, draft the written request that s 14ZW(2) requires to be lodged with the objection. It must state fully and in detail the circumstances concerning, and the reasons for, the failure to lodge in time (s 14ZW(3)). The ATO cannot consider a request until the objection itself is lodged (PS LA 2003/7 para 7).

Map the facts to the PS LA 2003/7 para 10 factors, with evidence for each: whether the objection and request were lodged as soon as circumstances permitted; the explanation; the length of the delay; whether the taxpayer kept the ATO informed that it disagreed; any negligent failure by an adviser to follow instructions; whether the taxpayer was told it could object; whether there is an arguable case; prejudice to the Commissioner; and any intent to let a review period expire. Para 11 lists cases where an extension would generally be allowed, including an individual or small business with a 2-year time limit that lodges, within 4 years, an objection disclosing an arguable case; para 12 lists cases where it normally would not.

The Commissioner decides the request and gives written notice (s 14ZX(1)-(2)). If it is agreed, the objection is taken to have been lodged in time (s 14ZX(3)); a refusal can be reviewed by the ART (s 14ZX(4)). Whether to make the request, alone or in the alternative to an in-time position, is the agent's decision.

### Step 5: Draft the grounds

An objection must be in the approved form, lodged within the s 14ZW period and state fully and in detail the grounds relied on (s 14ZU). The ATO asks for full details of the decision, including the year or period, and the reasons supported by documents (ATO, What to include in your objection); a tax agent lodges through the ATO's objection form for tax professionals (ATO, Complete and lodge your objection; no fee). Number each ground and give: the item disputed, the result as decided, the result contended for, the facts, the provision and the authority.

On ART review or a court appeal the taxpayer is limited to the grounds in the objection unless the ART or court orders otherwise, and must prove that an assessment is excessive or otherwise incorrect and what it should have been, or for another decision that it should not have been made or should have been made differently (ss 14ZZK, 14ZZO). List alternative grounds for the agent to consider so they are not lost.

### Step 6: Tie evidence to each ground

Build a schedule: document, the fact it proves, its source and whether it is held. A ground that depends on a fact with no supporting document is marked `UNSUPPORTED` and stays in the draft only with that flag and the evidence needed. Label a client's statement as a representation, not evidence. Supply no facts, figures or documents that the file does not contain.

### Step 7: Record the payment position

A pending ART review or court appeal does not affect the decision, and the amount may be recovered as if none were pending (ss 14ZZM(1), 14ZZR); for a small business taxation assessment decision the ART may stay it, subject to s 14ZZH (ss 14ZZB(6), 14ZZM(2)). The ATO can recover a disputed debt (PS LA 2011/4 para 2) and GIC keeps accruing (para 23). For straightforward, low-risk cases it does not take recovery action whilst an objection, review or appeal is on foot (para 22); large business and wealthy group taxpayers must pay in full or enter a 50:50 arrangement (para 6). A 50:50 arrangement is subject to a risk assessment (para 25) and is not available for a debt under the *Superannuation Guarantee (Administration) Act 1992* or a diverted profits tax assessment, amongst the para 38 exclusions; security does not satisfy it (para 31). Tie amounts due and paid to the account statement and route GIC rates, deductibility and remission to `au-lodgment-deadlines-penalties`.

### Step 8: Give the reviewer the later steps (information only)

- The Commissioner allows the objection in whole or part, or disallows it, and serves written notice (s 14ZY).
- If no decision is made within the s 14ZYA(1) period, the taxpayer may give written notice requiring one; 60 days later the objection is taken to be disallowed (s 14ZYA(2)-(3)).
- A dissatisfied taxpayer may apply to the ART or appeal to the Federal Court against a reviewable objection decision (s 14ZZ(1)(a)); the ART replaced the Administrative Appeals Tribunal from 14 October 2024 (ATO, Seek an external review of ATO decisions; TAA s 14ZQ defines ART as the Administrative Review Tribunal and the ART Act as the *Administrative Review Tribunal Act 2024*). The ART application must be in writing with a statement of reasons (s 14ZZC(2)-(3)), and the hearing is in private if the applicant asks (s 14ZZE).
- The ART may extend the period to apply under s 19 of the ART Act (note to s 14ZZC(1)). The period for applying to the ART against an extension-of-time refusal is not set by s 14ZZC(1), and s 14ZZB(2) disapplies the ART Act's general time rule: **Needs Input**, verify before advising.
- Complaints about ATO administration go to the Tax Ombudsman, separately from these review rights (ATO external review page).

### Permitted factual defaults

| Missing fact | Default | Disclose |
| --- | --- | --- |
| Date a notice was given or served | Use the earliest date the evidence supports to set the period end; show the alternatives | The timing is `UNVERIFIED` |
| Which s 170(1) item applies | Work to the 2-year period until the facts are confirmed | The 4-year period may be available |
| Whether the period has ended | Prepare the s 14ZW(2) request in the alternative | The agent decides whether to lodge it |
| A last day that falls on a weekend or holiday | Target the earlier calendar day; note the s 36(2) day | Holidays depend on the place of lodgment |

No default is permitted for the decision, its enabling provision, the grounds or the evidence. Return Needs Input for each.

### Working paper additions

Add to the base outputs: (1) the notice chain with period workings and timing status; (2) the objection provision and any limit on grounds; (3) the numbered grounds; (4) the evidence schedule; (5) any draft s 14ZW(2) request mapped to PS LA 2003/7 para 10; (6) the payment and charges note; and (7) a blank decision block for the agent.

## Worked cases

All facts are hypothetical. Day counts follow *Acts Interpretation Act 1901* s 36.

### Case 1: ART application after an objection decision served on 14 October 2026 (2026-27)

Notice of a disallowed objection was served on Wednesday 14 October 2026. Under s 14ZZC(1) the ART application is due within 60 days after service, so 14 October is excluded.

```oa-check
name: ART application period after an objection decision served on 14 October 2026 (2026-27)
inputs:
  served_day_of_october: 14
  days_in_october: 31
  days_in_november: 30
  period_days: 60
steps:
  - october_days_counted: days_in_october - served_day_of_october
  - through_november: october_days_counted + days_in_november
  - last_day_in_december: period_days - through_november
expected:
  october_days_counted: 17
  through_november: 47
  last_day_in_december: 13
```

Day 60 is Sunday 13 December 2026, so s 36(2) allows lodgment on Monday 14 December 2026 if that day is not a holiday in the place of lodgment. The conservative default targets Friday 11 December. The same count applies to a Federal Court appeal (s 14ZZN).

### Case 2: A 50:50 arrangement for a disputed debt (2026-27)

A company owes $6,000 of undisputed debt and disputes $84,000 of principal tax (penalties, SIC and GIC excluded from the principal). It is not a large business or wealthy group, the debt is not SGC or diverted profits tax, and the ATO's risk assessment allows the arrangement. The GIC that will accrue on the unpaid balance during the arrangement is stipulated at $2,400 for the example; actual GIC needs the daily rates in `au-lodgment-deadlines-penalties`.

```oa-check
name: 50:50 arrangement payment and GIC remission under PS LA 2011/4 (2026-27)
inputs:
  undisputed_debt: 6000
  disputed_principal: 84000
  minimum_share_percent: 50
  gic_on_unpaid_balance: 2400
  remission_percent: 50
  test_case_remission_percent: 75
steps:
  - minimum_disputed_payment: pct(disputed_principal, minimum_share_percent)
  - payment_to_enter: undisputed_debt + minimum_disputed_payment
  - deferred_balance: disputed_principal - minimum_disputed_payment
  - gic_remitted: pct(gic_on_unpaid_balance, remission_percent)
  - gic_payable: gic_on_unpaid_balance - gic_remitted
  - gic_remitted_test_case: pct(gic_on_unpaid_balance, test_case_remission_percent)
expected:
  minimum_disputed_payment: 42000
  payment_to_enter: 48000
  deferred_balance: 42000
  gic_remitted: 1200
  gic_payable: 1200
  gic_remitted_test_case: 1800
```

GIC runs at the full rate until the 50% payment and again from the 15th day after the objection decision or final tribunal or court decision (PS LA 2011/4 para 33). The remission applies only to GIC in between.

### Case 3: Earliest deemed disallowance after an information request (2026-27)

An objection is lodged in time on day 0. Within the first 60 days the Commissioner serves a notice requiring information, which the taxpayer supplies on day 75.

```oa-check
name: Earliest deemed disallowance under s 14ZYA after an information request (2026-27)
inputs:
  original_period_days: 60
  information_received_day: 75
  information_period_days: 60
  notice_period_days: 60
steps:
  - information_period_end_day: information_received_day + information_period_days
  - decision_window_end_day: max(original_period_days, information_period_end_day)
  - earliest_notice_day: decision_window_end_day + 1
  - deemed_disallowance_day: earliest_notice_day + notice_period_days
expected:
  information_period_end_day: 135
  decision_window_end_day: 135
  earliest_notice_day: 136
  deemed_disallowance_day: 196
```

A notice given before day 136 is premature. Whether and when a deemed decision starts the s 14ZZC or s 14ZZN period is not settled by the text read here: **Needs Input**.

### Case 4: Objecting to an amended assessment late in the 2-year period

An individual in the 2-year group was given notice of assessment on 30 September 2024. Within the 2 years that ITAA 1936 s 170(1) item 1 allows, the ATO amended one deduction by notice served on 25 September 2026. Under s 14ZW(1BA) the objection is due by whichever ends last: 2 years after the original notice (30 September 2026) or 60 days after the amended notice (24 November 2026), so 24 November 2026. Under s 14ZV the objection is limited to the amended deduction and matters relating to it; a ground on unrelated income needs a late objection request against the original assessment.

### Case 5: A late objection inside 4 years

A sole trader in the 2-year group missed the period by 9 months, has documents showing an arguable case and told the ATO by email before the period ended that she disagreed. Draft the s 14ZW(2) request mapping these facts to PS LA 2003/7 paras 10 and 11 (lodged within 4 years with an arguable case; the ATO was kept informed). Do not predict the outcome; the Commissioner decides under s 14ZX.

### Case 6: A nil assessment

A taxpayer assessed with a loss and no taxable income wants to object to increase the loss. Section 175A(2) bars an objection under s 175A(1) against an assessment of no taxable income unless the taxpayer seeks an increase in its liability or tax offset refunds (s 175A(3)); on that text a larger loss is neither. Record the assessment as not shown to be objectable under s 175A and ask the agent whether another provision or an amendment request applies (refusal R-AU-OBJ-3).

## When to refuse or refer

Stop the affected work where a fact, condition or source in this guide is unresolved, and return Needs Input or refer it for qualified review.

| Code | Trigger | Message (verbatim) |
| --- | --- | --- |
| R-AU-OBJ-1 | A request to run, plan or settle ART or court proceedings, or to negotiate with the ATO | 'I prepare the objection pack only. Proceedings, settlement and litigation strategy are for the agent and the taxpayer's lawyers.' |
| R-AU-OBJ-2 | A request to decide whether the objection is in time, whether to object or whether to seek an extension | 'Timing status and the decision to object or request an extension are for the registered tax agent and the taxpayer. The workings show each possible period end.' |
| R-AU-OBJ-3 | No objection provision found for the decision, or a statutory bar such as s 175A(2) | 'No objection right has been shown for this decision. The alternatives are listed for the agent to consider.' |
| R-AU-OBJ-4 | Fraud, evasion, a promoter penalty or a Part IVA determination is in issue | 'This dispute needs specialist and legal advice before any objection is drafted. Refer it.' |
| R-AU-OBJ-5 | A state or territory tax assessment | 'State and territory objections follow that jurisdiction's Act and revenue office, not Part IVC. Route to au-land-tax, au-stamp-duty or the relevant revenue office.' |

**Reviewer attention thresholds.** These are this guide's review settings, not statutory figures. Flag for reviewer attention regardless of confidence:

| Threshold | Why |
| --- | --- |
| Tax, penalty and interest in dispute of $25,000 or more | Grounds, evidence and payment strategy need senior review |
| Any late objection request | The request is refused or granted on its explanation and evidence |
| Any period end within 14 days, or any `UNVERIFIED` timing | A missed period can end the objection right |
| Any recovery action already started, or a large business or wealthy group taxpayer | Disputed-debt rules differ (PS LA 2011/4) |
| Any `UNSUPPORTED` ground | The burden of proof is on the taxpayer (ss 14ZZK, 14ZZO) |

**Prohibitions.** Never state an objection period from a generic figure without the provision. Never treat a pending objection as deferring payment. Never add facts or documents the file does not hold.

## Completion checklist

- [ ] The decision, its enabling objection provision and any s 175A(2), 14ZV or 14ZVA limit are recorded.
- [ ] Every notice has its issue date, channel and evidence of giving or service.
- [ ] The period row cites its s 14ZW paragraph, and the arithmetic follows the *Acts Interpretation Act 1901* s 36.
- [ ] Any late request states the circumstances and reasons in full and maps to PS LA 2003/7 para 10.
- [ ] Each ground gives the result contended for, the facts, the provision and the authority.
- [ ] Each ground traces to evidence or carries `UNSUPPORTED`.
- [ ] The payment position ties to the ATO account statement, and the disputed-debt options are noted.
- [ ] Penalties, interest, private ruling applications, director penalties and state taxes were routed.

Change log: v0.1 (2 November 2026), first draft from TAA Part IVC (compilation 227), ITAA 1936 ss 170 and 175A, PS LA 2003/7, PS LA 2011/4 and the ATO objection pages.

## Sources

All read on 2 November 2026; figures and dates rechecked against the same sources on 11 November 2026.

| Source | URL | Read on |
| --- | --- | --- |
| TAA 1953, compilation 227 (C2026C00468, from 1 October 2026), Volume 1: Part IVC, ss 14ZL to 14ZZS | https://www.legislation.gov.au/C1953A00001/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html | 2 November 2026 |
| ITAA 1936 s 175A (ATO legal database) | https://www.ato.gov.au/law/view/document?docid=PAC/19360027/175A | 2 November 2026 |
| ITAA 1936 s 170, items 1 to 4 and the 'medium business entity' definition (ATO legal database) | https://www.ato.gov.au/law/view/document?docid=PAC/19360027/170 | 2 November 2026 |
| *Acts Interpretation Act 1901*, compilation 39 (C2026C00117): ss 29 and 36 | https://www.legislation.gov.au/C1901A00002/2026-03-28/2026-03-28/text/original/epub/OEBPS/document_1/document_1.html | 2 November 2026 |
| ATO, What you can object to, and the time limits (QC107660, last updated 3 July 2026) | https://www.ato.gov.au/individuals-and-families/your-tax-return/if-you-disagree-with-an-ato-decision/object-to-a-decision/what-you-can-object-to-and-the-time-limits | 2 November 2026 |
| ATO, What to include in your objection (QC102388) | https://www.ato.gov.au/individuals-and-families/your-tax-return/if-you-disagree-with-an-ato-decision/object-to-a-decision/what-to-include-in-your-objection | 2 November 2026 |
| ATO, Complete and lodge your objection (QC33792, last updated 4 June 2026) | https://www.ato.gov.au/individuals-and-families/your-tax-return/if-you-disagree-with-an-ato-decision/object-to-a-decision/complete-and-lodge-your-objection | 2 November 2026 |
| ATO, Seek an external review of ATO decisions (QC33793, last updated 30 September 2025) | https://www.ato.gov.au/individuals-and-families/your-tax-return/if-you-disagree-with-an-ato-decision/seek-an-external-review-of-ato-decisions | 2 November 2026 |
| PS LA 2003/7, How to treat a request to lodge a late objection (amended 2 April 2026): paras 7, 8, 10 to 12, 15 | https://www.ato.gov.au/law/view/document?DocID=PSR/PS20037/NAT/ATO/00001&PiT=99991231235958 | 2 November 2026 |
| PS LA 2011/4, Collection and recovery of disputed debts: paras 2, 6, 22, 23, 25, 27, 28, 31, 33, 38 | https://www.ato.gov.au/law/view/document?docid=PSR/PS20114/NAT/ATO/00001 | 2 November 2026 |

Not yet confirmed: the period for applying to the ART against an extension-of-time refusal, and how a deemed disallowance interacts with the s 14ZZC and s 14ZZN periods (both Needs Input). Sch 1 s 155-35 was not reread for this draft; `au-lodgment-deadlines-penalties` holds it. No accountant has reviewed this draft.

Method adapted by its author from the `au-ato-objection` skill in ryanduguid/australian-accounting-skills (commit 3e110da). This guide is licensed under FSL-1.1-ALv2, not the OA Guide License; see LICENSING.md.

Topic chosen from the public Ask Nagaris skill list (names only); no Nagaris text was used.

Copyright 2026 Ryan Duguid. From github.com/ryanduguid/australian-accounting-skills, FSL-1.1-ALv2. Copies and adaptations of this file must keep this notice.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained in the
[ryanduguid/openaccountants fork](https://github.com/ryanduguid/openaccountants).
Check its quality tier, recorded review status and cited sources before use.
Choose a practitioner whose credentials and engagement scope you have verified.
The links below are optional upstream services; they do not publish or verify
this fork's changes.

- Upstream connection service: https://www.openaccountants.com/connect
- Upstream accountant network: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
