---
name: canada-payroll
description: Use this skill whenever asked about Canadian payroll, source deductions, CPP contributions, EI premiums, or employer obligations in Canada. Trigger on phrases like "source deductions", "CPP", "Canada Pension Plan", "CPP2", "EI", "employment insurance", "T4", "TD1", "payroll deductions", "CRA payroll", "remittance", "ROE", "record of employment", "statutory holiday pay", "vacation pay Canada", "minimum wage Canada", "provincial tax", "payroll Canada", "PD7A", "remitter type", or any question about running payroll in Canada. This skill covers federal rules; Quebec (QPP/QPIP) differences are noted but not fully detailed. ALWAYS read this skill before processing any Canadian payroll work.
version: 1.1
jurisdiction: CA
tax_year: 2026
tax_year_notes: The payroll tables and worked inputs below are for calendar 2026; midyear wage changes are dated separately. This correction reuses the 21 November 2026 audit and does not certify unresolved coverage, eligibility or province-specific calculations.
last_updated: 2026-11-25
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

## Canada -- Payroll Skill v1.1

Use these tables only for 2026 payroll. Establish province of employment, federal/provincial labour coverage, employee eligibility, pay frequency and year-to-date deductions first. **HOLD** means that the affected result must not be calculated or finalized until its stated conditions are resolved; it does not mean zero entitlement or an automatic disallowance. This correction is not whole-skill verification.

## Rates and thresholds

Reviewed against the cited tax authorities by **Nathan Wiebe** on 2026-06-21.
The historical review attribution above is preserved; it does not certify this proposed correction. Unresolved items are explicitly held below. Repeated payroll facts must stay consistent with the detailed sections.

### Payroll

- **$0–$58,523** — 14%  _(Bill C-4; CRA — 2026 payroll deductions tables (T4032) — verify on canada.ca)_
- **$58,523–$117,045** — 20.5%  _(CRA T4032 2026)_
- **$117,045–$181,440** — 26%  _(CRA T4032 2026)_
- **$181,440–$258,482** — 29%  _(CRA T4032 2026)_
- **$258,482+** — 33%  _(CRA T4032 2026)_
- **BPA (2026)** — $16,452 (up to $181,440); $14,829 (above $258,482)  _(CRA — Basic personal amount 2026 — canada.ca (verify))_
- **CPP employee rate** — 5.95%  _(CRA — CPP rates — canada.ca)_
- **CPP employer rate** — 5.95% (matches employee)  _(Canada Pension Plan Act s.9)_
- **YMPE (2026)** — $74,600  _(CRA — CPP contribution rates — canada.ca (verify 2026 announcement))_
- **CPP2 employee rate** — 4.00%  _(CRA — CPP rates — canada.ca)_
- **YAMPE (2026)** — $85,000  _(CRA — CPP contribution rates — canada.ca (verify 2026 announcement))_
- **Basic exemption** — $3,500  _(Canada Pension Plan Act s.20)_
- **Max CPP contribution (EE, 2026)** — $4,230.45  _(CRA — CPP contribution rates — canada.ca (verify 2026 YMPE))_
- **Max CPP2 contribution (EE, 2026)** — $416.00  _(CRA — CPP contribution rates — canada.ca (verify 2026 YAMPE))_
- **EI employee rate (non-QC)** — 1.63%  _(ESDC — EI premium rates — canada.ca (verify 2026))_
- **EI employer rate** — 2.282% (1.4× employee)  _(Employment Insurance Act s.68)_
- **Max insurable earnings** — $68,900 for 2026. [CRA T4032 Quebec](https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4032-payroll-deductions-tables/t4032qc-jan/t4032qc-january-general-information.html)
- **Max EE premium** — $1,123.07  _(ESDC — EI premium rates — canada.ca)_
- **Max ER premium** — $1,572.30  _(ESDC — EI premium rates — canada.ca)_
- **EI QC employee rate** — Quebec EI rate 1.30% for 2026. [Official source](https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4032-payroll-deductions-tables/t4032qc-jan/t4032qc-january-general-information.html)
- **Ontario EHT threshold** — Conditional $1,000,000; **HOLD** for eligibility/group and shared-exemption tests in Section 4. [Official source](https://www.ontario.ca/document/employer-health-tax-eht)
- **Ontario EHT rate** — 0.98%–1.95%; **HOLD** for the full-payroll rate basis and conditions in Section 4. [Official source](https://www.ontario.ca/document/employer-health-tax-eht)
- **BC EHT threshold** — Conditional $1,000,000; **HOLD** for the special/group and part-year cases in Section 4. [Official source](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/18042)
- **BC EHT rate** — Ordinary eligible single-employer case: 1.95% of total above $1.5M; 5.85% of excess over $1M through $1.5M. **HOLD** for the conditions in Section 4. [Official source](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/18042)
- **Federal** — Federal minimum wage $18.15/hr as of April 2026. Indexed to CPI and updated each April.  _(Canada Labour Code s.178; ESDC — Minimum wage — canada.ca)_
- **Ontario** — Historical $17.60/hour from 1 October 2025; $17.95/hour from 1 October 2026 for general covered employees. [Official source](https://news.ontario.ca/en/release/1008075/ontario-protecting-workers-by-raising-minimum-wage)
- **British Columbia** — BC minimum wage $18.25/hr as of June 1, 2026  _(Employment Standards Act (BC); BC government)_
- **Alberta** — $15.00/hr  _(Employment Standards Code (AB); Alberta government)_
- **Federal — after 1 year** — 4% (2 weeks)  _(Canada Labour Code s.184)_
- **Federal — after 5 years** — 6% (3 weeks); after 10 years, 8% (4 weeks). [Official source](https://www.canada.ca/en/services/jobs/workplace/federal-labour-standards/vacations-holidays.html)
- **T4 slips to employees** — Ordinary deadline: last day of February following the calendar year. ITR 209(2), (3) and (5) tie recipient copies to the date the information return is required to be filed. **HOLD:** the effect of weekend/public-holiday extensions on recipient-copy timing has not been resolved here; do not finalize an adjusted employee-copy deadline from CRA's filing on-time treatment alone. [ITR 209](https://laws-lois.justice.gc.ca/eng/regulations/c.r.C.,_c._945/page-6.html) [Official source](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/file-information-returns-slip-summaries/when-to-file.html); [CRA distribution](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/file-information-returns-slip-summaries/distribute-slips.html)  _(ITA s.153(1); CRA — T4 guide)_
- **ROE** — For electronic ROEs, weekly/biweekly/semi-monthly payrolls: within 5 calendar days after the end of the pay period in which the interruption occurs. Monthly/13-cycle payrolls: the earlier of 5 calendar days after pay-period end and 15 calendar days after the first day of interruption. [Official source](https://www.canada.ca/en/employment-social-development/programs/ei/ei-list/reports/roe-guide.html)
- **Late T4 penalty** — Minimum $100, maximum $7,500 (ITA s.162(7.01)). Graduated by NUMBER of slips, per day up to 100 days: 1-50 slips $10/day (max $1,000); 51-500 $15/day (max $1,500); 501-2,500 $25/day (max $2,500); 2,501-10,000 $50/day (max $5,000); 10,001+ $75/day (max $7,500). CRA small-filer administrative policy: 1-5 slips flat $100; 6-10 slips $5/day (max $500).  _(ITA s.162(7.01))_

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Canada |
| Currency | CAD ($) only |
| Tax year | Calendar year (1 January -- 31 December) |
| Primary legislation | Income Tax Act (federal); Canada Pension Plan Act; Employment Insurance Act; Canada Labour Code (federal employees) |
| Tax authority | Canada Revenue Agency (CRA) |
| Reporting system | T4/T4A information returns; PD7A remittance voucher |
| Pay frequency | Biweekly (most common), semi-monthly, monthly, weekly |
| Employer registration | Business Number (BN) + payroll program account (RP) via CRA |
| Provincial variation | Each province/territory has its own income tax brackets, ESA, and minimum wage |
| Validated by | Verified by Nathan Wiebe on 2026-06-21 |

Skill version: 1.1.

## Section 2 -- Income Tax Withholding (Source Deductions)

Employers withhold both federal and provincial/territorial income tax from each pay. CRA publishes payroll deduction tables (T4032) and formulas (T4127) annually.

### Federal Tax Brackets (2026)

**Federal Tax Brackets (2026)**

| Taxable Income (CAD) | Rate |
| --- | --- |
| 0 -- 58,523 | 14% |
| 58,523 -- 117,045 | 20.5% |
| 117,045 -- 181,440 | 26% |
| 181,440 -- 258,482 | 29% |
| 258,482+ | 33% |

- **Lowest bracket rate change** — The 2026 lowest rate is 14%; the reduction began during 2025, whose annual lowest rate was 14.5%. Do not apply the 2026 table to 2025 payroll. [Official source](https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4032-payroll-deductions-tables/t4032qc-jan/t4032qc-january-general-information.html)

### Federal Basic Personal Amount (BPA) -- 2026

**Federal Basic Personal Amount (BPA) -- 2026**

| Payroll NI (net income for the year from the employer) | BPA (CAD) |
| --- | --- |
| Up to $181,440 | $16,452 |
| $181,440 -- $258,482 | Phases down to $14,829 using payroll NI (A + HD), not simply taxable income. [CRA T4127 BPAF formula](https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/payroll-deductions-t4127-payroll-deductions-formulas/t4127-jan-122nd-edition-effective-january-1-2026/t4127-jan-payroll-deductions-formulas-computer-programs.html) |
| Above $258,482 | $14,829 |

### Provincial/Territorial Tax

Each province has its own tax brackets applied on top of federal tax. The employer determines the applicable province based on the employee's **province of employment** (physical reporting is only one branch; establishment and remote-attachment rules also matter). **HOLD:** determine the actual province under the applicable rules before computing provincial withholding. [Official source](https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4032-payroll-deductions-tables/t4032on-jan/t4032on-january-general-information.html) Employees complete a federal TD1 and a provincial TD1 form.

### Key Provincial Top Marginal Rates (Combined Federal + Provincial, 2026)

**Key Provincial Top Marginal Rates (Combined Federal + Provincial, 2026)**

| Province | Top Combined Rate (approx.) |
| --- | --- |
| Ontario | ~53.5% |
| British Columbia | ~53.5% |
| Alberta | ~48.0% |
| Quebec | ~53.3% |
| Manitoba | ~50.4% |
| Saskatchewan | ~47.5% |

## Section 3 -- Social Security: Employee Deductions

### Canada Pension Plan (CPP) -- 2026

**Canada Pension Plan (CPP) -- 2026**

| Component | Rate (Employee) | Ceiling | Maximum Contribution |
| --- | --- | --- | --- |
| CPP base + first additional | 5.95% | YMPE $74,600 (less $3,500 basic exemption) | $4,230.45 |
| CPP2 (second additional) | 4.00% | Earnings between YMPE $74,600 and YAMPE $85,000 | $416.00 |

- **Basic exemption** — $3,500/year (pro-rated per pay period)
- **CPP age eligibility** — **HOLD:** the old 18--69 shorthand is not an eligibility algorithm. An election to stop at ages 65--69 requires the applicable CPP/QPP retirement-pension conditions and CPT30 process; resolve age, pension status and effective dates first. [Official source](https://www.canada.ca/en/services/benefits/publicpensions/cpp/cpp-post-retirement/eligibility.html)
- **CPP2** — CPP2 is a second tier introduced in 2024 on earnings between the first and second ceilings

### Employment Insurance (EI) -- 2026

**Employment Insurance (EI) -- 2026**

| Item | Rate | Maximum Insurable Earnings | Maximum Annual Premium |
| --- | --- | --- | --- |
| Employee (Canada except Quebec) | 1.63% | $68,900 | $1,123.07 |
| Employee (Quebec -- reduced for QPIP) | 1.30% | $68,900 | $895.70 [Official source](https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4032-payroll-deductions-tables/t4032qc-jan/t4032qc-january-general-information.html) |

### Quebec Differences

For covered Quebec employees, QPP replaces CPP. The 2026 combined QPP base/first-additional rate is **6.30%**. QPIP is **0.430% employee / 0.602% employer**, separate from Quebec EI. **HOLD:** this is not a complete Quebec payroll calculation; bind contribution bases, ceilings, second-tier QPP and individual eligibility through the operative Quebec formulas before use. [Revenu Québec 2026 changes](https://www.revenuquebec.ca/en/businesses/source-deductions-and-employer-contributions/employers-principal-changes-for-2026/)

## Section 4 -- Social Security: Employer Contributions

### CPP Employer Contributions -- 2026

**CPP Employer Contributions -- 2026**

| Component | Rate | Maximum |
| --- | --- | --- |
| CPP base + first additional | 5.95% (matches employee) | $4,230.45 |
| CPP2 | 4.00% (matches employee) | $416.00 |

- **Employer CPP matching** — Employer CPP contributions mirror the employee amount exactly (1:1 match).

### EI Employer Contributions -- 2026

**EI Employer Contributions -- 2026**

| Item | Rate | Maximum |
| --- | --- | --- |
| Employer (Canada except Quebec) | 2.282% (1.4× employee rate) | $1,572.30 |
| Employer (Quebec) | 1.820% (standard 1.4× employee rate) | $1,253.98 [Official source](https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4032-payroll-deductions-tables/t4032qc-jan/t4032qc-january-general-information.html) |

- **Employer EI multiplier** — The employer pays 1.4 times the employee EI premium. Employers may apply for an EI premium reduction if they have a qualifying short-term disability plan.

### Workers' Compensation

Provincial/territorial requirement. Premiums vary by industry classification and province. **HOLD:** the former generic $0.50--$3.00 per $100 office-worker range has no verified province/class/year schedule in this audit and must not price a payroll. Obtain the actual classification and operative assessment schedule.

### Employer Health Tax (Select Provinces)

**Employer Health Tax (Select Provinces)**

| Province | Threshold | Rate |
| --- | --- | --- |
| Ontario (EHT) | Conditional $1,000,000 exemption | **HOLD:** eligibility, associated-group $5M ceiling, shared exemption and full-payroll rate basis must be resolved before applying 0.98%--1.95%. [Official source](https://www.ontario.ca/document/employer-health-tax-eht) |
| British Columbia (EHT) | Conditional $1,000,000 threshold | Ordinary eligible single-employer case: 5.85% of excess over $1M through $1.5M; above $1.5M, 1.95% of total. **HOLD:** associated groups, charities/nonprofits and part-year proration must be resolved. [Official source](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/18042) |
| Manitoba (HE levy) | $2,500,000 exemption from 1 January 2026 | Over $2.5M through $5M: 4.3% of excess over $2.5M; over $5M: 2.15% of total remuneration. [Official source](https://payment.manitoba.ca/finance/taxation/taxes/payroll.html); [effective date](https://www.gov.mb.ca/finance/taxation/pubs/bulletins/2025budget.pdf) |
| Quebec (HSF) | Sector/payroll dependent | **HOLD:** the former universal 1.65%--4.26% range excludes the 1.25% primary/manufacturing endpoint. Sector formulas, total payroll and temporary-exemption conditions must be resolved. [Official source](https://www.revenuquebec.ca/en/businesses/source-deductions-and-employer-contributions/employers-principal-changes-for-2026/) |

## Section 5 -- Minimum Wage and Overtime

### Federal Minimum Wage

- **Federal minimum wage** — $18.15/hour (as of April 2026, indexed annually to CPI). Applies to federally regulated industries only (banking, telecom, interprovincial transport).

### Select Provincial Minimum Wages (2026)

**Select Provincial Minimum Wages (2026)**

| Province | Rate (CAD/hour) |
| --- | --- |
| Ontario | $17.60 before 1 October 2026; $17.95 from that date. [Official source](https://news.ontario.ca/en/release/1008075/ontario-protecting-workers-by-raising-minimum-wage) |
| British Columbia | $18.25 |
| Alberta | $15.00 |
| Quebec | $16.10 before 1 May 2026; $16.60 from that date. [Official source](https://www.cnesst.gouv.qc.ca/en/working-conditions/wage-and-pay/wages); [CNESST minimum-wage page](https://www.cnesst.gouv.qc.ca/en/working-conditions/wage-and-pay/wages/minimum-wage) |
| Manitoba | $16.00 before 1 October 2026; $16.40 from that date. [Official source](https://news.gov.mb.ca/news/?archive=&item=73242) |
| Saskatchewan | $15.70 from 1 October 2026; **HOLD:** this correction does not verify an earlier-2026 amount. [Official source](https://www.saskatchewan.ca/Business/Employment-Standards/payment-of-wages-payroll-administration-benefits-and-time-sheets) |

These rows concern general covered employees for the stated periods. Establish any special worker category before applying a wage minimum.

### Overtime

**Overtime**

| Jurisdiction | Threshold | Rate |
| --- | --- | --- |
| Federal | 8 hrs/day or 40 hrs/week | 1.5× regular rate |
| Ontario | 44 hrs/week | 1.5× regular rate |
| British Columbia | > 8 hrs/day or > 40 hrs/week | 1.5×; > 12 hrs/day = 2× |
| Alberta | > 8 hrs/day or > 44 hrs/week | 1.5× regular rate |
| Quebec | > 40 hrs/week | 1.5× regular rate |

These overtime rows describe ordinary covered cases. Exemptions, averaging/modified schedules, holiday weeks, BC double-counting rules and Alberta daily-versus-weekly comparison can change the result; establish the applicable branch before calculating.

## Section 6 -- Mandatory Benefits

### Vacation Pay

**Vacation Pay**

| Jurisdiction | After 1 Year | After 5+ Years |
| --- | --- | --- |
| Federal | 4% (2 weeks) after 1 year | 6% (3 weeks) after 5 years; **8% (4 weeks) after 10 years**. [Official source](https://www.canada.ca/en/services/jobs/workplace/federal-labour-standards/vacations-holidays.html) |
| Ontario | 4% (2 weeks) | 6% (3 weeks after 5 years) |
| British Columbia | 4% (2 weeks) | 6% (3 weeks after 5 years) |
| Alberta | 4% (2 weeks), for non-monthly-paid employees | 6% (3 weeks after 5 years), for non-monthly-paid employees. **HOLD:** monthly salary follows the regular-wage rule; resolve the pay basis. [Official source](https://www.alberta.ca/vacation-pay) |
| Quebec | 4% (2 weeks) initially; 6% after 3 years | 6% (3 weeks) |
| Saskatchewan | 5.77% (3 weeks) | 7.69% (4 weeks after 10 years) |

### Statutory / Public Holidays

There are **10 federal general holidays** under federal coverage. [Official source](https://www.canada.ca/en/services/jobs/workplace/federal-labour-standards/vacations-holidays.html) Provincial counts differ: BC lists **11 for 2026**, disproving the former national 6--10 range; this is not a census of every province. [Official source](https://www2.gov.bc.ca/gov/content/employment-business/employment-standards-advice/employment-standards/statutory-holidays) **HOLD:** determine jurisdiction, eligibility, holiday pay and any work premium separately. Federal/BC rules can require holiday pay plus premium; “1.5× or time off” is not a complete total-pay formula.

### Sick Leave

**Sick Leave**

| Jurisdiction | Paid Days | Unpaid Days |
| --- | --- | --- |
| Federal | After the initial 30 days of continuous employment, 3 paid medical-leave days accrue; then 1 at the start of each month following a completed month of employment, up to 10 per year including carried-over days. [Official source](https://www.canada.ca/en/services/jobs/workplace/federal-labour-standards/leaves.html) | Up to 27 weeks of unpaid medical-leave protection for covered federal employees. **HOLD:** apply the actual absence, notice and certificate conditions before finalizing entitlement. [Official source](https://www.canada.ca/en/services/jobs/workplace/federal-labour-standards/leaves.html) |
| Ontario | No paid sick days under this ESA minimum; greater contractual rights can apply | 3 unpaid days after 2 consecutive weeks of employment, subject to coverage. [Official source](https://www.ontario.ca/document/your-guide-employment-standards-act-0/sick-leave) |
| British Columbia | 5 paid days after 90 consecutive days, subject to eligibility. [ESA 49.1](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/00_96113_01); [Regulation 45.031](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/396_95) | 3 unpaid days after 90 consecutive days. [Official source](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/00_96113_01) |
| Quebec | 2 paid days after 3 months, shared annual entitlement subject to conditions | Illness/accident absence protection up to 26 weeks in 12 months, not 24 unpaid days; resolve the shared paid days and coverage. [Official source](https://www.cnesst.gouv.qc.ca/fr/conditions-travail/conges/accidents-maladies/maladie-accident-non-lie-au-travail) |
| Alberta | No paid entitlement under this long-term illness/injury leave | Up to 27 unpaid weeks per calendar year, after 90 days of employment and subject to certificate/coverage conditions; not 16 days. [Official source](https://www.alberta.ca/long-term-illness-injury-leave) |

### Maternity / Parental Leave (EI Benefits)

**Maternity / Parental Leave (EI Benefits)**

| Benefit | Duration | EI Rate |
| --- | --- | --- |
| Maternity (birth parent only) | 15 weeks | 55% of insurable earnings; 2026 maximum $729/week. [Official source](https://www.canada.ca/en/services/benefits/ei/ei-maternity-parental/benefit-amount.html) |
| Standard parental | Up to 35 weeks for one parent; 40 total if shared, with no parent over 35 | 55%; 2026 maximum $729/week. [Official source](https://www.canada.ca/en/services/benefits/ei/ei-maternity-parental/benefit-amount.html) |
| Extended parental | Up to 61 weeks for one parent; 69 total if shared, with no parent over 61 | 33%; 2026 maximum $437/week. [Official source](https://www.canada.ca/en/services/benefits/ei/ei-maternity-parental/benefit-amount.html) |

- **Top-up / waiting period** — Employers are not required to top up EI benefits, though many do contractually. The temporary one-week EI waiting-period waiver applies to claims starting **30 March 2025 through 9 October 2027**, with the stated exception option; do not infer permanent abolition. [Official source](https://www.canada.ca/en/services/benefits/ei/temporary-measures-for-major-economic-conditions.html)

### Group Benefits

Not legally mandated, but most Canadian employers provide extended health, dental, life insurance, and short/long-term disability as part of competitive compensation.

## Section 7 -- Payslip Requirements

The Canada Labour Code (federal) and provincial Employment Standards Acts require employers to provide a pay statement each pay period.

**HOLD:** this is a workpaper checklist, not a verified province-by-province statement of every mandatory field. Establish the relevant statute and employee category before concluding that a payslip complies.

### Mandatory Payslip Contents

- Pay period dates
- Gross earnings
- All deductions itemised (CPP, EI, federal tax, provincial tax, other)
- Net pay
- Hours worked (if hourly)
- Rate of pay
- Overtime hours and pay (if applicable)
- Vacation pay (if applicable)

### Additional Requirements by Province

Ontario requires the employer's name and address, the employee's name, and the pay period. Quebec requires similar plus contribution details. Most provinces align with the above minimum.

## Section 8 -- Filing Obligations

### Remittance of Source Deductions

**Remittance of Source Deductions**

| Remitter Type | Threshold (Avg Monthly Withholding) | Due Date |
| --- | --- | --- |
| Quarterly | New-remitter branch: under $1,000 with perfect compliance; established-account branch can use AMWA under $3,000 after the required 12-month compliance period | 15th of month after quarter end. **HOLD:** confirm the actual eligibility branch and CRA remitter status. [Official source](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/remitting-source-deductions/how-when-remit-due-dates.html) |
| Regular | < $25,000 | 15th of following month |
| Threshold 1 accelerated | $25,000 -- $99,999.99 | Paydays 1--15: due 25th of that month; paydays 16--month-end: due 10th of next month. [Official source](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/remitting-source-deductions/how-when-remit-due-dates.html) |
| Threshold 2 accelerated | ≥ $100,000 | Within 3 working days after the remitting period ending on the 7th, 14th, 21st or month-end; not 3 days after each pay date. [Official source](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/remitting-source-deductions/how-when-remit-due-dates.html) |

### Year-End Filing (T4)

**Year-End Filing (T4)**

| Task | Deadline |
| --- | --- |
| T4 slips to employees | Ordinary last day of February following the calendar year; ITR 209(2), (3) and (5) link recipient copies to the required return-filing date. **HOLD:** resolve the actual year and statutory weekend/public-holiday extension before finalizing an adjusted employee-copy deadline. [ITR 209](https://laws-lois.justice.gc.ca/eng/regulations/c.r.C.,_c._945/page-6.html) [Official source](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/file-information-returns-slip-summaries/when-to-file.html); [CRA distribution](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/file-information-returns-slip-summaries/distribute-slips.html) |
| T4 Summary to CRA | Last day of February |
| T4A slips (contract/other income) | Last day of February |
| Quebec: RL-1 slips to employees and Revenu Québec | Ordinary last-day-of-February deadline. **HOLD:** cessation/death exceptions and the specific year-adjusted date are not resolved here. [Official source](https://www.revenuquebec.ca/en/online-services/forms-and-publications/rl-1-g-v/guide-to-filing-the-rl-1-slip-employment-and-other-income/) |

### Record of Employment (ROE)

- **ROE issuance** — For electronic ROEs, weekly/biweekly/semi-monthly payrolls: within 5 calendar days after the end of the pay period in which the interruption occurs. Monthly/13-cycle payrolls: the earlier of 5 calendar days after pay-period end and 15 calendar days after the first day of interruption. [Official source](https://www.canada.ca/en/employment-social-development/programs/ei/ei-list/reports/roe-guide.html) Paper-ROE deadlines are a separate branch; do not apply this electronic schedule to paper.

### Penalties

**Penalties**

| Violation | Penalty |
| --- | --- |
| Late remittance | 3% for 1--3 days late; 5% for 4--5; 7% for 6--7; 10% for more than 7 days, plus applicable arrears interest. The ordinary remittance penalty generally applies to the part over $500, but knowing/gross-negligence failures can use the total; knowing/gross-negligence second or later failures in the calendar year can attract 20%. **HOLD:** establish the actual penalty base and failure history before assessing a charge. [Official source](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4001/employers-guide-payroll-deductions-remittances.html) |
| Failure to deduct | **HOLD:** the ordinary 10% headline does not settle contribution/tax recovery treatment or knowing/gross-repeat 20% conditions. The $500 base qualification belongs to failure to remit, not this failure-to-deduct rule. Do not calculate liability from this shorthand. [Official source](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4001/employers-guide-payroll-deductions-remittances.html) |
| Late T4 filing | Min $100, max $7,500; graduated $10-$75/day by slip count up to 100 days (small filers: 1-5 slips flat $100, 6-10 slips $5/day) |
| Failure to issue ROE | T4001 states a possible $2,000 fine / 6-month imprisonment maximum for not providing a correct ROE. **HOLD:** its application to failure to issue, and the actual applicable offence/assessment, remain unresolved; this is not an automatic charge. [Official source](https://www.canada.ca/en/employment-social-development/programs/ei/ei-list/reports/roe-guide.html); [Official source](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4001/employers-guide-payroll-deductions-remittances.html) |

## Section 9 -- Common Payroll Patterns

### Pattern 1 -- Biweekly Employee (Ontario)

Annual salary $75,000. Paid biweekly (26 pay periods).

1. Gross per period: $75,000 ÷ 26 = $2,884.62
2. CPP: truncate $3,500 ÷ 26 to the CRA period exemption $134.61; ($2,884.62 - $134.61) × 5.95% = **$163.63**, rounded to cents. [Official source](https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/payroll-deductions-t4127-payroll-deductions-formulas/t4127-jan-122nd-edition-effective-january-1-2026/t4127-jan-payroll-deductions-formulas-computer-programs.html)
3. CPP2: use the cumulative formula and actual year-to-date facts; annualized salary above $74,600 does not authorize premature deductions. For an exact $75,000 full year, potential CPP2 is ($75,000 - $74,600) × 4% = $16 before payroll rounding/adjustment. **HOLD:** no period-specific CPP2 without year-to-date inputs. [Official source](https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/payroll-deductions-t4127-payroll-deductions-formulas/t4127-jan-122nd-edition-effective-january-1-2026/t4127-jan-payroll-deductions-formulas-computer-programs.html)
4. EI: $2,884.62 × 1.63% = $47.02
5. Federal tax: per T4032 table for biweekly pay
6. Ontario provincial tax: per T4032-ON table
7. Employer CPP: **$163.63** (matches employee). [Official source](https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/payroll-deductions-t4127-payroll-deductions-formulas/t4127-jan-122nd-edition-effective-january-1-2026/t4127-jan-payroll-deductions-formulas-computer-programs.html)
8. Employer EI: $47.02 × 1.4 = $65.83


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

### Pattern 2 -- Employee Reaching CPP Maximum

Employee paid $80,000 semi-monthly ($3,333.33/period). With no other pensionable earnings and that rounded regular pay, period 11 totals **$36,666.63**; period 22 totals **$73,333.26**; the first YMPE crossing is **period 23**, at **$76,666.59**. The general CPP annual maximum remains $4,230.45, and the general CPP2 ceiling/cap remains $85,000/$416; this employee does not reach that second ceiling on salary alone. An exact $80,000 full-year salary gives CPP2 of **$216** before payroll-rounding adjustments. **HOLD:** the actual deduction requires year-to-date contributions, eligibility and the final-pay rounding adjustment; 24 payments of $3,333.33 total $79,999.92. [Official source](https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/payroll-deductions-t4127-payroll-deductions-formulas/t4127-jan-122nd-edition-effective-january-1-2026/t4127-jan-payroll-deductions-formulas-computer-programs.html)


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

### Pattern 3 -- Vacation Pay Payout

Employee earning $52,000/year with 4% vacation pay. Vacation pay accrues: $52,000 × 4% = $2,080/year. **HOLD:** the assumed 4% is an example input, not a universal entitlement. Province, service, monthly/non-monthly pay basis and payment/consent requirements determine whether vacation pay may be paid on each cheque or when leave is taken. Resolve those and the gross-pay/deduction treatment before paying. [Official source](https://www.alberta.ca/vacation-pay); [Official source](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/00_96113_01)


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

### Pattern 4 -- Termination with ROE

Employee terminated without cause. Final pay includes:
- Outstanding regular wages through last day
- Accrued vacation pay (mandatory payout)
- Termination pay: **HOLD**, there is no national one-week-per-year rule. For example, BC ESA 63 has service tiers (1 week after 3 months, 2 after 12 months, 3 after 3 years, then increases to an 8-week cap); actual jurisdiction, service, contract and civil entitlement remain required. [Official source](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/00_96113_01)
- Ontario severance: **HOLD**, the ordinary one-week-per-year formula and 5-year/$2.5M payroll branch are incomplete without global-payroll scope, the alternative 50-employees/6-month closure branch, partial years and the 26-week cap. Do not finalize an individual entitlement from the headline. [Official source](https://www.ontario.ca/document/your-guide-employment-standards-act-0/severance-pay)

Issue the electronic ROE through ROE Web using the pay-frequency deadline in Section 8. [Official source](https://www.canada.ca/en/employment-social-development/programs/ei/ei-list/reports/roe-guide.html) **HOLD:** select the interruption code from the actual reason; this correction does not independently verify Code M or every code condition.

## Section 10 -- Interaction with Other Skills

**Interaction with Other Skills**

| Skill | Interaction |
| --- | --- |
| payroll-workflow-base | Provides generic payroll processing steps; this skill adds Canadian-specific rules |
| canada-bookkeeping | Payroll journals: salaries + ER CPP/EI + ER EHT/WCB to P&L; net pay + source deductions payable to BS |
| canada-corporate-tax | Employer CPP/EI and provincial health taxes are deductible business expenses |
| canada-gst-hst | No GST/HST on wages; but taxable benefits may trigger GST/HST |

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.


## Sources

This correction reuses the completed **21 November 2026** audit reads against the unchanged source file. The 21 November rows are reused bounded reads; the 25 November rows identify only follow-ups needed to resolve actual independent-review gaps or conflicts, not a new whole-skill read. The original skill had authority names and placeholders but no explicit official URLs; the audit located the official pages below. Restrictions and partial scope remain disclosed.

| Official source | Scope actually read and reused | Date read |
| --- | --- | --- |
| [CRA T4032 Ontario 2026](https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4032-payroll-deductions-tables/t4032on-jan/t4032on-january-general-information.html) | Read bounded text: 2026 federal, CPP and non-QC EI rates; BPA and province-of-employment boundaries | 2026-11-21 |
| [CRA T4032 Quebec 2026](https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4032-payroll-deductions-tables/t4032qc-jan/t4032qc-january-general-information.html) | Read bounded text: 2026 Quebec EI rates and maxima; abatement and 2025/2026 lowest-rate context | 2026-11-21 |
| [Revenu Québec 2026 changes](https://www.revenuquebec.ca/en/businesses/source-deductions-and-employer-contributions/employers-principal-changes-for-2026/) | Read bounded text: 2026 QPP/QPIP inputs and HSF sector/payroll boundaries, not complete individual Quebec formulas | 2026-11-21 |
| [CRA T4127 2026](https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/payroll-deductions-t4127-payroll-deductions-formulas/t4127-jan-122nd-edition-effective-january-1-2026/t4127-jan-payroll-deductions-formulas-computer-programs.html) | Read bounded text: 2026 basic-exemption truncation/table, CPP and cumulative CPP2 formulas; example inputs preserved | 2026-11-21 |
| [CPP post-retirement eligibility](https://www.canada.ca/en/services/benefits/publicpensions/cpp/cpp-post-retirement/eligibility.html) | Read bounded text: CPP pension-status/election qualification; age alone is not a stopping algorithm | 2026-11-21 |
| [Ontario EHT](https://www.ontario.ca/document/employer-health-tax-eht) | Read bounded text: Authority-indexed exemption/group and rate-basis text; direct restrictions disclosed | 2026-11-21 |
| [BC Employer Health Tax Act](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/18042) | Read bounded text: Ordinary rate formula with group, special-employer and part-year qualifications | 2026-11-21 |
| [Manitoba levy table](https://payment.manitoba.ca/finance/taxation/taxes/payroll.html) | Read bounded text: Current levy exemption/rate table | 2026-11-21 |
| [Manitoba budget bulletin](https://www.gov.mb.ca/finance/taxation/pubs/bulletins/2025budget.pdf) | Read bounded text: Budget bulletin's operative 1 January 2026 levy effective-date passage | 2026-11-21 |
| [National minimum-wage data](https://minwage-salairemin.service.canada.ca/en/general.html?1353fe24_page=3&86c20c73_page=2) | Read bounded text: General covered-employee wage rates/effective dates, not all special worker categories | 2026-11-21 |
| [Ontario wage release](https://news.ontario.ca/en/release/1008075/ontario-protecting-workers-by-raising-minimum-wage) | Read bounded text: 1 October 2026 general minimum-wage change | 2026-11-21 |
| [CNESST wages](https://www.cnesst.gouv.qc.ca/en/working-conditions/wage-and-pay/wages) | Read bounded text: 1 May 2026 general minimum-wage change | 2026-11-21 |
| [Manitoba wage release](https://news.gov.mb.ca/news/?archive=&item=73242) | Read bounded text: Pre/post 1 October 2026 general minimum rates | 2026-11-21 |
| [Saskatchewan wage guidance](https://www.saskatchewan.ca/Business/Employment-Standards/payment-of-wages-payroll-administration-benefits-and-time-sheets) | Read bounded text: 1 October 2026 general rate; earlier-2026 amount not confirmed here | 2026-11-21 |
| [Federal vacations and holidays](https://www.canada.ca/en/services/jobs/workplace/federal-labour-standards/vacations-holidays.html) | Read bounded text: Federal service tiers including 10-year vacation tier; ten general holidays | 2026-11-21 |
| [BC Employment Standards Act](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/00_96113_01) | Read bounded text: ESA 40, 49.1, 57–58 and 63; ordinary overtime, sick-leave eligibility, vacation and termination | 2026-11-21 |
| [BC Employment Standards Regulation](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/396_95) | Read bounded text: Regulation 45.031: prescribed five paid days; completed audit follow-up | 2026-11-21 |
| [BC statutory holidays](https://www2.gov.bc.ca/gov/content/employment-business/employment-standards-advice/employment-standards/statutory-holidays) | Read bounded text: 2026 list of eleven holidays; not a province-wide national census | 2026-11-21 |
| [Federal leaves](https://www.canada.ca/en/services/jobs/workplace/federal-labour-standards/leaves.html) | Read bounded text: Medical-leave accrual, initial wait and carryover conditions | 2026-11-21 |
| [Ontario sick leave](https://www.ontario.ca/document/your-guide-employment-standards-act-0/sick-leave) | Read bounded text: Authority-indexed operative text: three unpaid days/two-week service; direct access restricted | 2026-11-21 |
| [CNESST illness leave](https://www.cnesst.gouv.qc.ca/fr/conditions-travail/conges/accidents-maladies/maladie-accident-non-lie-au-travail) | Read bounded text: Shared paid entitlement and 26-week/12-month absence protection | 2026-11-21 |
| [Alberta illness/injury leave](https://www.alberta.ca/long-term-illness-injury-leave) | Read bounded text: 27-week leave and 90-day/certificate conditions | 2026-11-21 |
| [EI maternity/parental benefits](https://www.canada.ca/en/services/benefits/ei/ei-maternity-parental/benefit-amount.html) | Read bounded text: 2026 EI weekly maxima, individual weeks and shared extras | 2026-11-21 |
| [EI temporary measures](https://www.canada.ca/en/services/benefits/ei/temporary-measures-for-major-economic-conditions.html) | Read bounded text: Temporary waiting-period waiver claim-start dates and stated exception option | 2026-11-21 |
| [CRA remittance due dates](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/remitting-source-deductions/how-when-remit-due-dates.html) | Read bounded text: Quarterly branches and accelerated pay/remitting-period due-date tables | 2026-11-21 |
| [CRA information-return deadlines](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/file-information-returns-slip-summaries/when-to-file.html) | Read bounded text: Ordinary February filing deadline and continuing small-filer administrative relief | 2026-11-21 |
| [Revenu Québec RL-1 guide](https://www.revenuquebec.ca/en/online-services/forms-and-publications/rl-1-g-v/guide-to-filing-the-rl-1-slip-employment-and-other-income/) | Read bounded text: Ordinary RL-1 deadline; exceptional/year-adjusted dates remain held | 2026-11-21 |
| [Service Canada ROE guide](https://www.canada.ca/en/employment-social-development/programs/ei/ei-list/reports/roe-guide.html) | Read bounded text: Electronic timing by pay frequency; paper/code branches not completed here | 2026-11-21 |
| [CRA T4001](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4001/employers-guide-payroll-deductions-remittances.html) | Read bounded text: Remittance day ladder, failure-to-deduct conditions and ROE penalty maxima | 2026-11-21 |
| [Alberta vacation pay](https://www.alberta.ca/vacation-pay) | Read bounded text: Monthly versus non-monthly vacation-pay basis; no universal per-cheque permission | 2026-11-21 |
| [Ontario severance](https://www.ontario.ca/document/your-guide-employment-standards-act-0/severance-pay) | Read bounded text: Authority-indexed Ontario payroll/closure/partial-year/cap text; individual outcome held | 2026-11-21 |
| [CRA T4001 bounded follow-up](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4001/employers-guide-payroll-deductions-remittances.html) | Read bounded text: Failure-to-deduct versus remittance paragraphs (559–586); the $500 base qualification is remittance-specific; old audit summary corrected | 2026-11-25 |
| [CRA T4127 BPAF follow-up](https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/payroll-deductions-t4127-payroll-deductions-formulas/t4127-jan-122nd-edition-effective-january-1-2026/t4127-jan-payroll-deductions-formulas-computer-programs.html) | Read bounded text: Archived January 2026 BPAF formula and NI glossary (224–235,312); not a final personal-return assessment | 2026-11-25 |
| [CNESST wage follow-up](https://www.cnesst.gouv.qc.ca/en/working-conditions/wage-and-pay/wages) | Read bounded text: Wages heading/current-rate passage (16–22): $16.60 from 1 May 2026; reviewer extraction had stale $14.25 | 2026-11-25 |
| [Ontario rendered release](https://news.ontario.ca/en/release/1008075/ontario-protecting-workers-by-raising-minimum-wage) | Read bounded text: Browser-rendered 1 October 2026 headline and opening: $17.60 to $17.95; plain fetch was JavaScript-only | 2026-11-25 |
| [CNESST illness follow-up](https://www.cnesst.gouv.qc.ca/fr/conditions-travail/conges/accidents-maladies/maladie-accident-non-lie-au-travail) | Read bounded text: 26 weeks/12 months and shared two-day annual entitlement after three months (73–96); reviewer fetch failed | 2026-11-25 |
| [RL-1 guide section 4.2](https://www.revenuquebec.ca/en/online-services/forms-and-publications/rl-1-g-v/guide-to-filing-the-rl-1-slip-employment-and-other-income/) | Read bounded text: Ordinary filing/distribution deadline and exceptional table (259–272); reviewer fetch failed | 2026-11-25 |
| [Federal medical-leave follow-up](https://www.canada.ca/en/services/jobs/workplace/federal-labour-standards/leaves.html) | Read bounded text: Medical section (504–541): unpaid protection up to 27 weeks; paid initial wait, month-start accrual and carryover | 2026-11-25 |
| [CRA slip distribution](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/file-information-returns-slip-summaries/distribute-slips.html) | Read bounded text: When to distribute (44–51): employee/recipient copies due last February; filing adjustments cited separately | 2026-11-25 |
| [ITR 209](https://laws-lois.justice.gc.ca/eng/regulations/c.r.C.,_c._945/page-6.html) | Read bounded text: 209(2), (3), (5) link recipient-copy timing to the information-return filing date; relationship confirmed; statutory holiday/weekend-extension effect on recipient copies remains unresolved | 2026-11-25 |
| [CNESST specific minimum wage](https://www.cnesst.gouv.qc.ca/en/working-conditions/wage-and-pay/wages/minimum-wage) | Read bounded text: heading and current general rate (28–34); $16.60, corroborating the parent page after the reviewer's stale-cache result | 2026-11-25 |
| [T4001 correct-ROE qualification](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4001/employers-guide-payroll-deductions-remittances.html) | Read bounded text: SIN/ROE paragraph (420), not the separate general-offence paragraph; exact failure-to-issue offence remains held | 2026-11-25 |

**Not yet confirmed:** complete 2025 payroll (outside this 2026 correction); employee-specific province/coverage and pension elections; actual Quebec contribution bases, second tier and individual formulas; WCB class/year schedules; health-tax group/special/proration cases; detailed holiday-pay totals; province-specific complete payslip fields; quarterly eligibility and CRA status; T4 recipient-copy weekend/public-holiday extensions and RL-1 exceptional/year-adjusted deadlines; penalty/recovery exceptions; individual period CPP2, vacation-payment consent and termination/severance outcomes. Saskatchewan pre-1 October 2026 amount and ROE code/paper branches are not certified here. The scope of the ROE offence for a failure to issue also remains unverified. No client payroll, payslip or filing was verified.
