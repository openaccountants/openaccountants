---
name: au-director-penalties
description: >
  Use this guide to prepare the evidence on an Australian company director's personal
  liability for director penalties under Division 269 of Schedule 1 to the Taxation
  Administration Act 1953, on the law at 2 November 2026 (2026-27). Covers unpaid PAYG
  withholding, GST and super guarantee charge, including the Payday Super rules for
  QE days from 1 July 2026 and the saved rules for earlier quarters, ATO estimates,
  director penalty notices, the 21-day remission window, lockdown, new and resigned
  directors, parallel liabilities and the statutory defences. Trigger on 'director
  penalty notice', 'DPN', 'locked down DPN', 'director personally liable' or
  'Division 269'.
jurisdiction: AU
category: international
tax_year: 2026
tax_year_notes: "2026-27 (QE days from 1 July 2026; saved law for earlier quarters)"
tier: 2
last_updated: 2026-11-11
version: 0.1
review_status: pending_review
depends_on:
  - workflow-base
verified_by: pending
license: FSL-1.1-ALv2
---

# Australian Director Penalties (Division 269) v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

This guide prepares the evidence on whether, and to what extent, a director or former director is personally liable for a company's unpaid PAYG withholding, GST or super guarantee charge (SGC) under Division 269 of Schedule 1 to the *Taxation Administration Act 1953* (TAA). The output is for the director's lawyer, insolvency adviser or registered tax agent; it decides nothing. The law is TAA compilation 227 (C2026C00468, in force from 1 October 2026), read on 2 November 2026, with the Payday Super amendments made by the *Treasury Laws Amendment (Payday Superannuation) Act 2025*.

**Covered:** which company obligations Division 269 reaches (s 269-10), including ATO estimates under Division 268; the directors' obligation and when it ends (s 269-15); when a penalty arises for existing and new directors (s 269-20); the director penalty notice (DPN) and how it is given (ss 269-25, 269-50, 269-52); remission and lockdown (s 269-30); the defences (s 269-35); and the parallel liabilities and contribution rights (ss 269-40, 269-45). The company must be registered under the *Corporations Act 2001*.

**Not covered, and where it goes:**

- Computing the SGC, Payday Super deadlines and voluntary disclosure: `au-super-guarantee`.
- PAYG withholding amounts and BAS labels: `au-bas-preparation` and `australia-payroll`. GST net amounts: `au-gst-bas` and `australia-gst`.
- GIC, penalty units, other penalties, remission of interest and the summary of other recovery powers: `au-lodgment-deadlines-penalties` (Section 9 holds the outline this guide expands).
- Objections against the company's assessments: `au-objections`. Division 269 has no objection provision; the defence route is in Step 6.
- PAYG withholding non-compliance tax (Subdivision 18-D of Schedule 1), insolvent trading and other Corporations Act duties, and any insolvency decision (refusals R-AU-DPN-1 and R-AU-DPN-4).

## Ask the client first

1. ASIC records for the company: registration, each director's appointment and cessation dates, and each director's residential and business addresses on record over time.
2. The company's ATO account and lodgment history by period: activity statements (PAYG withholding and GST), voluntary disclosure statements and SGC assessments for QE days from 1 July 2026, SG statements for quarters before then, Division 268 estimate notices, payments and credits.
3. Each DPN: the date on it, the date it was posted or left, the address used, the liabilities and amounts listed, and whether a copy went to a registered tax agent.
4. Any administrator, small business restructuring practitioner or liquidator appointment, with its date.
5. Any instalment arrangement under Sch 1 s 255-15 covering the company's obligation.
6. Evidence the director offers for a defence: illness or other reason for not taking part in management, steps taken and when, and the positions the company took on GST or SG with the reasoning at the time.

## The method, step by step

### Key figures

Every figure below was read on 2 November 2026 in TAA Schedule 1, compilation 227, unless another source is named; full URLs are in Sources.

| Item | Value | Source |
| --- | --- | --- |
| Recovery proceedings | Not before the end of 21 days after the Commissioner gives the DPN; the day of giving is not counted | s 269-25(1); *Acts Interpretation Act 1901* s 36(1) item 6 |
| Remission window | Penalty remitted if the directors' obligation ends before the DPN is given or within 21 days after, counted the same way | s 269-30(1) |
| When a DPN is given | When the Commissioner leaves or posts it, despite s 29 of the *Acts Interpretation Act 1901* | s 269-25(4) |
| DPN address | An address that appears from ASIC information to be, or to have been within the last 7 days, the director's residence or business | s 269-50 |
| New director | Liable if still under the obligation 30 days after becoming a director; penalty due at the end of that 30th day | s 269-20(3)-(4) |
| PAYG withholding and GST lockdown | Where the administration, restructuring or winding up comes after the last day of the 3 months after the due day, remission that way is lost to the extent of amounts not reported by that day | s 269-30(2) items 1, 5 |
| Estimates of PAYG withholding or GST | Same 3-month test, measured from the underlying due day (GST: the return due day); lockdown to any extent | s 269-30(2) items 2, 6 |
| New director's 3 months | For a person who became a director during or after the 3 months, they run from the day the person became a director; items 1, 2, 5 and 6 only | s 269-30(3) |
| SGC due day, QE day from 1 July 2026 | The earlier of: the first day after the end of the 60-day period starting on the QE day; or the day the charge is payable under s 36(4) of the *Superannuation Guarantee (Administration) Act 1992* (SGAA), which is the day an assessment is made. The first limb applies even if the charge has not yet been assessed | s 269-10(3) (substituted by Payday Super Act Sch 1 item 169); SGAA s 36(4) |
| SGC lockdown, QE day from 1 July 2026 | Remission by administration, restructuring or winding up after the due day is lost: if a voluntary disclosure statement for the QE day was lodged under SGAA s 33 by the due day, to the extent the charge worked out from it is less than the charge payable; otherwise to any extent | s 269-30(2) item 3 (substituted by Payday Super Act Sch 1 item 171) |
| Payday Super application | Applies to QE days on or after 1 July 2026; the old law continues for SGC relating to quarters ending before that day | Payday Super Act s 2 (commenced 1 July 2026); Sch 1 items 182, 183 |
| SGC due day, quarter ending before 1 July 2026 | The day the SG statement for the quarter had to be lodged under old SGAA s 33; the ATO states it as one month and 28 days after the quarter ends | s 269-10(3) as at 30 June 2026 (compilation 224); PS LA 2011/18 Table 1 |
| SGC lockdown, quarter ending before 1 July 2026 | Lost to the extent the SG statement amount fell short, or to any extent if no statement was lodged by the due day | s 269-30(2) item 3 as at 30 June 2026 (compilation 224) |
| Defence information to the Commissioner | Within 60 days starting when the Commissioner gives a garnishee notice for the penalty or notifies in writing that some of it was recovered | s 269-35(4A) |
| Historical reach | SGC: quarters whose SG statement was due on or after 30 June 2012. GST: tax periods or quarters starting on or after 1 April 2020 | PS LA 2011/18 para 47 |

### Step 1: Build the liability schedule

For each company and period record: the obligation (PAYG withholding under Subdivision 16-B, including alienated personal services payments and non-cash benefits; SGC for a QE day or an old quarter; GST assessed net amount; GST instalment; or a Division 268 estimate), the initial day, the due day, the date and amount reported, any estimate and its notice date, payments and credits, and the balance (s 269-10(1)-(5)). Keep estimates separate: the ATO treats estimated PAYG withholding, GST and SGC as never reported (ATO, Director penalties). A director's obligation on an estimate exists even if the underlying liability never existed or is smaller (s 269-15(2A)). Reconcile the schedule to the ATO account; an unreconciled balance stays an open item.

### Step 2: Classify the reporting timing for each liability

For PAYG withholding and GST, record whether the amount was notified (under s 16-150 or s 389-5 for withholding) or the GST return lodged by the last day of the 3 months after the due day. For SGC, identify the QE day or quarter first. For a QE day from 1 July 2026, record the QE day, the due-day workings under s 269-10(3), whether a voluntary disclosure statement was lodged by the due day, the charge it discloses, the charge payable and the difference, as separate items. For an earlier quarter, apply the saved old law: record the SG statement due day and lodgment date. Record the classification and its source as an input for the director's advisers, not a conclusion.

### Step 3: Build each director's timeline

The obligation binds the directors 'from time to time' on or after the initial day (s 269-15(1)) and continues until the company complies, an administrator is appointed under Corporations Act s 436A, 436B or 436C, a small business restructuring practitioner is appointed under s 453B, or the company begins to be wound up (s 269-15(2)). A penalty arises at the end of the due day for each person who was under the obligation at or before then, even if they have since resigned (s 269-20(1)-(2) and note). The ATO's page applies this to resigned directors: PAYG withholding where the first withholding event in the reporting period occurred before resignation; GST and SGC where the reporting period ended before resignation; liability survives deregistration (ATO, Director penalties). Its SGC test describes quarters; for a QE day from 1 July 2026 the initial day is the QE day (s 269-10(1) item 5), so test SGC tenure from the QE day. For a new director appointed after a due day, test the 30-day rule in s 269-20(3). Correcting ASIC records is outside this guide; record any discrepancy as an open item.

### Step 4: Register each DPN

Record the issue date, the date posted or left, the address and whether it came from ASIC information within the 7-day window (s 269-50), the amounts by liability and the remission options stated. A DPN must state the unpaid amount, that the director is liable for an equal penalty, and the main circumstances in which it will be remitted; one notice may cover several penalties (s 269-25(2)-(3)). A copy sent to a registered tax agent's address does not affect whether the notice itself was given (s 269-52). An instalment arrangement under s 255-15 bars proceedings but not the giving of a DPN (s 269-15(3) and note 2).

### Step 5: List the remission options and the lockdown position

The penalty equals the unpaid amount of the company's liability (s 269-20(5)). It is remitted if the directors' obligation ends before the DPN or within 21 days after it (s 269-30(1)), but s 269-30(2) removes that remission where the obligation ends through administration, restructuring or winding up after the column 2 day, to the column 3 extent:

- PAYG withholding (item 1): after the last day of the 3 months after the due day, to the extent not notified by then.
- PAYG withholding estimate (item 2): after the last day of the 3 months after the underlying due day, to any extent.
- SGC (item 3) and SGC estimate (item 4): after the due day (item 4: the underlying due day), as in Key figures.
- GST assessed net amount (item 5): after the last day of the 3 months after the due day, to the extent the net amount worked out from a GST return lodged by then, and any other information the company gave the Commissioner by then, is less than the assessed net amount; to any extent if no return was lodged.
- GST estimate (item 6): after the last day of the 3 months after the return due day, to any extent.
- GST instalments are not affected (note 3).

Payment towards the company's liability discharges each parallel liability by the same amount (s 269-40(2)), so payment in full always clears the penalty. Mark each option as appearing available or not on the evidence, conditional on the advisers' review. An insolvency appointment is the directors' decision with a registered insolvency practitioner (refusal R-AU-DPN-1).

### Step 6: Collect the defence evidence

The statutory defences (s 269-35):

- **Illness or other good reason:** it would have been unreasonable to expect the director to take part, and the director did not take part, in management at any time when a director and under the obligation (s 269-35(1)).
- **All reasonable steps:** the director took all reasonable steps to ensure the company complied, an administrator or restructuring practitioner was appointed, or winding up began; or there were no reasonable steps available. Regard is had to when and for how long the person was a director and took part in management (s 269-35(2)-(3)).
- **Reasonably arguable position (SGC and GST only):** to the extent the penalty resulted from the company applying the SGAA or the GST Act in a reasonably arguable way, with reasonable care (s 269-35(3A)). It does not extend to PAYG withholding.

In court the director must prove the illness or reasonable-steps defence (s 269-35(4)); outside court the Commissioner must be satisfied on information given within the s 269-35(4A) 60 days. Corporations Act s 1318 relief does not apply (s 269-35(5)). The ATO's page summarises case law that reliance on others is no defence and that the defences must cover the whole period from when the obligation arose to the end of the notice period, and describes review under the *Administrative Decisions (Judicial Review) Act 1977* only for a defence lodged within those 60 days (ATO, Director penalties). Prepare a dated evidence list for the director's lawyer; do not assess whether a defence succeeds (refusal R-AU-DPN-2).

### Step 7: Reconcile the parallel liabilities

Reconcile payments by the company and by every director against the company balance and each DPN: each payment reduces every other liability then existing by the same amount, and nothing is discharged beyond its amount (s 269-40(2)-(4)). A director who pays has guarantor-style rights of indemnity and contribution against the company and the other directors (s 269-45).

### Permitted factual defaults

| Missing fact | Default | Disclose |
| --- | --- | --- |
| Date a DPN was posted or left | Use the date on the notice as the giving date and count the 21 days from the next day, which ends them earliest | The actual posting date can be later |
| Whether a liability was reported within 3 months, or an SGC statement by the due day | Treat it as locked down | Remission by appointment may in fact be available |
| A QE day due day where the SGAA s 36(4) payable day is unknown | Use the s 269-10(3)(a) day only if it is earlier than any assessment the file shows; otherwise Needs Input | The due day may be earlier |
| A last day on a weekend or holiday | Do not rely on *Acts Interpretation Act 1901* s 36(2) roll-forward | Whether s 36(2) moves a Division 269 day is not settled here |

No default is permitted for appointment and resignation dates, amounts, or the facts of a defence. Return Needs Input for each.

### Working paper additions

Add to the base outputs: (1) the reconciled liability schedule; (2) the reporting-timing classification with its source and date; (3) each director's tenure timeline; (4) the DPN register with the 21-day end dates, counted from the day after the giving date; (5) the parallel-payment reconciliation; (6) the conditional options list; and (7) the dated defence evidence list.

## Worked cases

All facts are hypothetical.

### Case 1: Parallel liabilities after part payments (2026-27)

A company owes $48,000 of reported PAYG withholding. Two directors receive DPNs. Director A pays $15,000 and the company pays $9,000.

```oa-check
name: Parallel director penalty liabilities after part payments under s 269-40 (2026-27)
inputs:
  company_paygw_unpaid: 48000
  director_a_payment: 15000
  company_payment: 9000
steps:
  - company_balance: company_paygw_unpaid - director_a_payment - company_payment
  - director_a_balance: company_balance
  - director_b_balance: company_balance
  - total_collected: director_a_payment + company_payment
  - total_collected_and_owing: total_collected + company_balance
expected:
  company_balance: 24000
  director_a_balance: 24000
  director_b_balance: 24000
  total_collected: 24000
  total_collected_and_owing: 48000
```

Each balance is $24,000, but the ATO can collect no more than $24,000 more in total. Director A's contribution claim against Director B is for the advisers (s 269-45).

### Case 2: GST under-reported in time, administrator appointed late (2026-27)

A company lodged its BAS within 3 months after the due day, reporting a net amount of $30,000, unpaid. An ATO review later assessed the net amount for the period at $42,000. More than 3 months after the due day a DPN issues, and within 21 days the directors appoint an administrator. Nothing has been paid.

```oa-check
name: Partial GST lockdown under s 269-30(2) item 5 (2026-27)
inputs:
  assessed_net_amount: 42000
  net_amount_reported_in_time: 30000
  paid: 0
steps:
  - locked_down: max(assessed_net_amount - net_amount_reported_in_time, 0)
  - remitted_by_administration: assessed_net_amount - paid - locked_down
expected:
  locked_down: 12000
  remitted_by_administration: 30000
```

Had the administrator been appointed on or before the last day of the 3 months after the due day, column 2 of item 5 would not be met and the whole penalty could be remitted under s 269-30(1). No appointment remits the $12,000; only payment discharges it, unless a s 269-35 defence applies. The example assumes the penalty covers the whole $42,000; the due day for an amount added by an amended assessment needs its own check (Needs Input).

### Case 3: A Payday Super QE day (2026-27)

A company paid wages on Thursday 16 July 2026 (the QE day) and missed the contribution deadline. It lodged a voluntary disclosure statement on 1 September 2026 disclosing a charge of $6,200; the charge payable is later found to be $8,900. No assessment has made the charge payable before the s 269-10(3)(a) day. The 60-day period starts on, and includes, the QE day (*Acts Interpretation Act 1901* s 36(1) item 2).

```oa-check
name: SGC due day and partial lockdown for a QE day under ss 269-10(3) and 269-30(2) item 3 (2026-27)
inputs:
  qe_day_of_july: 16
  days_in_july: 31
  days_in_august: 31
  period_days: 60
  charge_from_statement: 6200
  charge_payable: 8900
steps:
  - july_days_in_period: days_in_july - qe_day_of_july + 1
  - through_august: july_days_in_period + days_in_august
  - period_end_day_of_september: period_days - through_august
  - due_day_of_september: period_end_day_of_september + 1
  - locked_down: max(charge_payable - charge_from_statement, 0)
expected:
  july_days_in_period: 16
  through_august: 47
  period_end_day_of_september: 13
  due_day_of_september: 14
  locked_down: 2700
```

The due day is Monday 14 September 2026, and the statement was lodged before it. Had the ATO assessed the charge before then, the assessment day would have been the due day (s 269-10(3)(b); SGAA s 36(4)). If the directors stop being under the obligation through an appointment after that day, $2,700 cannot be remitted that way. Without a statement by the due day, the whole charge would be locked down.

### Case 4: A new director

A person became a director on 2 November 2026; a PAYG withholding amount was due and reported before then, and is unpaid. Unless the company pays, appoints an administrator or restructuring practitioner, or begins to be wound up within 30 days, the new director is liable at the end of the 30th day (s 269-20(3)-(4)). The 3-month reporting test for items 1, 2, 5 and 6 runs from the appointment (s 269-30(3)); there is no equivalent for SGC.

### Case 5: An old-quarter SGC liability

SG for the January to March 2026 quarter was not paid and no SG statement was lodged. The quarter ended before 1 July 2026, so the old law applies (Payday Super Act Sch 1 item 183(2)): the due day is the SG statement day for the quarter, and with no statement lodged by then the penalty is locked down to any extent. Route the charge computation to `au-super-guarantee`.

### Case 6: An estimate for a liability that may not exist

The ATO estimated unpaid PAYG withholding for a quarter in which the company says it paid no wages. The director's obligation on the estimate stands even if the underlying liability never existed (s 269-15(2A)); an appointment more than 3 months after the underlying due day leaves the penalty locked down to any extent (item 2). Record the estimate separately and refer how to challenge it to the advisers.

## When to refuse or refer

Stop the affected work where a fact, condition or source in this guide is unresolved, and return Needs Input or refer it for qualified review.

| Code | Trigger | Message (verbatim) |
| --- | --- | --- |
| R-AU-DPN-1 | A request to recommend administration, restructuring, liquidation or payment | 'Whether to appoint an administrator, restructure, wind up or pay is for the directors with a registered insolvency practitioner and their lawyer. I list the options and evidence only.' |
| R-AU-DPN-2 | A request to say whether a defence will succeed | 'Whether a defence succeeds is for the director's lawyer and, in the end, the Commissioner or a court. I prepare the dated evidence list.' |
| R-AU-DPN-3 | Recovery proceedings, a garnishee notice, a departure prohibition order or judicial review | 'Recovery action is under way. Refer this to the director's lawyer now; the time limits are short.' |
| R-AU-DPN-4 | Insolvent trading, other Corporations Act duties or PAYG withholding non-compliance tax | 'These are separate liabilities outside Division 269. Refer them to the director's lawyer.' |
| R-AU-DPN-5 | The company is not, or was not on the initial day, registered under the Corporations Act 2001 | 'Division 269 applies only to a company registered under the Corporations Act 2001 on the initial day. Refer the entity question.' |

**Reviewer attention thresholds.** These are this guide's review settings, not statutory figures. Flag for reviewer attention regardless of confidence:

| Threshold | Why |
| --- | --- |
| Any DPN, whatever the amount | The 21-day window cannot be extended by this work |
| Any director exposure of $10,000 or more | Personal liability needs senior review |
| Any locked-down amount | Administration, restructuring or winding up cannot remit it; only payment or a s 269-35 defence avoids it |
| Any estimate | It binds even if the underlying liability is disputed |
| Any QE day from 1 July 2026 | The Payday Super due day and lockdown test are new |
| Any defence claimed | The 60-day information period and the court onus apply |

**Prohibitions.** Never treat an estimate as a reported amount. Never treat resignation as ending liability for amounts already within the director's tenure. Never present the lockdown classification as a conclusion.

## Completion checklist

- [ ] The company was registered under the Corporations Act 2001 on each initial day.
- [ ] Each liability has its obligation type, initial day, due day, reporting date, amount, estimate status and balance, reconciled to the ATO account.
- [ ] Each SGC liability is labelled QE day (new law) or quarter (saved law), with the matching due-day and lockdown test.
- [ ] Each director's tenure is tied to ASIC records and tested against each initial day (for SGC, the QE day), each due day and the 30-day new-director rule.
- [ ] Each DPN has its giving date, address check and 21-day end date.
- [ ] Payments by the company and each director are reconciled across the parallel liabilities.
- [ ] Remission options are conditional and no insolvency recommendation is made.
- [ ] Defence evidence is dated and covers the whole period.

Change log: v0.1 (2 November 2026), first draft from Division 269 of TAA Schedule 1 (compilations 227 and 224), the Payday Super Act as made, PS LA 2011/18 and the ATO director penalties page.

## Sources

All read on 2 November 2026; figures and dates rechecked against the same sources on 11 November 2026.

| Source | URL | Read on |
| --- | --- | --- |
| TAA 1953, compilation 227 (C2026C00468, from 1 October 2026), Volume 2: Sch 1 Division 269 (ss 269-1 to 269-55) | https://www.legislation.gov.au/C1953A00001/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html | 2 November 2026 |
| TAA 1953, compilation 224 (C2026C00303, in force 30 June 2026), Volume 2: Sch 1 ss 269-10(3) and 269-30(2) item 3 before Payday Super | https://www.legislation.gov.au/C1953A00001/2026-06-30/2026-06-30/text/original/epub/OEBPS/document_2/document_2.html | 2 November 2026 |
| *Treasury Laws Amendment (Payday Superannuation) Act 2025* (No. 57, 2025), as made: s 2 and Sch 1 items 164 to 172, 181 to 183 | https://www.legislation.gov.au/C2025A00057/asmade/2025-11-07/text/original/epub/OEBPS/document_1/document_1.html | 2 November 2026 |
| SGAA, compilation 78 (compilation date 1 July 2026): ss 33, 36 | https://www.legislation.gov.au/C2004A04402/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_1/document_1.html | 2 November 2026 |
| *Acts Interpretation Act 1901*, compilation 39 (C2026C00117): s 36 | https://www.legislation.gov.au/C1901A00002/2026-03-28/2026-03-28/text/original/epub/OEBPS/document_1/document_1.html | 2 November 2026 |
| ATO, Director penalties (QC44005, last updated 16 April 2026) | https://www.ato.gov.au/individuals-and-families/paying-the-ato/if-you-don-t-pay/firmer-action-we-may-take/director-penalty-regime | 2 November 2026 |
| PS LA 2011/18, Enforcement measures used for the collection and recovery of tax-related liabilities and other amounts (amended 20 May 2026): paras 47, 58 to 61, Table 1, 84 to 88 | https://www.ato.gov.au/law/view/document?docid=PSR/PS201118/NAT/ATO/00001 | 2 November 2026 |

Not yet confirmed: PS LA 2011/18 Table 1 and the ATO page still describe SGC lockdown by reference to SG statements and the 'SGC due date'; for QE days from 1 July 2026 this guide follows the substituted statutory text. Beyond SGAA ss 33 and 36, `au-super-guarantee` holds the SGC rules. Whether *Acts Interpretation Act 1901* s 36(2) moves a Division 269 due day that falls on a weekend is not settled here. No accountant has reviewed this draft.

Method adapted by its author from the `au-director-penalty-review` skill in ryanduguid/australian-accounting-skills (commit 3e110da). This guide is licensed under FSL-1.1-ALv2, not the OA Guide License; see LICENSING.md.

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
