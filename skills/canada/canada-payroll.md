---
name: canada-payroll
description: >
  Run and reconcile Canadian employee payroll for 2026: determine province
  of employment, collect TD1 declarations, calculate income tax and CPP/EI,
  track annual limits and employer contributions, prepare pay statements,
  remit source deductions, file T4/T4A returns and issue Records of Employment.
  Includes effective-dated general minimum wages and selected provincial
  overtime, vacation and illness rules, with a separate Quebec payroll overlay.
  Use for Canadian payroll, CPP2, EI, TD1, PD7A, remitter type, T4, ROE,
  vacation pay and final pay. Self-employed annual CPP/EI uses ca-fed-cpp-ei.
version: 1.1
jurisdiction: CA
tax_year: 2026
last_updated: 2026-11-13
depends_on:
  - payroll-workflow-base
category: payroll
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: payroll
type: computation
---

# Canada employee payroll v1.1

## Scope

Prepare a 2026 Canadian payroll working paper, employee pay statements, proposed journals, remittance schedule and year-end reconciliation. Use CAD and actual pay dates. This revision is **Built from the law** and **Not yet approved**; an old approval does not approve this changed version. Do not submit returns, pay staff or authorities, or post journals without the authorized person's sign-off.

Federal payroll tax rules apply alongside the applicable employment standards. A CRA province-of-employment decision does not decide which labour law governs. Determine federal versus provincial employment jurisdiction separately. Use [qc-employer-contributions](quebec/qc-employer-contributions.md) for Quebec income-tax/QPP/QPIP/HSF/CNESST coordination and [ca-fed-cpp-ei](ca-fed-cpp-ei.md) for an individual's annual self-employed calculation. Never apply self-employed two-share rates to an employee's pay. [Payroll responsibilities](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4001/employers-guide-payroll-deductions-remittances.html); [province of employment](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/set-up-new-employee/determine-province-employment.html).

**Use the pay-date edition.** CRA has January and July 2026 withholding formulas. The July update changes BC, Newfoundland and Labrador and PEI; a correct annual provincial tax rate may still be the wrong rate for a July payroll. Income tax is not gross pay multiplied by an approximate combined top marginal rate. [January formulas](https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4127-payroll-deductions-formulas/t4127-jan/t4127-jan-payroll-deductions-formulas-computer-programs.html); [July update](https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4127-payroll-deductions-formulas/t4127-jul/t4127-jul-payroll-deductions-formulas.html).

## Ask the client first

- What are the pay dates, frequency and actual number of periods, employee start/leaving dates, remuneration and taxable benefits? Obtain approved time, overtime, commissions, bonuses, leave, vacation balances and reimbursements.
- Which legal employer/account pays, and where does each worker report or attach under a full-time remote-work agreement? Establish employee/contractor status, employment-standards jurisdiction and foreign duties separately.
- Obtain SIN information securely, current federal/provincial TD1 declarations, multiple-employer declarations, pension/benefit deductions and any CRA authorization to reduce withholding. Do not publish identity numbers.
- Obtain date of birth, CPP/QPP retirement/disability evidence, CPT30 or Quebec election and effective dates. Obtain this employer's year-to-date pensionable/insurable earnings and separate CPP/CPP2/EI totals, including any documented qualifying succession.
- Obtain CRA remitter assignment, payroll-account age, relevant monthly withholding and associated-company totals, compliance history, payment records and any Service Canada reduced-EI decision.
- Obtain service dates, contract/collective agreement, industry exemptions, employer health-tax/compensation-board registrations and rating notices. For final pay or leave, get the actual reason and eligibility documents; do not assume a generic week per year or paid sick-day entitlement.

## The method, step by step

### 1. Set up the employer, employee and tax province

Confirm the employer's business number and payroll RP account and CRA access for the authorized representative. Classify the worker from the relationship, not an invoice label. Record the province of employment and the supporting establishment/remote-work facts. CRA's administrative remote policy, effective January 1, 2024, can attach a qualifying full-time remote worker to an establishment; when no reporting/attachment applies, the paying establishment may govern. Home address alone does not choose payroll deductions. [Province-of-employment decision](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/set-up-new-employee/determine-province-employment.html).

Obtain the federal and relevant provincial/territorial TD1; Quebec uses its own provincial declaration through Revenu Quebec. Check multiple employers and credits already claimed. Apply CRA's missing-form instructions rather than inventing additional credits or a zero-tax setting. A TD1 changes income tax; it does not by itself exempt CPP/EI. [TD1 instructions](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/set-up-new-employee/filing-form-td1.html).

Separate cash wages, taxable non-cash benefits, expenses, bonuses, vacation, retiring allowances and termination pay. Pensionable, insurable and income-taxable bases can differ. Apply the relevant payment rule before using the rates. [Payment classification](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4001/employers-guide-payroll-deductions-remittances.html).

### 2. Calculate income-tax withholding using the correct edition

Use current payroll software, CRA's PDOC/T4032 or the applicable T4127 formulas with the exact pay date, frequency, TD1 amounts, pension/enhancement deductions and year-to-date facts. Reconcile federal and provincial/territorial deductions separately; Quebec provincial tax requires its Revenu Quebec method. [CRA withholding formulas](https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4127-payroll-deductions-formulas/t4127-jan/t4127-jan-payroll-deductions-formulas-computer-programs.html).

T4127's regular-pay method annualizes the relevant taxable pay after authorized adjustments, calculates federal tax and credits, calculates provincial tax including its own reductions/surtaxes/premiums, and converts back to the period. Bonuses and retroactive pay use their own method. Record the calculation inputs, edition and output; never substitute an estimated top marginal rate or treat gross salary as annual taxable income without adjustments. [January formulas, Chapter 4](https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4127-payroll-deductions-formulas/t4127-jan/t4127-jan-payroll-deductions-formulas-computer-programs.html).

| Federal annual reference, not a standalone pay-run formula | 2026 value | Official source |
|---|---|---|
| Tax bands and rates | Up to 58,523: 14%; to 117,045: 20.5%; to 181,440: 26%; to 258,482: 29%; above:33% | https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4127-payroll-deductions-formulas/t4127-jan/t4127-jan-payroll-deductions-formulas-computer-programs.html |
| Maximum / minimum federal BPA | 16,452 /14,829; phase-down between net-income measures 181,440 and 258,482 | https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4127-payroll-deductions-formulas/t4127-jan/t4127-jan-payroll-deductions-formulas-computer-programs.html |
| Federal BPA phase-down | 16,452 minus (NI minus 181,440) x 1,623/77,042, bounded by the maximum/minimum; use T4127's NI definition | https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4127-payroll-deductions-formulas/t4127-jan/t4127-jan-payroll-deductions-formulas-computer-programs.html |

For payroll from July, read the July changes with the unchanged January chapters. For example, BC's Option 1 first withholding rate is **6.14%** from July, while the annual first tax rate is **5.60%**; the catch-up must not be used as the annual return rate. Newfoundland and Labrador's BPA and PEI's high-income withholding also change. Use the published formulas, including the distinction between Options 1 and 2, rather than replacing one constant everywhere. [July 2026 changes](https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4127-payroll-deductions-formulas/t4127-jul/t4127-jul-payroll-deductions-formulas.html).

### 3. Calculate employee CPP/CPP2 and match the employer share

| Annual full-year CPP item | 2026 value | Official source |
|---|---|---|
| First ceiling / basic exemption | 74,600 /3,500 | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/payroll-deductions-contributions/canada-pension-plan-cpp/cpp-contribution-rates-maximums-exemptions.html |
| First-tier employee rate / employer rate | 5.95% /5.95%, each comprising 4.95% base plus 1% additional | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/payroll-deductions-contributions/canada-pension-plan-cpp/cpp-contribution-rates-maximums-exemptions.html |
| First-tier employee / employer annual maximum, each | 4,230.45 | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/payroll-deductions-contributions/canada-pension-plan-cpp/cpp-contribution-rates-maximums-exemptions.html |
| Second ceiling / second band | 85,000 /10,400 | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/calculating-deductions/making-deductions/second-additional-cpp-contribution-rates-maximums.html |
| CPP2 employee / employer rate, each | 4%; maximum 416 each | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/calculating-deductions/making-deductions/second-additional-cpp-contribution-rates-maximums.html |
| Published regular-period exemptions | 26 biweekly:134.61; 24 semi-monthly:145.83; 12 monthly:291.66; 52 weekly:67.30 | https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4127-payroll-deductions-formulas/t4127-jan/t4127-jan-payroll-deductions-formulas-computer-programs.html |

For ordinary periodic pay, apply the published period exemption to that period's pensionable remuneration, calculate first-tier CPP and limit it by this employer's remaining annual maximum. Track CPP2 separately using cumulative pensionable earnings above the first ceiling and its own remaining maximum. Do not charge CPP2 from the first pay merely because annual salary will exceed YMPE. Use the actual formula for bonuses, irregular payments, partial years or non-cash benefits. Use decimal half-up rounding to cents; do not round a generic annual exemption division instead of the published pay-period amount. [T4127, Chapter 6](https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4127-payroll-deductions-formulas/t4127-jan/t4127-jan-payroll-deductions-formulas-computer-programs.html).

Start deductions in the first pay dated after the month the employee turns 18; include the last pay dated in the month they turn 70. Stopping at 65 is not automatic: the employee must be 65 to under 70, receive a CPP/QPP retirement pension and make a valid CPT30 election. Stop/restart normally takes effect the following month. Disability changes depend on the Service Canada determination and require proration. Retain evidence and check both contribution limits; QPP has different age/election rules. [CPP start/stop rules](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/payroll-deductions-contributions/canada-pension-plan-cpp/starting-stopping-cpp-deductions.html).

A normal new employer does not inherit another employer's deductions. A qualifying successor may carry them forward only under the statutory succession conditions. Identify the transaction and records before deciding which year-to-date totals apply. [Succession rules](https://www.canada.ca/en/revenue-agency/services/tax/canada-pension-plan-cpp-employment-insurance-ei-rulings/cpp-ei-explained/employer-restructuring-succession-employers.html).

### 4. Calculate EI and the employer's actual rate

| Ordinary employee EI | 2026 value | Official source |
|---|---|---|
| Annual insurable earnings maximum | 68,900 | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/payroll-deductions-contributions/employment-insurance-ei/ei-premium-rates-maximums.html |
| Outside Quebec employee / annual maximum | 1.63% /1,123.07 | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/payroll-deductions-contributions/employment-insurance-ei/ei-premium-rates-maximums.html |
| Outside Quebec standard employer / annual maximum | 2.282% /1,572.30, based on 1.4 x employee premium | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/payroll-deductions-contributions/employment-insurance-ei/ei-premium-rates-maximums.html |
| Quebec employee / annual maximum | 1.30% /895.70 | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/payroll-deductions-contributions/employment-insurance-ei/ei-premium-rates-maximums.html |
| Quebec standard employer / annual maximum | 1.82% /1,253.98, based on 1.4 x employee premium | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/payroll-deductions-contributions/employment-insurance-ei/ei-premium-rates-maximums.html |

Calculate employee EI on the period's insurable remuneration, limited by the remaining annual maximum with this employer. No CPP-style basic exemption applies. Standard employer EI is 1.4 times the employee premium; retain the employer-rate decision and reconcile both sides. EI is not subject to CPP's age 18/70 limits. Confirm exempt employment separately. [CRA EI rates and calculation](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/payroll-deductions-contributions/employment-insurance-ei/ei-premium-rates-maximums.html).

A short-term disability plan does not itself authorize a lower rate. Use a reduced rate only after Service Canada's entitlement decision assigns it, and only for the employees covered. Keep uncovered employees separately. [Premium Reduction Program](https://www.canada.ca/en/employment-social-development/programs/ei/ei-list/ei-employers/premium-reduction-program.html). Return the employees' **5/12** share of savings during the reduction year or the first four months of the next year, using an accepted arrangement; retain the calculation and evidence. [Employer responsibilities](https://www.canada.ca/en/employment-social-development/programs/ei/ei-list/reports/reduction-program/responsibilities.html).

### 5. Add Quebec and other employer-only costs without merging their bases

Quebec payroll has QPP/QPP2 and QPIP alongside federal EI. The old 6.40% QPP and 0.494% QPIP employee figures were 2025, not 2026. Load the reviewed Quebec overlay for its current figures, remittances and RL-1 fields. Do not use CPP age limits, add QPIP to federal EI's base, or assume HSF and CNESST use the same wages. [qc-employer-contributions](quebec/qc-employer-contributions.md).

| Employer cost | Method and conditions | Official source |
|---|---|---|
| Ontario EHT | Use [on-eht](ontario/on-eht.md) with current official eligibility, associated-group allocation and part-year rules. A stated exemption is not available to every employer; do not deduct a monthly one-twelfth automatically. | https://www.ontario.ca/document/employer-health-tax-eht/tax-exemption |
| BC EHT | Use [bc-eht](british-columbia/bc-eht.md) and current official regular-employer notch/full-base formulas. Charity, associated-group and part-year treatment differ; do not describe a marginal rate as an effective rate. | https://www2.gov.bc.ca/gov/content/taxes/employer-health-tax/employer-health-tax-overview |
| Manitoba HE Levy | Regular full-year employer: exempt through 2.5 million; above 2.5 million through 5 million,4.3% of excess over 2.5 million; above 5 million,2.15% of all subject payroll. Associated employers share the exemption; part-year presence can prorate it. | https://www.gov.mb.ca/finance/taxation/taxes/payroll.html |
| Quebec HSF and other levies | Use the Quebec overlay's distinct rate-setting payroll, subject wages, exemptions, training and CNESST methods, not a universal percentage of gross wages. | https://www.revenuquebec.ca/en/businesses/source-deductions-and-employer-contributions/employers-principal-changes-for-2026/ |

Use each compensation board's registration, covered earnings, classification and current assessment notice. A generic office-worker range is not a rate determination. Keep employer CPP/EI, health taxes, workers' compensation, benefits and vacation liabilities separate in the cost reconciliation. Group health/dental/life plans are not a universal substitute for statutory entitlements; contracts, collective agreements and protected leave can create continuing obligations.

### 6. Check effective-dated employment standards before gross pay

The following are selected **general** rates/rules. Determine coverage, profession/industry exclusions, youth/tipped/special rates, agreements and the date worked first. Other provinces and territories require their own official standards. A payroll-tax province does not automatically establish labour-law jurisdiction.

| General minimum hourly wage | Rate and effective period relevant to 2026 | Official source |
|---|---|---|
| Federal sector | 18.15 from April 1, 2026; before that 17.75. Pay the higher applicable provincial rate where required. | https://www.canada.ca/en/services/jobs/workplace/federal-labour-standards/pay-deductions.html |
| Ontario | 17.60 through September 30, 2026;17.95 from October 1, 2026 | https://www.ontario.ca/document/your-guide-employment-standards-act-0/minimum-wage |
| BC | 17.85 through May 31, 2026;18.25 from June 1, 2026 | https://www2.gov.bc.ca/gov/content?id=C387B7BAA362419C99B991D825561C45 |
| Alberta | General rate 15.00; check student and occupation-specific rules | https://www.alberta.ca/minimum-wage |
| Quebec | 16.10 through April 30, 2026;16.60 from May 1, 2026; tipped workers have a distinct rate | [Decree 576-2026 sections 1/4, Gazette p1991](https://www.publicationsduquebec.gouv.qc.ca/fileadmin/gazette/pdf_encrypte/gaz_entiere/2615-F.pdf); [CNESST current wage](https://www.cnesst.gouv.qc.ca/en/working-conditions/wage-and-pay/wages) |
| Manitoba | 16.00 through September 30, 2026;16.40 from October 1, 2026 | [Official wage history](https://www.gov.mb.ca/labour/standards/history-min.html); [current fact sheet](https://www.gov.mb.ca/labour/standards/doc,minimum-wage,factsheet.html) |
| Saskatchewan | 15.35 through September 30, 2026;15.70 from October 1, 2026 | https://www.saskatchewan.ca/business/employment-standards/payment-of-wages-payroll-administration-benefits-and-time-sheets/minimum-wage-and-reporting-for-duty-pay ; https://www.saskatchewan.ca/government/news-and-media/2025/july/10/minimum-wage-set-to-increase-october-1 |

| Ordinary overtime, subject to exclusions | Rule | Official source |
|---|---|---|
| Federal | Standard 8 hours/day and 40/week, at least 1.5 x; take the greater daily/weekly overtime count. Holiday weeks and approved schedules can change the standard. | https://www.canada.ca/en/services/jobs/workplace/federal-labour-standards/work-hours.html |
| Ontario | Generally hours above 44/week at 1.5 x; no general daily 8-hour overtime rule. Check exemptions and averaging. | https://www.ontario.ca/document/your-guide-employment-standards-act-0/overtime-pay |
| BC | Above 8 through 12/day at 1.5 x, above 12 at 2 x; weekly above 40 at 1.5 x, with daily-overtime hours excluded from double counting. | https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/00_96113_01 |
| Alberta | Greater of daily hours above 8 and weekly hours above 44, at 1.5 x; a valid written banked-overtime arrangement has different time-off rules. | https://www.alberta.ca/overtime-hours-overtime-pay |
| Quebec | Generally above 40/week at 1.5 x; qualifying vacation/holiday hours count. Check exclusions and eligible time-bank agreement. | https://www.cnesst.gouv.qc.ca/en/working-conditions/wage-and-pay/wages/overtime |

| Annual vacation | General minimum | Official source |
|---|---|---|
| Federal | After 1 year:2 weeks/4%; after 5 consecutive years:3 weeks/6%; after 10: 4 weeks/8% | https://www.canada.ca/en/services/jobs/workplace/federal-labour-standards/vacations-holidays.html |
| Ontario | Under 5 years:2 weeks after the entitlement year and 4% pay;5 years or more:3 weeks/6%; use the proper entitlement/stub-year rules | https://www.ontario.ca/document/your-guide-employment-standards-act-0/vacation |
| BC | After 12 months:2 weeks; after 5 consecutive years:3 weeks; pay 4% after 5 days employment,6% after 5 years | https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/00_96113_01 |
| Alberta | Generally 2 weeks after each of first 4 years,3 weeks after 5; non-monthly employees 4%/6%; monthly-salary method differs | https://www.alberta.ca/vacation-pay |
| Quebec | Under 1 year:1 day per complete month, up to 2 weeks,4%;1 to under 3 years:2 weeks/4%;3 years or more:3 weeks/6% | https://www.cnesst.gouv.qc.ca/en/working-conditions/leave/annual-vacation |
| Saskatchewan |3 weeks, then 4 weeks after 10 years; calculate exact 3/52 or 4/52 of eligible wages rather than truncated 5.77%/7.69% | https://www.saskatchewan.ca/business/employment-standards/vacations-and-vacation-pay/annual-vacation-and-vacation-pay/calculating-and-paying-vacation-pay |

Choose the legally permitted vacation payment timing; paying an allowance every cheque does not automatically extinguish the right to vacation time. Do not add a second vacation payout where it was already paid correctly. Determine the wage base separately by province and include any required vacation-on-vacation treatment. [Vacation rules](https://www.canada.ca/en/services/jobs/workplace/federal-labour-standards/vacations-holidays.html); [Alberta distinctions](https://www.alberta.ca/vacation-pay).

Federal employees have **ten general holidays**, not nine. Apply eligibility, holiday-pay base, work-on-holiday and substitute-day rules under the actual jurisdiction; there is no universal Canadian 1.5 x-only holiday formula. Federal ordinary holiday pay is generally 1/20 of wages excluding overtime in the preceding four-week period, with special rules for commission-based and other categories. [Federal holidays](https://www.canada.ca/en/services/jobs/workplace/federal-labour-standards/vacations-holidays.html).

| Illness leave | Current general entitlement and conditions | Official source |
|---|---|---|
| Federal | Paid medical leave accrues:3 days after 30 days continuous employment, then 1 day per completed month as prescribed, up to 10 including carried-over days. Other unpaid protected medical leave is separate. | https://www.canada.ca/en/services/jobs/workplace/federal-labour-standards/leaves.html |
| Ontario |3 unpaid sick days per calendar year after 2 consecutive weeks; longer protected leaves and contractual paid benefits are separate | https://www.ontario.ca/laws/statute/00e41 |
| BC | After 90 consecutive days,5 paid and 3 unpaid days per calendar year for personal illness/injury; serious illness leave is separate | [ESA section 49.1](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/00_96113_01); [Regulation section 45.031](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/396_95); [paid leave guidance](https://www2.gov.bc.ca/gov/content/employment-business/employment-standards-advice/paid-sick-leave) |
| Quebec | Up to 26 weeks protected absence in 12 months; first 2 paid days after 3 months service if not already used for the shared eligible reasons. Not 24 unpaid days. | https://www.cnesst.gouv.qc.ca/en/working-conditions/leave/accidents-and-illnesses/non-work-related-accident-or-illness |
| Alberta |5 unpaid personal/family responsibility days after 90 days; eligible long-term illness/injury leave up to 27 weeks under current rules, not 16 unpaid days | https://www.alberta.ca/personal-family-responsibility-leave ; https://www.alberta.ca/long-term-illness-injury-leave |

Separate job-protected maternity/parental leave from EI benefit payments. For 2026 EI benefits: maternity up to 15 weeks at 55%, maximum 729/week; standard parental up to 40 shared weeks, no more than 35 for one parent, at 55%/729; extended up to 69 shared, no more than 61 for one parent, at 33%/437. Quebec's maternity/parental benefits use QPIP. Assess benefit eligibility separately from payroll leave and any agreed top-up. [Service Canada](https://www.canada.ca/en/services/benefits/ei/ei-maternity-parental.html).

The usual EI waiting week is waived for new claims starting March 30,2025 through October 9, 2027, with a stated SUB-plan choice exception. Do not present the waiver as permanent or use an expired end date. Current separation-earnings measures can also affect benefits; this does not change the employer's statutory final-pay liability. [Current temporary measures](https://www.canada.ca/en/services/benefits/ei/temporary-measures-for-major-economic-conditions.html).

### 7. Produce the pay statement and proposed journal

Calculate gross cash pay and taxable non-cash benefits separately. Subtract employee CPP/CPP2 or QPP/QPIP, EI, federal/provincial income tax and lawful employee deductions to reconcile cash net pay. Employer contributions are employer costs, not extra employee deductions. Explain any rounding and year-to-date adjustment.

Give a pay statement for each payment with the required jurisdiction-specific fields: employer/employee identity, period/pay date, regular/overtime hours and rates where required, earnings/benefit details, each deduction and net amount. Quebec also requires its relevant tips, allowances and other particulars. A generic payslip checklist is not proof of compliance everywhere. [Quebec pay slip](https://www.cnesst.gouv.qc.ca/en/working-conditions/wage-and-pay/pay/pay-slip); [BC ESA section 27](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/00_96113_01).

Prepare a balanced journal/import file with wage and employer-cost expenses, employee deductions payable, employer contributions payable, vacation/benefit liabilities and cash/net-pay control. Tie the payroll register to the bank file, remittance totals and employee records. This is proposed work for human approval; do not post to a read-only ledger. Use [canada-bookkeeping](canada-bookkeeping.md) for the accounting workflow and [canada-gst-hst](canada-gst-hst.md) for benefit-related GST/HST; wages and taxable benefit GST/HST are not interchangeable.

For a sole proprietor or partnership, carry eligible gross employee wages and the employer's CPP/QPP, EI, QPIP and workers' compensation contributions into the business-expense working paper, supported by payroll records, without deducting the employee share a second time. Do not treat an owner's or partner's own drawings as wages. Follow [ca-fed-t2125](ca-fed-t2125.md) for the business return and [CRA line 9060](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/report-business-income-expenses/completing-form-t2125/line-9060-salaries-wages-benefits-including-employer-s-contributions.html) for the covered expenses and exclusions. A corporation uses its own return and expense classification; this payroll method does not determine deductibility of every employer levy.

## Boundary and exception table

| Situation | Required treatment |
|---|---|
| Employee or contractor disputed | Obtain relationship facts and a CRA ruling if necessary. Do not deduct or omit contributions solely because an invoice says contractor. |
| Remote, travelling or foreign employee | Document payroll tax province and labour coverage separately. Non-resident Canadian work can still require withholding despite an expected treaty exemption; use the actual CRA waiver/certification and separately check CPP/EI coverage. [CRA non-resident employees](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/payroll-deductions-contributions/income-tax/non-resident-employees-who-perform-services-canada.html). |
| New employer or business acquisition | Restart ordinary deductions; use succession carryforward only with qualifying evidence. Do not carry another employer's totals automatically. |
| Partial-year age, pension or disability | Use actual dated eligibility and prorated contribution maxima; do not apply the ordinary full-year limits blindly. |
| Quebec | Load the Quebec overlay for QPP/QPIP/income tax/HSF/CNESST. Federal EI remains separately due at the applicable rate. |
| Benefits, allowances, bonuses or termination | Identify taxable/pensionable/insurable treatment by payment type before calculating; non-cash benefits and retiring allowances do not all follow salary rules. |
| Health-tax exemption, associated group or compensation board | Obtain the employer's qualification, allocation, subject remuneration and assigned rate. Never guess an exempt status or a board rate. |
| Payroll correction | Notify the employee and follow CRA correction/amended-slip instructions; do not silently recover all past deductions from one pay. Preserve the original calculation and adjustment trail. |

## Worked cases

Fictional 2026 cases. These test the displayed contributions and decision points, not an unprovided full income-tax/net-pay result. Check the tax year, pay date, eligibility, correct employer and current software output before using a result.

### Case 1. Regular biweekly Ontario pay

A full-year CPP-eligible employee receives regular pensionable/insurable cash pay of 2,884.62, with no annual cap close and no CPP2 band reached yet. Use the published 26-period exemption 134.61. Employee CPP is 163.63, EI 47.02; standard employer CPP 163.63 and EI 65.83. Income tax must still be calculated from the employee's TD1 and the current tables. Annual salary 75,000 does not create CPP2 on the first payment.

```oa-check
name: 2026 regular Ontario biweekly contribution components
inputs:
  gross: 2884.62
  cpp_exemption: 134.61
steps:
  - employee_cpp: round(max(0, gross - cpp_exemption) * 0.0595, 2)
  - employee_ei: round(gross * 0.0163, 2)
  - employer_cpp: employee_cpp
  - employer_ei: round(employee_ei * 1.4, 2)
  - employee_contributions: employee_cpp + employee_ei
  - employer_contributions: employer_cpp + employer_ei
expected:
  employee_cpp: 163.63
  employee_ei: 47.02
  employer_cpp: 163.63
  employer_ei: 65.83
  employee_contributions: 210.65
  employer_contributions: 229.46
```

### Case 2. Annual ceilings and the Quebec EI decision

Compare ordinary full-year employee EI at the ceiling inside and outside Quebec, with no reduced employer rate. Quebec EI is 895.70, employer 1,253.98; outside Quebec 1,123.07 and 1,572.30. CPP outside Quebec reaches 4,230.45 plus 416 CPP2 only when eligible pensionable earnings reach both ceilings. Quebec pension contributions need the separate overlay, not these CPP amounts.

```oa-check
name: 2026 annual CPP ceilings and regional EI comparison
inputs:
  ympe: 74600
  yampe: 85000
  mie: 68900
steps:
  - first_cpp: round((ympe - 3500) * 0.0595, 2)
  - second_cpp: round((yampe - ympe) * 0.04, 2)
  - total_cpp: first_cpp + second_cpp
  - non_quebec_ei: round(mie * 0.0163, 2)
  - quebec_ei: round(mie * 0.013, 2)
  - non_quebec_employer_ei: round(non_quebec_ei * 1.4, 2)
  - quebec_employer_ei: round(quebec_ei * 1.4, 2)
expected:
  first_cpp: 4230.45
  second_cpp: 416
  total_cpp: 4646.45
  non_quebec_ei: 1123.07
  quebec_ei: 895.70
  non_quebec_employer_ei: 1572.30
  quebec_employer_ei: 1253.98
```

### Case 3. Correct the 80,000 semi-monthly ceiling story

At regular rounded pay 3,333.33, cumulative gross after 11 periods is 36,666.63; it cannot have exceeded 74,600. After 22 payments it is 73,333.26 and after 23 it is 76,666.59. Track actual CPP withheld and remaining annual maxima: a gross-earnings crossing alone does not prove the exact first-tier deduction in that pay, especially with period exemptions and rounding. If final annual pensionable pay is exactly 80,000, annual CPP2 is 216, not 416. Reconcile the last payment if a salary is split into rounded periods.

```oa-check
name: 2026 semi-monthly gross crossing and second CPP band
inputs:
  period_pay: 3333.33
  annual_actual: 80000
steps:
  - after_11: period_pay * 11
  - after_22: period_pay * 22
  - after_23: period_pay * 23
  - annual_cpp2: round(max(0, min(annual_actual, 85000) - 74600) * 0.04, 2)
expected:
  after_11: 36666.63
  after_22: 73333.26
  after_23: 76666.59
  annual_cpp2: 216
```

### Case 4. Vacation pay depends on service and the wage base

Assume eligible annual wages 52,000 with no adjustment to the relevant legal base. Four percent gives 2,080; six percent 3,120; federal ten-year entitlement 8% gives 4,160. Saskatchewan uses the exact fractions:3,000 at 3/52, or 4,000 at 4/52. Select the legally applicable rate and payment timing rather than always paying 4%. This case does not settle eligibility or permit buying out vacation time.

```oa-check
name: 2026 vacation pay with verified eligible wage base
inputs:
  eligible_wages: 52000
steps:
  - four_percent: round(eligible_wages * 0.04, 2)
  - six_percent: round(eligible_wages * 0.06, 2)
  - eight_percent: round(eligible_wages * 0.08, 2)
  - sask_three_weeks: round(eligible_wages * 3 / 52, 2)
  - sask_four_weeks: round(eligible_wages * 4 / 52, 2)
expected:
  four_percent: 2080
  six_percent: 3120
  eight_percent: 4160
  sask_three_weeks: 3000
  sask_four_weeks: 4000
```

### Case 5. Final pay and the ROE are different jobs

An Ontario employee's final package must separately identify outstanding wages, accrued unpaid vacation, any overtime, pay in lieu of notice and statutory severance if eligible. The ordinary ESA notice bands, after the qualifying three-month service condition, are 1 week below 1 year,2 weeks from 1 to under 3 years,3 weeks from 3 to under 4, rising by service band to 8 weeks at 8 years or more. Exceptions, mass terminations, contracts and common-law entitlement need separate review. Do not default every Canadian employee to 1 week per year. [Ontario notice](https://www.ontario.ca/document/employment-standard-act-policy-and-interpretation-manual/part-xv-termination-and-severance-employment).

Ontario statutory severance is distinct: normally at least 5 years plus global employer payroll of at least 2.5 million, or the qualifying permanent-closure/50-employees-in-six-months branch. Include completed months and the statutory notice-period adjustment in service, cap at 26 weeks and check exemptions. Do not combine severance with notice or assume an Ontario-only payroll test. [Ontario severance](https://www.ontario.ca/document/your-guide-employment-standards-act-0/severance-pay).

Issue the ROE on its correct medium/pay-frequency deadline below, and choose the reason from facts. Code M is not an automatic code for every departure. Classify final payments for T4, income-tax and CPP/EI purposes separately. No numerical severance amount is given without the missing service/pay/eligibility facts.

## When to refuse or refer

Do not produce final net pay without the missing TD1, taxable-benefit, province, year-to-date or eligibility facts. Return the supported component and identify the unresolved input. Refer disputed employment status, foreign coverage, complex succession, exempt workers, non-standard pay, mass termination and contractual/common-law dismissal rights to the relevant practitioner. Do not invent current professional approval from an old credit line.

## Filing and payment

### CRA remittances

Read the assigned remitter type and notices. AMWA generally includes associated corporations and the relevant months requiring remittances, not a default division by 12. The ordinary regular/accelerated classification uses AMWA from the second preceding calendar year:2024 for 2026. A qualifying prior-year election under subsection 108(1.11) can permit slower remittance with the required notice; do not substitute 2025 automatically. [Income Tax Regulations 108](https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-108.html).

| Remitter | Eligibility/period | Due date | Official source |
|---|---|---|---|
| New small quarterly | Payroll account under 12 months, each month's withholding below 1,000 and perfect compliance | April 15, July 15, October 15, January 15 for the preceding quarter | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/remitting-source-deductions/how-when-remit-due-dates.html |
| Established small quarterly | Account at least 12 months, AMWA below 3,000 in either of the two preceding calendar years under ITR 108(1.12), with compliance conditions; obtain CRA notification | Same quarter dates | https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-108.html |
| Regular | AMWA below 25,000 unless entitled/assigned to quarterly |15th of following month | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/remitting-source-deductions/how-when-remit-due-dates.html |
| Accelerated threshold 1 | AMWA 25,000 to 99,999.99; remuneration days 1-15 and 16-month-end |25th same month and 10th next month, respectively | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/remitting-source-deductions/how-when-remit-due-dates.html |
| Accelerated threshold 2 | AMWA at least 100,000; periods end 7th,14th,21st, last day | Third working day after each period end | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/remitting-source-deductions/how-when-remit-due-dates.html |

CRA's current summary simplifies the established quarterly lookback to two years ago; ITR 108(1.12)(a), consistent with T4001, expressly allows either of the two prior years. For 2026, examine 2024 and 2025 and the compliance/notice conditions rather than rejecting a statutory route based only on 2024. Do not change an assigned schedule silently. [Enacted rule](https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-108.html).

Apply CRA's weekend/recognized-holiday receipt rule and appropriate payment method. Threshold 2 remitters must use the specified electronic/financial-institution route; payment initiation is not proof the correct payroll account was credited. Retain the RP account, period, payment reference and CRA confirmation, then reconcile the bank. Report nil remittances when required; ordinary cessation/final remittance is within 7 calendar days under the applicable special-event rule. [Due dates](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/remitting-source-deductions/how-when-remit-due-dates.html); [how to pay](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/remitting-source-deductions/how-when-remit-make-payment.html). Keep Revenu Quebec remittances separate under the Quebec overlay.

### T4/T4A and year-end reconciliation

The ordinary deadline for 2026 T4/T4A returns is **March 1, 2027**, applying the last-day-of-February/weekend rule. Deliver employee slips by the applicable deadline too. More than 5 slips of a type requires electronic filing. Use CRA Web Forms or Internet file transfer, with a return for each payroll account; a summary without slips is not a complete return. T4A is not a substitute for classifying a worker correctly. [Filing dates](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/file-information-returns-slip-summaries/when-to-file.html); [filing method](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/file-information-returns-slip-summaries/how-to-file.html); [T4 instructions](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4120/employers-guide-filing-t4-slip-summary.html).

Reconcile T4 employment income, CPP/CPP2, QPP/QPP2, EI, tax withheld and their earnings boxes to the register, remittances and general ledger; use the final applicable-year schema and employee benefit fields. Check discrepancies before submission. Keep the Quebec RL-1/summary stream separate. A business stopping operations, death, amalgamation or account closure can change the filing deadline; do not automatically wait until February. [Special filing situations](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/file-information-returns-slip-summaries/when-to-file.html).

### Record of Employment

| ROE medium and pay frequency | Ordinary issuing deadline after an interruption of earnings | Official source |
|---|---|---|
| Electronic, weekly/biweekly/semi-monthly | Within 5 calendar days after the end of the pay period containing the interruption | https://www.canada.ca/en/employment-social-development/programs/ei/ei-list/reports/roe-guide.html |
| Electronic, monthly or 13 periods/year | Earlier of 5 calendar days after that period end or 15 calendar days after the first interruption day | https://www.canada.ca/en/employment-social-development/programs/ei/ei-list/reports/roe-guide.html |
| Paper | Within 5 calendar days after the later of the first interruption day and the day the employer becomes aware of it | [EIR section 19(3)](https://laws-lois.justice.gc.ca/eng/regulations/SOR-96-332/section-19.html); [ROE guide](https://www.canada.ca/en/employment-social-development/programs/ei/ei-list/reports/roe-guide.html) |

Determine whether there is an interruption and whether a special rule applies. Enter actual insurable hours, earnings, pay-period details, final payments and reason in ROE Web or the applicable paper form; confirm submission. An electronic ROE does not require an employee paper copy; paper ROEs have separate distribution requirements. Preserve records and amend errors through the proper process. [ROE guide, Chapters 1-2](https://www.canada.ca/en/employment-social-development/programs/ei/ei-list/reports/roe-guide.html).

### Penalties, interest and records

| Failure | Applicable rule | Official source |
|---|---|---|
| Late remittance |3% for 1-3 days,5% for 4-5,7% for 6-7,10% after 7 days or no remittance; repeated knowing/grossly negligent failures can reach 20%. Under Income Tax Act subsection 227(9.1), the ordinary penalty applies only to the part of the total required remittance for that due date exceeding 500; this restriction does not apply to a knowing or grossly negligent delay or short remittance. This is not a permission to retain the first 500. | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/remitting-source-deductions/how-when-remit-due-dates.html); [Income Tax Act subsections 227(9)-(9.1)](https://www.lois.justice.gc.ca/PDF/I-3.3.pdf) |
| Failure to deduct | Potential 10% penalty,20% for qualifying repeat knowing/grossly negligent failures. Undeducted CPP/EI can leave the employer liable for both shares; income-tax recovery differs. | https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4001/employers-guide-payroll-deductions-remittances.html |
| Late T4/T4A | Statutory bands by slip count:1-50 slips 10/day, maximum 1,000;51-500 slips 15/day, maximum 1,500;501-2,500 slips 25/day, maximum 2,500;2,501-10,000 slips 50/day, maximum 5,000;10,001 or more slips 75/day, maximum 7,500. Up to 100 days, with minimum 100. Administrative small-filer treatment:1-5 slips 100 flat;6-10 slips 5/day, maximum 500, subject to minimum 100. | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/file-information-returns-slip-summaries/when-to-file.html |
| Wrong filing format | Separate electronic-filing penalty; e-filing threshold is more than 5 slips, not 50 | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/file-information-returns-slip-summaries/how-to-file.html |

CRA interest is compounded daily at its quarterly prescribed rate; obtain the rate for the actual overdue period and notice, including unpaid penalties. ROE duties arise under Employment Insurance Regulations section 19. Contravention can be an offence under Employment Insurance Act subsection 136(1). Where no other penalty applies, section 137 provides, on summary conviction, a fine from 100 to 2,000, imprisonment up to six months, or both. This is an offence/conviction route, not an automatic charge for every late ROE. [EIR section 19](https://laws-lois.justice.gc.ca/eng/regulations/SOR-96-332/section-19.html); [EIA sections 136-137](https://laws-lois.justice.gc.ca/eng/acts/E-5.6/FullText.html). [CRA remittance consequences](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/remitting-source-deductions/how-when-remit-due-dates.html).

Retain payroll/source records and approvals for the applicable retention period; CRA's ordinary rule is at least six years after the year concerned, with exceptions and other authorities' requirements checked separately. Preserve submission confirmations, correction history, benefit/election evidence and reconciliation. [Records](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4001/employers-guide-payroll-deductions-remittances.html).

## Completion checklist

- Evidence supports the employer, worker classification, payroll tax province, labour jurisdiction, pay-date edition and all input bases.
- Gross-to-net reconciles; CPP, CPP2, QPP, QPIP, EI and income tax are separate, with correct limits and employer costs.
- Effective wage, overtime, leave, vacation and final-pay rules match actual work dates, service and the governing law.
- RP and Quebec/board accounts, periods, due dates, filings and bank confirmations reconcile; a saved draft is not filed or paid.
- Proposed journals and submissions remain for authorized approval. The actual current skill label determines whether a named accountant approves this method.

## Sources

Read on **2026-11-13**. Use official effective dates, not only page dates. Ontario direct HTML often returned 403; the official indexed text and independently read official publication supplied the stated rules, as identified below. Current CRA T4001/RC 4120 publications still carry Rev 25 in parts;2026 rates and current pay-date formulas are sourced separately.

| ID and official source | Section/table read | Read on |
|---|---|---|
| P01: https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4127-payroll-deductions-formulas/t4127-jan/t4127-jan-payroll-deductions-formulas-computer-programs.html | Read for Chapters 2-8, federal annualization/BPA, CPP/EI formulas and Table 6.1 exemptions | 2026-11-13 |
| P02: https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4127-payroll-deductions-formulas/t4127-jul/t4127-jul-payroll-deductions-formulas.html | Read for July 2026 update, BC/NL/PEI pay-period adjustments and unchanged chapters | 2026-11-13 |
| P03: https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/payroll-deductions-contributions/canada-pension-plan-cpp/cpp-contribution-rates-maximums-exemptions.html | Read for 2026 annual first-tier table | 2026-11-13 |
| P04: https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/calculating-deductions/making-deductions/second-additional-cpp-contribution-rates-maximums.html | Read for 2026 second-tier table | 2026-11-13 |
| P05: https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/payroll-deductions-contributions/employment-insurance-ei/ei-premium-rates-maximums.html | Read for 2026 federal and Quebec employee/employer EI tables | 2026-11-13 |
| P06: https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/payroll-deductions-contributions/canada-pension-plan-cpp/starting-stopping-cpp-deductions.html | Read for age 18/70, disability and CPT30 timing | 2026-11-13 |
| P07: https://www.canada.ca/en/revenue-agency/services/tax/canada-pension-plan-cpp-employment-insurance-ei-rulings/cpp-ei-explained/employer-restructuring-succession-employers.html | Read for qualifying successor conditions and previous-employer contribution continuity | 2026-11-13 |
| P08: https://www.canada.ca/en/employment-social-development/programs/ei/ei-list/ei-employers/premium-reduction-program.html | Read for entitlement decision and individual assigned reduced rate | 2026-11-13 |
| P09: https://www.canada.ca/en/employment-social-development/programs/ei/ei-list/reports/reduction-program/responsibilities.html | Read for covered employees, savings 5/12 and return timing | 2026-11-13 |
| P10: https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/set-up-new-employee/determine-province-employment.html | Read for establishment, residence, remote-work attachment and 2024 policy | 2026-11-13 |
| P11: https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/set-up-new-employee/filing-form-td1.html | Read for federal/provincial TD1, multiple employers and missing declarations | 2026-11-13 |
| P12: https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4001/employers-guide-payroll-deductions-remittances.html | Read for payroll account, separate payment types, records and deduction failures; Rev 25 dated amounts not used as 2026 rates | 2026-11-13 |
| P13: https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/remitting-source-deductions/how-when-remit-due-dates.html | Read for remitter periods, due dates, nil/final remittance and late-remittance consequences | 2026-11-13 |
| P14: https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-108.html | Read for 108(1.1)-(1.4), statutory quarterly lookback and AMWA definition | 2026-11-13 |
| P15: https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/file-information-returns-slip-summaries/when-to-file.html | Read for T4/T4A ordinary and cessation dates, late filing and administrative penalty table | 2026-11-13 |
| P16: https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/file-information-returns-slip-summaries/how-to-file.html | Read for more-than-five-slips e-filing, account-level returns and format penalties | 2026-11-13 |
| P17: https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4120/employers-guide-filing-t4-slip-summary.html | Read for slip fields, employee delivery and correction; final 2026-specific schema to be checked before filing | 2026-11-13 |
| P18: https://www.canada.ca/en/employment-social-development/programs/ei/ei-list/reports/roe-guide.html | Read for Chapter 1 issuing deadlines, Chapter 2 blocks/reasons and records | 2026-11-13 |
| P19: https://www.canada.ca/en/services/jobs/workplace/federal-labour-standards/pay-deductions.html | Read for 2026 federal minimum wage, higher provincial wage and permitted deductions | 2026-11-13 |
| P21: https://www.ontario.ca/document/your-guide-employment-standards-act-0/minimum-wage | Read for indexed official Ontario 2026 general wage table; direct open 403, official search text read | 2026-11-13 |
| P22: https://www2.gov.bc.ca/gov/content?id=C387B7BAA362419C99B991D825561C45 | Read for BC general minimum wage effective June 1, 2026 | 2026-11-13 |
| P23: https://www.alberta.ca/minimum-wage | Read for Alberta general wage and special worker categories | 2026-11-13 |
| P24: https://www.gov.mb.ca/labour/standards/doc,minimum-wage,factsheet.html | Read for Manitoba 2026 general minimum wage and effective date | 2026-11-13 |
| P25: https://www.saskatchewan.ca/business/employment-standards/payment-of-wages-payroll-administration-benefits-and-time-sheets/minimum-wage-and-reporting-for-duty-pay | Read for Saskatchewan 2026 general minimum wage/effective date | 2026-11-13 |
| P26: https://www.canada.ca/en/services/jobs/workplace/federal-labour-standards/work-hours.html | Read for standard hours, overtime, holiday week and exceptions | 2026-11-13 |
| P27: https://www.ontario.ca/document/your-guide-employment-standards-act-0/overtime-pay | Read for official indexed Ontario 44-hour rule and exceptions | 2026-11-13 |
| P28: https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/00_96113_01 | Read for ESA sections 27,35,40,49.1,57-58; current to November 10, 2026 | 2026-11-13 |
| P29: https://www.alberta.ca/overtime-hours-overtime-pay | Read for 8/44 greater-of rule and written time-bank arrangements | 2026-11-13 |
| P30: https://www.cnesst.gouv.qc.ca/en/working-conditions/wage-and-pay/wages/overtime | Read for 40-hour rule, holiday/vacation hours, exclusions and banked overtime | 2026-11-13 |
| P31: https://www.canada.ca/en/services/jobs/workplace/federal-labour-standards/vacations-holidays.html | Read for vacation 2/3/4 weeks and 4/6/8%, ten general holidays and holiday-pay method | 2026-11-13 |
| P32: https://www.ontario.ca/document/your-guide-employment-standards-act-0/vacation | Read for official indexed vacation pay 4/6% and service threshold | 2026-11-13 |
| P33: https://www.alberta.ca/vacation-pay | Read for vacation 4/6% and monthly-salary distinction | 2026-11-13 |
| P34: https://www.cnesst.gouv.qc.ca/en/working-conditions/leave/annual-vacation | Read for Quebec reference year and 3-year vacation threshold | 2026-11-13 |
| P35: https://www.saskatchewan.ca/business/employment-standards/vacations-and-vacation-pay/annual-vacation-and-vacation-pay/calculating-and-paying-vacation-pay | Read for exact 3/52 and 4/52 vacation formulas | 2026-11-13 |
| P36: https://www.canada.ca/en/services/jobs/workplace/federal-labour-standards/leaves.html | Read for medical leave accrual and continued benefits conditions | 2026-11-13 |
| P37: https://www.ontario.ca/laws/statute/00e41 | Read for section 50 through official indexed current-law text: sick leave after two weeks, three unpaid days | 2026-11-13 |
| P38: https://www.cnesst.gouv.qc.ca/en/working-conditions/leave/accidents-and-illnesses/non-work-related-accident-or-illness | Read for 26 weeks protected leave and shared two paid days after three months | 2026-11-13 |
| P39: https://www.alberta.ca/personal-family-responsibility-leave | Read for five unpaid days after 90 days service | 2026-11-13 |
| P40: https://www.alberta.ca/long-term-illness-injury-leave | Read for current 27-week unpaid leave after 90 days service | 2026-11-13 |
| P41: https://www.canada.ca/en/services/benefits/ei/ei-maternity-parental.html | Read for maternity/standard/extended parental weeks, sharing and benefit rates | 2026-11-13 |
| P42: https://www.canada.ca/en/services/benefits/ei/temporary-measures-for-major-economic-conditions.html | Read for waiting-period waiver through October 9, 2027 and SUB-plan exception | 2026-11-13 |
| P43: https://www.cnesst.gouv.qc.ca/en/working-conditions/wage-and-pay/pay/pay-slip | Read for pay-slip fields | 2026-11-13 |
| P44: https://www.ontario.ca/document/employment-standard-act-policy-and-interpretation-manual/part-xv-termination-and-severance-employment | Read for section 57 statutory notice bands and PartXV exceptions through official indexed text | 2026-11-13 |
| P45: https://www.ontario.ca/document/your-guide-employment-standards-act-0/severance-pay | Read for global payroll/closure alternative, completed months and 26-week cap; independent reviewer opened official PDF/indexed text | 2026-11-13 |
| P46: https://www.ontario.ca/document/employer-health-tax-eht/tax-exemption | Read for official indexed exemption eligibility, group allocation and daily proration | 2026-11-13 |
| P47: https://www2.gov.bc.ca/gov/content/taxes/employer-health-tax/employer-health-tax-overview | Read for official indexed 2024-onward regular-employer exemption/notch/flat formulas | 2026-11-13 |
| P48: https://www.gov.mb.ca/finance/taxation/taxes/payroll.html | Read for Manitoba 2.5 m/5 m exemption/notch and associated-group/part-year rules | 2026-11-13 |
| P49: https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/payroll-deductions-contributions/income-tax/non-resident-employees-who-perform-services-canada.html | Read for Canadian-work withholding, certified non-resident employer/employee exception and waiver route | 2026-11-13 |
| P50: https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/remitting-source-deductions/how-when-remit-make-payment.html | Read for payment account/reference, threshold 2 method and received-date rules | 2026-11-13 |

| P51: https://www.saskatchewan.ca/government/news-and-media/2025/july/10/minimum-wage-set-to-increase-october-1 | Read for 15.35 effective October 1, 2025, retained into 2026 before the next increase | 2026-11-13 |

| P59: https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/396_95 | BC Employment Standards Regulation section 45.031 prescribes five paid illness/injury days | 2026-11-13 |
| P60: https://www2.gov.bc.ca/gov/content/employment-business/employment-standards-advice/paid-sick-leave | BC five paid plus three unpaid days after 90 days, read with ESA and regulation | 2026-11-13 |
| P61: https://www.lois.justice.gc.ca/PDF/I-3.3.pdf | Income Tax Act 227(9)-(9.1): late-remittance penalty bands and ordinary first-500 restriction; official indexed statutory text | 2026-11-13 |
| P62: https://www.cnesst.gouv.qc.ca/en/working-conditions/wage-and-pay/wages | Quebec general minimum wage 16.60 effective May 1,2026 | 2026-11-13 |
| P63: https://www.gov.mb.ca/labour/standards/history-min.html | Manitoba general wage history:16.00 October 1,2025;16.40 October 1,2026 | 2026-11-13 |
| P64: https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/report-business-income-expenses/completing-form-t2125/line-9060-salaries-wages-benefits-including-employer-s-contributions.html | T2125 line 9060 employer wages/contributions, supporting records and owner/partner exclusions | 2026-11-13 |
| P65: https://laws-lois.justice.gc.ca/eng/regulations/SOR-96-332/section-19.html | EIR19(3)-(3.1): paper later-of trigger, electronic frequency-specific earlier-of deadline; current to October 19,2026 | 2026-11-13 |

| P66: https://www.publicationsduquebec.gouv.qc.ca/fileadmin/gazette/pdf_encrypte/gaz_entiere/2615-F.pdf | Quebec Gazette April 15,2026,p1991 (PDF page55), decree576-2026 sections1/4:16.10 replaced by16.60 effective May1,2026 | 2026-11-13 |

| P67: https://laws-lois.justice.gc.ca/eng/acts/E-5.6/FullText.html | EIA136(1)/137: contravention offence and summary-conviction fine/imprisonment, no-other-penalty condition | 2026-11-13 |

**Not yet confirmed:** the federal minimum-wage database returned no usable table and is not evidence for a wage rate here; the provincial sources support the rates. This skill does not supply every province's complete employment-standards code, every board classification or a full tax-withholding engine. Use the applicable official calculator/formulas and employer documents for the actual run. Final 2026 T4-specific schema changes must be checked when filing. Complex non-standard employment, statutory exceptions and cross-border coverage are not made certain by these ordinary examples. Earlier unsourced wage ranges, approximate combined top tax rates, universal ROE timing, Quebec contribution figures and the fictitious period 11 ceiling claim have been replaced or expressly retired.
