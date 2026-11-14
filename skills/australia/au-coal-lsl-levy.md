---
name: au-coal-lsl-levy
description: >
  Use this guide for the Australian black coal mining industry portable long service leave
  payroll levy: whether an employer and each worker are covered (Coal Mining Industry (Long
  Service Leave) Administration Act 1992 s 4), eligible wages under s 3B of the Payroll Levy
  Collection Act 1992, the levy rate, the monthly Levy Advice return and payment, additional
  levy, adjustments and the annual audit report. Covers national system employers, including
  contractors and labour hire firms, for 2026-27. Trigger on 'Coal LSL', 'coal long service
  leave levy', 'Levy Advice', 'eligible wages' or 'black coal mining payroll'.
jurisdiction: AU
category: payroll
tax_year: 2026
tax_year_notes: "2026-27"
tier: 2
last_updated: 2026-11-11
version: 0.1
review_status: pending_review
verified_by: pending
license: FSL-1.1-ALv2
depends_on:
  - workflow-base
  - payroll-workflow-base
---

# Australia Coal Mining Long Service Leave Payroll Levy v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

This guide loads on `workflow-base` and `payroll-workflow-base` and fills the Section 7 slots for the black coal mining industry portable long service leave scheme, administered by the Coal Mining Industry (Long Service Leave Funding) Corporation (Coal LSL). It covers an employer's:

- coverage position: whether it is an employer under the scheme and which workers are eligible employees;
- eligible wages for each eligible employee each month;
- levy at the prescribed rate;
- monthly return (the Levy Advice) and payment, additional levy for late payment, and corrections by Adjustment Levy Advice;
- annual audit report; and
- tie-out of the return to payroll, the ledger and the bank.

The output is a levy workpaper and a coverage file note for an authorised person to sign off. The guide does not conclude on coverage.

**Not covered here; route to the guide that holds it:**

| Topic | Guide |
|---|---|
| General payroll, PAYG withholding, Single Touch Payroll and state and territory long service leave entitlements | `australia-payroll` |
| Payroll tax on wages and on long service leave payments | `au-payroll-tax` |
| Superannuation guarantee and ordinary time earnings (a different base from eligible wages) | `au-super-guarantee` |
| Tax on unused long service leave paid on termination | `au-employment-termination-payments` |
| Accounting for the leave provision and the reimbursement right | `australia-financial-statements` |

Also out of scope: approving and paying long service leave under Part 5A of the Administration Act, reimbursement claims under Part 7 (s 44 and the Employer Reimbursement Rules made under s 45), unpaid levy payment arrangements under Schedule 1 to the Collection Act, and the income tax treatment of the levy (not verified here; Needs Input). Refer them (R-AU-CLSL-4, R-AU-CLSL-5).

**Period coverage.** The law as read on 2 November 2026 on the Federal Register of Legislation: the Administration Act compilation 25 and the Payroll Levy Collection Act compilation 12, both in force from 1 September 2026 and including the *Coal Mining Industry (Long Service Leave) Legislation Amendment Act 2026* (Act No. 63, 2026); the Payroll Levy Act compilation registered C2012C00097; and the Payroll Levy Regulations 2018 compilation 1 (F2023C00557), in force from 1 July 2023. The Register lists the Regulations as due to be repealed on 1 April 2028 under s 50 of the *Legislation Act 2003*; recheck the rate instrument for any month after that date.

## Ask the client first

1. Employer legal structure, where it carries on activities and employs workers, and whether it is registered with Coal LSL.
2. For each worker, a firm-held employee reference (no names, dates of birth or Coal LSL numbers in skill input): duties, work location, roster or work pattern, engagement model (full time, part time, casual, labour hire), start and cease dates and any unpaid leave or workers compensation period.
3. Payroll detail for every payroll week ending in the reporting month, with week start dates and hours, separating base or ordinary pay, salary, casual loading, overtime, penalty rates, shift loading, allowances, expense reimbursements, salary sacrifice, and incentives and bonuses with their payment frequency.
4. The industrial instrument for each casual, showing whether a casual loading is specified and can be quantified.
5. Workers compensation or income protection amounts, split by whether the insurer pays the employee directly or reimburses the employer.
6. Prior Levy Advice forms, payment confirmations and any Adjustment Levy Advice.
7. Ledger accounts for levy expense and levy payable, and bank statements for levy paid.
8. The financial year end and who will give the annual audit report.
9. Any waiver agreement under s 39B of the Administration Act: the signed agreement, its lodgment date with Coal LSL, the Board's decision (or that 30 days passed without one), its take-effect date, any variation or termination, and the prescribed kind the employee falls in.

## The method, step by step

### Key figures and rules (read 2 November 2026)

| Item | Value | Source |
|---|---|---|
| Who pays | The person who paid the eligible wages | Payroll Levy Act 1992 s 6 |
| Levy rate | 2.7% of the eligible wages paid, for eligible wages paid on or after 1 July 2023 | Payroll Levy Regulations 2018 ss 6, 8; Payroll Levy Act s 5; Coal LSL levy returns page |
| Return | Within 28 days after the end of each month in which the person employs an eligible employee at any time, in the approved form | Collection Act s 5(1)-(2A) |
| Payment due | At the end of the period for the return for that month, unless Coal LSL extends the time or permits instalments | Collection Act ss 4, 6 |
| Additional levy | On levy unpaid after it became payable, at 2 percentage points above the Reserve Bank's most recently published cash rate target, unless regulations prescribe a rate; Coal LSL describes it as per annum, calculated daily | Collection Act s 7(1)-(2); Coal LSL levy returns page |
| Remission of additional levy | Written request to Coal LSL; no decision within 30 days is a deemed refusal; decisions are reviewable by the Administrative Review Tribunal | Collection Act s 8 |
| Annual audit report | Given to Coal LSL no later than 6 months after the end of the financial year, by an auditor, with reasons | Collection Act s 10(1) |
| Auditor report on Coal LSL's notice | The notice sets the due date, which must be at least 28 days after the notice is given to the auditor, and the auditor must comply; the employer is repaid the auditor's fee from the Fund if the report finds all levy and additional levy paid | Collection Act ss 10A(2)-(3), 10B(2) |
| Penalties for a late return or audit report | Civil penalty 40 penalty units; strict liability offence 30 penalty units; an executive officer's civil penalty 60 penalty units | Collection Act ss 5, 10, 13B |
| Overpaid levy | Refunded from the Fund | Administration Act s 47 |
| Waiver agreement in effect | No levy on that employee's eligible wages for the period; the return still includes the employee | Administration Act ss 39B, 39BD |

The dollar value of a penalty unit is not stated here; read the *Crimes Act 1914* s 4AA figure current at the time of the contravention if a penalty is in issue (refer: R-AU-CLSL-5).

### Step 1: Employer status

The Administration Act defines employer as a national system employer under s 14 of the *Fair Work Act 2009* (s 4). Coal LSL's registration page lists who can register: a company registered with ASIC, a trust with a corporate trustee, a partnership including a company partner, an entity incorporated under State law and a foreign company. It says sole traders, partnerships of individuals only and trusts without a corporate trustee are not national system employers and cannot register, and that a sole trader cannot be their own eligible employee. Record the employing entity and its structure. Where the structure is unusual or Coal LSL's list does not plainly answer it, stop and refer (R-AU-CLSL-1); do not conclude registration from legal form alone.

### Step 2: Eligible employee test, per person

Section 4 of the Administration Act has 4 limbs:

- **(a)** employed in the black coal mining industry by an employer engaged in that industry, with duties directly connected with the day to day operation of a black coal mine;
- **(b)** employed in the black coal mining industry, with duties carried out at or about a place where black coal is mined and directly connected with its day to day operation (Coal LSL applies this limb to contractors whose main business is outside the industry, including labour hire);
- **(c)** permanently employed with a mine rescue service for the industry; or
- **(d)** a prescribed person employed in the industry;

excluding anyone the regulations declare not to be an eligible employee. 'Black coal mining industry' has its meaning in the Black Coal Mining Industry Award 2010 as in force on 1 January 2010. A working director can be an eligible employee if they do daily operational work at a black coal mine and are properly treated as an employee paid eligible wages; Coal LSL may ask for contracts, payslips, bank records and site log records (registration page).

### Step 3: Weigh the coverage factors

Coal LSL's scheme coverage guidance weighs nature of duties, work pattern and location of work: no single factor is determinative and all are viewed in totality. The guidance says the duties factor applies whatever the work status (full time, part time, casual, contract or labour hire). Record the reasoning for each role with the indicators both ways, and put the proposed position to the responsible person or Coal LSL (R-AU-CLSL-2).

### Step 4: Eligible wages under s 3B

Choose the method for each employee's category for the month:

| Category | Eligible wages | Provision |
|---|---|---|
| Paid a base rate, not casual | The greater of Formula A (base rate of pay, including incentive-based payments and bonuses) and Formula B (75% of base rate of pay, including incentive-based payments and bonuses, overtime or penalty rates, and allowances other than expense reimbursements) | s 3B(1) |
| Annual salary | Annual salary paid, including incentive-based payments and bonuses, excluding overtime, penalty rates and shift loadings | s 3B(2) |
| Casual, with a casual loading specified in a covering industrial instrument that can be quantified | Base rate of pay, including incentive-based payments, bonuses and the casual loading | s 3B(3)(a) |
| Casual, otherwise | Ordinary rate of pay, including incentive-based payments and bonuses | s 3B(3)(b) |

In every category, pay is taken before salary sacrifice deductions, and an incentive-based payment or bonus counts only if paid at least once a month (s 3B(4)). Base rate of pay has its *Fair Work Act 2009* meaning (Collection Act s 3).

Coal LSL's eligible wages guidance (issued 21 June 2024) adds: compute each employee's eligible wages each month, never as an automatic fixed payment; at the end of the month include eligible wages for all payroll weeks that end in the month; for casuals include all hours worked in those weeks; exclude workers compensation or income protection paid directly by an insurer or other source, but where the employer is compensated and pays the employee in the ordinary way, apply the normal method.

**Casual periods before 1 January 2024.** The current s 3B(3) came from Schedule 6 to the *Fair Work Legislation Amendment (Protecting Worker Entitlements) Act 2023*, commencing 1 January 2024 (Collection Act endnote 3); Coal LSL says the earlier casual method mirrored s 3B(1)(a). Its application rule (Schedule 6 item 17) was not read here: refer any adjustment reaching back before 1 January 2024 (R-AU-CLSL-3).

Eligible wages are not superannuation ordinary time earnings and not payroll tax wages: never reuse a figure from `au-super-guarantee` or `au-payroll-tax`.

### Step 5: Compute the levy

Levy for each employee = eligible wages x the rate in the key figures table, with the Regulations compilation and read date cited. The rounding convention on the Levy Advice is not stated in the sources read: follow the current form and its guide, and record the convention used.

**Waiver agreements: nil levy.** An eligible employee of a kind prescribed by the Administration Regulations may make a written waiver agreement with the employer for additional remuneration or superannuation contributions in lieu of long service leave (Administration Act s 39B(1)). The prescribed kinds are an employee who is at least 55 years of age with no qualifying service or with at least 8 years of it; a manager, or a senior professional employee engaged in management, of a corporation that employs eligible employees in the industry; an employee whose annual salary (including allowances) is at least $174,700 in 2017, adjusted by the Consumer Price Index for 2017 and each later completed year; and an employee on an undergraduate or work training placement (Administration Regulations 2018 s 7). The CPI-adjusted salary figure for the current year is not computed here (Needs Input). For any period during which a waiver agreement is in effect, the employee is taken not to be an eligible employee for the purposes of ss 4 and 6 of the Payroll Levy Act, so no levy is payable on their eligible wages; the note to s 39BD says returns 'will still need to include information in relation to the employee' (Administration Act s 39BD). Levy is nil only from the agreement's take-effect date, which must be after it is lodged with Coal LSL (s 39B(3)(e)), and only until it ceases: on the Board's refusal, on termination or when the employee stops being a prescribed kind (ss 39B(6), 39BC(5)). The Board is taken to approve an agreement it has not decided within 30 days after lodgment (s 39BC(2)). The agreed payments must be worth at least the levy that would otherwise have been payable (s 39B(2)); computing and paying them is outside this guide (refer: R-AU-CLSL-5).

### Step 6: Prepare the Levy Advice workpaper

For each employee reference and month record work status, hours worked per week, eligible wages and levy. An authorised person merges the Coal LSL number, name and date of birth into the Levy Advice inside the firm's approved system. Use the approved form for the period: Coal LSL says a new Levy Advice form applies from 1 January 2024, with a separate form for wages up to 31 December 2023. Reconcile each weekly entry to payroll and the current Levy Advice guide.

### Step 7: Diarise lodgment and payment

Diarise the return and payment for 28 days after month end (Collection Act ss 4, 5). The sections read set no weekend or public holiday rule of their own. Where the last day is a Saturday, Sunday or holiday, *Acts Interpretation Act 1901* s 36(2) may let the thing be done on the next day that is not; confirm the date with Coal LSL before relying on it. Coal LSL says returns are submitted through its Online Services and payment is by direct electronic funds transfer into the Fund, using the account details on the form. Do not set a fixed recurring payment: eligible wages move with hours, overtime, incentives and bonuses. Late payment attracts additional levy daily under s 7; reconcile any additional levy to Coal LSL's assessment rather than computing a day-count convention the Act does not state.

### Step 8: Correct errors

Correct an earlier return by an Adjustment Levy Advice: underpayments are paid into the Fund and overpayments are refunded (Coal LSL levy returns page; Administration Act s 47). Coal LSL says a refund does not offset levy or adjustment levy owed, so never net them.

### Step 9: Reconcile

Eligible wages per the return reconcile to payroll gross with a quantified bridge for each exclusion; hours agree to payroll hours; levy paid agrees to the bank; levy expense and levy payable agree to the ledger.

### Step 10: Schedule the annual audit report

Diarise the s 10 report for 6 months after the financial year end. It must state whether all levy and additional levy for the year was paid, specify any shortfall, state whether any Part 7 reimbursement received was correct and give reasons (s 10(1)). Coal LSL says the report can be given by the company's *Corporations Act 2001* auditor or by an independent accountant holding appropriate qualifications, professional memberships and insurances, and that its audit report template is optional. Where the employer's financial year is not 1 July to 30 June, confirm with the reviewer which period s 10 uses (Needs Input).

### Permitted factual defaults

| Missing fact | Default | Disclosure |
|---|---|---|
| Whether a bonus or incentive is paid at least once a month | Treat it as monthly and include it (higher levy) | Show the levy with and without it |
| Whether an allowance reimburses an expense | Treat it as not a reimbursement and include it in Formula B | Ask for the expense evidence |
| Whether a casual loading can be quantified under the instrument | Apply whichever of s 3B(3)(a) and (b) gives the higher eligible wages | Show both; confirm against the instrument |

**No default is permitted** for coverage of an employer or employee, whether a waiver agreement is in effect, the levy rate, the employee's category, hours worked or the payroll weeks in the month. Each is Needs Input.

### Working paper extension

```
AUSTRALIA COAL LSL LEVY -- MONTHLY WORKPAPER
Employer: [name]   Month: [mm/yyyy]   Return and payment due: [28 days after month end]
Regulations compilation and rate read: [F2023C00557; 2.7%; date]

PER EMPLOYEE REFERENCE (no names, DOB or Coal LSL numbers)
  Coverage position (limb, 3 factors, sign-off): [____]
  Category (base rate | salary | casual a | casual b): [____]
  Payroll weeks ending in month and hours per week: [____]
  Components (pre-salary-sacrifice base or ordinary pay, monthly incentives and bonuses,
    overtime, penalties, allowances, reimbursements excluded, casual loading): [____]
  Formula A / Formula B / eligible wages: [____]
  Levy: [____]

TIE-OUT: payroll gross bridge | hours | bank | ledger | prior adjustments
DIARY: return and payment date | audit report date | auditor
REVIEWER FLAGS: [refusal codes raised]
```

## Worked cases

All facts and figures are hypothetical, for July 2026 (2026-27), with the 2.7% rate from the key figures table.

### Case 1: Non-casual employee paid a base rate (s 3B(1))

Base rate of pay $10,000 before a $1,000 salary sacrifice; monthly incentive $500; overtime $3,000; penalty rates $1,000; a site allowance of $800; an expense reimbursement of $200 (excluded); a quarterly bonus of $2,000 paid this month (excluded: not paid at least once a month).

```oa-check
name: Coal LSL non-casual base rate Formula A and B levy July 2026
tolerance: 0.001
inputs:
  base_rate_pay_before_salary_sacrifice: 10000
  monthly_incentives: 500
  overtime: 3000
  penalty_rates: 1000
  allowances_not_reimbursements: 800
  levy_rate_percent: 2.7
steps:
  - formula_a: base_rate_pay_before_salary_sacrifice + monthly_incentives
  - formula_b: pct(base_rate_pay_before_salary_sacrifice + monthly_incentives + overtime + penalty_rates + allowances_not_reimbursements, 75)
  - eligible_wages: max(formula_a, formula_b)
  - levy: pct(eligible_wages, levy_rate_percent)
expected:
  formula_a: 10500
  formula_b: 11475
  eligible_wages: 11475
  levy: 309.825
```

Formula B is greater, so eligible wages are $11,475 and the levy is $309.825 before the form's rounding convention. Removing overtime or penalties before the comparison would understate the levy.

### Case 2: Salaried employee (s 3B(2))

Monthly salary $12,000 before salary sacrifice, a monthly bonus of $600, overtime of $900 and shift loading of $400 (both excluded).

```oa-check
name: Coal LSL annual salary eligible wages and levy July 2026
tolerance: 0.001
inputs:
  monthly_salary_before_salary_sacrifice: 12000
  monthly_bonus: 600
  levy_rate_percent: 2.7
steps:
  - eligible_wages: monthly_salary_before_salary_sacrifice + monthly_bonus
  - levy: pct(eligible_wages, levy_rate_percent)
expected:
  eligible_wages: 12600
  levy: 340.2
```

### Case 3: Casual with a quantifiable loading (s 3B(3)(a))

A casual works 160 hours in the payroll weeks ending in July 2026 at a base rate of $45 an hour. The covering enterprise agreement specifies a 25% casual loading on the base rate (a hypothetical instrument term). A monthly incentive of $200 is paid.

```oa-check
name: Coal LSL casual with quantifiable loading levy July 2026
tolerance: 0.001
inputs:
  hours_worked: 160
  base_hourly_rate: 45
  casual_loading_percent: 25
  monthly_incentive: 200
  levy_rate_percent: 2.7
steps:
  - base_rate_pay: hours_worked * base_hourly_rate
  - casual_loading: pct(base_rate_pay, casual_loading_percent)
  - eligible_wages: base_rate_pay + casual_loading + monthly_incentive
  - levy: pct(eligible_wages, levy_rate_percent)
expected:
  base_rate_pay: 7200
  casual_loading: 1800
  eligible_wages: 9200
  levy: 248.4
```

If the instrument specified no quantifiable loading, s 3B(3)(b) would use the ordinary rate of pay instead.

### Case 4: Return and payment dates

For July 2026 the return must be made within 28 days after 31 July 2026, so by 28 August 2026, and the levy for July is payable at the end of that period (ss 4, 5). The workpaper diarises 28 August 2026, a Friday, so the question whether *Acts Interpretation Act 1901* s 36(2) moves the day does not arise. A payment made on 4 September 2026 attracts additional levy under s 7 for each day it was unpaid; reconcile the amount to Coal LSL's assessment.

### Case 5: A labour hire maintenance fitter

A labour hire firm whose main business is outside coal mining places a fitter full time on a black coal mine's maintenance roster, working on site. The duties, regular rostered pattern and on-site location all point towards limb (b); Coal LSL's scheme coverage guidance applies limb (b), not (a), to employees of contracting companies whose main business is outside the industry and lists labour hire amongst its examples. Record the indicators, propose limb (b) for sign-off and note that the levy falls on the labour hire firm as the person paying the wages (Payroll Levy Act s 6).

## When to refuse or refer

Stop the affected calculation where a fact, source condition or scope requirement above is unresolved, and return Needs Input or the refusal below.

### Refusal catalogue

| Code | Trigger | Message (verbatim) |
|---|---|---|
| R-AU-CLSL-1 | An employer structure that Coal LSL's registration list does not plainly answer, or any question whether a person is a national system employer | "Whether this entity is an employer under the scheme turns on s 14 of the Fair Work Act 2009 and Coal LSL's assessment. I have recorded the structure; refer it to Coal LSL and the responsible adviser." |
| R-AU-CLSL-2 | Asked to decide whether a worker is an eligible employee | "Coverage is decided by the responsible person and, where doubt remains, Coal LSL. I have recorded the limb and the 3 factors both ways for sign-off." |
| R-AU-CLSL-3 | An adjustment or audit reaching casual periods before 1 January 2024 | "The casual method changed on 1 January 2024 and its application rule was not verified here. Refer the earlier periods for review before computing them." |
| R-AU-CLSL-4 | Historical arrears, a Schedule 1 unpaid levy payment arrangement, or an extension or instalment request under s 6 | "Arrears arrangements and extensions are decided by Coal LSL and its Board under the Collection Act. Assemble the facts and refer to the responsible adviser." |
| R-AU-CLSL-5 | Long service leave approval, payment or reimbursement claims; disputes; penalties; or the income tax or accounting treatment of the levy | "That is outside this levy guide. Refer to the responsible adviser; under s 49 of the Administration Act the Board may determine matters of fact on whether an amount is payable from the Fund." |

### Reviewer attention thresholds

The reviewer attention threshold is **AUD 0**: every difference between levy computed and levy paid, every coverage position and every Adjustment Levy Advice requires review whatever its amount. Flag regardless of amount: any employee whose category changed in the month; any excluded component; any month with workers compensation; and any return or payment made after its due date.

### Prohibitions

- NEVER state the levy rate, additional levy basis or a due date without the compilation or Coal LSL page and the date read.
- NEVER decide coverage of an employer or employee.
- NEVER remove overtime or penalties before the Formula A and B comparison.
- NEVER reuse a superannuation or payroll tax wage figure as eligible wages.
- NEVER net a refund against levy owed.
- NEVER lodge, pay or communicate with Coal LSL; prepare the hand-off for an authorised person.
- NEVER present figures as definitive.

## Completion checklist

- [ ] Every employee carries a proposed coverage position with the limb and the 3 factors, sent for sign-off.
- [ ] Each employee's category and method match s 3B for the month.
- [ ] Eligible wages reconcile to payroll gross, with every exclusion listed and quantified.
- [ ] Levy equals eligible wages times the rate from the compilation read this session.
- [ ] Every employee required on the return is present, including zero-hour and ceasing cases.
- [ ] Each employee with a waiver agreement shows nil levy only for the period it is in effect (ss 39B, 39BD), with the agreement evidence on file, and is still reported on the return.
- [ ] Return, payment and audit report dates are diarised with their source.
- [ ] Levy paid agrees to the bank and ledger; adjustments are not netted against refunds.
- [ ] Every unresolved item records the evidence needed, owner, status and next action.

## Sources

| Source | URL | Read on |
|---|---|---|
| Coal Mining Industry (Long Service Leave) Payroll Levy Regulations 2018, compilation 1 (F2023C00557), ss 6, 8 | https://www.legislation.gov.au/F2018L00217/2023-07-01/2023-07-01/text/original/epub/OEBPS/document_1/document_1.html | 2026-11-02 |
| Federal Register of Legislation API: Regulations title record (status, scheduled repeal 1 April 2028) | https://api.prod.legislation.gov.au/v1/titles('F2018L00217') | 2026-11-02 |
| Coal Mining Industry (Long Service Leave) Payroll Levy Act 1992 (C2012C00097), ss 4-6, 8 | https://www.legislation.gov.au/C2004A04353/2012-01-01/2012-01-01/text/original/epub/OEBPS/document_1/document_1.html | 2026-11-02 |
| Coal Mining Industry (Long Service Leave) Payroll Levy Collection Act 1992, compilation 12 (C2026C00364), ss 3, 3B, 4-10B, 13B, Schedule 1, endnotes | https://www.legislation.gov.au/C2004A04352/2026-09-01/2026-09-01/text/original/epub/OEBPS/document_1/document_1.html | 2026-11-02 |
| *Acts Interpretation Act 1901*, compilation 39 (C2026C00117): s 36(2) | https://www.legislation.gov.au/C1901A00002/2026-03-28/2026-03-28/text/original/epub/OEBPS/document_1/document_1.html | 2026-11-11 |
| Coal Mining Industry (Long Service Leave) Administration Act 1992, compilation 25 (C2026C00370), ss 4, 39B, 39BC, 39BD, 44, 45, 47, 49 | https://www.legislation.gov.au/C2004A04351/2026-09-01/2026-09-01/text/original/epub/OEBPS/document_1/document_1.html | 2026-11-02 |
| Coal Mining Industry (Long Service Leave) Administration Regulations 2018 (F2018L00216, as made, the latest version), s 7 | https://www.legislation.gov.au/F2018L00216/2018-03-07/2018-03-07/text/original/epub/OEBPS/document_1/document_1.html | 2026-11-02 |
| Federal Register of Legislation API: Administration Regulations title record (scheduled repeal 1 April 2028) | https://api.prod.legislation.gov.au/v1/titles('F2018L00216') | 2026-11-02 |
| Coal LSL, Levy returns and payments: 28 days, 2.7%, forms from 1 January 2024, additional levy, adjustments, refunds | https://coallsl.com.au/employer/administer-lsl/levy | 2026-11-02 |
| Coal LSL, Guidance note: determining eligible wages (issued 21 June 2024) | https://coallsl.com.au/guidance-notes/eligible-wages | 2026-11-02 |
| Coal LSL, Guidance note: scheme coverage | https://coallsl.com.au/guidance-notes/scheme-coverage | 2026-11-02 |
| Coal LSL, Employer registration | https://coallsl.com.au/employer/legal-obligations/registration | 2026-11-02 |
| Coal LSL, Annual audits and audit FAQs (who can do the audit) | https://coallsl.com.au/employer/legal-obligations/audit | 2026-11-02 |
| Coal LSL, Understand your obligations | https://coallsl.com.au/employer/legal-obligations/overview | 2026-11-02 |
| Coal LSL, Protecting Worker Entitlements (casual changes from 1 January 2024) | https://coallsl.com.au/employer/protecting-worker-entitlements | 2026-11-02 |

Not read in this session: *Fair Work Act 2009* ss 13, 14 and 16, *Crimes Act 1914* s 4AA, the Employer Reimbursement Rules, the Levy Advice form and guide, Schedule 6 item 17 to Act No. 43, 2023, and any Ministerial determination under Schedule 1 to the Collection Act.

**Currency and revision.** Version 0.1, currency date 2 November 2026. Change log: v0.1 (2 November 2026) first draft from primary sources read that day; awaiting qualified Australian review.

Method adapted by its author from the `coal-lsl-levy` skill in ryanduguid/australian-accounting-skills (commit 3e110da). This guide is licensed under FSL-1.1-ALv2, not the OA Guide License; see LICENSING.md.

Copyright 2026 Ryan Duguid. From github.com/ryanduguid/australian-accounting-skills, FSL-1.1-ALv2. Copies and adaptations of this file must keep this notice.

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
