---
name: us-irs-notices-cp2000-and-letters
description: Decide how to answer a US IRS CP2000 underreporting proposal (agree, partly agree or disagree) and what to do with an identity and return verification notice (CP5071, Letter 5071C, CP5071F). Reads the notice, matches each proposed item to the client's records, splits the items into agreed and disputed, and sets the response date (30 days from the notice date, 60 days for a client living outside the United States). Trigger on "CP2000", "IRS says I underreported", "IRS matched a 1099", "Letter 5071C", "CP5071", "verify my identity IRS", "irs.gov/verifyreturn". Bills, reminders, levy notices, math-error notices and penalties are handled in us-irs-collections-and-controversy. Federal only.
version: "1.0"
jurisdiction: US
tax_year: 2026
last_updated: 2026-11-13
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: references
type: decision
---

# IRS CP2000 and identity verification letters: what to answer (US federal)

> **Source-cited draft.** Built from IRS Topic 652, the IRS pages "Understanding your CP2000 series notice", "Understanding your CP5071 series notice" and "Verify your return", read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** A CP2000 is a proposal, not a bill. Answer it within **30 days of the notice date** (60 days if the client lives outside the United States), item by item: agree with the items the records support, disagree with the rest, with a signed statement and documents. A CP5071, Letter 5071C or CP5071F means the IRS is holding a return filed under the client's SSN or ITIN until the client verifies identity and the return; do it at irs.gov/verifyreturn or as the notice says. If the client did not file that return, say so in the verification: it may be identity theft.

This skill is a companion to `us-irs-collections-and-controversy`, which owns the other notices (CP11 and other math-error notices, CP14, CP501, CP503, CP504, LT11), audits, collection, the penalty rates (failure to file, failure to pay, the minimum late-filing penalty, accuracy-related) and penalty relief (First Time Abate, reasonable cause, Form 843). Those figures are not restated here.

## Scope and who this is for

In scope: an individual (Form 1040 series) who has received a CP2000 (Automated Underreporter proposal) or a CP5071 series identity and return verification notice, and the practitioner answering it.

| Topic | Skill |
| --- | --- |
| CP11, CP12 (math error), CP14 (first bill), CP501 and CP503 (reminders), CP504 (intent to levy), LT11 and CDP rights | `us-irs-collections-and-controversy` |
| Penalty rates, interest rate, First Time Abate, reasonable cause, Form 843 | `us-irs-collections-and-controversy` |
| The statutory notice of deficiency and the 90-day Tax Court clock | `us-irs-collections-and-controversy` |
| Recomputing the 1040 after an agreed change | `us-federal-income-tax-return-1040` |
| Underpayment of estimated tax | `us-quarterly-estimated-tax` |
| 1099-K and payment-processor mismatches | `us-1099-k-and-payment-processors` |

## Ask the client first

1. **The notice itself**, all pages: its number (top right, for example CP2000, CP5071, 5071C, CP5071F), its **date**, the tax year, and the response form. Deadlines run from the notice date, not the day it arrived.
2. **Where the client lives now.** Outside the United States, the CP2000 response time is 60 days instead of 30.
3. **The return as filed** for that year (or the processed amended return), with its schedules and the client's ledger.
4. **For each item the CP2000 lists:** the payer's form (W-2, 1098, 1099) and whether that amount is already somewhere on the return (for example a 1099-NEC already counted in Schedule C gross receipts, or a 1099-B whose basis was not reported to the IRS).
5. **Filing status.** For a joint return, both spouses must sign the CP2000 response form.
6. **For a CP5071 series notice:** did the client file a return for that year? Does the client have the prior-year return and the supporting forms (W-2, 1099, Schedule C, F)? Is the client under 18?
7. **Other items to report** for that year that the notice does not show (credits or deductions missed). These go on Form 1040-X marked "CP2000".
8. **A power of attorney** (Form 2848) if the practitioner will deal with the IRS on the client's behalf beyond this notice.

## The method, step by step

### Rates, bands and thresholds

| Item | Rule | Tax year | Source |
| --- | --- | --- | --- |
| CP2000 response time | 30 days from the date of the notice | Any notice received in 2026 | [Topic 652](https://www.irs.gov/taxtopics/tc652) |
| CP2000 response time, client outside the United States | 60 days from the date of the notice | Any notice received in 2026 | [Topic 652](https://www.irs.gov/taxtopics/tc652) |
| Interest shown on a CP2000 | From the return due date (regardless of extensions) to 30 days from the notice date; it keeps running until paid | Any | [Topic 652](https://www.irs.gov/taxtopics/tc652) |
| Joint return signatures | Both spouses sign the response form | Any | [Topic 652](https://www.irs.gov/taxtopics/tc652) |
| CP5071 series refund timing | Check the refund 2 to 3 weeks after verifying; processing can take up to 9 weeks after verification | Any | [Verify your return](https://www.irs.gov/identity-theft-fraud-scams/verify-your-return) |

### Step 1: identify the notice

- **CP2000** (and the CP2000 series): the Automated Underreporter compared the client's return with information returns (W-2, 1098, 1099) and found a difference. It proposes changes to income, payments, credits or deductions. It can lead to more tax or to a refund. It is not a bill and not an assessment. [Topic 652](https://www.irs.gov/taxtopics/tc652)
- **CP5071, 5071C, CP5071F**: a Form 1040 series return was filed under the client's SSN or ITIN and the IRS needs the client to verify identity and the return before it continues processing. [Understanding your CP5071 series notice](https://www.irs.gov/individuals/understanding-your-cp5071-series-notice)
- Anything else (CP11, CP14, CP501, CP503, CP504, LT11): go to `us-irs-collections-and-controversy`.

### Step 2 (CP2000): match every proposed item

Put each item on the notice in a row: payer, form, amount reported by the payer, where (if anywhere) it is on the return, and the evidence. Each row ends in one of three answers:

| Finding | Answer for that item |
| --- | --- |
| The amount is missing from the return and the form is right | Agree |
| The amount is already on the return under another line or name (for example 1099-NEC in Schedule C gross receipts) | Disagree, show where it is |
| The form is wrong (wrong recipient, duplicate, wrong amount) or the basis was left off a 1099-B | Disagree, attach the corrected form or the basis records; ask the payer to correct the form |

### Step 3 (CP2000): the decision, agree in full, partly or not at all

- **Agree in full** when every row is "Agree" and the client has nothing else to report for that year. Complete, sign and date the response form and send it by the due date. No amended return is needed. [Understanding your CP2000 series notice](https://www.irs.gov/individuals/understanding-your-cp2000-series-notice)
- **Partly agree or disagree** when any row is "Disagree". Mark the box on the response form and send a signed statement explaining why, with the documents for each disputed row. [Topic 652](https://www.irs.gov/taxtopics/tc652)
- **Agree, but with other items to report** (a missed deduction or credit): send Form 1040-X with "CP2000" written on top, with the response form. [Understanding your CP2000 series notice](https://www.irs.gov/individuals/understanding-your-cp2000-series-notice)
- **Paying.** Paying the proposed amount within 30 days stops further interest and possibly further penalties. A client who agrees but cannot pay may ask for a payment plan; the response form must still be signed and returned by the due date. Payment plans: `us-irs-collections-and-controversy`. [Topic 652](https://www.irs.gov/taxtopics/tc652)
- **Never agree to an item to make the notice go away.** Agreeing to income already reported taxes it twice.

### Step 4 (CP2000): send and track

Reply by the IRS Document Upload Tool, by fax to the number for the service centre shown on the notice, or by mail to the address on the notice. Keep proof of the date sent. If there is no reply, or the IRS cannot resolve the difference, it may send another notice and a bill; the next formal step is a statutory notice of deficiency, handled in `us-irs-collections-and-controversy`. Also check the prior years: if the same item was left off before, amend those years. [Understanding your CP2000 series notice](https://www.irs.gov/individuals/understanding-your-cp2000-series-notice)

### Step 5 (CP5071 series): verify identity and the return

1. Use the online service at irs.gov/verifyreturn if the notice offers it; it works only for a CP5071 series notice or Letter 5447C. The client signs in or creates an IRS account and answers questions about the return. [Verify your return](https://www.irs.gov/identity-theft-fraud-scams/verify-your-return)
2. Have to hand: the notice, the return for the year on the notice, the prior-year return if filed, and the supporting forms. [Understanding your CP5071 series notice](https://www.irs.gov/individuals/understanding-your-cp5071-series-notice)
3. If the client did not file the return, use the same service to tell the IRS. Someone may have filed with the client's details.
4. If the client cannot verify online, or is under 18, follow the notice instructions or call the number on it. That number is for verification only; it may not answer refund or other account questions.
5. After verifying, Form 14039 (Identity Theft Affidavit) is not needed unless the IRS asks for it. Suggest an Identity Protection PIN to stop returns being filed under the client's number in future.

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| CP2000 item already reported elsewhere on the return | Disagree for that item; show the line and the ledger |
| CP2000 includes a 1099-B with no basis reported | Disagree; send the basis records; the proposed tax is usually on the gross proceeds |
| CP2000 proposes a refund | Still answer it; agree if right |
| More time needed to answer a CP2000 | Send an extension request by one of the reply options before the due date |
| CP2000 answered, then a statutory notice of deficiency arrives | The 90-day Tax Court clock now controls: `us-irs-collections-and-controversy` |
| CP5071 series notice and the client filed no return | Verify and report it as not filed; possible identity theft |
| CP5071 series notice and the client did file | Verify so processing continues; the refund can follow up to 9 weeks after |
| Letter or text claiming to be the IRS asking for payment by gift card, crypto or wire | Not an IRS notice; do not respond to it; check the client's IRS online account |

### Defaults when a fact is missing

| Missing fact | Default |
| --- | --- |
| Notice date unclear | Treat the earliest plausible date as the notice date and answer early |
| Where the client lives | Use 30 days, not 60 |
| Whether an item is already on the return | Do not agree to it until the return and ledger have been read |

### Red flags to raise with the client

| Flag | Why |
| --- | --- |
| The same item missing in earlier years | The IRS may check those years; amend them |
| A CP2000 the client ignored and a later bill | Interest has kept running; the deficiency route may already have started |
| A CP5071 series notice when the client has not filed yet | Someone else filed first; identity theft steps are needed |

## Worked cases

**Case 1, the decision: agree in full or partly agree.** The client's 2025 CP2000 proposes adding USD 9,200 of income: a 1099-NEC of USD 8,000 and a 1099-INT of USD 1,200. The ledger shows the USD 8,000 is in Schedule C gross receipts. The USD 1,200 of interest is not on the return.

Agreeing in full would accept USD 9,200 of extra income, USD 8,000 of it already taxed. Partly agreeing accepts USD 1,200 and disputes USD 8,000, about 13.04% of the proposed income change agreed. Decision: mark "partly agree", attach a signed statement, the Schedule C, the ledger report and bank entries for the USD 8,000. Agreeing in full would only be right if the 1099-NEC amount were missing from Schedule C too.

```oa-check
name: CP2000 decision, agree in full or partly agree
inputs:
  proposed_nec: 8000
  proposed_int: 1200
  nec_already_reported: 8000
  int_already_reported: 0
steps:
  - proposed_total: proposed_nec + proposed_int
  - disputed: min(nec_already_reported, proposed_nec) + min(int_already_reported, proposed_int)
  - agreed: proposed_total - disputed
  - agreed_share: round(agreed / proposed_total, 4)
  - double_counted_if_full_agree: disputed
expected:
  proposed_total: 9200
  disputed: 8000
  agreed: 1200
  agreed_share: 0.1304
  double_counted_if_full_agree: 8000
```

**Case 2, the response date, client in the United States and abroad.** A CP2000 is dated 14 September 2026, day 257 of 2026. A client in the United States has 30 days: day 287, 14 October 2026 (September ends on day 273). A client living outside the United States has 60 days: day 317, 13 November 2026 (October ends on day 304).

```oa-check
name: CP2000 response date by residence (notice dated 14 Sep 2026)
inputs:
  notice_day: 257
  days_us: 30
  days_abroad: 60
  end_september: 273
  end_october: 304
steps:
  - due_day_us: notice_day + days_us
  - due_day_abroad: notice_day + days_abroad
  - due_date_us_october_day: due_day_us - end_september
  - due_date_abroad_november_day: due_day_abroad - end_october
expected:
  due_day_us: 287
  due_day_abroad: 317
  due_date_us_october_day: 14
  due_date_abroad_november_day: 13
```

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-NOT-DEFICIENCY | A statutory notice of deficiency has been issued | Refer to `us-irs-collections-and-controversy`; Tax Court timing applies |
| R-NOT-FRAUD | The CP2000 suggests omitted income the client hid on purpose | Refer to a tax attorney before any reply |
| R-NOT-BUSINESS | The notice is for a business return (Form 1120, 1065, 941) | Out of scope; refer |
| R-NOT-IDTHEFT | Identity theft confirmed and returns filed for several years | Refer; the Identity Theft Victim Assistance process and Taxpayer Advocate Service apply |
| R-NOT-SCAM | The "notice" asks for payment by gift card, crypto or wire, or came only by text or email | Refuse to act on it; the client checks the IRS online account |

## Filing and payment

| Step | Where | When |
| --- | --- | --- |
| CP2000 response form, signed (both spouses if joint) | IRS Document Upload Tool, fax to the service centre on the notice, or mail to the address on the notice | Within 30 days of the notice date (60 days if living outside the US) |
| Form 1040-X marked "CP2000" (only if other items to report) | With the response form | Same date |
| Payment of an agreed amount | IRS online payment, or mail to the address listed for the service centre | Within 30 days to stop further interest |
| CP5071 series verification | irs.gov/verifyreturn, or as the notice instructs | As soon as the notice arrives; the return is held until then |

## Completion checklist

- [ ] Notice number, date and tax year recorded; response date computed (30 or 60 days).
- [ ] Every CP2000 item matched to the return and the client's records.
- [ ] Response form marked agree, partly agree or disagree; signed by both spouses if joint.
- [ ] Signed statement and documents for each disputed item.
- [ ] Form 1040-X marked "CP2000" only if other items need reporting.
- [ ] Prior years checked for the same omission.
- [ ] For a CP5071 series notice: verified online or by phone; told the IRS if the return was not the client's; IP PIN suggested.
- [ ] Proof of sending kept.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| IRS Topic 652, Notice of underreported income, CP2000. Read for the Automated Underreporter, "isn't a bill", 30 days or 60 days outside the United States, interest to 30 days from the notice date, both spouses' signatures, signed statement on disagreement. | https://www.irs.gov/taxtopics/tc652 | 2026-11-13 |
| IRS, Understanding your CP2000 series notice. Read for reply methods (upload, fax, mail), no amended return when agreeing with nothing else to report, Form 1040-X marked "CP2000", checking prior years. | https://www.irs.gov/individuals/understanding-your-cp2000-series-notice | 2026-11-13 |
| IRS, Understanding your CP5071 series notice. Read for the series (CP5071, 5071C, CP5071F), why it is sent, documents to have, the verification-only phone line, Form 14039 not needed after verifying. | https://www.irs.gov/individuals/understanding-your-cp5071-series-notice | 2026-11-13 |
| IRS, Verify your return. Read for use only with a CP5071 series notice or Letter 5447C, under-18 rule, 2 to 3 weeks and up to 9 weeks refund timing. | https://www.irs.gov/identity-theft-fraud-scams/verify-your-return | 2026-11-13 |

Not yet confirmed: the response deadline printed on a CP5071 series notice (the IRS pages read do not state a fixed number of days, so this skill uses the notice's own instructions); the separate Letter 4883C and 5747C identity letters are not covered.
