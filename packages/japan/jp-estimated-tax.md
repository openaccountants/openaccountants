---
name: jp-estimated-tax
description: Use this skill for Japanese individual estimated income tax prepayments (yotei nozei / 予定納税), the notified baseline, instalments, reduction applications, non-payment interest and payment reconciliation. Trigger on 予定納税基準額, 減額申請, Japanese advance tax or freelancer prepayments. Resident individual ordinary regime; special agriculture, non-residence, foreign credits and corporations require separate review.
version: 2.1
jurisdiction: JP
tax_year: 2026
last_updated: 2026-11-14
depends_on:
  - income-tax-workflow-base
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
---

# Japan estimated income-tax payments v2.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Resident individuals, including self-employed people, freelancers and sole proprietors, under the ordinary 2026 estimated-payment regime. Income tax and reconstruction income tax are included together in the baseline. Japan's National Tax Agency (国税庁, NTA) administers this; amounts are JPY. These payments credit the final annual return; they are not deductible business expenses.

| Quick reference | Amount/condition | Official source |
| --- | --- | --- |
| Obligation threshold | Notified baseline at least JPY 150,000, including reconstruction income tax | Income Tax Act art. 104; Reconstruction Finance Act art. 16: https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/2040.htm |
| Ordinary instalments | Each 1/3 of baseline, rounded down to JPY 100 | Income Tax Act art. 104(1),(3), figure written in words on the statute page: https://laws.e-gov.go.jp/law/340AC0000000033 |
| Ordinary payment periods | 1-31 July and 1-30 November; holiday/extension rules apply | Income Tax Act art. 104; General Tax Act arts. 10-11: https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/2040.htm |
| Special agricultural regime | Separate rule: 1/2 of baseline in second period only; do not use the ordinary pair | Income Tax Act art. 107: https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/2040.htm |
| Reduction dates | Ordinarily 15 July or 15 November; shift for holidays and late notice as law provides | Income Tax Act art. 111: https://www.nta.go.jp/taxes/tetsuzuki/shinsei/annai/shinkoku/annai/02.htm |

The final amount is actual annual tax after the other credits less estimated payments shown for the year. It is **not** automatically the remaining 1/3 of the baseline. A refund can arise.

## Ask the client first

Minimum: NTA notice stating the 予定納税基準額 and instalments, prior-year final return and current residence status. Without a confirmed baseline, HARD STOP: no computed payment instruction. Obtain income types, source and withholding documents; blue-return status; foreign credit/disaster relief; current income/deduction changes; payment notices, bank records, direct-debit registration and any reduction/extension decision. Reconcile the notice against the return rather than inventing a baseline from a bank debit.

Preserved referrals:

- **R-JP-ET-1 -- Cross-border income:** Foreign-source income or treaty-credit timing needs a Japanese tax accountant (zeirishi); the baseline has special foreign-credit adjustments.
- **R-JP-ET-2 -- Non-resident estimated tax:** Separate rules, not computed here.
- **R-JP-ET-3 -- Corporate estimated tax:** Corporate prepayments are not individual 予定納税.
- Special agricultural status, death/departure, disasters or an exceptional notice must be reviewed before the ordinary calculation.

## The method, step by step

### Establish the baseline

Use the NTA's notice, ordinarily sent by 15 June. The baseline generally starts from the previous year's declared amount as fixed at 15 May. A smaller amount fixed later within the statutory interval can change it (Income Tax Act arts. 105-106). Do not simply take the last year's total tax before withholding.

NTA No. 2040 excludes specified non-recurring/separately taxed items, including capital gains, occasional income, miscellaneous income, timber and retirement, subject to its explicit exception for separately taxed listed-share dividends. Prior-year foreign tax credit or disaster relief also requires its special baseline computation. Corresponding excluded-income withholding is left out; reconstruction tax is included. In particular, miscellaneous income is not automatically recurring income eligible for the baseline merely because it was earned repeatedly. The exact notice takes precedence over a shorthand spreadsheet formula.

Blue approval does not itself alter the instalment fraction or calendar. New activity with no prior assessed baseline generally has no prepayment; check the notice and complete prior-year position, not merely whether the client says they filed a return.

### Compute and reconcile

If the confirmed baseline is below the threshold, the ordinary liability is nil. Otherwise each ordinary instalment is `floor(baseline / 3 / 100) * 100`. For the special agricultural regime refer rather than using that formula. Compare the result with both notice lines before instructing payment.

At annual filing enter the total notified estimated-payment amount in **予定納税額** as the current-year NTA notice instructs. Reconcile payments and any unpaid collection separately; do not omit the notice credit merely because the cash proof is missing, or count a debit twice. The annual balance can differ from a third of the old baseline, and an excess can produce a refund. `jp-income-tax` owns the annual tax computation; this file supplies the reconciled prepayment schedule.

### Payment and bank classification

These are bookkeeping matching aids, not evidence that a liability has been settled. Match exact tax, year, period and amount to the notice and payment result.

| Pattern | Classification and check |
| --- | --- |
| 税務署 / tax office | Possible prepayment; verify tax and notice |
| 予定納税 / 予定 | Candidate estimated payment |
| 所得税 / 申告所得税 | Could be final tax or prepayment; identify period |
| 振替納税 | Registered direct debit; verify actual successful debit |
| e-Tax + 所得税 + 予定 | Electronic estimated payment; retain payment result |
| 納付書 | Payment slip; inspect tax/year/instalment |
| クレジットカード + 国税 | Possible card tax payment; separate service fee and verify completion |
| Pay-easy + 国税 | Possible electronic banking payment; verify completion |
| 消費税 / 住民税 | Exclude from income-tax prepayment; consumption/local tax |
| 国民健康保険 / 国民年金 | Exclude; social insurance, potentially separate income deduction |
| 加算税 / 延滞税 | Exclude from principal credit; surcharge/interest |
| 還付金 | Refund; reconcile nature before classification |

July/August, November/December and February/March date ranges from the old matching library are only search windows. They do not prove payment type or a delayed statutory debit. For 2026 the NTA's actual ordinary prepayment debit dates are **31 July and 30 November**, the same as the ordinary due dates. The old assertion of an automatic 1-month grace period is wrong. Final-return payments around February/March are not estimated instalments without notice evidence. A bank row `2025/07/31 ; 振替納税 所得税予定1期 ; 出金 ; -200,000 ; JPY` remains a historical matching fixture, not proof of a current liability.

### Reduction application

A lower annual estimate following closure, suspension, declining income, unemployment, disaster/theft/embezzlement, new dependants, medical/insurance expenses or other increased deductions/credits can support an application. Do not reduce cash payments on the client's own forecast alone.

1. Compute the supported annual **申告納税見積額** from the position at 30 June for the July application or 31 October for the November application. This is a projected full-year amount, not merely the tax on income earned to that date. Include reconstruction tax. NTA's 2026 instruction specifically excludes the new 2026 basic-deduction revision from this estimate; the change is settled at final filing.
2. Complete **令和8年分所得税及び復興特別所得税の予定納税額の7月（11月）減額申請書**, stating estimate, reasons and supporting facts. Attach documents based on transaction records, not an unexplained income-drop percentage.
3. Submit through e-Tax software to the competent tax office, or by paper delivered/posted. First-time electronic applicants obtain a user identification number. Retain receipt and copy.
4. Await the tax office's approval, revised estimate or rejection and reasons. Article 113 mandates approval for the named events reducing the estimate, or otherwise when the estimate is at most 70% of the relevant baseline/previous approved estimate; other cases require the statutory decision, not a presumed automatic entitlement. Keep the official decision with the working paper.
5. An approved July reduction generally replaces each instalment with 1/3 of the approved estimate. An approved November ordinary-regime reduction is **1/2 of approved estimate less the first instalment liability**, with the subtraction **inside** the halving: `(approved estimate - first instalment liability) / 2`, rounded down to JPY 100. Follow the revised notice where the result or prior adjustments need interpretation. Approved estimate below JPY 150,000 means no reduced instalment under art. 114(4).

A forecast 50% fall in revenue is not itself a 50% fall in tax. Have the zeirishi check the forecast and application; missed deadlines require separate relief analysis. The old unsourced claim of an automatic penalty merely for a low estimate is held under Sources, not a usable rule.

## Boundary and exception table

| Situation | Action | Official source |
| --- | --- | --- |
| Excluded income or prior foreign tax credit/disaster relief | Rebuild under the specific baseline rule and reconcile NTA notice | NTA No. 2040 calculation section: https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/2040.htm |
| Low income now but unrevised notice | Apply for reduction; do not unilaterally reduce payment | Income Tax Act arts. 111-114: https://www.nta.go.jp/taxes/tetsuzuki/shinsei/annai/shinkoku/annai/02.htm |
| Disaster extension puts instalment deadline after year-end | That extended instalment is treated as absent under the special rule; confirm actual extension | Income Tax Act art. 104(2): https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/2040.htm |
| Failed direct debit | Interest can run from the original deadline, not failed-debit discovery | NTA No. 2040 payment notes: https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/2040.htm |
| Late notice | Statutory application extension may apply, not a guessed new date | Income Tax Act art. 111(3): https://laws.e-gov.go.jp/law/340AC0000000033 |

## Worked cases

Inputs are fixtures. Derived results, estimated and not reviewed. First-year/no-baseline and foreign-credit cases remain conditional routing cases rather than dummy arithmetic.

### Ordinary liability, threshold and final refund

```oa-check
name: Ordinary two instalments and final refund
inputs:
  baseline: 600000
  actual_after_other_credits: 300000
steps:
  - first: floor(baseline / 3 / 100) * 100
  - second: first
  - credit: first + second
  - refund: max(credit - actual_after_other_credits, 0)
expected:
  first: 200000
  second: 200000
  credit: 400000
  refund: 100000
```

At a baseline of JPY 120,000 there is no ordinary instalment; at exactly JPY 150,000 there are 2 instalments of JPY 50,000. A baseline of JPY 600,250 gives JPY 200,000 each after rounding, not JPY 200,083.33.

### Approved November reduction

```oa-check
name: November reduction uses one half after subtracting first liability
inputs:
  approved_annual_estimate: 300000
  first_liability: 200000
steps:
  - second_reduced: floor((approved_annual_estimate - first_liability) / 2 / 100) * 100
  - total_liability: first_liability + second_reduced
expected:
  second_reduced: 50000
  total_liability: 250000
```

### Late payment, corrected calendar and rounding

JPY 200,000 due 31 July 2026 and paid 15 October is 76 days late: 61 days from 1 August through 30 September at the lower rate, then 15 days at the higher rate. Two calendar months are not a fixed 60 days. No partial payments or exclusions are assumed.

```oa-check
name: 2026 estimated payment late through 15 October
inputs:
  unpaid: 200000
  lower_days: 61
  higher_days: 15
steps:
  - interest_base: floor(unpaid / 10000) * 10000
  - raw_interest: interest_base * 0.028 * lower_days / 365 + interest_base * 0.091 * higher_days / 365
  - rounded_interest: floor(raw_interest / 100) * 100
expected:
  rounded_interest: 1600
```

The old JPY 1,551 example used historical rates, a fixed 60-day split and no statutory final rounding. It is not a payment instruction for 2026.

## When to refuse or refer

Keep all named referrals above. Do not compute without the confirmed baseline or reduce without the official reduction basis. Do not include excluded capital/retirement/occasional/miscellaneous items by calling them recurring. Do not use the ordinary fraction for special agriculture. Do not assess withholding non-payment surcharge on an estimated income-tax instalment: late estimated principal is subject to interest under General Tax Act art. 60(1)(4); annual-return penalties are a separate question. Refer cross-year interest, partial payments, disasters, disputed notices and questionable estimates. Every output is estimated until professionally reviewed.

## Filing and payment

| Event | Date or amount | Official source |
| --- | --- | --- |
| 2026 first ordinary instalment | 1-31 July; bank debit 31 July | NTA 2026 leaflet pp. 2-3: https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/pdf/2040_01.pdf |
| 2026 second ordinary instalment | 1-30 November legally; counter-payment business days start 2 November; debit 30 November | Same: https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/pdf/2040_01.pdf |
| July reduction filing | 1-15 July; based on 30 June position | Income Tax Act arts. 111-112: https://www.nta.go.jp/taxes/tetsuzuki/shinsei/annai/shinkoku/annai/02.htm |
| November reduction filing | 1-15 November ordinarily; 2026 deadline 16 November, derived because 15 November is Sunday | Same; holiday rule: https://www.nta.go.jp/taxes/tetsuzuki/shinsei/annai/shinkoku/annai/02.htm |
| Final 2026 return and payment | Ordinarily 16 February-15 March 2027; specific extensions separate | Income Tax Act art. 120: https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/2020.htm |
| Convenience-store QR limit | At most JPY 300,000; cash, no receipt certificate (payment receipt supplied) | NTA payment procedure: https://www.nta.go.jp/taxes/nozei/nofu/conveni_qr_nofu/index.htm |
| Late interest incurred in 2026 | 2.8% annually through first 2 calendar months, 9.1% thereafter; split at calendar-year changes | General Tax Act art. 60; special rates: https://www.nta.go.jp/taxes/nozei/entaizei/keisan/entai_wariai.htm |
| Historical interest incurred in 2025 | 2.4% / 8.7%, historical use only | Same: https://www.nta.go.jp/taxes/nozei/entaizei/keisan/entai_wariai.htm |
| Interest rounding | Base down to JPY 10,000; final down to JPY 100; entire charge below JPY 1,000 omitted (in words on statute page) | General Tax Act arts. 118(3),119(4): https://laws.e-gov.go.jp/law/337AC0000000066 |

Use the notice's correct year, tax and period for payment slip, bank counter, registered debit, Pay-easy/internet banking, e-Tax direct payment or card payment. A filing receipt is not payment proof. For convenience-store QR create the code in NTA/e-Tax, obtain the kiosk barcode and pay cash at the designated counter; retain the payment receipt. Check the notice and funded account before each registered debit. Card fees and other payment-method conditions require that method's live NTA instruction.

## Completion checklist

- Confirmed notice and prior return; baseline exclusions, withholding and reconstruction tax reconciled.
- Threshold includes equality; each ordinary instalment divided by 3 and rounded correctly.
- Special agriculture, foreign credits, disaster and residence issues resolved or referred.
- Reduction evidence, timely application and actual decision retained; approved November formula correct.
- Payment route, successful settlement and actual 2026 debit dates recorded.
- Annual notice credit and unpaid collection distinguished; no duplicate credit or business deduction.
- Interest uses correct year, calendar-month periods and statutory rounding; output estimated, not reviewed.

## Sources

| Source | Official URL | Read on | Operative material read |
| --- | --- | --- | --- |
| NTA No. 2040 | https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/2040.htm | 2026-11-14 | Read for entire baseline calculation, excluded-income and foreign-credit/disaster cases, thresholds, ordinary/agricultural fractions, deadlines, extension and failed-debit notes; law dated 1 June 2026 |
| NTA 2026 estimated-payment leaflet | https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/pdf/2040_01.pdf | 2026-11-14 | Read for notice credit, baseline, both actual 2026 debit dates, counter dates and payment instructions, pp. 1-4; malformed extracted form image not used as a box map |
| Income Tax Act arts. 104-114 | https://laws.e-gov.go.jp/law/340AC0000000033 | 2026-11-14 | Read for full main arts. 104-114 through official e-Gov API, text effective 1 October 2026; ordinary rounding, baseline dates, agriculture boundary, reductions and late notice |
| Reconstruction Finance Act art. 16 | https://laws.e-gov.go.jp/law/423AC0000000117 | 2026-11-14 | Read for entire combined baseline and reconstruction-tax prepayment rule, official e-Gov API text effective 1 April 2026 |
| NTA reduction procedure A1-3 | https://www.nta.go.jp/taxes/tetsuzuki/shinsei/annai/shinkoku/annai/02.htm | 2026-11-14 | Read for conditions, annual forecast, 2026 deduction restriction, forms, dates, attachments, submission and decision/review routes |
| General Tax Act arts. 60,118,119 | https://laws.e-gov.go.jp/law/337AC0000000066 | 2026-11-14 | Read for estimated-payment interest, calendar-month boundary and all rounding paragraphs, official e-Gov API text effective 1 November 2026 |
| NTA interest schedule | https://www.nta.go.jp/taxes/nozei/entaizei/keisan/entai_wariai.htm | 2026-11-14 | Read for lower/higher rates and 2025/2026 rows, not interest-tax or refund-addition columns |
| NTA No. 9205 | https://www.nta.go.jp/taxes/shiraberu/taxanswer/osirase/9205.htm | 2026-11-14 | Read for interest commencement, two calendar months and principal-only basis |
| NTA No. 2020 | https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/2020.htm | 2026-11-14 | Read for final-return reconciliation, filing/payment dates, forms and payment routes |
| NTA convenience-store QR | https://www.nta.go.jp/taxes/nozei/nofu/conveni_qr_nofu/index.htm | 2026-11-14 | Read for amount ceiling, cash requirement, code creation, barcode payment and receipt distinction |

Not yet confirmed: case-specific foreign tax credit or disaster relief; special agricultural baseline computation beyond the referral; non-resident/corporate prepayment computation; card payment fees/limits; annual interest rates after 2026; a specific client's notice, reduction decision or payment; the old claim that an unreasonably low forecast automatically incurs a penalty. Bank timing/narrations are matching aids, not independently validated bank specifications.
