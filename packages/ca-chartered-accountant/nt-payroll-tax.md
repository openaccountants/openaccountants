---
name: nt-payroll-tax
description: Use this skill for the Northwest Territories Payroll Tax — 2% employer-paid payroll tax (with refundable Cost of Living Tax Credit for residents). Unique to NWT. Triggers "NWT payroll tax", "Northwest Territories payroll tax", "NWT 2% payroll", "Cost of Living Offset NWT", "Form NWT401".
jurisdiction: CA
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# NT Payroll Tax

## Northwest Territories — Payroll Tax — Skill v1.0

## 1. Quick reference

- **Rate** — 2.0% of gross remuneration
- **Who pays** — Employer (statutory liability) — but employer is required to withhold from the employee's pay
- **Refundability for residents** — NWT residents reclaim it via the **Cost of Living Tax Credit** on their T1 (Form NT479)
- **Net effect for low-income NWT residents** — Approximately zero (fully offset by the credit)
- **Net effect for non-residents working in NWT (fly-in workers)** — 2% out-of-pocket — no credit available
- **Filing frequency** — Monthly remittances + annual reconciliation (Form NWT401)
- **Administered by** — NWT Department of Finance — *not* CRA

**Key characteristics — unique among Canadian jurisdictions**

| Feature | Value |
| --- | --- |
| Rate | 2.0% of gross remuneration |
| Who pays | Employer (statutory liability) — but employer is required to withhold from the employee's pay |
| Refundability for residents | NWT residents reclaim it via the **Cost of Living Tax Credit** on their T1 (Form NT479) |
| Net effect for low-income NWT residents | Approximately zero (fully offset by the credit) |
| Net effect for non-residents working in NWT (fly-in workers) | 2% out-of-pocket — no credit available |
| Filing frequency | Monthly remittances + annual reconciliation (Form NWT401) |
| Administered by | NWT Department of Finance — *not* CRA |

> **Why it exists.** The NWT has a small resident workforce and a large transient/fly-in workforce (mining, oil & gas, construction). The payroll tax is structured so that the *cost* falls on non-resident workers (who use NWT infrastructure but pay no NWT income tax) while *residents* are made whole through the refundable Cost of Living Tax Credit.

## 2. Required inputs + refusal catalogue

### Required inputs

- **Employer details** — Legal name, business number, NWT payroll tax account number (assigned on registration with NWT Finance).
- **Permanent establishment status** — Does the employer have a PE in NWT? (Office, mine, camp, construction site lasting > 30 days, etc.)
- **Per-employee data for the period** — Employee name and SIN; NWT resident vs non-resident status (for the employee's own T1 — does not change employer remittance); Gross remuneration paid in the period (salary, wages, bonuses, taxable benefits, vacation pay, commissions, directors' fees, gratuities reported to employer, stock option benefits); Days worked in NWT vs days worked elsewhere (for allocation if employee splits time)
- **Period** — Calendar month for remittance; calendar year for NWT401 reconciliation.
- **Prior remittances** — Running total of monthly remittances for the year-to-date.

### Refusal catalogue — out of scope for this skill

- **R-NT-PAY-1** — Self-employed individuals / sole proprietors with no employees — payroll tax does not apply to drawings or self-employment income. Refuse and redirect to T1 / T2125.  _(R-NT-PAY-1)_
- **R-NT-PAY-2** — Allocation disputes between NWT and another jurisdiction for an employee splitting time across multiple provinces/territories with complex facts. Escalate to NWT Finance ruling.  _(R-NT-PAY-2)_
- **R-NT-PAY-3** — Treaty-protected non-resident-of-Canada employees (e.g., short-term US-based employees relying on Article XV of the Canada-US Treaty) — federal treaty protection does not override NWT payroll tax, but the analysis is non-trivial. Escalate.  _(R-NT-PAY-3)_
- **R-NT-PAY-4** — Status Indian employees working on a reserve — reserves are uncommon in NWT but the s. 87 Indian Act analysis interacts with the Payroll Tax Act. Escalate.  _(R-NT-PAY-4)_
- **R-NT-PAY-5** — Stock option benefits where the option was granted while the employee was in another jurisdiction and exercised while in NWT — sourcing rules are complex. Escalate.  _(R-NT-PAY-5)_
- **R-NT-PAY-6** — Successor employer / asset-purchase scenarios where account transfer is contemplated. Escalate.  _(R-NT-PAY-6)_

## 3. Rate and incidence

- **Rate** — 2.0% on all wages, salaries, and other remuneration paid to employees who report for work in the Northwest Territories.
- **Employer-paid only** — There is no separate employee contribution. However, the Payroll Tax Act requires the employer to withhold the 2% from the employee's pay, so the economic incidence is on the employee even though the statutory liability is on the employer.  _(Payroll Tax Act)_
- **Remittance destination** — The employer remits the withheld amount to the NWT Department of Finance — this is entirely separate from CRA payroll remittances (CPP/EI/income tax withholding) and is not part of the PD7A workflow.

### Base of the tax — what counts as "remuneration"

- **Includes** — Salary, wages, hourly pay; Overtime, shift premiums, on-call pay; Bonuses, commissions, incentive pay; Vacation pay (paid out or accrued); Directors' fees; Stock option benefits taxable under ITA s. 7; Taxable allowances and benefits (housing, automobile, etc.); Tips and gratuities controlled by the employer; Severance and retiring allowances; Pay in lieu of notice
- **Excludes** — Reimbursements of business expenses; Non-taxable benefits (e.g., reasonable per-diem travel allowances); Pension benefits paid to former employees (paid by pension administrators, not by the employer in respect of employment); Workers' compensation benefits

## 4. Coordination with the Cost of Living Tax Credit (NWT residents)

- **Cost of Living Tax Credit** — NWT residents reclaim the 2% via the Cost of Living Tax Credit on their T1, computed on Form NT479 — Northwest Territories Credits.  _(Form NT479)_

### How it works

- **Step 1** — Employer withholds 2% and remits it to NWT Finance throughout the year.
- **Step 2** — At year-end, employer reports total NWT payroll tax withheld in Box 14 of the T4 informational note (the T4 itself does not have a dedicated box — the amount is typically disclosed on the T4 "Other information" area using code 80 / employer note; verify current CRA T4 guide).
- **Step 3** — NWT-resident employee files T1 + NT(S2) provincial schedule + NT479.
- **Step 4** — NT479 computes the Cost of Living Tax Credit, which is a refundable credit. For low-to-middle income NWT residents the credit is calibrated to approximately offset the 2% payroll tax. The credit phases down at higher income levels — so high-income NWT residents bear a partial 2% cost, and very high-income earners bear nearly the full 2%.  _(Form NT479)_
- **Step 5** — Non-residents of NWT (e.g., Alberta fly-in workers, Ontario consultants) cannot claim NT479 — they bear the full 2% with no offset.

> **Practical implication.** When advising NWT-resident employees, emphasise that the 2% withheld from each paycheque is largely recovered at tax time via NT479 — they should not view it as a permanent cost. When advising employers with fly-in workforces, flag that fly-in workers' net pay is permanently reduced by 2% (no recovery), which may affect compensation negotiations.

## 5. Registration

- **Intro** — 

### Who must register

- **Registration triggers** — Any employer that: (a) has a permanent establishment in the Northwest Territories, OR (b) pays remuneration to an employee who reports for work at a PE in NWT, OR (c) pays remuneration to an employee who works in NWT for any period (the "deemed PE" rule for transient employers) — regardless of where the employer itself is incorporated or resident.

> **This means** a Calgary or Toronto company with even one NWT-resident remote worker has an NWT payroll tax registration and remittance obligation. The "we have no NWT office, we just have a remote employee in Yellowknife" defence does not work.

### How to register

- **Registration process** — File the Application for Registration as an Employer with the NWT Department of Finance, Taxation Division. An NWT Payroll Tax account number is issued.
- **Registration deadline** — Before the first remittance is due (i.e., before the 20th of the month following the first month wages are paid).

### Deregistration

- **Deregistration process** — File a closure form with NWT Finance when the last NWT employee leaves payroll. File the final NWT401 reconciliation.

## 6. Filing — monthly remittances + annual reconciliation

- **Intro** — 

### Monthly remittances

- **Due date** — Due on or before the 20th day of the month following the month in which the remuneration was paid.

Example: remuneration paid in October 2025 → remit by 20 November 2025.

- **Remittance form** — Monthly payroll tax remittance return (PDF or NWT Finance e-portal).
- **Late filing / late payment penalty** — Typically the greater of 10% of the amount owing or a fixed dollar minimum, plus interest at the prescribed NWT rate (verify current rate in NWT Finance bulletins).  _(NWT Finance bulletins)_

### Quarterly remittance option

- **Quarterly option** — Small employers (total annual remuneration below a low threshold set by NWT Finance — verify current threshold) may apply to remit quarterly. Approval is discretionary.

### Annual reconciliation — Form NWT401

- **Due date** — Due on or before 28 February of the year following the calendar year.  _(Form NWT401)_
- **Purpose** — Reconciles the sum of monthly remittances to the actual 2% × total remuneration for the year. Any shortfall is paid with the NWT401; any overpayment is refunded or credited forward on application. Also reports the per-employee remuneration figures used to compute the credit (so NWT Finance can cross-check NT479 claims).  _(Form NWT401)_

## 7. Form NWT401 — annual reconciliation

The NWT401 is the employer's annual reconciliation. Key sections:

**NWT401 sections**

| Section | Content |
| --- | --- |
| Part 1 | Employer identification (legal name, NWT payroll tax account number, business number, address) |
| Part 2 | Total remuneration paid in the year to all employees subject to NWT payroll tax |
| Part 3 | 2% × total remuneration = payroll tax payable for the year |
| Part 4 | Sum of monthly remittances paid during the year |
| Part 5 | Balance owing (Part 3 minus Part 4, if positive) or refund / carryforward (if negative) |
| Part 6 | Per-employee schedule — name, SIN, gross remuneration, NWT payroll tax withheld |
| Part 7 | Certification by employer |

- **Filing channel and retention** — Filing channel: paper or NWT Finance e-portal. Retain supporting payroll records for 6 years.

## 8. Worked example — Yellowknife mining services company

**Facts.**
- "Arctic Drill Services Ltd." — a CCPC with a PE (drilling yard + offices) in Yellowknife.
- 50 employees on the NWT payroll for calendar year 2025:
  - 35 NWT residents (Yellowknife and Hay River-based) earning $3.5M total
  - 15 fly-in workers from Alberta and Saskatchewan earning $1.5M total
- Total NWT remuneration for 2025: **$5,000,000**.

**Computation.**

1. NWT Payroll Tax = 2% × $5,000,000 = **$100,000**.
2. Monthly remittances throughout 2025 (illustrative, even payroll):
   - $100,000 ÷ 12 ≈ $8,333.33 per month
   - Due on or before 20th of the following month
3. Annual reconciliation NWT401 filed 28 February 2026 — confirms $100,000 paid, no balance owing.
4. **T4 reporting.** Each employee's T4 shows gross employment income (no reduction for the 2% — the withholding is a tax, not an employment deduction). The 2% withheld is reported in the T4 "Other information" area with the appropriate code (verify code in current CRA T4 guide; commonly code 80 / employer note).
5. **NT479 credit on individual returns.**
   - The 35 NWT residents file T1 + NT(S2) + **NT479** and claim the Cost of Living Tax Credit. For most of them — low- to middle-income earners — the credit effectively returns the 2% to them.
   - Example: an NWT resident earning $80,000 has $1,600 withheld in NWT payroll tax during the year. On NT479, after applying the credit formula, the credit is roughly $1,500–$1,600 — substantially offsetting the cost. (Exact numbers depend on the year's NT479 formula — see Sources.)
   - The 15 Alberta/Saskatchewan fly-in workers file their T1 in their province of residence, cannot claim NT479, and bear the full 2% (≈ $30,000 in aggregate across the 15 workers) as a permanent cost.

**Net cost to employer.** Zero direct cost (employer withholds from employee pay, then remits to NWT Finance). Indirect cost: administrative compliance burden plus possible compensation pressure from fly-in workers asking for a "NWT premium" to offset their 2% drag.

## 9. Coordination with federal payroll deductions

- **Intro** — The NWT Payroll Tax is completely separate from CRA payroll remittances.

**CRA vs NWT Finance comparison**

| Item | CRA (federal) | NWT Finance |
| --- | --- | --- |
| CPP contributions (employee + employer) | Yes — PD7A | No |
| EI premiums (employee + employer) | Yes — PD7A | No |
| Income tax withholding (federal + provincial/territorial) | Yes — PD7A | No |
| NWT Payroll Tax | No | Yes — monthly remittance + NWT401 |
| Forms | T4 slip, T4 Summary, PD7A | NWT401 + monthly remittance |
| Account | CRA payroll account (RP) | NWT payroll tax account |
| Deadline for monthly remittance | Varies (regular: 15th of following month; threshold-based) | 20th of following month |
| Year-end deadline | T4 / T4 Summary by last day of February | NWT401 by 28 February |

### T4 reporting

- **T4 Box 14** — Employment income — reports gross remuneration. The 2% NWT payroll tax is not subtracted from Box 14 — it is a tax withheld, not an employment expense.
- **T4 Box 22** — Income tax deducted — reports federal + territorial income tax withheld. Do not include the 2% NWT payroll tax here.
- **T4 Other information** — The 2% NWT payroll tax withheld is reported separately so that the NWT-resident employee can claim NT479. Use the code specified in the current CRA T4 guide (commonly the employer note / Other Info code 80; verify annually).  _(CRA T4 Guide)_

### Deduction for the employer

- **Employer deduction status** — Because the statutory incidence is the employer but the tax is withheld from employee pay, the employer's net cash outlay is zero. There is no employer deduction for the 2% withheld and remitted (the employer is acting as a withholding agent, not bearing the cost).
- **Gross-up scenario** — If, by contract, an employer agrees to gross up the employee's pay to absorb the 2%, the gross-up itself is additional remuneration — which is itself subject to 2% NWT payroll tax (circular, but small).

## 10. Conservative defaults

When facts are ambiguous, apply the following defaults:

- **Default 1** — Default to "remuneration is taxable" — if uncertain whether a payment is "remuneration", include it in the 2% base. The employee will recover it via NT479 if they are an NWT resident.
- **Default 2** — Default to "employee is reporting for work in NWT" — if the employee has any NWT connection (NWT address on file, days worked in NWT, NWT-based supervisor), apply the 2%. Excluding by mistake creates an employer liability with penalties; including by mistake is recovered by the employee at year-end.
- **Default 3** — Default to registering — if the employer has even one possibly-NWT employee, register. The cost of an unused account is near zero; the cost of unregistered remittance liability is significant.
- **Default 4** — Default to monthly remittance — quarterly is by application only; assume monthly unless NWT Finance has approved otherwise in writing.
- **Default 5** — Default to reconciling annually even if no remittance was due — if registered, file the NWT401 with zeros rather than skip filing.
- **Default 6** — Default to escalating non-resident-of-Canada employees — treaty interactions are out of scope for this skill (R-NT-PAY-3).  _(R-NT-PAY-3)_
- **Default 7** — Default to verifying the current NT479 formula and Cost of Living Tax Credit parameters annually — the credit amounts and phase-out are updated by NWT Finance each year.

## 11. Sources

- **Primary legislation — Payroll Tax Act** — Payroll Tax Act, R.S.N.W.T. 1988, c. P-2 (Northwest Territories) — establishes the 2% payroll tax, the employer's obligation to withhold and remit, registration requirements, monthly remittance, annual reconciliation, and penalties.  _(Payroll Tax Act, R.S.N.W.T. 1988, c. P-2)_
- **Primary legislation — Payroll Tax Regulations** — Payroll Tax Regulations, R.R.N.W.T. 1990, c. P-9 — administrative detail, forms, prescribed information.  _(Payroll Tax Regulations, R.R.N.W.T. 1990, c. P-9)_
- **Federal coordination — Income Tax Act** — Income Tax Act (Canada), R.S.C. 1985, c. 1 (5th Supp.) — s. 7 (stock option benefits), s. 87 Indian Act interaction (federal side), T1 individual return mechanics.  _(Income Tax Act (Canada), R.S.C. 1985, c. 1 (5th Supp.))_
- **Federal coordination — CRA T4 Guide** — CRA T4 Guide (RC4120) — current year — for T4 reporting of NWT payroll tax in "Other information" boxes.  _(CRA T4 Guide (RC4120))_
- **Forms — Form NWT401** — Form NWT401 — Annual Payroll Tax Reconciliation (NWT Finance).  _(Form NWT401)_
- **Forms — Monthly Payroll Tax Remittance Return** — Monthly Payroll Tax Remittance Return (NWT Finance).  _(Monthly Payroll Tax Remittance Return)_
- **Forms — Form NT479** — Form NT479 — Northwest Territories Credits (Cost of Living Tax Credit) — filed by NWT residents with their T1.  _(Form NT479)_
- **Forms — Form NT(S2)** — Form NT(S2) — Northwest Territories Provincial / Territorial Tax (T1 schedule).  _(Form NT(S2))_
- **Forms — T1 General** — T1 General — federal individual return.  _(T1 General)_
- **Administrative guidance — Payroll Tax Information Circular** — NWT Department of Finance — Payroll Tax — Information Circular (current edition).  _(NWT Department of Finance Information Circular)_
- **Administrative guidance — Employer's Guide** — NWT Department of Finance — Payroll Tax — Employer's Guide (current edition).  _(NWT Department of Finance Employer's Guide)_
- **Administrative guidance — CRA T4 Guide cross-reference** — CRA T4 Guide RC4120 — current edition — for cross-reference on T4 reporting of provincial/territorial payroll taxes.  _(CRA T4 Guide RC4120)_

See `packages/canada/federal/ca-t1-individual-return.md` for the federal T1 return into which NT479 feeds.
See `packages/canada/federal/ca-t4-issuance.md` for the T4 slip preparation, including the "Other information" coding for NWT payroll tax.
See `packages/canada/northwest-territories/nt-individual-return.md` for the NWT-resident individual return and full NT479 / Cost of Living Tax Credit computation.

## End of skill notice

*End of skill — nt-payroll-tax v1.0 (2025 tax year, pending verification).*

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
