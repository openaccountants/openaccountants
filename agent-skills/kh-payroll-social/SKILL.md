---
name: kh-payroll-social
description: "Prepare a Cambodia 2026 payroll working paper separating monthly Tax on Salary, employer fringe-benefit tax and employee/employer social-security liabilities. Use for Cambodian payroll, payslip reconciliation, NSSF contribution review and salary-tax withholding. Computes bounded salary cases from confirmed tax rules and documented contribution inputs. Current NSSF wage tables, transition, coverage and contribution assessments remain pending primary-source confirmation."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/kh-payroll-social"
  jurisdiction: "KH"
  tax_year: "2026"
  last_updated: "2026-11-15"
---

# Cambodia Payroll and Social Contributions v0.1

**General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Prepare a review working paper for Cambodian employment payroll in 2026, checked against the identified official sources on 15 November 2026. The General Department of Taxation (GDT), Ministry of Economy and Finance, administers salary tax; NSSF social contributions require separate registration, coverage, wage-base and period evidence. This skill does not establish a complete current NSSF assessment. Keep its social-contribution coverage marked partial.

Use [income tax](kh-income-tax.md) for the complete resident salary-band/dependent/foreign-income method. Salary and fringe-benefit calculations below use [Law arts 41-53](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e), [SD48 art 3](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/1f25fa42-ed6e-4757-a15f-94ec109aae35) and [Prakas575 arts 3-22](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/fb78dfde-8342-4e3c-80e0-84ef81919c70). Original Khmer controls. Never treat a tax-free salary band as a social-contribution exemption or combine employee and employer liabilities on a payslip.

| Confirmed tax item | Amount / population and rule | Official source |
|---|---|---|
| Resident salary tax | Monthly progressive 0% to 20% on the resident taxable salary base after lawful adjustments, not the company-income base | [Law arts 41-47](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e); [SD48 art 3](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/1f25fa42-ed6e-4757-a15f-94ec109aae35) |
| Non-resident salary tax | 20% final tax on Cambodian-source taxable salary; technical-assistance source rule and separate fringe benefits apply; no resident dependent relief | [Law arts 42,46,49](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e); [Prakas575 arts 3,14](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/fb78dfde-8342-4e3c-80e0-84ef81919c70) |
| Fringe-benefit tax | 20% of taxable fair-market benefit value inclusive of taxes; employer withholding/payment; tax in the month provided, regardless of expense timing; test exclusions before taxing | [Law art 48](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e); [Prakas575 arts 15-18](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/fb78dfde-8342-4e3c-80e0-84ef81919c70) |
| Salary return/payment | Statutory 20th of following month; actual period/channel calendar must be checked separately | [Law art 53](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e); [Prakas575 art 22](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/fb78dfde-8342-4e3c-80e0-84ef81919c70) |

## Ask the client first

Obtain the actual payroll month and payment date, employer and worker identities, employment terms, residence/domicile/abode/day-count evidence, gross cash salary, bonuses/allowances, exempt reimbursements, advances/repayments, dependent evidence and separate benefit register. Obtain the official currency conversion instruction and period rate for any USD amounts. Bank statements alone do not establish gross wages, worker status or taxable benefits.

For NSSF obtain employer/worker registration, each worker's coverage and scheme, actual current assessment/contribution schedule, underlying contributory-wage instrument and applicable table, scheme phase and commencement/transition rule, employer/employee allocation, prior declarations, payment receipts and any notice. Confirm registration immediately from the applicable instrument rather than assume that a small employer is exempt. Worker pension coverage/age and new-hire procedures require their own conditions; scheme phases do not automatically restart with each worker's tenure.

## The method, step by step

1. **Establish the salary-tax population.** Apply all residence limbs and the employment test, not a bank descriptor. Residence includes more than 182 days in a 12-month period ending in the current tax year; Prakas575 art 5 counts any part of a day as a full day and aggregates stays. Art 4 has a 2-of-4 employment-condition test. Refer uncertain residence, treaties and foreign-credit claims with the underlying facts. [Law arts 41-42](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e); [Prakas575 arts 3-5](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/fb78dfde-8342-4e3c-80e0-84ef81919c70).
2. **Build the resident base.** Separate fringe benefits, apply confirmed salary exemptions, deduct mandatory withholding required by labour/social-security law under Law art 45, then evidenced resident dependent relief. Never insert the old NSSF maximum as that deduction. The income-tax skill sets out the KHR 150,000 monthly spouse/child rules and age/proof/transition conditions. Where both spouses work, only one receives child relief; do not split different children between them. A repayment/advance needs its separate Law art 46 schedule. [Law arts 44-47](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e); [SD48 art 3](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/1f25fa42-ed6e-4757-a15f-94ec109aae35); [Prakas575 arts 8,12-14](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/fb78dfde-8342-4e3c-80e0-84ef81919c70).
3. **Apply the proper tax.** Use resident marginal tranches or the non-resident final 20% as appropriate. Compute fringe tax separately at 20% only after nature, exemptions and inclusive fair-market value are established. Necessary business transport/accommodation/meals provided to all staff regardless of role are excluded under Prakas575 art 16. Do not tax an unexplained payment automatically or infer the contractual cash allocation from the statutory employer payment obligation. [Law arts 47-49](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e); [Prakas575 arts 14-18](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/fb78dfde-8342-4e3c-80e0-84ef81919c70).
4. **Establish social contributions separately.** A current NSSF calculation requires the operative coverage, wage table, rate/share and transition instruments, followed by reconciliation to the actual assessment. The complete current table/transition has not been recovered; stop that assessment rather than substitute a historical floor/cap or infer all intermediate bands from endpoints. Documented contribution amounts may be inputs to a bounded salary/cash reconciliation; this does not validate the assessment that produced them. Employer-only costs must remain employer costs, not employee deductions.
5. **Reconcile cash and employer costs.** Cash paid equals gross cash less employee salary tax and actual lawful employee deductions; avoid double deduction. Employer cost adds actual employer contributions, benefit expense and tax actually borne by the employer to gross cash. A benefit's tax valuation need not equal the actual expense; record both separately. Distinguish a complete cost from a subtotal that excludes unresolved contributions. Reconcile liability payments to the payroll register, return and receipts. Under Law arts 51-53/Prakas575 arts 21-22 retain worker identity, salary, benefits, adjustment evidence and withholding records, with required employee/GDT reporting. [Law arts 51-53](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e); [Prakas575 arts 21-22](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/fb78dfde-8342-4e3c-80e0-84ef81919c70).
6. **Separate calendars.** The salary-tax statutory 20th does not establish NSSF payment or declaration deadlines. The GDT calendar actually read on 14 November 2026 shows October 2026 manual returns on 20 November and online returns on 25 November; do not extrapolate that extension. Confirm the actual NSSF payment/reporting notice separately before filing. [Law art 53](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e); [GDT calendar](https://www.tax.gov.kh/en/).

## Boundary and exception table

| Issue | Required action |
|---|---|
| Current NSSF floor, cap, intermediate brackets or November transition missing | Hold the contribution assessment; obtain full operative instruments and current schedule. Do not reuse the old ceiling. |
| Risk / health / pension employer-employee split or phase unknown | Hold allocation; require the actual lawful share and phase, not an assumed individual-tenure phase. |
| Registration or new worker unclear | Confirm actual current employer/worker obligations and deadlines; do not infer exemption from headcount. |
| Salary residence / dependent / benefit evidence missing | Hold the affected computation and identify the missing evidence. |
| Employee deduction includes an employer-only cost | Remove it from the proposed employee deduction and reconcile the liability to the actual legal assessment. |
| Labour minimum wage, working time, leave, work permits or sector allowances | Separate labour compliance review with current MLVT instruments; salary-tax bands do not answer these questions. |
| Filing box, currency or rounding rule unavailable | Obtain the actual current instruction; no invented field IDs or exchange rate. |

## Worked cases

These are hypothetical KHR inputs. The stated contribution/withholding amount is an independently documented scenario input, not a current NSSF maximum or rate calculation. Source tax rules: [Law arts 45-49](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e), [SD48 art 3](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/1f25fa42-ed6e-4757-a15f-94ec109aae35) and [Prakas575 arts 14-18](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/fb78dfde-8342-4e3c-80e0-84ef81919c70).

### Resident salary and cash reconciliation

Gross cash 6,000,000, no dependents, documented legally mandatory employee withholding 24,000: taxable base 5,976,000. Tax is 25,000 on the first taxed tranche plus 397,600 on the balance: 422,600. Cash pay is 5,553,400. If actual employer contributions documented for the scenario are 50,000, gross-cash-plus-contribution cost is 6,050,000 before any separate benefits. The 50,000 input is not derived from an asserted current rate.

```oa-check
name: Resident payroll cash and documented employer contribution
inputs:
  gross_cash: 6000000
  mandatory_employee_withholding: 24000
  documented_employer_contributions: 50000
steps:
  resident_base: gross_cash - mandatory_employee_withholding
  salary_tax: (2000000 - 1500000) * 0.05 + (resident_base - 2000000) * 0.10
  net_cash: gross_cash - mandatory_employee_withholding - salary_tax
  cost_before_benefits: gross_cash + documented_employer_contributions
expected:
  resident_base: 5976000
  salary_tax: 422600
  net_cash: 5553400
  cost_before_benefits: 6050000
```

### Non-resident salary and employer benefit subtotal

Confirmed Cambodian-source taxable cash salary 8,000,000 gives final tax 1,600,000 and cash 6,400,000 **before separately assessed employee deductions**. Confirmed taxable private housing at inclusive fair-market value 2,000,000, with no exemption, creates 400,000 fringe tax; the scenario assumes the employer pays and bears it and that actual housing expense equals the stated valuation. Salary plus housing plus fringe tax is a 10,400,000 employer subtotal **excluding unresolved employer social contributions**. It is not the employee's cash pay or a complete statutory contribution computation.

```oa-check
name: Nonresident cash and separate employer-benefit subtotal
inputs:
  taxable_salary: 8000000
  taxable_private_housing: 2000000
steps:
  final_salary_tax: taxable_salary * 0.20
  cash_before_other_deductions: taxable_salary - final_salary_tax
  employer_fringe_tax: taxable_private_housing * 0.20
  employer_subtotal_before_social: taxable_salary + taxable_private_housing + employer_fringe_tax
expected:
  final_salary_tax: 1600000
  cash_before_other_deductions: 6400000
  employer_fringe_tax: 400000
  employer_subtotal_before_social: 10400000
```

## When to refuse or refer

Refuse to label payroll complete when the NSSF assessment, worker coverage, contribution allocation or period rules remain unconfirmed. Refer cross-border residence/treaty/foreign-credit, contested benefits, employment status and enforcement matters with their documents. Produce a pending reconciliation and missing-evidence list; do not file or sign off from the two illustrations.

## Sources

| Source | Official URL | Read for / actual date |
|---|---|---|
| 2023 Law on Taxation, original Khmer salary pages 20-24, full corresponding English reference passages read separately | https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e | Salary scope/base/art45withholding, nonresident, benefits, employer/employee obligations;2026-11-15(original) |
| SD48, original Khmer pages 2-3, full salary and annual tables/population/abrogation | https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/1f25fa42-ed6e-4757-a15f-94ec109aae35 | Salary marginal bands art3;2026-11-14, page2re-read2026-11-15 |
| Prakas575, all 10 original Khmer pages visually read | https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/fb78dfde-8342-4e3c-80e0-84ef81919c70 | Employment/residence/exemptions/base/dependents/benefits/records/calendar;2026-11-15 |
| GDT calendar | https://www.tax.gov.kh/en/ | Actual October2026manual/online deadlines;2026-11-14 |
| NCDD government-library catalogue, Prakas449 metadata only | https://library.ncdd.gov.kh/detail/12321?lang=en | Original instrument identified; PDFdownload403, no operative rate/annex reading claimed from catalogue;2026-11-15 |

Access provenance: the [English reference Law translation](https://embindpp.gov.in/pdf/menu/Tax-Law-Cambodia-2023.pdf) is unofficial, hosted by the Embassy of India in Phnom Penh; its corresponding salary clauses were read 14 November 2026 and original Khmer was visually read 15 November. NSSF URLs for [Prakas168](https://www.nssf.gov.kh/wp-content/uploads/2023/02/16.Prakas-168.pdf), [SD144](https://www.nssf.gov.kh/wp-content/uploads/2023/02/11.-Sub_Decree_144_Determination_of_Contributory_Salary_or-1.pdf) and [SD32](https://www.nssf.gov.kh/wp-content/uploads/2023/02/9.-Sub_Decree_No_32_on_Pension_Scheme_for_Persons_Defined_by_the_Provisions_of-_the_Labour_Law-1.pdf) returned Rejected Request HTML on 15 November. A rejected response is not an operative document. Earlier read English pension/reference material is not asserted to validate current 2026 transitions.

Not yet confirmed: full current NSSF coverage/registration/new-hire rules and deadlines, current contributory-wage floor/cap/intermediate table, operative current rates/shares/phase/start and late-2026 transition, payment versus declaration deadlines, current sector wage/labour rules, FX/rounding and filing box instructions. Reported Prakas234/26 and Notification3135/26 were discovery leads only; full official instruments were not recovered. No current contribution result is supplied until these are read.

Historical old-skill topics retained for audit, excluded from current instructions: risk 0.8% employer; health 2.6% employer; pension first-phase total 4% split 2%/2%; old KHR400,000minimum and KHR1,200,000maximum; employer risk+health 3.4% and with pension 5.4%; NSSF payment15th and at-least-one-worker registration assertion. These are not confirmed as a complete current 2026 assessment by an accessible operative instrument. Neither a rejected page nor a source catalogue proves their present application.

Built from the law. Written by Codex. Not reviewed by an accountant.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-15. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `kh-payroll-social` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/kh-payroll-social. If neither is available, confirm every figure against the official source pages cited above before relying on it.
