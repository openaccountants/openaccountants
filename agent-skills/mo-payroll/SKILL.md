---
name: mo-payroll
description: "Missouri 2026 withholding formula and MO-941 frequencies, 9,000 UI base and new rates, registration/CW reports, wage administration and unresolved city filings."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/mo-payroll"
  jurisdiction: "US-MO"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Missouri payroll withholding and unemployment insurance, 2026

> **General reference only.** Source-cited draft, not approved by an accountant. For US Treasury Circular 230 §10.37 purposes this is general reference material; a qualified professional must check the facts, current law and forms before filing or taking a position.

## Who this applies to

Employers paying employees who work in Missouri or Missouri residents working elsewhere. This skill owns state **income-tax withholding and unemployment insurance (UI)**, with related employer reporting. Federal payroll figures and returns belong to `us-form-941-940-payroll`; employee annual deductions/credits belong to `mo-income-tax`; entity and nonresident-owner taxation to `mo-corporate-tax`. Use that federal skill for federal wage bases, rates and returns.

Use DOR's published **2026 employer booklet/Form 4282 and withholding formula** for withholding and DES's 2026 rate table for UI. The final 2025 annual income return does not supply payroll rates. Local earnings-tax returns are separate: city-specific current rates, filing rules and remote-work refunds remain explicitly partial below. This is a source-cited writer draft, not an accountant's approval. [2026 employer booklet](https://dor.mo.gov/forms/4282_2026.pdf); [2026 UI rates](https://labor.mo.gov/des/employers/tax-rates).

## Rates, bands and thresholds

All amounts USD. State withholding is employee tax held in trust; Missouri UI is employer cost and cannot be deducted from wages.

| 2026 item | Rule / amount | Official source |
| --- | --- | --- |
| Withholding formula top rate | 4.7% (top bracket of the 2026 formula; do not carry an older top rate) | [2026 formula](https://dor.mo.gov/forms/Withholding%20Formula_2026.pdf) |
| Separate supplemental wages | Optional flat 4.7% when the regular-wage withholding conditions are met, or prescribed aggregate method | [2026 booklet, supplemental wages](https://dor.mo.gov/forms/4282_2026.pdf) |
| Formula annual deduction: single / MFS / married spouse works | 16,100 | [2026 state employer formula](https://dor.mo.gov/forms/Withholding%20Formula_2026.pdf) |
| Formula annual deduction: married spouse does not work | 32,200 | [2026 state employer formula](https://dor.mo.gov/forms/Withholding%20Formula_2026.pdf) |
| Formula annual deduction: head of household | 24,150 | [2026 state employer formula](https://dor.mo.gov/forms/Withholding%20Formula_2026.pdf) |
| UI taxable wage base | First 9,000 of covered wages **per employee per employer for calendar 2026**, with predecessor/interstate credits where allowed | [DES2026 table](https://labor.mo.gov/des/employers/tax-rates); [CW instructions](https://labor.mo.gov/media/21311/download) |
| New employer UI: general, mining and construction | 2.376%; nonprofit/government categories differ | [DES2026 table](https://labor.mo.gov/des/employers/tax-rates) |
| New 501(c)(3) / governmental contributing employer | 1%, or approved reimbursing method | [DES rates](https://labor.mo.gov/des/employers/tax-rates) |
| Experience-rated UI | Ordinary base 0%-6% before maximum-rate surcharge/CRA; actual DES notice controls | [DES rates](https://labor.mo.gov/des/employers/tax-rates) |
| New Shared Work employer | 9% plus applicable adjustments until experienced | [DES rates](https://labor.mo.gov/des/employers/tax-rates) |
| UI wage-report electronic threshold | 50 or more workers, subject to good-cause permission for paper | [Current CW instructions](https://labor.mo.gov/media/21311/download) |
| DOR W-2 electronic threshold | 250 or more; do not replace this with the UI threshold | [2026 booklet, section 21](https://dor.mo.gov/forms/4282_2026.pdf) |
| State minimum wage | 15/hour; covered tipped cash wage at least 7.50 plus make-up to 15 | [2026 DOLIR minimum-wage page](https://labor.mo.gov/dls/minimum-wage) |

The three deduction rows are **Missouri employer formula inputs published by DOR**, not a substitute schedule of federal annual deductions. The formula does not use obsolete personal-allowance amounts or the employee's annual federal-income-tax deduction. Do not predict later individual rate cuts from revenue triggers: use each year's published formula.

## The base

**Withholding calculation.** Obtain the completed MO W-4, filing status, spouse-work checkbox, additional withholding and any valid exempt/military-spouse claim. Annualize taxable wages by 260 daily,52 weekly,26 biweekly,24 semimonthly or 12 monthly. Subtract the appropriate state formula deduction, floor taxable amount at zero, apply the 2026 annual schedule below, divide by annual payroll periods and round withholding to the nearest whole dollar. Apply authorized additional/total-tax instructions as the certificate directs. The employee's actual annual MO-1040 federal-tax deduction, itemization and credits are not built into this routine formula. [2026 formula](https://dor.mo.gov/forms/Withholding%20Formula_2026.pdf); [MO W-4](https://dor.mo.gov/forms/MO%20W-4.pdf).

| Annual formula taxable income | Annual withholding before dividing by periods | Official source |
| --- | --- | --- |
| 0-1,348 | 0 | [2026 formula](https://dor.mo.gov/forms/Withholding%20Formula_2026.pdf) |
| Over 1,348-2,696 | 2% of excess over 1,348 | [2026 formula](https://dor.mo.gov/forms/Withholding%20Formula_2026.pdf) |
| Over 2,696-4,044 | 27 +2.5% of excess over 2,696 | [2026 formula](https://dor.mo.gov/forms/Withholding%20Formula_2026.pdf) |
| Over 4,044-5,392 | 61 +3% of excess over 4,044 | [2026 formula](https://dor.mo.gov/forms/Withholding%20Formula_2026.pdf) |
| Over 5,392-6,740 | 101 +3.5% of excess over 5,392 | [2026 formula](https://dor.mo.gov/forms/Withholding%20Formula_2026.pdf) |
| Over 6,740-8,088 | 148 +4% of excess over 6,740 | [2026 formula](https://dor.mo.gov/forms/Withholding%20Formula_2026.pdf) |
| Over 8,088-9,436 | 202 +4.5% of excess over 8,088 | [2026 formula](https://dor.mo.gov/forms/Withholding%20Formula_2026.pdf) |
| Over 9,436 | 263 +4.7% of excess over 9,436 | [2026 formula](https://dor.mo.gov/forms/Withholding%20Formula_2026.pdf) |

Regular and supplemental wages in one payment use the combined/aggregate method. For separately paid supplemental wages, use the prescribed aggregate calculation less regular withholding already taken, or flat 4.7% where the conditions apply; do not apply flat tax when no regular withholding was required without checking the booklet. Bonuses, overtime, taxable fringe and deferred-compensation payments need their actual wage characterization. MO W-4 line 2 permits additional withholding; line 3 a specified total under its conditions, not an employee's unilateral tax exemption. Exempt claims need eligibility and annual renewal; qualifying military-spouse claims require supporting documents. Retain certificates, and apply the booklet's default when a valid one is absent. [2026 booklet, sections 9-12](https://dor.mo.gov/forms/4282_2026.pdf); [MO W-4 instructions](https://dor.mo.gov/forms/MO%20W-4.pdf).

**Register and maintain accounts.** DOR withholding registration uses MyTax Missouri/Form 2643 and a Missouri Tax ID; DES UI uses UInteract and its employer account. One account does not replace the other. Update owners/addresses with Form 126 and use Form 2827 for DOR authority as needed. A payroll service's filing/payment error does not remove employer liability. DOR's online filing, ACH debit and TXP/ACH-credit channels have distinct reconciliation requirements. The old 8,000 annual EFT threshold was not substantiated by the current booklet and is not a current rule here. Confirm the account's required payment channel and quarter-monthly instructions rather than inferring paper eligibility from that old figure. [2026 employer booklet, pp.2-3](https://dor.mo.gov/forms/4282_2026.pdf); [DES CW instructions](https://labor.mo.gov/media/21311/download).

**UI coverage and wages.** General employers ordinarily become liable through 1,500 wages in a calendar quarter, a worker in 20 different weeks of the current/prior year, FUTA liability with a Missouri worker, or successorship. Domestic coverage uses 1,000 cash wages/quarter; agricultural coverage 10 workers/20 weeks or 20,000 cash wages/quarter, plus the other applicable triggers.501(c)(3) coverage has a 4-workers/20-weeks test. Notify DES within 30 days of liability/acquisition. Do not assume withholding coverage, federal payroll treatment and UI coverage are identical. [DES liability](https://labor.mo.gov/des/employers/liability); [employer handbook, pp.5-7](https://labor.mo.gov/media/21246/download).

Report covered cash and noncash remuneration, including bonuses, commissions, tips and other remuneration within DES's wage definition. Corporate officers' compensated services can be covered. Sole-proprietor owner/spouse/parents/children-under 21 and partners have specific exclusions; LLC treatment follows tax classification and actual applicable rule. Do not extend a sole-proprietor family exclusion to every corporation. Review real-estate/direct-seller, student, religious/nonprofit and other statutory exclusions against the actual facts. [Reportable wages/employment](https://labor.mo.gov/des/employers/reportable); [DES handbook, excluded employment](https://labor.mo.gov/media/21246/download).

For each employee, current-quarter taxable UI wages equal the portion of current covered wages remaining below the 9,000 annual base after eligible prior-quarter wages. Report **all gross covered wages**, plus current-quarter excess, not only the taxable 9,000. Predecessor wages and wages the same employer previously reported as taxable in another state can reduce the remaining base under the instructions; an unrelated former employer's wages are not a universal credit. [CW instructions, items 4-5](https://labor.mo.gov/media/21311/download).

Experience rates reflect taxable payroll, contributions and charged benefits; first experience eligibility generally follows two full calendar years. Maximum-rate surcharges can rise in stages to 1.5 percentage points, with CRA applied as a percentage adjustment. New-employer published 2.376 already reflects the adjustment: do not add 2.7% again. Eligible voluntary payments may reduce the rate if made by January 15, shifted for a closed day; evaluate DES's quoted reduction rather than treating the payment as automatically worthwhile. [DES rates](https://labor.mo.gov/des/employers/tax-rates).

The automation adjustment redirects an amount from first-quarter UI taxes; **no additional first-quarter tax is due**. The currently published cap is 0.020% of the relevant preceding 12-month taxable wages, not a new employee deduction. DES notifies the amount; redirected amounts are excluded from the rate calculation/FUTA certification as described. Do not add a historical generic “automation surcharge” on top of the 2026 notice. [DES automation adjustment](https://labor.mo.gov/des/employers/tax-rates).

**Classification.** DES applies its twenty-factor common-law analysis: instructions, training, integration, personal service, hiring/supervising/paying assistants, continuity, set hours, full-time requirement, premises, sequence, reports, hour/week/month pay, expenses, tools/materials, investment, profit/loss, multiple firms, public availability, discharge and termination rights. Weigh the relationship; a 1099, LLC, written contractor label, possession of tools or one isolated factor does not settle it. Federal IRS classifications/Section 530 relief do not establish Missouri UI exemption. Preserve facts and seek the actual DES determination rather than assume a federal safe harbour binds the state. [DES reportable employment](https://labor.mo.gov/des/employers/reportable); [handbook, pp.8-10](https://labor.mo.gov/media/21246/download).

## Deadlines and filing

DOR frequency is based on the specified preceding periods and actual account assignment, not the old generic July-to-June average table.

| Withholding category | Current qualifying test | Filing/payment | Official source |
| --- | --- | --- | --- |
| Monthly | Withheld 500 or more/month in at least 2 months of preceding 12 | MO-941 monthly; normally 15th following month, but third month of quarter due end of following month | [2026 booklet, sections 13-14](https://dor.mo.gov/forms/4282_2026.pdf) |
| Quarterly | Not monthly;100 or more in at least 1 of preceding 4 quarters | MO-941 by last day after quarter | [2026 booklet](https://dor.mo.gov/forms/4282_2026.pdf) |
| Annual | Less than 100 in each preceding 4 quarters | MO-941 January 31 following | [2026 booklet](https://dor.mo.gov/forms/4282_2026.pdf) |
| Quarter-monthly | Withheld 9,000 or more in each of at least 2 months of preceding 12 | Four deposit periods/month, with **monthly** reconciliation | [2026 booklet; official 2026 calendar](https://dor.mo.gov/forms/4282_2026.pdf); [calendar](https://dor.mo.gov/forms/2414W_2026.pdf) |

Quarter-monthly means days 1-7,8-15,16-22,23-end: **four**, not eight. Generally remit within 3 banking days after period end, or the applicable 4-day depository rule; follow the published calendar. Minimum interim payment is 90% of actual period liability or 100% of DOR's estimate under the authorized method; reconcile the balance by the monthly return date. ACH-credit payment does not itself replace the required reconciliation. Quarter-monthly status generally continues 12 months before requesting less frequent treatment. A new employer's initial assignment uses expected withholding, not an automatic monthly default. Notify DOR of an incorrect assignment; do not unilaterally switch. [2026 booklet, sections 13-17](https://dor.mo.gov/forms/4282_2026.pdf); [calendar](https://dor.mo.gov/forms/2414W_2026.pdf).

Apply weekends/holidays. Ordinary 2026 withholding Q3 is due November 2,2026; Q4/annual February 1,2027. Monthly March/June/September/December are the **quarter-ending monthly exception**, not always the 15th. File an assigned zero MO-941 until the account is properly closed, including inactive periods unless the actual seasonal assignment says otherwise. Amend the affected period on MO-941; use the stated authorization/refund process rather than offset another period without approval. Form 4854 refund claims generally use later of 3 years from return or 2 years from payment, with the no-return rule distinct. [2026 booklet, sections 14,18](https://dor.mo.gov/forms/4282_2026.pdf).

Timely eligible employers can retain compensation on annual cumulative withholding:2% of first 5,000,1% of next 5,000,0.5% above 10,000. Government employers and agents handling multiple accounts have special restrictions; do not claim the full first bands afresh every month or for each client without the applicable rule. [2026 booklet, section 19](https://dor.mo.gov/forms/4282_2026.pdf).

**Annual statements.** Provide employee W-2 copies by January 31 following wages, subject to closed-day rules. DOR's annual MO W-3/W-2/1099-R reporting distinguishes required electronic filing by January 31 from permitted paper by the last day of February;250 or more W-2 s require electronic submission. For 2026 wages the ordinary shifted dates are February 1,2027 electronically and March 1,2027 for allowed paper, subject to final annual specifications. MO W-3 does not replace the last MO-941. Correct W-2 withholding with amended MO-941/W-3 and W-2 c as instructed. Retain undeliverable employee statements at least 4 years. The booklet lists participating CF/SF forms and requires IRS approval and notification to Missouri; it does not establish universal 1099-NEC automatic transmission. Confirm current information-at-source reporting separately. [2026 booklet, section 21](https://dor.mo.gov/forms/4282_2026.pdf).

**DES quarterly CW report.** Use UInteract or authorized Quarterly Contribution and Wage Report **MODES-4**, with continuation MODES-10B, not the old unverified “MODES-4-7”. File every quarter even at 0% rate, reimbursing status or zero wages. Ordinary deadlines April 30, July 31, October 31, January 31 after the relevant quarter; closed days shift.2026 Q3 therefore November 2,2026 and Q4 February 1,2027. Report each worker's name/SSN/gross wages, current excess, taxable wages, monthly worker counts for the pay period including the 12th, and actual notice rate. Employers with 50 or more workers generally file electronically, subject to good-cause paper permission. Leave the federal-interest/automation item for DES notice rather than inventing an assessment. [CW instructions](https://labor.mo.gov/media/21311/download); [DES handbook, pp.14-16](https://labor.mo.gov/media/21246/download).

**New hires and wage administration.** DOR's 2026 booklet directs reporting a new employee within 20 days by sending the completed MO W-4 copy to DOR's new-hire reporting channel; use the designated new-hire instructions and retain reporting evidence. Complete the actual instructions for rehires, electronic/multistate reporting and required identifiers; do not treat a routine state tax-certificate retention file as proof reporting occurred. Keep transmission evidence. [2026 booklet, new hire reporting](https://dor.mo.gov/forms/4282_2026.pdf); [MO W-4](https://dor.mo.gov/forms/MO%20W-4.pdf).

On discharge, earned wages are due on the day of dismissal. The written-request/seven-day provision concerns the additional continuing-wage penalty, capped at 60 days; it does not postpone the original due date. Commission/audit cases have an exception. Quit pay, routine pay-frequency scope, required pay-statement particulars, deductions and contract benefits need their actual state rules; the old universal “at least monthly” assertion is not adopted. [290.110](https://revisor.mo.gov/main/OneSection.aspx?section=290.110); [DOLIR wage administration](https://labor.mo.gov/dls/general).

For covered 2026 work, state minimum wage is 15/hour; tipped cash at least 7.50 plus the employer's make-up if tips do not reach 15. Retail/service businesses below 500,000 gross sales and specified employees/agriculture have exemptions; federal coverage can still matter. HB567 removed the prior automatic future CPI increases, so do not describe annual CPI indexing after 2026 as current law. Overtime and public-works prevailing wage have their own coverage and calculation rules. [Current minimum-wage page](https://labor.mo.gov/dls/minimum-wage).

The statewide earned-paid-sick-time requirement was repealed effective August 28,2025. The old 1 hour/30 hours,40/56 annual caps and 2025 accrual records are historical, not a 2026 statewide accrual mandate. Contract/promised leave can remain enforceable. The old assertion that St. Louis Ordinance 71926 independently mandates ongoing accrual is withdrawn:290.528 expressly preempts local employment-benefit requirements exceeding state law. Do not delete contract benefits or assume repeal cures accrued 2025 claims. [DOLIR repeal announcement](https://labor.mo.gov/dls/prevailing-wage); [290.528](https://revisor.mo.gov/main/OneSection.aspx?section=290.528); [wage/benefit administration](https://labor.mo.gov/dls/general).

## Penalties and interest

DOR's 2026 booklet gives 5% per late-filing month/fraction up to 25%,5% late payment, possible 5% negligence and 50% fraud, and personal 100% trust-tax liability for willful failure to collect/account/pay. Calendar 2026 interest is 7% annually, daily factor 0.0001918; it is published annually, not a quarterly rate or universal UI rate. The old 25 zero-tax-return penalty and 8,000 EFT threshold remain unconfirmed, not assumed. Failure to file required wage statements can attract 2 per statement up to 1,000 unless reasonable-cause/non-willful-neglect conditions apply. [2026 employer booklet, sections 20-21](https://dor.mo.gov/forms/4282_2026.pdf).

UI delinquency is separate. CW instructions assess greater of 10% contributions or 100 after the first full overdue month, then greater of 20% or 200 after the second, using the actual due/penalty dates. The handbook describes further monthly delinquency charges and an aggregate ceiling; use DES's assessment for continuing delinquency rather than treating 20% as a universal final cap. UI interest is variable and accrues by month/part from the due date; obtain DES's applicable amount, not DOR's income-tax 7%. Estimated assessments can result from missing reports. [CW instructions](https://labor.mo.gov/media/21311/download); [DES handbook, pp.15-16](https://labor.mo.gov/media/21246/download).

## Cross-border points

**Withholding:** services physically performed in Missouri generally require Missouri withholding even for an out-of-state employer/remote worker. A nonresident working wholly outside Missouri is not taxable merely because the employer is headquartered here. For partly Missouri nonresident wages, first calculate withholding **as if all wages were taxable**, then multiply by Missouri wages divided by total federal wages; do not apply the progressive schedule directly to the lower Missouri-only wage base. Residents working elsewhere may require Missouri withholding for the excess over the other state's withholding, with MO W-4C affidavit relief as instructed. No general reciprocal wage exemption with neighbouring states is assumed. [2026 booklet](https://dor.mo.gov/forms/4282_2026.pdf); [DOR remote-work instructions](https://dor.mo.gov/taxation/business/remote.html).

Interstate rail/motor-carrier employees, air/water transport and military spouses have special federal/state protection and fact tests. Transient employers not domiciled in Missouri and expecting business under 24 months can have special registration/bond requirements. Nonresident entertainer venues have a separate 2% withholding on gross event compensation exceeding 300 and MO-2ENT/MO-1ENT, distinct from ordinary payroll and owner distributions. Nonresident partner/shareholder withholding is annual entity work with specific exceptions; household withholding can be elective even where UI applies. [2026 booklet, pp.2-5](https://dor.mo.gov/forms/4282_2026.pdf).

**UI localization:** apply coverage tests in sequence: localized services, including incidental temporary out-of-state work; otherwise base of operations in a state where services occur; otherwise direction/control in a state of service; otherwise residence with some service there when earlier tests fail. Residence or headquarters alone is not the first test, and UI normally reports the whole covered service to one state, not wage-days split like income tax. Approved interstate reciprocal coverage arrangements and foreign/maritime services have special rules. [DES handbook, p.17](https://labor.mo.gov/media/21246/download).

**City earnings taxes:** preserve the distinct Kansas City versus St. Louis City jobs; St. Louis County, Clayton and other suburbs are not automatically within St. Louis City. Exact corporate boundaries and actual workdays/delivery routes matter; a postal city name or headquarters does not establish work situs. The old 1% rate assumptions, resident/worldwide versus nonresident-work sourcing, employer-location duties, KC RD-110/RD-109/RD-108/RD-112/RD-113, St. Louis W-10/W-11/E-1/E-4/E-5/E-6, thresholds, deposits, annual reconciliation/refunds, remote-day litigation (including the old Boles v. City of St. Louis citation/date) and local penalties were not re-established from permitted state-hosted sources. They are **unresolved city rules**, not current filing instructions. The cases below retain the original inputs and conditional 1% arithmetic so the historical work is reviewable, while withholding/UI use current state rules. Do not conclude that an unresolved local rule means no local filing. The old continued St. Louis sick-leave mandate is separately corrected above.

## Two worked examples that recompute

**Formula and UI base decision.** Invented regular employee with 35,000 annualized taxable wages, monthly payroll, married/spouse works MO W-4, no additional withholding. Deduct 16,100: annual formula taxable 18,900, annual tax 707.808, divide 12 and round to 59/month. Separately, if a new general employer pays that worker 3,000 this quarter after 7,500 covered prior wages, only 1,500 remains under the 2026 UI base; current UI35.64 at 2.376%, rather than 71.28 on all 3,000. Employee withholding and employer UI are not netted.

```oa-check
name: Missouri 2026 monthly withholding formula
inputs:
  annual_wages: 35000
  formula_deduction: 16100
  periods: 12
steps:
  - annual_taxable: annual_wages - formula_deduction
  - annual_tax: 263 + (annual_taxable - 9436) * 0.047
  - monthly_withholding: round(annual_tax / periods, 0)
expected:
  annual_taxable: 18900
  monthly_withholding: 59
```
```oa-check
name: Missouri UI remaining base decision
inputs:
  prior_covered: 7500
  quarter_wages: 3000
  base: 9000
  new_rate: 0.02376
steps:
  - remaining: max(base - prior_covered, 0)
  - taxable: min(quarter_wages, remaining)
  - ui: round(taxable * new_rate, 2)
  - incorrect_full_wages: round(quarter_wages * new_rate, 2)
expected:
  remaining: 1500
  taxable: 1500
  ui: 35.64
  incorrect_full_wages: 71.28
```

**Preserved employer profiles, corrected for 2026.** All are invented. These are annual UI illustrations assuming covered services/no predecessor credits and wages above the base, not quarterly returns. City amounts are explicitly conditional at an assumed validated 1% and do not establish the unverified current legal obligations.

| Original profile and people | Preserved facts | Corrected 2026 state UI / conditional city arithmetic |
| --- | --- | --- |
| Cottonwood Bakery, LLC, Kansas City | Anya KC resident 52,000 all on site; Brendan Lee's Summit 48,000 all on site; Carla Independence 26,000,20 hours/week:8 at KC store+4 KC deliveries+8 outside | With actual assumed 2% experience notice:3 x 9,000 x 2%=540, replacing 570 at old 9,500 base. Carla's assumed city fraction 12/20=60%, city wages 15,600; conditional city tax 520+480+156=1,156 |
| Riverfront Engineering, P.C.,1010 Market Street, St. Louis City | David city resident 115,000,3 office/2 home-city days; Erin Webster Groves 72,000 city on site; Frank city resident 58,000 home-city; Grace Clayton 95,000 wholly remote in Clayton | With actual assumed 1.5% notice:4 x 9,000 x 1.5%=540, replacing 570. Conditional city amounts 1,150+720+580+0=2,450; Grace is not allocated to the city merely by HQ |
| Heartland Auto Repair, Columbia | Hannah 54,000 and Ian 42,000 | With actual assumed 2.7% experience notice:2 x 9,000 x 2.7%=486, replacing 513. If instead new general employer, published 2.376% gives 427.68; do not call 2.7% the new rate |

Cottonwood's old 480/month, Riverfront's 1,250/month and Heartland's 370/month withholding were unsupported approximations without complete MO W-4/pay-period inputs. Do not report them as computed tax. Frequency follows actual prior-period tests and DOR assignment;480 or 370 monthly averages alone do not prove the old quarterly 100-499/month rule. Riverfront monthly liability likewise needs actual qualifying months. New-hire and local filings still need dated evidence, not the old assumed calendar.

```oa-check
name: Missouri preserved Cottonwood and Riverfront UI cases
inputs:
  ui_base: 9000
  bakery_workers: 3
  bakery_notice_rate: 0.02
  engineering_workers: 4
  engineering_notice_rate: 0.015
steps:
  - bakery_ui: bakery_workers * ui_base * bakery_notice_rate
  - engineering_ui: engineering_workers * ui_base * engineering_notice_rate
expected:
  bakery_ui: 540
  engineering_ui: 540
```
```oa-check
name: Missouri Heartland actual versus new rate decision
inputs:
  workers: 2
  ui_base: 9000
  assumed_experience_rate: 0.027
  published_new_rate: 0.02376
steps:
  - experience_ui: workers * ui_base * assumed_experience_rate
  - new_ui: round(workers * ui_base * published_new_rate, 2)
  - difference: round(experience_ui - new_ui, 2)
expected:
  experience_ui: 486
  new_ui: 427.68
  difference: 58.32
```

## Ask the client first

1. Legal entity, tax year, all actual work/residence addresses, remote/multistate days, UI localization and city boundaries?
2. MO W-4/W-4C, spouse-work/exempt/military documentation, pay frequency and regular/supplemental taxable wages?
3. DOR/DES IDs, assigned filing/payment frequency, actual DES2026 rate/adjustments, provider authority and notices?
4. Per-worker covered gross/prior wages, predecessor/interstate wage credits, family/officer/contractor roles and current/prior coverage tests?
5. Dated returns/deposits, annual statements, new-hire transmissions, zero periods, claims/benefit charges and account changes?
6. Hiring/discharge/quit dates, promised leave/benefits, minimum-wage/tipped/industry coverage and any local filing/refund obligations?

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| 2026 employer booklet/Form 4282. Read for withholding coverage, certificates, supplemental wages, registration, frequencies/deposits, MO-941, statements, new hires and penalties. | https://dor.mo.gov/forms/4282_2026.pdf | 2026-11-13 |
| 2026 withholding formula. Read for annualization, published state deduction inputs, eight bands and whole-dollar rounding. | https://dor.mo.gov/forms/Withholding%20Formula_2026.pdf | 2026-11-13 |
| MO W-4. Read for certificate selections, extra/total/exempt instructions and new-hire channel. | https://dor.mo.gov/forms/MO%20W-4.pdf | 2026-11-13 |
| 2026 quarter-monthly calendar. Read for four periods, banking-day deadlines and reconciliation. | https://dor.mo.gov/forms/2414W_2026.pdf | 2026-11-13 |
| DES2026 tax rates. Read for 9,000 base,2.376 new/1 nonprofit rates, experience/contribution-rate-adjustment/surcharges, voluntary payments and automation redirection. | https://labor.mo.gov/des/employers/tax-rates | 2026-11-13 |
| Current CW instructions. Read for reporting,50-worker electronics,9,000 base, predecessor/interstate credits, quarterly filing and penalties. | https://labor.mo.gov/media/21311/download | 2026-11-13 |
| DES employer handbook. Read for coverage, registration, exclusions, classification, reporting, penalties and localization; historical rate tables superseded by 2026 DES page. | https://labor.mo.gov/media/21246/download | 2026-11-13 |
| DES liability. Read for general/domestic/agricultural/nonprofit coverage triggers. | https://labor.mo.gov/des/employers/liability | 2026-11-13 |
| DES reportable employment. Read for covered wages, exclusions and twenty-factor classification. | https://labor.mo.gov/des/employers/reportable | 2026-11-13 |
| DOR remote-work resources. Read for nonresident/all-wage-first proportional withholding. | https://dor.mo.gov/taxation/business/remote.html | 2026-11-13 |
| DOLIR minimum wage. Read for 2026 minimum/tipped wages, exemptions and repeal of automatic indexing. | https://labor.mo.gov/dls/minimum-wage | 2026-11-13 |
| DOLIR repeal announcement. Read for August 28,2025 sick-time repeal; voluntary benefits distinction. | https://labor.mo.gov/dls/prevailing-wage | 2026-11-13 |
| DOLIR wage administration. Read for discharge and contract-benefit boundaries. | https://labor.mo.gov/dls/general | 2026-11-13 |
| 290.110. Read for same-day discharge wages, written request/seven-day continuing-pay penalty and commission exception. | https://revisor.mo.gov/main/OneSection.aspx?section=290.110 | 2026-11-13 |
| 290.528. Read for preemption of local wage/employment-benefit requirements exceeding state law. | https://revisor.mo.gov/main/OneSection.aspx?section=290.528 | 2026-11-13 |

Not yet confirmed: current city rates and KC/St. Louis returns, deposits, thresholds, resident/nonresident business allocation, remote-work/refund litigation and local penalties; full 2026 elected PTE/nonresident-owner work, special transient/entertainer/transport/military cases, detailed UI exclusions/reimbursement/successor/continuing-delinquency assessments, actual UI interest, detailed quit/pay-frequency/pay-statement/deduction rules, current 1099-NEC/information-source specifications, old 8,000 EFT and 25 zero-return claims, final 2026 annual W-2 specifications and 2027 DOR interest. Legacy local paid-sick-leave mandate is withdrawn; contract/accrued 2025 claims require separate analysis.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `mo-payroll` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/mo-payroll. If neither is available, confirm every figure against the official source pages cited above before relying on it.
