---
name: nz-company-income-tax-ir4
description: "Use for an ordinary New Zealand resident company’s 2025-26 income-tax reconciliation and 2026 IR4 filing handoff. Trigger on company tax, IR4, company income tax, residual income tax, company withholding credits or accounting profit to taxable income. Covers an evidenced ordinary company-rate base, selected return boxes, credit ordering, actual provisional payments and refund limitations. It requires confirmed company status, residence, balance date and supported adjustments. It does not determine special regimes, loss eligibility, cross-border treatment, full imputation-account operations or Companies Office reporting. Produce working papers for qualified review, not an automatically filed return."
jurisdiction: NZ
category: international
tier: 2
review_status: pending_review
tax_year: 2026
tax_year_notes: "2025-26 ordinary resident company; standard year 1 April 2025 to 31 March 2026; 2026 IR4"
last_updated: 2026-11-13
version: 0.1
depends_on:
  - workflow-base
  - corporate-income-tax-workflow-base
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# New Zealand company income tax and IR4 v0.1

## Scope and period

This source-cited working-paper guide covers an ordinary New Zealand resident company’s 2026 IR4 for 1 April 2025 to 31 March 2026, with a confirmed 31 March balance date. Confirm the entity, tax residence, ordinary company-rate status and every material income, deduction, credit and payment. A company name or incorporation alone does not establish all tax conditions. Load both workflow bases; their intake, source gates, refusals, outputs and qualified-review requirements apply.

The selected core reconciles supported accounting-to-tax adjustments, ordinary business income, established NZ interest/dividend amounts, losses already verified as available, permitted credits and actual provisional payments. An accounts entry, supplier name or bank narration does not prove treatment. Keep unresolved items and amounts in the reconciliation. Do not silently omit them, use unproved zeros or present incomplete figures as a complete return.

The Income Tax Act consolidation checked is dated 4 September 2026. BB 1, BC 4–6, Schedule 1 Part A clause 2 and the annual-rates Act’s section 3 establish the selected 2025-26 charge, base and ordinary rate. The live 13-source unincorporated-amendment set was matched to retained texts screened for these provisions. This is a scoped check, not whole-Act assurance. The currently served form and guide are IR4 2026 and April 2026 IR4GU. [ITA core][S6], [Schedule 1][S7], [annual rates][S8], [IR4][S1], [IR4GU][S2].

Non-residents, dual residence, branches, LTCs, Māori authorities, PIEs/funds, charities, qualifying-company regimes, groups/subventions, property regimes, financial-arrangement determinations, foreign/CFC/FIF income, FITC, R&D/other incentives, restructuring, Pillar Two, full ICA operations and deferred-tax recognition require separate current analysis. Unknown applicability requires Needs Input. This guide supplies no zero-rate or inapplicability conclusion for them. Companies Office incorporation, annual returns and statutory financial reporting remain separate obligations.

## Filing, payment and schedule handoffs

Active resident companies generally file IR4 each year; LTCs file IR7. Zero tax does not make a company non-active. An accepted non-active declaration and all applicable conditions must be established before treating filing as excused. IRD identifies income, deductions, asset disposals, relevant transactions, GST cessation and group-withdrawal conditions. Do not infer an exemption, stop returns or cease another registration merely from no sales. [IR4GU p 5][S2], [Non-active companies][S5].

| Item | Selected standard-year rule | Condition |
| --- | --- | --- |
| 2026 IR4 filing | 7 July 2026 | Unless a valid extension applies |
| Agent filing extension | May extend to 31 March 2027 | Confirm the company’s actual extension; agent engagement is not itself proof |
| 2026 terminal income tax | Nominal 7 February 2027; 9 February 2027 after the Sunday and observed 8 February holiday | Calendar derivation; confirm actual myIR conditions |
| Extended terminal payment | May extend to 7 April 2027 | Confirm applicable agent/extension conditions |
| Ordinary 2027 provisional dates | Generally 28 August 2026, 15 January 2027 and 7 May 2027 | Dates alone do not establish liability/options. Six-monthly GST, ratio/AIM, initial liability and changed balance dates need separate schedules |

Sources: [IR4GU pp 5,39–40][S2], [IRD payment-day rule][S9], [government 2027 calendar][S10]. Working-day adjustment applies; provincial anniversary days have a separate electronic-payment rule. Record the actual account period, deadline and extension evidence. Filing and payment are distinct. Q32/Q33 provisional completion is a separate company handoff; do not copy the individual-only 'nz-provisional-tax' guide into a company return or infer an instalment schedule from annual RIT.

File in the company’s myIR income-tax account or use the applicable paper form. The public steps establish no logged-in access, portal behaviour or successful submission. A working paper is not a filed return. [File IR4][S3].

## Rate and corporate content slots

| Slot | Supported rule or required stop |
| --- | --- |
| Ordinary basic rate | 28%, only to the extent Schedule 1 Part A clause 2 applies instead of clauses 3–9. The annual-rates Act s 3 expressly adopts rates for 2025-26. [Schedule 1][S7], [annual rates][S8] |
| Small/reduced/activity rates, surcharges and sectoral/regional overlays | No separate entitlement or absence is verified here. Establish any applicable special treatment before using 28%. |
| Branch/non-resident rate | Outside scope; Needs Input, not a zero-tax finding. |
| Non-deductible expenses and exempt income | Require a provision, period and evidence for each adjustment. No comprehensive local catalogue is verified. |
| Tax depreciation, Investment Boost, capital/revenue and interest limits | Require separately established current treatment and amounts. Book depreciation is not itself a tax deduction. |
| Loss periods/caps, carryback, ownership/business continuity and group relief | Not determined. BC 5 permits only an available Part I loss; establish availability and permitted use first. |
| Withholding credits | Use allowed return-year amounts and fields; Q17A/Q30I are not provisional payments. Apply the ordering below. |
| R&D, investment/IP incentives, foreign tax credit and FITC | No eligibility/cap/ordering analysis for these regimes is supplied. Obtain it separately; tax paid alone proves no foreign-credit entitlement. |
| Filing support, reporting and audit thresholds | Complete applicable IR4 questions and IR10/accounts, shareholder and imputation handoffs. Reporting/audit exemptions and thresholds are not established here. |
| GAAR, CFC, hybrid mismatch and other cross-border overlays | No local conclusion is verified. Relevant facts require current specialist analysis before a result. |
| Pillar Two IIR, UTPR, QDMTT/domestic top-up | No applicability/commencement finding. Confirm the group and overlay profile; unknown is not ‘not applicable’. |

The public rate page also gives 28% for most companies; it cannot replace statutory status confirmation. [Business rates][S4]. The table states the boundaries of this limited companion; it does not establish comprehensive corporate coverage.

## Intake and evidence

Complete both bases’ corporate intake and establish:

- Entity, tax residence, ordinary status, year/balance date, agent and extension evidence.
- Approved accounts/trial balance, business ledger, GST treatment and a complete profit-before-tax bridge to each return income category.
- Each adjustment’s amount, direction, legal source, operative period and record; donations, current/prior losses and group/subvention amounts, including evidenced absence where appropriate.
- Gross interest/dividend statements and recognition analysis; RWT/imputation schedules and each credit’s allowed amount/year. Company financial-arrangement timing is not established by cash receipt or withholding alone. [IR4GU pp 12–14,30][S2].
- Return-year tax-account payments, reversals, transfers and allocations. An assessed or scheduled liability is not proof of payment.
- ICA opening/movements/closing, required annual/interim returns and refund conditions; shareholder/director remuneration, current accounts and additional schedules.
- Foreign/property/group/special-regime/incentive/audit/notice/restructuring/overlay facts. Run the bases’ refusals first.

Demonstrations use hypothetical data. They need no credentials, ID documents or bank-account details.

## Computation and return mapping

### Reconcile income and deductions

Start from approved accounting profit before tax. Trace each supported add-back, deduction, exempt item and timing difference. Box 20B is net business/other rental profit after allowable expenditure; separate income reported elsewhere and keep Q24 donations out of that expense claim. Attach IR10 or the applicable financial accounts, and retain required accounts/records. An IR10 summary does not itself remove a reporting or record obligation. [IR4GU p 27][S2].

Box 23 adds 12B, 13B, 14B, 15B, 16B, 18B, 19H, 20B, 21B and 22B once. Excluded income categories require their own current analysis before assembling a complete total. If the accounts already include interest/dividends reported separately, remove the duplicate from the business component. Gross taxable income is not reduced by withholding credits. [IR4 pp 2–3][S1].

For established ordinary NZ interest, 13B holds gross taxable interest and 13A the allowed RWT/NRWT; lawful timing remains a separate condition. Gross taxable NZ dividends include cash, imputation and RWT. Apply the 28% credit ceiling to each dividend, rather than pooling credits against other income. Establish permitted allocations to Box 14 imputation and 14A RWT before populating those fields. Exempt group dividends, PIEs or uncertain allocations need separate analysis. [IR4GU pp 12–14][S2].

Deduct the separately established eligible donation at 24B once, within the Box 23 income limit, to reach 25. Only a separately verified available-loss claim at 26B reduces 27. Group/subvention items at 28/28A also require verified treatment. A historical loss ledger proves no availability. Box 29 is the form’s income/loss result; preserve loss signs where required. BC 4–6 give zero net income/basic tax for a current net loss, rather than a negative income-tax charge. [IR4 p 3][S1], [IR4GU pp 30–33][S2], [BC 4–6][S6].

### Apply tax and credits in order

Ordinary basic tax is established non-negative taxable income × 0.28. Determine the base and available losses first; do not use individual tax bands. The examples use whole-dollar taxable amounts and exact arithmetic. They establish no rule for dropping cents, filing rounding or fractional-cent tax; establish current filed-value requirements before preparing a return amount. [BC 6][S6], [Schedule 1][S7], [IR4 p 3][S1].

| Field | Calculation and boundary |
| --- | --- |
| 30A/30B | Transfer the supported Box 29 base as the form requires; 30B is ordinary basic tax. Retain loss reporting separately; basic tax cannot be negative. |
| 30C/30D | 30C copies the separately established allowed overseas-tax amount from 18A; 30D = max(30B − 30C, 0). A non-zero foreign claim needs its own analysis. |
| 30E/30F | Deduct separately established FITC in the prescribed order. No foreign-investor entitlement or excess-credit election is assumed. |
| 30G/30H | Copy permitted Q14 imputation to 30G; 30H = max(30F − 30G, 0). Excess imputation is not refundable RWT. |
| 17A/30I | 17A totals allowed 12A, 13A, 14A, 15A and 16A; 30I copies it. Exclude overseas tax/imputation already used at 30C/30G. |
| 30IA | Copy separately established RLWT from 21A; property/credit eligibility is outside this core. |
| 30J | Signed workpaper RIT = 30H − 30I − 30IA. The form records amount plus Credit/Debit. This precedes provisional payments. |
| 30K | Actual properly allocated 2026 provisional tax paid, supported by the tax account. |
| 30L | Signed workpaper balance = signed RIT − 30K. Negative indicates overpayment; the form uses absolute amount plus Refund/Tax to pay. Zero is a reconciled zero balance. |

Source: [IR4 pp 2–4][S1]. Every non-zero credit requires eligibility, limit, year and allocation evidence. Unknown foreign/imputation/withholding/property fields cannot be set to zero. Never deduct a credit again after RIT, substitute assessed provisional liability for payments or use another year’s payment in 30K.

Where permitted imputation exceeds 30F, (30G − 30F) ÷ 0.28 gives the arithmetic potential increase in tax loss. It establishes neither loss availability/carryforward/group use nor a cash refund. Verify the associated loss and ICA requirements separately. [IR4GU p 34][S2].

### Complete refund and schedule checks

Negative 30L is an indicated overpayment, not guaranteed cash. IRD may hold a refund where the ICA credit balance is insufficient. An annual/interim imputation return may affect release. Establish the actual ICA, returns, account allocations and transfer conditions before stating refund availability or timing. Complete ICA operations, penalties and transfer entitlement are not computed here. [IR4GU pp 8,34–36,49][S2].

Most resident companies also need an annual imputation return. IR4 page 7 covers 1 April 2025 to 31 March 2026 regardless of balance date; exceptions/separate IR4J cases require confirmation. Zero income tax does not remove this check. Q40 and any IR4S require supported shareholder/director remuneration, loss/subvention and current-account details. [IR4 pp 6–7][S1], [IR4GU pp 8,45–49][S2].

Determine IR10/accounts support and separate IRD financial reporting. This guide does not verify reporting/audit thresholds, exemptions or Companies Office obligations. IR4 alone does not discharge every reporting duty. [IR4GU p 27][S2], [financial reporting][S11].

Q32/Q33 company provisional options/liability, instalments, interest, penalties and rounding need a separately verified handoff. The annual reconciliation never deducts a future provisional amount. It resolves no disputed statutory instalment allocation.

## Topical refusals

Base refusals remain binding. Use these additional messages verbatim and record affected amounts where known:

| Code | Trigger | Message |
| --- | --- | --- |
| NZ-CIT-STATUS | Unknown regime, residence, year, balance date or overlay | ‘Needs Input: confirm the company’s applicable regime and period before using the ordinary IR4 calculation.’ |
| NZ-CIT-BASE | Unsupported material income, expense, timing or adjustment | ‘Needs Input: the tax base is incomplete. Record the affected items and obtain their treatment and evidence; do not omit or zero them.’ |
| NZ-CIT-LOSS | Unproved loss availability, continuity or group treatment | ‘Needs Input: establish the available loss and permitted use before reducing company taxable income.’ |
| NZ-CIT-CREDIT | Unknown entitlement, per-dividend limit, allocation or year | ‘Needs Input: establish the allowable credit and its correct return field before calculating the overall tax balance.’ |
| NZ-CIT-PAYMENT | Unreconciled payments, year, transfers or reversals | ‘Needs Input: reconcile actual return-year payments to the tax account; a scheduled liability is not a paid amount.’ |
| NZ-CIT-REFUND | Unresolved ICA or release conditions | ‘Needs Input: the calculation shows an indicated overpayment only. Do not promise a cash refund until the imputation and account conditions are established.’ |
| NZ-CIT-HANDOFF | Incomplete provisional, shareholder, imputation or other schedule | ‘Needs Input: complete the separately verified company schedule and reviewer handoff before treating this as a complete IR4 filing.’ |
| NZ-CIT-SPECIAL | Excluded regime or unsupported legal question | ‘Needs Input: obtain the applicable current specialist analysis; this ordinary company core cannot decide that treatment.’ |

## Defaults and reviewer controls

No missing tax fact has a numerical or classification default. Permitted mechanical conventions are a signed workpaper balance, an evidenced zero shown as zero and a proved debit/credit mapped to the form indicator. They supply no evidence or entitlement and waive no material item.

The workflow reviewer threshold is NZD 0: every financial position, including zero/loss, needs qualified review. This is a workflow control, not a statutory threshold. Unresolved law, facts and amounts always receive flags. Conditional arithmetic illustrations supply no engagement conclusion.

## Worked positions

These hypothetical NZD cases use the 2025-26 ordinary standard-year core. Eligibility, classification, timing, adjustments and absence of other items are independently established inputs except where a diagnostic expressly stops. Arithmetic checks do not test those inputs, portal filing or practitioner approval. All indicated overpayments retain the ICA/account conditions above.

### Accounting profit to the ordinary business tax base

The approved accounts show $100,000 profit before tax. Separately verified adjustments add back $12,000 book depreciation and $2,000 non-deductible expense and deduct $8,000 tax depreciation. These are established amounts, not assumed tax allowances. There are no other income categories, donations, available losses or tax credits. The evidenced 2026 provisional payments total $25,000. Taxable income is $106,000, tax and RIT are $29,680 and the indicated balance to pay is $4,680.

```oa-check
name: nz-company-ir4-profit-bridge
tolerance: 0
inputs:
  pbt: 100000
  book_depreciation: 12000
  non_deductible: 2000
  tax_depreciation: 8000
  provisional_paid: 25000
steps:
  box20b: pbt + book_depreciation + non_deductible - tax_depreciation
  box23: box20b
  box29: box23
  box30b: box29 * 0.28
  signed_rit: box30b
  signed_balance: signed_rit - provisional_paid
expected:
  box20b: 106000
  box23: 106000
  box29: 106000
  box30b: 29680
  signed_rit: 29680
  signed_balance: 4680
```

### Separate gross interest without counting it twice

A reconciled $11,000 accounting total includes $1,000 gross NZ interest with $280 evidenced RWT. No other tax adjustments or credits apply. Move the interest to Box 13B and leave $10,000 in Box 20B; total income remains $11,000. Tax is $3,080, RIT is $2,800 and $3,000 actual provisional payments give a $200 indicated overpayment. Cash release still needs the ICA/refund checks.

```oa-check
name: nz-company-ir4-separate-interest
tolerance: 0
inputs:
  included_total: 11000
  gross_interest: 1000
  rwt: 280
  provisional_paid: 3000
steps:
  box20b: included_total - gross_interest
  box13b: gross_interest
  box23: box20b + box13b
  box30b: box23 * 0.28
  box17a: rwt
  signed_rit: box30b - box17a
  signed_balance: signed_rit - provisional_paid
  indicated_overpayment: max(0, -signed_balance)
expected:
  box20b: 10000
  box13b: 1000
  box23: 11000
  box30b: 3080
  box17a: 280
  signed_rit: 2800
  signed_balance: -200
  indicated_overpayment: 200
```

### A current loss does not produce negative income tax

Verified business deductions exceed business income by $20,000. Separately reported gross interest is $1,000 and evidenced RWT is $280. The reported net loss is $19,000; ordinary net income and basic income-tax liability are zero. RWT creates a $280 credit RIT balance, not negative basic tax. With $1,000 actual provisional payments, the indicated overpayment is $1,280, subject to ICA and account checks. This does not establish future loss availability.

```oa-check
name: nz-company-ir4-current-loss-credit
tolerance: 0
inputs:
  business_net: -20000
  gross_interest: 1000
  rwt: 280
  provisional_paid: 1000
steps:
  reported_loss: business_net + gross_interest
  net_income: max(0, reported_loss)
  basic_tax: net_income * 0.28
  signed_rit: basic_tax - rwt
  signed_balance: signed_rit - provisional_paid
  indicated_overpayment: max(0, -signed_balance)
expected:
  reported_loss: -19000
  net_income: 0
  basic_tax: 0
  signed_rit: -280
  signed_balance: -1280
  indicated_overpayment: 1280
```

### Unused imputation is a potential loss, not a cash refund

An independently established taxable dividend has $7,200 cash, $2,800 imputation credits and no RWT. Gross dividend income is $10,000. The $2,800 claim has passed the per-dividend limit. After an established $5,000 business loss, taxable income is $5,000 and basic tax is $1,400. Box 30H is zero. Excess imputation of $1,400 converts arithmetically to a potential $5,000 tax loss; availability and carryforward/group use require separate verification. With no other credits or payments, there is no indicated cash overpayment.

```oa-check
name: nz-company-ir4-imputation-excess
tolerance: 0
inputs:
  cash_dividend: 7200
  eligible_imputation: 2800
  business_net: -5000
steps:
  gross_dividend: cash_dividend + eligible_imputation
  taxable_income: gross_dividend + business_net
  box30f: taxable_income * 0.28
  box30h: max(0, box30f - eligible_imputation)
  unused_imputation: max(0, eligible_imputation - box30f)
  potential_loss_increase: unused_imputation / 0.28
  signed_balance: box30h
expected:
  gross_dividend: 10000
  taxable_income: 5000
  box30f: 1400
  box30h: 0
  unused_imputation: 1400
  potential_loss_increase: 5000
  signed_balance: 0
```

### Check the credit ceiling for each dividend

A separately established $1,000 gross taxable dividend carries $330 nominal combined dividend tax credits. The ordinary 28% per-dividend ceiling is $280, so $50 cannot simply shelter other income. This diagnostic establishes the ceiling only. The proper allocation between eligible imputation and RWT must be established before either return credit field is populated; do not treat the combined ceiling as permission to choose an allocation.

```oa-check
name: nz-company-ir4-dividend-credit-cap
tolerance: 0
inputs:
  gross_dividend: 1000
  nominal_credits: 330
steps:
  dividend_ceiling: gross_dividend * 0.28
  combined_credit_ceiling: min(dividend_ceiling, nominal_credits)
  unusable_excess: nominal_credits - combined_credit_ceiling
expected:
  dividend_ceiling: 280
  combined_credit_ceiling: 280
  unusable_excess: 50
```

### Use an established withholding credit once

The evidenced taxable-income total is $100,000 and includes the related gross income. Allowable withholding credits are $3,000; actual provisional payments are $20,000. Basic tax is $28,000, RIT is $25,000 and the indicated balance is $5,000. Subtracting the withholding credit again after RIT would incorrectly reduce that balance to $2,000.

```oa-check
name: nz-company-ir4-no-double-credit
tolerance: 0
inputs:
  taxable_income: 100000
  allowable_withholding: 3000
  provisional_paid: 20000
steps:
  basic_tax: taxable_income * 0.28
  signed_rit: basic_tax - allowable_withholding
  signed_balance: signed_rit - provisional_paid
  wrong_double_credit_balance: signed_balance - allowable_withholding
expected:
  basic_tax: 28000
  signed_rit: 25000
  signed_balance: 5000
  wrong_double_credit_balance: 2000
```

### Deduct a separately established donation once

Box 23 is $105,000 before donations. A $5,000 donation deduction is independently established and within the income limit; it was excluded from the Box 20B expense claim. With no losses or credits, Box 25 and taxable income are $100,000, basic tax is $28,000 and $28,000 actual provisional payments leave zero balance. This arithmetic does not verify donee status or deduction entitlement.

```oa-check
name: nz-company-ir4-donation-once
tolerance: 0
inputs:
  income_before_donation: 105000
  eligible_donation: 5000
  provisional_paid: 28000
steps:
  box25: income_before_donation - eligible_donation
  taxable_income: box25
  basic_tax: taxable_income * 0.28
  signed_balance: basic_tax - provisional_paid
expected:
  box25: 100000
  taxable_income: 100000
  basic_tax: 28000
  signed_balance: 0
```

### An active company can have zero tax and still need its return

The active ordinary company has $60,000 established taxable business income and $60,000 allowable current-year deductions. There are no other income, credit or payment amounts. Net income and basic tax are zero. This is not an accepted non-active-company exemption; the IR4 filing obligation still has to be met. A zero amount does not authorise omitting the imputation-return check.

```oa-check
name: nz-company-ir4-active-zero
tolerance: 0
inputs:
  gross_business: 60000
  allowable_deductions: 60000
steps:
  net_income: gross_business - allowable_deductions
  basic_tax: net_income * 0.28
  signed_balance: basic_tax
expected:
  net_income: 0
  basic_tax: 0
  signed_balance: 0
```

### Use only an independently established available loss

The verified current net income is $100,000. A separate current Part I analysis establishes that exactly $20,000 of brought-forward loss is available and claimed this year. With no credits and $20,000 actual provisional payments, taxable income is $80,000, basic tax and RIT are $22,400 and the indicated balance is $2,400. If availability or the claim amount is unconfirmed, stop before this calculation; a historical ledger balance alone is insufficient.

```oa-check
name: nz-company-ir4-available-loss-only
tolerance: 0
inputs:
  net_income: 100000
  available_loss_claimed: 20000
  provisional_paid: 20000
steps:
  taxable_income: net_income - available_loss_claimed
  basic_tax: taxable_income * 0.28
  signed_rit: basic_tax
  signed_balance: signed_rit - provisional_paid
expected:
  taxable_income: 80000
  basic_tax: 22400
  signed_rit: 22400
  signed_balance: 2400
```

If a prior-year loss appears in the accounts but availability is unconfirmed, issue NZ-CIT-LOSS before producing a tax figure. If trading stopped but an accepted non-active exemption is not evidenced, obtain the return obligation and declaration status; do not infer that filing ceased.

## Output extension and self-checks

Deliver the bases’ required outputs and these company working papers:

1. Confirmed profile, period, source library/currency, exclusions/refusals and missing-evidence register.
2. Accounts-to-tax bridge, non-duplicated 12B–29 income/deduction map, adjustment citations and documentary index.
3. Basic tax, per-dividend credit checks, 30C–30J ordering, actual-payment reconciliation and signed 30L balance with the form indicator.
4. Separate potential-loss, ICA/refund-restriction, Q32/Q33 provisional, IR10/accounts, shareholder and imputation handoffs. Distinguish computed overpayment, confirmed refundable amount and any unresolved amount.
5. Reviewer brief, material variances, qualifications, questions and sign-off status. No submission or practitioner approval is implied.

Complete every base self-check. Confirm the entity/year, supported base, loss availability, ordinary rate, credit cap/year/field, gross-income allocation, no duplicate donations/credits/payments, actual 30K payments, balance sign/indicator, ICA/schedules and actual deadlines/extensions. Cross-check totals with the form and accounts. Passing arithmetic cannot clear a source or evidence stop.

## Primary sources and revision

- [S1: IR4 2026][S1], pp 2–4 and 6–7: selected income, credit, payment, shareholder and imputation fields. All 7 pages captured; pp 3–4 visually inspected.
- [S2: April 2026 IR4GU][S2], selected pp 5,8,12–14,27,30–34,39–40,45,49. The full 53-page guide is not substantively verified. The p 14 dividend-credit worksheet was visually inspected.
- [S3: File IR4][S3], [S4: business rates][S4], [S5: non-active companies][S5] and [S11: financial reporting][S11]: public pages checked 13 November 2026. Only the stated claims are adopted; reporting thresholds are not certified.
- [S6: ITA BB 1/BC 4–6][S6], [S7: Schedule 1 Part A clause 2][S7] and [S8: 2026 No 8 s 3][S8]: selected ordinary charge/base/rate and express 2025-26 annual adoption. Consolidation dated 4 September 2026; scoped currentness screen only.
- [S9: IRD payment-day rule][S9] and [S10: government 2027 holidays][S10]: exact matching captures checked in the preceding NZ batch are reused. The selected 9 February 2027 date is a calendar derivation, subject to actual myIR conditions.

Version 0.1, checked 13 November 2026. Initial bounded IR4 working-paper core, tier 2 and pending review. No whole corporate-tax/reporting completion or practitioner approval is recorded. Wider regimes, deduction/credit eligibility, full losses/ICA, company provisional calculations, tax provision, reporting thresholds, rounding and end-to-end filing remain outstanding.

[S1]: https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir1---ir99/ir4/ir4-2026.pdf?modified=20260331185611
[S2]: https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir1---ir99/ir4gu/ir4gu-2026.pdf?modified=20260331185400
[S3]: https://www.ird.govt.nz/ir4
[S4]: https://www.ird.govt.nz/income-tax/income-tax-for-businesses-and-organisations/tax-rates-for-businesses
[S5]: https://www.ird.govt.nz/roles/companies/non-active-companies
[S6]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/parts/DLM1512313/
[S7]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/parts/DLM1523173/#DLM1523192
[S8]: https://www.legislation.govt.nz/act/public/2026/8/en/latest/
[S9]: https://www.ird.govt.nz/managing-my-tax/make-a-payment/when-to-pay
[S10]: https://www.govt.nz/browse/work/public-holidays-and-work/public-holidays-and-anniversary-dates/
[S11]: https://www.ird.govt.nz/managing-my-tax/record-keeping/financial-reporting-for-companies/financial-reporting-requirements-for-companies

## Disclaimer

This source-cited draft produces conditional working papers for an appropriately qualified New Zealand tax practitioner. Verify law, source conditions, facts and all required schedules for the actual period before relying on a figure or filing. No live return, spreadsheet artifact, LLM upload or practitioner sign-off has been tested or obtained.

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
