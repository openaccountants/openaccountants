---
name: mn-payroll
description: "Minnesota2026 withholding formula and filings, UI44,000base/assessments/industry rates, Paid Leave premiums, ESST, construction classification and corrected cases."
jurisdiction: US-MN
tax_year: 2026
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: payroll
type: computation
category: state-tax
version: "0.3"
---

# Minnesota employer withholding, UI and Paid Leave, 2026

> **General reference only.** Source-cited draft, not approved by an accountant. For US Treasury Circular 230 §10.37 purposes this is general reference material; a qualified professional must check the facts, current law and forms before filing or taking a position.

## Who this applies to

Minnesota employers paying resident or Minnesota-source wages, with state withholding, unemployment insurance(UI),2026 Paid Leave premiums and the existing wage/leave/classification topics. Use `us-form-941-940-payroll` for federal withholding/FICA/FUTA. State income returns belong to `mn-income-tax`; entities to `mn-corporate-and-pte`. Employer tax and employee deductions are separate, as are the Revenue withholding account and the Joint UI/Paid Leave account. Do not use the old nonexistent companion slugs as operational instructions.

## Rates, bands and thresholds

| Item | 2026 rate / amount | Official source |
| --- | --- | --- |
| W-4MN allowance value in computer formula | 5,300 annually per certified allowance | [2026 booklet, p.34](https://www.revenue.state.mn.us/sites/default/files/2025-12/wh-inst-26.pdf) |
| Separate or separately identified supplemental wages | 6.25% using the booklet's method | [Booklet, p.7](https://www.revenue.state.mn.us/sites/default/files/2025-12/wh-inst-26.pdf) |
| UI taxable wage base | First 44,000 covered wages per employee/calendar year | [DEED2026 rates](https://mn.gov/uimn/employers/wages-taxes/tax-rates/) |
| UI base rate and experience component | Base 0.40%; experience 0%-8.90%; new employer industry component assigned separately | [DEED2026 rates](https://mn.gov/uimn/employers/wages-taxes/tax-rates/) |
| New employer industry-component examples | Professional/scientific/technical 1.08%; information 1.29%; roofing 5.27%; residential building 1.98%; not one generic construction maximum | [2026 industry table](https://www.uimn.org/employers/wages-taxes/tax-rates/new-employer-rates.jsp) |
| UI additional/special assessments | Additional 14% **of UI tax before assessments**; federal-loan assessment 0% | [DEED2026 rates](https://mn.gov/uimn/employers/wages-taxes/tax-rates/); [calculation sheet](https://mn.gov/uimn/assets/quarterly-total-amount-calculated_tcm1068-548928.pdf) |
| Workforce-development assessment | 0.10% of taxable wages, separate from UI; reimbursing-employer exception | [116L.20](https://www.revisor.mn.gov/statutes/cite/116L.20); [DEED calculation](https://mn.gov/uimn/assets/quarterly-total-amount-calculated_tcm1068-548928.pdf) |
| Paid Leave regular combined premium | 0.88%; ordinary employer minimum 0.44%, employee maximum 0.44%, subject to lawful wage floor | [DEED2026 designation](https://mn.gov/deed/assets/paid-leave-small-employer-premium-rate-designation-acc_tcm1045-716947.pdf); [268B.14](https://www.revisor.mn.gov/statutes/cite/268B.14) |
| Eligible small-employer combined premium | 0.66%; employer minimum 0.22% (derived: 25% of the 0.88% annual rate), employee maximum 0.44%; requires designation, not size alone | [DEED designation](https://mn.gov/deed/assets/paid-leave-small-employer-premium-rate-designation-acc_tcm1045-716947.pdf); [268B.14 subd. 5a](https://www.revisor.mn.gov/statutes/cite/268B.14) |
| Withholding quarterly-deposit exception | Prior quarter withholding 1,500 or less AND prior quarterly return timely | [Booklet, p.8](https://www.revenue.state.mn.us/sites/default/files/2025-12/wh-inst-26.pdf) |
| Annual filing/payment eligibility | Generally prior calendar-year withholding 500 or less; verify assigned status; in-year threshold deposits can still arise | [Booklet, pp.8-9](https://www.revenue.state.mn.us/sites/default/files/2025-12/wh-inst-26.pdf) |
| Withholding electronic payment | 10,000 or more in last 12 months endingJune 30, or other specified business-tax/payroll-service trigger | [Booklet, p.8](https://www.revenue.state.mn.us/sites/default/files/2025-12/wh-inst-26.pdf) |
| W-2/1099 mandatory electronic information filing | **More than 10 combined forms**;10 or fewer may use paper if otherwise permitted | [Booklet, pp.12-13](https://www.revenue.state.mn.us/sites/default/files/2025-12/wh-inst-26.pdf) |

**Regular computer formula.** Annualize period wages and subtract allowances x 5,300. Apply the chart to that result; it is not the annual M1 bracket schedule without the payroll offsets. For a result at/below the first offset there is no table tax. Divide annual formula tax by pay periods and add certified additional withholding, using permitted rounding. [Booklet, p.34](https://www.revenue.state.mn.us/sites/default/files/2025-12/wh-inst-26.pdf).

| Status | Adjusted annual wage band | Formula tax | Official source |
| --- | --- | --- | --- |
| Single | Over 4,700 to 38,010 | 5.35% of excess over 4,700 | [p.34](https://www.revenue.state.mn.us/sites/default/files/2025-12/wh-inst-26.pdf) |
| Single | Over 38,010 to 114,130 | 1,782.09+6.80% of excess over 38,010 | [p.34](https://www.revenue.state.mn.us/sites/default/files/2025-12/wh-inst-26.pdf) |
| Single | Over 114,130 to 207,850 | 6,958.25+7.85% of excess over 114,130 | [p.34](https://www.revenue.state.mn.us/sites/default/files/2025-12/wh-inst-26.pdf) |
| Single | Over 207,850 | 14,315.27+9.85% of excess over 207,850 | [p.34](https://www.revenue.state.mn.us/sites/default/files/2025-12/wh-inst-26.pdf) |
| Married | Over 14,700 to 63,400 | 5.35% of excess over 14,700 | [p.34](https://www.revenue.state.mn.us/sites/default/files/2025-12/wh-inst-26.pdf) |
| Married | Over 63,400 to 208,180 | 2,605.45+6.80% of excess over 63,400 | [p.34](https://www.revenue.state.mn.us/sites/default/files/2025-12/wh-inst-26.pdf) |
| Married | Over 208,180 to 352,630 | 12,450.49+7.85% of excess over 208,180 | [p.34](https://www.revenue.state.mn.us/sites/default/files/2025-12/wh-inst-26.pdf) |
| Married | Over 352,630 | 23,789.82+9.85% of excess over 352,630 | [p.34](https://www.revenue.state.mn.us/sites/default/files/2025-12/wh-inst-26.pdf) |

## The base

**Withholding.** Use wages subject to Minnesota withholding and residence/work-source allocation. Corporate officers performing services are employees; family relationship/cash payment does not itself exempt wages. For most wages, the duty follows federal withholding, with the booklet's state exceptions. A nonresident's anticipated Minnesota wages below 15,300 have a specific 2026 exception; it is not a general resident wage exemption. Pension/annuity W-4MNP, mining royalties, backup withholding, nonresident entertainers and contractor surety deposits are separate withholding regimes. The 2026 booklet gives 6.25% mining royalty withholding,9.85% backup personal-service withholding where applicable,2% nonresident-entertainer tax, and 8% surety deposit for a non-Minnesota construction contract over 50,000 absent approved SDE. Use the actual specialized forms rather than mix them into payroll returns. [Booklet, pp.4-7](https://www.revenue.state.mn.us/sites/default/files/2025-12/wh-inst-26.pdf).

Every new employee completing federal W-4 must complete W-4MN. Without a valid certificate use single/zero allowances. Collect status, allowances, extra withholding and actual Section 2 exemption; do not use the old incorrect “Line 7” description. Exempt certificates need annual renewal. Submit required copies when more than 10 allowances, Section 2A/B with expected pay over 200 weekly, or suspected excessive allowances; retain the actual signed certificate and follow current form instructions for timing. Federal allowances cannot simply be copied from the redesigned W-4. [Booklet, pp.3,6](https://www.revenue.state.mn.us/sites/default/files/2025-12/wh-inst-26.pdf).

Separate supplemental payments use 6.25%. Where regular and supplemental payments are paid together but separately identified, choose the permitted aggregate or separate calculation; if not separately identified, aggregate. This collection rate does not establish the employee's final tax rate or eliminate the need for additional withholding/estimates. [Booklet, p.7](https://www.revenue.state.mn.us/sites/default/files/2025-12/wh-inst-26.pdf).

**UI.** Register covered employment in the UI/Paid Leave employer system and obtain the actual coverage/rate determination. Do not import the old generic 1,500 quarter/20 week threshold into every Minnesota industry or assume a paid owner is exempt without the coverage test. Determine agricultural, domestic, nonprofit/reimbursement, corporate-owner, predecessor/successor and multi-state localization rules for the actual employer. New employers generally retain industry assignment until more than two years of wage experience; do not claim three years at a single 9% rate. UI is an employer cost and cannot be deducted from employee wages. Report gross wages even after the taxable base is exhausted. [DEED2026 rates](https://mn.gov/uimn/employers/wages-taxes/tax-rates/); coverage details pending below.

For a taxpaying employer, compute quarterly taxable wages x(experience/new-industry component+0.40% base); multiply that tax by 14% additional assessment. The federal-loan assessment is 0% for 2026. Sum UI tax/assessments and truncate to whole dollars **at account total**, then separately compute taxable wages x 0.10% workforce assessment and truncate that to whole dollars; add the two totals. Do not apply 14% to wages or add 0.1% before computing the 14% tax assessment. Quarterly rounding differs from truncating one annual estimate. [DEED quarterly calculation](https://mn.gov/uimn/assets/quarterly-total-amount-calculated_tcm1068-548928.pdf); [116L.20](https://www.revisor.mn.gov/statutes/cite/116L.20).

**Paid Leave.** Premium collection and benefits began January 1,2026. It is distinct from UI with a different annual wage ceiling. Use the Paid Leave premium notice and current state wage-cap determination rather than copying the old 176,100 federal base or the UI44,000 base. The state designation PDF describes a rounded 185,000 ceiling while 268B.14 references the federal earnings ceiling; that discrepancy is explicitly unresolved below. All numerical premium examples below stay below either candidate ceiling. [DEED designation](https://mn.gov/deed/assets/paid-leave-small-employer-premium-rate-designation-acc_tcm1045-716947.pdf); [268B.14](https://www.revisor.mn.gov/statutes/cite/268B.14).

At ordinary 0.88%, employers fund at least 0.44% and may absorb more; employee deduction cannot breach the applicable minimum-wage floor. Small-employer designation requires 30 or fewer employees under the maximum-quarter record rule and average wages within 150% of the state average during the basis period, with reporting compliance. Use the annual notice, combining relevant same-FEIN accounts. The reduced total 0.66% leaves a minimum 0.22% employer share; employee maximum stays 0.44%. New-employer estimates and later recalculation have statutory rules. Private-plan coverage needs actual approval and scope; it is not an election to stop paying because a private disability policy exists. [268B.14](https://www.revisor.mn.gov/statutes/cite/268B.14); [DEED designation](https://mn.gov/deed/assets/paid-leave-small-employer-premium-rate-designation-acc_tcm1045-716947.pdf).

The existing benefits/HR topics remain distinct: qualifying medical/family/bonding/safety/military events,12 week medical/12 week family and 20 combined cap, wage-replacement tiers, job protection/health insurance, FMLA/ESST/PTO/disability/workers'comp coordination, notices/posters, employer-response times, private plans and grants. Their detailed current eligibility, calculations and deadlines are **not yet confirmed** here; do not use the old 90%/66%/55%,100 minimum,1.2% premiumcap, December 1 notice or 5-business-day response as defaults. Statutory premium cap is 1.1% under 268B.14 subd. 7. [268B.14](https://www.revisor.mn.gov/statutes/cite/268B.14).

**ESST.** For employees expected to work at least 80 hours in Minnesota in a year, start accrual on day one at 1 hour/30 hours worked, at least 48 hours per accrual year with carryover to 80 hours total. No generic 90 day waiting period delays use of earned hours. Instead of accrual/carryover, provide 48 hours immediately and pay unused time at year-end, OR80 hours immediately without year-end payout/carryover. Do not prorate frontloaded statutory hours for part-timers. No separation payout is required by ESST itself; contractual/commingled PTO can differ. Qualified construction-CBA waiver and specified public responder/official exclusions require actual facts. [DLI FAQ](https://www.dli.mn.gov/sick-leave-FAQs).

Permitted ESST uses include illness/preventive care, qualifying family care, safety reasons and defined closure/communicable-disease reasons, subject to exceptions. Broad family coverage is not simply federal FMLA. Pay the statutory **base rate**, not an automatic federal overtime regular rate including all differentials. Foreseeable-use notice may be up to 7 days under a supplied written policy; unforeseeable notice is as soon as reasonably required, not “never required.” At period end provide used/available hours on an earnings statement or accessible electronic system; a separate bucket on every paper stub is not the only lawful method. Provide the required English/primary-language notice and handbook information, maintain records and avoid retaliation. July 2026 rules require current review for detailed cases/local overlays. [DLI FAQ](https://www.dli.mn.gov/sick-leave-FAQs).

**Pay statements, wage notices and separation.**181.032 requires the written hire notice covering pay/basis, permitted allowances, leave terms, exemption status, deductions, period/payday and employer legal/contact details; retain signed acknowledgement and provide written changes before effect. Translation procedure is request-based under this wage-notice provision, distinct from ESST notice. Pay statements include gross/net pay, hours/rates where required, deductions, period end, employer identity/contact and employee/employer Paid Leave amounts. Electronic access must permit review/printing; required paper requests must be honored. [181.032](https://www.revisor.mn.gov/statutes/cite/181.032).

On discharge, earned wages/commissions are due upon written demand with default after 24 hours; statutory default penalties can run up to 15 days. A voluntary quit ordinarily pays the first regular payday, with a second-payday exception if the first is less than 5 calendar days away, never over 20 days; migrant and money/property audit exceptions have their own conditions. Do not apply the quit 20 day rule to every discharge. PTO payout follows actual entitlement/policy, not a blanket state vacation mandate; deductions from final pay need authority. Criminal theft thresholds, universal equal-liquidated-damages claims and per-stub fines are not confirmed below. [181.13](https://www.revisor.mn.gov/statutes/cite/181.13); [181.14](https://www.revisor.mn.gov/statutes/cite/181.14).

**Classification.** General withholding classification considers behavioral/financial control and relationship; the 2026 manual imposes a 3%-of-wages tax for misclassification that the worker cannot claim as withholding. UI and labor-specific tests must be separately applied, not an invented universal “nine-factor” safe harbor. [Booklet, p.4](https://www.revenue.state.mn.us/sites/default/files/2025-12/wh-inst-26.pdf).

For building construction/improvement,181.723 subd. 4 requires a business entity meeting **all 14 conditions at the time of services**: independent establishment; own/rented business facilities/tools; public/multiple-customer offering; required taxIDs/forms/returns; good standing; required UI account; workers'comp; licences/registrations; proper signed written per-job/commission/bid contract; entity invoices/noncash payment; actual control; main costs; completion responsibility; profit/loss risk. Contracts generally must be executed within 30 days of starting, subject to change-order rule. Keep the supporting classification file at least 3 years. Registration alone does not establish all conditions; old ICEC/annual-fee statements are not current instructions. Misclassification can yield compensatory damages, up to 10,000 per individual and per violation,1,000 per day of obstruction and knowing/repeated individual liability. Do not substitute old 5,000/automatic-treble-damages claims. Prevailing-wage/apprenticeship/public-project and workers'comp requirements remain separate obligations. [181.723](https://www.revisor.mn.gov/statutes/cite/181.723).

## Deadlines and filing

1. Register Revenue withholding before withholding; the 2026 booklet specifies a 100 nonregistration penalty. Add the account to the existing seven-digit taxID when appropriate. Register UI/Paid Leave separately, confirm coverage, actual 2026 UI determination and Paid Leave notice. Payroll providers do not relieve employer responsibility. [Booklet, p.3](https://www.revenue.state.mn.us/sites/default/files/2025-12/wh-inst-26.pdf).
2. Determine **deposit** schedule separately from return frequency. If prior-quarter state withholding exceeds 1,500, follow the applicable federal monthly or semiweekly deposit schedule. Monthly deposits are due the 15 th following month; semiweekly Wednesday/Thursday/Friday paydays deposit nextWednesday, other paydays nextFriday. Minnesota did not adopt the federal one-day rule. If prior-quarter withholding is 1,500 or less and the previous return was timely, the quarterly-deposit exception may apply. Annual filers with prior-year 500 or less can payJanuary 31, but when current withholding exceeds 500 an in-year deposit is due by the last day of the following month, subject to December rules. [Booklet, pp.8-9](https://www.revenue.state.mn.us/sites/default/files/2025-12/wh-inst-26.pdf).
3. In e-Services select withholding and period, enter wages/employee count/tax withheld, reconcile deposits/credits, submit and pay; retain acceptance/reference. Quarterly returns are dueApril 30, July 31, October 31, January 31, adjusted for closed days, including zero returns. Approved seasonal/annual filing has its own status. **MWR is the reciprocity certificate, not a quarterly withholding return.** There is no supported W-3M reconciliation form requirement here. [Booklet, pp.9-13](https://www.revenue.state.mn.us/sites/default/files/2025-12/wh-inst-26.pdf).
4. Provide/submit W-2 s and required 1099 withholding information byJanuary 31, adjusted for closed days. More than 10 combined forms requires electronic filing; KeyandSend, SimpleFile and authorized EFW2/Publication 1220 formats are available. Do not resend paper after electronic acceptance. Reconcile payroll, all period returns/deposits and W-2 box 17; the old automatic-one-dollar-audit claim is unsubstantiated. W-2 state allocation follows resident/work facts and reciprocal certificates. Correct W-2 c and each affected period in e-Services; federal changes affecting state wages are reported within 180 days. Retain tax records at least 4 years and close the account after final returns. [Booklet, pp.6,12-14](https://www.revenue.state.mn.us/sites/default/files/2025-12/wh-inst-26.pdf).
5. UI/Paid Leave wage-detail reports and payments are due the last day of month after each quarter, with weekend/holiday adjustment. Submit required employee wages/hours/identifiers, zero reports where no employees, and complete all reporting before termination. Joint and Paid Leave-only accounts use the joint employer system; preserve payment and rate/assessment reconciliation separately from Revenue tax. [DEED due dates](https://mn.gov/uimn/employers/wages-taxes/due-dates/); [268B.14](https://www.revisor.mn.gov/statutes/cite/268B.14). Exact current portal field/file layouts are pending below.

## Penalties and interest

Withholding late-payment penalties are 5% for 1-30 days,10% for 31-60,15% after 60; late filing adds 5% of unpaid tax. Wrong mandatory payment method adds 5%; repeat delinquency can add 25%, and extended nonfiling has the greater-of 5%/100 charge under notice conditions. W-2/information-return failures have 50 per event up to 25,000 annually; W-4MN false employee certificate 500 and employer non-submission 50 each are distinct.2026 interest is 7% on applicable tax plus penalty using actualdays/365. [Booklet, pp.6,8,14](https://www.revenue.state.mn.us/sites/default/files/2025-12/wh-inst-26.pdf). UI/Paid Leave late-report/interest schedules need the actual notices/current statutes; do not repeat the old 25 minimum or 250 peremployee claim as confirmed law.

## Cross-border points

Wage reciprocity covers **Michigan and North Dakota**, with a new MWR each year and copies submitted as required. Wisconsin is not reciprocal. Resident wages can require Minnesota withholding wherever performed, with the other-state withholding worksheet; nonresident Minnesota work, deferred awards/severance, interstate carriers, aircrew and entertainers have specific rules. UI/Paid Leave localization and ESST hours are separate tests; employee residence alone does not choose the UI state. [2026 booklet, pp.4-6,12](https://www.revenue.state.mn.us/sites/default/files/2025-12/wh-inst-26.pdf).

## Two worked examples that recompute

**1: ACME Software StudioLLC.** Retain five annual salaries 120,000/95,000/85,000/70,000/55,000 and two 10,000 bonuses. Assume all five are covered after actual owner-coverage review, all work in Minnesota and none reaches the Paid Leave ceiling. For the 95,000 single employee with 2 allowances, adjusted annual wages 84,400; formula annual tax 4,936.61, or 189.87 biweekly before optional whole-dollar rounding/additional withholding. Each separate 10,000 bonus withholds 625. Annual UI taxable wages 220,000 at an assumed 1.4% experience component plus.4% base yield 3,960 before assessment,554.40 additional and 220 workforce: annual **untruncated planning total 4,734.40**. Actualquarterly amounts truncate separately.

The existing 425,000 salary budget omitted 20,000 bonuses: actual premium wages 445,000 give regular employer 1,958 andemployee 1,958. If formally eligible for small-employer treatment, employer 979 andemployee 1,958, total 2,937. Five 2,080 hour workers accrue at least 48 each after cap,240 total; at an invented 40 base rate, fullusecost 9,600. This is a planning ceiling, not a reason to withhold leave.

```oa-check
name: Minnesota ACME 2026 payroll and premium decision
inputs:
  wage: 95000
  allowances: 2
  ui_wages: 220000
  salary_sum: 425000
  bonuses: 20000
steps:
  - adjusted: wage - allowances * 5300
  - annual_wh: 1782.09 + (adjusted - 38010) * 0.068
  - biweekly: round(annual_wh / 26, 2)
  - bonus_wh: 10000 * 0.0625
  - ui_before: ui_wages * (0.014 + 0.004)
  - ui_additional: ui_before * 0.14
  - workforce: ui_wages * 0.001
  - ui_plan: ui_before + ui_additional + workforce
  - premium_wages: salary_sum + bonuses
  - regular_employer: premium_wages * 0.0044
  - small_employer: premium_wages * 0.0022
  - employee: premium_wages * 0.0044
  - esst_hours: 5 * min(2080 / 30, 48)
  - esst_cost: esst_hours * 40
expected:
  adjusted: 84400
  annual_wh: 4936.61
  biweekly: 189.87
  bonus_wh: 625
  ui_plan: 4734.4
  regular_employer: 1958
  small_employer: 979
  employee: 1958
  esst_hours: 240
  esst_cost: 9600
```

**2: NorthPoint RoofingLLC and Sam.** Preserve the existing three 60,000 employees plus Sam paid 60,000, company tools/dispatch, exclusive jobs, hourly invoices and no independent qualifying business. These facts fail the all-elements construction test. If the actual 2026 new-roofing component 5.27% applies, Sam's 44,000 taxable annual wages produce 2,494.80 before 14% assessment; annual untruncated UI+workforce planning exposure 2,888.072. A genuinely qualifying independent business would have no covered employee wages for that contract. Minnesota's separate 3% misclassification tax on 60,000 is 1,800; it is not a worker withholding credit. A60,000 covered premium base has 264 regular employer plus 264 employee Paid Leave. Actuallatecharges, damages, coverage and corrections require the period records; the old 9%/3,870/rough 6% withholding example is superseded.

```oa-check
name: Minnesota Sam classification and current roofing UI
inputs:
  wages: 60000
  base: 44000
  industry: 0.0527
steps:
  - taxable: min(wages, base)
  - before: taxable * (industry + 0.004)
  - additional: before * 0.14
  - workforce: taxable * 0.001
  - ui_plan: before + additional + workforce
  - misclassification_tax: wages * 0.03
  - regular_employer_premium: wages * 0.0044
  - genuine_contractor_employee_ui: 0
expected:
  taxable: 44000
  before: 2494.8
  ui_plan: 2888.072
  misclassification_tax: 1800
  regular_employer_premium: 264
  genuine_contractor_employee_ui: 0
```

**3: GoodSoftInc. localization decision.** Retain 35 employees at 114,000 each:3,990,000, not exactly the earlier rounded 4 million. If all 35 are Minnesota-covered, regular employer premium 17,556 plus the same employee amount. If the three exclusively out-of-state workers in WI/ND/TX are properly excluded after actual localization,32 covered workers produce 3,648,000 premium wages and 16,051.20 each share. Neither residence nor reciprocity alone proves exclusion. UnlimitedPTO must satisfy ESST; choose lawful accrual or 48-with-year-end-payout/80-without-payout frontloading. Do not backdate a fictional 48-hour “no payout” fix.

```oa-check
name: Minnesota GoodSoft covered headcount decision
inputs:
  salary: 114000
  all_count: 35
  covered_count: 32
steps:
  - all_wages: salary * all_count
  - covered_wages: salary * covered_count
  - all_employer: all_wages * 0.0044
  - covered_employer: covered_wages * 0.0044
  - difference: all_employer - covered_employer
expected:
  all_wages: 3990000
  covered_wages: 3648000
  all_employer: 17556
  covered_employer: 16051.2
  difference: 1504.8
```

## Ask the client first

1. Pay dates/frequency, wages/benefits/bonuses, W-4MN/MWR and year-to-date UI/Paid Leave wages?
2. Residence, all work locations/localization, owner/officer/relative status, industry/NAICS and acquisition history?
3. Revenue/UI/Paid Leave accounts, actual notices, prior-quarter withholding/prior return timeliness and assigned annual/seasonal status?
4. Paid Leave small-employer designation/private-plan approval, employee counts/average wages, wage floor and notice records?
5. Filed periods, payments, W-2/1099 totals, provider changes, amendments and notices?
6. Construction contracts/classification evidence, ESST/PTO/notice policies, hours, local ordinances and separation/demand dates?

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| 2026 withholding booklet. Read for pp.3-14 and computer formula p.34: all state method/certificate/filing/payment/penalty rules. | https://www.revenue.state.mn.us/sites/default/files/2025-12/wh-inst-26.pdf | 2026-11-13 |
| DEED2026 UI rates. Read for base, experience range, industry assignment, assessments and account determination. | https://mn.gov/uimn/employers/wages-taxes/tax-rates/ | 2026-11-13 |
| 2026 new-employer table. Read for professional/information/roofing/residential-building industry components. | https://www.uimn.org/employers/wages-taxes/tax-rates/new-employer-rates.jsp | 2026-11-13 |
| DEED quarterly calculation sheet. Read for separate UI and workforce bases, assessment ordering and account-total truncation. | https://mn.gov/uimn/assets/quarterly-total-amount-calculated_tcm1068-548928.pdf | 2026-11-13 |
| DEED due dates. Read for joint/Paid Leave-only reports, payments, zero reporting and closure. | https://mn.gov/uimn/employers/wages-taxes/due-dates/ | 2026-11-13 |
| 116L.20. Read for workforce assessment and reimbursement exception. | https://www.revisor.mn.gov/statutes/cite/116L.20 | 2026-11-13 |
| 2026 small-employer designation. Read for regular/small premium, employee ceiling, eligibility and stated rounded wage ceiling. | https://mn.gov/deed/assets/paid-leave-small-employer-premium-rate-designation-acc_tcm1045-716947.pdf | 2026-11-13 |
| 268B.14. Read for premium split, wage floor, small-employer basis rules, ceiling, adjustment authority and quarterly payment. | https://www.revisor.mn.gov/statutes/cite/268B.14 | 2026-11-13 |
| DLI ESST FAQ. Read for coverage, accrual, use, frontloading, payout, notice, base pay, records and July 2026 rules. | https://www.dli.mn.gov/sick-leave-FAQs | 2026-11-13 |
| 181.032. Read for hire/change notice, earnings statement and Paid Leave disclosure. | https://www.revisor.mn.gov/statutes/cite/181.032 | 2026-11-13 |
| 181.13/181.14. Read for discharge demand, quit timing, exceptions and statutory penalties. | https://www.revisor.mn.gov/statutes/cite/181.13 ; https://www.revisor.mn.gov/statutes/cite/181.14 | 2026-11-13 |
| 181.723. Read for full 14-condition construction test, documentation, liability and penalties. | https://www.revisor.mn.gov/statutes/cite/181.723 | 2026-11-13 |

Not yet confirmed: exact 2026 Paid Leave annual ceiling: DEED designation PDF describes rounded 185,000 while 268B.14 references federal annual earnings ceiling; use the actual current account notice before capping. FullPaid Leave benefit tiers/eligibility/job-protection/coordination, private-plan fees/grants/notices/responses; UI coverage thresholds/exempt owner/household/agriculture/nonprofit/localization/successor details and late-report/interest schedules; new-hire reporting 20 day claim/penalties; general UI classification rule factors; local Minneapolis/StPaul ordinances and prevailing-wage/workerscomp details; ESST fullJuly 2026 rule application/record-retention/remedies; criminal wage-theft thresholds/per-stub penalties, exactcurrent registration fee and final 2026 file specifications. Old ICEC/9 factor/annualUIdefaults and unsubstantiatedauditpredictions are withdrawn.
