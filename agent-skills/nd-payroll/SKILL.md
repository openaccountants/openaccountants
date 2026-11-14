---
name: nd-payroll
description: "Compute North Dakota 2026 wage income-tax withholding using the published 2026 tables, NDW-R reciprocity and NDW-M military-spouse exemptions. Complete Form 306, Form 307 and state information reporting; route UI to nd-social-contributions and identify new-hire, final-pay and WSI boundaries."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/nd-payroll"
  jurisdiction: "US-ND"
  tax_year: "2026"
  last_updated: "2026-11-13"
---

# North Dakota payroll withholding, 2026

> **Built from the law. Not yet approved.** Written by Codex. Not reviewed by an accountant. A qualified professional must review the established facts and filing result. Circular 230 section 10.37: consider relevant facts and circumstances; do not assume missing facts or rely on audit risk.

**Answer first.** Use the actual 2026 withholding booklet, the employee's federal W-4 vintage and state exemption documents. Withholding wage cutoffs differ from the annual-return taxable-income brackets. File Form 306 and reconcile Form 307 through the state system; state unemployment belongs to `nd-social-contributions`. [2026 booklet](https://www.tax.nd.gov/sites/www/files/documents/forms/individual/2026-iit/2026-income-tax-withholding-rates-booklet.pdf); [state filing instructions](https://www.tax.nd.gov/income-tax-withholding).

## Scope

State wage income-tax withholding, employer registration, quarterly/annual reconciliation, reciprocity and information returns. Federal withholding, FICA, FUTA and federal forms belong to `us-form-941-940-payroll`. UI wage base, assigned contributions and SFN 41263 are owned by `nd-social-contributions`; this avoids two state skills maintaining competing UI tables. New hires, final pay, garnishments and WSI are retained as employer compliance boundaries below, not a substitute for resolving an actual order or coverage dispute.

## Ask the client first

1. Employer account, entity, locations, payroll provider, filing-frequency notice and prior-year North Dakota withholding.
2. Employee residences/work locations, start/move dates, federal W-4 version/status and current NDW-R or NDW-M with attachments.
3. Taxable wages, pay frequency, benefits/reimbursements, supplemental wages and extra-withholding requests.
4. Quarter/year payroll totals, tax withheld, Forms W-2/1099, prior payments and corrected statements.
5. New hires, separations, garnishment/support orders, UI and WSI notices, approved coverage/exclusion documents.

## The method, step by step

### Rates, bands and thresholds

These annual wage tables apply to **2020-and-later W-4s**, from Section 2 of the 2026 booklet. They are not the ND-1 return brackets.

| 2026 annual taxable wages / condition | Rate / withholding calculation | Official source |
| --- | --- | --- |
| Single through USD 57,625 | Zero | [2026 p45](https://www.tax.nd.gov/sites/www/files/documents/forms/individual/2026-iit/2026-income-tax-withholding-rates-booklet.pdf) |
| Single over 57,625 through 258,450 | 1.95% of excess over 57,625 | [2026 p45](https://www.tax.nd.gov/sites/www/files/documents/forms/individual/2026-iit/2026-income-tax-withholding-rates-booklet.pdf) |
| Single over 258,450 | 3,916.09 + 2.50% of excess over 258,450 | [2026 p45](https://www.tax.nd.gov/sites/www/files/documents/forms/individual/2026-iit/2026-income-tax-withholding-rates-booklet.pdf) |
| Married filing jointly through 57,500 | Zero | [2026 p45](https://www.tax.nd.gov/sites/www/files/documents/forms/individual/2026-iit/2026-income-tax-withholding-rates-booklet.pdf) |
| Joint over 57,500 through 168,525 | 1.95% of excess over 57,500 | [2026 p45](https://www.tax.nd.gov/sites/www/files/documents/forms/individual/2026-iit/2026-income-tax-withholding-rates-booklet.pdf) |
| Joint over 168,525 | 2,164.99 + 2.50% of excess over 168,525 | [2026 p45](https://www.tax.nd.gov/sites/www/files/documents/forms/individual/2026-iit/2026-income-tax-withholding-rates-booklet.pdf) |
| Head of household through 78,475 | Zero | [2026 p45](https://www.tax.nd.gov/sites/www/files/documents/forms/individual/2026-iit/2026-income-tax-withholding-rates-booklet.pdf) |
| Head over 78,475 through 289,675 | 1.95% of excess over 78,475 | [2026 p45](https://www.tax.nd.gov/sites/www/files/documents/forms/individual/2026-iit/2026-income-tax-withholding-rates-booklet.pdf) |
| Head over 289,675 | 4,118.40 + 2.50% of excess over 289,675 | [2026 p45](https://www.tax.nd.gov/sites/www/files/documents/forms/individual/2026-iit/2026-income-tax-withholding-rates-booklet.pdf) |
| Separately paid/identified supplemental wage option | 1.5%; aggregate-difference option also permitted | [2026 p57](https://www.tax.nd.gov/sites/www/files/documents/forms/individual/2026-iit/2026-income-tax-withholding-rates-booklet.pdf) |
| Form 306 mandatory electronic filing | Prior-year withholding at least USD 1,000 **or** qualifying third-party payroll provider | [current state page](https://www.tax.nd.gov/income-tax-withholding) |
| Forms 307, W-2, 1099, W-2G, 1042-S | Electronic state filing; waiver/actual filing duties must be checked | [current state page](https://www.tax.nd.gov/income-tax-withholding); [information-return instructions](https://www.tax.nd.gov/sites/www/files/documents/guidelines/business/it-withhold/income-tax-withholding-information-returns-guideline.pdf) |

1. Register the withholding account before filing/remitting. Establish wages subject to state withholding under 57-38-59 and the state guideline. Resident wages and North Dakota services by nonresidents generally enter; the resident out-of-state wage exception depends on withholding required by the other state. Certain agricultural wages and other statutory exclusions need actual facts. A federal treaty exemption does not automatically establish a state exemption.
2. Use the federal W-4. For a W-4 before 2020, Section 1 supplies its own allowance amounts and pay-period tables. For W-4s from 2020 onward, Section 2 uses taxable wages, pay periods and status from Step 1(c). A newly hired employee without W-4 uses Section 2 as single. **NDW-M is a military-spouse exemption certificate, not a pension allowance certificate or general state W-4.**
3. Under the Section 2 percentage worksheet, annualize the taxable wage by 52 weekly, 26 biweekly, 24 semimonthly, 12 monthly, 4 quarterly, 2 semiannual or 260 daily periods. Apply the annual status table, divide by periods and round to the nearest whole dollar. Check additional North Dakota withholding requests separately. Percentage withholding is generally recommended for automated payroll; the booklet does not mandate it merely because software is used. Wage-bracket methods have their own published wage limits, not a universal USD 1 million ceiling.
4. If supplemental pay is combined without separate identification, use the combined wage amount. If separately paid or identified, use the permitted 1.5% option or aggregate-difference method. Pension/annuity, nonresident owner and oil/gas royalty withholding have separate rules; do not force them into these wage tables.
5. Review exemptions on their exact forms. NDW-R covers qualifying Minnesota/Montana residents' wage compensation, not Schedule C, partnership/S corporation distributions, rent or gambling. A Minnesota employee must return to a permanent Minnesota residence at least monthly; the Montana form has no identical monthly-return condition. Establish actual domicile/residence and cease exemption when no longer eligible.
6. NDW-R is renewed annually by February 28, or supplied within 30 days after beginning employment/moving to the reciprocity state. For regular annual forms the employer retains a copy and sends the original to the agency by March 31; a new-hire/move original must be sent within 30 days **after employer receipt**. Stop withholding under the form's effective-date instructions, not retroactively for already paid wages. Without a valid form, withhold; the employee may seek a refund on the proper state income-tax return. The former guaranteed six-to-twelve-month refund delay was unsupported. Home-state employer obligations require that state's skill.
7. NDW-M applies only to a qualifying civilian spouse of an active-duty servicemember under the form's domicile, North Dakota duty-station and accompanying-spouse conditions. Complete every item, attach dependent military ID, retain the original and send the agency copy with attachment. Renew annually and notify ineligibility. The exemption takes effect on the later of delivery or the first payroll able to implement it; it does not erase prior withholding. Refer changed military elections/law or inconsistent facts rather than extending the form beyond its conditions.

### Preserved historical comparison, 2025-2026 filing cycle

The old 2025 annual wage tables were single 55,975/252,325/base 3,828.83; joint 55,488/164,038/base 2,116.73; head 76,200/282,700/base 4,026.75, with positive rates 1.95%/2.50%. They are retained only as the old skill's historical comparison and **not yet confirmed by a fresh 2025 booklet read**. The read 2026 booklet supersedes them for wages paid in 2026. Historical HB 1158 bracket reform remains background; this skill does not rely on the former unsupported comparisons to other states or future revenue triggers.

## Boundary and exception table

| Situation | Required treatment |
| --- | --- |
| Minnesota commuter keeps Fargo accommodation | Determine permanent residence and monthly return; an address or driver's license alone does not settle eligibility |
| Montana wage earner | Current NDW-R, annual renewal and actual residency; home-state withholding separately |
| Nonresident owner/royalty recipient | Separate pass-through/royalty withholding forms and annual rules |
| UI/SUTA contribution or worker classification | Use `nd-social-contributions`; MN/MT income-tax reciprocity does not determine UI localization |
| Pension/annuity, reasonable compensation, accountable-plan per diem or cafeteria-plan design | Refer to the relevant state/federal owner; do not invent wage exemptions |
| Tribal-government employer or disputed Indian-country immunity | Specialist analysis of status, location and source |

## Worked cases

**Anna, updated from the original case to 2026.** Bismarck resident, single current W-4, USD 2,500 biweekly taxable wages, no retirement/cafeteria deductions. Annual wages are 65,000. Annual withholding is (65,000 - 57,625) × 1.95% = 143.81; divided by 26 is 5.53, rounded to **USD 6 each pay**. Six Q1 pays produce USD 36. The historical 2025 example gave annual 175.99, per-pay 6.77 rounded 7 and quarter 42; those are not current 2026 results.

```oa-check
name: ND Anna 2026 biweekly withholding and quarter
inputs:
  taxable_pay: 2500
  periods: 26
  quarter_pays: 6
steps:
  - annual_wages: taxable_pay * periods
  - annual_tax: round((annual_wages - 57625) * 0.0195, 2)
  - per_pay_unrounded: round(annual_tax / periods, 2)
  - per_pay: round(annual_tax / periods, 0)
  - quarter_tax: per_pay * quarter_pays
expected:
  annual_wages: 65000
  annual_tax: 143.81
  per_pay_unrounded: 5.53
  per_pay: 6
  quarter_tax: 36
```

**Bjorn, preserved reciprocity case.** Moorhead resident commuting daily to Fargo, USD 3,200 biweekly, NDW-R delivered February 1, 2025. The original daily-return facts satisfy the form's monthly-return condition. The employer sends this new-hire form within 30 days of receipt, not automatically waiting until March 31. The 2025 exemption does not roll over: obtain the 2026 form by February 28 and follow current effective-date instructions. Valid exempt wages have zero North Dakota withholding; determine Minnesota duties separately. Already withheld amounts require the proper refund return; no refund timetable is promised.

**Carla, updated from the original case to 2026.** Bismarck engineer, single current W-4, USD 325,000 annual taxable salary, 24 semimonthly pays (displayed 13,541.67 is rounded), plus a separately identified USD 50,000 bonus. Annual regular withholding is 3,916.09 + (325,000 - 258,450) × 2.5% = 5,579.84; per pay 232.49 rounds to **232**. Flat bonus withholding is 750. A purely illustrative 2.5% marginal comparison is 1,250, leaving 500 more than the flat withholding; final taxable income and credits determine actual balance. Consider extra withholding or Form **ND-1ES**, never the former erroneous Form 540-ES. Historical 2025 regular amounts 5,645.71/235.24/235 remain year-specific, not 2026 figures.

```oa-check
name: ND Carla 2026 regular salary and identified bonus
inputs:
  annual_wages: 325000
  periods: 24
  bonus: 50000
steps:
  - annual_tax: round(3916.09 + (annual_wages - 258450) * 0.025, 2)
  - per_pay_unrounded: round(annual_tax / periods, 2)
  - per_pay: round(annual_tax / periods, 0)
  - bonus_withholding: bonus * 0.015
  - illustrative_marginal_difference: bonus * 0.025 - bonus_withholding
expected:
  annual_tax: 5579.84
  per_pay_unrounded: 232.49
  per_pay: 232
  bonus_withholding: 750
  illustrative_marginal_difference: 500
```

## When to refuse or refer

Refer contested domicile, multistate allocation, tribal immunity, classification, retirement distribution, reasonable compensation, plan design, WSI claims and disputed court orders. Fixed amounts cannot substitute for current account notices. The old deterministic/judgment/refusal catalogue is implemented by the method, boundary table and these gates; no accountant has approved this skill.

### Retained employer-law topics

- **New hires:** chapter 34-15, not the old 14-09-09.5 citation, requires a report within 20 days of hire/rehire after at least 60 consecutive separated days. Electronic reporters may use two monthly transmissions 12-16 days apart if necessary. More than 24 employees requires the agency electronic method unless waived. Report employee name/address/SSN/hire date and whether health insurance is offered, plus employer name/address/EIN. The old date-of-birth and USD 2,500 independent-contractor assertions are not established by this statute. A qualifying multistate electronic reporter may designate one state and notify the federal department under the state law; retain evidence. [34-15](https://ndlegis.gov/cencode/t34c15.pdf).
- **WSI:** chapter 65-01 describes a state fund with broad covered employment and specific exceptions, including agricultural/domestic employment and defined owner/family/contractor categories. A national private policy alone does not establish the required North Dakota state-fund coverage; verify before assigning staff to North Dakota. Do not apply the old blanket officer Form C-3 exclusion, nine-factor test or day-one assertion without checking actual status/localization. Premium classification, payroll and experience treatment require the actual WSI account; the old NAICS industry-average/three-year promises are unconfirmed. Uninsured premiums, claim costs, willful misrepresentation penalties, officer liability and injunction remedies differ under 65-04-33; there is no universal automatic triple-premium penalty. The former treble injury-suit recovery and specific stop-work characterization remain unconfirmed. [65-01](https://ndlegis.gov/cencode/t65c01.pdf); [65-04-33](https://ndlegis.gov/cencode/t65c04.pdf).
- **Final pay/PTO:** final wages on voluntary or involuntary separation are due at the next established regular payday. A discharged employee is paid by certified mail unless otherwise agreed; this is not an employee option to demand payment within 15 days. Section 34-14-09.2 narrowly permits withholding accrued PTO on voluntary departure only when written hiring notice, less than one year's service and less than five days' resignation notice all apply; a separate provision covers awarded-but-unearned advance PTO with required notice. Do not use the former blanket no-payout default. State paid-sick/family-leave mandates were asserted absent before; their full current scope is not confirmed here. [34-14-03,09.2](https://ndlegis.gov/cencode/t34c14.pdf).
- **Garnishment/support:** ordinary creditor garnishment under 32-09.1-03 uses the lesser of 25% disposable weekly earnings or excess over **40**, not 30, times the applicable federal minimum hourly wage, reduced by USD 20 per qualifying resident dependent after the required declaration. Refer tax/bankruptcy/support exceptions and actual period conversion. Chapter 32 has general support-order maxima varying with other dependents and arrears; an income-withholding order under **14-09-09.3** specifically limits total withholding including allowed administration charge to **50%** of disposable income from that payer. Begin no later than the first payday after service, remit within seven business days of payment, retain the withholding-date report and handle multiple orders proportionately under the statute. The old 14-day start and blanket federal 50-65% substitution are wrong for that statutory IWO workflow. [32-09.1](https://ndlegis.gov/cencode/t32c09-1.pdf); [14-09-09.3](https://ndlegis.gov/cencode/t14c09.pdf).

## Filing and payment

Form 306 is due at the end of the month after each quarter: April 30, July 31, October 31 and January 31, moved to the next business day where applicable. File even if no withholding or wages while the account is open. The state may authorize annual filing when all four prior quarters were timely filed/paid and prior-year withholding was below USD 1,000; contact it before Q1 rather than electing independently. No monthly/semiweekly ordinary state wage deposit cycle is supplied by the read instructions.

Electronic Form 306 is mandatory with prior-year withholding at least USD 1,000 or a qualifying third-party payroll provider. Submit through ND TAP; ACH credit with the required identification can act as the return under the guideline, whereas a no-login account payment alone does not file Form 306. Save return acceptance and separately confirm credited payment.

Form 307 annual reconciliation is due January 31 with required state W-2 copies; an open withholding account files 307 even without W-2s. All state W-2 filing is electronic, not only employers with ten forms. The state accepts the specified EFW2-format upload/TAP entry subject to its current specifications. Reconcile wage statements, all 306 periods, corrections and actual payments.

Do not omit a 1099-NEC merely because it has no North Dakota withholding. Under the state nonwage guideline, a payer residing, owning property or conducting business in North Dakota has state reporting duties for specified federally reportable payments; for nonresident recipients, source conditions apply. Forms 1099-MISC/R/NEC, W-2G and 1042-S have type-specific conditions. File electronically, checking any allowed waiver and due date. The federal combined program is not a blanket substitute. Pension/royalty/nonresident pass-through withholding remains separate.

Under 57-38-45 and the guideline, ordinary timely-filed unpaid tax generally incurs 5% or USD 5 minimum; late filing incurs 5% per month/part to 25%, subject to minimums and conditions. Interest is 1% per month/part after the due month, not a newly assumed annually set rate. Filing paper when electronic filing is mandatory can be treated as not filed. The old fixed USD 500 electronic-return penalty and generic 5% EFT penalty are unconfirmed and must not be automatically charged.

## Completion checklist

- Correct W-4 vintage, 2026 table and taxable wage base selected.
- Current reciprocity/military-spouse certificates, deadlines and residence facts supported.
- State UI handled once through `nd-social-contributions`; WSI status separately supported.
- Form 306 periods and Form 307/W-2/nonwage statements reconcile; zero-return duties checked.
- New-hire/separation/order actions documented, acceptance retained and payment verified.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, payroll, or workers' compensation advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing, depositing, or acting upon.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| 2026 withholding booklet. Read for W-4 vintage, percentage/wage methods, annual tables, period factors, rounding and supplemental pay. | https://www.tax.nd.gov/sites/www/files/documents/forms/individual/2026-iit/2026-income-tax-withholding-rates-booklet.pdf | 2026-11-13 |
| Current withholding page. Read for registration, electronic 306 triggers, zero returns and annual reconciliation. | https://www.tax.nd.gov/income-tax-withholding | 2026-11-13 |
| Withholding and information returns guideline. Read for wage exceptions, annual authorization, payment/return distinction, penalties and nonwage reporting. | https://www.tax.nd.gov/sites/www/files/documents/guidelines/business/it-withhold/income-tax-withholding-information-returns-guideline.pdf | 2026-11-13 |
| NDW-R. Read for MN monthly-return condition, MT eligibility, renewal, new/move deadlines, agency copies and refunds. | https://www.tax.nd.gov/sites/www/files/documents/forms/business/ndwrfillable.pdf | 2026-11-13 |
| NDW-M. Read for military-spouse conditions, ID attachment, annual form, effective date, employer retention and agency copy. | https://www.tax.nd.gov/sites/www/files/documents/forms/business/it-withholding/form-ndw-m.pdf | 2026-11-13 |
| Chapter 57-38. Read for withholding obligation and section 45 ordinary delinquency penalties/interest. | https://ndlegis.gov/cencode/t57c38.pdf | 2026-11-13 |
| Chapter 34-15. Read for new-hire/rehire definition, reporting data/timing, mandatory electronic threshold and multistate election. | https://ndlegis.gov/cencode/t34c15.pdf | 2026-11-13 |
| Chapter 34-14. Read for next-payday/certified-mail final pay and conditional PTO withholding. | https://ndlegis.gov/cencode/t34c14.pdf | 2026-11-13 |
| Chapter 32-09.1. Read for creditor garnishment, dependent reduction and exceptions. | https://ndlegis.gov/cencode/t32c09-1.pdf | 2026-11-13 |
| Chapter 14-09. Read for section 09.3 IWO first-payday start, seven-business-day remittance, 50% cap and multiple orders. | https://ndlegis.gov/cencode/t14c09.pdf | 2026-11-13 |
| Chapter 65-01. Read for state fund, employee/employer and hazardous-employment coverage definitions/exclusions. | https://ndlegis.gov/cencode/t65c01.pdf | 2026-11-13 |
| Chapter 65-04. Read for section 33 differentiated uninsured/willful penalties, claim costs and injunction remedies. | https://ndlegis.gov/cencode/t65c04.pdf | 2026-11-13 |

Not yet confirmed: current military-spouse facts beyond the read form's conditions; actual WSI classification/exclusion, premium method and specialized sanctions; general sick/family-leave mandates; historical 2025 withholding comparison without a fresh source read; specific electronic/EFT penalty assertions; current upload schemas and specialized nonwage deadlines. Do not file a disputed exemption, order or specialist return using a historical example.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `nd-payroll` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/nd-payroll. If neither is available, confirm every figure against the official source pages cited above before relying on it.
