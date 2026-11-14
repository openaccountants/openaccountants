---
name: nz-company-ica-ir4j
description: "Use for an ordinary New Zealand resident company's imputation credit account reconciliation, original credit lots, ownership continuity, further income tax, imputation penalty tax and 2026 IR4J handoff. Trigger on ICA, imputation account, IR4J, credit continuity, year-end debit or further income tax. Primary annual examples cover 1 April 2025 to 31 March 2026. Refunds, transfers and later transactions require event-specific law. This component requires complete dated records and qualified review; it supplies no complete company return, unsupported special-branch computation or 2027 annual form mapping."
jurisdiction: NZ
category: international
tier: 2
review_status: pending_review
tax_year: 2026
tax_year_notes: "2025-26 ICA and IR4J2026; selected later events require their own operative dates; no annual 2027 form mapping"
last_updated: 2026-11-14
version: 0.2
depends_on:
  - workflow-base
  - corporate-income-tax-workflow-base
  - nz-company-income-tax-ir4
  - nz-company-dividend-rwt-core
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# New Zealand company ICA and IR4J v0.2

## Scope and source periods

Reconcile an eligible ordinary resident company's ICA from statutory events and original credit lots, then prepare its period-correct return and qualified-review handoff. ICA balance, income tax payable, cash available, shareholder credit entitlement and tax-loss continuity are separate results. A bank balance, incorporation record or journal label does not establish them. [OB1], [OB3], [OA3], [OA8].

Load both workflow bases and retain their intake, profile confirmation, source gates, refusal catalogues, computation order, ambiguity checkpoint, outputs and checks. This component supplements the [2025-26 IR4 guide](nz-company-income-tax-ir4.md) and [ordinary dividend/RWT guide](nz-company-dividend-rwt-core.md). Neither dependency is a verified 2027 return companion. Missing mandatory country content, sources or outputs prevents a complete company result.

The selected Income Tax Act consolidation is dated **4 September 2026** and Tax Administration Act consolidation **1 October 2026**, checked on **14 November 2026**. Selected bodies, histories and relevant clauses in their 14 distinct warning instruments were reviewed. This establishes the selected rules and date distinctions below, not whole-Act currency or all later law. Recheck the operative event period before use. [OB1], [TAA], [W03], [W07], [W10], [W11].

**IR4J2026** and April 2026 IR4JG cover **1 April 2025 to 31 March 2026**, regardless of accounting income year. The statutory ICA tax year is 1 April to 31 March. No 2027 annual form mapping is established. Original credit dates can precede the current year and must survive rollover. [YA1], [OA7], [IR4J2026], [IR4JG2026].

| Date-sensitive item | Required distinction |
| --- | --- |
| Ordinary paid-tax, dividend, continuity and year-end debit rules | Selected text/history supports the bounded 2025-26 examples with every stated condition |
| OB7BB top-up credit | Commences 1 January 2026; the ordinary credit catalogue is not exhaustive. Special computation requires complete authority. [W03] |
| Pooling transfer definition and related OB6/OB35 wording | Relevant additions commence 1 April 2025; pooling machinery and actual events remain separate. [W11], [OB6], [OB35], [YA1] |
| OB37(1C) R&D wording | Effective 1 April 2019; preserve RM15's differing 'refundable tax credit' wording. [W11], [OB37], [RM15] |
| RM10/RM13/RM17 references | Current RM2/RM4 wording begins 31 March 2026. An earlier balance year does not select law for a later refund request. Pre-change entitlement/refund chronology needs historical authority. [W07], [RM10], [RM13], [RM17] |
| YD2 foreign-company visitor exception | Starts 1 April 2026; YD1B, visit-start and treaty conditions remain if invoked. Do not import it into 2025-26. [YD2], [W07] |
| RP17B(2)(b) replacement | Starts 1 April 2026 and applies for 2026-27 and later income years; it cannot silently govern 2025-26 pooling. [RP17B], [W07] |
| LA5(2) TSWT exception | Starts 1 April 2026; obtain the period-specific branch if relevant. [LA5], [W11] |
| Ownership/look-through | Retrospective/application provisions can affect earlier lot periods. Current ownership alone is insufficient. [YC4], [YC11], [YC20], [W07], [W11] |

## Figures and filing/payment clocks

| Item | Rule and condition |
| --- | --- |
| Ordinary continuity | At least **66%** aggregate minimum voting interests throughout the credit period, plus at least **66%** minimum market-value interests where required. [OA8], [YC2], [YC3] |
| Annual ICA return | TAA69 generally links the deadline to the last date permitted under TAA37 for the income return. Establish the actual extension/route; the Australian no-income-return branch has its own July rule. [TAA], [IRD-annual] |
| Consolidated-member exception | TAA69(3) requires membership and nil individual ICA **at all times** during the year; nil closing alone is insufficient. [TAA] |
| Voluntary interim return | TAA70(3): period begins on the tax-year first day and ends no more than **7 days** before furnishing. [TAA], [IRD-interim] |
| Cessation return | TAA70(2): furnish within **2 calendar months** after the last day of ICA status for the statutory stub period. Liquidation/insolvency also engages corporate refusals. [TAA] |
| Specified retrospective pooling adjustment | TAA70(2B): revised return within **2 calendar months** of refund/transfer if its stated balance trigger is met. [TAA] |
| Ordinary year-end FIT | Nominal **20 June** following tax-year end, subject to OB65's exclusion and other applicable provisions. [OB65] |
| IPT | **10%** of qualifying FIT/additional tax under TAA140B; TAA142E supplies payment treatment. Do not apply it automatically to an unadjusted display balance. [TAA] |
| Working day/receipt | Apply actual statutory, channel and next-working-day conditions. Printed 20 June 2026 does not establish an overdue account balance. [IRD-pay], [IR4J2026], [TAA] |
| Reviewer attention floor | **NZ$0**, internal policy. Flag every non-zero difference including NZ$0.01, unquantified impact and status/source/date/continuity/notice/election/rounding condition. |

TAA70(1) permits a Commissioner-required return for its specified period and allowed time. A voluntary-interim rule does not replace a notice. Do not infer that a filing extension defers a separate payment duty. TAA37's 31 March 2026 publication amendment does not itself create a new ordinary deadline. [TAA], [W07].

TAA22(2)(k) memorandum-account/attached-credit records generally require at least **7 years** after the relevant tax or income-year end, with statutory conditions and a possible notified extension of up to **3 further years**. Retain the evidence needed to support original lots; this period is not a rule that an old unconsumed credit acquires a new date. [TAA].

## Intake, defaults and completion gates

Use redacted schedules and fictional or reviewer-held references. The professional retains legal identities, tax numbers, addresses, bank details, authentication/signing credentials and performs any authorised submission or payment. Establish both bases' authority-to-provide-data and qualified-review conditions.

Record requested obligation, ICA tax year/accounting income year, currency, balance date, entity/capacity, residence, status periods, industry, group/ownership structure, foreign establishments, notices/disputes and material positions. YD2's incorporation, head-office, management and director-control bases are alternatives; treaty/disputed residence needs its own analysis. Test OB1/OB2 and YA1 eligibility rather than assuming every company maintains an ordinary ICA. [YD2], [OB1], [OB2], [YA1].

Obtain and reconcile prior filed/revised/interim returns, opening sign/amount, tax-account allocations and original credit lots. Collect every payment/refund/transfer/distribution, its legal and book dates, source amount and statutory class. Obtain all persons' decision rights/interests throughout each lot period, ownership changes, options/fixed-rate securities, market-value circumstances, look-through relationships and any concession/arrangement. Establish assessment/refund chronology, applicable return/extension, earlier refunds/offsets, requests/notices/statements, elections, form/channel and actual delivery/payment evidence.

Infer and confirm both bases' profile before substantive computation. Every source item remains in the working paper, including excluded, disputed and held items. Unknown is not zero or inapplicable.

| Missing/conflicting condition | Permitted treatment |
| --- | --- |
| Entity, residence, ICA status or special profile | Needs Input; establish facts and operative rule before computing |
| Opening, original lots, ownership/market value | Hold continuity and affected closing/result; no date reset or stable-ownership assumption |
| Class, amount, legal date, entitlement/allocation | Preserve the item/impact as held; no unsupported date, cash or zero substitute |
| Notice, extension, election, revised return or law | Require actual evidence; a journal or practitioner engagement does not establish it |
| Rounding, zero-sign or field behaviour | No invented rounding/truncation/checkbox default; hold affected final representation |
| Submission, payment, recalculation or review | No completion assumption; identify evidence and responsible person |

These are T3 holds. This companion grants no new T2 missing-fact defaults or higher-tax default for unknown law. Use the bases' shared ambiguity checkpoint and prescribed T2 question/cash-impact ranking. If more than 10 grouped factual questions remain and no applicable loaded catalogue supplies the excessive-ambiguity code/message, retain Needs Input for that configuration gap; invent no code or deliverable result.

Run every applicable universal/R-CIT refusal first, retaining its exact canonical trigger/message/action. R-CIT-6 concerns a current audit or notice of deficiency. Disputed/dual residence, regulated funds and liquidation have separate triggers. An ordinary related-party relationship alone does not establish an audit trigger. Intake confirmation or a reviewer flag cannot override a fired refusal.

| Additional code | Trigger | Exact message |
| --- | --- | --- |
| R-NZ-ICA-SPECIAL | Requested computation requires an unsupported special entity, transaction, group, tax-pooling, historical or other ICA branch | This ICA companion cannot compute the requested special treatment. Establish its applicable primary sources, conditions and qualified review before continuing. |
| R-NZ-ICA-INCOMPLETE | A complete company or ICA result is requested whilst mandatory applicable content, source conditions or outputs remain unsupported | This ICA schedule is an incomplete corporate companion. Do not deliver a complete company result or mark the workflow complete. Establish every mandatory source condition, country slot and required output first. |

Follow a fired refusal's full stop; do not issue partial computed work through it. Record fired/cleared codes and exact messages in the brief, or the reply if refusal precedes a brief. A missing ordinary fact remains Needs Input unless a catalogue trigger actually applies.

## Corporate country requirements remain binding

| Required group | Contribution here and remaining requirement |
| --- | --- |
| Regime/authority/forms/calendar | Selected NZ ICA/IR4J2026; actual status, route, notices, extensions and all company obligations remain |
| Rates | Selected IPT/account conditions; complete headline/reduced/activity/branch rates and surcharges need period-appropriate companions |
| Adjustments | ICA postings only; full expense/exemption/depreciation/interest-limit reconciliation remains |
| Losses | ICA continuity does not establish loss availability, caps, carryback or group relief |
| Credits | Selected posting/refund/election bridge; underlying withholding/foreign/R&D/investment/other entitlements remain |
| Filing mechanics | Selected ICA duties; full company forms/documents/accounts/audit requirements remain |
| Anti-avoidance | GB34/arrangement gates supplement, without replacing, GAAR/CFC/hybrid/other corporate analysis |
| Pillar Two | Top-up credit existence is not a full domestic/IIR/UTPR applicability or computation conclusion |
| Cross-references | Load applicable income/dividend/withholding/transfer-pricing/MDR/IP/R&D/free-zone companions; missing authority is not inapplicability |

Retain all 4 universal outputs and every corporate domain output. A supported ICA schedule contributes to the package; missing mandatory slots, sources or outputs prevents a complete company financial result or workflow-completion claim.

## Reconcile the account mechanically

### Establish dates and signed balances

1. Establish eligibility/status for every relevant period and special/sector/consolidated/QC/Australian applicability before an ordinary model.
2. Reconcile opening to prior closing, using positive credit/negative debit in the working paper. Preserve original component dates/identities; rollover supplies no new credit date. [OA3], [OA7], [OA8].
3. Keep one row per source event with class, amount, source/legal/book/effective dates, provision, period, capacity and evidence/uncertainty. Tax-account and ICA dates are not interchangeable.
4. Identify every applicable credit/debit class; the common rows below are not exhaustive. Resolve unclassified events before certifying closing. [OA5], [OA6], [OB3].
5. Reconcile signed closing = signed opening + eligible credits − eligible debits, plus gross credit/debit totals and lot consumption. Net balance alone cannot prove completeness/continuity.

| Common event | Source/date control |
| --- | --- |
| Income/provisional tax paid | OB4 overriding exclusions; ordinary payment date and no double credit. Specified credited-tax payments and FIT application are excluded. [OB4] |
| Excess tax transferred | TAA173L/173M/RC32 machinery and express OB4/OB32 ICA dates, including request-year conditions, must all be met. Preserve tax-account and ICA dates. [OB4], [OB32], [RC32], [TAA] |
| RWT on interest | OB8 qualifying credit/withholding date and underlying RA9 evidence. [OB8], [RA9] |
| Attached credit received/paid | OB9/OB30 valid amounts/payment rules; DRCD can deem a different date. Declaration/journal date is no automatic substitute. [OB9], [OB30], [RA6] |
| Income-tax refund | OB32 debit with overrides/exceptions, distinct from underlying entitlement/actual refund. [OB32], [OB37] |
| Overpaid income tax used for other taxes | OB33 including pooling distinction; offset need not be cash refund. [OB33], [RM10], [TAA] |
| Refundable/R&D credit refund/transfer | OB37 dates/continuity after underlying eligibility; preserve differing RM15 wording. [OB37], [RM15], [LA5], [LA6] |
| Continuity loss | OA8/OB41 unused affected lots after correct consumption/exceptions. [OA8], [OB41] |
| Pooling, reversal, cessation or group movement | Complete OB5/6/25/34/35/54/56, OP2 and operative dependencies or stop under R-NZ-ICA-SPECIAL. [OB5], [OB6], [OB25], [OB34], [OB35], [OB54], [OB56], [OP2] |

OA6(1)'s published text contains a tax-pooling credit sentence under 'Debits' in HTML and the official PDF. Preserve publisher wording; it is not an extraction mismatch or permission to invent a posting. OB5/OB6 distinguish company-provided deposits/transfers; OB4(3)(a) prevents a second credit merely on transfer to a tax account. Period-correct RP17B/RP19 and intermediary records remain required. This guide does not compute pooling. [OA6], [OB4], [OB5], [OB6], [RP17B], [RP19].

OP2 concerns listed postings in a specified consolidated setting with exceptions, not every posting in every group. RC32 requires a wholly-owned group, actual overpayment/shortfall and timely notice naming recipient/amount/date, subject to RM13–17; express ICA dates remain distinct. [OP2], [RC32], [OB4], [OB32].

### Preserve lots and test continuity

For each lot determine its credit period and each person's minimum voting interest throughout, using statutory decision rights rather than cash ownership alone. Sum minima and test **66%**. If a market-value circumstance applies, separately test minimum market-value interests; voting alone is insufficient. Use YC2/YC3 and complete applicable YA1/YC machinery. [OA8], [YC2], [YC3], [YA1].

Corporate/partnership ownership can require YC4 look-through, YC11 overrides, YC10, associated-person and limited-attribution rules. YC20 modifies YC6 and excluded-option/market-value definitions for continuity. Unmodified YA1 alone is insufficient where those features arise. Retrospective changes can affect earlier lots; unsupported chains, options/securities, concessions/arrangements remain held. [YC4], [YC11], [YC20], [GB34], [YC15], [W07], [W11].

For continuity, consume oldest credits first and count each debit once. Debit unused failed lots, without debiting consumed credits, erasing later valid lots or resetting dates on 1 April. This is not a general intraday convention. Resolve facts/authority where same-day sequence changes a result. [OA7], [OA8], [OB41].

QC cessation under HA18/OA8(3B)/OB41(3B) differs from ordinary continuity loss. Member-fund, sector, group-transition and pre-1992 branches need separate conditions. Ordinary examples do not prove their inapplicability to an actual company. [HA18], [OA8], [OB41], [OB46].

### FIT, IPT and elected application

OB65 imposes year-end FIT for closing debit, disregarding the specified OB46 member-fund debit. Establish all applicable reductions/branches first; underlying member/master-fund expenditure rules are not ordinary defaults. [OB65], [OB46].

OB67(1)–(2B) requires previous and following year-end debits, total following-year credits **less than** the previous debit and notification to the Commissioner. In the qualifying case, reduction is previous debit less following-year credits; apply the statutory FIT adjustment. Reconcile inconsistent inputs; invent no clamp. Equality fails the strict comparison. The separate QC refund route in OB67(3)–(5) grants no general ordinary-company refund-based reduction. [OB67].

Gross IPT is **10%** of qualifying FIT/additional tax under TAA140B. Keep gross IPT, evidenced remission and net IPT separately, alongside FIT, other penalties, interest and cash. Original-due-date examples are not current overdue balances. TAA139B's specified incremental-penalty exception is not exemption from every initial penalty/interest. TAA181C remission has specified FIT/late-payment/overlap conditions; no blanket zero-interest or equivalent cessation relief is established. Emergency remission/actual overdue rates and periods need current authority. [TAA], [IR4JG2026], [IR274].

Before finalising net IPT, screen **TAA180** and establish its facts and Commissioner-satisfaction conditions. Its mandatory relief is limited to the established extent: an OB54 arrangement debit subsequently matched by an OB25 credit; a refund sent but not received, or not known to have been received, before year end; or the specified OB33/OP31/OZ3 debit not known in time to remove the balance. Section 180(2) also remits corresponding late-payment penalty on remitted IPT; section 180(3) adds the stated FIT late-penalty relief only for the arrangement ground in 180(1)(a). Preserve separate amounts and decisions. These grounds are not blanket interest relief. Unresolved facts or satisfaction conditions hold the affected net penalty result. TAA181C remains a separate provision with its own conditions. [TAA], [OB54], [OB25], [OB33].

An OB69 election can apply paid FIT to a qualifying income/provisional liability for an income year corresponding to ICA status. Preserve payment/election/liability/status evidence. OB69(4) treats the qualifying liability as paid on the FIT payment day. For its specified later-instalment purposes, RC35(1)–(3) allocates to the first provisional instalment payable after FIT payment, then later instalments in order, treating the applicable amount as provisional tax paid on its payable date for RC35's purposes. OB4(3)(g) supplies no extra ICA credit merely from that application. IPT is not FIT. RM17 concerns an obligation yet to arise, not a universal ban on all FIT refunds. [OB69], [RC35], [OB4], [RM17].

### Refund entitlement, cap, offset and cash

First establish substantive entitlement. RM2 distinguishes original/specified amended assessments from other amendments and their notice/satisfaction periods. RM4 concerns excess paid following an assessment increase with its own conditions. TAA108 is not a universal cash-refund deadline; TAA78B concerns specified LJ2/LK1 applications/discretionary extension, not an automatic six-year refund rule. GC13's seven-year branch needs its audit/notification/arrangement/application conditions. Assume no waiver or entitlement. [RM2], [RM4], [GC13], [TAA].

Determine the correct RM13 latest prescribed return balance or extension/interim alternative. Apply RM15 earlier-refund/continuity adjustments once, distinguishing a gross reference balance from one already adjusted. RM14 cessation, RM32 QC-arrangement and RZ6 historical branches remain conditional. RM16 treatment of restricted amounts does not automatically forfeit them. [RM13], [RM14], [RM15], [RM16], [RM32], [RZ6].

LA5/LA6 preserve underlying credit conditions. LA6(2) orders earlier income liabilities, later income liabilities, later provisional tax, transfer treatment and then applicable refund. Remaining credit is not automatically cash. LB4 family-credit wording is no general company entitlement. RM10 requested/discretionary application/exclusions differs from cash remittance; TAA173T permits a requested date allowed by section 173L for applying excess, not an automatic ICA date. [LA5], [LA6], [LB4], [RM10], [TAA].

Record assessment/entitlement, request/decision and actual payment dates, applicable law, reference return, earlier refunds, cap adjustments, offsets and ICA dates. Current RM2/RM4-only references cannot simply govern an event before 31 March 2026. Unsupported chronology/entitlement prevents a final refund result. [W07], [RM10], [RM13], [RM17], [OB32].

## Map a supported 2025-26 result to IR4J2026

Confirm standalone ICA filing versus combined IR4 and actual channel. Australian/new-group form labels do not establish eligibility. Carry TAA69 information for the correct annual or TAA70 period. [IR4J2026], [IR4JG2026], [IRD-annual], [IRD-interim], [TAA].

| Field | Reconciliation |
| --- | --- |
| Box6 | Opening magnitude plus separate credit/debit sign; original lots retained |
| 7A/7B/7C/7D → 7E | Eligible income tax paid, RWT interest, attached credits received and other credits, without double counting |
| 8A/8B/8C → 8D | Eligible tax refunds, attached credits paid and other debits including continuity |
| Box9 | Signed opening +7E−8D; magnitude and separate credit/debit sign |
| 9A/9B | Permitted adjustment and FIT, without automatically deducting an unproved old debit/refund |
| 10/10A | Qualifying IPT and FIT-plus-IPT total; reconcile separate payments/other account liabilities |

This is a 2-page form readback, not an implemented filing specification. Zero-sign, display precision, rounding/truncation and interactive-field behaviour remain unverified. Keep exact calculations/source precision and obtain authority before an affected final conversion/field selection. Whole-dollar examples avoid those unresolved representation choices. [IR4J2026], [IR4JG2026].

## Worked examples

All amounts are **NZD** and hypothetical. Stipulate ordinary ICA eligibility throughout, complete records, no unsupported group/sector/QC/Australian/DRCD/top-up/pooling branch, no dispute and all applicable conditions. These are explicit example facts, never missing-client-data defaults. Annual arithmetic covers **1 April 2025–31 March 2026**; later events are separately dated. Checks demonstrate arithmetic after classification, not eligibility, source completeness or professional approval.

### 1. Signed opening and ordinary movements

An original $5,000 credit dated 30 September 2024 carries into 1 April 2025. Eligible tax paid on 10 June 2025 is $3,000, RWT on 30 June 2025 $250 and valid attached credits received on 1 October 2025 $1,000. An established actual refund on 15 September 2025 is $600 and attached credits paid on 15 December 2025 are $2,000. There are no other movements and continuity holds. Refund entitlement under then-applicable law is stipulated; later RM references are not used to compute it. Closing is credit **$6,650**, with no year-end FIT/IPT in this ordinary case. [OA7], [OB4], [OB8], [OB9], [OB30], [OB32], [OB65], [IR4J2026].

```oa-check
name: nz-ica-ir4j-credit-closing
tolerance: 0
inputs:
  opening_credit: 5000
  tax_paid: 3000
  rwt: 250
  attached_received: 1000
  tax_refund: 600
  attached_paid: 2000
steps:
  total_credits: tax_paid + rwt + attached_received
  total_debits: tax_refund + attached_paid
  closing_credit: opening_credit + total_credits - total_debits
expected:
  total_credits: 4250
  total_debits: 2600
  closing_credit: 6650
```

### 2. Debit opening and year-end liability

Opening on 1 April 2025 is debit $1,200. Eligible credit $1,700 arises on 10 June 2025 and ordinary debit $800 on 15 December 2025. Closing on 31 March 2026 is debit **$300**. No OB46 exclusion, OB67 reduction, additional tax or remission applies. Qualifying FIT is **$300**, IPT **$30** and their original-due-date total **$330**, not a later overdue balance. [OB65], [OB67], [TAA], [IR4J2026].

```oa-check
name: nz-ica-ir4j-debit-closing
tolerance: 0
inputs:
  signed_opening: -1200
  credits: 1700
  debits: 800
steps:
  signed_closing: signed_opening + credits - debits
  fit: -signed_closing
  ipt: fit * 0.10
  total: fit + ipt
expected:
  signed_closing: -300
  fit: 300
  ipt: 30
  total: 330
```

### 3. Consecutive-year reduction needs notification

The 31 March 2025 debit is $1,000. Following-year credit is $200 on 10 June 2025 and debit $400 on 15 December 2025, with no other movements. Closing on 31 March 2026 is debit $1,200. All OB67 conditions and actual notification are stipulated. Credits are less than old debit, giving reduction **$800**, FIT **$400**, IPT **$40** and total **$440**. Without notification/conditions, this is no automatic adjustment. [OB67], [TAA].

```oa-check
name: nz-ica-ir4j-consecutive-year-reduction
tolerance: 0
inputs:
  prior_debit: 1000
  credits: 200
  debits: 400
steps:
  closing_debit: prior_debit - credits + debits
  reduction: prior_debit - credits
  fit: closing_debit - reduction
  ipt: fit * 0.10
  total: fit + ipt
expected:
  closing_debit: 1200
  reduction: 800
  fit: 400
  ipt: 40
  total: 440
```

### 4. Credits equal to the previous debit

Use the same prior date, with credit $1,000 on 10 June 2025 and debit $200 on 15 December 2025. Equality fails OB67(1)'s strict comparison. With no other adjustment, closing debit/FIT is **$200**, IPT **$20** and total **$220**. [OB67], [TAA].

```oa-check
name: nz-ica-ir4j-reduction-boundary
tolerance: 0
inputs:
  prior_debit: 1000
  credits: 1000
  debits: 200
steps:
  comparison_difference: prior_debit - credits
  closing_debit: prior_debit - credits + debits
  fit: closing_debit
  ipt: fit * 0.10
  total: fit + ipt
expected:
  comparison_difference: 0
  closing_debit: 200
  fit: 200
  ipt: 20
  total: 220
```

### 5. Continuity fails at 65%

A $1,000 eligible credit arises on 2 June 2025 and $600 debit on 1 August 2025. Three direct individuals hold ordinary decision rights: A40%, B60%, C0% until 1 December 2025, then A35%, B30%, C35%. Interests are constant between profiles; no relevant options, look-through, market-value circumstance, concession, QC or avoidance branch applies. Minima total **65%**. Debit only unused old credit **$400**. A valid new $300 credit on 2 February 2026 retains its own continuity, leaving closing credit **$300**. This establishes no general intraday order. [OA8], [OB41], [YC2].

```oa-check
name: nz-ica-ir4j-continuity-65
tolerance: 0
inputs:
  old_credit: 1000
  consumed: 600
  a_min: 35
  b_min: 30
  c_min: 0
  new_credit: 300
steps:
  minimum_total: a_min + b_min + c_min
  threshold_shortfall: 66 - minimum_total
  unused_old: old_credit - consumed
  continuity_debit: unused_old
  closing_credit: old_credit - consumed - continuity_debit + new_credit
expected:
  minimum_total: 65
  threshold_shortfall: 1
  unused_old: 400
  continuity_debit: 400
  closing_credit: 300
```

### 6. Exactly 66% passes the stipulated test

Keep example 5's dates and conditions, with changed profile A36%, B30%, C34%. Minima total **66%**. No continuity debit arises; $400 unused old credit plus $300 new credit gives closing credit **$700**. An actual required market-value test cannot be omitted. [OA8], [OB41].

```oa-check
name: nz-ica-ir4j-continuity-66
tolerance: 0
inputs:
  old_credit: 1000
  consumed: 600
  a_min: 36
  b_min: 30
  c_min: 0
  new_credit: 300
steps:
  minimum_total: a_min + b_min + c_min
  threshold_difference: minimum_total - 66
  unused_old: old_credit - consumed
  closing_credit: unused_old + new_credit
expected:
  minimum_total: 66
  threshold_difference: 0
  unused_old: 400
  closing_credit: 700
```

### 7. Later refund request, separate chronology

For a request on 10 July 2026, the correct RM13 return selection and 31 March 2026 reference credit **$2,000** are independently established. Earlier refund **$500** on 15 June 2026 is in the same request tax year and not already deducted from that reference balance. The 9 July 2026 assessment establishes otherwise refundable excess **$2,600**, net of earlier refund and required entitlement/offset adjustments. No interim, extension, continuity, AIM, QC or other special adjustment applies. Conditional cap/refundable amount is **$1,500**, leaving **$1,100** not refunded. This cap example establishes no entitlement, Commissioner approval or actual cash receipt. [RM2], [RM4], [RM10], [RM13], [RM15], [RM16], [W07].

```oa-check
name: nz-ica-ir4j-refund-cap
tolerance: 0
inputs:
  reference_credit: 2000
  earlier_refund: 500
  established_entitlement: 2600
steps:
  adjusted_cap: reference_credit - earlier_refund
  conditional_refund: adjusted_cap
  not_refunded: established_entitlement - conditional_refund
expected:
  adjusted_cap: 1500
  conditional_refund: 1500
  not_refunded: 1100
```

### 8. FIT allocation supplies no extra ICA credit

FIT paid on 18 June 2026 is **$1,000**, with **$100 IPT** separately paid. Valid OB69 election and qualifying income-year/status are established. Three separately verified provisional liabilities of **$600 each** are first payable after payment, ordered I1/I2/I3. Their dates/options must come from the applicable validated schedule; this arithmetic supplies none and resolves no missing timing rule. FIT applies **$600/$400/$0**, leaving **$0/$200/$600**. Its application gives no additional ICA credit; IPT is not added to available FIT. [OB69], [RC35], [OB4], [RM17].

```oa-check
name: nz-ica-ir4j-fit-allocation
tolerance: 0
inputs:
  fit_paid: 1000
  first_liability: 600
  second_liability: 600
  third_liability: 600
steps:
  first_applied: first_liability
  after_first: fit_paid - first_applied
  second_applied: after_first
  after_second: after_first - second_applied
  third_applied: after_second
  first_remaining: first_liability - first_applied
  second_remaining: second_liability - second_applied
  third_remaining: third_liability - third_applied
expected:
  first_applied: 600
  after_first: 400
  second_applied: 400
  after_second: 0
  third_applied: 0
  first_remaining: 0
  second_remaining: 200
  third_remaining: 600
```

### 9. Consume the oldest lot once

Credits are $100 on 2 June 2025 and $200 on 1 July 2025. A $150 ordinary debit on 1 August 2025 consumes all older $100 and newer $50. Established continuity failure on 3 November 2025 affects remaining newer **$150**, debited once. A valid post-failure $50 credit on 2 February 2026 leaves closing credit **$50**. No other events, special exceptions or same-day order are assumed. [OA7], [OA8], [OB41].

```oa-check
name: nz-ica-ir4j-fifo-once
tolerance: 0
inputs:
  old_lot: 100
  newer_lot: 200
  debit: 150
  post_failure_credit: 50
steps:
  newer_consumed: debit - old_lot
  newer_remaining: newer_lot - newer_consumed
  continuity_debit: newer_remaining
  closing_credit: old_lot + newer_lot - debit - continuity_debit + post_failure_credit
expected:
  newer_consumed: 50
  newer_remaining: 150
  continuity_debit: 150
  closing_credit: 50
```

### 10. Evidenced partial IPT remission

The qualifying FIT base is **$300**, giving gross IPT of **$30** at the established 10% rate. A dated Commissioner decision establishes the TAA180(1)(b) refund ground and the Commissioner's satisfaction for **$10** of that IPT, and remits that amount. The decision's amount is an evidenced input; this example does not derive remission entitlement from a refund label. Net IPT is **$20** and FIT plus net IPT is **$320**. Remitting IPT does not itself reduce the $300 FIT. Late-payment penalties, interest and any separate relief require their own amounts and conditions; none is included here. [TAA].

```oa-check
name: nz-ica-ir4j-partial-ipt-remission
tolerance: 0
inputs:
  fit: 300
  evidenced_remission: 10
steps:
  gross_ipt: fit * 0.10
  net_ipt: gross_ipt - evidenced_remission
  fit_plus_net_ipt: fit + net_ipt
expected:
  gross_ipt: 30
  net_ipt: 20
  fit_plus_net_ipt: 320
```

**Unresolved-condition control.** If the refund ground, the Commissioner's satisfaction or the remitted amount is not established, retain the **$30 gross IPT** and mark net IPT and FIT-plus-net-IPT **Needs Input**. Do not assume the $10 remission or substitute zero for an unknown decision. This is a required manual control, not a claim that the arithmetic block tests a missing-evidence workflow. [TAA].

## Outputs and reviewer handoff

Produce all 4 actual universal outputs when an authorised engagement is run:

1. **Recalculated Excel working paper.** Preserve every source item, classification, provision/date, period, evidence and flag/default/reviewer reason. Add signed opening/closing, original-lot/FIFO/continuity, tax-account, refund-cap/offset, FIT/IPT/election, return-box and notice/deadline schedules. Retain prescribed colours, formulas/SUMIFS, source precision and zero-formula-error/recalculation checks from the bases.
2. **Reviewer brief.** Retain the universal template and all 7 corporate components: executive summary, computation walk-through, applicable cross-border/Pillar Two analysis, deferred-tax provision, supporting schedules, reviewer questions and filing assembly. Include periods, unknown amounts, fired/cleared refusals, notices/elections and every T2/T3 position. ICA cannot replace the profit-to-tax bridge or other applicable corporate work.
3. **Action list.** Identify responsible person, action/evidence, deadline, cash impact and brief reference for source gaps, questions, notices, extensions, elections, review, filing and payment.
4. **Review checklist.** Follow both bases' section order and record every check, flag/default/T2 position, cross-document reconciliation and practitioner acceptance/rejection.

Retain every corporate domain deliverable, including return/forms, current/deferred tax provision, payment/instalment schedules and documentation index. Reading these examples creates no actual workbook, recalculation, engagement output, submission, payment or practitioner sign-off.

## Self-checks before delivery

Run both bases' complete checks, including all **18 corporate self-checks**, without replacing them with ICA checks. Confirm residence/currency/financial statements/PBT, cited adjustments/exemptions/depreciation, losses/foreign credits, transfer pricing/PE, Pillar Two/deferred-tax/recapture, GAAR/disclosures, complete calendar and every T2/T3 reviewer position as those bases require. Evidence must establish applicable/inapplicable conclusions.

- [ ] Source periods, entity/status and refusal conditions are established, without an unsupported ordinary default.
- [ ] Every source item remains; gross movements, tax-account allocations and totals reconcile.
- [ ] Opening sign/magnitude matches prior closing; original lots/dates survive rollover.
- [ ] Every class/effective date is supported and no amount is counted twice.
- [ ] Every relevant person's minimum voting interest covers the lot period, with required market-value/look-through/options/securities rules.
- [ ] Required market-value continuity of 65% fails despite voting is 66%; voting alone does not pass OA8.
- [ ] FIFO and unused failed lots reconcile; unresolved intraday sequence remains held.
- [ ] QC/sector/group/DRCD/pooling/historical/arrangement branches are established or stopped under their actual refusal/hold.
- [ ] OB46/OB67 and FIT adjustments are evidenced, including strict comparison/notification; IPT has its separate base and gross/remission/net trace, with TAA180/181C screening and unresolved relief held.
- [ ] FIT application has payment/election/status evidence and ordered instalments, without duplicate ICA credit or IPT substitution.
- [ ] Refund entitlement/event law/reference return/earlier refunds/cap/offset/cash/ICA dates reconcile without double reduction.
- [ ] Annual/interim/final/revised duties, extensions/notices/payment channels are separately established; no 2027 annual result uses IR4J2026.
- [ ] Form signs/precision and overdue interest/penalty/remission conditions are established or held.
- [ ] Every mandatory country slot, output, formula/recalculation, source trace and professional review is complete before a completed-company or filing-ready claim.

## Provenance and limitations

Version 0.2 was prepared on 14 November 2026 from selected primary sources below. Independent preparation checks covered source bindings/boundaries, operative-period distinctions, form/native/visual mapping and hypothetical arithmetic. They are not practitioner sign-off, complete historical/current-law assurance, an executed engagement or corporate-topic completion. This tier 2 guide remains pending licensed practitioner review; its examples establish no actual taxpayer result.

The 2026 form's 2 pages were read natively without OCR and visually checked. Font-rendering warnings, zero-sign, precision and interactive-field limits remain. IR2742024 has column-layout/example-year limitations and does not establish general intraday order or blanket interest relief. Use operative provisions and period-specific evidence for a relied-on result.

## Primary sources

- Income Tax Act 2007: selected OA/OB/OP account, RA/RC payment, RM refund and YA/YC/YD definition/ownership/residence provisions, consolidation 4 September 2026.
- Tax Administration Act 1994: selected record, return, assessment, transfer, penalty and interest provisions, consolidation 1 October 2026.
- IR4J2026 and April 2026 IR4JG: 2025-26 annual form/instructions, with the representation limits above.
- IRD annual/interim return and payment guidance; IR274 April 2024 is supplementary with its stated layout/period limits.
- Selected commencement/application provisions in the 2024 multinational-tax, 2026 compliance, 2023 platform-economy and 2025 remedial Acts. No source below establishes every later amendment or every special branch.

[GB34]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1516995/
[GC13]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1517112/
[HA18]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1517176/
[IR274]: https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir200---ir299/ir274/ir274-2024.pdf?modified=20240604223621
[IR4J2026]: https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir1---ir99/ir4j/ir4j-2026.pdf?modified=20260331190002
[IR4JG2026]: https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir1---ir99/ir4jg/ir4jg.pdf?modified=20260331224857
[IRD-annual]: https://www.ird.govt.nz/income-tax/income-tax-for-businesses-and-organisations/income-tax-for-companies/imputation-for-companies/how-imputation-credits-work/file-an-annual-imputation-return-ir4j
[IRD-interim]: https://www.ird.govt.nz/income-tax/income-tax-for-businesses-and-organisations/income-tax-for-companies/imputation-for-companies/how-imputation-credits-work/file-an-interim-imputation-return---ir4j
[IRD-pay]: https://www.ird.govt.nz/managing-my-tax/make-a-payment/when-to-pay
[LA5]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1517901/
[LA6]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1517903/
[LB4]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1517921/
[OA3]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1518637/
[OA5]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1518642/
[OA6]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1518651/
[OA7]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1518661/
[OA8]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1518664/
[OB1]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1518696/
[OB2]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1518700/
[OB25]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1518751/
[OB3]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1518702/
[OB30]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1518762/
[OB32]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1518766/
[OB33]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1518772/
[OB34]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1518774/
[OB35]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1518776/
[OB37]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1518780/
[OB4]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1518705/
[OB41]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1518791/
[OB46]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1518820/
[OB5]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1518708/
[OB54]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1518839/
[OB56]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1518843/
[OB6]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1518710/
[OB65]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1518870/
[OB67]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1518874/
[OB69]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1518881/
[OB8]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1518714/
[OB9]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1518716/
[OP2]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1519412/
[RA6]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1519737/
[RA9]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1519743/
[RC32]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1519904/
[RC35]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1519914/
[RM10]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1520433/
[RM13]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1520441/
[RM14]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1520443/
[RM15]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1520445/
[RM16]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1520447/
[RM17]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1520449/
[RM2]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1520416/
[RM32]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1520489/
[RM4]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1520420/
[RP17B]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM2630341/
[RP19]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1520541/
[RZ6]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1520562/
[TAA]: https://www.legislation.govt.nz/act/public/1994/166/en/latest/
[W03]: https://www.legislation.govt.nz/act/public/2024/11/en/latest/
[W07]: https://www.legislation.govt.nz/act/public/2026/8/en/latest/
[W10]: https://www.legislation.govt.nz/act/public/2023/5/en/latest/
[W11]: https://www.legislation.govt.nz/act/public/2025/9/en/latest/
[YA1]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1520575/
[YC11]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1523090/
[YC15]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1523108/
[YC2]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1523060/
[YC20]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1523128/
[YC3]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1523063/
[YC4]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1523065/
[YD2]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1523137/

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
