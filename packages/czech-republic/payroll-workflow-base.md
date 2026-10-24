---
name: payroll-workflow-base
description: Universal payroll computation workflow base that defines the gross-to-net calculation, statutory deduction handling, payslip generation, and payroll reporting runbook for all jurisdictions. Contains no jurisdiction-specific content — no tax brackets, no social security rates, no minimum wages, no filing forms. This skill MUST be loaded alongside a country-specific payroll skill that provides the withholding tables, contribution rates, and local payroll rules. This skill alone cannot produce any output.
version: 1.0
category: foundation
jurisdiction: GLOBAL
tier: 2
last_updated: 2026-06-12
---

# Payroll Workflow Base Skill v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## What this file is, and what it is not

**This file contains workflow architecture only.** It defines how Claude should approach a payroll computation task: the order of operations, how to calculate gross-to-net pay, how to handle statutory deductions, how to produce payslips and payroll journals, what to check before delivering. It contains no tax brackets, no social security rates, no employer contribution percentages, no minimum wage figures, no overtime multipliers, no filing deadlines, no return form names.

**This file must always be loaded with a country-specific payroll skill** that provides the withholding tables, social security rates, employer contribution schedules, and local employment law parameters (e.g., `uk-payroll`, `au-payroll`, `de-payroll`). This file alone cannot produce a payslip, a payroll journal, or a filing calendar. Loading it without a companion is a configuration error and Claude must refuse to proceed.

**This file is the contract.** When a country payroll skill says it conforms to v1.0 of this base, it means: it fills the country slots specified in Section 6, it produces outputs in the format specified in Section 3, its computations can be validated by the self-checks in Section 5, and it participates in the workflow in Section 1.

---

## Section 1 — The workflow (read this first, follow exactly)

You are helping a small business owner compute payroll for one or more employees. The output will be reviewed by a qualified accountant or payroll specialist before use. Your job is to do the mechanical computation work and produce a complete set of payslips, journal entries, and a payroll summary plus a reviewer brief that makes the human reviewer's job fast and accurate.

Execute these nine steps in order. Do not skip. Do not reorder. Do not begin gross pay computation before step 4. Do not build any output files before step 7.

### Step 1 — Confirm the companion skills are loaded

This workflow base requires a country-specific payroll skill providing withholding tables, social security rates, employer contribution schedules, minimum wage, overtime rules, and filing deadlines.

If no country-specific skill is loaded, stop and tell the user: "I need a country-specific payroll skill loaded alongside this workflow base. Which jurisdiction is this payroll for?" Do not proceed without it.

If a bookkeeping workflow skill is also loaded, note its presence — the payroll journal entries produced at Step 8 must conform to the bookkeeping skill's chart of accounts and posting conventions.

### Step 2 — Read the employee data

The user will provide employment contracts, salary details, timesheets, benefit elections, or a combination. Read every document provided. Do not skim. For each employee, identify: full name and ID, employment start/end dates, employment type (full-time, part-time, casual, contractor — flag contractors separately), contract type, base salary or hourly rate and basis, pay frequency, agreed working hours, overtime eligibility, bonus/commission components, benefits-in-kind, pension elections, tax code or withholding status, bank details (note presence, do not store), salary sacrifice arrangements, and garnishment or court-ordered deduction instructions.

If any employee record is incomplete to the point where gross pay cannot be determined, queue for Step 4 clarification. If no employee data is provided at all, stop and tell the user what is needed.

### Step 3 — Determine the pay period and frequency

From the employee data and user instructions, establish:

- The specific pay period being computed (start date to end date)
- The pay frequency for each employee (may differ across employees)
- Whether this is a regular payroll run, a supplementary run (bonus, back-pay), or a termination run
- The payment date (when funds leave the employer's bank account)
- Any mid-period changes (salary increase effective partway through the period, new starter, leaver)

If the pay period is ambiguous, ask the user: "Which pay period are you computing? Please confirm the start date, end date, and payment date."

### Step 4 — Confirm employee details and resolve ambiguities

For each employee, produce a one-line summary:

> "[Name] — [employment type], [base pay] [frequency], [overtime status], [benefits if any], [tax code/status if provided]"

Present all summaries to the user:

> "Here are the employees I will compute payroll for this period:
>
> [Numbered list of one-line summaries]
>
> Is this correct? If anything is wrong, tell me and I will adjust before I start computing. If it is correct, reply 'confirmed' and I will proceed."

Wait for confirmation. If the user corrects anything, update and re-confirm. For any employee where data was insufficient at Step 2, ask the specific missing items now.

### Step 5 — Gross pay computation

For every employee, compute total gross pay for the period. Gross pay is the sum of all components before any deductions:

**Base pay.** For salaried employees, divide annual salary by the number of pay periods per year (or use the monthly/weekly rate as stated). For hourly employees, multiply hourly rate by hours worked. For part-time employees, pro-rate according to contracted hours vs. full-time equivalent.

**Overtime.** Apply the country skill's overtime rules. Determine which hours qualify as overtime (beyond the standard working week/day). Apply the correct multiplier per the country skill's rates. If the employee is exempt under the country skill's exemption rules, record zero overtime and note the basis.

**Bonuses and commissions.** Include any bonus or commission payable in this period. Determine the tax treatment per the country skill's rules (flat supplemental rate vs. aggregation with regular pay).

**Benefits-in-kind.** Compute the taxable value per the country skill's benefit valuation rules. Add to gross pay for withholding purposes. The benefit value is included in gross for tax computation but not in cash pay — it appears on the payslip as a non-cash component.

**Salary sacrifice.** If applicable, reduce gross pay by the sacrifice amount before computing deductions, per the country skill's rules. Record pre-sacrifice and post-sacrifice gross separately.

**Back-pay.** If this period includes back-pay (e.g., a backdated salary increase), compute arrears separately and include in this period's gross. Flag for the reviewer.

**Gross pay must be computed completely before any deductions are calculated.** Do not net deductions against gross during computation.

### Step 6 — Statutory deductions (employee share)

For every employee, compute all mandatory deductions from gross pay, in the order specified by the country skill (order matters — some deductions are computed on gross, others on gross-after-prior-deductions):

**Income tax withholding.** Apply the country skill's withholding method:

- If cumulative/year-to-date method: compute total tax liability for the year to date based on cumulative gross, subtract tax already withheld in prior periods, the remainder is this period's withholding.
- If period-based method: annualize the period gross, apply the annual tax table, de-annualize the result to get the period withholding.
- If flat-rate supplemental method (for bonuses): apply the flat rate specified by the country skill to the supplemental payment.
- Apply the employee's tax code or status as provided. If no tax code is available, apply the country skill's default code for a new employee.
- Apply any tax-free allowance, personal allowance, or threshold per the country skill's tables.

**Social security / national insurance (employee share).** Apply the country skill's employee contribution rate to the applicable earnings base. Observe the annual ceiling — if year-to-date earnings exceed it, no further contributions are due. If multiple programs exist (pension, health, unemployment, disability), compute each separately.

**Pension / retirement contributions (employee share).** Compute per the country skill's rates. Include voluntary additional contributions if elected. Apply earnings caps. Determine pre-tax vs. post-tax treatment per the country skill.

**Other statutory deductions.** Apply any additional mandatory deductions per the country skill (training levies, solidarity surcharges, local taxes, mandatory union dues).

**Court-ordered deductions.** Compute per the order's terms and the country skill's protected earnings rules.

Record every deduction as a separate line item with: the deduction type, rate, earnings base, and resulting amount.

### Step 7 — Employer contributions

Separately from employee deductions, compute all amounts the employer must pay on top of the employee's gross salary. These are NOT deducted from the employee's pay — they are additional costs borne by the employer:

**Social security (employer share).** Apply the country skill's employer contribution rate to the applicable earnings base. Observe the annual ceiling (which may differ from the employee ceiling). Compute each program separately.

**Workers' compensation / accident insurance.** Apply the rate per the country skill, based on industry classification and payroll amount.

**Payroll tax, training levy, employer pension, and other obligations.** Apply each employer-side charge specified by the country skill (payroll taxes, training levies, mandatory employer pension contributions, any other statutory employer charges).

Record every employer contribution as a separate line item. These appear on the employer cost summary and in the payroll journal, but NOT on the employee's payslip as deductions from pay.

### Step 8 — Net pay computation and payslip generation

**Net pay.** For every employee: Net pay = Gross pay − Total employee deductions (from Step 6). This is the amount to be paid to the employee's bank account.

Verify: Gross pay − (income tax + social security employee + pension employee + other statutory + court-ordered) = Net pay. If the arithmetic does not balance, stop and find the error.

**Payslip.** Produce one payslip per employee in the format specified in Section 3. Every gross component listed, every deduction itemized, net pay prominent. Year-to-date totals included if the country skill requires them.

### Step 9 — Produce payroll summary, journal entries, and filing reminders

**Payroll summary.** Employer-facing summary: total gross pay, total of each deduction type, total net pay, total employer contributions, total cost (gross + employer contributions).

**Payroll journal entries.** Double-entry: debit salary/wage expense (gross), debit employer social security/pension/other contribution expenses; credit income tax payable, social security payable (employee + employer shares), pension payable (employee + employer shares), other deductions payable, net wages payable/bank. Total debits must equal total credits. If a bookkeeping skill is loaded, use its nominal codes.

**Filing calendar.** List upcoming payroll filings per the country skill's deadlines: income tax remittance, social security remittance, pension remittance, periodic returns, annual reconciliation filings, and employee annual tax certificates — each with amount, due date, and filing body.

Run the self-checks in Section 5 against all outputs. If any check fails, fix and re-run. Only present outputs to the user when all checks pass.

---

## Section 2 — Classification tiers

Every payroll computation decision falls into one of three tiers.

### Tier 1 — Confident

The employee's contract, the country skill's rules, and the data provided all point to one and only one computation. The base salary is stated, the tax code is provided, the rates are in the country skill's tables. A competent payroll administrator would compute the same figures without hesitation.

**Action:** Compute silently. Do not narrate. Do not flag.

### Tier 2 — Assumed

The data provides clues but not certainty for a payroll computation decision. A competent payroll administrator would make an assumption and note it.

**Action:** Apply the conservative default (below), flag in the reviewer brief with the alternative treatment and cash impact, and record the assumption.

Conservative defaults for payroll:

- **Overtime eligibility unknown:** Treat as non-exempt (eligible for overtime). Excluding overtime pay for an eligible employee is an underpayment risk.
- **Benefit taxable value ambiguous:** Use the higher taxable value. Undertaxing a benefit creates a liability for the employer.
- **Tax code not provided:** Apply the country skill's default emergency/standard code for a new employee. This typically results in higher withholding, which the employee recovers via their annual return.
- **Pension opt-in/out unclear:** Assume opted in at the statutory minimum rate. Failing to enroll creates a compliance risk.
- **Salary sacrifice validity unclear:** Do not apply the sacrifice (compute on full gross). Applying an invalid sacrifice creates a tax liability.
- **Working hours ambiguous for part-timer:** Use the lower hour figure (less pay, less employer cost). Overpaying requires recovery; underpaying is correctable in the next run.
- **Bonus tax treatment unclear:** Aggregate with regular pay rather than applying a supplemental flat rate. Aggregation typically produces higher withholding.

### Tier 3 — Needs Input

The computation cannot proceed without information only the user possesses. The data provides insufficient basis for even a conservative assumption.

**Action:** Queue for user question in Step 4. Do not guess. Do not apply a default until the user has been asked and either answered or selected "don't know."

Examples:
- Employee classified as "contractor" — is this person genuinely self-employed or should they be on payroll? (Misclassification risk is severe.)
- Hours worked not provided for an hourly employee — cannot compute gross pay.
- Multiple tax codes possible and the employee's personal circumstances are unknown.
- Termination pay requested but the reason for termination (resignation vs. redundancy vs. dismissal) determines the tax treatment.

---

## Section 3 — Output specification

Five outputs per payroll run. All five are mandatory. Never produce one without the others.

### Output 1 — Individual payslips

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
  Benefits-in-kind (taxable)      [amount]       [amount]
  [Other components]              [amount]       [amount]
                                  ----------     ----------
  GROSS PAY                       [amount]       [amount]

DEDUCTIONS
  Income tax                      [amount]       [amount]
  Social security (employee)      [amount]       [amount]
  Pension (employee)              [amount]       [amount]
  [Other statutory deductions]    [amount]       [amount]
  [Court-ordered deductions]      [amount]       [amount]
                                  ----------     ----------
  TOTAL DEDUCTIONS                [amount]       [amount]

NET PAY                           [amount]       [amount]

Employer contributions (for information):
  Social security (employer)      [amount]
  Pension (employer)              [amount]
  [Other employer contributions]  [amount]
  TOTAL EMPLOYER COST             [amount]
```

Year-to-date columns are mandatory if the country skill's withholding method is cumulative. If period-based, year-to-date columns are recommended but optional per the country skill's payslip requirements.

The country skill specifies any additional mandatory payslip fields (tax code display, national insurance number, pension scheme reference, etc.) and any legal formatting requirements.

### Output 2 — Payroll journal entries

Double-entry journal entries as specified in Step 9. Tabular format:

| Account | Debit | Credit |
|---|---|---|
| Salary expense | [total gross] | |
| Employer social security expense | [amount] | |
| Employer pension expense | [amount] | |
| Income tax payable | | [amount] |
| Social security payable | | [employee + employer shares] |
| Pension payable | | [employee + employer shares] |
| Net wages payable / bank | | [total net pay] |
| **TOTAL** | **[amount]** | **[amount]** |

Debits must equal credits. If a bookkeeping skill is loaded, use its nominal codes and account names.

### Output 3 — Employer cost summary

Per-employee and total cost breakdown:

| Employee | Gross Pay | Employer SS | Employer Pension | Other Employer | Total Cost |
|---|---|---|---|---|---|
| [Name] | [amount] | [amount] | [amount] | [amount] | [amount] |
| ... | | | | | |
| **TOTAL** | **[amount]** | **[amount]** | **[amount]** | **[amount]** | **[amount]** |

Total cost = Gross pay + All employer contributions. This is the true cost of each employee to the business.

### Output 4 — Filing calendar

| Filing / Payment | Amount | Due Date | Sinker |
|---|---|---|---|
| Income tax remittance | [amount] | [date] | [tax authority name] |
| Social security remittance | [amount] | [date] | [social security body] |
| Pension remittance | [amount] | [date] | [pension provider] |
| [Periodic return name] | N/A | [date] | [filing portal] |
| [Annual reconciliation] | N/A | [date] | [filing portal] |

The country skill provides the specific form names, filing bodies, portals, and deadline rules.

### Output 5 — Reviewer brief

```markdown
# [Country] Payroll — Reviewer Brief
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
"don't know — default applied", and the resulting treatment.]

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

## Section 4 — Withholding computation rules

This section defines the universal mechanics of income tax withholding. The country skill provides the rates and thresholds; this section provides the computational framework.

### Progressive vs. flat rate

**Progressive (bracketed) withholding.** Determine taxable pay for the period (gross minus pre-tax deductions per the country skill's ordering). If cumulative method: use year-to-date taxable pay, apply annual brackets, subtract year-to-date tax already withheld. If period-based method: annualize the period taxable pay, apply annual brackets, de-annualize. Apply the tax-free allowance before the first bracket. Compute tax at each bracket rate on the portion falling within that bracket. Sum to get total withholding.

**Flat rate withholding.** Some jurisdictions or specific payment types (bonuses, supplemental pay) use a flat percentage. Apply the rate to the applicable earnings base as specified by the country skill.

### Tax-free allowance handling

The country skill specifies the annual tax-free amount and how it is distributed across pay periods: pro-rated evenly (divide by number of pay periods), cumulative (track year-to-date usage, self-correcting for mid-year starters), or claimed via tax code (allowance embedded in the code, applied as specified by the country skill).

### Multiple employment handling

Apply the country skill's rules for secondary employment (often a higher tax rate or no personal allowance). If the country skill is silent, flag as Tier 3 and ask the user. Never apply the full personal allowance to multiple employments simultaneously unless the country skill explicitly permits splitting.

### Year-to-date cumulative vs. period-based

**Cumulative:** Each period considers all prior periods in the tax year, self-correcting over time. Requires year-to-date gross and tax withheld as inputs. **Period-based:** Each period computed independently by annualizing/de-annualizing. Simpler but does not self-correct. The country skill specifies which method is standard. If the user provides year-to-date figures, use the cumulative method regardless of the country default.

### Rounding rules

Apply the country skill's rounding rules for each component. If the country skill is silent, round each deduction to two decimal places and compute net pay as the exact difference (gross minus the sum of rounded deductions). Net pay rounds to the currency's smallest denomination.

---

## Section 5 — Self-checks (run before delivering output)

Run these twelve checks against all outputs. If any fails, fix and re-run. Do not deliver until all pass.

### Arithmetic integrity

**Check 1 — Gross minus deductions equals net.** For every employee: Gross pay − Total deductions = Net pay. Not approximately — exactly. A difference of even 0.01 means a computation error.

**Check 2 — Employer contributions computed separately.** No employer contribution appears as a deduction on any employee's payslip. Employer contributions are additional costs, not deductions from pay. Scan every payslip's deductions section; none should contain employer-share items.

**Check 3 — Tax withholding within valid brackets.** For every employee, the effective tax rate (tax withheld ÷ gross pay) falls within the range of the lowest and highest marginal rates in the country skill's tax table. An effective rate of 0% is valid only if gross pay is below the tax-free threshold. An effective rate above the highest marginal rate is always wrong.

**Check 4 — Social security respects annual ceiling.** For every employee, verify that year-to-date social security contributions (employee share) do not exceed the annual ceiling specified by the country skill. If contributions in this period would push the total above the ceiling, the contribution for this period must be reduced to the ceiling remainder.

**Check 5 — Payroll journal entries balance.** Total debits in the payroll journal equal total credits. Not approximately — exactly.

**Check 6 — Total bank payment reconciles.** The sum of all employees' net pay equals the net wages payable credit in the payroll journal. The sum of all tax and social security remittance amounts in the filing calendar equals the corresponding payable credits in the journal (tax payable + SS payable + pension payable).

### Cross-output consistency

**Check 7 — Payslip totals match summary.** The sum of all individual payslips' gross pay equals the total gross pay on the employer cost summary. The sum of all net pays on payslips equals the total net pay on the summary.

**Check 8 — Employer cost summary adds up.** For every employee: Gross pay + Employer SS + Employer pension + Other employer contributions = Total cost. The total row is the sum of all employee rows.

**Check 9 — Filing calendar amounts reconcile.** The income tax remittance amount equals the sum of all employees' income tax withholding. The social security remittance equals the sum of all employees' SS (employee share + employer share). The pension remittance equals the sum of all employees' pension (employee share + employer share).

### Disclosure and completeness

**Check 10 — All employees accounted for.** Every employee confirmed in Step 4 has a payslip, appears in the journal entries, and appears in the employer cost summary. Count employees across all outputs; counts must match.

**Check 11 — Tier 2/3 disclosure complete.** Every computation decision marked as Tier 2 or Tier 3 has a corresponding entry in the reviewer brief. Count on both sides; they must match.

**Check 12 — Minimum wage compliance.** For every hourly employee and every salaried employee (converted to hourly equivalent), verify that the effective hourly rate meets or exceeds the country skill's minimum wage. If it does not, flag in the reviewer brief as a high-priority item — do not silently adjust the pay, as the employment contract may need to be reviewed.

### Failure handling

If any check fails, fix the output and re-run all twelve. Do not deliver until all pass. If a check fails twice in a row on the same item, stop and report the failure to the user rather than silently working around it.

---

## Section 6 — Country skill contract

Every country-specific payroll skill loaded alongside this workflow base MUST provide the following. The country skill is incomplete without all mandatory slots.

### Mandatory slots

1. **Income tax withholding tables** — current tax brackets with rates, personal allowance or tax-free threshold, withholding method (cumulative or period-based), current tax year effective date.

2. **Social security rates and ceilings** — employee and employer contribution rates, earnings base, annual ceiling for each program. List each program separately (pension, health, unemployment, disability, accident).

3. **Minimum wage** — current national minimum wage (and age-based or regional variations), unit (hourly/monthly), effective date.

4. **Overtime rules** — standard working week (hours), overtime threshold, multipliers, daily overtime rules, exempt employee categories.

5. **Mandatory benefits and their tax treatment** — list of required/common benefits with taxable value computation methods.

6. **Filing deadlines and return forms** — form names, filing bodies, portals, frequency, and deadline rules for each payroll-related filing.
7. **Payslip legal requirements** — mandatory payslip fields for the jurisdiction.
8. **Pension/retirement scheme rules** — enrollment rules, minimum contribution rates (employee and employer), tax treatment of contributions.
9. **Pay frequency norms** — standard frequencies and legal constraints.
10. **Tax code system** — how codes work, default code for new employees, how to read a code to determine the allowance.
11. **Termination pay rules** — notice periods, severance requirements, accrued leave treatment, tax treatment of termination payments.
12. **Currency and rounding** — base currency, ISO code, rounding rules for tax, social security, and net pay.

### Optional slots

13. **Industry-specific variations** — different overtime rules, penalty rates, or allowances for specific industries.
14. **Salary sacrifice schemes** — rules governing pre-tax deductions, tax/SS implications, and caps.
15. **Integration notes** — how the payroll skill interacts with the country's bookkeeping, income tax, or social security skills.

---

## Section 7 — Reference material

### Validation status

This file is v1.0 of `payroll-workflow-base`, drafted as part of the Open Accountants skill architecture in May 2026. It follows the structural pattern established by `bookkeeping-workflow-base` v1.0.

### Design decisions

1. **Three-tier model consistent with bookkeeping.** The same two meaningfully different "don't know" cases exist: "I can make a conservative assumption" (Tier 2) and "I genuinely cannot compute without user input" (Tier 3).

2. **Employer contributions as separate step.** Step 7 exists separately from Step 6 because employer contributions are not deducted from pay, have different rates/ceilings, and appear in different outputs. Mixing them causes the most common payroll error: treating an employer contribution as an employee deduction.

3. **Year-to-date as optional input.** Both cumulative and period-based computation are supported. If the user provides year-to-date data, the cumulative method is used regardless of the country default.

4. **Minimum wage check as self-check, not blocker.** Check 12 flags non-compliance in the reviewer brief rather than refusing to compute — the reviewer decides whether it is a legal issue.

### Known gaps

1. Multi-currency payroll (expatriate employees) is not covered.
2. Stock options and equity compensation are not addressed.
3. Leave management (annual leave accrual, sick leave) is referenced but not fully specified.
4. Payroll correction runs are not covered beyond the back-pay mechanism in Step 5.
5. Contractor/freelancer payments are deliberately excluded — this is an employee payroll workflow.

### Change log

- **v1.0 (May 2026):** Initial release. Establishes the universal payroll workflow, three-tier classification system, five-output specification, 12 self-checks, and country skill contract.

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://www.openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
