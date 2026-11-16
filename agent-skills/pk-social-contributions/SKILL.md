---
name: pk-social-contributions
description: "Use for pakistan social contributions and coverage. Read the stated period, eligibility conditions, evidence requirements, owner skills and unresolved boundaries before calculating or preparing a return."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/pk-social-contributions"
  jurisdiction: "PK"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Pakistan social contributions and coverage v1.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

For Pakistan workers, employers and self-employed freelancers in 2026. Separate federal EOBI pension cover from provincial medical/contingency social security and salary income-tax withholding. A self-employed freelancer with no employees is not automatically an employer owing contributions on freelance profits. Existing insurance, employment elsewhere, voluntary admission, notified categories and actual hires still require checking. Do not turn that distinction into an exemption from income or services tax.

## Ask the client first

Obtain legal form, worker/contractor relationships, present and prior headcount, establishment/worker locations, existing EOBI/SESSI/PESSI/KPESSI/BESSI registrations, insured-person records, any voluntary/notified coverage, wage/base notifications and the period. For a solo freelancer establish whether they also work in insurable employment. For an employer obtain wage and contribution/payment records.

## The method, step by step

1. Identify whether there is an employer/employee relationship and an establishment within the scheme. Do not assess a payroll contribution just because an individual earns freelance receipts.
2. Test EOBI coverage using the current administrative position and the legal-source conflict below. The current ministry FAQ and 2026 parliamentary reply state 10 or more employees/persons, with notified establishments and voluntary smaller establishments. Prior coverage/headcount can matter; do not deregister merely because headcount falls. The general 10-person threshold appears in words and numerals in the parliamentary reply; the consolidated 5-person and prior 12-month quantities are in words on the page. [Ministry FAQ 4](https://ophrd.gov.pk/Detail/OGI0NzE3NGEtMzllOS00NjUwLTgzYjgtM2QwNzY4OGNkZWYy); [parliamentary reply pp 48-49](https://na.gov.pk/uploads/documents/6ae817d42a069_262.pdf); [Act s.1(4)](https://pakistancode.gov.pk/pdffiles/administratorf3be1ec8d21dfebb9c5d1733f43cffe6.pdf).
3. Establish the applicable contribution base from a current federal notification and the actual insured status, not from a province's minimum-wage headline or the worker's whole salary. Keep employer and employee shares separate, and never deduct the employer share from the worker. [Act ss.9/9 B](https://pakistancode.gov.pk/pdffiles/administratorf3be1ec8d21dfebb9c5d1733f43cffe6.pdf); [Ministry FAQ 5](https://ophrd.gov.pk/Detail/OGI0NzE3NGEtMzllOS00NjUwLTgzYjgtM2QwNzY4OGNkZWYy).
4. Test the relevant provincial scheme separately: Sindh SESSI, Punjab PESSI, KPKPESSI or Balochistan BESSI. Obtain the applicable coverage/wage-ceiling/rate/base/date and any continued-insurance rule. Do not assume every low-wage worker qualifies or every higher-paid worker stops coverage. Medical/sickness/maternity/employment-injury/survivor benefits are distinct from federal pension coverage.
5. Reconcile contributions by insured person and period to the relevant institution's records/payments. For staff load `pk-payroll-eobi` and `pk-payroll`; for a documented solo-only case keep the finding and revisit when employees are hired.

## Rates, bands and thresholds

| EOBI item and conditions | Current source position | Official source |
|---|---|---|
| Current ministry contribution description, per insured person | Employer 5% plus employee 1% of federal-notified minimum wage; total 6% (figures in words on the page); actual base not confirmed here | [Ministry FAQ 5](https://ophrd.gov.pk/Detail/OGI0NzE3NGEtMzllOS00NjUwLTgzYjgtM2QwNzY4OGNkZWYy) |
| Current administrative general headcount | 10 or more, plus establishments specified by notification; smaller establishments may join voluntarily (10-person threshold in words and numerals on the page) | [Parliamentary reply pp 48-49](https://na.gov.pk/uploads/documents/6ae817d42a069_262.pdf) |
| Conflicting consolidated statutory print | s.1(4) prints 5, including previous 12 months, continued coverage and voluntary branch, with a Finance Act 2008 substitution footnote; this conflict requires legal/court reconciliation before a threshold-only coverage decision (5-person and 12-month quantities in words on the page) | [Act s.1(4)](https://pakistancode.gov.pk/pdffiles/administratorf3be1ec8d21dfebb9c5d1733f43cffe6.pdf) |

## Boundary and exception table

| Situation | Supported treatment |
|---|---|
| Solo freelancer, no employment or prior/voluntary/notified coverage | No employer payroll arises merely on own freelance profit; retain evidence and check income/services-tax separately |
| Freelancer hires staff | Reassess EOBI and the province's social-security law; do not wait for an assumed 5-person threshold or assume every 1-person business is mandatory |
| Previously insured establishment/headcount falls | Check continued applicability/registration, not automatic cessation |
| Voluntary employer or self-employed route | Smaller-establishment voluntary admission is evidenced; a standalone self-employed voluntary scheme is not confirmed by that rule |
| Provincial low-wage/medical scheme | Apply actual provincial coverage/base/notification; it is not interchangeable with EOBI |


### Sindh coverage requires a separate test

The Sindh 2021 amendment adds self-employed workers to the employee definition and inserts s.20A: an employee other than one employed by an employer pays a fixed **PKR 1,500 monthly**, subject to prescribed conditions. The definition includes daily-wage, construction, home-based, transport, fisheries, agricultural, seasonal and shops/commercial-establishment workers. This is a separate provincial route; absence of employees does not establish absence of all social-security obligations. Obtain the implementing conditions and actual category/registration before charging a solo freelancer. The 1,500 amount is in words on the page. [2021 amendment ss.2-3](https://www.sessi.gov.pk/assets/files/content/2026/01/Sindh-Act-No.XIX-of-2021.pdf).

The 2018 amendment retains existing insurance when wages exceed the upper limit. It defines the lower wage limit by the prevailing Sindh minimum wage and the upper limit as that minimum plus **PKR 5,000**; the self-assessment scheme uses **6% of the lower limit** per secured employee. Read the actual scheme and s.20 provisos before choosing a base: these are not authority for a universal 6%-of-actual-pay rule. The current minimum-wage notification and applicability remain outstanding. The 5,000 amount and 6% contribution are in words on the page. [2018 amendment ss.4(ii),(vi),8-9,20](https://www.sessi.gov.pk/assets/files/content/2026/01/SINDH-EMPLOYEES-SOCIAL-SECURITY-AMENDMENT-ACT-2018.pdf).


### Other provincial contribution branches

KP Act 2021 s.20 requires employer 6% of wages for covered employees, capped by the minimum wage or s.12 determination, with no recovery of employer contribution from wages. Initial wage eligibility under s.2(k)(e) is 60% above the notified minimum, and existing secured employees continue despite a later increase. Thus eligibility ceiling and contribution base differ. Section 22 requires employer particulars within 60 days of applicability. Obtain actual current notification/establishment coverage before computing. [KP Act ss.2(k),20/22](https://kpcode.kp.gov.pk/uploads/THE_KHYBER_PAKHTUNKHWA_EMPLOYEES_SOCIAL_SECURITY_ACT_2021.pdf), read 2026-11-14; figures in words on the page are shown as numerals.

Balochistan Act 2022 s.20 uses employer 6% with upper-limit cap and prevailing-minimum-wage proviso; s.75 lower limit is the notified minimum, upper is minimum plus 15%. Section 21 self-assessment uses 6% of lower limit per secured employee and a separate 60 monthly employee share. Sindh's self-assessment employee share is 40 monthly under s.21(3), separate from conditional self-employed 1,500 and employer-share recovery prohibition. These province-specific branches replace the universal “no employee ESSI deduction” assumption; they do not establish current numerical wage notifications or every professional's coverage. [Balochistan Act ss.20/21/75](https://pabalochistan.gov.pk/storage/4287/2022-11-28_10_00_34_34dbd.pdf); [Sindh Act ss.20/21](https://www.sessi.gov.pk/assets/files/content/2026/01/Sindh-Employees-Social-Security-Act-2016-with-rules-and-ammendments.pdf), read 2026-11-14 for these provisions; worded figures shown as numerals.

## Worked cases

Examples are conditional arithmetic on an **assumed**, already-verified contribution base; PKR 40,000 is not asserted to be the legally notified base. Coverage and actual base must be established first.

```oa-check
name: Separate employer and employee EOBI shares
inputs:
  assumed_monthly_base: 40000
  insured_workers: 10
steps:
  - employer_share: assumed_monthly_base * 0.05 * insured_workers
  - employee_share: assumed_monthly_base * 0.01 * insured_workers
  - total_remittance: employer_share + employee_share
expected:
  employer_share: 20000
  employee_share: 4000
  total_remittance: 24000
```

```oa-check
name: Reconcile paid contributions without shifting employer cost
inputs:
  assumed_monthly_base: 40000
  insured_workers: 12
  actual_paid: 28000
steps:
  - required_employer: assumed_monthly_base * 0.05 * insured_workers
  - required_employee: assumed_monthly_base * 0.01 * insured_workers
  - supported_due: required_employer + required_employee
  - shortfall: supported_due - actual_paid
expected:
  required_employer: 24000
  required_employee: 4800
  supported_due: 28800
  shortfall: 800
```

The 800 shortfall needs correction/evidence; it is not an extra deduction from employees to recover the employer share. The older solo-freelancer case remains a coverage question: without employees or another applicable insurance route there is no employer payroll; hiring 5 staff now triggers a review, not an automatic conclusion on the conflicting threshold sources.

## When to refuse or refer

Never impose a mandatory self-employed profit contribution without an operative rule, omit employer scheme review after hiring, quote a rate/base/ceiling without the actual period source, treat federal/provincial schemes as one, or promise a self-employed voluntary route from the smaller-employer provision. Refer the unresolved headcount/judicial issue, retroactive/continued coverage, cross-province workers, benefit claims and contribution disputes.

## Filing and payment

Use each institution's actual current registration, insured-person schedule/challan and due date. Keep EOBI and provincial payments/returns separate from FBR salary tax and quarterly withholding statements. The old blanket 15th/31 July provincial calendar is not confirmed here.

## Completion checklist

Employment and locations established; coverage/continuation/voluntary branch supported; source conflict resolved for the actual case; notification/base/rate period obtained; employer/employee shares separated; paid records reconciled; provincial scheme checked separately; no unconfirmed voluntary self-employed promise.

## Sources

| Source and actual portions read | Official URL | Read on |
|---|---|---|
| Read for KP Act ss.2(k)(e),20/22, Balochistan Act ss.20/21/75 and Sindh compilation contribution ss.20/21 on 2026-11-14 | https://kpcode.kp.gov.pk/uploads/THE_KHYBER_PAKHTUNKHWA_EMPLOYEES_SOCIAL_SECURITY_ACT_2021.pdf; https://pabalochistan.gov.pk/storage/4287/2022-11-28_10_00_34_34dbd.pdf; https://www.sessi.gov.pk/assets/files/content/2026/01/Sindh-Employees-Social-Security-Act-2016-with-rules-and-ammendments.pdf. | 2026-11-14 |
| Read for Sindh 2021 amendment ss.2-3 definitions and fixed self-employed contribution subject to conditions | https://www.sessi.gov.pk/assets/files/content/2026/01/Sindh-Act-No.XIX-of-2021.pdf | 2026-11-14 |
| Read for Sindh 2018 amendment ss.4(ii),(vi),8-9,20 continued insurance, limits, self-assessment and s.20 provisos | https://www.sessi.gov.pk/assets/files/content/2026/01/SINDH-EMPLOYEES-SOCIAL-SECURITY-AMENDMENT-ACT-2018.pdf | 2026-11-14 |
| Read for ministry EOBI FAQ 4-5 current administrative threshold and contribution split/base description | https://ophrd.gov.pk/Detail/OGI0NzE3NGEtMzllOS00NjUwLTgzYjgtM2QwNzY4OGNkZWYy | 2026-11-14 |
| Read for National Assembly reply pp 48-49, general 10-person rule, notified establishments and voluntary smaller establishments | https://na.gov.pk/uploads/documents/6ae817d42a069_262.pdf | 2026-11-14 |
| Read for EOB Act 1976 ss.1(4),9,9 B,10/11 and Finance Act 2008 footnotes; consolidated threshold conflicts with current administrative sources | https://pakistancode.gov.pk/pdffiles/administratorf3be1ec8d21dfebb9c5d1733f43cffe6.pdf | 2026-11-14 |

Not yet confirmed: judicial reconciliation of 5-person consolidated print against current 10-person administrative rule; current numeric federal contribution base; current provincial wage notifications, Punjab operative law, establishment coverage and calendars beyond the read branches; standalone federal self-employed voluntary admission; Sindh s.20A implementing conditions and actual category coverage. The old 40,000/37,000 provincial/federal base assumptions are not usable instructions. No current pension-benefit calculation is supplied.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `pk-social-contributions` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/pk-social-contributions. If neither is available, confirm every figure against the official source pages cited above before relying on it.
