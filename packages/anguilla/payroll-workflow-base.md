---
name: payroll-workflow-base
description: Shared 2026 payroll computation workflow base that defines the gross-to-net calculation, statutory deduction handling, payslip generation, and payroll reporting runbook for all jurisdictions. Uses official authority guidance for workflow controls, without importing that country's tax brackets, contribution rates, minimum wages or forms as worldwide rules. This skill MUST be loaded alongside a country-specific payroll skill that provides the withholding tables, contribution rates, and local payroll rules. This skill alone cannot certify country payroll; an explicitly incomplete data inventory and working calculation may be produced.
version: 1.1
category: foundation
jurisdiction: GLOBAL
last_updated: 2026-11-14
tax_year: 2026
type: cross-country-method
tier: 2
domain: payroll
---

# Payroll Workflow Base Skill v1.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

### What this file is, and what it is not

**This file contains workflow architecture only.** It defines how Claude should approach a payroll computation task: the order of operations, how to calculate gross-to-net pay, how to handle statutory deductions, how to produce payslips and payroll journals, what to check before delivering. It contains no tax brackets, no social security rates, no employer contribution percentages, no minimum wage figures, no overtime multipliers, no filing deadlines, no return form names.

**This file must always be loaded with a country-specific payroll skill** that provides the withholding tables, social security rates, employer contribution schedules, and local employment law parameters (e.g., `uk-payroll`, `au-payroll`, `de-payroll`). Without current country evidence, do not label a payslip, journal or filing calendar final. Preserve the employee inventory, proposed mappings and exact missing inputs as an incomplete workpaper rather than inventing local law. The official UK examples below demonstrate why the old global defaults are unsafe; they are not worldwide rules.

**This file is the contract.** When a country payroll skill says it conforms to v1.1 of this base, it means: it fills the country slots specified in Section 6, it produces outputs in the format specified in Section 3, its computations can be validated by the self-checks in Section 5, and it participates in the workflow in Section 1.

---

## The method, step by step

### Section 1: The workflow

You are helping a small business owner compute payroll for one or more employees. The output will be reviewed by a qualified accountant or payroll specialist before use. Your job is to do the mechanical computation work and produce a complete set of payslips, journal entries, and a payroll summary plus a reviewer brief that makes the human reviewer's job fast and accurate.

Execute these nine steps in order. Do not skip. Do not reorder. Resolve material employee/pay-period facts before final computation. Draft workpapers may be built during the calculation, but payment-ready output waits for the evidence and reconciliation checks.

### Step 1 , Confirm the companion skills are loaded

This workflow base requires a country-specific payroll skill providing withholding tables, social security rates, employer contribution schedules, minimum wage, overtime rules, and filing deadlines.

Identify the jurisdiction and actual work locations from the full records before asking. Establish employment/payroll jurisdiction, tax residence, social coverage and any different local/state obligations, current pay date/tax year and effective rule version. Load the relevant country method and official tables, preserving name/version/date and actual approval label. Missing country evidence holds the affected final result, not the complete inventory; a named author's method does not approve this new payroll run.

If a bookkeeping workflow skill is also loaded, note its presence , the payroll journal entries produced at Step 8 must conform to the bookkeeping skill's chart of accounts and posting conventions.

### Step 2 , Read the employee data

The user will provide employment contracts, salary details, timesheets, benefit elections, or a combination. Read every document provided. Do not skim. For each employee, identify: full name and ID, employment start/end dates, employment type (full-time, part-time, casual, contractor , flag contractors separately), contract type, base salary or hourly rate and basis, pay frequency, agreed working hours, overtime eligibility, bonus/commission components, benefits-in-kind, pension elections, tax code or withholding status, bank details only in the authorised secure payment record (note completeness in this workpaper; do not expose full details in the reviewer brief or public output), salary sacrifice arrangements, and garnishment or court-ordered deduction instructions.

If any employee record is incomplete to the point where gross pay cannot be determined, queue for Step 4 clarification. If no employee data is provided at all, stop and tell the user what is needed.

### Step 3 , Determine the pay period and frequency

From the employee data and user instructions, establish:

- The specific pay period being computed (start date to end date)
- The pay frequency for each employee (may differ across employees)
- Whether this is a regular payroll run, a supplementary run (bonus, back-pay), or a termination run
- The actual contractual and legal payment date, value/receipt date and bank cut-off separately; the country rule determines tax/reporting recognition, not a universal date funds leave the bank
- Any mid-period changes (salary increase effective partway through the period, new starter, leaver)

Reconcile contract, timesheets, prior payroll and instructed dates first. Ask only for genuinely missing period/payment facts; do not infer a different country tax year or use an old table simply because it was loaded first.

### Step 4 , Confirm employee details and resolve ambiguities

For each employee, produce a one-line summary:

> "[Name] , [employment type], [base pay] [frequency], [overtime status], [benefits if any], [tax code/status if provided]"

Present all summaries to the user:

> "Here are the employees I will compute payroll for this period:
>
> [Numbered list of one-line summaries]
>
> Is this correct? If anything is wrong, tell me and I will adjust before I start computing. If it is correct, reply 'confirmed' and I will proceed."

Record actual confirmations/corrections without treating silence as approval. Resolve only the specific missing items after reading the full available records. Material uncertainty holds that employee's final calculation while evidenced employees/workpapers can proceed; do not repeatedly request confirmation already given in this engagement.

### Step 5 , Gross pay computation

For every employee, compute total gross pay for the period. Track cash contractual earnings, taxable pay, each contribution/pension base, non-cash benefits and reimbursements separately. They need not be equal; gross-to-net must not pay a non-cash benefit again as cash:

**Base pay.** Apply the actual contractual and lawful pay-period/proration method, paid hours and applicable award/collective rules. Divide an annual salary by the actual pay-period basis only where that method applies; handle extra paydays and starters/leavers explicitly. For hourly staff reconcile authorised actual payable hours. A part-time salary may already be prorated: do not reduce it again using an FTE fraction. Preserve contractual and statutory entitlement even when different.

**Overtime.** Apply the country skill's overtime rules. Determine which hours qualify as overtime (beyond the standard working week/day). Apply the correct multiplier per the country skill's rates. If the employee is exempt under the country skill's exemption rules, record zero overtime and note the basis.

**Bonuses and commissions.** Include any bonus or commission payable in this period. Determine the tax treatment per the country skill's rules (flat supplemental rate vs. aggregation with regular pay).

**Benefits-in-kind.** Apply actual country valuation, payroll/reporting eligibility, period allocation, employee payments and contribution treatment. Add the taxable non-cash value to the relevant tax base only where required; keep it out of cash payable, or show an equal explicitly labelled non-cash offset if the payslip format combines it. Prevent duplicate taxation through tax code and payroll. Employer benefit cost and taxable cash equivalent are not necessarily equal. [HMRC payrolled-benefit mechanics](https://www.gov.uk/guidance/payrolling-tax-employees-benefits-and-expenses-through-your-payroll).

**Salary sacrifice.** Confirm contractual validity, effective date, actual cash entitlement, minimum-wage limits and country treatment of each tax/contribution base. A valid cash-pay reduction does not automatically remove the amount from every taxable/contribution base. Record pre/post-sacrifice cash and every statutory base separately; do not change a contract or withhold earned wages to make an uncertain arrangement work.

**Back-pay.** Compute arrears separately with earned and paid dates, affected periods and the actual country tax/reporting/correction rule; do not assume all prior-period pay is ordinary current-period pay. Preserve original results and correction references. Include statutory sick/family/leave pay, reimbursements, advances and termination components when applicable, each with its actual cash/tax/contribution treatment. Flag incomplete leave/statutory-pay evidence rather than silently zeroing it. [HMRC pay categories](https://www.gov.uk/running-payroll/payments).

**Gross pay must be computed completely before any deductions are calculated.** Do not net deductions against gross during computation.

### Step 6 , Statutory deductions (employee share)

For every employee, compute all mandatory deductions from gross pay, in the order specified by the country skill (order matters , some deductions are computed on gross, others on gross-after-prior-deductions):

**Income tax withholding.** Apply the country skill's withholding method:

- If the actual authorised method/code is cumulative, compute tax due to the correct pay period using the prescribed period-to-date allowances/bands, taxable pay and valid prior-pay/tax figures; subtract prior tax. Do not apply full-year bands/free pay to partial-year earnings. A supported refund can make current withholding negative. [HMRC cumulative codes](https://www.gov.uk/hmrc-internal-manuals/paye-manual/paye11090).
- If the actual method is non-cumulative/period-based, use the prescribed table/formula, code and period basis. Annualise/de-annualise only if that country method requires it; period tables, credits and special payments can have their own formulas.
- If flat-rate supplemental method (for bonuses): apply the flat rate specified by the country skill to the supplemental payment.
- Validate the current issued tax code/status, operation basis and effective date against the records. If missing, use an official starter/emergency rule only after its actual conditions are met; do not invent a higher code as a conservative substitute.
- Apply any tax-free allowance, personal allowance, or threshold per the country skill's tables.

**Social security / national insurance (employee share).** Apply each programme's actual base, category, earnings period, bands, cap and aggregation rules separately. A ceiling may apply to earnings, a contribution amount or one programme only; another band/charge may continue above it. Do not stop all social charges at a generic annual cap. UK ordinary employee pay-period calculations and director annual/reconciliation rules illustrate the distinction. [HMRC employee calculator inputs](https://www.gov.uk/guidance/work-out-an-employees-national-insurance-contributions), [director rules](https://www.gov.uk/employee-directors).

**Pension / retirement contributions (employee share).** Verify actual eligibility/age/earnings assessment, existing scheme, enrolment/postponement, elections, joining/opt-in/opt-out evidence and effective dates. Compute actual scheme/country base, cap and tax-relief mechanism; distinguish employee withholding from employer salary-sacrifice funding. No invented election is a substitute for the actual automatic-enrolment rule. [The Pensions Regulator assessment](https://www.thepensionsregulator.gov.uk/en/business-advisers/automatic-enrolment-guide-for-business-advisers/check-who-to-enrol-in-a-workplace-pension).

**Other statutory deductions.** Apply any additional mandatory deductions per the country skill (training levies, solidarity surcharges, local taxes, mandatory union dues).

**Court-ordered deductions.** Compute per the order's terms and the country skill's protected earnings rules.

Record every deduction as a separate line item with: the deduction type, rate, earnings base, and resulting amount.

### Step 7 , Employer contributions

Separately from employee deductions, compute all amounts the employer must pay on top of the employee's gross salary. These are NOT deducted from the employee's pay , they are additional costs borne by the employer:

**Social security (employer share).** Apply the country skill's employer contribution rate to the applicable earnings base. Apply each programme's actual period/bands/caps and any different employer base/category; no universal annual cessation rule. Separate any valid employer relief/credit and benefit-specific charge from employee deductions.

**Workers' compensation / accident insurance.** Apply the rate per the country skill, based on industry classification and payroll amount.

**Payroll tax, training levy, employer pension, and other obligations.** Apply each employer-side charge specified by the country skill (payroll taxes, training levies, mandatory employer pension contributions, any other statutory employer charges).

Record every employer contribution as a separate line item. These appear on the employer cost summary and in the payroll journal, but NOT on the employee's payslip as deductions from pay.

### Step 8 , Net pay computation and payslip generation

**Net cash pay.** Cash earnings plus separately payable non-taxable cash reimbursements, minus actual employee cash deductions, adjusted for authorised refunds/recoveries/advances, equals net cash payable. If displayed gross includes non-cash benefits, remove them in the bridge without duplicating the associated tax. Distinguish a signed refund from a positive deduction. Do not add employer contributions to employee deductions, and do not equate taxable gross with the bank payment base.

Verify the full cash-to-taxable-to-net bridge, with separately identified benefits, reimbursements, income-tax deductions/refunds, employee social/pension/other/court deductions and authorised non-statutory deductions. Reconcile sign conventions and currency-specific rounding. If it does not balance, hold the payment-ready output and resolve the error.

**Payslip.** Produce one payslip per employee in the format specified in Section 3. Every gross component listed, every deduction itemized, net pay prominent. Year-to-date totals included if the country skill requires them.

### Step 9 , Produce payroll summary, journal entries, and filing reminders

**Payroll summary.** Employer-facing summary: total gross pay, total of each deduction type, total net pay, total employer contributions, cash payroll cost plus employer contributions and actual other employee-benefit costs, separately showing accruals, reimbursements and any benefit expense already booked. Taxable benefit value is not automatically additional wage expense.

**Proposed payroll journal entries.** Debit the actual wage/employee-benefit expense or relevant accrual and employer contribution expenses, credit the actual deduction/contribution payables and net wages payable. Reconcile any non-cash benefit cost already booked, reimbursements, advances and recovery/refund signs; do not expense the taxable benefit equivalent again. Payment later debits the relevant payable and credits bank only when actually evidenced. Balance every currency/entity journal and use the approved chart of accounts. Deliver a proposed posting list/import file for human approval; availability of ledger credentials is not posting authority.

**Filing calendar.** List upcoming payroll filings per the country skill's deadlines: income tax remittance, social security remittance, pension remittance, periodic returns, annual reconciliation filings, and employee annual tax certificates , each with amount, due date, and filing body.

Run the self-checks in Section 5 against all outputs. If any check fails, fix and re-run. Present final payment-ready results only when required checks pass. A labelled incomplete workpaper must keep unresolved employees, amounts and deadlines visible, with a clear hold on affected payment/filing readiness.

---

## Section 2 , Classification tiers

Every payroll computation decision falls into one of three tiers.

### Tier 1 , Confident

The employee's contract, the country skill's rules, and the data provided all point to one and only one computation. The base salary is stated, the tax code is provided, the rates are in the country skill's tables. A competent payroll administrator would compute the same figures without hesitation.

**Action:** compute from the actual evidence and retain calculation inputs, source/table version, period, rounding and reconciliation. Avoid unnecessary narration, but do not hide evidence merely because the decision is straightforward.

### Tier 2 , Assumed

The data provides clues but not certainty for a payroll computation decision. A competent payroll administrator would make an assumption and note it.

**Action:** record bounded alternative scenarios and their cash/tax effect. Apply a provisional treatment only if an explicit current country rule permits it and its required facts are established. Higher tax, lower pay or assumed pension membership is not inherently lawful or conservative. Hold the affected final result until material uncertainty is resolved.

Resolution controls for every formerly proposed default:

- **Overtime eligibility unknown:** obtain actual worker classification, contract/award, hours and country eligibility. Show payable-hour/eligibility scenarios; do not invent an exemption or a universal overtime entitlement.
- **Benefit taxable value ambiguous:** apply the actual valuation/evidence or explicitly permitted estimation rule; do not choose an unsupported higher value. Identify the calculation/employee-payment fact still missing.
- **Tax code not provided:** establish the actual current starter/code rule and required facts. Do not promise automatic annual-return recovery or choose a code merely because it deducts more.
- **Pension opt-in/out unclear:** assess statutory enrolment duties and existing records, opt-in/out status and effective dates. Comply with an established automatic duty; do not fabricate a voluntary election or override a valid opt-out.
- **Salary sacrifice validity unclear:** separate actual contracted cash pay from disputed tax relief/base treatment, quantify alternatives and hold the disputed conclusion. Do not restore or reduce contractual cash pay without authority.
- **Working hours ambiguous for part-timer:** reconcile timesheets, contract and actual payable hours. Never choose fewer hours to reduce employer cost, or presume an underpayment can wait until the next run. Calculate supported undisputed amounts and flag the unresolved entitlement before payment.
- **Bonus tax treatment unclear:** apply the actual permitted supplemental/aggregation method and conditions; a higher result is not evidence of the correct method.

### Tier 3 , Needs Input

The computation cannot proceed without information only the user possesses. The data provides insufficient basis for even a conservative assumption.

**Action:** Queue for user question in Step 4. Do not guess. A user answering "don't know" does not authorise a fabricated statutory default or underpayment. Preserve the unresolved field and the actual rule/evidence needed.

Examples:
- Employee classified as "contractor" , is this person genuinely self-employed or should they be on payroll? (Misclassification risk is severe.)
- Hours worked not provided for an hourly employee , cannot compute gross pay.
- Multiple tax codes possible and the employee's personal circumstances are unknown.
- Termination pay requested but the reason for termination (resignation vs. redundancy vs. dismissal) determines the tax treatment.

---

## Section 3 , Output specification

Five outputs per payroll run. All five are mandatory. Never produce one without the others.

### Output 1 , Individual payslips

One payslip per employee. Format:

```
[Employer name]
Pay Period: [start date] to [end date]
Payment Date: [date]
Employee: [name]    Employee ID: [id]

EARNINGS                          This Period    Year to Date
  Base salary / wages             [amount]       [amount]
  Overtime                        [amount]       [amount]
  Bonus / commission              [amount]       [amount]
  [Other cash earnings]           [amount]       [amount]
  [Other components]              [amount]       [amount]
                                  ----------     ----------
  CASH EARNINGS                   [amount]       [amount]
  Non-cash taxable benefit        [amount]       [amount]
  TAXABLE PAY (separate base)     [amount]       [amount]

DEDUCTIONS
  Income tax                      [amount]       [amount]
  Social security (employee)      [amount]       [amount]
  Pension (employee)              [amount]       [amount]
  [Other statutory deductions]    [amount]       [amount]
  [Court-ordered deductions]      [amount]       [amount]
                                  ----------     ----------
  TOTAL DEDUCTIONS                [amount]       [amount]

Non-taxable cash reimbursements    [amount]       [amount]
[Other authorised cash adjustments][amount]       [amount]
NET CASH PAY                      [amount]       [amount]

Employer contributions (for information):
  Social security (employer)      [amount]
  Pension (employer)              [amount]
  [Other employer contributions]  [amount]
  TOTAL EMPLOYER COST             [amount]
```

Retain year-to-date workpaper totals required for actual withholding/contribution/filing controls, with imported opening balances reconciled. Public payslip display follows the country law, not the computation method alone; include period hours where required. Protect identifiers and deliver payslips only through the authorised secure channel. [HMRC payslip content](https://www.gov.uk/running-payroll/payslips).

The country skill specifies any additional mandatory payslip fields (tax code display, national insurance number, pension scheme reference, etc.) and any legal formatting requirements.

### Output 2 , Payroll journal entries

Double-entry journal entries as specified in Step 9. Tabular format:

| Account | Debit | Credit |
|---|---|---|
| Salary expense / relevant accrual | [actual cash earnings cost, separate non-cash cost reconciliation] | |
| Employer social security expense | [amount] | |
| Employer pension expense | [amount] | |
| Income tax payable | | [amount] |
| Social security payable | | [employee + employer shares] |
| Pension payable | | [employee + employer shares] |
| Net wages payable | | [total net cash pay; bank only on evidenced settlement] |
| **TOTAL** | **[amount]** | **[amount]** |

Debits must equal credits. If a bookkeeping skill is loaded, use its nominal codes and account names.

### Output 3 , Employer cost summary

Per-employee and total cost breakdown:

| Employee | Gross Pay | Employer SS | Employer Pension | Other Employer | Total Cost |
|---|---|---|---|---|---|
| [Name] | [amount] | [amount] | [amount] | [amount] | [amount] |
| ... | | | | | |
| **TOTAL** | **[amount]** | **[amount]** | **[amount]** | **[amount]** | **[amount]** |

Reconcile cash earnings cost, employer contributions and actual other employee-benefit costs to the expense/accrual ledger. Separately identify non-cash expense already booked and reimbursements/advances. Gross taxable pay plus contributions alone is not a universally complete employer-cost measure; do not double-count a benefit or treat a refundable advance as wage expense.

### Output 4 , Filing calendar

The table is an empty output template. Populate each selected-country source, liability-bridge evidence and actual due date; the linked official payroll example supports keeping reporting and payment tasks distinct, not any country amount or deadline.

| Filing / Payment | Amount | Due Date | Authority / recipient | Evidence |
|---|---|---|---|---|
| Income tax remittance | [amount] | [date] | [tax authority name] | [Official payroll workflow example](https://www.gov.uk/guidance/what-payroll-information-to-report-to-hmrc); [populate actual country rule and run balance IDs] |
| Social security remittance | [amount] | [date] | [social security body] | [Official payroll workflow example](https://www.gov.uk/guidance/what-payroll-information-to-report-to-hmrc); [populate actual country rule and run balance IDs] |
| Pension remittance | [amount] | [date] | [pension provider] | [Official payroll workflow example](https://www.gov.uk/guidance/what-payroll-information-to-report-to-hmrc); [populate actual country rule and run balance IDs] |
| [Periodic return name] | N/A | [date] | [filing portal] | [Official payroll workflow example](https://www.gov.uk/guidance/what-payroll-information-to-report-to-hmrc); [populate actual country rule and run balance IDs] |
| [Annual reconciliation] | N/A | [date] | [filing portal] | [Official payroll workflow example](https://www.gov.uk/guidance/what-payroll-information-to-report-to-hmrc); [populate actual country rule and run balance IDs] |

The country skill provides the specific form names, filing bodies, portals, and deadline rules.

### Output 5 , Reviewer brief

```markdown
# [Country] Payroll , Reviewer Brief
**Period:** [pay period]
**Payment Date:** [date]
**Generated:** [date]
**Employees processed:** [count]

## Summary
- Total gross pay: [amount] [currency]
- Total employee deductions: [amount]
- Total net pay: [amount]
- Total employer contributions: [amount]
- Total payroll cost: [amount]
- Tier 1 (confident): [count of computation decisions]
- Tier 2 (assumed, flagged): [count]
- Tier 3 (user-answered): [count]

## High-priority items (review first)
[Numbered list: items with largest financial impact or highest
uncertainty. Each: one sentence what, one sentence why it matters,
one sentence what the reviewer should do.]

## Assumptions made (Tier 2 defaults)
[For each Tier 2 decision: employee name, the decision point,
the default applied, the alternative, and the cash impact of
the alternative.]

## Questions asked and user answers (Tier 3)
[For each Tier 3 item: the question, the user's answer or
"don't know, unresolved", the actual supported provisional rule if any, and the resulting hold/treatment.]

## Withholding verification
[For each employee: gross pay, tax withheld, effective rate,
and whether the effective rate falls within the expected range
for that employee's tax code/bracket.]

## Items the reviewer should verify
[Specific items: contracts to check, tax code confirmations to
obtain, benefit valuations to verify, overtime approvals to
confirm. Not generic "check everything."]
```

---

## Section 4 , Withholding computation rules

This section sets evidence/calculation controls, not a universal statutory withholding algorithm. The country skill provides the rates and thresholds; this section provides the computational framework.

### Progressive vs. flat rate

**Progressive (bracketed) withholding.** Establish the actual taxable base and method/code. Use the prescribed allowance/bands for the relevant period or period-to-date, avoiding both a full-year allowance on partial-year pay and a second allowance already embedded in a code/table. Respect credits, caps, special payments, starting balances and rounding in the country algorithm. Annualisation is a supported option only where prescribed; cumulative withholding can include a refund. [HMRC code operation](https://www.gov.uk/hmrc-internal-manuals/paye-manual/paye11090).

**Flat rate withholding.** Some jurisdictions or specific payment types (bonuses, supplemental pay) use a flat percentage. Apply the rate to the applicable earnings base as specified by the country skill.

### Tax-free allowance handling

The country skill specifies the annual tax-free amount and how it is distributed across pay periods: pro-rated evenly (divide by number of pay periods), cumulative (track year-to-date usage, self-correcting for mid-year starters), or claimed via tax code (allowance embedded in the code, applied as specified by the country skill).

### Multiple employment handling

Apply the country skill's rules for secondary employment (often a higher tax rate or no personal allowance). If the country skill is silent, flag as Tier 3 and ask the user. Never apply the full personal allowance to multiple employments simultaneously unless the country skill explicitly permits splitting.

### Year-to-date cumulative vs. period-based

**Cumulative:** apply actual authorised period-to-date rules and valid opening pay/tax. **Non-cumulative/period-based:** use the prescribed independent-period algorithm/code, which need not be an annualise/de-annualise formula. Available YTD data does not authorise switching methods. Preserve it for reconciliation even if the actual code excludes it from this calculation; code instructions and the effective country rule decide. [HMRC cumulative versus week/month-one basis](https://www.gov.uk/hmrc-internal-manuals/paye-manual/paye11090).

### Rounding rules

Apply the country skill's rounding rules for each component. If the applicable country rounding rule is missing, hold the final statutory calculation rather than inventing a two-decimal rule. Preserve precision, actual rounding order/direction, currency unit and reconciliation adjustments separately; tax components may truncate or use non-standard increments. Do not round intermediate numbers twice or silently adjust wages to force a balance.

---

## Section 5 , Self-checks (run before delivering output)

Run all twelve checks with pass/fail/unresolved/not-applicable and evidence. Correct failures before payment-ready output; incomplete workpapers retain the precise unresolved result and any deadline risk.

### Arithmetic integrity

**Check 1: Cash-to-net bridge balances.** For every employee reconcile cash earnings, non-cash additions/offsets, reimbursements, refunds and actual deductions to net cash pay at the prescribed precision. Any unexplained difference holds readiness; do not treat a taxable non-cash benefit as a bank payment or invent a universal currency tolerance.

**Check 2 , Employer contributions computed separately.** No employer contribution appears as a deduction on any employee's payslip. Employer contributions are additional costs, not deductions from pay. Scan every payslip's deductions section; none should contain employer-share items.

**Check 3: Withholding matches actual method/code.** Recompute from the supported current table/formula, period, taxable base, allowances/credits and prior pay/tax. Do not validate only by comparing an effective rate with marginal brackets: lawful cumulative refunds, code adjustments, separate bases and zero withholding can invalidate that heuristic. Investigate unusual results with the actual rule, not an automatic zero/refund rejection. [HMRC code operation](https://www.gov.uk/hmrc-internal-manuals/paye-manual/paye11090).

**Check 4: Each contribution follows its own base/period/bands/cap.** Distinguish earnings caps from contribution caps, continuing upper bands, employee/employer differences and actual annual aggregation versus ordinary pay-period or director reconciliation rules. A general stop-at-annual-cap test is invalid. [HMRC period inputs](https://www.gov.uk/guidance/work-out-an-employees-national-insurance-contributions), [director rules](https://www.gov.uk/employee-directors).

**Check 5 , Payroll journal entries balance.** Total debits in the payroll journal equal total credits. Not approximately , exactly.

**Check 6 , Total bank payment reconciles.** The sum of all employees' net pay equals the net wages payable credit in the payroll journal. Bridge each remittance from opening liability plus this run and other adjustments less evidenced prior payments/credits to the amount due. Do not equate one run's journal credit with a multi-period or adjusted cash remittance.

### Cross-output consistency

**Check 7 , Payslip totals match summary.** The sum of all individual payslips' gross pay equals the total gross pay on the employer cost summary. The sum of all net pays on payslips equals the total net pay on the summary.

**Check 8: Employer cost summary reconciles.** Add actual wage/benefit expense and employer contributions once, reconciling accrued or separately booked benefits and distinguishing taxable equivalent from economic cost. Summary totals match employee rows, source ledger and journal without double-counting.

**Check 9: Filing/payments follow actual scope and liability bridge.** Reconcile income-tax, each social programme and pension totals to this run plus opening balances, adjustments, reliefs, refunds and payments for the actual filing period. Keep preparation, submission, acceptance and cash payment as separate evidenced statuses, not inferred completion. [HMRC reporting duties](https://www.gov.uk/guidance/what-payroll-information-to-report-to-hmrc).

### Disclosure and completeness

**Check 10 , All employees accounted for.** Every employee confirmed in Step 4 has a payslip, appears in the journal entries, and appears in the employer cost summary. Count employees across all outputs; counts must match.

**Check 11 , Tier 2/3 disclosure complete.** Every computation decision marked as Tier 2 or Tier 3 has a corresponding entry in the reviewer brief. Count on both sides; they must match.

**Check 12 , Minimum wage compliance.** For every hourly employee and every salaried employee (converted to hourly equivalent), verify that the effective hourly rate meets or exceeds the country skill's minimum wage. Use the actual eligible work category, hours, pay-reference period, included/excluded pay and lawful deductions, not a generic contract salary divided by scheduled hours. Flag a shortfall as a compliance failure and hold a claim that the run is compliant; preserve the supported shortfall and correction task. Do not silently alter contract pay or presume underpayment may wait. [Pay components](https://www.gov.uk/national-minimum-wage/employers-and-the-minimum-wage), [working-hour categories](https://www.gov.uk/guidance/calculating-the-minimum-wage/working-hours-for-which-the-minimum-wage-must-be-paid).

### Failure handling

Correct and rerun failures. A repeated failure holds the affected final result with the exact missing evidence/calculation and deadline risk; do not silently work around it. Deliver only a clearly incomplete draft while a required check remains unresolved, preserving all employees and every affected item.

---

## Section 6 , Country skill contract

Every country-specific payroll skill loaded alongside this workflow base MUST provide the following. The country skill is incomplete without all mandatory slots.

### Mandatory slots

1. **Income tax withholding tables** , current tax brackets with rates, personal allowance or tax-free threshold, withholding method (cumulative or period-based), current tax year effective date.

2. **Social security rates and ceilings** , employee and employer contribution rates, earnings base, actual contribution period, bands and any earnings/contribution ceiling for each programme; explicitly state when a programme has no such cap. List each program separately (pension, health, unemployment, disability, accident).

3. **Minimum wage** , current national minimum wage (and age-based or regional variations), unit (hourly/monthly), effective date.

4. **Overtime rules** , standard working week (hours), overtime threshold, multipliers, daily overtime rules, exempt employee categories.

5. **Mandatory benefits and their tax treatment** , list of required/common benefits with taxable value computation methods.

6. **Filing deadlines and return forms** , form names, filing bodies, portals, frequency, and deadline rules for each payroll-related filing.
7. **Payslip legal requirements** , mandatory payslip fields for the jurisdiction.
8. **Pension/retirement scheme rules** , enrollment rules, minimum contribution rates (employee and employer), tax treatment of contributions.
9. **Pay frequency norms** , standard frequencies and legal constraints.
10. **Tax code system** , how codes work, default code for new employees, how to read a code to determine the allowance.
11. **Termination pay rules** , notice periods, severance requirements, accrued leave treatment, tax treatment of termination payments.
12. **Currency and rounding** , base currency, ISO code, rounding rules for tax, social security, and net pay.

### Optional slots

13. **Industry-specific variations** , different overtime rules, penalty rates, or allowances for specific industries.
14. **Salary sacrifice schemes** , rules governing pre-tax deductions, tax/SS implications, and caps.
15. **Integration notes** , how the payroll skill interacts with the country's bookkeeping, income tax, or social security skills.

---

## Worked cases

### Non-cash taxable benefit does not increase the bank payment

Assume cash earnings 3,000, a properly valued/payrolled non-cash benefit 500, actual calculated employee tax 500, employee social contribution 200 and employee pension 100. Taxable pay is 3,500 but net cash pay is 2,200, not 2,700. Employer contributions of 300 are an additional employer expense, not an employee deduction. If the benefit's actual economic cost is 450 already booked elsewhere, total employee cost is 3,750, not taxable pay plus contributions. The rates, valuation and eligibility are case assumptions requiring the actual country calculation; no illustrative amount is a statutory threshold. [HMRC taxable-benefit base mechanics](https://www.gov.uk/guidance/payrolling-tax-employees-benefits-and-expenses-through-your-payroll).

```oa-check
name: Separate taxable noncash value from cash wages and actual employer cost
inputs:
  cash_earnings: 3000
  noncash_taxable_benefit: 500
  calculated_income_tax: 500
  employee_social: 200
  employee_pension: 100
  employer_contributions: 300
  benefit_cost_already_booked: 450
steps:
  - taxable_pay: cash_earnings + noncash_taxable_benefit
  - employee_deductions: calculated_income_tax + employee_social + employee_pension
  - net_cash_pay: cash_earnings - employee_deductions
  - payroll_expense_before_separate_benefit: cash_earnings + employer_contributions
  - total_employee_economic_cost: payroll_expense_before_separate_benefit + benefit_cost_already_booked
  - journal_credits: net_cash_pay + calculated_income_tax + employee_social + employee_pension + employer_contributions
expected:
  taxable_pay: 3500
  employee_deductions: 800
  net_cash_pay: 2200
  payroll_expense_before_separate_benefit: 3300
  total_employee_economic_cost: 3750
  journal_credits: 3300
```

### Supported cumulative refund is not an invalid negative tax rate

Assume the actual issued cumulative code and prescribed period-to-date tables give tax due to date of 1,800, with valid prior tax withheld 2,000. Current withholding is negative 200, a refund. With current cash earnings 1,000 and no other deductions/adjustments in this simplified case, net cash is 1,200. Do not clamp the refund to zero or change a non-cumulative code merely because YTD figures exist. The tax-to-date result is an assumed country calculation, not computed here from a made-up annual bracket. [HMRC cumulative versus non-cumulative operation and refunds](https://www.gov.uk/hmrc-internal-manuals/paye-manual/paye11090).

```oa-check
name: Actual cumulative liability can require a current tax refund
inputs:
  supported_tax_due_to_date: 1800
  valid_prior_tax_withheld: 2000
  current_cash_earnings: 1000
steps:
  - current_tax_deduction: supported_tax_due_to_date - valid_prior_tax_withheld
  - current_net_cash: current_cash_earnings - current_tax_deduction
  - tax_after_current_adjustment: valid_prior_tax_withheld + current_tax_deduction
expected:
  current_tax_deduction: -200
  current_net_cash: 1200
  tax_after_current_adjustment: 1800
```

## When to refuse or refer

Do not certify a final payslip, payment-ready schedule or filed/posted status when material pay entitlement, actual hours, country tables, code/method, required YTD balances, contribution base or rounding is unresolved. Do not choose fewer hours, assume a pension election, invent higher taxable values or force a positive tax deduction. Continue supported calculations as incomplete workpapers, with affected employees and deadline/correction tasks visible. Contractor classification, termination, expatriate/social-coverage, equity awards and complex leave/corrections need their actual country specialist; a contractor label alone does not establish exclusion from employee obligations. Human approval of a proposed posting/import does not prove payment or filing occurred.

## Section 7 , Reference material

### Validation status

This file is v1.1 of `payroll-workflow-base`, updated for the shared 2026 workflow with actual bounded authority reads and recomputing examples. No country rate or live payroll submission is certified by this base. It follows the structural pattern established by `bookkeeping-workflow-base` v1.0.

### Design decisions

1. **Three-tier model consistent with bookkeeping.** The same two meaningfully different "don't know" cases exist: "I can make a conservative assumption" (Tier 2) and "I genuinely cannot compute without user input" (Tier 3).

2. **Employer contributions as separate step.** Step 7 exists separately from Step 6 because employer contributions are not deducted from pay, have different rates/ceilings, and appear in different outputs. Mixing them causes the most common payroll error: treating an employer contribution as an employee deduction.

3. **Year-to-date evidence does not choose the method.** Support cumulative and period-based calculations only as the actual country rule/code directs, retaining YTD records for reconciliation rather than overriding an issued non-cumulative instruction.

4. **Minimum wage is a compliance check.** Compute supported contractual/statutory comparisons and shortfalls, but do not label a known shortfall compliant or assume it is merely a discretionary reviewer preference. Hold the affected readiness claim and record the correction needed.

### Known gaps

1. Multi-currency payroll (expatriate employees) is not covered.
2. Stock options and equity compensation are not addressed.
3. Leave management (annual leave accrual, sick leave) is referenced but not fully specified.
4. Payroll correction runs are not covered beyond the back-pay mechanism in Step 5.
5. Contractor/freelancer payments are deliberately excluded , this is an employee payroll workflow.

### Change log

- **v1.1 (14 November 2026):** Corrects cash/non-cash pay, unsupported lower-hours/higher-tax defaults, code-driven cumulative calculations, contribution periods/caps and reconciliation while retaining nine steps, five outputs, twelve checks and fifteen country slots.

- **v1.0 (May 2026):** Initial release. Establishes the universal payroll workflow, three-tier classification system, five-output specification, 12 self-checks, and country skill contract.

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

## Sources

| Source and what was actually read | Official URL | Read on |
|---|---|---|
| HMRC payroll overview. Read for record, deduction, employer-cost, payslip and reporting workflow plus distinct filing/payment steps; no displayed numerical employer threshold is adopted | https://www.gov.uk/running-payroll/overview | 2026-11-14 |
| HMRC employees pay. Read for ordinary wages, statutory sick/family/leave categories, tips, benefits and special non-cash payment distinctions; no current rate/threshold adopted | https://www.gov.uk/running-payroll/payments | 2026-11-14 |
| HMRC payslips. Read for full operative timing/content/hours and secure delivery options | https://www.gov.uk/running-payroll/payslips | 2026-11-14 |
| HMRC PAYE11090. Read for opening code instructions, suffix/prefix cases, cumulative allowance/band periods, refunds, non-cumulative basis and initial prefix-code discussion; not all later JSA material | https://www.gov.uk/hmrc-internal-manuals/paye-manual/paye11090 | 2026-11-14 |
| HMRC voluntary payrolling benefits. Read for employee tax-code coordination, separate contribution duty, regular/irregular benefit allocation and taxable-pay examples, plus actual versus taxable-value distinction; not the entire later underpayment/cessation procedure | https://www.gov.uk/guidance/payrolling-tax-employees-benefits-and-expenses-through-your-payroll | 2026-11-14 |
| HMRC contribution calculator guidance. Read for current-year limitation and period/pay-date/earnings/category inputs; the calculator was not run and no statutory rate is supplied here | https://www.gov.uk/guidance/work-out-an-employees-national-insurance-contributions | 2026-11-14 |
| HMRC directors. Read for annual and alternative calculations, reconciliation, category changes and ceasing to be a director; not a universal employee annual cap | https://www.gov.uk/employee-directors | 2026-11-14 |
| HMRC minimum wage employers. Read for pay inclusions/exclusions, underpayment/record duties and need for pay/hours records; no numerical wage rate adopted | https://www.gov.uk/national-minimum-wage/employers-and-the-minimum-wage | 2026-11-14 |
| HMRC minimum-wage hours. Read for opening equivalent-hourly-rate and work-category distinctions, including mixed work types; not every specialist on-call/travel/salaried example | https://www.gov.uk/guidance/calculating-the-minimum-wage/working-hours-for-which-the-minimum-wage-must-be-paid | 2026-11-14 |
| The Pensions Regulator. Read for assessment categories, automatic duty versus join/opt-in/opt-out, director and bonus assessment distinctions; no age/earnings/contribution figure adopted | https://www.thepensionsregulator.gov.uk/en/business-advisers/automatic-enrolment-guide-for-business-advisers/check-who-to-enrol-in-a-workplace-pension | 2026-11-14 |
| HMRC payroll reporting. Read for opening FPS/EPS, nil-pay and employer-reference/related-year field distinctions; not all later return fields | https://www.gov.uk/guidance/what-payroll-information-to-report-to-hmrc | 2026-11-14 |

Not yet confirmed: every country's operative 2026 withholding tables/formula and issued-code basis; precise earnings/benefit/expense, social coverage, programme period/category/cap, pension enrolment/base/relief, minimum-wage pay/hours/award, overtime and statutory sick/family/leave entitlement; actual salary-sacrifice/benefit valuation, rounding and currency rules; cross-border/expatriate, equity compensation, leave accrual and correction-run treatment; actual current forms, remittance balances, filing/payment deadlines and acceptance evidence. No UK figure displayed on a cited page is imported as a worldwide rate or certified country computation; use each country's current law and dated primary tables.
