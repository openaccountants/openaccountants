---
name: ca-return-assembly
description: Assemble and reconcile the Canadian sole proprietor's GST/HST, T2125, CPP/QPP and voluntary EI, T1, provincial or Quebec work and instalment schedules into one reviewer package. Keep every required income source and return in the completion register. Missing validated calculations or unresolved material differences prevent whole-package completion. Current 2026 planning is separate from the dated 2025 form bridge and from actual filing or payment.
version: 0.2
jurisdiction: CA
tax_year: 2026
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
category: orchestrator
type: filing-howto
depends_on:
  - canada-gst-hst
  - ca-fed-t2125
  - ca-fed-cpp-ei
  - ca-fed-t1-return
  - ca-fed-instalments
---

# Canada: assemble the sole proprietor return package

## Scope

Produce the full working-paper package for a full-year Canadian-resident individual with an unincorporated business or professional practice. The ordinary case has a calendar fiscal period. Load the actual current versions of the five named dependencies, the structured `ca-freelance-intake` output if available, and the applicable provincial method. A dependency can be not applicable to the facts; record why. This is an assembly and reconciliation method, not a replacement tax engine or an electronic filing service.

**Answer first:** assemble books and business/GST work, then contributions, then final federal and provincial tax, then the balance and future instalment decision. Keep all income. A completed worksheet is not a completed return, an accountant's approval, a filing acknowledgement or a payment receipt. The actual T1 requires complete income disclosure; missing relevant work leaves the whole package **INCOMPLETE**. [Actual 2025 T1, income and certification](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-r/5006-r-25e.pdf).

**Year control:** this version covers 2026 assembly/planning, with an explicitly dated 2025 final-form bridge for 2025 filing/amendment work. As read on 13 November 2026, the observed T1/T1139 catalogues and NETFILE service do not establish availability of final 2026 annual forms or certified 2026 filing. A 2026 estimate must be labelled as such. Recheck actual 2026 forms, software and line meanings before producing a filing-ready 2026 return; do not substitute a 2025 printed form or invent boxes. [T1 catalogue](https://www.canada.ca/en/revenue-agency/services/forms-publications/forms/5006-r.html), [T1139 catalogue](https://www.canada.ca/en/revenue-agency/services/forms-publications/forms/t1139.html), [actual software/service years](https://www.canada.ca/en/services/taxes/income-tax/personal-income-tax/how-file/tax-software.html).

Reuse collected facts and the whole intake record. Resolve contradictions against documents; ask only for the specific fact still missing. Do not ask which of the required deliverables to prioritize or how much detail the user wants. Continue unaffected work and preserve a checkpoint if context or tools run out, stating which calculations and artifacts remain incomplete. Follow the user's runtime communication instructions. Use available tools and an authorized output directory; no particular assistant, tool name or filesystem path is required.

### Completion and the accountant behind the work

For **each** consumed method, record its slug, returned version, tax year, scope, source/read date, returned approval label, approving accountant's name if actually present, input evidence, outputs and checks. Also record the exact rule/form used for any resolution. A missing name stays missing. A historic approval, a directory listing, the package preparer's identity, or approval of one child cannot approve another method or the assembled package. Do not derive professional approval from a source audit, a commit author or a successful numerical check. Preserve the platform's actual `Approved by [name]` or `Not yet approved` result for that version. This assembly remains unapproved unless the platform records a professional's approval of it.

Use these separate working-paper statuses:

| Status | Meaning and evidence required |
|---|---|
| INCOMPLETE | A required fact, income source, method, return, material reconciliation or required artifact is unresolved; list the owner and consequence. |
| WORKING PAPERS COMPLETE | Every applicable return and reconciliation has a supported computation and all required artifacts have been checked; still record any actual review/authorization required before filing. |
| FILED | The particular return was actually transmitted by an authorized filer and its acknowledgement was received. Record authority, account, year, receipt and any rejection separately for each return. |
| PAID | An authorized payment was actually made and matched to its authority, account, year/period and receipt. A bank instruction or return balance is not payment. |

These are workflow statuses, not additional public trust labels. There is no universal statutory CPA-signoff rule in this method: follow the actual filing channel, authorization and any agreed professional review. [T1 certification](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-r/5006-r-25e.pdf), [NETFILE](https://www.canada.ca/en/services/taxes/income-tax/personal-income-tax/how-file/tax-software.html), [T183 EFILE authorization purpose](https://www.canada.ca/en/revenue-agency/services/forms-publications/forms/t183.html).

## Ask the client first

Read the whole available case/intake, source documents and prior outputs first. Obtain only missing or conflicting items from these six groups:

1. Tax year, residence throughout the year, marital/common-law status, year-end province and each business permanent establishment; any migration, death or corporation/partnership involvement.
2. Every business/profession, fiscal period, ownership share, accounting basis, sales/other income, expense evidence and reconciled books; all employment, rental, investment, capital and foreign income/slips. A business bank account alone is not a complete income inventory.
3. GST/HST registration/effective dates, normal or Quick Method, reporting periods, returns/elections, associates where relevant, ITC eligibility, payments and adjustments; separate QST or other sales-tax work where applicable.
4. Prior CCA/UCC and home-office carryforwards, additions/dispositions and available-for-use dates, logs and mixed-use evidence; prior returns/assessments, loss/credit carryforwards, RRSP room, receipts and unused contributions.
5. All employment contribution slips, CPP/QPP/CPP2/QPP2 amounts and coverage, age/pension/disability/elections and dates, self-employed EI agreement/history; Quebec QPIP and related provincial work where relevant.
6. Current and prior-year instalment facts/reminders, actual payments/withholding by account/year, provincial work, outstanding amendments and filing authorization. Identify required output format and available filing software/channel without asking whether to omit required work.

The source forms and annual methods determine which fields are necessary: [T1](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-r/5006-r-25e.pdf), [T2125](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t2125/t2125-25e.pdf), [CPP/QPP routes](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-22200-deduction-cpp-qpp-contributions-on-self-employment-other-earnings.html), [RRSP room](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/rrsps-related-plans/contributing-a-rrsp-prpp/contributions-affect-your-rrsp-prpp-deduction-limit.html), [instalment options](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/options-calculate.html).

## The method, step by step

### 1. Build the completeness register and dependency record

List every required return/workstream, tax year or GST period, applicable method, current content/version, actual approval/name, input status, output status and owner. Preserve a row for something out of this assembler's computation scope when the client's actual return still needs it. Unknown is not zero and not automatically not applicable.

Inspect actual content. Remove the old Q2/Q4-placeholder assumptions: the named children may have substantial content, and an old version label proves neither availability nor correctness. If a child is missing, stale, internally inconsistent or unsuitable for the facts, get a source-supported replacement calculation/review. Do not fabricate its tax engine from memory, use a frozen fallback or present its unchecked result as validated. Continue independent work with the whole package INCOMPLETE.

Use the dependency chain below. Preparing an initial T1 income inventory before CPP is fine; finalizing T1 before the contributions/deductions and province are available is not.

| Order | Work and dependency | Required output and control |
|---|---|---|
| 1 | Confirm intake, books, each business/fiscal period, income inventory and provincial/Quebec route | Document index, reconciled facts, required-return register and open items. |
| 2 | `canada-gst-hst` and `ca-fed-t2125`, on their actual periods and methods | GST account-period return lines and business profit/CCA/home/vehicle schedules. Resolve recoverable taxes and Quick Method effects between them. [GST instructions](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/calculate-prepare-report/instructions-preparing-return.html), [T2125](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t2125/t2125-25e.pdf). |
| 3 | `ca-fed-cpp-ei` from final covered business/partnership and employment facts | CPP/QPP form/parts, base and enhancements, deduction, credit base, contribution payable; voluntary EI/Schedule 13 if applicable; actual Quebec QPIP route. [Schedule 8](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5000-s8/5000-s8-25e.pdf), [CPP/QPP](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-22200-deduction-cpp-qpp-contributions-on-self-employment-other-earnings.html), [EI](https://www.canada.ca/en/services/benefits/ei/ei-self-employed-workers/premiums.html). |
| 4 | `ca-fed-t1-return` plus actual provincial/territorial and Quebec work | Complete income/deductions, taxable income, federal/provincial credits/tax/contributions, Quebec abatement where applicable and final payable/credits. [T1](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-r/5006-r-25e.pdf), [T2203](https://www.canada.ca/en/revenue-agency/services/forms-publications/forms/t2203.html), [Quebec abatement](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-44000-refundable-quebec-abatement.html). |
| 5 | Final-year settlement and `ca-fed-instalments` for the specified next/current instalment year | Match actual withholding and instalments once; distinguish final balance, NTO threshold, amount due, chosen option and separate GST/Quebec schedules. Verify any older child result against the current actual chart, not a presumed prior-year fallback. [2026 chart](https://www.canada.ca/content/dam/cra-arc/migration/cra-arc/tx/ndvdls/tpcs/ncm-tx/pymnts/nstlmnts/Instalment-chart-fill-26e.pdf), [options](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/options-calculate.html). |
| 6 | Reconcile, assemble, check artifacts, obtain actual required authorization, hand off | All eleven components, ten workbook sheets and three artifacts below; five reconciliations and thirteen checks; unresolved required work blocks whole completion. |

### 2. Integrate business, GST/HST and CCA work

Prepare a separate business/profession computation and appropriate T2125 for each applicable activity. Retain accounting-period dates, gross revenue and adjustments, expense detail, CCA, partner adjustments if relevant, home-office limit/carryforward and final net income. **T2125 line 9368 is the expense subtotal, not a replacement for every later adjustment; Part 7 is business use of home; Part 8 is other partners; motor vehicle work is in its separate chart.** [Actual 2025 T2125, Parts 3-8 and motor-vehicle chart](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t2125/t2125-25e.pdf).

Use `canada-gst-hst` for classification and each actual GST return: account, effective dates, normal/Quick Method, period, taxable/zero-rated/exempt/outside-scope supply treatment, tax/adjustments, ITCs, other debits/credits and final remittance or refund. Registered does not mean every sale bears tax; an ordinary small supplier may have registered voluntarily. Non-registered/nonrecoverable tax is included only in an otherwise eligible cost, with capital and private use still distinguished. [GST return instructions](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/calculate-prepare-report/instructions-preparing-return.html), [ETA 148 threshold definition](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-148.html); use the child method for the actual registration/supply decision.

Carry CCA/UCC forward from the prior schedule and reconcile opening pools, additions, business use, recoverable tax/assistance, disposals, recapture/terminal loss, available-for-use dates, class and chosen claim. Missing opening records require reconstruction/evidence; do not set existing assets to zero or depreciate only new purchases. **AIIP is not an election to expense every asset in full.** AIIP, RIIP, designated immediate-expensing property and a class-specific first-year allowance have different dates and conditions. Consume the child CCA schedule and applicable enacted law, even where older printed 2025 form notes still call an enacted change proposed. [ITR 1100, actual applicable allowance and subsection (2)](https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-1100.html), [ITR 1104, definitions (3.1)-(4.01)](https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-1104.html), [ITA 230 records](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-230.html).

### 3. Import the right income and contribution lines

This table is the **actual 2025 form bridge**, not a claim that the final 2026 layout has been observed. Verify each final-year form before filing. The amounts retain their business/owner/year identity; do not send all professional income to the business line. [Actual T1](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-r/5006-r-25e.pdf), [actual T2125 final instructions](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t2125/t2125-25e.pdf).

| Output/meaning | Actual 2025 destination | Assembly control |
|---|---|---|
| Business gross / final net | T1 13499 / 13500 | Carry separately; never call 13500 gross. |
| Professional gross / final net | T1 13699 / 13700 | 13700 is professional net, not the net partner of 13500. |
| Commission gross / final net | T1 13899 / 13900 | Classify actual activity; include each final result once. |
| Employment income | 10100 | Match the relevant slips/adjustments, not business receipts. |
| Total income / net income / taxable income | 15000 / 23600 / 26000 | Include every applicable income schedule, deduction, loss and adjustment. |
| RRSP deduction / applicable dues | 20800 / 21200 where eligible | Use actual room/receipts and the correct deduction route; do not duplicate business expense claims. |
| Self-employed CPP/QPP deduction | 22200 | Import the actual form computation, not half total contributions. |
| Employment enhanced CPP/QPP deduction | 22215 | Employment enhancements; do not put all self-employed CPP2 here. |
| Employment base contribution credit / self-employed base contribution credit | 30800 / 31000 | Credit bases, not dollar-for-dollar refunds; the T1 method applies its actual year credit rate. |
| Self-employed voluntary EI credit / payable | 31217 / 42120 | If applicable, use actual Schedule 13 and the year/Quebec rules. |
| Other payments deduction | 25000 where applicable | Only its actual supported inputs; not a balancing amount. |
| Basic personal amount | 30000 | Actual year income-sensitive amount from T1, not a universal flat maximum. |
| Federal non-refundable credits / net federal tax | 35000 / 42000 | Use the applicable T1 method, credits and limitations. |
| CPP contributions payable | 42100 | This is not provincial tax. |
| Provincial/territorial tax | 42800 | Actual province form/PE allocation; Quebec TP-1 is separate. |
| Total payable / tax withheld | 43500 / 43700 | Withholding may include more than T4 box 22; reconcile all relevant slips. |
| Quebec abatement / actual income-tax instalments | 44000 / 47600 | Actual entitlement/payment year/account; not projected instalments or GST/QST payments. |
| Total credits / refund / balance owing | 48200 / 48400 / 48500 | Include all applicable credits; refund and owing are separate outcomes. |

For pure full-year CPP self-employment with no employment/QPP or special-month/election issue, the **base contribution** is split: half is the credit base at 31000, while half plus **all** first/second additional contributions is deducted at 22200; total contributions are payable at 42100. The two portions are not equal halves of total CPP. Employment/combined/QPP cases require their actual Schedule 8/RC381 and all relevant T4 boxes, coverage/elections/months; do not derive them by simply subtracting employment box 26 or one basic exemption from each business. [Actual Schedule 8 Parts 3-5](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5000-s8/5000-s8-25e.pdf), [ITA 60(e), (e.1)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-60.html), [CRA CPP/QPP routes](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-22200-deduction-cpp-qpp-contributions-on-self-employment-other-earnings.html).

Do not restate a full CPP rate table here. Published 2025 ceilings in the older version are not estimates: use the applicable year in the audited contribution method and [actual first-ceiling table](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/payroll-deductions-contributions/canada-pension-plan-cpp/cpp-contribution-rates-maximums-exemptions.html)/[second-ceiling table](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/calculating-deductions/making-deductions/second-additional-cpp-contribution-rates-maximums.html). Likewise the older 2025 basic-personal-amount maximum is a dated, income-sensitive maximum, not a missing/universal amount; use `ca-fed-t1-return` and the [actual indexed BPA rows](https://www.canada.ca/en/revenue-agency/services/tax/individuals/frequently-asked-questions-individuals/adjustment-personal-income-tax-benefit-amounts.html). Keep one parameter owner.

### 4. Complete province, Quebec and additional income work

For an ordinary single-jurisdiction case, use the correct province/territory and year, its tax/credits/surtax and the final federal inputs it requires. Federal bands are not provincial bands. Residence on December 31 is an input, not the only test when business permanent establishments allocate tax to multiple jurisdictions. Obtain the actual T2203 calculation if required. [T1 provincial field](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-r/5006-r-25e.pdf), [T2203 purpose](https://www.canada.ca/en/revenue-agency/services/forms-publications/forms/t2203.html).

Quebec requires actual TP-1 and relevant business schedules, QPP/CPP coordination, QPIP and federal abatement/other federal adjustments. Do not apply the pure-CPP calculation as a QPP engine. For the observed 2025 Quebec route, line 445 may use Schedule U or **LE-35-V instead** where the specified CPP amounts apply; QPIP line 439 may require Schedule R even when the person has not joined voluntary EI. Read the exact applicable-year conditions, not an old annual amount relabelled as current. The federal 44000 route also depends on residence and permanent establishments/T2203. [RQ 445](https://www.revenuquebec.ca/en/citizens/income-tax-return/completing-your-income-tax-return/line-by-line-help/400-to-447-income-tax-and-contributions/line-445/), [RQ 439](https://www.revenuquebec.ca/en/citizens/income-tax-return/completing-your-income-tax-return/line-by-line-help/400-to-447-income-tax-and-contributions/line-439/), [CRA 44000](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-44000-refundable-quebec-abatement.html). Federal work can progress while Quebec work is pending, but that is not a complete Quebec package.

Inventory rental/T776, capital/Schedule 3, foreign income/foreign tax credits/T2209 and any other required return/information reporting. Assign the right separate method/reviewer where this assembler lacks that computation, then incorporate validated results into T1/provincial work and the final balances. Do not exclude actual income just because it lies outside this method's direct engine. Non-resident/part-year, corporate, trust, special farming/fishing, death and complex partnership cases require the appropriate method before a complete-return claim. [T1 all-sources income and certification](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-r/5006-r-25e.pdf).

### 5. Run all five cross-skill reconciliations

Use a reconciliation record with source document, source/output line, entity/activity, period/year, method, signed amount, difference, explanation, evidence and resolved/pending status. A convenient monetary tolerance never cures a wrong line, missed business or period mismatch. Round only as the applicable form/method requires; explain actual rounding separately.

| Check | What must reconcile | How to resolve a difference |
|---|---|---|
| X1: GST/HST to business revenue | Bridge each GST account/period and the correct method to the matching books and all T2125 activities/fiscal periods; also explain 8299's other income/Quick Method adjustments. | Do not force GST 101 to equal one T2125 8299. Normal versus Quick Method, non-calendar reporting, multiple businesses, adjustments and timing can create supported differences. Exempt/zero-rated revenue is not automatically excluded from normal 101. Keep a quantified bridge and evidence. [GST instructions](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/calculate-prepare-report/instructions-preparing-return.html), [T2125](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t2125/t2125-25e.pdf). |
| X2: Business income to contributions | Trace each covered net self-employed/partnership amount, actual employment/coverage and appropriate form/parts to contribution inputs. | Explain adjustments, multiple activities, losses, elections and months. Do not apply an exemption twice, cap all CPP2 earnings at the first ceiling or use a universal box-26 subtraction. [Schedule 8](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5000-s8/5000-s8-25e.pdf), [CPP/QPP](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-22200-deduction-cpp-qpp-contributions-on-self-employment-other-earnings.html). |
| X3: Contributions to T1 | Match base/additional contribution components to 22200, 22215, 30800, 31000 and 42100, and applicable EI credit/payable. | Reconcile contributions, deduction and credit bases under the selected form. Do not confuse the credit base with the tax reduction or claim the same enhancement twice. [T1](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-r/5006-r-25e.pdf), [Schedule 8](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5000-s8/5000-s8-25e.pdf), [ITA 60](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-60.html). |
| X4: Payments and final balance | Match 43700 withholding and 47600 actual tax-year instalments to slips, bank and CRA records; include every other applicable credit in 48200. | Compare 43500 less 48200: positive goes to owing 48500, negative to refund 48400. Reconcile each payment's year/account, transfers and reversals; no forecast instalment, GST or Quebec payment enters 47600 merely because paid to a tax authority. [T1](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-r/5006-r-25e.pdf), [instalment chart](https://www.canada.ca/content/dam/cra-arc/migration/cra-arc/tx/ndvdls/tpcs/ncm-tx/pymnts/nstlmnts/Instalment-chart-fill-26e.pdf). |
| X5: Provincial/Quebec integration | Match residence/PE facts, federal taxable inputs and actual province calculations/credits/surtax; Quebec federal and TP-1 adjustments separately. | Verify each required return exists, the year is right and allocation/abatement/QPP/QPIP are resolved. Matching federal/provincial taxable income is not a substitute for actual provincial computation. [T2203](https://www.canada.ca/en/revenue-agency/services/forms-publications/forms/t2203.html), [abatement](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-44000-refundable-quebec-abatement.html), [RQ 445](https://www.revenuquebec.ca/en/citizens/income-tax-return/completing-your-income-tax-return/line-by-line-help/400-to-447-income-tax-and-contributions/line-445/), [RQ 439](https://www.revenuquebec.ca/en/citizens/income-tax-return/completing-your-income-tax-return/line-by-line-help/400-to-447-income-tax-and-contributions/line-439/). |

GST settlement has its own reconciliation: 105 includes applicable output-tax adjustments, 108 includes applicable credit adjustments, and 109 is their difference; then 110/111 credits and 205/405 other debits can change the final balance. Keep paper 113A/B/C and electronic field meanings distinct; the CRA working-copy worksheet is not a filed return. A GST refund does not automatically offset a T1 debt. [Actual return instructions](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/calculate-prepare-report/instructions-preparing-return.html), [actual working-copy warning and full flow](https://www.canada.ca/content/dam/cra-arc/migration/cra-arc/tx/bsnss/tpcs/gst-tps/bspsbch/rtrns/wrkngcp-eng.pdf).

### 6. Separate final-year payment from future planning

Current-year **actual instalments paid** are a credit in that year's return. Future instalments are a separate liability/amount decision. Use the current official chart and actual reminders; verify an older `ca-fed-instalments` output against them rather than inheriting its formulas unchecked.

For the **2026 ordinary individual income-tax instalment test**, net tax owing must exceed CAD 3,000 (CAD 1,800 for Quebec) in 2026 **and** either 2025 or 2024. NTO for this test excludes CPP and voluntary EI; the actual chart adds them when deriving the annual amount due. Do not subtract withholding twice, or subtract actual 47600 payments in the threshold calculation. The three choices are the actual no-calculation reminder amounts, prior-year calculation and current-year calculation, with underestimation interest/penalty risk for a chosen insufficient estimate. [CRA liability](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/who-pays-instalments.html), [2026 chart, lines 21-24](https://www.canada.ca/content/dam/cra-arc/migration/cra-arc/tx/ndvdls/tpcs/ncm-tx/pymnts/nstlmnts/Instalment-chart-fill-26e.pdf), [three options](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/options-calculate.html), [ITA 156, subject to 156.1](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-156.html).

INNS1 reminders are distinct from a notice of assessment. Check the August-only reminder branch and farming/fishing/death exceptions; do not force every case into four equal instalments. Quebec provincial and GST/HST instalments are separate workstreams. A 2026 return alone cannot establish mandatory 2027 instalments: the next-year current-income test and relevant history/actual reminder must be assessed. Show an explicitly conditional forecast with its assumptions. [Who pays, including August-only](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/who-pays-instalments.html), [actual options/chart](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/options-calculate.html), [due-date exceptions](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/due-dates.html).

RRSP planning uses defined prior-year **earned income**, unused room, the annual ceiling and relevant PA/PSPA/PAR adjustments, not 18% of T1 23600. Reconcile receipts, previously unused contributions, prior deductions and the chosen claim to the actual limit; neither current cash paid nor unused room alone is the deduction. Transfers/HBP/LLP repayments require their own treatment. Keep TFSA room as an uncomputed planning item unless separately verified. [CRA RRSP room/claim guidance](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/rrsps-related-plans/contributing-a-rrsp-prpp/contributions-affect-your-rrsp-prpp-deduction-limit.html), [ITA 146(1), (5), (5.1)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-146.html).

Carry next-year opening UCC/home-office losses, actual GST registration monitoring, instalment assumptions and applicable legislative changes into planning. Use dated published changes from the owning method; do not call a proposal enacted or an enacted rule still only a proposal because an old form says so. There is no Canadian `s290-170 equivalent` action to invent for RRSP.

### 7. Assemble all eleven components

| Component | Required content |
|---|---|
| 1. Executive summary | Client/year/status; single/married/common-law as applicable; residence/PE; business and GST periods; each income source, business gross/net, total/net/taxable income, RRSP, federal/provincial/QC tax, contributions, actual credits, refund/owing, conditional next-year instalments and remaining work. |
| 2. GST/HST worksheet | Each registration/account/period/method, classification, line 101 bridge, output tax/adjustments, ITCs/adjustments, 109, 110/111/205/405 and final balance/return flow; applicable elections and separate payment/filing status. |
| 3. T2125 worksheet | Each business/profession and fiscal period; 8299, cost of sales and other adjustments, detailed expenses/9368, partner/other adjustments, CCA, home-office 9945 and final 9946; actual vehicle chart and carryforwards. |
| 4. T1 worksheet | Complete income inventory/slips and schedules, correct gross/net activity lines, deductions including RRSP/CPP, 23600/26000, income-sensitive BPA, credits, federal tax, contributions, provincial tax, all credits and separate owing/refund. |
| 5. CCA schedule | Opening UCC, class, rate/rule/year, additions, assistance/recoverable tax, dispositions, available use, eligibility/elections, selected CCA, recapture/terminal loss and closing UCC. |
| 6. CPP/CPP2/EI worksheet | Coverage/form/parts, all covered earnings and slips, elections/months, base/enhancements, contribution payable, deduction/credit bases and EI agreement/Schedule 13; actual QPP/QPIP work if relevant. |
| 7. Provincial tax worksheet | Province/PE allocation, year/source/method, required tax/credit/surtax calculations, applicable Form 428/479, and Quebec TP-1/schedules and federal coordination. No invented provincial rate fallback. |
| 8. Instalment schedule | Specific instalment year, threshold history/current estimate, NTO and added contributions, actual reminder/method, dates and amounts/forecast status; distinguish CRA, Revenu Quebec and GST obligations. |
| 9. Reconciliation summary | X1-X5 with source/period/signed amounts, explained differences and resolved/pending status, plus GST final-balance bridge and the thirteen checks below. |
| 10. Reviewer brief | All of the above, dependency/approval record, positions with primary citations/evidence, flags, decisions, supported next-year planning, open items and actual completion/review/filing/payment status. |
| 11. Client action list | Authority/account/year, concrete authorized filer/payment steps, dates/amounts or exact missing input, relevant instalment calendar, recordkeeping/logging and next-year actions. |

Use this reviewer-brief structure and fill actual values rather than leaving `$X` as a computation:

```markdown
# Canada return package: [client], [tax year]
Status: [INCOMPLETE / WORKING PAPERS COMPLETE]; estimate or actual form year: [...]
## Executive summary
Residence/PE, family status, entities/businesses, periods, complete income,
T1 totals, provincial/QC work, contributions, credits, refund/owing, next-year assumptions.
## Methods, sources and accountants
One row per actual returned method/version/year/scope/approval/name/checks.
## GST/HST by account and period
Normal/Quick Method, revenue bridge, every applicable return line, final balance and dates.
## Business/professional statements
Per-activity T2125, expenses, home/vehicle/CCA/partner schedules, final net and T1 destination.
## T1 and provincial/Quebec work
All income/deductions/credits/contributions, actual form lines, province/PE and TP-1 status.
## Contributions
CPP/QPP/CPP2/QPP2, voluntary EI, QPIP; component/deduction/credit/payable reconciliation.
## Instalments and final-year settlement
Actual paid credits once; NTO eligibility separate from future annual amount/options/calendar.
## Cross-skill reconciliations and self-checks
X1-X5, CA1-CA13, differences and resolved/pending evidence.
## Reviewer attention flags
Missing/contradictory facts, mixed use, missing logs, home-office conditions,
CCA claim/election/UCC, RRSP room, meal exceptions, registration, Quebec and special income.
## Positions taken
Facts, selected rule, statutory provision, current official URL, consequence and reviewer decision.
## Next-year planning
Conditional instalments, defined earned-income RRSP room, UCC/carryforwards,
GST registration monitoring, verified changes, TFSA room only if separately established.
## Client action list and outstanding work
Per-return filing/payment/authorization/receipt, owner, date, amount, dependencies and missing artifacts.
```

Keep these six original example position patterns, with the actual facts and correct authority, not a boilerplate declaration that they apply:

| Position pattern | Evidence and legally supported question |
|---|---|
| Home office | Principal-place-of-business **or** exclusive income use plus regular client meetings; allocation, income limit and carryforward. [ITA 18(12)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-18.html). |
| Motor vehicle | Actual business purpose/use, full-year km log and child calculation of current cost/CCA/automobile limits. ITA 18(1)(r) is an allowance limit, not generic authority for every sole-proprietor vehicle deduction. [ITA 18(1)(a), (r)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-18.html), [T2125 vehicle chart](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t2125/t2125-25e.pdf). |
| Dell laptop | Cost, class, business use, acquisition and available-use dates, opening pool/assistance and actual allowance rule/claim. Do not label all AIIP a full immediate-expensing election. [ITR 1100](https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-1100.html), [1104](https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-1104.html). |
| Meals and entertainment | Actual reasonable business cost and ordinary restriction, eligible long-haul or other statutory exception, with evidence; do not apply one percentage to all costs. [ITA 67.1](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-67.1.html). |
| RRSP | Receipts/current and carried unused contributions, actual limit/adjustments, chosen deduction and applicable-year timing. [ITA 146](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-146.html), [CRA](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/rrsps-related-plans/contributing-a-rrsp-prpp/contributions-affect-your-rrsp-prpp-deduction-limit.html). |
| CPP | Actual coverage/form, all earnings/month/election facts, contribution components and separate deduction/credit/payable; pure-SE split is not all-total half. [Schedule 8](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5000-s8/5000-s8-25e.pdf), [ITA 60](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-60.html). |

### 8. Produce and verify the three artifacts

Produce `[client_slug]_[tax_year]_canada_master.xlsx`, `reviewer_brief.md` and `client_action_list.md` using the available authorized artifact/file tools. If XLSX generation is unavailable, supply the actual available tables/equivalent and say the workbook was not produced; the full requested artifact set remains incomplete. Do not claim to have used a particular tool or created a file without doing so. Preserve partial work and list exactly what remains.

The master workbook retains **all ten** original sheets: **Cover, GST34, T2125, T1 Summary, CCA Schedule, Expense Detail, CPP/EI Calculation, Provincial Tax, Instalment Schedule, Cross-Check Summary**. Use extra per-business/period or special-income sheets where needed; ten sheets are a minimum structure, not a reason to drop a return. Keep `GST34` as the preparatory sheet name without calling a working copy an accepted return.

Use formulas to connect the correct final net business/professional/commission output to its T1 destination, contribution inputs to their actual source, and payments/credits to the correct final-year calculation. Forecast instalments must reference their own year and eligible base. Preserve source references and inputs, avoid double-counted subtotals and hard-coded copied totals. Recalculate and read back results, check `#REF!`, `#VALUE!`, circular references, broken links and displayed precision; match the validated model with the actual form rounding rules, not a generic one-dollar tolerance. An unrendered/unrecalculated workbook is not verified merely because its formulas look right. Workbook checks do not establish legal eligibility or filing.

## Boundary and exception table

| Boundary | Treatment and effect on completion | Primary basis |
|---|---|---|
| Calendar versus elected non-calendar business period | Ordinary calendar path is covered. Eligible alternative fiscal years are **not** limited to pre-1995 businesses. Confirm actual election, eligibility, timing and any change/consent. Obtain T1139 fiscal-to-calendar/additional-income reconciliation before the final T1 result; do not silently switch periods. | [ITA 249.1(1), (4)-(7)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-249.1.html), [actual T1139 Parts 1/2/4/5/6](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t1139/t1139-25e.pdf). |
| Quebec | Federal progress is allowed; complete actual TP-1, QPP/CPP, QPIP and federal adjustment work before whole completion. | [RQ filing](https://www.revenuquebec.ca/en/citizens/income-tax-return/filing-your-income-tax-return/deadline-for-filing-your-income-tax-return/), [445](https://www.revenuquebec.ca/en/citizens/income-tax-return/completing-your-income-tax-return/line-by-line-help/400-to-447-income-tax-and-contributions/line-445/), [439](https://www.revenuquebec.ca/en/citizens/income-tax-return/completing-your-income-tax-return/line-by-line-help/400-to-447-income-tax-and-contributions/line-439/), [44000](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-44000-refundable-quebec-abatement.html). |
| Multiple business permanent establishments | Obtain actual jurisdiction allocation/T2203; year-end residence alone is insufficient. | [T2203](https://www.canada.ca/en/revenue-agency/services/forms-publications/forms/t2203.html). |
| Rental, capital and foreign income | Required specialist/schedule work must be incorporated, not omitted from taxable income because it was flagged. | [T1 income/certification](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-r/5006-r-25e.pdf). |
| Missing prior CCA schedule | Obtain/reconstruct evidence; leave affected computation and whole completion pending rather than dropping existing assets. | [T2125](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t2125/t2125-25e.pdf), [ITA 230](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-230.html). |
| Normal/Quick Method, registered small supplier, separate GST periods | Follow actual registration/method/period; document X1 bridge and final return balance; no automatic gross-expense or tax-all-sales rule. | [GST instructions](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/calculate-prepare-report/instructions-preparing-return.html), [ETA 148](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-148.html). |
| Self-employed EI or Quebec employment/coverage | Actual agreement, calendar-year premium, earnings/slips and Schedule 13; benefit eligibility is separate. QPIP is not eliminated by not joining voluntary EI. | [EI premiums](https://www.canada.ca/en/services/benefits/ei/ei-self-employed-workers/premiums.html), [RQ 439](https://www.revenuquebec.ca/en/citizens/income-tax-return/completing-your-income-tax-return/line-by-line-help/400-to-447-income-tax-and-contributions/line-439/). |
| Missing child method or failed material check | Work can continue independently; required computation and whole package remain INCOMPLETE until supported and resolved. | [T1 complete-disclosure certification](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-r/5006-r-25e.pdf); assembly control. |
| Final 2026 forms/software not observed | 2026 estimate remains an estimate; retain dated 2025 bridge and recheck actual 2026 forms/channel before filing readiness. | [T1 catalogue](https://www.canada.ca/en/revenue-agency/services/forms-publications/forms/5006-r.html), [NETFILE years](https://www.canada.ca/en/services/taxes/income-tax/personal-income-tax/how-file/tax-software.html). |

### Capability limits retained from the original

1. PDF population is not automated by this method; working papers are not prescribed filed returns.
2. Electronic filing requires the actual eligible software/channel, filer and authorization; see Filing and payment.
3. Payment execution is separate and needs actual authority and confirmation.
4. Quebec work must be provided by the appropriate actual method; no permanent Q4-stub assumption.
5. Rental/T776 work is separately computed and then integrated if present.
6. Capital/Schedule 3 work is separately computed and then integrated if present.
7. Foreign income/FTC/T2209 and other required reporting are separately computed and integrated if present.
8. Prior CCA/UCC gaps require evidence/reconstruction; no zero-opening fallback.
9. Missing/unsuitable upstream work remains a real gap; no from-memory calculation substitute.
10. Instalments need current-year/history/actual-reminder facts and source-checked options; no automatic prior-year fallback.
11. Provincial work needs its own tax/credit/PE method; do not use federal rates as provincial rates.
12. Current 2026 estimates and actual 2025 forms are distinguished; final 2026 layouts remain to be verified.
13. Voluntary EI premiums and agreement history are integrated; special-benefit entitlement is not awarded by this assembler.

## Worked cases

All amounts below are **illustrative upstream inputs**, not a client's return or an independent rerun of every child tax engine. The checks test assembly arithmetic and choices. Eligibility, source documents, form year and complete income still require the method above.

### Case 1. Two businesses and a reasoned GST bridge

For a normal-method, calendar-year example, matching GST account revenue is CAD 150,000: business sales 100,000 and professional sales 50,000. Validated T2125 outputs include business 8299 of 102,000 (the 100,000 plus separately established other business income of 2,000 outside this example's GST 101) and net 60,000; professional gross 50,000 and net 30,000. The aggregate T2125 gross is 152,000, with an evidenced 2,000 bridge difference, not a failed mandatory equality or a reason to alter sales. In the actual 2025 bridge, business gross/net go to 13499/13500 and professional gross/net to 13699/13700. Only net 90,000 enters the relevant total-income computation once. Whether the specific 2,000 really lies outside 101 must be established from its nature; this example supplies that validated fact rather than inferring it from a bank label. [GST period/method instructions](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/calculate-prepare-report/instructions-preparing-return.html), [T2125](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t2125/t2125-25e.pdf), [T1](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-r/5006-r-25e.pdf).

```oa-check
name: Two activities and evidenced GST revenue bridge
inputs:
  gst_101: 150000
  business_sales: 100000
  other_business_income: 2000
  business_net: 60000
  professional_gross: 50000
  professional_net: 30000
steps:
  - business_gross: business_sales + other_business_income
  - all_business_gross: business_gross + professional_gross
  - bridge_difference: all_business_gross - gst_101
  - unexplained_difference: bridge_difference - other_business_income
  - net_income_once: business_net + professional_net
expected:
  business_gross: 102000
  all_business_gross: 152000
  bridge_difference: 2000
  unexplained_difference: 0
  net_income_once: 90000
```

### Case 2. Contribution components are not two equal halves

An actual validated pure-SE, full-year, non-Quebec/no-employment 2026 contribution output at the annual maxima supplies base CPP 7,038.90, first additional 1,422.00 and second additional 832.00. The assembly credit **base** is 3,519.45; deduction is 5,773.45; payable is 9,292.90. These sum correctly; neither portion is the half-total of 4,646.45. The difference of 1,127.00 identifies the old wrong allocation. This is a consumption test of the named child result, not a general mixed-income contribution formula or a dollar-for-dollar credit. [2026 CPP/CPP2 source rows](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/payroll-deductions-contributions/canada-pension-plan-cpp/cpp-contribution-rates-maximums-exemptions.html), [second ceiling](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/calculating-deductions/making-deductions/second-additional-cpp-contribution-rates-maximums.html), [actual 2025 form bridge](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5000-s8/5000-s8-25e.pdf), [ITA 60(e)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-60.html); before 2026 filing verify the final annual form.

```oa-check
name: Imported 2026 pure-SE CPP components and allocation
inputs:
  base_cpp: 7038.90
  first_additional: 1422
  second_additional: 832
steps:
  - total_cpp: base_cpp + first_additional + second_additional
  - credit_base: base_cpp / 2
  - deduction: base_cpp / 2 + first_additional + second_additional
  - allocation_check: deduction + credit_base - total_cpp
  - wrong_half: total_cpp / 2
  - wrong_allocation_difference: deduction - wrong_half
expected:
  total_cpp: 9292.90
  credit_base: 3519.45
  deduction: 5773.45
  allocation_check: 0
  wrong_half: 4646.45
  wrong_allocation_difference: 1127
```

### Case 3. Owing versus refund and separate GST balance

Suppose a completed T1 computation supplies total payable 20,000, actual withholding 8,000, instalments paid for this year 9,000 and all other credits 1,000. Credits total 18,000: owing is 2,000 and refund zero. With actual instalments of 12,000 instead, credits are 21,000: owing zero, refund 1,000. Do not subtract payments a second time. The actual 2025 destinations are 43500/43700/47600/48200/48400/48500. [T1](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-r/5006-r-25e.pdf).

Separately, suppose verified GST 109 is 4,000, 110/111 are 1,000/200 and 205/405 are 500/100: the final amount is 3,400, not 4,000. These are distinct authority accounts; a taxpayer cannot silently net one against the other in this worksheet. [GST instructions](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/calculate-prepare-report/instructions-preparing-return.html), [working-copy final flow](https://www.canada.ca/content/dam/cra-arc/migration/cra-arc/tx/bsnss/tpcs/gst-tps/bspsbch/rtrns/wrkngcp-eng.pdf).

```oa-check
name: T1 payment credit once and owing or refund decision
inputs:
  payable: 20000
  withholding: 8000
  paid_a: 9000
  paid_b: 12000
  other_credits: 1000
steps:
  - credits_a: withholding + paid_a + other_credits
  - owing_a: max(0, payable - credits_a)
  - refund_a: max(0, credits_a - payable)
  - credits_b: withholding + paid_b + other_credits
  - owing_b: max(0, payable - credits_b)
  - refund_b: max(0, credits_b - payable)
expected:
  credits_a: 18000
  owing_a: 2000
  refund_a: 0
  credits_b: 21000
  owing_b: 0
  refund_b: 1000
```

```oa-check
name: GST final settlement includes other credits and debits
inputs:
  net_tax_109: 4000
  instalments_110: 1000
  rebates_111: 200
  other_debit_205: 500
  other_debit_405: 100
steps:
  - after_credits: net_tax_109 - instalments_110 - rebates_111
  - final_balance: after_credits + other_debit_205 + other_debit_405
expected:
  after_credits: 2800
  final_balance: 3400
```

### Case 4. Instalment eligibility differs from amount, with both decisions

For a non-Quebec ordinary 2026 individual, supplied NTO is 4,000 and a prior relevant year's NTO was also above the standard threshold; supplied annual CPP and voluntary EI for the selected calculation option are 1,000/100. The threshold is satisfied on the given history. Annual amount is 5,100 and, **only for this ordinary equal-quarter chosen option**, each instalment is 1,275. The source chart owns the actual computation. If current NTO is 2,500 with CPP 9,000 instead, CPP does not make that NTO exceed the threshold: that case does not require standard instalments on those facts. Exactly 3,000 does not exceed 3,000; current above the threshold with neither previous year above also fails the ordinary liability condition. The August-only/no-calculation and farmer/fisher branches must not inherit this equal-quarter example. [Actual 2026 liability](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/who-pays-instalments.html), [chart](https://www.canada.ca/content/dam/cra-arc/migration/cra-arc/tx/ndvdls/tpcs/ncm-tx/pymnts/nstlmnts/Instalment-chart-fill-26e.pdf), [options](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/options-calculate.html).

```oa-check
name: Ordinary instalment annual amount is not the NTO threshold
inputs:
  eligible_nto: 4000
  cpp: 1000
  voluntary_ei: 100
  below_threshold_nto: 2500
  standard_threshold: 3000
  high_cpp: 9000
steps:
  - annual_due: eligible_nto + cpp + voluntary_ei
  - ordinary_quarter: annual_due / 4
  - below_threshold_margin: below_threshold_nto - standard_threshold
  - misleading_total: below_threshold_nto + high_cpp
  - exactly_threshold_margin: standard_threshold - standard_threshold
expected:
  annual_due: 5100
  ordinary_quarter: 1275
  below_threshold_margin: -500
  misleading_total: 11500
  exactly_threshold_margin: 0
```

### Case 5. RRSP room is not a fraction of net income

Assume the properly defined earned-income input is business income 60,000; interest 10,000 does not enter that earned-income input and an existing-year RRSP deduction is 5,000. For this limited illustration, net income is 65,000. The raw next-year earned-income component at 18% is 10,800, not 11,700. This is **not final new room or the available deduction**: the applicable annual cap, carryforward and PA/PAR/PSPA adjustments and actual contributions/claim must still be applied. [CRA room calculation](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/rrsps-related-plans/contributing-a-rrsp-prpp/contributions-affect-your-rrsp-prpp-deduction-limit.html), [ITA 146 defined earned income](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-146.html).

```oa-check
name: RRSP earned-income component versus wrong net-income proxy
inputs:
  earned_income: 60000
  interest_income: 10000
  existing_rrsp_deduction: 5000
steps:
  - illustrated_net_income: earned_income + interest_income - existing_rrsp_deduction
  - raw_earned_component: earned_income * 0.18
  - wrong_net_component: illustrated_net_income * 0.18
  - proxy_error: wrong_net_component - raw_earned_component
expected:
  illustrated_net_income: 65000
  raw_earned_component: 10800
  wrong_net_component: 11700
  proxy_error: 900
```

### Case 6. Complete federal worksheet, incomplete Quebec package

A Quebec client's federal worksheet reconciles, but TP-1/QPP/QPIP work is not supplied; or a rental/foreign schedule remains missing. Preserve the completed supported federal work, identify each missing schedule and its consequential federal/provincial effects, and mark the whole package INCOMPLETE. Do not fill the missing amount with zero, omit the income or call it a complete return because the workbook formulas balance. Once the required work is provided and integrated, rerun all affected checks and final balances. [T1 full disclosure](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-r/5006-r-25e.pdf), [Quebec routes](https://www.revenuquebec.ca/en/citizens/income-tax-return/completing-your-income-tax-return/line-by-line-help/400-to-447-income-tax-and-contributions/line-445/), [QPIP](https://www.revenuquebec.ca/en/citizens/income-tax-return/completing-your-income-tax-return/line-by-line-help/400-to-447-income-tax-and-contributions/line-439/), [abatement](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-44000-refundable-quebec-abatement.html).

## When to refuse or refer

Keep these six original IDs so existing workflow references still point to a concrete action:

| ID | Trigger | Action and completion effect |
|---|---|---|
| R-CA-1 | Required upstream method/output missing or not validated | Name it, record required facts/year/source and obtain supported output; continue independent work, hold affected calculation and whole completion. |
| R-CA-2 | Upstream self-check failed | Name the actual failure and financial/return effect; resolve or keep pending. A failed material check is not merely a warning attached to a complete return. |
| R-CA-3 | Cross-skill reconciliation failed | Quantify the difference, inspect period/scope/basis/rounding and underlying evidence; resolve or hold completion, never alter figures just to make them match. |
| R-CA-4 | Intake fact missing/contradictory | Search existing records, resolve documentary conflicts, then ask only for the exact unavailable item and explain what depends on it. No guessed defaults. |
| R-CA-5 | Rental/capital/foreign/other specialist work discovered | Obtain the appropriate calculation/schedule, integrate it and rerun dependencies. Keep whole package incomplete while required income/reporting remains unresolved. |
| R-CA-6 | Quebec work required | Obtain actual TP-1, QPP/CPP, QPIP and federal coordination work. Continue useful federal preparation without claiming the whole Quebec package is complete. |

These are assembly safeguards grounded in the [T1 complete-disclosure certification](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-r/5006-r-25e.pdf) and actual contribution/provincial routes above. They do not prohibit answering a supported narrower question with its precise scope. They do prohibit inventing an accountant's approval, unverified tax result, filed return or payment confirmation.

## Filing and payment

### Separate calendar by return, authority and year

Keep one row per obligation with authority/account, return or instalment year/period, ordinary deadline, exception, actual adjusted date, amount/source, owner and current status. For a past due date, show overdue status and obtain actual current balance/interest rather than silently moving it to a future date. Filing extensions do not automatically extend payment.

| Ordinary branch | Dated deadline/control | Source |
|---|---|---|
| Ordinary self-employed 2025 T1 | Payment April 30, 2026; qualifying self-employed filing June 15, 2026. Record business primarily involving tax-shelter costs and other exceptions through the actual T1 method. | [Actual 2025 T1 payment note](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-r/5006-r-25e.pdf), [current CRA deadline explanation](https://www.canada.ca/en/services/taxes/resources-for-small-and-medium-businesses/2026-tax-deadlines-canadian-businesses-self-employed-individuals.html). |
| Ordinary self-employed 2026 T1 | Payment April 30, 2027; qualifying filing June 15, 2027. These are actual dates on the current CRA **2027** page despite its 2026 URL slug; final annual forms/software still require checking. | [Actual current CRA page](https://www.canada.ca/en/services/taxes/resources-for-small-and-medium-businesses/2026-tax-deadlines-canadian-businesses-self-employed-individuals.html). |
| GST monthly/quarterly or ordinary annual | Use the actual period: ordinarily one month after monthly/quarterly end or three months after annual end. The individual calendar-year business exception requires all applicable criteria; payment April 30 and filing June 15 are not every annual filer's deadlines. | [GST reporting/deadlines](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/file-gst-hst-return/reporting-requirements-deadlines.html). |
| Qualifying calendar-year individual annual GST for 2026 | Payment April 30, 2027 and filing June 15, 2027, only if the actual exception applies. Match own GST account/return, not T1. | [GST deadline criteria](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/file-gst-hst-return/reporting-requirements-deadlines.html), [CRA 2027 explanation](https://www.canada.ca/en/services/taxes/resources-for-small-and-medium-businesses/2026-tax-deadlines-canadian-businesses-self-employed-individuals.html). |
| Quebec annual return | Ordinary filing April 30, or qualifying business/spouse-business June 15; payment remains April 30. Check actual year, special cases and recognized non-business days separately. | [RQ deadline rule](https://www.revenuquebec.ca/en/citizens/income-tax-return/filing-your-income-tax-return/deadline-for-filing-your-income-tax-return/). |
| Ordinary CRA 2026 income-tax instalments | March **16**, June 15, September 15 and December 15, 2026: nominal March 15 is Sunday. Actual reminder/method/eligibility and special branches control the amounts. | [CRA nominal dates/weekend rule](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/due-dates.html), [liability](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/who-pays-instalments.html). |
| Conditional ordinary 2027 instalment forecast | Nominal March 15, June 15, September 15, December 15, 2027; all are weekdays by calendar calculation. Recheck recognized holidays, actual current-year conditions and reminders before presenting actual obligations. | [ITA 156 dates](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-156.html), [CRA exceptions](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/due-dates.html). |
| RRSP 2025 / 2026 contribution timing | Actual CRA 2025 period ends March 2, 2026. For 2026, the statutory first-60-days calculation reaches March 1, 2027; this is a calculated ordinary endpoint, not a claimed observed final 2026 CRA form/calendar. Actual deductibility/age/claim/plan conditions remain necessary. | [CRA 2025 period](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/rrsps-related-plans/contributing-a-rrsp-prpp/contributions-affect-your-rrsp-prpp-deduction-limit.html), [ITA 146(5), (5.1)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-146.html). |

Do not print obsolete example amounts or rates into client actions. Use the actual child result, including the taxability/place rules for invoices, not “charge GST on all sales.” For ongoing work, retain km logs and allocation records, track home-office expenses/use, monitor the actual registration test and review instalment assumptions as income changes. Reconcile tax accounts and maintain next-year UCC/carryforward records.

### Actual filing, confirmation and payment handoff

1. Select the actual tax-year form/software and eligible channel. NETFILE is the individual's certified-software route; EFILE is the eligible preparer's route. Paper/other channels follow their actual requirements. The observed current NETFILE initial-return service covers 2018-2025 and ReFILE 2022-2025; it does not prove 2026 annual return filing is open. [CRA actual software/service page](https://www.canada.ca/en/services/taxes/income-tax/personal-income-tax/how-file/tax-software.html).
2. Give the filer the completed supported schedules and open-item register. Resolve required missing work before complete filing readiness. The preparer obtains actual authorization for the actual channel; T183 is the individual's EFILE authorization form, not a blanket authority to access accounts or make payments. This method has not newly verified every T183 signature/retention detail; the filer must use the actual year form/instructions. [T183 catalogue/purpose](https://www.canada.ca/en/revenue-agency/services/forms-publications/forms/t183.html).
3. GST/HST is filed through the applicable account/channel specified in `canada-gst-hst`; TP-1 through the applicable Revenu Quebec channel. Recheck any actual submission and mandate rules. No working-copy sheet, draft PDF or this package itself is a filed return. [GST working-copy warning](https://www.canada.ca/content/dam/cra-arc/migration/cra-arc/tx/bsnss/tpcs/gst-tps/bspsbch/rtrns/wrkngcp-eng.pdf), [RQ annual filing information](https://www.revenuquebec.ca/en/citizens/income-tax-return/filing-your-income-tax-return/deadline-for-filing-your-income-tax-return/).
4. Preserve submission acknowledgement/status per return; handle a rejection as not filed. Record the transmitted version and actual confirmation number/date, not just “sent to reviewer.” Actual filing is outside this method's automatic capabilities.
5. Prepare payment instructions only from actual verified authority/account/year and balance. Do not guess a bank payee/reference, send an unauthorized payment, or assume an income-tax payment also settles GST/QST/Quebec. If current balance/interest or account reference is unknown, list that exact item. Match any authorized executed payment to a receipt/account entry and report pending processing honestly.
6. Retain supporting records: generally six years from the end of the last tax year they relate to, with the actual late-filed-return, objection/appeal, Minister extension and other retention rules. Keep electronic records readable and capital/UCC evidence for the later years it supports; do not indiscriminately delete at six years after acquisition. [ITA 230(1), (4)-(8)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-230.html).

## Completion checklist

Record **pass, not applicable with evidence, or pending**, with reviewer/source and consequence. Every required material pending item leaves whole completion INCOMPLETE. Keep a separate artifact/filing/payment status.

| Original check | Revised check |
|---|---|
| CA1 | All applicable child and provincial/special-income outputs exist, source/year/version/actual approval are recorded, checks are supported; no placeholder fallback. |
| CA2 | X1 bridges actual GST periods/method/business scope to T2125 with all differences explained; no false one-dollar-equality requirement. |
| CA3 | X2 traces every covered net-income/employment/partnership input and correct CPP/QPP form/month/election; exemption and bands are not guessed or duplicated. |
| CA4 | X3 separates base and enhancements, self-employed/employment deductions, credit bases and payable; no half-total or self-employed-CPP2-to-22215 error. |
| CA5 | Actual current-return-year 47600 instalments and 43700 withholding matched once to records; transfers/reversals/other accounts separated, refund/owing correct. |
| CA6 | Actual registered normal/Quick Method revenue, recoverable tax/cost/ITC and full GST final-balance treatment reconcile without double counting. |
| CA7 | Actual registration/effective dates and small-supplier/voluntary status established; nonrecoverable tax only enters an otherwise eligible expense/asset. |
| CA8 | CCA class/UCC/additions/disposals/business use/available-use/assistance and chosen dated rule/election supported; no all-AIIP-full-expensing assumption. |
| CA9 | RRSP limit, unused contributions, receipts, prior claims/adjustments and chosen eligible deduction agree; no 18%-of-23600 room proxy. |
| CA10 | Actual reasonable business meals/entertainment restriction or evidenced long-haul/statutory exception applied by the child; no automatic one-rate-all rule. |
| CA11 | Fiscal period/election/timing/T1139 calendar reconciliation established; no pre-1995-only condition or silent fiscal-year change. |
| CA12 | All applicable filing/payment, income-tax/GST/Quebec instalment and RRSP dates/amounts have the correct year/account/conditions and non-business-day adjustment. |
| CA13 | Residence, business PE allocation, actual province/territory rates/credits/surtax, T2203 and required Quebec TP-1/QPP/QPIP/federal adjustments integrated. |

Also check all eleven document components, ten original sheets and three artifacts; recompute/read back formulas; compare every displayed total with the validated model; retain detailed positions/citations, unresolved flags and next-year planning. Do not call missing artifacts produced, a source reviewer an approving accountant, or prepared work filed/paid.

## Sources

Read date **2026-11-13** for the bounded portions below. “Read” means the operative content, not a successful download. The 2025 forms are explicitly dated bridges; current 2026 parameters/chart and enacted law are separate. These reads do not certify whole Acts, all provincial/Quebec engines, benefit awards, client inputs, actual filing, software generation or payments. Three normal Revenu Quebec command-line downloads returned HTTP 403; the relevant public pages were read through ordinary web access. No access control was bypassed. Justice consolidations observed current to October 19, 2026, last amended June 18, 2026; reconfirm later operative amendments before a later-year filing.

| ID | Official source and portion read | Short exact locator | Read on |
|---|---|---|---|
| A01 | [Read for: Actual2025 OntarioT1 pages1,3–8; income, deductions, CPP/EI, province, credits, refund and certification](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-r/5006-r-25e.pdf) | “all sources inside and outside Canada” | 2026-11-13 |
| A02 | [Read for: Observed current catalogue](https://www.canada.ca/en/revenue-agency/services/forms-publications/forms/5006-r.html) | “2025 - Standard print PDF” | 2026-11-13 |
| A03 | [Read for: Actual2025T2125 pp1–4, motor-vehicle chart; source also read in child review](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t2125/t2125-25e.pdf) | “For each business or profession” | 2026-11-13 |
| A04 | [Read for: Actual2025Schedule8 pp1–2,6–7 and Part5 inputs](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5000-s8/5000-s8-25e.pdf) | “no employment income” | 2026-11-13 |
| A05 | [Read for: Calculating deduction; CPP/QPP routes, partnership and proration](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-22200-deduction-cpp-qpp-contributions-on-self-employment-other-earnings.html) | “whichever applies” | 2026-11-13 |
| A06 | [Read for: ITA60(e),(e.1) deduction portions; selected operative provisions](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-60.html) | “CPP/QPP contributions on self-employed earnings” | 2026-11-13 |
| A07 | [Read for: Actual2025/2026 annual CPP rows](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/payroll-deductions-contributions/canada-pension-plan-cpp/cpp-contribution-rates-maximums-exemptions.html) | “Maximum annual self-employed contribution” | 2026-11-13 |
| A08 | [Read for: Actual2025/2026 CPP2 rows](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/calculating-deductions/making-deductions/second-additional-cpp-contribution-rates-maximums.html) | “Maximum annual self-employed contribution” | 2026-11-13 |
| A09 | [Read for: Current self-employed EI premiums and entire-calendar-year paragraph](https://www.canada.ca/en/services/benefits/ei/ei-self-employed-workers/premiums.html) | “entire calendar year” | 2026-11-13 |
| A10 | [Read for: GST return instructions: account/period,101/90/91/102, method differences, other debits](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/calculate-prepare-report/instructions-preparing-return.html) | “for the reporting period” | 2026-11-13 |
| A11 | [Read for: GST deadlines, reporting period, nil return and individual annual exception](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/file-gst-hst-return/reporting-requirements-deadlines.html) | “all 3 criteria” | 2026-11-13 |
| A12 | [Read for: Actual working-copy PDF text read; field bridge](https://www.canada.ca/content/dam/cra-arc/migration/cra-arc/tx/bsnss/tpcs/gst-tps/bspsbch/rtrns/wrkngcp-eng.pdf) | “Do not use this working copy to file your return” | 2026-11-13 |
| A13 | [Read for: 2026 instalment liability and August-only reminder](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/who-pays-instalments.html) | “either 2025 or 2024” | 2026-11-13 |
| A14 | [Read for: Three calculation options and interest risk](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/options-calculate.html) | “3 options” | 2026-11-13 |
| A15 | [Read for: Actual two-page2026 instalment chart read entirely](https://www.canada.ca/content/dam/cra-arc/migration/cra-arc/tx/ndvdls/tpcs/ncm-tx/pymnts/nstlmnts/Instalment-chart-fill-26e.pdf) | “Net tax owing” | 2026-11-13 |
| A16 | [Read for: ITA156(1) and actual instalment-base alternatives](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-156.html) | “Subject to section 156.1” | 2026-11-13 |
| A17 | [Read for: Actual2026 nominal due dates and exceptions](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/due-dates.html) | “next business day” | 2026-11-13 |
| A18 | [Read for: CRA current fact sheet, self-employed and GST paragraphs](https://www.canada.ca/en/services/taxes/resources-for-small-and-medium-businesses/2026-tax-deadlines-canadian-businesses-self-employed-individuals.html) | “June 15, 2027” | 2026-11-13 |
| A19 | [Read for: ITA249.1(1),(4)–(7)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-249.1.html) | “Alternative method” | 2026-11-13 |
| A20 | [Read for: Actual currentT1139 catalogue and purpose](https://www.canada.ca/en/revenue-agency/services/forms-publications/forms/t1139.html) | “first fiscal period ends in 2025” | 2026-11-13 |
| A21 | [Read for: RRSP calculation/claim/premium timing help](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/rrsps-related-plans/contributing-a-rrsp-prpp/contributions-affect-your-rrsp-prpp-deduction-limit.html) | “18% of your earned income” | 2026-11-13 |
| A22 | [Read for: ITA146(1) earned income/room;146(5),(5.1) deduction timing and exceptions](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-146.html) | “60 days after the end of the year” | 2026-11-13 |
| A23 | [Read for: Actual2025/2026 indexedBPA rows](https://www.canada.ca/en/revenue-agency/services/tax/individuals/frequently-asked-questions-individuals/adjustment-personal-income-tax-benefit-amounts.html) | “Basic personal amount (maximum)” | 2026-11-13 |
| A24 | [Read for: T2203 actual current catalogue/purpose](https://www.canada.ca/en/revenue-agency/services/forms-publications/forms/t2203.html) | “payable to multiple jurisdictions” | 2026-11-13 |
| A25 | [Read for: Quebec abatement andPE branches](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-44000-refundable-quebec-abatement.html) | “permanent establishment outside Quebec” | 2026-11-13 |
| A26 | [Read for: RevenuQuebec filing/payment deadline paragraphs](https://www.revenuquebec.ca/en/citizens/income-tax-return/filing-your-income-tax-return/deadline-for-filing-your-income-tax-return/) | “until June 15 to file” | 2026-11-13 |
| A27 | [Read for: RQline445 actual operating instructions](https://www.revenuquebec.ca/en/citizens/income-tax-return/completing-your-income-tax-return/line-by-line-help/400-to-447-income-tax-and-contributions/line-445/) | “Part C of Schedule U” | 2026-11-13 |
| A28 | [Read for: RQline439 actual operating instructions](https://www.revenuquebec.ca/en/citizens/income-tax-return/completing-your-income-tax-return/line-by-line-help/400-to-447-income-tax-and-contributions/line-439/) | “complete Schedule R” | 2026-11-13 |
| A29 | [Read for: Certifiedsoftware andactualservedfilingyears](https://www.canada.ca/en/services/taxes/income-tax/personal-income-tax/how-file/tax-software.html) | “software certified” | 2026-11-13 |
| A30 | [Read for: T183 actual currentform purpose](https://www.canada.ca/en/revenue-agency/services/forms-publications/forms/t183.html) | “allow their electronic filer” | 2026-11-13 |
| A31 | [Read for: ITA230(1),(4)–(8) records](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-230.html) | “electronically readable format” | 2026-11-13 |
| A32 | [Read for: ITR1100(2) A/A.1,class50 selectedformula read fromactualofficialcache](https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-1100.html) | “A(B) + A.1(B.1)” | 2026-11-13 |
| A33 | [Read for: ITR1104(3.1)–(3.6),(4),(4.01) selecteddefinitions actuallyread](https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-1104.html) | “reaccelerated investment incentive property” | 2026-11-13 |
| A34 | [Read for: ITA67.1(1)–(5) meals andexceptions;actualofficialcachedtextread](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-67.1.html) | “Exceptions” | 2026-11-13 |
| A35 | [Read for: ITA18(1)(a),(r),(12) actualofficialcachedtextread](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-18.html) | “principal place of business” | 2026-11-13 |
| A36 | [Read for: ETA148 actualthresholdandexclusions](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-148.html) | “Small suppliers” | 2026-11-13 |
| A37 | [Read for: Actual 2025 T1139, Parts 1, 2, 4, 5, 6 and related notes; PDF text read and page 4 rendered](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t1139/t1139-25e.pdf) | “Reconciliation of 2025 Business Income for Tax Purposes” | 2026-11-13 |


**Not yet confirmed:** final 2026 T1/Schedule 8/13/T1139/TP-1 layouts and certified filing availability; actual 2027 reminders/amounts and later recognized holidays; every provincial/QPP/QPIP/special-income calculation; live client records/assessments/account balances, signatures/mandates, filing or payment confirmations; actual generated/recalculated workbook. Obtain the applicable validated work before whole filing readiness. No unknown amount is treated as zero.

**Removed and why:** unsupported Q2/Q4-placeholder labels and from-memory fallbacks; invented mandatory CPA gate and assistant-specific `present_files`/output path; the foreign s290-170 analogy; wrong field/half-CPP/forced-revenue-equality/universal-AIIP/all-meals/pre-1995 claims are replaced by the sourced controls above. Supported topics, eleven components, three artifacts, ten sheets, five reconciliations, six position patterns, thirteen checks, six refusal IDs and thirteen capability limits are retained and corrected. No historical professional approval existed on this tier-2 assembly version; none is invented here.

### Change log

- **v0.2, 13 November 2026:** Detailed source audit and current-year assembly update; correct income/CPP/GST/payment/province/fiscal-year/RRSP integration, complete-income/completion controls, dated final-form bridge, actual method/accountant provenance, full package/artifact preservation and recomputing assembly cases. Source review is not professional approval.
- **v0.1, April 2026; metadata updated July 2026:** Original Canadian capstone draft for GST/HST, T2125, T1, contributions, instalments and province.
