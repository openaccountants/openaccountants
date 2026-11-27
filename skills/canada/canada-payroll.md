---
name: canada-payroll
description: Use this skill whenever asked about Canadian payroll, source deductions, CPP contributions, EI premiums, or employer obligations in Canada. Trigger on phrases like "source deductions", "CPP", "Canada Pension Plan", "CPP2", "EI", "employment insurance", "T4", "TD1", "payroll deductions", "CRA payroll", "remittance", "ROE", "record of employment", "statutory holiday pay", "vacation pay Canada", "minimum wage Canada", "provincial tax", "payroll Canada", "PD7A", "remitter type", or any question about running payroll in Canada. This skill covers federal rules; Quebec (QPP/QPIP) differences are noted but not fully detailed. ALWAYS read this skill before processing any Canadian payroll work.
version: 1.2
jurisdiction: CA
tax_year: 2026
tax_year_notes: Calendar 2026 payroll reference; dated wage changes and original examples retained. Individual eligibility and referred branches require separate resolution.
type: computation
last_updated: 2026-11-26
depends_on:
  - payroll-workflow-base
category: payroll
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
reviewed_by: "Nathan Wiebe"
reviewed_on: 2026-11-03
tier: 1
domain: payroll
---

# Canada Payroll

## Scope

A calendar-2026 Canadian payroll working reference in CAD. Determine coverage before using any table: a number alone does not establish an employee's entitlement or a payroll deduction. Referred points are non-usable for calculation until resolved; a referral does not mean zero liability or entitlement. This Guide does not submit payroll, slips or returns.

Reviewed against the cited tax authorities by **Nathan Wiebe** on 2026-06-21.
This historical attribution and the original approval metadata are preserved; they do not approve this correction.

## Ask the client first

Obtain the employer's BN/RP account, assigned remitter status, pay dates/frequency, gross remuneration and benefits, year-to-date pensionable/insurable earnings and deductions with this employer, and TD1 instructions. Obtain the establishment/reporting and remote-work facts, employee status, age/pension/election dates, applicable labour jurisdiction, occupation, service dates, contracts/collective agreements, leave history and any termination facts. Do not infer these from home address or salary alone.

## The method, step by step

### Section 1 -- Quick Reference

Use the dated rates below; calculate employee deductions and employer contributions separately, reconcile the payroll register, then use the applicable filing schedule. The worked cases illustrate limited components, not net pay.

### Rates and thresholds

#### Payroll

These annual limits assume full-year coverage with this employer; age/election or other proration and cross-province transfers require separate resolution.

- **Basic exemption** – $3,500 annually for CPP; period exemption is truncated, not rounded. [CRA CPP](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/payroll-deductions-contributions/canada-pension-plan-cpp/cpp-contribution-rates-maximums-exemptions.html); [T4127 ch. 1](https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/payroll-deductions-t4127-payroll-deductions-formulas/t4127-jan-122nd-edition-effective-january-1-2026/t4127-jan-payroll-deductions-formulas-computer-programs.html)
- **CPP employee rate** – 5.95% on contributory pensionable earnings through YMPE. [CRA CPP](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/payroll-deductions-contributions/canada-pension-plan-cpp/cpp-contribution-rates-maximums-exemptions.html)
- **YMPE (2026)** – $74,600. [CRA CPP](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/payroll-deductions-contributions/canada-pension-plan-cpp/cpp-contribution-rates-maximums-exemptions.html)
- **YAMPE (2026)** – $85,000. [CRA CPP2](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/calculating-deductions/making-deductions/second-additional-cpp-contribution-rates-maximums.html)
- **EI employee rate (non-QC)** – 1.63% on insurable earnings, subject to the annual maximum. [CRA EI](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/payroll-deductions-contributions/employment-insurance-ei/ei-premium-rates-maximums.html)
- **Max insurable earnings** – $68,900 for 2026 EI. [CRA EI](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/payroll-deductions-contributions/employment-insurance-ei/ei-premium-rates-maximums.html)

### Section 2 -- Income Tax Withholding (Source Deductions)

#### Federal Tax Brackets (2026)

Marginal annual taxable-income bands before credits; each higher band applies only to the excess above its lower boundary. They are not flat withholding percentages on gross pay. Use the actual pay-date payroll tables/formulas and TD1 facts for deductions. [CRA T4032](https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4032-payroll-deductions-tables/t4032on-jan/t4032on-january-general-information.html)

| Taxable Income (CAD) | Rate | Official source |
| --- | --- | --- |
| 0 -- 58,523 | 14% | [CRA 2026 federal table](https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4032-payroll-deductions-tables/t4032on-jan/t4032on-january-general-information.html) |
| 58,523 -- 117,045 | 20.5% | [CRA 2026 federal table](https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4032-payroll-deductions-tables/t4032on-jan/t4032on-january-general-information.html) |
| 117,045 -- 181,440 | 26% | [CRA 2026 federal table](https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4032-payroll-deductions-tables/t4032on-jan/t4032on-january-general-information.html) |
| 181,440 -- 258,482 | 29% | [CRA 2026 federal table](https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4032-payroll-deductions-tables/t4032on-jan/t4032on-january-general-information.html) |
| 258,482+ | 33% | [CRA 2026 federal table](https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4032-payroll-deductions-tables/t4032on-jan/t4032on-january-general-information.html) |

#### Federal Basic Personal Amount (BPA) -- 2026

This is the payroll BPAF formula, not the final personal-return credit. The income measure is payroll NI = A + HD: annual taxable income plus the annual deduction for living in a prescribed zone shown on Form TD1. Endpoints below include equality; the middle formula applies strictly between them. [Archived January-2026 T4127 chs. 2–3](https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/payroll-deductions-t4127-payroll-deductions-formulas/t4127-jan-122nd-edition-effective-january-1-2026/t4127-jan-payroll-deductions-formulas-computer-programs.html)

| Payroll NI | BPA (CAD) | Official source |
| --- | --- | --- |
| Up to $181,440 | $16,452 | [T4127 BPAF](https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/payroll-deductions-t4127-payroll-deductions-formulas/t4127-jan-122nd-edition-effective-january-1-2026/t4127-jan-payroll-deductions-formulas-computer-programs.html) |
| $181,440 -- $258,482 | Phases down to $14,829: $16,452 − (NI − $181,440) × ($1,623 / $77,042). Do not round the ratio; round the result to cents. | [T4127 BPAF](https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/payroll-deductions-t4127-payroll-deductions-formulas/t4127-jan-122nd-edition-effective-january-1-2026/t4127-jan-payroll-deductions-formulas-computer-programs.html) |
| Above $258,482 | $14,829 | [T4127 BPAF](https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/payroll-deductions-t4127-payroll-deductions-formulas/t4127-jan-122nd-edition-effective-january-1-2026/t4127-jan-payroll-deductions-formulas-computer-programs.html) |

For provincial/territorial withholding, province-of-employment determination (including establishment, remote attachment and transfers), Quebec income-tax forms and employee-specific TD1 claims: **Check this point with one of our partner accountants.** The former approximate combined top-rate table is omitted because it does not calculate payroll withholding.

### Section 3 -- Social Security: Employee Deductions

#### Canada Pension Plan (CPP) -- 2026

For pensionable employment outside Quebec, full-year contribution limits with this employer are:

| Component | Rate (Employee) | Ceiling | Maximum Contribution | Official source |
| --- | --- | --- | --- | --- |
| CPP base + first additional | 5.95% | YMPE $74,600 less $3,500 annual basic exemption | $4,230.45 | [CRA CPP](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/payroll-deductions-contributions/canada-pension-plan-cpp/cpp-contribution-rates-maximums-exemptions.html) |
| CPP2 (second additional) | 4.00% | Earnings between YMPE $74,600 and YAMPE $85,000 | $416.00 | [CRA CPP2](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/calculating-deductions/making-deductions/second-additional-cpp-contribution-rates-maximums.html); [CRA CPP](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/payroll-deductions-contributions/canada-pension-plan-cpp/cpp-contribution-rates-maximums-exemptions.html) |

Employer CPP/CPP2 matches the employee amount. [CRA matching rule](https://www.canada.ca/en/revenue-agency/services/e-services/digital-services-businesses/business-account/respond-notices.html) For age, pension receipt, CPT30 elections, disability, contribution-month proration, non-pensionable payments and Quebec transfers: **Check this point with one of our partner accountants.** No age-only eligibility shortcut is supplied. [CPP2 rates](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/calculating-deductions/making-deductions/second-additional-cpp-contribution-rates-maximums.html)

#### Employment Insurance (EI) -- 2026

For insurable employment, with annual maxima per employer:

| Location | Employee rate | Maximum insurable earnings | Employee maximum | Standard employer rate / maximum | Official source |
| --- | --- | --- | --- | --- | --- |
| Outside Quebec | 1.63% | $68,900 | $1,123.07 | 2.282% / $1,572.30 | [CRA EI](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/payroll-deductions-contributions/employment-insurance-ei/ei-premium-rates-maximums.html); [T4127 table 8.7](https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/payroll-deductions-t4127-payroll-deductions-formulas/t4127-jan-122nd-edition-effective-january-1-2026/t4127-jan-payroll-deductions-formulas-computer-programs.html) |
| Quebec | 1.30% | $68,900 | $895.70 | 1.820% / $1,253.98 | [T4127 table 8.7](https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/payroll-deductions-t4127-payroll-deductions-formulas/t4127-jan-122nd-edition-effective-january-1-2026/t4127-jan-payroll-deductions-formulas-computer-programs.html) |

The standard employer premium is 1.4 times the employee premium. [CRA standard/reduced rule](https://www.canada.ca/en/revenue-agency/services/e-services/digital-services-businesses/business-account/respond-notices.html) Approved reduced-rate employers are a separate branch: **Check this point with one of our partner accountants.** Employee/owner insurability is also referred; a rate does not prove coverage.

#### Quebec Differences

| Contribution | 2026 reference for covered earnings | Official source |
| --- | --- | --- |
| QPP base + first additional | 6.30% employee and employer; $74,600 pensionable ceiling, $3,500 exemption and $4,479.30 annual maximum each | [RQ QPP year table](https://www.revenuquebec.ca/en/businesses/source-deductions-and-employer-contributions/calculating-source-deductions-and-contributions/qpp-contributions/maximum-pensionable-earnings-and-contribution-rate/) |
| QPIP | 0.430% employee / 0.602% employer; $103,000 insurable ceiling; maximum $442.90 / $620.06 respectively | [RQ QPIP year table](https://www.revenuquebec.ca/en/businesses/source-deductions-and-employer-contributions/calculating-source-deductions-and-contributions/qpip-premiums/maximum-insurable-earnings-and-premium-rate/) |

For QPP second-tier calculations, QPP/QPIP eligibility, actual contribution bases, Quebec income-tax deductions and complete individual Quebec payroll formulas: **Check this point with one of our partner accountants.** The table is a bounded reference, not a substitute for those calculations.

### Section 4 -- Social Security: Employer Contributions

CPP matching and standard/reduced EI are addressed above; budget employer costs separately in the working paper. For the following complex coverage/base/assessment branches, no executable headline rate is supplied:

- Workers' compensation: province, industry/class, year and actual assessment schedule. **Check this point with one of our partner accountants.**
- Ontario EHT: eligible employer, associated/global payroll, shared exemption and full-payroll rate basis. **Check this point with one of our partner accountants.**
- BC EHT: associated employers, ordinary versus charity/nonprofit, remuneration location and part-year calculations. **Check this point with one of our partner accountants.**
- Manitoba HE levy: permanent establishment, taxable remuneration, associated-group exemption and part-year proration. **Check this point with one of our partner accountants.**
- Quebec HSF: sector, total payroll, contribution formula and temporary exemptions. **Check this point with one of our partner accountants.**

### Section 5 -- Minimum Wage and Overtime

The following are general hourly minimums only. Establish coverage and worker category first; student, tipped, piece-rate, platform and special-occupation rules are referred rather than silently treated as general employees. Greater contractual rights remain relevant.

| Jurisdiction | General rate during 2026 | Official source |
| --- | --- | --- |
| Federal coverage | $17.75 before 1 April; $18.15 from 1 April. A higher applicable provincial/territorial minimum prevails. | [Federal pay rules](https://www.canada.ca/en/services/jobs/workplace/federal-labour-standards/pay-deductions.html) |
| British Columbia | $17.85 before 1 June; $18.25 from 1 June | [BC 2026 release](https://news.gov.bc.ca/releases/2026LBR0002-000191) |
| Alberta | $15.00; general employees, excluding special student/occupation rates | [Alberta minimum wage](https://www.alberta.ca/minimum-wage) |
| Ontario | $17.60 before 1 October; $17.95 from 1 October | [Ontario 1 October release](https://news.ontario.ca/en/release/1008075/ontario-protecting-workers-by-raising-minimum-wage) |
| Quebec | $16.10 before 1 May; $16.60 from 1 May | [CNESST current date](https://www.cnesst.gouv.qc.ca/en/working-conditions/wage-and-pay/wages); [Government historical table](https://www.quebec.ca/nouvelles/actualites/details/hausse-du-salaire-minimum-des-aujourdhui-le-taux-general-du-salaire-minimum-setablit-a-1660-lheure-70097) |
| Manitoba | $16.00 before 1 October; $16.40 from 1 October | [Manitoba 1 April release](https://news.gov.mb.ca/news/?archive=&item=73242) |
| Saskatchewan | $15.35 before 1 October; $15.70 from 1 October | [2025 effective rate](https://www.saskatchewan.ca/government/news-and-media/2025/july/10/minimum-wage-set-to-increase-october-1); [2026 effective rate](https://www.saskatchewan.ca/Business/Employment-Standards/payment-of-wages-payroll-administration-benefits-and-time-sheets) |

Ordinary overtime defaults below apply only to covered employees without an averaging, banking or modified-schedule arrangement or occupational exemption. For those exceptions and holiday-week interactions: **Check this point with one of our partner accountants.**

| Jurisdiction | Ordinary overtime | Official source |
| --- | --- | --- |
| Federal | Beyond 8 hours/day or 40/week at least 1.5× regular hourly wage; use the greater daily or weekly overtime total. The standard week is reduced by 8 hours per general holiday. | [Federal hours rules](https://www.canada.ca/en/services/jobs/workplace/federal-labour-standards/work-hours.html) |
| Ontario | Beyond 44 hours/week at 1.5× regular rate; no statutory daily overtime under the ordinary rule | [Ontario overtime](https://www.ontario.ca/document/your-guide-employment-standards-act-0/overtime-pay) |
| BC | Beyond 8/day at 1.5×; beyond 12/day at 2×; beyond 40/week at 1.5×. Count only the first 8 daily hours for weekly overtime to avoid double counting. | [BC ESA s.40](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/00_96113_01) |
| Alberta | Greater of overtime hours beyond 8/day or 44/week, at least 1.5× regular wage absent a written overtime agreement | [Alberta overtime](https://www.alberta.ca/overtime-hours-overtime-pay) |
| Quebec | Beyond the ordinary 40-hour week at 1.5× regular hourly rate; covered holiday/vacation hours count. Agricultural and other exceptions are excluded. | [CNESST overtime](https://www.cnesst.gouv.qc.ca/fr/conditions-travail/salaire-paye/salaire/heures-supplementaires) |

### Section 6 -- Mandatory Benefits

Vacation time and vacation pay have different accrual rules. The table states ordinary minimums for covered employees; determine the actual wage base and completed continuous-service/reference-year facts. For exemptions, stub periods, special bases, payment timing/consent and greater contractual rights: **Check this point with one of our partner accountants.**

| Jurisdiction | Ordinary vacation reference | Official source |
| --- | --- | --- |
| Federal | After 1 completed year: 2 weeks / 4% of applicable gross wages for that year (excluding tips/gratuities); after 5 consecutive years: 3 weeks / 6%; after 10: 4 weeks / 8% | [Federal vacations](https://www.canada.ca/en/services/jobs/workplace/federal-labour-standards/vacations-holidays.html) |
| Ontario | After each completed vacation-entitlement year: 2 weeks below 5 years' employment, 3 weeks at 5+. Vacation pay: 4% below 5 years, 6% at 5+, on gross wages excluding vacation pay; service at year/stub-period end controls. | [Ontario vacation](https://www.ontario.ca/document/your-guide-employment-standards-act-0/vacation) |
| BC | 2 weeks after 12 consecutive months; 3 after 5 consecutive years. Pay: at least 4% of total wages after 5 calendar days of employment; 6% after 5 consecutive years. | [BC ESA ss.57–58](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/00_96113_01) |
| Alberta | 2 weeks after each of the first 4 years; 3 after 5 consecutive years. Non-monthly pay: 4% / 6% of applicable wages. Monthly salary: regular pay for the vacation, not that percentage shortcut. | [Alberta vacations](https://www.alberta.ca/vacation-pay) |
| Quebec | Continuous service at reference-year end: less than 1 year, 1 day/completed month (maximum 2 weeks) / 4%; 1–under 3 years, 2 weeks / 4%; 3+ years, 3 weeks / 6% of gross reference-year wages | [CNESST vacation table](https://www.cnesst.gouv.qc.ca/fr/conditions-travail/conges/vacances-annuelles) |
| Saskatchewan | 3 weeks, vacation pay 3/52 of applicable wages (approximately 5.77%); after 10 completed years with the employer, 4 weeks and 4/52 (approximately 7.69%) | [Saskatchewan vacation calculation](https://www.saskatchewan.ca/business/employment-standards/vacations-and-vacation-pay/annual-vacation-and-vacation-pay/calculating-and-paying-vacation-pay) |

Federal coverage has 10 general holidays; BC ESA s.1 names 11 statutory holidays. This is not an all-province census. For eligibility, substitution and total holiday pay/work premiums in any jurisdiction: **Check this point with one of our partner accountants.** [Federal holidays](https://www.canada.ca/en/services/jobs/workplace/federal-labour-standards/vacations-holidays.html); [BC ESA s.1](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/00_96113_01)

Ordinary personal illness/injury leave references, subject to coverage and notice/evidence conditions:

| Jurisdiction | Leave reference | Official source |
| --- | --- | --- |
| Federal | 3 paid medical days after 30 continuous days; then 1 at the beginning of each month following a completed month of employment, maximum 10/year including carryover. Unpaid medical protection up to 27 weeks. Paid days are for days scheduled or expected to be available for work; qualifying equivalent contractual leave is not an extra statutory bank. Written notice normally 4 weeks ahead, otherwise as soon as possible for a valid reason; a certificate may be requested for 5+ days' absence. | [Federal medical leave](https://www.canada.ca/en/services/jobs/workplace/federal-labour-standards/leaves.html) |
| Ontario | ESA s.50: 3 unpaid days/calendar year after at least 2 consecutive weeks; personal illness, injury or medical emergency. Advise the employer, or as soon as possible if already absent. Reasonable evidence may be requested, but not a health-practitioner certificate under this section. | [Ontario ESA s.50](https://www.ontario.ca/laws/statute/00e41) |
| BC | ESA s.49.1: after 90 consecutive days, up to 5 paid and 3 unpaid days each calendar year for personal illness/injury. Reasonably sufficient proof on request; separate serious-illness and sick-note restrictions require review. | [BC ESA s.49.1](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/00_96113_01); [Reg.45.031](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/396_95) |
| Quebec | Up to 26 weeks' protected non-work illness/accident absence in 12 months; ordinarily unpaid except the first 2 days after 3 months' service if not already used in the shared annual paid-day pool (family-care and other specified reasons share it). Notify the employer as soon as possible. | [CNESST illness](https://www.cnesst.gouv.qc.ca/fr/conditions-travail/conges/accidents-maladies/maladie-accident-non-lie-au-travail) |
| Alberta | Up to 27 unpaid weeks/calendar year after 90 days with the same employer. Medical certificate stating estimated duration, before leave or as soon as reasonable; written notice as soon as reasonable. Contract/collective agreement may provide pay. | [Alberta long-term leave](https://www.alberta.ca/long-term-illness-injury-leave) |

For individual leave-pay calculations, certificates/notice exceptions, overlapping leave types and contractual benefits: **Check this point with one of our partner accountants.**

EI benefits below are possible maxima for claims starting in 2026, not employment-leave entitlements or guaranteed payments. Service Canada determines eligibility and the amount; Quebec residents use QPIP instead. For qualifying hours, earnings reduction, application windows, sharing/elections and the individual's benefit: **Check this point with one of our partner accountants.**

| Benefit | Potential duration | 2026 rate / weekly maximum | Official source |
| --- | --- | --- | --- |
| Maternity | Up to 15 weeks, not shareable | 55% / $729 | [Service Canada amounts](https://www.canada.ca/en/services/benefits/ei/ei-maternity-parental/benefit-amount.html) |
| Standard parental | Up to 35 for one parent; up to 40 shared, no parent over 35 | 55% / $729 | [Service Canada amounts](https://www.canada.ca/en/services/benefits/ei/ei-maternity-parental/benefit-amount.html) |
| Extended parental | Up to 61 for one parent; up to 69 shared, no parent over 61 | 33% / $437 | [Service Canada amounts](https://www.canada.ca/en/services/benefits/ei/ei-maternity-parental/benefit-amount.html) |

The temporary one-week waiting-period waiver covers new EI claims starting 30 March 2025 through 9 October 2027. A person may serve it if advantageous because of a Supplemental Unemployment Benefit plan top-up. For employer top-up commitments and their EI interaction: **Check this point with one of our partner accountants.** [Service Canada temporary measure](https://www.canada.ca/en/services/benefits/ei/temporary-measures-for-major-economic-conditions.html)

### Section 7 -- Payslip Requirements

Use a working checklist of pay-period dates, gross pay, hours/rates, overtime, vacation pay, itemized deductions, net pay and employer/employee identifiers. This is not a statement of statutory completeness in any province. For mandatory payslip fields/frequency and Ontario/Quebec-specific requirements: **Check this point with one of our partner accountants.**

### Section 8 -- Filing Obligations

Use CRA's assigned remitter type, generally based on AMWA from 2 calendar years earlier. The table concerns ordinary continuing CRA payroll remittances; Quebec remittances and business cessation/death/status changes are referred. For quarterly qualification (new versus established employer, compliance record and status changes): **Check this point with one of our partner accountants.** [CRA remittance rules](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/remitting-source-deductions/how-when-remit-due-dates.html)

| Assigned remitter | Ordinary due date | Official source |
| --- | --- | --- |
| Quarterly, if eligible | April 15, July 15, October 15, January 15 for the preceding calendar quarter | [CRA remittance schedule](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/remitting-source-deductions/how-when-remit-due-dates.html) |
| Regular, AMWA below $25,000 and not quarterly | 15th of following month | [CRA remittance schedule](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/remitting-source-deductions/how-when-remit-due-dates.html) |
| Threshold 1, AMWA $25,000–$99,999.99 | Pay/remitting period 1–15: 25th same month; 16–month-end: 10th next month | [CRA remittance schedule](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/remitting-source-deductions/how-when-remit-due-dates.html) |
| Threshold 2, AMWA $100,000+ | Third working day after each remitting-period end: 7th, 14th, 21st and month-end | [CRA remittance schedule](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/remitting-source-deductions/how-when-remit-due-dates.html) |

When a remittance due date falls on Saturday, Sunday or a CRA-recognized public holiday, it is on time if CRA receives it or a Canadian financial institution processes it by the next business day. [CRA timing rule](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/remitting-source-deductions/how-when-remit-due-dates.html)

For continuing employers, the ordinary T4/T4 Summary and T4A return deadline is the last day of February following the calendar year. CRA treats the return as on time if received or postmarked by the next business day when that date is Saturday, Sunday or a recognized public holiday. T4 recipient copies are due by the required filing date under ITR s.209. For the statutory effect of holiday extensions on employee-copy timing, electronic delivery and cessation/death exceptions: **Check this point with one of our partner accountants.** [CRA information returns](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/file-information-returns-slip-summaries/when-to-file.html); [ITR s.209](https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-209.html)

For continuing Quebec employers, RL-1 filing/distribution and RL-1 Summary have the ordinary last-day-of-February deadline following the slip year. For adjusted dates, permanently stopped remittances, cessation/death and delivery exceptions: **Check this point with one of our partner accountants.** [RQ RL-1 guide §4.2](https://www.revenuquebec.ca/en/online-services/forms-and-publications/rl-1-g-v/guide-to-filing-the-rl-1-slip-employment-and-other-income/)

Electronic ROEs for weekly, biweekly or semi-monthly cycles are due within 5 calendar days after the end of the pay period containing the interruption of earnings. For monthly or 13-cycle payrolls, use the earlier of 5 calendar days after that period end and 15 calendar days after the first day of interruption. For determining an interruption, special triggers, paper ROEs and interruption codes: **Check this point with one of our partner accountants.** [ROE guide ch.1](https://www.canada.ca/en/employment-social-development/programs/ei/ei-list/reports/roe-guide.html)

For late-remittance penalties and their bases/repeat-failure exceptions, failure-to-deduct liability/recovery, late-slip statutory penalties versus small-filer administrative relief, interest and ROE offence scope: **Check this point with one of our partner accountants.** No penalty amount or liability is calculated from a headline.

## Worked cases

### Section 9 -- Common Payroll Patterns

#### Pattern 1 -- Biweekly Employee (Ontario)

Original inputs: annual salary $75,000, 26 biweekly periods, 2026. Assume this is the first ordinary pay, all gross is CPP-pensionable/EI-insurable, full-year CPP eligibility with this employer, no Quebec transfer, no previous deductions and standard employer EI. These are hypothetical assumptions, not established employee facts.

Gross rounds to $2,884.62; 26 such payments total $75,000.12, so an exact $75,000 salary needs a $0.12 final-pay reduction. The $3,500/26 CPP exemption truncates to $134.61. Employee CPP = ($2,884.62 − $134.61) × 5.95% = $163.63; employer matches. EI is $47.02 and standard employer EI $65.83. No first-pay CPP2 arises under the cumulative formula at these earnings. Exact full-year $75,000 salary has potential CPP2 of ($75,000 − $74,600) × 4% = $16 before period/final-pay adjustments. Federal/Ontario income-tax deductions are not computed here. [T4127 rounding and ch.6](https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/payroll-deductions-t4127-payroll-deductions-formulas/t4127-jan-122nd-edition-effective-january-1-2026/t4127-jan-payroll-deductions-formulas-computer-programs.html)

```oa-check
name: 2026 Ontario first ordinary biweekly pay, caps not yet reached
inputs:
  annual_salary: 75000
  pay_periods: 26
  annual_exemption: 3500
steps:
  gross: round(annual_salary / pay_periods, 2)
  exemption: floor(annual_exemption / pay_periods * 100) / 100
  employee_cpp: round((gross - exemption) * 0.0595, 2)
  employer_cpp: employee_cpp
  employee_ei: round(gross * 0.0163, 2)
  employer_ei: round(employee_ei * 1.4, 2)
  full_year_cpp2_potential: (annual_salary - 74600) * 0.04
expected:
  gross: 2884.62
  exemption: 134.61
  employee_cpp: 163.63
  employer_cpp: 163.63
  employee_ei: 47.02
  employer_ei: 65.83
  full_year_cpp2_potential: 16
```

#### Pattern 2 -- Employee Reaching CPP Maximum

Original inputs: 2026 salary $80,000, semi-monthly regular pay $3,333.33. Assume full-year pensionable earnings with this employer, no other earnings or Quebec transfer and no eligibility/proration exception. Period 11 totals $36,666.63; period 22 $73,333.26; period 23 $76,666.59, the first YMPE crossing. Twenty-four rounded payments total $79,999.92, so an exact $80,000 salary needs an $0.08 final-pay adjustment. General annual CPP/CPP2 maxima remain $4,230.45/$416; exact-salary CPP2 potential is $216, not the general cap. The crossing of YMPE identifies the CPP2 earnings boundary, not necessarily the pay on which CPP1 reaches its rounded contribution cap. For the actual capped period deductions and final-pay reconciliation: **Check this point with one of our partner accountants.** [T4127 ch.6](https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/payroll-deductions-t4127-payroll-deductions-formulas/t4127-jan-122nd-edition-effective-january-1-2026/t4127-jan-payroll-deductions-formulas-computer-programs.html)

```oa-check
name: 2026 semi-monthly 80000 salary, stated rounded regular pay
inputs:
  annual_salary: 80000
  regular_pay: 3333.33
  ympe: 74600
steps:
  period_11: regular_pay * 11
  period_22: regular_pay * 22
  first_crossing: floor(ympe / regular_pay) + 1
  period_23: regular_pay * 23
  rounded_year_total: regular_pay * 24
  exact_salary_cpp2: (annual_salary - ympe) * 0.04
expected:
  period_11: 36666.63
  period_22: 73333.26
  first_crossing: 23
  period_23: 76666.59
  rounded_year_total: 79999.92
  exact_salary_cpp2: 216
```

#### Pattern 3 -- Vacation Pay Payout

Original inputs: annual earnings $52,000 and an assumed 4% vacation-pay rate. The arithmetic accrual is $2,080. The assumed rate does not establish entitlement or the correct wage base. For province, continuous service, monthly/non-monthly basis, payment/consent, gross-pay inclusion and deductions: **Check this point with one of our partner accountants.**

```oa-check
name: Assumed 4 percent vacation accrual, eligibility and timing held
inputs:
  earnings: 52000
  assumed_rate: 0.04
steps:
  accrual: earnings * assumed_rate
expected:
  accrual: 2080
```

#### Pattern 4 -- Termination with ROE

Original situation: employee terminated without cause. Reconcile unpaid regular wages and any accrued vacation pay as working-paper items, without assuming an entitlement amount or payment date.

- Termination notice/pay, including the former generic one-week-per-year claim and BC service tiers, exceptions, contractual and civil entitlements: **Check this point with one of our partner accountants.**
- Ontario severance, including service, global-payroll/closure alternatives, partial years and cap: **Check this point with one of our partner accountants.**

Apply Section 8's electronic ROE timing only after the interruption and pay cycle are established. For the reason code (including Code M), final-pay treatment and paper ROE branches: **Check this point with one of our partner accountants.**

## When to refuse or refer

Do not produce a filing-ready result with unresolved coverage, province, eligibility, YTD earnings, remitter status or a referred branch. For remote/foreign employment, treaties/social-security coordination, disputed worker status and province-specific exceptions: **Check this point with one of our partner accountants.**

### Section 10 -- Interaction with Other Skills

Use payroll-workflow-base for workflow and canada-bookkeeping for journal design; links are navigation, not proof of a tax result. For corporate deductibility of employer contributions/health taxes or GST/HST treatment of wages versus taxable benefits: **Check this point with one of our partner accountants.** Do not infer those outcomes from the payroll journal.

## Sources

The 21/25 November completed reads were checked once for applicability. Exact Canada CPP/EI and slip-deadline reads were reused; missing exact text, changed dependencies and operative conditions were read on 2026-11-26. Ontario authority-indexed passages were read where direct pages returned 403 or JavaScript; the Quebec historical wage release was read through the authority's indexed text after the direct page required JavaScript. No failed direct fetch is counted as a read. The old RQ 2026-changes URL now redirects to 2027, so the year tables below replace it.

| Official source | Scope read / reused | Date read |
| --- | --- | --- |
| [CRA employer matching and EI multiplier](https://www.canada.ca/en/revenue-agency/services/e-services/digital-services-businesses/business-account/respond-notices.html) | Reused read for ordinary CPP matching and standard EI multiplier/reduced-rate exception | 2026-11-26 |
| [CRA CPP2026 annual table](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/payroll-deductions-contributions/canada-pension-plan-cpp/cpp-contribution-rates-maximums-exemptions.html) | Reused read: 2026 annual CPP row | 2026-11-26 |
| [CRA CPP2 annual table](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/calculating-deductions/making-deductions/second-additional-cpp-contribution-rates-maximums.html) | Reused read: 2026 annual CPP2 row and matching | 2026-11-26 |
| [CRA EI2026 annual table](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/payroll-deductions-contributions/employment-insurance-ei/ei-premium-rates-maximums.html) | Reused read: 2026 EI row | 2026-11-26 |
| [Archived CRA T4127 January2026](https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/payroll-deductions-t4127-payroll-deductions-formulas/t4127-jan-122nd-edition-effective-january-1-2026/t4127-jan-payroll-deductions-formulas-computer-programs.html) | Read in the following part of the source: Archived January-2026 chs.1–3 rounding/BPAF/NI, ch.6 cumulative CPP/CPP2 and tables8.3/8.7/8.8; exact gaps recovered | 2026-11-26 |
| [CRA T4032 Ontario2026](https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4032-payroll-deductions-tables/t4032on-jan/t4032on-january-general-information.html) | Read in the following part of the source: 2026 federal bracket table and payroll-table use | 2026-11-26 |
| [Revenu Québec QPP year table](https://www.revenuquebec.ca/en/businesses/source-deductions-and-employer-contributions/calculating-source-deductions-and-contributions/qpp-contributions/maximum-pensionable-earnings-and-contribution-rate/) | Read in the following part of the source: 2026 base/first-additional row; individual formulas not certified | 2026-11-26 |
| [Revenu Québec QPIP year table](https://www.revenuquebec.ca/en/businesses/source-deductions-and-employer-contributions/calculating-source-deductions-and-contributions/qpip-premiums/maximum-insurable-earnings-and-premium-rate/) | Read in the following part of the source: 2026 premium row; individual coverage referred | 2026-11-26 |
| [Federal minimum wage](https://www.canada.ca/en/services/jobs/workplace/federal-labour-standards/pay-deductions.html) | Read in the following part of the source: Federal rate dates and higher provincial minimum | 2026-11-26 |
| [BC2026 wage release](https://news.gov.bc.ca/releases/2026LBR0002-000191) | Read in the following part of the source: 2026 wage change and previous general rate | 2026-11-26 |
| [Alberta minimum wage](https://www.alberta.ca/minimum-wage) | Read in the following part of the source: General rate and student/occupation exclusions | 2026-11-26 |
| [Ontario2026 wage release](https://news.ontario.ca/en/release/1008075/ontario-protecting-workers-by-raising-minimum-wage) | Read in the following part of the source: Authority-indexed 1 October 2026 headline/opening; prior rendered read reused for applicability | 2026-11-26 |
| [CNESST wages](https://www.cnesst.gouv.qc.ca/en/working-conditions/wage-and-pay/wages) | Read in the following part of the source: Current general wage and 1 May 2026 start | 2026-11-26 |
| [Québec historical wage table](https://www.quebec.ca/nouvelles/actualites/details/hausse-du-salaire-minimum-des-aujourdhui-le-taux-general-du-salaire-minimum-setablit-a-1660-lheure-70097) | Read in the following part of the source: Authority-indexed historical May2025/May2026 general rates; direct page not read | 2026-11-26 |
| [Manitoba2026 wage release](https://news.gov.mb.ca/news/?archive=&item=73242) | Read in the following part of the source: 2026 change and previous general rate | 2026-11-26 |
| [Saskatchewan2025 wage release](https://www.saskatchewan.ca/government/news-and-media/2025/july/10/minimum-wage-set-to-increase-october-1) | Read in the following part of the source: 1 October 2025 general rate | 2026-11-26 |
| [Saskatchewan current wage](https://www.saskatchewan.ca/Business/Employment-Standards/payment-of-wages-payroll-administration-benefits-and-time-sheets) | Read in the following part of the source: 1 October 2026 general rate | 2026-11-26 |
| [Federal hours of work](https://www.canada.ca/en/services/jobs/workplace/federal-labour-standards/work-hours.html) | Read in the following part of the source: Ordinary hours/overtime, daily-v-weekly, holidays and exclusions | 2026-11-26 |
| [Ontario overtime](https://www.ontario.ca/document/your-guide-employment-standards-act-0/overtime-pay) | Read in the following part of the source: Authority-indexed ordinary overtime and exception/averaging text; direct403 | 2026-11-26 |
| [BC Employment Standards Act](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/00_96113_01) | Read in the following part of the source: ESA ss.1,40,49.1,57–58 and related coverage/exception text | 2026-11-26 |
| [Alberta overtime](https://www.alberta.ca/overtime-hours-overtime-pay) | Read in the following part of the source: 8/44 comparison, premium, agreement/occupation exceptions | 2026-11-26 |
| [CNESST overtime](https://www.cnesst.gouv.qc.ca/fr/conditions-travail/salaire-paye/salaire/heures-supplementaires) | Read in the following part of the source: Ordinary hours/premium and vacation/holiday counting | 2026-11-26 |
| [Federal vacations/holidays](https://www.canada.ca/en/services/jobs/workplace/federal-labour-standards/vacations-holidays.html) | Read in the following part of the source: Vacation service tiers, wage-base percentages and general holidays | 2026-11-26 |
| [Ontario vacation](https://www.ontario.ca/document/your-guide-employment-standards-act-0/vacation) | Read in the following part of the source: Authority-indexed service/year/base vacation rules; direct403 | 2026-11-26 |
| [Alberta vacations](https://www.alberta.ca/vacation-pay) | Read in the following part of the source: Service tiers and monthly versus non-monthly bases | 2026-11-26 |
| [CNESST vacation](https://www.cnesst.gouv.qc.ca/fr/conditions-travail/conges/vacances-annuelles) | Read in the following part of the source: Reference-year service table and gross-wage base | 2026-11-26 |
| [Saskatchewan vacation pay](https://www.saskatchewan.ca/business/employment-standards/vacations-and-vacation-pay/annual-vacation-and-vacation-pay/calculating-and-paying-vacation-pay) | Read in the following part of the source: Service tiers, wages and exact3/52 or4/52 basis | 2026-11-26 |
| [Federal medical leave](https://www.canada.ca/en/services/jobs/workplace/federal-labour-standards/leaves.html) | Read in the following part of the source: Medical-leave accrual, carryover, notice/certificate and unpaid protection | 2026-11-26 |
| [Ontario Employment Standards Act](https://www.ontario.ca/laws/statute/00e41) | Read in the following part of the source: Authority-indexed ESA s.50 entitlement, notice/evidence and no-certificate condition; direct403 | 2026-11-26 |
| [BC Employment Standards Regulation](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/396_95) | Read in the following part of the source: Regulation45.031 prescribed5days | 2026-11-26 |
| [CNESST illness leave](https://www.cnesst.gouv.qc.ca/fr/conditions-travail/conges/accidents-maladies/maladie-accident-non-lie-au-travail) | Read in the following part of the source: 26weeks/12months; shared2paid days/3months; notification | 2026-11-26 |
| [Alberta long-term leave](https://www.alberta.ca/long-term-illness-injury-leave) | Read in the following part of the source: 27weeks/90days, certificate, notice and contractual pay | 2026-11-26 |
| [EI2026 benefit maxima](https://www.canada.ca/en/services/benefits/ei/ei-maternity-parental/benefit-amount.html) | Read in the following part of the source: 2026 maxima, individual/shared weeks and Quebec routing | 2026-11-26 |
| [EI temporary measures](https://www.canada.ca/en/services/benefits/ei/temporary-measures-for-major-economic-conditions.html) | Read in the following part of the source: Waiting-period date window and top-up exception | 2026-11-26 |
| [CRA remittance schedule](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/remitting-source-deductions/how-when-remit-due-dates.html) | Read in the following part of the source: Remitter classification, ordinary due-date schedules and next-business-day treatment | 2026-11-26 |
| [CRA information returns](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/file-information-returns-slip-summaries/when-to-file.html) | Read in the following part of the source: Ordinary deadline and filing on-time treatment | 2026-11-26 |
| [Income Tax Regulations209](https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-209.html) | Read in the following part of the source: Recipient copies by required filing date; extension interaction referred | 2026-11-26 |
| [Revenu Québec RL1 guide](https://www.revenuquebec.ca/en/online-services/forms-and-publications/rl-1-g-v/guide-to-filing-the-rl-1-slip-employment-and-other-income/) | Read in the following part of the source: §4.2 ordinary deadline/exceptions; reused 23November read | 2026-11-23; applicability 2026-11-26 |
| [Service Canada ROE guide](https://www.canada.ca/en/employment-social-development/programs/ei/ei-list/reports/roe-guide.html) | Read in the following part of the source: Ch.1 electronic frequency-dependent deadlines; paper/codes/trigger exceptions referred | 2026-11-26 |

**Not yet confirmed:** all individually referred eligibility, province/remote/foreign, Quebec formula, WCB, health-tax/levy, special employee, leave/pay, holiday, payslip, quarterly/status, slip-copy holiday extension/special deadline/delivery, penalty/recovery, final-pay, termination/severance and GST/HST/deductibility branches. Those branches are excluded from usable calculations until resolved. This reference does not verify a client payroll or approve the correction.
