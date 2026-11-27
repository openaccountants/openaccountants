---
name: us-1099-nec-issuance
description: Determine which US business contractor payments need Form 1099-NEC for 2026, with the USD 2,000 threshold, corporate and attorney rules, payment-network exclusions, W-9 and backup withholding conditions, filing, penalties and preserved 2025 cases. Federal only; state and uncommon matters require a partner accountant.
version: "1.1"
jurisdiction: US
tax_year: 2026
last_updated: 2026-11-27
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: situation-rules
---

# US Form 1099-NEC issuance, payments made in 2026

**Answer first.** For a US sole proprietor or disregarded single-member LLC, report business payments for nonemployee services totaling **USD 2,000 or more per payee in calendar 2026**. Apply the corporate exception and its attorney exception. Exclude payment-card and qualifying third-party network transactions from the payer's 1099-NEC. File and furnish the 2026 forms by **1 February 2027**, absent an approved extension. Backup withholding requires a separate test; a missing W-9 signature alone does not establish a withholding duty. [IRS instructions, reporting and exceptions](https://www.irs.gov/instructions/i1099mec); [26 U.S.C. 3406(a), (b)(6), before the 2026 threshold amendment](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleC-chap24-sec3406.htm).

## Scope and who this is for

Federal working papers for those businesses paying US nonemployees in 2026; not filing execution or worker classification. Retain the original 2025 cases below as historical cases, not 2026 instructions. Tax deductibility is a separate question: route bookkeeping to `us-sole-prop-bookkeeping`, Schedule C/SE to `us-schedule-c-and-se-computation`, payroll to `us-form-941-940-payroll`, and payment-processor reporting to `us-1099-k-and-payment-processors`. Load `us-tax-workflow-base` for the wider workflow. This Guide does not establish that an expense is deductible merely because a form was issued or omitted.

**Circular 230 §10.37 working policy:** use the actual facts, identify missing information and refer unresolved positions before filing. This is general guidance for professional review, not a filed return or a professional approval.

## Ask the client first

Collect the payment year; each payee's legal name, address, US/foreign status, federal classification and TIN; W-9 or other valid documentation; every payment and its method; service/merchandise split; attorney or medical involvement; reimbursements and accounting; prior-year reporting and withholding; actual tax withheld; IRS notices and receipt dates; total original information returns required in the filing calendar year; IRIS access; and payer/payee states. Retain the original facts. Do not invent an entity type, payment method or withholding amount when information is missing.

## The method, step by step

### Rates, bands and thresholds

| Item and operative period | Value | Official source |
| --- | --- | --- |
| Nonemployee service payments made in calendar 2026, aggregate per payee | USD 2,000 or more | [Public Law 119-21 §70433(a), (c), (f)](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| Historical 2025 service payments, aggregate per payee | USD 600 or more | [26 U.S.C. 6041A(a), pre-amendment text](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap61-subchapA-partIII-subpartB-sec6041A.htm) |
| Backup withholding, only where the trigger and reportable-payment tests below are met | 24% | [Pub. 1099, part N](https://www.irs.gov/pub/irs-pdf/p1099.pdf) |
| Direct consumer-product sales for resale, outside a permanent retail establishment, on the statutory commission/buy-sell basis | USD 5,000 or more; 1099-NEC box 2 or 1099-MISC box 7 | [26 U.S.C. 6041A(b)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap61-subchapA-partIII-subpartB-sec6041A.htm); [IRS instructions](https://www.irs.gov/instructions/i1099mec) |
| Ordinary late/incorrect IRS return, due in 2027: corrected within 30 days / later but by the statutory August cutoff / later or never | USD 60 / USD 130 / USD 340 per return | [Rev. Proc. 2025-32 §4.57](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Ordinary late/incorrect payee statement, due in 2027, same timing tiers assessed separately | USD 60 / USD 130 / USD 340 per statement | [Rev. Proc. 2025-32 §4.58](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |

**1. Classify each payment.** Only trade or business payments belong here; personal payments do not. Report services, including incidental parts/materials, professional fees, nonemployee directors’ fees, commissions and prizes for services. Do not exclude separately priced incidental parts merely because the invoice separates them. Goods-only purchases are excluded. Include unaccounted travel reimbursements with fees; for accounted reimbursements, hold the treatment for a partner accountant. Employees go to the payroll route, not 1099-NEC. [IRS instructions, exceptions and box 1a](https://www.irs.gov/instructions/i1099mec).

**2. Establish the settlement method.** Card payments and third-party network transactions within §6050W are excluded from the payer's 1099-NEC; the processor's own reporting threshold does not transfer those payments back to the payer. A platform name alone (PayPal, Venmo, Cash App, Stripe or Square) does not establish the transaction's status. Check the transaction record; direct cash, check, ACH, wire or bank transfers including Zelle remain in the payer's test. If the method is unclear, hold the conclusion rather than issue a duplicate form. [IRS instructions, Form 1099-K](https://www.irs.gov/instructions/i1099mec).

**3. Identify the payee and apply the threshold.** Generally exclude corporations, including LLCs taxed as C or S corporations; attorney fees are an exception. For a disregarded LLC use the owner's name and TIN, with the LLC on the second name line as appropriate. Document classification using the W-9; a verbal assertion is not a completed working paper. If documentation is absent or contradictory, do not assume non-corporate US status: apply the documentation/presumption review hold below. [Treas. Reg. 1.6041-3(p)](https://www.ecfr.gov/current/title-26/section-1.6041-3); [W-9 requester instructions](https://www.irs.gov/instructions/iw9); [Pub. 1099, presumption rules](https://www.irs.gov/pub/irs-pdf/p1099.pdf).

For reportable services, test the whole annual amount per payee, not each invoice. Exactly USD 2,000 meets the 2026 threshold; USD 1,999.99 does not, absent the actual-withholding rule below. Report the whole amount, not just the excess. Attorneys' service fees follow this same threshold even when the firm is incorporated: “always report attorneys” does not mean below-threshold fees. [§70433](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm); [IRS attorney instructions](https://www.irs.gov/instructions/i1099mec).

**4. Test backup withholding separately.** Section 3406(a)(1)(A) covers failure to furnish a TIN in the required manner; (B) covers an IRS incorrect-TIN notice. The underreporting and certification-failure triggers in (C) and (D) apply only to reportable interest/dividends, not ordinary contractor compensation. A missing form or signature is not automatically a missing TIN. [26 U.S.C. 3406(a)(1)–(2)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleC-chap24-sec3406.htm).

Under §3406(b)(6), a 2026 service payment is reportable for this purpose if current-year cumulative relevant payments reach USD 2,000, or the payer had to report payments to that payee for the preceding year, or preceding-year reportable payments required backup withholding. Withhold at 24% on applicable payments; do not automatically multiply the entire year's payments by 24% when dates, prior-year status and the trigger are unknown. “Applied for” a TIN does not give contractor compensation the interest/dividend waiting period. [§3406(b)(6)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleC-chap24-sec3406.htm), as amended by [§70433(d), (f)](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm); [Pub. 1099, part N](https://www.irs.gov/pub/irs-pdf/p1099.pdf).

Report actual withholding in box 4 and report the payment even below the ordinary filing threshold if any federal backup withholding was taken. Do not enter tax that was never withheld. Form 945 is required where nonpayroll income tax was withheld or required to be withheld; its deposits and exact filing deadline require a separate review. IRS TIN Matching is available to eligible payers before filing. [IRS box 4 instructions](https://www.irs.gov/instructions/i1099mec); [W-9 requester instructions, TIN matching and Form 945](https://www.irs.gov/instructions/iw9).

**5. Prepare the fields.** Use the form for the actual payment year. For 2026, put reportable service compensation in box 1a and actual federal withholding in box 4. Direct sales use box 2. Boxes 1b–1d (cash tips, occupation codes and overtime), box 3 (excess golden parachutes), and state boxes 5–7 are separate topics held below. The historical 2025 compensation field was box 1; do not retroactively use 2026 box labels for it. [IRS 2026 instructions](https://www.irs.gov/instructions/i1099mec); [2025 form](https://www.irs.gov/pub/irs-prior/f1099nec--2025.pdf).

**6. File and furnish.** The statutory January 31 deadline moves to the next business day when necessary: 2026 forms are due **Monday 1 February 2027**; historical 2025 forms were due **Monday 2 February 2026**. Copy A goes to the IRS and Copy B to the recipient; retain the payer's copy. State copies are held for state review. [26 U.S.C. 6071(c)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap61-subchapA-partV-sec6071.htm); [§7503](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap77-sec7503.htm); [IRS instructions, statements](https://www.irs.gov/instructions/i1099mec).

Count original covered information returns required during the filing calendar year in aggregate, including W-2s, not just NECs. At 10 or more, e-file unless an applicable waiver or exemption applies; corrections do not enter the threshold count, but a correction to a required electronic original must also be electronic. Five NECs plus six W-2s equals 11. W-2 filing remains with the Social Security Administration. [Treas. Reg. 301.6011-2(b)–(d)](https://www.ecfr.gov/current/title-26/section-301.6011-2).

For these information returns the IRS identifies IRIS as the intake system beginning tax year 2026/filing season 2027; FIRE stops accepting current, prior-year and correction submissions after its 2026 shutdown. Arrange an IRIS TCC before filing season; the typical application takes 45 business days but can vary. If paper filing is permitted, use compliant Copy A with a separate Form 1096 for each form type. Do not send the same return both electronically and on paper. Keep copies or reconstructible data at least 3 years from the due date, or 4 years when federal withholding was imposed. [Pub. 1099, What's New and parts E–F](https://www.irs.gov/pub/irs-pdf/p1099.pdf).

There is no automatic 1099-NEC filing extension. A filing-extension request uses Form 8809; a recipient-statement extension is a separate Form 15397 request. Do not assume either request was granted. [Pub. 1099, parts C and M](https://www.irs.gov/pub/irs-pdf/p1099.pdf).

**7. Correct errors.** Correct IRS returns and recipient statements promptly, subject to applicable reasonable-cause and de minimis exceptions; hold those exception claims for the partner accountant. Paper amount/code/checkbox errors generally use the one-return procedure; missing/incorrect payee TIN, name or wrong return type use the two-return procedure: identify/zero the incorrect return, then file the correct one. Do not use VOID for a correction. Electronic corrections follow the relevant IRIS procedure (Pub. 5717 portal / Pub. 5718 A2A); do not use the paper algorithm universally. [Pub. 1099, parts F and H](https://www.irs.gov/pub/irs-pdf/p1099.pdf).

**8. Calculate ordinary penalties only with complete facts.** IRS-return and recipient-statement failures are separate. The middle tier ends August 1 of the calendar year of the relevant due date, subject to the weekend/holiday rule. Thus for ordinary 2026 forms due 1 February 2027 the 30-day window ends 3 March 2027, and the August window ends 2 August 2027. Rev. Proc. 2025-32's §4.57/4.58 tables print “August 1, 2026”; follow the operative filing-year rule in §§6721(b)(2)/6722(b)(2), not that inconsistent year. [§6721](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapB-partII-sec6721.htm); [§6722](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapB-partII-sec6722.htm); [§7503](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap77-sec7503.htm).

Reasonable cause, without willful neglect, can remove a penalty; it is not automatic. Caps, intentional disregard and de minimis exceptions require the review hold below before an assessment is final. Respond to a notice by its stated date. [26 U.S.C. 6724(a)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapB-partII-sec6724.htm).

## Boundary and exception table

Each following hold is **non-usable for filing or deciding the issue**. Keep the actual facts and route it; no numeric or categorical conclusion is supplied by this Guide.

| Topic retained from current or historical text | Action |
| --- | --- |
| Missing/contradictory US status, payee classification, TIN documentation, or ambiguous settlement method | Check this point with one of our partner accountants. |
| Worker classification, full-time controlled contractor, Form SS-8/state ABC tests | Check this point with one of our partner accountants. |
| Foreign/nonresident payee; W-8BEN, Form 1042-S, §1441/treaty withholding | Check this point with one of our partner accountants. |
| Medical/health care and corporate exceptions; own health insurance; 1099-MISC box 6 | Check this point with one of our partner accountants. |
| Attorney settlement/gross proceeds, claimant reporting, 1099-MISC box 10, distinct from service fees | Check this point with one of our partner accountants. |
| Fish for resale/cash purchases, substitute dividends/interest, royalties/rents, other 1099-MISC/INT/DIV payments | Check this point with one of our partner accountants. |
| Deceased payee/estate, married qualified joint venture, staffing agency/intermediary | Check this point with one of our partner accountants. |
| Accounted contractor reimbursements, virtual currency valuation and reporting | Check this point with one of our partner accountants. |
| Cash tips/occupation codes/overtime and excess golden parachute fields | Check this point with one of our partner accountants. |
| CP2100/CP2100A, first/second B-notice, three-year repeat notices, IRS/SSA validation and start/stop withholding dates | Check this point with one of our partner accountants. |
| Form 945 deadline, deposits, liability for uncollected tax or missing-TIN payment history | Check this point with one of our partner accountants. |
| State thresholds, state copies, Combined Federal/State Filing participation; no exemption inferred from absence of a wage income tax | Check this point with one of our partner accountants. |
| Annual penalty caps, gross-receipts averaging, intentional disregard, de minimis/error exceptions, waiver and extension eligibility | Check this point with one of our partner accountants. |

## Worked cases

The ordinary reporting results below are conditional on business service payments to documented US nonemployees by check/ACH, with no backup-withholding trigger, except where a case states otherwise. These are branch assumptions, not missing facts supplied for a real client; establish the method/status before using a result. Cases do not establish deductibility.

**Case 1 — 2026 threshold sort.** Original facts: the designer's sole proprietorship paid non-corporate contractors with W-9s: copywriter USD 1,950, developer USD 2,000, photographer USD 8,500 and office-dog walker eight payments of USD 80 = USD 640. Two NECs: developer USD 2,000 and photographer USD 8,500, box 1a, due 1 February 2027. Under the historical 2025 threshold these amounts would produce four forms; the separate original dog-walker case remains a 2025 case below.

```oa-check
name: 2026 threshold sort and historical comparison
inputs:
  copywriter: 1950
  developer: 2000
  photographer: 8500
  dog_payments: 8
  dog_each: 80
  threshold: 2000
steps:
  - dog_walker: dog_payments * dog_each
  - copywriter_form: floor(min(copywriter, threshold) / threshold)
  - developer_form: floor(min(developer, threshold) / threshold)
  - photographer_form: floor(min(photographer, threshold) / threshold)
  - dog_walker_form: floor(min(dog_walker, threshold) / threshold)
  - forms_required: copywriter_form + developer_form + photographer_form + dog_walker_form
expected:
  dog_walker: 640
  copywriter_form: 0
  developer_form: 1
  photographer_form: 1
  dog_walker_form: 0
  forms_required: 2
```

**Case 2 — six missed 2026 forms.** Original facts: small business, gross receipts well under USD 5,000,000, discovers on 20 February 2027 that six 2026 NECs were neither filed nor furnished. Ordinary potential exposure, before relief/caps and assuming no intentional disregard: both copies corrected by 3 March 2027, 6 × USD 60 × 2 = USD 720; later but by 2 August 2027, 6 × USD 130 × 2 = USD 1,560; later or never, 6 × USD 340 × 2 = USD 4,080. Filing now saves USD 3,360 compared with the last tier. Confirm each copy's actual correction date. A USD 3,600 payee with no W-9 does not by itself establish USD 864 due: USD 864 is only 24% of the whole amount; determine the actual TIN and payment/prior-year history. That withholding conclusion is non-usable pending the Form 945/missing-TIN hold. Check this point with one of our partner accountants.

```oa-check
name: Six missed 2026 forms and conditional whole-payment arithmetic
inputs:
  forms: 6
  tier_30_days: 60
  tier_aug_1: 130
  tier_general: 340
  unwithheld_payee: 3600
steps:
  - within_30_days: forms * tier_30_days * 2
  - by_august_cutoff: forms * tier_aug_1 * 2
  - after_august_cutoff: forms * tier_general * 2
  - saving_filing_now: after_august_cutoff - within_30_days
  - whole_payment_arithmetic_only: unwithheld_payee * 0.24
expected:
  within_30_days: 720
  by_august_cutoff: 1560
  after_august_cutoff: 4080
  saving_filing_now: 3360
  whole_payment_arithmetic_only: 864
```

**Original individual cases — preserve both payment years.** Historical 2025 service compensation uses box 1 and deadline 2 February 2026; the corresponding 2026 cases use box 1a and deadline 1 February 2027. The 2025 USD 600 threshold must never be substituted into a 2026 answer.

| Original facts | Historical 2025 result | Existing 2026 result |
| --- | --- | --- |
| Freelance graphic designer, individual/SSN, W-9, USD 8,500 | Report USD 8,500; no federal tax withheld | Report USD 8,500; no federal tax withheld |
| IT firm, W-9 shows S corporation, USD 12,000 | Corporate exception: no NEC | Corporate exception: no NEC |
| “Smith and Jones, P.C.”, C corporation, contract review, USD 4,200 | Attorney fee: report USD 4,200 | Attorney fee: report USD 4,200 |
| Handyman, no W-9, USD 3,600, no withholding performed | Actual withholding box 4 is zero. Reporting/TIN status and liability held; USD 864 is whole-payment arithmetic only. Check this point with one of our partner accountants. | Same hold and original inputs; never insert USD 864 in box 4. Check this point with one of our partner accountants. |
| Virtual assistant, W-9 individual, USD 2,400 via original PayPal Business / current Goods and Services example | No payer NEC if the transaction was a qualifying third-party network transaction; hold if “Business” alone does not establish that | Same condition; no payer NEC for a qualifying transaction, even if processor issues no 1099-K |
| Dog walker, individual/W-9, eight USD 80 payments = USD 640 | Original 2025 test: report USD 640 | Current 2026 sort: below threshold, no NEC absent actual withholding |
| Attorney's law firm, USD 1,500 service fees | Historical comparison: report, subject to stated business-payment assumptions | Existing 2026 case: below threshold, no NEC absent actual withholding |

**Original 2025 late-filing case.** Three NECs for TY2025 filed 15 March 2026; small business gross receipts below USD 5 million. The due date was 2 February 2026: 41 days late, not the original 42. Potential ordinary IRS penalty 3 × USD 130 = USD 390. If the three recipient statements were also corrected in that same middle window, an additional USD 390 gives USD 780 total. Do not infer the statement dates from the IRS filing date. [Rev. Proc. 2024-40 §§2.58–2.59, returns/statements due 2026](https://www.irs.gov/pub/irs-drop/rp-24-40.pdf).

```oa-check
name: Original 2025 three-form case and e-file aggregate
inputs:
  forms: 3
  middle_tier: 130
  nec_returns: 5
  w2_returns: 6
  dog_payments: 8
  dog_each: 80
steps:
  - irs_penalty: forms * middle_tier
  - if_statements_also_late: irs_penalty * 2
  - total_original_returns: nec_returns + w2_returns
  - original_dog_walker: dog_payments * dog_each
expected:
  irs_penalty: 390
  if_statements_also_late: 780
  total_original_returns: 11
  original_dog_walker: 640
```

## When to refuse or refer

Prepare the payee list, documented decisions and form data for professional review. Do not transmit returns in this workflow, invent a missing fact, report qualifying card/network payments twice, omit a withholding duty, issue NEC for known employee wages, or assume a filing extension. Requests to restructure payments solely to suppress reporting, disputed classification, and every boundary-table hold: Check this point with one of our partner accountants.

## Completion checklist

Reconcile all service payees and payment years; document payment-network exclusions and classification; apply the annual threshold and actual-withholding exception; distinguish actual tax withheld from potential liability; verify aggregate filing count and access; record IRS/recipient filing evidence and copies; and leave each hold visibly non-usable until the referred point is resolved.

## Sources

| Official source and sections actually read | Read on |
| --- | --- |
| [Public Law 119-21 §70433(a)–(f)](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm): threshold, indexing after 2026, withholding cross-reference and payment-date commencement; this law controls unrevised regulation/2024 Code threshold text. | 2026-11-27 |
| [26 U.S.C. 6041A(a), (b)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap61-subchapA-partIII-subpartB-sec6041A.htm): 2025 threshold, aggregation and direct sales; read with amendment above. | 2026-11-27 |
| [IRS 1099-MISC/NEC instructions, rev. 12/2026](https://www.irs.gov/instructions/i1099mec): reporting, exceptions, attorney fees, materials, reimbursements, fields and statements. | 2026-11-27 |
| [26 U.S.C. 3406(a), (b)(3)–(6)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleC-chap24-sec3406.htm): trigger restrictions and current/prior-year tests, read with §70433. | 2026-11-27 |
| [Treas. Reg. 1.6041-3(c), (p)](https://www.ecfr.gov/current/title-26/section-1.6041-3): merchandise and corporate exceptions; [W-9 requester instructions](https://www.irs.gov/instructions/iw9): disregarded entity, TIN Matching and Form 945. | 2026-11-27 |
| [Treas. Reg. 301.6011-2(b)–(d)](https://www.ecfr.gov/current/title-26/section-301.6011-2): aggregation, corrections, electronic threshold and hardship waiver. | 2026-11-27 |
| [Pub. 1099 (2026), What's New, E–H, J, M–N and presumption rules](https://www.irs.gov/pub/irs-pdf/p1099.pdf): IRIS transition, paper/corrections, records, names/TINs, extensions and withholding. | 2026-11-27 |
| [26 U.S.C. 6071(c)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap61-subchapA-partV-sec6071.htm) and [7503](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap77-sec7503.htm): due dates and weekend/holiday rule. | 2026-11-27 |
| [Rev. Proc. 2025-32 §§4.57–4.58](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf), [6721(a)–(c)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapB-partII-sec6721.htm), [6722(a)–(c)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapB-partII-sec6722.htm) and [6724(a)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapB-partII-sec6724.htm): 2027 ordinary penalty tiers, operative timing, exceptions and reasonable cause. | 2026-11-27 |
| [Rev. Proc. 2024-40 §§2.58–2.59](https://www.irs.gov/pub/irs-drop/rp-24-40.pdf): historical penalty tier for returns/statements due 2026; [2025 Form 1099-NEC](https://www.irs.gov/pub/irs-prior/f1099nec--2025.pdf): historical box labels. | 2026-11-27 |

Not yet confirmed for usable guidance: the boundary-table issues are non-usable referrals, including state law, B-notice mechanics, rare payees/payments and final assessment/extension conditions. No rate for payments made after 2026 is supplied.
