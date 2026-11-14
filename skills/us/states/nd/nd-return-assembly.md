---
name: nd-return-assembly
description: Assemble a reviewer package for a North Dakota full-year-resident sole proprietor/disregarded SMLLC
  for tax 2026. Consume federal/state owners without duplicating computations, reconcile taxable-income and payment
  handoffs, maintain workbook/brief/actions, and distinguish planning from final filing. Actual 2025-2026 return
  lines/procedures are explicitly labelled; final 2026 forms remain a filing gate. Trigger on ND return assembly,
  complete ND package, ND-1 reviewer brief and final filing checklist.
jurisdiction: US-ND
tax_year: 2026
last_updated: '2026-11-14'
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
version: '2.3'
type: filing-howto
category: orchestrator
---

# North Dakota return assembly, 2026

> **Source-cited draft.** Written by Codex. Not reviewed by an accountant. Circular 230 section 10.37: this is a sourced working-paper method, not an opinion or permission to file. Resolve taxpayer facts, source gaps and professional review before acting.

**Answer first.** Run federal computations first, then ND income tax and estimates, and assemble the source outputs into one reviewer package. A package is a draft until actual form-year mapping, tax/payment reconciliations and professional review pass. ND TAP payment confirmation does not file an individual income tax return. [2025-2026 booklet pp 1,7,11-16](https://www.tax.nd.gov/sites/www/files/documents/forms/individual/2025-iit/2025-individual-income-tax-booklet.pdf); [agency filing/payment guidance](https://www.tax.nd.gov/individual-income-tax).

## Scope and who this is for

Full-year ND-resident sole proprietors and federally disregarded SMLLCs, original individual returns. This is an assembly method, not another tax calculator. Prepare 2026 working papers with current owners; use the read **2025-2026 filing-cycle** procedures only as a labelled mapping reference. Do not submit a 2026 return on 2025 forms or claim final 2026 mapping has been verified.

Nonresident/part-year and mixed-residency returns go to `nd-cross-border-tax`; S corporations, partnerships and corporate elections to their entity workflow (`nd-corporate-tax` routing; Form 60 S corporation, Form 58 partnership, Form 40 corporate). Fiduciaries, amendments, foreign/treaty work, complex multistate business and specialist mineral-extraction/coal filings are separate jobs. Income-tax treatment of ordinary royalties can still flow through the federal/state owners. The read booklet says an individual amendment uses the affected year's ND-1 marked amended, **not a separate ND-1X**. [pp 7-8](https://www.tax.nd.gov/sites/www/files/documents/forms/individual/2025-iit/2025-individual-income-tax-booklet.pdf); [mixed-residency scope](https://www.tax.nd.gov/sites/www/files/documents/forms/individual/2025-iit/28724-schedule-nd-1nr-2025.pdf).

Reuse documented intake. Ask only for missing taxpayer facts, never ask the taxpayer to research a tax rule. Continue independent preparation while an unresolved item is flagged, but do not label a materially inconsistent return ready to file. Preserve the source date/year, unresolved assumptions and scope boundaries instead of a generic PASS.

## Ask the client first

1. Confirm the intake record: tax year, filing status, both spouses' domicile/moves, business classification, DOB/dependents and prior returns.
2. Obtain source documents and completed federal/state workpapers, with the version, line outputs and actual self-check results for each producer.
3. Reconcile ND withholding, estimates, prior overpayment/extension payments and refunds to dated account records; obtain bank instructions securely.
4. Capture MN/MT work/certificates; military/retirement, reservation enrollment/source, Renaissance Zone certification, farm-averaging and mineral-income flags.
5. Obtain marketplace/COBRA coverage, retirement contributions and contractor records needed by federal owners; do not infer eligibility from a label.
6. Confirm filing/authorization method, outstanding notices, other-state recovery returns and the taxpayer's action/payment dates.

## The method, step by step

### Load the owners and keep the handoffs

| Order / track | Producer and required output |
| --- | --- |
| Workflow and intake | `us-tax-workflow-base`; facts, document index, missing-input log and scope |
| Books | `us-sole-prop-bookkeeping`; reconciled income/expense ledger and contractor records |
| Federal computations | `us-schedule-c-and-se-computation`, `us-self-employed-retirement`, `us-self-employed-health-insurance`, `us-qbi-deduction`; supported Schedule C/SE, depreciation/home-office, retirement, health/PTC and QBI outputs. Resolve dependency/iteration before assembly |
| Federal final workpaper | `us-federal-return-assembly` with `us-federal-income-tax-return-1040`; supported federal taxable-income calculation, tax, payments, schedules and review flags |
| State tax | `nd-income-tax`; state modifications, filing-status tax, credits, special schedules, withholding/payment and tax balance outputs |
| State source/credit if relevant | `nd-cross-border-tax`; reciprocity, ND-1CR or handoff of out-of-scope allocation |
| Estimates | `us-quarterly-estimated-tax` and `nd-estimated-tax`; independent federal/ND payment duty, installments and underpayment workpapers, with actual years |
| Parallel contractor track | `us-1099-nec-issuance` after books; W-9 gaps, contractor batch and actual federal deadline/threshold. Do not maintain competing federal values here |
| Separate employer/indirect/entity tracks | `nd-payroll`, `nd-social-contributions`, `nd-sales-tax`, `nd-corporate-tax`; status and separate engagements, not additions to individual income tax |
| Final assembly | This skill; source-linked workbook, reviewer brief, taxpayer action list and acceptance/payment follow-up |

An unused computation is marked N/A with the reason; do not manufacture empty returns. An upstream result includes its figure, form year, source worksheet, check result and open issues. Do not claim a required producer ran because its name appears in a checklist. Sales/UI/employer reconciliation are separate filing tracks; show their deadlines/status without withholding the otherwise supported individual working paper.

### Reconciliation matrix and current form-year gate

The read final mapping below is **2025-2026 filing cycle only**. For 2026, obtain the final form and update the map before filing. [ND-1 instructions pp 11-16](https://www.tax.nd.gov/sites/www/files/documents/forms/individual/2025-iit/2025-individual-income-tax-booklet.pdf); [ND-1UT](https://www.tax.nd.gov/sites/www/files/documents/forms/individual/2025-iit/28704-schedule-nd-1ut-2025.pdf).

| Check | Required tie-out / correction to the old draft |
| --- | --- |
| Federal start | ND-1 line 1b takes federal **taxable income**, not AGI. Where federal line 15 is displayed as zero but its calculation is negative, the 2025 NDinstructions require the negative calculation on 1b. Obtain the actual federal workpaper |
| State modifications | Reconcile each actual ND addition/subtraction and ND-1SA attachment; do not use the old invented generic lines 2/3 as totals of all modifications |
| State base and tax | ND taxable income 18; taxable amount 19; tax 20, from the state owner. Use its current tax schedule and rounding, not a second rate table in this orchestrator |
| Credits | ND-1CR credit 21; marriage credit 22; ND-1TC other credits 23; net tax 25. Do not infer that ND has no child/family-related credits because there is no duplicated federal deduction |
| Withholding | Line 26 equals ND W-2/1099/K-1 withholding actually supportable, not federal withholding or mineral production/extraction taxes |
| Payments | Line 27 equals actual estimate/extension payments plus valid prior overpayment applied to this year; do not include withholding twice |
| Result | Total payments 28; overpayment 29 or tax due 33. Reconcile refund allocations and voluntary contributions, ordinary penalty/interest 34 and total balance 36 |
| Estimate interest | ND-1UT line 17 to ND-1 line 37; follow the return instructions for its inclusion in payment/refund. Keep it distinct from ordinary late-file/pay or extension interest |
| Federal internal checks | Retain the federal owner's complete Schedule C/SE/retirement/health/PTC/QBI/Form 1040/2210 reconciliations with current form lines. The former assertion placing every federal penalty on a fixed Schedule 2 line is not a replacement for that owner's mapping |
| Federal/state coordination | State starting income already reflects the applicable federal deductions. No automatic second standard/itemized, retirement, health, SE or QBI deduction. State additions/subtractions and conformity must come from `nd-income-tax`, not blanket “no add-back ever” claims |
| Special-source/benefit checks | Require support for military retirement, Social Security, U.S.-obligation interest, non-ND municipal interest, reservation income, RZ certification, farm averaging and any unemployment adjustment. Do not take a Job Service unemployment subtraction merely because the old draft said it existed |
| Reciprocity | Certificates, monthly-home/service conditions and state withholding identified by `nd-cross-border-tax`. Erroneous MN/MT withholding is a separate recovery return; do not claim ND-1CR merely for that withholding |
| Estimates and cash actions | Reconcile each federal/ND installment to its owner, dates and actual payments. Distinguish legally required amounts from voluntary reserve and taxpayer cash availability |
| Review and rounding | Apply only the actual form's rounding. A material unexplained gap stays a failed check; the old case's inconsistent totals cannot be excused as a rounding tolerance |

All federal checks formerly labelledF-1 throughF-13, state checksN-1 throughN-15, coordinationC-1 throughC-17, reciprocityR-1 throughR-5, contractor 9-1 through 9-4, estimatesE-1 throughE-6, withholdingW-1 throughW-5 and special-populationS-1 throughS-5 are covered by the producer reports and matrix above. Record **pass, fail or N/A with source and explanation for each applicable check**. Source-specific judgments stay with the producing owner; no blanket PASS for undocumented military, RZ, tribal, farm or cross-border eligibility.

### Deliverables, workbook and brief

Produce three coordinated artifacts in the user's available output workspace, with secure identifiers, not a hard-coded runtime path or unavailable `present_files` tool. The files are `{taxpayer_slug}_2026_nd_master.xlsx`, `reviewer_brief.md` and `taxpayer_action_list.md`; if the environment cannot create one, finish supported work and identify that artifact as partial. Do not expose full SSNs in summaries or create real-client data from this example.

Preserve the original workbook's functional tabs, in this order where applicable:

1. Cover; Assumption Log; Taxpayer Input Log; Reviewer Flag Log; Income.
2. Schedule C; Form 4562; Form 8829; Schedule SE; Retirement; SE Health Insurance with PTC iteration; Form 8962; QBI.
3. Federal Schedules 1/2/3; Form 1040 with taxable-income handoff highlighted; Form 2210.
4. ND-1; ND-1SA; ND-1TC; ND-1CR; ND-1FA; ND-1UT.
5. Reciprocity; Military Retirement; Renaissance Zone; Tribal Reservation; ND Withholding Detail.
6. Federal estimate schedule and ND-1ES schedule, each with its actual payment year;1099-NEC Batch; ND Sales Tax Status; Verification Matrix.

These preserve all 34original sheet functions; use N/A for an inapplicable exhibit rather than fabricate it. Collect cell anchors before constructing cross-sheet formulas; check every formula/reference and compare totals to producer models. Keep documents, source citations and account confirmations linked to their figures.

The reviewer brief retains: Executive Summary, Federal Return, North Dakota Return, Bracket Math Audit from the state owner, MN/MT Reciprocity, Estimated Tax,1099-NEC, ND Sales Tax Status, Cross-skill Verification, Attention Flags, Refusals, Positions with citations, Planning Notes and Taxpayer Action List. Identify exact current year and source version. The executive summary reconciles tax, payments, refund/balance and separate-jurisdiction amounts; never report a combined net as if one authority can collect or refund both.

The taxpayer action list retains: review/signature requests and bank confirmation; federal filing/payment from its owner; ND filing/payment from the actual cycle; federal and ND installments separately; outstanding contractor/employer filings; bookkeeping and income monitoring; health-coverage records; reciprocity renewal; sales-tax cadence; refund tracking and reviewer contact. Every action has a responsible person, amount when known, actual due date and completion evidence. Replace stale pasted dates with owner-confirmed dates; do not repeat guessed processor fees, fixed IRS mailing addresses or unsupported taxpayer-account menu steps.

### Legacy worked-return correction and planning

The former **Sarah Lindgren** example is hypothetical, not a client record. Preserve its Fargo sole-proprietor/Minnesota wage and reviewer-package use case; do not treat the old federal retirement, COBRA, SE/QBI/tax amounts as checked inputs. The single-versus-spouse health-cover statement conflicted, federal calculations and summary totals did not tie, and future QBI claims were not sourced current law. Route those computations to their federal owners and resolve the actual coverage/retirement facts first.

For the **2026 assembly illustration** below, assume the producers have supplied the stated final amounts after those checks. Federal taxable income USD 90,604 is a handoff input, not computed here. The state owner supplies rounded ND net tax USD 800. Keep ND withholding USD 360 and estimates USD 400 as the example's actual payment ledger; state balance is USD 40. The old approximate ND interest USD 15 must not be added without an actual ND-1UT computation and duty test. The small current balance means the current-balance estimate condition fails. A prior-year net tax below the threshold also prevents compulsory estimates under the current 2026 ND-1ES rules. Do not recommend a compulsory next-year voucher from a small tax amount without that year's form. [2026 duty tests](https://www.tax.nd.gov/sites/www/files/documents/forms/individual/2025-iit/28709-form-nd-1es-2026.pdf); `nd-estimated-tax`.

Federal QBI/retirement/SE rates and 1099 thresholds belong to federal owners; do not repeat the old proposed QBI-rate increase as enacted law. Planning notes retain expense/contribution timing near an ND band boundary, projected income changes, military/RZ/tribal continuity, project expiry and federal-state coordination, subject to the actual owner's computation and eligibility. Farm averaging remains a supported specialist comparison, not an unsupported declaration of irrevocability. Municipal/entry/exit-tax absence cannot be certified from the old source list; flag a proposed additional local return for legal resolution rather than silently invent or discard it.

## Boundary and exception table

| Facts | Deliverable status |
| --- | --- |
| Supported in-scope federal/state outputs and tied payments | Complete reviewer package, then professional approval and separate filing authorization |
| Missing input or failed material equality | Complete unaffected worksheets; mark unresolved return and affected totals draft, with named discrepancy |
| Wrong entity, K-1, foreign/treaty or mixed-residency facts | Scope handoff; do not force data into the simple resident sole-proprietor template |
| Employer/UI/sales/contractor late filing | Separate action/status workpaper and owner; individual income-tax assembly is not proof those filings were completed |
| Claimed tax benefit without statutory/source evidence | Flag and obtain producer support before including the benefit |

## Worked cases

**Case 1, hypothetical Sarah Lindgren, supported inputs only.** Producers deliver federal total tax USD 30,940 and federal estimated payments USD 8,000; state net tax USD 800, ND withholding USD 360 and estimates USD 400. No additional interest is established. The package must show federal balance USD 22,940, state balance USD 40 and combined cash requirement USD 22,980. These are arithmetic tie-outs of assumed producer outputs, not an independent certification of federal tax. The former USD 23,001/23,031 summaries and repeated ND interest do not survive reconciliation.

```oa-check
name: Assumed producer-output package reconciles across jurisdictions
inputs:
  federal_tax_from_owner: 30940
  federal_paid: 8000
  nd_net_tax_from_owner: 800
  nd_withholding: 360
  nd_estimates: 400
steps:
  - federal_balance: federal_tax_from_owner - federal_paid
  - nd_payments: nd_withholding + nd_estimates
  - nd_balance: nd_net_tax_from_owner - nd_payments
  - combined_cash: federal_balance + nd_balance
expected:
  federal_balance: 22940
  nd_payments: 760
  nd_balance: 40
  combined_cash: 22980
```

**Case 2, proceed or hold.** Federal workpaper taxable-income calculation is USD 85,000, but the state import says USD 90,000. The USD 5,000 mismatch blocks ready-to-file status. Correcting the import to USD 85,000 removes this discrepancy; it does not waive the remaining checks. When the federal displayed taxable-income line is zero but the underlying calculation is negative, use the special ND-1 line 1b rule instead of demanding equality to the displayed zero. [p 11 line 1b](https://www.tax.nd.gov/sites/www/files/documents/forms/individual/2025-iit/2025-individual-income-tax-booklet.pdf).

```oa-check
name: State import mismatch versus corrected handoff
inputs:
  producer_taxable_income: 85000
  wrong_state_import: 90000
  corrected_state_import: 85000
steps:
  - failed_gap: abs(wrong_state_import - producer_taxable_income)
  - corrected_gap: abs(corrected_state_import - producer_taxable_income)
expected:
  failed_gap: 5000
  corrected_gap: 0
```

## When to refuse or refer

| Retained code | Required response |
| --- | --- |
| R-ND-FINAL-1 | Missing upstream output: identify the producer |
| R-ND-FINAL-2 | Unresolved upstream check: identify the check and affected amount |
| R-ND-FINAL-3 | Failed reconciliation: show equation and gap; no arbitrary tolerance waiver |
| R-ND-FINAL-4 | Suppressed upstream refusal: restore it visibly |
| R-ND-FINAL-5 | Missing intake/source document: identify it without repeating already answered questions |
| R-ND-FINAL-6,13,23 | Nonresident/part-year/mixed-residency: `nd-cross-border-tax` and ND-1NR |
| R-ND-FINAL-7 | Alleged local income return: resolve legal basis; old blanket absence assertion not confirmed |
| R-ND-FINAL-8,9,15 | Reserved legacy identifiers; no substantive rule |
| R-ND-FINAL-10,11,18,19 | Entity or corporate-tax election: route separate Form 40/58/60 workflow |
| R-ND-FINAL-12 | Wrong source/form year: get the actual year's rules;2026 planning is not final 2026 form verification |
| R-ND-FINAL-14 | Amendment: affected-year ND-1 amended process, separate review |
| R-ND-FINAL-16,17 | Complex multistate/foreign/FEIE/FTC: specialist/federal owner |
| R-ND-FINAL-20 | Inbound entity K-1: outside this narrow sole-proprietor package; retain document for expanded individual workflow |
| R-ND-FINAL-21 | Mineral extraction/coal-tax filing: separate job, ordinary royalty income still goes to income-tax owner |
| R-ND-FINAL-22 | Erroneous MN/MT withholding: separate refund recovery; supported ND package can continue |

## Filing and payment

For the **2025-2026 filing cycle**, complete federal return before ND-1, use approved tax software for individual income-tax e-filing or the permitted paper return. ND TAP is a payment/refund/account route, not a claim of direct ND-1 return preparation. Obtain required taxpayer/spouse signatures and actual e-file authorization; verify transmitted return **acceptance**, not just a draft PDF or payment receipt. A paper return includes the complete federal return and required W-2/1099/K-1 withholding evidence and schedules. Mail the ordinary individual return to **Office of State Tax Commissioner,PO Box 5621,Bismarck,ND 58506-5621**. This differs from the estimate-voucher mailing box. [pp 7,15-16](https://www.tax.nd.gov/sites/www/files/documents/forms/individual/2025-iit/2025-individual-income-tax-booklet.pdf).

The read 2025 return is due April 15,2026, with fiscal/weekend/holiday rules in the instructions. A valid federal extension is recognized; absent that, timely Form 101 requests a state extension requiring approval. Mark Extension on the return. Do not confuse an extension with removal of interest; `nd-income-tax` owns the extension/delinquency rates and conditions. For 2026 working papers, obtain final 2026 forms and actual 2027 filing dates before final authorization; current statutory timing alone is not a check of the final form.

For balance payment, use the agency's **Make A Payment** route, or the correct voucher/check process. In the read cycle, paper-return payment uses ND-1PRV; an electronically filed return paid by check uses ND-1V; extension payment uses ND-1EXT; estimates use ND-1ES. Do not mix the type/year. Verify bank instructions and retain confirmation plus posting evidence. Reconcile refundable overpayment, elected next-year estimate credit and voluntary contributions separately; the read return's next-year credit election cannot be changed after filing. [pp 15-16](https://www.tax.nd.gov/sites/www/files/documents/forms/individual/2025-iit/2025-individual-income-tax-booklet.pdf); [estimate-payment instructions](https://www.tax.nd.gov/sites/www/files/documents/forms/individual/2025-iit/28709-form-nd-1es-2026.pdf).

After filing, keep accepted return, all schedules, signed authorization, reviewer signoff, payment references, source workpapers and action status. Use the agency's refund route and bank/account evidence; a projected processing time is not a promise. No payment, signature, filing or professional approval is executed by this assembly skill.

## Completion checklist

- Intake/source documents and actual owner versions recorded; no named person approved this draft by implication.
- Federal taxable-income calculation, ND adjustments, credits, payments and result tied using actual form-year map.
- Every legacy check group resolved with evidence or explicit N/A; failed material checks remain visible.
- Military/RZ/tribal/farm/royalty and reciprocity documents attached where applicable; separate returns identified.
- Workbook, brief and action list agree; formulas/reference anchors checked; no fabricated acceptance or payment.
- Final 2026 mapping/authorization gate resolved before filing; all remaining gaps disclosed.


## Sources

| Source and actual read scope | URL | Read on |
| --- | --- | --- |
| 2025 ND-1 booklet, 2025-2026 filing cycle. Read for residency/reciprocity pp 4-6, filing/extension pp 7-8, return lines pp 11-16 and state modifications; final 2026 lines not confirmed. | https://www.tax.nd.gov/sites/www/files/documents/forms/individual/2025-iit/2025-individual-income-tax-booklet.pdf | 2026-11-14 |
| Individual Income Tax page. Read for filing methods and payment/refund distinction. | https://www.tax.nd.gov/individual-income-tax | 2026-11-14 |
| 2026 Form ND-1ES. Read for all instructions and worksheet for duty tests, net-tax definition, payment timing, mailing and interest; rates read only to check owner inputs. | https://www.tax.nd.gov/sites/www/files/documents/forms/individual/2025-iit/28709-form-nd-1es-2026.pdf | 2026-11-14 |
| 2025 Schedule ND-1UT, 2025-2026 filing cycle. Read for both pages, exceptions, payment allocation, actual-day interest and rounding; not final 2026 form authority. | https://www.tax.nd.gov/sites/www/files/documents/forms/individual/2025-iit/28704-schedule-nd-1ut-2025.pdf | 2026-11-14 |
| 2025 Schedule ND-1NR, 2025-2026 filing cycle. Read for all columns, lines 1-23 and allocation instructions; four-decimal ratio. | https://www.tax.nd.gov/sites/www/files/documents/forms/individual/2025-iit/28724-schedule-nd-1nr-2025.pdf | 2026-11-14 |

Not yet confirmed: final2026ND-1/schedule layout, e-file authorization and paper-voucher/address continuation; full federal producer calculations in the legacy Sarah example; disputed conformity, unemployment subtraction, farm-election irrevocability and the old blanket no-local-income-tax claim. Special credits, foreign/mixed-residency and mineral extraction returns require their separate owners. The sources support only the stated read scope, not every upstream federal or state computation.
