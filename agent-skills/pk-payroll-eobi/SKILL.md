---
name: pk-payroll-eobi
description: "Use for pakistan integrated payroll and social-contribution run. Read the stated period, eligibility conditions, evidence requirements, owner skills and unresolved boundaries before calculating or preparing a return."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/pk-payroll-eobi"
  jurisdiction: "PK"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Pakistan integrated payroll and social-contribution run v1.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

End-to-end payroll working papers for Pakistan employers in 2026: salary income-tax withholding, EOBI, provincial employee social security and separate employer-side WWF/WPPF flags. Tax year 2026 salary tables apply to 1 July 2025-30 June 2026. `pk-income-tax` owns the salary table, `pk-payroll` its payment adjustment and `pk-social-contributions` coverage/base evidence. Never apply a tax-year 2026 table to a later payment without checking the later law.

Quick answer: determine gross taxable pay and annual tax forecast, separate employee deductions from employer costs, then reconcile each authority's remittance and reporting. Employer pension/social/welfare costs are not an employee withholding-tax credit.

## Rates, bands and thresholds

| Component and conditions | Confirmed rule/boundary | Official source |
|---|---|---|
| Salary withholding | A/B uses estimated Salary only as B, with tax plus applicable s.4AB in A; actual permitted adjustments apply. Enacted Finance Act 2024 amendment 22(b) and current s.149(2) put s.4AB in A; the 2025 consolidation misprints it in B. Other-head income does not switch employer withholding to business slabs; retain the actual period's salary table | [FA 2024 amendment 22(b)](https://download1.fbr.gov.pk/Docs/2024630146346801FinanceAct-2024.pdf); [current ITO s.149(2)](https://download1.fbr.gov.pk/Docs/2026724177725705IncomeTaxOrdinanace2001.pdf) |
| EOBI shares for insured workers | Current ministry description: employer 5%,employee 1%,total 6% of federal-notified minimum-wage base; numeric base still needed (contribution figures in words on the page) | [Ministry FAQ 5](https://ophrd.gov.pk/Detail/OGI0NzE3NGEtMzllOS00NjUwLTgzYjgtM2QwNzY4OGNkZWYy) |
| EOBI general threshold conflict | Current administrative reply says 10+ or notified establishments, voluntary smaller; consolidated s.1(4) prints 5 with Finance Act 2008 footnote, prior 12-month/continued-coverage rules The general 10-person threshold appears in words and numerals in the parliamentary reply; the consolidated 5-person and prior 12-month quantities are in words on the page. | [Parliament pp 48-49](https://na.gov.pk/uploads/documents/6ae817d42a069_262.pdf); [Act s.1(4)](https://pakistancode.gov.pk/pdffiles/administratorf3be1ec8d21dfebb9c5d1733f43cffe6.pdf) |
| Employer share | Cannot be recovered from employee wages | [Act s.9(3)](https://pakistancode.gov.pk/pdffiles/administratorf3be1ec8d21dfebb9c5d1733f43cffe6.pdf) |
| Quarterly withholding statements | Current s.165 schedule:20 April,20 July,20 October,20 January after respective quarters | [ITO s.165(2)](https://download1.fbr.gov.pk/Docs/2026724177725705IncomeTaxOrdinanace2001.pdf) |

## The base

1. Establish employer/employee identities, NTN/CNIC records, legal form, establishment/worker locations, actual headcount/history, employment terms, gross pay/perquisites, bonuses/arrears and year-to-date salary/deductions. Capture EOBI/provincial registrations and actual wage/base notices. An absent high-earner NTN needs registration analysis; do not invent a second identifier or a rejection rule.
2. Compute the period's estimated annual salary tax using `pk-payroll` and `pk-income-tax`, documenting previous/current pay, allowable credits and s.149 adjustments. Employer costs do not automatically reduce the employee's chargeable salary. Do not subtract an employee EOBI contribution from the salary-tax base merely because it is deducted from net pay.
3. Resolve EOBI applicability, previous/voluntary/notified cover and base. Do not automatically impose coverage at 5 employees from the old text or cancel cover after a fall in headcount. Apply the supported employer/employee shares per insured person; the ministry uses the federal-notified minimum wage, not the whole salary or a provincial wage substituted without authority. [Act ss.1,9/9 B; ministry FAQ 4-5](https://pakistancode.gov.pk/pdffiles/administratorf3be1ec8d21dfebb9c5d1733f43cffe6.pdf).
4. Test SESSI(Sindh),PESSI(Punjab),KPESSI(KP) or BESSI(Balochistan) using the specific law/coverage/continued-insurance/wage-ceiling/base/rate/date. Route by actual establishment and employment facts; domicile alone does not decide it. Medical, sickness, maternity, injury and death-benefit eligibility also needs the actual scheme conditions. Multiple-province branches need separate analysis; do not assume cross-province credits or insurance ends instantly when wages rise.
5. Keep provincial employer contributions separate from employee deductions, subject to the actual scheme. The old universal 6%-of-actual-wage formula and 40,000/37,000 ceilings are not confirmed for every province/period. Do not over-contribute on an assumption that a refund is harmless or guaranteed.
6. Flag WWF and WPPF as separate employer/profit-side obligations. Preserve federal/provincial jurisdiction, covered entity/industrial status, profit/base, worker-distribution ceilings and residual linkage questions. Do not deduct a supposed 2% WWF or 5% WPPF from an employee payslip or assume headcount 50 alone settles liability. Refer the operative law/period and corporate specialist analysis; this skill supplies no unverified universal computation.
7. Produce the gross-to-net payslip, employer-cost schedule, authority-by-authority payment/return calendar, source documents and year-end reconciliation. Reconcile employees and periods to payments/certificates, with unknown coverage/base amounts explicitly outstanding rather than zero.

## Deadlines and filing

For s.165 use the sourced quarterly schedule. Withholding-tax deposit, deduction certificate, EOBI registration/challan/insured-person schedule and provincial contribution/return dates are separate requirements. Obtain each operative calendar; the old 15th-of-month deposit and 31 July annual-reconciliation claims are not blanket rules. Act s.11 requires employer registration particulars within 30 days after applicability (in words on the page); actual applicability still requires the threshold conflict/notification analysis. [EOB Act ss.10-11](https://pakistancode.gov.pk/pdffiles/administratorf3be1ec8d21dfebb9c5d1733f43cffe6.pdf); [ITO s.165](https://download1.fbr.gov.pk/Docs/2026724177725705IncomeTaxOrdinanace2001.pdf).

Retain the employer's tax payment instructions/CPRs, EOBI challan and insured-person schedule (historically PR-03/PR-04, current form not confirmed), and provincial records separately. Annual sums must reconcile to actual monthly insured-person records, not simply current headcount multiplied across the whole year. Issue the actual required employee deduction certificate; do not promise a guessed Rule 42 date.


### Deposit, salary statement and certificate rules now sourced

Income Tax Rules 43 requires federal/provincial government deposit on the day of collection/deduction; other persons deposit within 7 days from each week ending Sunday, with nonresident overseas remittances paid before remitting abroad. There is no separate other-agent fortnight rule. Rule 44(5) requires the s.149 deductor's **annual salary statement by 31 July** after financial-year end, Part IX Second Schedule, separately from quarterly s.165 reporting. Rule 44(4) requires reconciliation when the Commissioner requires it, not a universal annual reconciliation automatically replacing that salary statement. The 7-day deposit period is in words on the page. [Rules 43/44](https://download1.fbr.gov.pk/Docs/20269211394336470IncomeTaxRules2002.pdf).

Rule 42's non-salary collection/deduction certificate uses Part VII Second Schedule within 15 days after financial-year end or business discontinuation; an earlier in-year request is answered within 7 days. Duplicate/lost-certificate and serial-number rules apply. This non-salary rule is not an employer salary-certificate deadline. Verify actual salary certificate entitlement/form under the operative law rather than revive omitted rule 41. The 15-day and 7-day periods are in words on the page. [r 42](https://download1.fbr.gov.pk/Docs/20269211394336470IncomeTaxRules2002.pdf).

## Penalties and interest

Failure to deduct/deposit is assessed under ITO ss.161/182/205 using the actual default period. EOBI/provincial late contribution has its own law and recovery provisions. The old claim that EOB Act s.12 automatically imposes personal director default liability is not supported by that section's employer-record inspection text. Refer default recovery, notices and liability disputes; no unsourced fixed penalty or surcharge is adopted.

## Cross-border points

Preserve specialist referrals for non-resident/split/home-country payroll, expatriates, treaties, foreign currency, stock options/RSUs, termination/gratuity/golden handshake, provident-fund recognition, backdated pay across tax years, directors' fees outside payroll and casual/piece-rate coverage. Joining/leaving/bonus adjustments and perquisite valuation under s.13 need actual full-year evidence and operative provisions; a foreign-currency salary uses s.71 conversion evidence. No blanket same-currency contractual rate override is given.


### Sindh coverage requires a separate test

The Sindh 2021 amendment adds self-employed workers to the employee definition and inserts s.20A: an employee other than one employed by an employer pays a fixed **PKR 1,500 monthly**, subject to prescribed conditions. The definition includes daily-wage, construction, home-based, transport, fisheries, agricultural, seasonal and shops/commercial-establishment workers. This is a separate provincial route; absence of employees does not establish absence of all social-security obligations. Obtain the implementing conditions and actual category/registration before charging a solo freelancer. The 1,500 amount is in words on the page. [2021 amendment ss.2-3](https://www.sessi.gov.pk/assets/files/content/2026/01/Sindh-Act-No.XIX-of-2021.pdf).

The 2018 amendment retains existing insurance when wages exceed the upper limit. It defines the lower wage limit by the prevailing Sindh minimum wage and the upper limit as that minimum plus **PKR 5,000**; the self-assessment scheme uses **6% of the lower limit** per secured employee. Read the actual scheme and s.20 provisos before choosing a base: these are not authority for a universal 6%-of-actual-pay rule. The current minimum-wage notification and applicability remain outstanding. The 5,000 amount and 6% contribution are in words on the page. [2018 amendment ss.4(ii),(vi),8-9,20](https://www.sessi.gov.pk/assets/files/content/2026/01/SINDH-EMPLOYEES-SOCIAL-SECURITY-AMENDMENT-ACT-2018.pdf).


### Other provincial contribution branches

KP Act 2021 s.20 requires employer 6% of wages for covered employees, capped by the minimum wage or s.12 determination, with no recovery of employer contribution from wages. Initial wage eligibility under s.2(k)(e) is 60% above the notified minimum, and existing secured employees continue despite a later increase. Thus eligibility ceiling and contribution base differ. Section 22 requires employer particulars within 60 days of applicability. Obtain actual current notification/establishment coverage before computing. [KP Act ss.2(k),20/22](https://kpcode.kp.gov.pk/uploads/THE_KHYBER_PAKHTUNKHWA_EMPLOYEES_SOCIAL_SECURITY_ACT_2021.pdf), read 2026-11-14; figures in words on the page are shown as numerals.

Balochistan Act 2022 s.20 uses employer 6% with upper-limit cap and prevailing-minimum-wage proviso; s.75 lower limit is the notified minimum, upper is minimum plus 15%. Section 21 self-assessment uses 6% of lower limit per secured employee and a separate 60 monthly employee share. Sindh's self-assessment employee share is 40 monthly under s.21(3), separate from conditional self-employed 1,500 and employer-share recovery prohibition. These province-specific branches replace the universal “no employee ESSI deduction” assumption; they do not establish current numerical wage notifications or every professional's coverage. [Balochistan Act ss.20/21/75](https://pabalochistan.gov.pk/storage/4287/2022-11-28_10_00_34_34dbd.pdf); [Sindh Act ss.20/21](https://www.sessi.gov.pk/assets/files/content/2026/01/Sindh-Employees-Social-Security-Act-2016-with-rules-and-ammendments.pdf), read 2026-11-14 for these provisions; worded figures shown as numerals.


### Sindh employer-profit funds: keep the actual coverage tests

Sindh WPPF scheme paragraph 1 covers industrial-undertaking companies meeting **any** of:100 workers at any time in Pakistan, paid-up capital≥2,000,000 or fixed assets at cost≥4,000,000. For companies established from 1 July 2006 the latter tests become 5,000,000 and 20,000,000; notified other companies can also be covered. Act s.3 requires 5% of profits to the Fund and audited accounts within 9 months after year-end, subject to adjustment and SRB extension up to 90 days. This is not a universal 50-worker rule or a deduction from employee pay. Verify statutory profit, worker distribution/categories/ceilings and residual transfer separately before finalising. [Sindh Companies Profits(Workers Participation)Act ss.2/3 and Scheme 1](https://www.srb.gos.pk/srb/wp-content/uploads/2020/07/ARM-6.pdf).

Sindh WWF Act s.5 covers industrial establishments located in Sindh with total income≥500,000 for the specified account periods, contribution 2%. Section 2(l)uses higher book profit/declared-return income where a return is required,4% of statement receipts in the stated non-return branch, and combines the applicable mixed branches. The ordinary payment date is the income-return due date; the nonfiler proviso uses provisional accounting profit before tax within 30 days of account close. Assessments/adjustments and particular covered-establishment definitions still matter. Do not assume every company or every freelancer is covered, or net WWF against WPPF without the actual linkage/distribution law. [Sindh WWF Act ss.2(l)/5](https://www.sindhlaws.gov.pk/DownloadDocument.aspx?Lang=EN&PubID=PUB-NEW-26-000098). Both sources read 2026-11-14 for these operative conditions; worded figures shown as numerals.

## Two worked examples that recompute

### Earlier Karachi fintech case, retained and corrected

The earlier Pakistani-citizen software developer, resident in Karachi (Sindh), at a Karachi fintech has CNIC/NTN, earns PKR 250,000 monthly, has no bonus/perquisites in the stated month, and works for an EOBI-registered employer with 35 staff. Assume the tax-year 2026 salary table, no other salary/benefits/credits, established EOBI insurance and **hypothetical verified base 40,000**. This 40,000 is not a current legal base claim. Provincial coverage/base is not established by the old 50,000 placeholder or by salary alone, so no provincial liability is certified here.

```oa-check
name: Karachi salary and separate EOBI shares
inputs:
  monthly_salary: 250000
  months: 12
  assumed_eobi_base: 40000
steps:
  - annual_salary: monthly_salary * months
  - annual_salary_tax: 116000 + (annual_salary - 2200000) * 0.23
  - monthly_salary_tax: annual_salary_tax / months
  - employee_eobi: assumed_eobi_base * 0.01
  - employer_eobi: assumed_eobi_base * 0.05
  - net_before_other_deductions: monthly_salary - monthly_salary_tax - employee_eobi
  - employer_cost_before_other_levies: monthly_salary + employer_eobi
expected:
  annual_salary: 3000000
  annual_salary_tax: 300000
  monthly_salary_tax: 25000
  employee_eobi: 400
  employer_eobi: 2000
  net_before_other_deductions: 224600
  employer_cost_before_other_levies: 252000
```

The old 217,963 net combined a stale 31,667 tax with a 370 deduction despite its 400 calculation. The corrected conditional net is 224,600; the actual payroll still needs the real base and full employee facts. A worker paid 40,000 also needs actual provincial insurance/rate evidence before adopting the earlier 2,400 social-security amount.

```oa-check
name: Authority remittance reconciliation
inputs:
  supported_salary_tax: 25000
  supported_employee_eobi: 400
  supported_employer_eobi: 2000
  fbr_paid: 24000
  eobi_paid: 2400
steps:
  - eobi_due: supported_employee_eobi + supported_employer_eobi
  - fbr_shortfall: supported_salary_tax - fbr_paid
  - eobi_difference: eobi_paid - eobi_due
  - combined_supported_due: supported_salary_tax + eobi_due
expected:
  eobi_due: 2400
  fbr_shortfall: 1000
  eobi_difference: 0
  combined_supported_due: 27400
```

Do not net the 1,000 FBR shortfall against an unrelated authority or recover employer cost from employees.

## Ask the client first

Obtain every input listed in the method and actual authority notices/payments/returns. Refuse final payroll without the applicable tax year, salary forecast, insured-worker decision/base and necessary identifiers. For an uncertain contribution keep a pending item; do not invent a higher rate or declare no liability. A solo freelancer's later hires trigger the full coverage assessment. WWF/WPPF, multi-province and default questions go to the relevant specialist before finalisation.

## Sources





| Source and actual portions read | Official URL | Read on |
|---|---|---|
| Read for Sindh WWF s.2(l)/5 and WPPF s.2/3/Scheme 1 coverage/contribution/payment branches on 2026-11-14 | https://www.sindhlaws.gov.pk/DownloadDocument.aspx?Lang=EN&PubID=PUB-NEW-26-000098; https://www.srb.gos.pk/srb/wp-content/uploads/2020/07/ARM-6.pdf | 2026-11-14 |
| Read for KP Act ss.2(k)(e),20/22, Balochistan Act ss.20/21/75 and Sindh compilation contribution ss.20/21 on 2026-11-14 | https://kpcode.kp.gov.pk/uploads/THE_KHYBER_PAKHTUNKHWA_EMPLOYEES_SOCIAL_SECURITY_ACT_2021.pdf; https://pabalochistan.gov.pk/storage/4287/2022-11-28_10_00_34_34dbd.pdf; https://www.sessi.gov.pk/assets/files/content/2026/01/Sindh-Employees-Social-Security-Act-2016-with-rules-and-ammendments.pdf | 2026-11-14 |
| Read for Income Tax Rules 42-44 operative payment, non-salary certificate, annual salary statement and requested reconciliation branches on 2026-11-14 | https://download1.fbr.gov.pk/Docs/20269211394336470IncomeTaxRules2002.pdf | 2026-11-14 |
| Read for Sindh 2021 amendment ss.2-3 definitions and fixed self-employed contribution subject to conditions | https://www.sessi.gov.pk/assets/files/content/2026/01/Sindh-Act-No.XIX-of-2021.pdf | 2026-11-14 |
| Read for Sindh 2018 amendment ss.4(ii),(vi),8-9,20 continued insurance, limits, self-assessment and s.20 provisos | https://www.sessi.gov.pk/assets/files/content/2026/01/SINDH-EMPLOYEES-SOCIAL-SECURITY-AMENDMENT-ACT-2018.pdf | 2026-11-14 |
| Read for ITO s.149 salary average/adjustments and First Schedule tax-year 2026 salary table; s.71 conversion | https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf | 2026-11-14 |
| Read for enacted Finance Act 2024 amendment 22(b) and current 2026 s.149(1)-(2), resolving the 2025 consolidation A/B editorial error without adopting later salary bands | https://download1.fbr.gov.pk/Docs/2024630146346801FinanceAct-2024.pdf; https://download1.fbr.gov.pk/Docs/2026724177725705IncomeTaxOrdinanace2001.pdf | 2026-11-15 |
| Read for current 2026 ITO s.165 statement cadence/schedule | https://download1.fbr.gov.pk/Docs/2026724177725705IncomeTaxOrdinanace2001.pdf | 2026-11-14 |
| Read for EOB Act ss.1(4),9/9 B,10-12, coverage/registration/employer-share and inspection text, with Finance Act 2008 footnote conflict | https://pakistancode.gov.pk/pdffiles/administratorf3be1ec8d21dfebb9c5d1733f43cffe6.pdf | 2026-11-14 |
| Read for ministry FAQ 4-5 current administrative threshold and contribution-base/split description | https://ophrd.gov.pk/Detail/OGI0NzE3NGEtMzllOS00NjUwLTgzYjgtM2QwNzY4OGNkZWYy | 2026-11-14 |
| Read for parliamentary reply pp 48-49 current 10-person/notified/voluntary coverage description | https://na.gov.pk/uploads/documents/6ae817d42a069_262.pdf | 2026-11-14 |

Not yet confirmed: the old blanket post-devolution nationwide mandatory/judicial-history assertion beyond the read administrative sources; also, judicial resolution of 5/10-person threshold conflict, actual numeric EOBI base and its current challan/contribution calendar, current numeric wage notifications, Punjab operative law, actual establishment coverage and contribution-return calendars beyond the read branches, federal/other-province WWF/WPPF and Sindh worker distribution/residual/credit law beyond the read coverage/contribution branches. Old 40,000/37,000/50,000 placeholders, generic 6% provincial rule,the universal 50-worker assertion is wrong; federal/other-province 2% WWF/5% WPPF/9-month and specific distribution assertions remain unconfirmed, not deleted topics or usable instructions. No professional approval is claimed.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `pk-payroll-eobi` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/pk-payroll-eobi. If neither is available, confirm every figure against the official source pages cited above before relying on it.
