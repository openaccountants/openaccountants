---
name: co-payroll
description: "Colorado 2026 employer wage withholding, UI and FAMLI compliance. Covers the actual DR 1098 calculation, optional DR 0004, payment frequencies, MyUI Employer+ wage reporting, 2026 UI base and introductory rates, and FAMLI nationwide headcount and premium allocation. Labor-law overlays remain expressly partial."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/co-payroll"
  jurisdiction: "US-CO"
  tax_year: "2026"
  last_updated: "2026-11-13"
---

# Colorado payroll v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Employers with Colorado covered wages in 2026. This skill owns state wage
withholding, unemployment insurance (UI) and FAMLI payroll contributions.
Federal withholding/FICA/FUTA and the federal wage cap stay in
`us-form-941-940-payroll`; individual return tax stays in `co-income-tax`.

Labor-law topics from the former file remain identified below, with unresolved
rules reserved rather than carried forward as unsupported figures. Local
occupational privilege tax, workers' compensation and SecureSavings need separate
current analysis; the former referenced local skills are not assumed to exist.

## Ask the client first

1. Each worker's residence, physical workdays, multistate localization and employee/contractor facts.
2. Actual wages, payroll frequency, latest W-4/DR 0004 and any DOR adjustment.
3. UI account, industry, coverage start and actual 2026 rate notice/components.
4. Nationwide qualifying individual headcount in the preceding year and each worker's FAMLI localization.
5. Year-to-date UI/FAMLI wage histories, deductions and contribution elections.
6. Assigned withholding frequency, portal access, private-plan approval and outstanding notices.

## Rates, bands and thresholds

| Item | 2026 rule and conditions | Official source |
|---|---|---|
| Wage withholding multiplier | 4.40% in the actual 2026 DR 1098, not a final annual-return/TABOR determination | https://tax.colorado.gov/sites/default/files/documents/DR_1098_Colorado_Withholding_Worksheet_for_Employees.pdf |
| Default annual worksheet reduction | $11,000 MFJ/qualifying surviving spouse; $5,500 otherwise, only where DR 0004 line 2 is absent/blank | https://tax.colorado.gov/sites/default/files/documents/DR_1098_Colorado_Withholding_Worksheet_for_Employees.pdf |
| Quarterly withholding | Annual withholding less than $7,000; due last day following quarter | https://tax.colorado.gov/withholding-tax-guide |
| Monthly withholding | DOR table says at least $7,000 but not more than $50,000; due 15th following month; exactly $50,000 conflicts with its weekly row, so obtain the assigned frequency | https://tax.colorado.gov/withholding-tax-guide |
| Weekly withholding | DOR table says $50,000 or more; Saturday-Friday period, due third business day after Friday, EFT required; exact boundary as above | https://tax.colorado.gov/withholding-tax-guide |
| UI taxable wage base | First $30,600 per covered worker in 2026; do not use the page's separately labelled 2027 base | https://cdle.colorado.gov/ui/employers/requirements/premiums/premium-rates |
| New UI, ordinary/general construction/trades | 1.53% base + 0.17% support + 1.35% solvency = 3.05% combined, actual 2026 introductory table | https://cdle.colorado.gov/ui/employers/requirements/premiums/introductory-rates |
| New UI, heavy construction | 4.28% base + 0.48% support + 1.525% solvency = 6.285% combined, actual 2026 table | https://cdle.colorado.gov/ui/employers/requirements/premiums/introductory-rates |
| Introductory political subdivision | 0.20% combined in separately identified 2026 category; reimbursement alternatives require classification | https://cdle.colorado.gov/ui/employers/requirements/premiums/introductory-rates |
| Ordinary UI liability | $1,500 wages in a calendar quarter this/prior year OR a worker for part of a day in 20 different weeks; special classes differ | https://cdle.colorado.gov/ui/employers/requirements/employer-liability-requirements |
| Domestic/agricultural UI classes | Domestic $1,000 quarterly; agriculture $20,000 quarterly OR 10 workers in 20 weeks; apply actual class/coverage exceptions | https://cdle.colorado.gov/ui/employers/requirements/employer-liability-requirements |
| UI quarter due dates | April 30, July 31, October 31, January 31, next business day on weekend/holiday | https://cdle.colorado.gov/ui/employers/requirements/premiums/wage-reporting |
| FAMLI total | 0.88% of covered wages up to the federal Social Security wage cap, kept in federal owner | https://famli.colorado.gov/employers |
| FAMLI employee maximum | 0.44%; employer may pay it voluntarily, cannot recover missed deductions from later paychecks | https://famli.colorado.gov/employers |
| FAMLI employer share | 0.44% for 10+ qualifying nationwide employees; fewer than 10 no required employer share, but report/remit employee share | https://famli.colorado.gov/employers |
| FAMLI headcount | Count individuals who each worked at least 20 calendar workweeks in preceding year nationwide, including part-time/seasonal, not average weekly headcount | https://famli.colorado.gov/employers |
| FAMLI headcount report | Initially and first quarter annually by February 28, otherwise account defaults to full employer share | https://famli.colorado.gov/employers |
| FAMLI quarterly due dates | April 30, July 31, October 31, January 31 through My FAMLI+; check actual holiday-adjusted portal date | https://famli.colorado.gov/employers |
| Ordinary FAMLI benefit duration | Up to 12 weeks plus up to 4 for pregnancy/childbirth complications; additional up to 12 weeks for eligible neonatal intensive-care needs effective 2026 | https://leg.colorado.gov/bills/sb25-144 |
| Withholding late payment | Greater of $5 or 5%, plus 0.5% per month, capped 12%; collection penalty can apply after demand | https://tax.colorado.gov/withholding-tax-guide |
| Withholding 2026 interest | Regular 11%; discounted 8% if full payment before/within 30 days of deficiency notice | https://tax.colorado.gov/withholding-tax-guide |

## The method, step by step

### A. Register and establish coverage

1. Obtain the DOR wage-withholding account through MyBizColorado or CR 0100 and
   set up Revenue Online access. This is separate from MyUI Employer+ and
   My FAMLI+. Register the UI account when liable and retain the determination,
   industry classification, effective date and annual rate notice. Register
   FAMLI even for a small employer with no required employer share.
2. For UI, ordinary coverage and domestic/agricultural thresholds differ.
   Nonprofit, government, successor, voluntary coverage and statutory excluded
   employment need their own classification. Do not treat every corporate
   officer as automatically outside employment.
3. Determine withholding separately from UI and FAMLI localization. Colorado
   residents generally have all wages withheld, except wages for out-of-state
   services subject to that state's withholding. Nonresidents generally have
   wages for physical Colorado work withheld. DOR allocates by Colorado workdays
   over total workdays in the pay period, including its majority-of-workday and
   inbound/outbound travel rules. Do not allocate solely by employer address.
4. FAMLI first examines where work is localized. Incidental outside services,
   base of operations, direction/control and a residence tie-breaker can matter.
   Nationwide headcount determines employer contribution status; only covered
   Colorado-localized wages enter this Colorado premium calculation.

Sources: https://tax.colorado.gov/withholding-tax-guide;
https://cdle.colorado.gov/ui/employers/requirements/employer-liability-requirements;
https://famli.colorado.gov/employers (national/localization accordions).

### B. Compute each paycheck with actual DR 1098

DR 1098 is the **employer calculation worksheet**. DR 0004 is the optional
**employee Colorado withholding certificate**. They are not interchangeable.

1. DR 1098 line 1a: this payroll period's taxable wages, including overtime.
2. Line 1b: annual pay periods; line 1c = 1a times 1b.
3. Line 2a: use DR 0004 line 2 if completed, including zero. Only absent/blank
   uses the filing-status default above. A new W-4 without a new DR 0004 revokes
   the prior DR 0004. No certificate defaults to the single calculation.
4. Line 2b = max(0, 1c minus 2a); 2c = 2b times the worksheet multiplier;
   2d = 2c divided by annual pay periods.
5. Line 2e: DR 0004 line 3 additional amount, or preserved pre-2022 request until
   superseded; otherwise zero. Line 2f = 2d + 2e, withheld per paycheck.
6. A W-4 exemption with no DR 0004 follows DOR's review rules. The guide requires
   a copy submitted when expected wages exceed $200 weekly and both other
   stated conditions apply. Do not invent a DR 1098 annual employee renewal.
   Do not separately reduce withholding for federal deductions outside this
   worksheet. Overtime's federal treatment does not erase Colorado withholding.

Actual 2026 source:
https://tax.colorado.gov/sites/default/files/documents/DR_1098_Colorado_Withholding_Worksheet_for_Employees.pdf.

### C. Compute UI and FAMLI

For each covered worker, UI taxable pay for the period is the smaller of current
UI wages and the unused annual Colorado UI base, floored at zero. Multiply by
that employer's combined actual rate; do not add surcharges again to a combined
notice rate. The current CDLE page also displays 2027 figures. Use the explicitly
labelled 2026 table or actual 2026 notice, not a future untitled schedule.

For FAMLI, apply the annual federal wage-cap limitation per worker using the
federal owner; multiply covered pay by the employee share and, where required,
employer share. Headcount counts qualifying **individuals**, not a weekly
average. New hires' covered pay can attract premiums immediately even before
that individual has worked enough weeks to count for a later headcount test.
Keep employee deductions separate from employer expense.

### D. File, pay, correct and retain confirmation

- **DOR withholding:** use the assigned frequency, with weekend/holiday next-day
  rule. Monthly/quarterly zero returns are required unless approved seasonal
  treatment; weekly filers report periods with wages. Weekly EFT identifies the
  period-ending Friday. The final year-end weekly period ends December 31 and
  is due third business day afterwards. EFT satisfies return and payment;
  do not also file DR 1094 and create a duplicate bill. Non-EFT eligible filers
  use Revenue Online or DR 1094. Save confirmation and match account/period.
- **Corrections:** report only the additional withholding for underpayment,
  rather than re-reporting the original total. Same-year overpayments may offset
  a later period; year-end refunds use the applicable DR 1093/DR 0137 procedure.
  A notice may require a written protest within 30 days. Source:
  https://tax.colorado.gov/withholding-tax-guide, Parts 3-4.
- **W-2:** report state wages/withholding and provide to employee/DOR by January
  31 following year, using actual calendar adjustments. State e-filing follows
  the federal electronic-filing trigger, whose number remains in federal owner.
  Request Revenue Online withholding-submitter access at least five days before
  first filing: Additional Services > Submit Year-End Withholding > Request
  Withholding Submitter Access. Then submit manual entries or .txt file and save
  acceptance/errors. Electronic filers normally do not file paper DR 1093.
  Supply DR 0995 or its full written contents annually in required languages;
  a hyperlink or workplace posting alone is insufficient.
- **UI:** MyUI Employer+ > relevant quarter wage-detail report; enter/upload each
  worker's identifying information and gross wages, with monthly employment
  counts for workers employed on the 12th day. Correct errors, submit, save
  acceptance, verify taxable wages/rate and separately pay premiums. Reports
  are electronic unless the employer has an approved non-electronic waiver;
  third-party administrators cannot use that waiver. Copy Previous Quarter
  requires actual edits; it does not authorize repeating stale pay.
- **FAMLI:** My FAMLI+ > quarterly wage reporting; manual entry or supported file
  upload, validate workers/wages and headcount, submit and separately remit the
  assessed premium. Save report, payment and reconciliation. Follow current
  private-plan approval instructions before assuming an exemption. A private
  plan is not created by buying a policy alone.

UI source: https://cdle.colorado.gov/ui/employers/requirements/premiums/wage-reporting.
FAMLI source: https://famli.colorado.gov/employers (payment/reporting accordions).

### E. Classification and preserved labor-law subjects

The current CDLE independent-contractor page presumes covered employment until
both freedom from control/direction in contract **and fact**, and a customary
independent related business are established. The old categorical three-prong
ABC statement is withdrawn. A qualifying written contract shifts a rebuttable
presumption; it does not conclusively determine status. Read the page's complete
clauses and prominent unemployment/income-tax disclosure: nonexclusivity,
limited quality-control direction, contract rather than hourly pay, constrained
termination, minimal training, tools/benefits limits, time flexibility, payment
to business name and separate operations. Source:
https://cdle.colorado.gov/independent-contractors (ordinary browser read).

The former labor-law topics remain in scope as checks requiring current sources:
HFWA accrual/carryover, PHE supplemental leave and notices/records; Equal Pay for
Equal Work Act posting, compensation/benefits disclosure, application deadlines,
post-selection notices and wage-history restrictions; final wages and earned
vacation, including the cited Nieto v. Clark's Market (2021) issue; construction
classification, wage theft, retainage and prevailing wage; SecureSavings and
local occupational privilege taxes. Their former numerical claims have not been
confirmed for 2026 and are not usable computations here. Do not treat the old
private-plan approval duration, FAMLI weekly benefit maximum, federal wage-cap
number or final-pay penalty formula as current verified figures.

## Worked cases

### Five-employee Denver creative agency

Preserve the old invented agency: S-corporation owner earns $80,000 and four
employees $55,000 each, $300,000 total. Assume all wages covered, owner single,
other four MFJ, no DR 0004/additional amounts, equal full-year payroll, ordinary
new-employer UI, each worker over the UI base and below the federal FAMLI cap.
Annualized worksheet withholding is $11,022, not the old rough $11,700. UI is
$4,666.50. Five qualifying nationwide individuals means no required employer
FAMLI share; employees' total share is $1,320. Actual per-pay rounding can differ.
Annual withholding is in the monthly range, subject to assigned frequency.

```oa-check
name: Colorado five employee agency 2026
inputs:
  owner_pay: 80000
  other_pay: 55000
  other_count: 4
  ui_base: 30600
steps:
  payroll: owner_pay + other_pay * other_count
  owner_wh: max(0, owner_pay - 5500) * 0.044
  staff_wh: max(0, other_pay - 11000) * 0.044 * other_count
  annual_wh: owner_wh + staff_wh
  ui: ui_base * (other_count + 1) * 0.0305
  employee_famli: payroll * 0.0044
  required_employer_famli: payroll * 0
expected:
  payroll: 300000
  annual_wh: 11022
  ui: 4666.50
  employee_famli: 1320
  required_employer_famli: 0
```

### Fifty-employee technology company: contribution election

Preserve the invented company with 50 covered workers earning $120,000 each.
Assume all single/default worksheet, below the federal FAMLI cap and a supplied
2026 UI notice with **hypothetical combined 1.10%**; this is not a published
industry rate. UI is $16,830; annualized withholding $251,900. FAMLI is $52,800,
ordinarily $26,400 each side. Required employer UI plus FAMLI costs $43,230;
paying employees' FAMLI share voluntarily raises that to $69,630, a $26,400
employer cost decision. Withholding is weekly/EFT under the stated assumptions.

```oa-check
name: Colorado technology employer FAMLI election
inputs:
  count: 50
  annual_pay: 120000
  ui_base: 30600
  assumed_notice_rate: 0.011
steps:
  payroll: count * annual_pay
  annual_wh: count * max(0, annual_pay - 5500) * 0.044
  ui: count * ui_base * assumed_notice_rate
  half_famli: payroll * 0.0044
  total_famli: half_famli * 2
  standard_employer_cost: ui + half_famli
  absorb_employer_cost: ui + total_famli
  added_cost: absorb_employer_cost - standard_employer_cost
expected:
  payroll: 6000000
  annual_wh: 251900
  ui: 16830
  total_famli: 52800
  standard_employer_cost: 43230
  absorb_employer_cost: 69630
  added_cost: 26400
```

### Multistate employer

The old 20-person employer has 12 in Texas, five in Colorado and three in
Wyoming/New Mexico. Assume every person qualifies for the preceding-year
headcount, only the five Colorado workers are Colorado-localized, each paid
$120,000 below the federal FAMLI cap, and an ordinary new-employer UI rate.
Colorado employer UI/FAMLI expense is $7,306.50. Nationwide headcount requires
the employer FAMLI share even though only five work in Colorado. No other state's
rates or liability is inferred.

```oa-check
name: Colorado multistate nationwide headcount
inputs:
  colorado_count: 5
  colorado_pay: 120000
steps:
  colorado_payroll: colorado_count * colorado_pay
  ui: colorado_count * 30600 * 0.0305
  employer_famli: colorado_payroll * 0.0044
  employee_famli: employer_famli
  employer_cost: ui + employer_famli
expected:
  colorado_payroll: 600000
  ui: 4666.50
  employer_famli: 2640
  employee_famli: 2640
  employer_cost: 7306.50
```

### Boulder startup growing from eight to twelve in August

Hiring alone does not establish the next year's qualifying individual count.
Preserve the growth case but obtain each person's actual weeks. At assumed
$600,000 covered pay below each worker's federal cap, nine qualifying nationwide
individuals means zero required employer premium versus $2,640 for ten. The
employee share remains $2,640 in either scenario. Do not impose retroactive
employer premiums merely because the current payroll reached twelve people.

```oa-check
name: Colorado startup qualifying headcount scenarios
inputs:
  covered_pay: 600000
steps:
  employee_share: covered_pay * 0.0044
  nine_employer_share: covered_pay * 0
  ten_employer_share: covered_pay * 0.0044
  difference: ten_employer_share - nine_employer_share
expected:
  employee_share: 2640
  nine_employer_share: 0
  ten_employer_share: 2640
  difference: 2640
```

## Checks before finalising

- Reconcile certificate dates and all DR 1098 lines; worksheet is not certificate.
- Verify 2026 rate notice and year-labelled UI table; no duplicate surcharge.
- Track separate per-worker UI and federally capped FAMLI wage bases.
- Count nationwide qualifying individuals from weeks, not average headcount.
- Reconcile employee deductions, employer expense, three portal accounts and receipts.
- Check notices, labor-law overlays and private-plan approval independently.

## When to refuse or refer

Refer doubtful worker/localization status, reimbursement classes, private plans,
leave eligibility/protection, wage disputes and local obligations. Obtain DOR
assigned frequency at the published $50,000 boundary conflict. Do not use the
old unsourced experienced UI range, rough withholding percentages or obsolete
FAMLI premium/headcount method.

## Sources

| Source | URL | Reading scope | Read on |
|---|---|---|---|
| DOR wage withholding | https://tax.colorado.gov/withholding-tax-guide | Read for Parts 1-4 registration, certificates, resident/nonresident allocation, filing table/boundary conflict, EFT, corrections, W-2 and DR 0995 | 2026-11-13 |
| Actual 2026 DR 1098 | https://tax.colorado.gov/sites/default/files/documents/DR_1098_Colorado_Withholding_Worksheet_for_Employees.pdf | Read for all three pages, worksheet lines, defaults, certificate replacement and EFT/annual filing FAQs | 2026-11-13 |
| CDLE premium rates | https://cdle.colorado.gov/ui/employers/requirements/premiums/premium-rates | Read for year-labelled 2026 wage base in ordinary browser after direct403; current page also displays 2027 | 2026-11-13 |
| CDLE introductory rates | https://cdle.colorado.gov/ui/employers/requirements/premiums/introductory-rates | Read for every component/category of actual 2026 table in ordinary browser; did not apply separate 2027 table | 2026-11-13 |
| CDLE liability | https://cdle.colorado.gov/ui/employers/requirements/employer-liability-requirements | Read for general/domestic/agricultural coverage and nonprofit/government/successor exceptions in ordinary browser | 2026-11-13 |
| CDLE wage reporting | https://cdle.colorado.gov/ui/employers/requirements/premiums/wage-reporting | Read for quarterly due dates, monthly counts, electronic reporting/waiver, corrections and MyUI workflow in ordinary browser | 2026-11-13 |
| CDLE classification | https://cdle.colorado.gov/independent-contractors | Read for both substantive tests, rebuttable contract presumption, all expanded clauses and prominent disclosure in ordinary browser | 2026-11-13 |
| FAMLI employers | https://famli.colorado.gov/employers | Read for 2026 premium, employee/employer shares, cap, qualifying headcount, national example, localization, payment/reporting accordions in ordinary browser | 2026-11-13 |
| SB25-144 | https://leg.colorado.gov/bills/sb25-144 | Read for enacted summary's 2026 premium and additional neonatal intensive-care leave | 2026-11-13 |

Not yet confirmed: full actual 2026 experienced UI schedule and each notice, detailed UI registration/payment screen fields, precise holiday-adjusted FAMLI dates, final 2026 DR0004/1093/1094 fields, private-plan approval duration, current weekly benefit maximum, job-protection/leave eligibility and labor-law overlays named above. HFWA/PHE, Equal Pay, final-pay/vacation including Nieto v. Clark's Market (2021), construction/wage-theft/retainage, SecureSavings and local OPT need their own current sources. These gaps remain partial, not silently certified.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon. The most up-to-date version of this skill is maintained at https://www.openaccountants.com.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `co-payroll` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/co-payroll. If neither is available, confirm every figure against the official source pages cited above before relying on it.
