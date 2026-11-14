---
name: the-burden-of-proof-in-tax-cases
description: 'Kenyan tax objection and appeal evidence workflow for 2026: statutory burden, reconciliations, valid-objection conditions, deadlines, undisputed tax and referral boundaries.'
jurisdiction: KE
tax_year: 2026
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
version: 0.1
type: situation-rules
category: international
---

# The Burden of Proof in Kenyan Tax Disputes (2026)

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

This supports a Kenyan taxpayer's evidence file and deadline triage after an assessment. It does not decide litigation merits or replace legal representation. [TPA s56(1)](https://www.kra.go.ke/images/publications/Tax-Procedures-Act--2026.pdf) places the burden on the taxpayer in proceedings under the objections/appeals Part to prove the decision incorrect. It does not dispense with the Commissioner's statutory duties or make any arbitrary assessment lawful. Under s31, amendments use available information and best judgment to reach the correct liability; s29 separately governs default assessments.

## Ask the client first

- The assessment/decision, exact notification date, tax head and period.
- Grounds disputed, requested amendments, reasons and supporting records.
- Undisputed tax, payments or an extension/payment arrangement.
- Whether the objection was validly lodged and acknowledged, and any further-information notice.
- Appeal/ADR stage, prior grounds, service records and representation.
- Any fraud allegation, missing records, current challenge or deadline already missed.

## The method, step by step

### Evidence and burden

Build a reconciliation from the declared figure to invoices, eTIMS/ETR records, bank and M-PESA statements, contracts, local purchase orders, delivery notes, stock movements, payroll, audited accounts and schedules. Explain internal transfers and non-income credits rather than treating bank inflows as turnover. Retain an audit trail to source documents. A bank narration inconsistent with the declared position needs explanation and corroboration, not deletion.

Under [TPA ss23,31,51,56](https://www.kra.go.ke/images/publications/Tax-Procedures-Act--2026.pdf), keep records for 5 years from the end of the reporting period (in words on the page), and longer where amended-assessment rules or ongoing proceedings require it. Documents supporting a live dispute must not be destroyed when the ordinary retention period expires. Evidence strength is factual; do not guarantee a win or assume management explanations discharge the burden.

### Rates, bands and thresholds

| Stage | Time threshold and complete condition | Official source |
|---|---|---|
| Object | Within 30 days of notification; precise grounds, amendments and reasons, relevant documents, and undisputed tax paid or extension applied for, s51(2)-(3), in words on the page | https://www.kra.go.ke/images/publications/Tax-Procedures-Act--2026.pdf |
| Invalidity notice/information | Commissioner notifies within 14 days, requests information within 7 days; failure engages s51(4A), in words on the page | https://www.kra.go.ke/images/publications/Tax-Procedures-Act--2026.pdf |
| Objection decision | Within 60 days of receipt of valid notice; otherwise deemed allowed, s51(11), in words on the page. Invalid objections have separate s51(4A) treatment | https://www.kra.go.ke/images/publications/Tax-Procedures-Act--2026.pdf |
| Tribunal appeal | Within 30 days after notification of objection decision, s51(12); undisputed tax paid or payment arrangement at lodging, s52(2), in words on the page | https://www.kra.go.ke/images/publications/Tax-Procedures-Act--2026.pdf |
| High Court appeal | Within 30 days of notification or further time allowed; questions of law only, ss53,56(2), in words on the page | https://www.kra.go.ke/images/publications/Tax-Procedures-Act--2026.pdf |
| Grounds on appeal | Only objection grounds unless Tribunal/Court permits new grounds, s56(3) | https://www.kra.go.ke/images/publications/Tax-Procedures-Act--2026.pdf |

On receipt, record notification, preserve the assessment, gather evidence, separate disputed and undisputed amounts, prepare specific grounds and amendments and obtain professional review before casual replies or meetings. For an amended assessment, s51(5) limits the objection to alterations/additions. Late objection can be requested on statutory grounds under s51(6)-(7); do not assume it is granted.

## Boundary and exception table

| Situation | Response |
|---|---|
| Valid and timely objection | Track receipt, acknowledgement and decision clock |
| Invalid/incomplete objection | Cure the stated defects; do not assume automatic allowance |
| Fraud allegation or asserted heightened standard | Refer for case-law analysis; preserve relevant documents |
| New appeal ground | Seek Tribunal/Court permission; do not assume it is admitted |
| Unnamed constitutional challenge | Current s56(1) remains the source read; no outcome assumed |

## Worked cases

Hypothetical bank credits KES 1,200,000 include documented own transfers KES 200,000 and a loan KES 100,000. Reconciled trading receipts are KES 900,000. If an assessment treats every credit as sales, the disputed base difference is KES 300,000; the documents, not this subtraction alone, support the objection. No tax rate is assumed.

```oa-check
name: Bank-credit assessment reconciliation
inputs:
  credits: 1200000
  own_transfers: 200000
  loan: 100000
steps:
  - trading_receipts: credits - own_transfers - loan
  - base_difference: credits - trading_receipts
expected:
  trading_receipts: 900000
  base_difference: 300000
```

A hypothetical KES 500,000 assessment is challenged by KES 180,000. Undisputed tax is KES 320,000; KES 250,000 credited payment leaves KES 70,000 to pay or cover with the applicable extension/arrangement. Merely disputing part does not satisfy the undisputed-tax condition.

```oa-check
name: Undisputed-tax payment condition
inputs:
  assessment: 500000
  disputed: 180000
  paid: 250000
steps:
  - undisputed: assessment - disputed
  - remaining: max(0, undisputed - paid)
expected:
  undisputed: 320000
  remaining: 70000
```

## When to refuse or refer

Refer litigation, fraud, uncertain notification/service, expired deadlines, disputed validity, new appeal grounds, document gaps and constitutional issues. Do not tell a taxpayer that a letter/email alone necessarily satisfies the current electronic procedure. Confirm the approved channel and retain acknowledgement.

## Filing and payment

Lodge the objection through KRA iTax (https://itax.kra.go.ke), select the relevant decision/assessment and period, specify grounds, requested amendments and reasons, attach relevant documents, address undisputed tax and retain submission acknowledgement. Obtain current Tribunal filing/fee and service directions before appealing; TPA alone does not specify the whole Tribunal filing bundle or portal.

## Completion checklist

Reconcile the declared and assessed figures; retain source evidence; calendar notification, valid objection and appeal stages; record payments/arrangements and submission/service proof; obtain the decision and identify preserved grounds. No deadline is suspended by an informal meeting.

### How FFP Consult helps

We prepare objections, reconciliations, and evidence bundles, represent clients in Alternative Dispute Resolution, and appear before the Tax Appeals Tribunal. The earlier you involve us, the stronger your position. Contact us before the deadline, not after it.
Julian Njoroge Maina
Tax Partner, FFP Consult

## Sources

| Source and passages actually read | Official URL | Read on |
|---|---|---|
| Read for TPA ss23,29,31,51-56; record extensions, amended assessments, objection validity/decision clocks, appeals, burden and grounds | https://www.kra.go.ke/images/publications/Tax-Procedures-Act--2026.pdf | 2026-11-14 |

Not yet confirmed: Current Tribunal Act/rules text on the former 14-day document bundle and KES 20,000 fee, including whether refundable; the old refundable claim is not established. Kenya Law direct fetch produced a robot challenge; the ordinary browser opened a blank page, not readable law. Parliament’s linked file was unrelated and was rejected. The old general balance-of-probabilities/higher-fraud-standard claim and unnamed constitutional challenge require identified current judgments; neither is treated as confirmed here. Absolute iTax-only validity is not stated by s51 itself; confirm current channel requirements.

## Disclaimer

This guide provides general information on Kenyan tax procedure and does not constitute specific tax or legal advice. Treatment of any particular matter depends on its facts. Contact FFP Consult for advice on your situation.

> Contributed by CPA Julian Njoroge Maina, 25241.
