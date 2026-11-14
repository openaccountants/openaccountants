---
name: jp-return-assembly
description: "Final orchestrator skill that assembles the complete Japanese filing package for Japan-resident self-employed individuals and sole proprietors (個人事業主). Consumes outputs from all Japanese content skills (japan-consumption-tax for 消費税, jp-income-tax for 所得税確定申告, jp-social-insurance for 社会保険料, jp-estimated-tax for 予定納税) to produce a single unified reviewer package containing every worksheet, every form, every brief section, all cross-skill reconciliations, and the final action list with payment instructions, filing instructions, and next-year planning. This is the capstone skill that runs last and produces the final deliverable. MUST be loaded alongside all Japanese content skills listed above. Japan full-year residents only. Self-employed individuals and sole proprietors (個人事業主) only."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/jp-return-assembly"
  jurisdiction: "JP"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Japan return assembly v1.1

> **General reference only.** This skill prepares AI-assisted working papers. A qualified 税理士 must review the facts, elections, computations and current forms before filing, paying or taking a tax position.

## Scope

Assemble 2026 working papers for full-year Japan-resident sole proprietors from `jp-freelance-intake`, `japan-consumption-tax`, `jp-consumption-tax`, `jp-income-tax`, `jp-social-insurance` and `jp-estimated-tax`. The old names `japan-income-tax` and `japan-social-insurance` are legacy references; load the actual files named here. Latest final form orientation is the 2025-2026 filing cycle; label any 2025 package accordingly. This skill assembles and reconciles; the specialist computation skills own rates, deductions and elections. Contributor: Open Accountants Community.

### Answer layer

| Assembly control | Condition/value | Official source |
|---|---|---|
| Gross/net sales reconciliation | National output uses applicable 7.8%/6.24% national rates after gross-to-net conversion; combine with local only once | [Consumption Tax Act arts.28-30; NTA 6351](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6351.htm) |
| Blue deduction | JPY 550,000 (source: 55万円) ordinary eligible books/statements/timely filing; JPY 650,000 (source: 65万円) adds timely electronic filing OR qualifying excellent electronic books/notice; other eligible blue filers up to JPY 100,000 (source: 10万円), subject to relevant income cap | [Special Measures Act art.25-2; NTA 2072](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/2072.htm) |
|2026 individual final income/JCT due dates | 2027-03-15 /2027-03-31; valid transfer debits 2027-04-23 /2027-04-30 | [NTA payment calendar](https://www.nta.go.jp/taxes/nozei/nofu/24200042/noufu_kigen.htm) |
| Final 2025 package,2025-2026 filing cycle | Income due 2026-03-16/debit 2026-04-23; JCT due 2026-03-31/debit 2026-04-30 | [NTA payment calendar](https://www.nta.go.jp/taxes/nozei/nofu/24200042/noufu_kigen.htm) |
| Mandatory JCT interim trigger | Prior annual NATIONAL tax >JPY 480,000 (source: 48万円), local excluded; equality does not trigger | [Act arts.42-44; NTA 6609](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6609.htm) |

## Ask the client first

- Read the complete confirmed intake and upstream outputs before asking anything.
- Request only missing evidence that prevents a specific computation/reconciliation; say which source was checked.
- Resolve contradictory records through documented arithmetic and timing/gross-net adjustments first.
- Confirm only unresolved judgement/election facts, supported filing route and the final figures before taxpayer submission.

Do not ask how deep to go, which deliverables to prioritise or whether to run another content skill. The authorised package includes all deliverables below. Continue supported work when one schedule is incomplete, with unsupported outputs clearly excluded and quantified. Never turn unknown into zero or label a failed tax computation validated. Preserve sources beside each figure and in the final brief.

## The method, step by step

1. Load intake once; preserve confirmed residence, entity and year. Do not repeat scope interrogation. Validate document coverage, period, election evidence and open flags, then build an execution/evidence register.
2. Consumption tax first: `jp-consumption-tax` determines exempt/general/simplified/2割 eligibility, and `japan-consumption-tax` classifies the transactions and builds the national/local workpaper. Tax-inclusive books require a supported timing treatment of consumption-tax expense; tax-exclusive books reconcile tax control accounts. Do not deduct unpaid/not-yet-recognised JCT merely because a computation exists. Use current income-tax treatment of deductible timing.
3. Assemble paid social-insurance/mutual-aid evidence before finalising income deductions. `jp-social-insurance` verifies municipality NHI and pension payment/certificates, exemptions/deferrals and actual calendar-year amounts, and separates小規模企業共済/iDeCo from社会保険料. Never multiply an obsolete national-pension rate by months or treat unpaid assessed premiums as paid deductions.
4. Run `jp-income-tax`: revenue, COGS, expense/asset schedules, business-versus-miscellaneous classification, pre-blue profit, blue deduction, other income, all deductions, taxable income, income tax/reconstruction tax, credits, actual withholding and estimated-tax payments. Import the current-year tables and conditions, including 2026 reforms. Basic deduction is not a fixed JPY 480,000; spouse/dependent amounts, life/earthquake limits and small-asset concessions are not constants stored in this orchestrator. [NTA 1199](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1199.htm).
5. Run `jp-estimated-tax` using the assessed statutory base/notices and necessary adjustments. A prior final cash balance is not automatically the base. Reconcile actual instalment liabilities/payments credited on the current return and show next-year planning separately. Use notices for reduction applications and dates; do not invent next-year debit dates.
6. Reconcile all cross-skill outputs below. Any failure gets source-labelled amounts, difference, likely cause, evidence and reviewer action. Carry supported calculations forward; filing-ready status remains false for affected unvalidated outputs.
7. Build all final documents and perform arithmetic/formula/source QA. Produce a complete package when possible; if context/output constraints intervene, finish computations first and identify every missing/partial artifact at the end. No unsupported fallback figures.

### Cross-skill reconciliations, all retained

| Control | Reconciliation and exception |
|---|---|
| Revenue consistency | Bridge JCT taxable/exempt/export/outside-scope totals to income revenue, using gross/net accounting, accruals/cash election, asset disposals, timing and non-business transfers. These totals need not be identical. A difference must reconcile to evidence; JPY 1 is an internal rounding tolerance only, never a legal safe harbour |
| Business versus miscellaneous | Record scale, continuity, profitability, records and economic reality. Opening notice/blue approval alone do not establish business income, and a low revenue figure is not an automatic reclassification. Keep loss-offset/carryforward eligibility with the current computation skill; refer borderline facts |
| Blue deduction | Check actual blue approval, eligible business, regular books, balance sheet/profit statement, timely return, applicable e-Tax or excellent-electronic-book route, notice and income limitation; paper filing is not automatically restricted to JPY 550,000 |
| Social insurance | Actual paid calendar-year NHI/pension plus certificates/payment proof reconcile to claimed social-insurance deduction. Mutual aid/iDeCo belong to their separate deduction. No double counting amounts already in payroll/year-end adjustment |
| Withholding | Sum actual withholding from all源泉徴収票,支払調書, invoices/remittances and payer confirmations, investigate mismatches, credit the supported total. Payment-record availability is not itself a tax exemption. Apply correct art.204 category; no flat fee rule for every freelancer |
| JCT method | Confirm base/specified periods, invoice date, elections and restrictions. Simplified base-period ceiling and effective election; 2割 means otherwise exempt because of invoice registration in the eligible period, not merely exemption in the base year. General method cannot override a binding simplified election solely for a lower result |

For JCT transitional inputs, the 2026-10-01 credit changes to 70% under the reform, not the old 50% schedule.2割 applies to qualifying periods containing a date up to 2026-09-30, so eligible calendar 2026 can qualify. Do not cut it off by the period end date. [FY 2026 invoice reform](https://www.nta.go.jp/taxes/shiraberu/zeimokubetsu/shohi/keigenzeiritsu/invoice-review/index.htm), [2割 guidance](https://www.nta.go.jp/taxes/shiraberu/zeimokubetsu/shohi/keigenzeiritsu/pdf/0023011-048_01.pdf). National-only interim bands and strict inequalities come from [NTA 6609](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6609.htm). Never use combined tax for the trigger.

### Complete reviewer package

Produce 3 artifacts in the host's authorised output directory and link them using the available presentation mechanism; do not assume `/mnt/user-data/outputs/` or `present_files` exists.

1. `[client_slug]_[tax_year]_japan_master.xlsx`: Cover; source/document register; JCT computation/method comparison/form fields and付表;青色申告決算書 P/L and B/S or収支内訳書; income return/schedules; asset/depreciation roll-forward; deduction detail; withholding reconciliation; actual/next-period estimated tax; cross-check summary; action calendar. Use live formulas to connect income, statements and deductions; check no broken references and match computed results within the internal rounding tolerance. PDF form filling is not automated.
2. `reviewer_brief.md`: one-page executive summary followed by computation schedules, current form mappings, evidence, positions/legal citations, flags, cross-checks and next-period planning. State tax year, residence/business/blue/filing status, invoice registration, gross/net revenue, pre/post-blue income, taxable income, income/reconstruction tax, credits, withholding/estimated payments, final due/refund and separate JCT national/local due. Resident/enterprise-tax amounts are municipality/prefecture notices or explicitly scoped sourced estimates, never an official notice generated by this workflow.
3. `client_action_list.md`: specific return/payment steps, amounts and verified dates, taxpayer/reviewer responsibilities, missing evidence, estimated-tax/reduction actions and ongoing compliance. Separate assessed liabilities, paid credits, projections and unconfirmed actions.

The brief must preserve these detail sections:

- JCT: evidence for method, taxable sales/purchases by rate, general output/input or simplified activity/deemed credit or 2割 calculation, eligibility comparison, national/local interims and final balance. Do not compute unavailable methods as an actionable election.
- Income statement: sales, COGS, gross profit, all expense categories (taxes, shipping, utilities, travel, communications, advertising, entertainment, insurance, repairs, supplies, depreciation, welfare, wages, outsourcing, interest, rent, bad debts, custom categories and miscellaneous), pre-blue income, blue deduction and business income.
- Income return: receipts/income by class; social insurance, mutual aid/iDeCo, life/care/pension insurance, earthquake, spouse/special spouse, dependents, basic, medical and donation deductions; taxable income, progressive tax, applicable tax credits including dividend/housing, reconstruction tax, withholding, estimated payments and due/refund. No legacy `申告書B` mapping is assumed to survive current forms.
- Asset roll-forward: asset name, acquisition/in-service date, cost, units, useful life, method/rate, depreciation base, months, business share, current ordinary/special depreciation, disposals and closing unamortised balance. Consider qualifying small-asset and pooled regimes using current dated rules; never depreciate continuing assets from guessed acquisition history.
- Social insurance: municipality and NHI payment notices/bank reconciliation; pension certificates and unpaid/exempt/deferred periods; mutual aid/iDeCo monthly and annual actual totals and certificates.
- Estimated tax: statutory base, actual notice, instalment liabilities and credits, reduction eligibility and calendar, transfer arrangements; next-year projection visibly separate.
- Reconciliation/attention: all controls above, classification dispute, blue deduction route, JCT comparison/election sunset/transition, home-office/vehicle evidence, asset cap tracking, future threshold monitoring, withholding mismatch, carryforward losses and pension non-payment.
- Positions: only actually supported positions with source, article, year and underlying document. Do not copy the old illustrative home-office percentage or small-asset eligibility example as a finding.
- Planning: continuing assets; municipality insurance recalculation; future base/specified-period JCT exposure; post 2割 method/election transition; bookkeeping, certificate retention, mutual aid/iDeCo planning and current enacted reforms. Do not treat resident-tax rates/instalments as uniform national rules.

## Boundary and exception table

| Exception | Package treatment |
|---|---|
| Upstream did not run or failed | R-JP-A 1/A 2: name skill/check, mark affected figures incomplete, continue separable supported outputs |
| Reconciliation failed | R-JP-A 3: quantify discrepancy, preserve both source amounts and bridge, no forced plug |
| Missing facts prevent a computation | R-JP-A 4: identify exact evidence gap and ask only what records cannot answer |
| Property capital gains, forestry/retirement or complex treaties | R-JP-A 5: flag/exclude unsupported schedule and refer; do not silently describe the entire return as complete |
| Business/miscellaneous disputed | R-JP-A 6: explain facts and financial consequence; reviewer decides classification |
| No prior depreciation schedule | Seek prior records; current acquisitions may proceed but continuing assets remain unresolved rather than disappearing |
| Resident/enterprise tax or JCT interims | Reconcile actual notices; interim JCT return preparation and official municipal/prefectural assessments are outside this package |

## Worked cases

### Historical reviewer-position illustrations

The original 2025 reviewer-brief template included these illustrative facts: a dedicated home-office room of 9 square metres within a 30-square-metre home (raw area fraction 9/30 = 30%); a service-business example with base-period revenue JPY 8,200,000; and a MacBook Pro costing JPY 280,000, also the example's annual small-asset total JPY 280,000. Retain these as **historical hypothetical inputs**, not findings for the current taxpayer. The area fraction does not by itself prove deductible business use. The service example still needs actual activity classification and a binding valid simplified election. The MacBook example still needs its acquisition/in-service date, current dated asset regime, business use and annual-total evidence; the old automatic expensing assertion is not usable. The old business-income illustration also assumed opening notification, blue approval and double-entry books; these are evidence factors, not conclusive classification. The old JPY 650,000 blue-deduction position needs every current condition, including the supported electronic route and income limitation. Preserve the illustration only when the facts and applicable law support the resulting position; otherwise show it as rejected/pending in the brief.

Case 1, source-to-return revenue bridge: hypothetical standard domestic net JPY 10,000,000, export JPY 2,000,000, exempt revenue JPY 500,000 and outside-scope business subsidy JPY 300,000. Domestic combined output JPY 1,000,000; tax-inclusive P/L revenue JPY 13,800,000. Removing JCT gives JPY 12,800,000 net P/L revenue. The JCT taxable-sales numerator JPY 12,000,000 differs from P/L revenue by JPY 800,000 of exempt/subsidy items. A blind equality check would fail. Classification inputs must be independently established; method from [NTA 6351](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6351.htm), [outside-scope guidance](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6157.htm), [ratio guidance](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6405.htm).

```oa-check
name: Reconcile taxable sales with total business revenue
inputs:
  domestic_net: 10000000
  export: 2000000
  exempt_revenue: 500000
  subsidy: 300000
steps:
  output_combined: domestic_net * 0.10
  gross_profit_loss_revenue: domestic_net + output_combined + export + exempt_revenue + subsidy
  net_profit_loss_revenue: gross_profit_loss_revenue - output_combined
  jct_taxable_sales: domestic_net + export
  reconciling_items: net_profit_loss_revenue - jct_taxable_sales
expected:
  gross_profit_loss_revenue: 13800000
  net_profit_loss_revenue: 12800000
  jct_taxable_sales: 12000000
  reconciling_items: 800000
```

Case 2, credit and balance reconciliation: hypothetical upstream reviewed total income/reconstruction tax JPY 612,600, supported withholding JPY 204,200, first/second estimated payments JPY 150,000 each. Remaining balance JPY 108,400. Prior national JCT JPY 480,000 does not require mandatory interims; an internal test compares against the strict boundary, not>=. This example checks reconciliation of upstream reviewed amounts and does not invent an income-tax rate. [NTA 6609](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6609.htm).

```oa-check
name: Reconcile withholding estimated credits and strict interim boundary
inputs:
  reviewed_tax: 612600
  withholding: 204200
  first_paid: 150000
  second_paid: 150000
  prior_national_jct: 480000
steps:
  estimated_credits: first_paid + second_paid
  remaining: reviewed_tax - withholding - estimated_credits
  excess_over_interim_boundary: max(prior_national_jct - 480000, 0)
expected:
  estimated_credits: 300000
  remaining: 108400
  excess_over_interim_boundary: 0
```

## When to refuse or refer

Do not submit, sign or execute payment. Taxpayer/reviewer uses `jp-etax-filing`. Stop unsupported computations, preserve the work and refer cleanly under the boundaries above. Self-checks are working-paper controls, not permission to carry wrong or unsupported figures into a return. A partial package must name every exclusion and effect on final balances.

## Filing and payment

Use the year-specific calendar above, actual notices and `jp-estimated-tax`. Filing extensions, instalment deferral, interest, reduced estimated payments, local-tax schedules and unusual periods need their own current source confirmation. Do not reuse old approximate transfer dates, universal local-tax instalments or stale deferral interest. Payable returns do not trigger an automatic payment merely by transmission; record actual receipt and payment independently. [NTA receipt guidance](https://www.e-tax.nta.go.jp/toiawase/qa/yokuaru01/13.htm).

## Completion checklist

Retain controlsJP 1-JP 12: all upstream outputs; source-reconciled revenue bridge; defensible income classification; eligible blue deduction including alternative electronic-books route; paid insurance reconciliation; actual withholding; valid JCT method; current basic deduction; reconstruction tax from computation; both estimated credits; year-specific calendar; article-cited positions. Validate all formulas, national/local and gross/net units, source dates and document links. The final brief has open flags and a single reviewer-signoff reminder; every artifact is linked or explicitly reported missing.

## Sources

| Source | URL | Read on |
|---|---|---|
| NTA 6351: Read for gross/net and national-output method | https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6351.htm | 2026-11-14 |
| NTA blue: Read for deduction routes and limitations | https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/2072.htm | 2026-11-14 |
| NTA basic: Read for 2026 reform and year-specific basic deduction | https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1199.htm | 2026-11-14 |
| NTA reform: Read for 2026 transitional credit and election changes | https://www.nta.go.jp/taxes/shiraberu/zeimokubetsu/shohi/keigenzeiritsu/invoice-review/index.htm | 2026-11-14 |
| NTA two: Read for 2割 qualifying periods/exclusions | https://www.nta.go.jp/taxes/shiraberu/zeimokubetsu/shohi/keigenzeiritsu/pdf/0023011-048_01.pdf | 2026-11-14 |
| NTA 6609: Read for strict national-only interim boundary | https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6609.htm | 2026-11-14 |
| NTA 6157: Read for business-subsidy outside-scope boundary | https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6157.htm | 2026-11-14 |
| NTA 6405: Read for taxable/export numerator and excluded items | https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6405.htm | 2026-11-14 |
| NTA receipt: Read for receipt versus filing/payment evidence | https://www.e-tax.nta.go.jp/toiawase/qa/yokuaru01/13.htm | 2026-11-14 |
| NTA dates: Read for final 2025/2026 calendar and transfer dates | https://www.nta.go.jp/taxes/nozei/nofu/24200042/noufu_kigen.htm | 2026-11-14 |

Not yet confirmed: Final 2026 return layouts and exact boxes; specific penalty/interest/deferral calculation; local resident/enterprise-tax assessment; unresolved asset history, deduction limits and treaty positions not verified by the relevant current computation skill. Historical fixed basic/pension amounts, fixed opening-notice deadline, universal retention rule and small-asset price/cap examples are not operative instructions; obtain current dated source and conditions through the relevant skill. Final 2025 forms are used only as 2025-2026 filing-cycle orientation.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `jp-return-assembly` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/jp-return-assembly. If neither is available, confirm every figure against the official source pages cited above before relying on it.
