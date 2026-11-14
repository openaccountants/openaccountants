---
name: us-state-payroll-matrix
description: "State payroll for US employers in 2026, every state and DC on one page. Gives the method for a multi-state employer (which state's withholding, unemployment insurance and paid leave apply, under the FUTA localization test), and a row for every state with its 2026 unemployment insurance taxable wage base, new employer rate and any state paid leave or disability payroll deduction, each linked to that state's own agency (for example California SDI 1.3% with no wage limit, New York PFL 0.432%, Washington PFML 1.13% and WA Cares 0.58%, Massachusetts PFML 0.88%, Colorado FAMLI 0.88%, Rhode Island TDI 1.1%, wage bases from USD 7,000 to USD 78,200). Trigger on \"state payroll\", \"SUI wage base\", \"SUTA rate\", \"new employer rate\", \"state disability insurance\", \"paid family leave deduction\", \"multi-state payroll\". Federal payroll (941, 940, FUTA) is in us-form-941-940-payroll; withholding detail is in each state's payroll skill."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/us-state-payroll-matrix"
  jurisdiction: "US"
  tax_year: "2026"
  last_updated: "2026-11-13"
---

# US state payroll: unemployment insurance and paid leave by state, 2026

> **Source-cited draft.** Figures come from each state's own labor or revenue agency, through the state payroll skills rewritten on 13 November 2026 where they exist, and the agencies' 2026 pages read on 2026-11-13. A row that says "not confirmed" links the agency and gives no figure. No accountant has reviewed it.

**Answer first.** Each state where an employee works can require four things: income tax withholding (if it has an income tax), unemployment insurance contributions, new hire reports, and in some states a paid leave or disability deduction. Unemployment insurance goes to one state per employee, chosen by the federal localization test. State wage bases for 2026 run from USD 7,000 (Arkansas, California, Florida, Louisiana) to USD 78,200 (Washington).

## Scope and who this is for

In scope: state unemployment insurance (SUI) wage bases and new employer rates, and state paid leave and disability payroll deductions, for 2026, plus the method for an employer with staff in several states. Out of scope, and where it goes:

| Topic | Skill |
| --- | --- |
| Federal Forms 941, 940, W-2, FUTA and the Social Security wage base | `us-form-941-940-payroll` |
| New hire reporting deadlines and contractor reports | `us-state-new-hire-reporting-matrix` |
| Which state taxes a remote worker's wages (convenience rule, reciprocity) | `us-multi-state-residency-and-allocation` |
| A state's withholding tables, forms and local taxes | that state's payroll skill (named in the table) |
| Local wage taxes (Pennsylvania EIT, Ohio municipal, New York City, Detroit, and others) | `us-local-income-tax-matrix` |

## Ask the client first

1. Where does each employee live, and where do they physically work (office, home, travel)?
2. Where is the base of operations and the place of direction and control?
3. Which state accounts are open (withholding, SUI, paid leave) and which rate notices have arrived?
4. Headcount per state (paid leave rates differ by employer size)?
5. Any employees earning above a state's wage base or the Social Security base?

## The method, step by step

1. **SUI: one state per employee.** Wages are reported to the state where the service is localized: performed entirely in one state, or mostly there with only incidental work elsewhere. If not localized anywhere, use the state of the base of operations; then the state the service is directed and controlled from; then the employee's state of residence, if some service is performed there ([26 U.S.C. 3306(c)(1) and (j)](https://www.govinfo.gov/content/pkg/USCODE-2023-title26/html/USCODE-2023-title26-subtitleC-chap23-sec3306.htm), with each state's matching law).
2. **SUI amount.** Rate on the employer's state rate notice (or the new employer rate in the table) times wages up to that state's wage base. Wages paid to the same employee in another state can usually count toward the base when the employee moves: check the state rule.
3. **Withholding.** Withhold for the state where the work is done, plus the resident state where it requires it, after any reciprocity agreement (`us-multi-state-residency-and-allocation`). Nine states have no tax on wages: Alaska, Florida, Nevada, New Hampshire, South Dakota, Tennessee, Texas, Washington and Wyoming.
4. **Paid leave and disability.** Where the state has a program (table), register and withhold or pay at the 2026 rate, up to that program's wage cap.
5. **New hire reports** in each work state (`us-state-new-hire-reporting-matrix`).
6. **Local taxes** where they apply.
7. **File** each state's quarterly returns on its own schedule (see the state payroll skill).

### Rates, bands and thresholds

| State | 2026 SUI taxable wage base | New employer SUI rate | State paid leave or disability deduction, 2026 | Source | State skill |
| --- | --- | --- | --- | --- | --- |
| Alabama | USD 8,000 | 2.70% | None | [ADOL wage base FAQ](https://adol.alabama.gov/faq/what-is-the-taxable-wage-base/); [new account rate](https://adol.alabama.gov/faq/what-is-the-new-account-rate/) | `al-unemployment-contributions` |
| Alaska | USD 54,200 (employer and employee shares) | Industry-based (first-time filers use 1.50% total maximum until assigned) | Employee UI contribution 0.50% | [Alaska DOL 2026 first-time filers](https://dol.alaska.gov/estax/forms/2026_First_Time_Filers.pdf); [wages FAQ](https://www.labor.alaska.gov/estax/faq/WagesDeductions.htm) | `ak-payroll` |
| Arizona | USD 8,000 | 2.00% | None | [A.R.S. 23-622](https://www.azleg.gov/ars/23/00622.htm); [DES 2026 rate chart](https://des.az.gov/sites/default/files/dl/UIT-0603A_FY26.pdf) | `az-payroll` |
| Arkansas | USD 7,000 | Not confirmed | None | [Division of Reemployment, 2026 notice](https://reemployment.arkansas.gov/calculating-taxable-wages/) | `ar-payroll` |
| California | USD 7,000 (UI and ETT) | 3.4% | SDI (including Paid Family Leave) 1.3% employee, no wage limit | [EDD rates and withholding](https://edd.ca.gov/en/Payroll_Taxes/Rates_and_Withholding) | `ca-payroll` |
| Colorado | USD 30,600 (USD 32,100 for 2027) | Not confirmed | FAMLI 0.88% of wages (10 or more employees; 0.44% for nine or fewer), split employer and employee | [CDLE premium rates](https://cdle.colorado.gov/ui/employers/requirements/premiums/premium-rates); [FAMLI 2026 premiums](https://famli.colorado.gov/news-article/update-your-employee-headcount-for-2026-premiums) |  |
| Connecticut | USD 27,000 | 1.90% | CT Paid Leave: not confirmed | [CT DOL tax rates and wage base](https://portal.ct.gov/dol/knowledge-base/articles/unemployment-taxes/tax-rates-and-taxable-wage-base) |  |
| Delaware | Not confirmed | Not confirmed | Delaware Paid Leave: not confirmed | [Delaware Division of Unemployment Insurance](https://labor.delaware.gov/divisions/unemployment-insurance/) |  |
| District of Columbia | Not confirmed | Not confirmed | DC Paid Family Leave (employer): not confirmed | [DC Department of Employment Services](https://does.dc.gov/) |  |
| Florida | USD 7,000 (reemployment tax) | 2.7% (first 10 quarters) | None | [Florida DOR, reemployment tax](https://floridarevenue.com/taxes/taxesfees/Pages/reemployment.aspx); [rate information](https://floridarevenue.com/taxes/taxesfees/Pages/rt_rate.aspx) | `fl-payroll` |
| Georgia | USD 9,500 | 2.70% | None | [GDOL employer UI FAQs](https://dol.georgia.gov/faqs-employers/employers-faqs-unemployment-insurance) | `ga-payroll` |
| Hawaii | USD 64,500 | 2.4% | TDI: not confirmed | [DLIR 2026 rate schedule](https://labor.hawaii.gov/ui/tax-rate-schedule-and-weekly-benefit-amount/) | `hi-payroll` |
| Idaho | USD 58,300 | 1.000% | None | [Idaho DOL Order 682](https://www.labor.idaho.gov/wp-content/uploads/2024/12/AO.682.pdf) | `id-payroll` |
| Illinois | USD 14,250 | 3.350% | None statewide (paid leave is an accrual duty, not a deduction) | [IDES 2026 rate chart](https://ides.illinois.gov/content/dam/soi/en/web/ides/ides_forms_and_publications/UI_tax_rates_2026.pdf) | `il-payroll` |
| Indiana | Not confirmed | Not confirmed | None | [Indiana DWD](https://www.in.gov/dwd/) |  |
| Iowa | USD 20,400 | 1.000% (construction 5.400%) | None | [IWD employer handbook, UI taxes](https://workforce.iowa.gov/employers/unemployment-insurance/unemployment-insurance-employer-handbook/unemployment-insurance-taxes) | `ia-payroll` |
| Kansas | Not confirmed | Not confirmed | None | [Kansas Department of Labor](https://www.dol.ks.gov/) |  |
| Kentucky | Not confirmed | Not confirmed | None | [Kentucky Office of Unemployment Insurance](https://kcc.ky.gov/) |  |
| Louisiana | USD 7,000 | Industry average assigned by LWC | None | [LWC 2026 rate table](https://www.laworks.net/Downloads/UI/WTS/2026RateTable.pdf); [LWC FAQ](https://www.laworks.net/FAQs/FAQ_UI_EmployerTaxes.asp) | `la-payroll` |
| Maine | Not confirmed | Not confirmed | Maine PFML: not confirmed | [Maine Bureau of Unemployment Compensation](https://www.maine.gov/unemployment/) |  |
| Maryland | USD 8,500 | Not confirmed | Maryland FAMLI: not confirmed | [Maryland Labor, 2026 tax rates](https://labor.maryland.gov/unemployment-insurance/employer-agent/tax-rate.shtml) |  |
| Massachusetts | USD 15,000 | 2.42% | PFML 0.88% (25 or more covered individuals; up to 0.46% withheld) or 0.46% (fewer than 25), to the Social Security wage base | [M.G.L. c. 151A, s. 14](https://malegislature.gov/Laws/GeneralLaws/PartI/TitleXXI/Chapter151A/Section14); [DFML contribution rates](https://www.mass.gov/info-details/paid-family-and-medical-leave-employer-contribution-rates-and-calculator) | `us-ma-payroll` |
| Michigan | USD 9,500 (USD 9,000 for a qualified employer) | 2.7% (construction 5.0%) | None | [UIA taxable wage base](https://www.michigan.gov/leo/bureaus-agencies/uia/employers/forms/accordion/taxable-wage-base); [UIA taxes](https://www.michigan.gov/leo/bureaus-agencies/uia/employers/about-taxes-and-ui/unemployment-insurance-taxes) | `mi-payroll` |
| Minnesota | USD 44,000 | By industry | Minnesota Paid Leave (from 2026): not confirmed | [UI Minnesota tax rates](https://www.uimn.org/employers/wages-taxes/tax-rates/index.jsp); [new employer rates](https://www.uimn.org/employers/wages-taxes/tax-rates/new-employer-rates.jsp) |  |
| Mississippi | USD 14,000 | Not confirmed | None | [MDES employer FAQs](https://www.mdes.ms.gov/employer-faqs/) | `ms-payroll` |
| Missouri | USD 9,000 | Not confirmed | None | [Missouri DES tax rates](https://labor.mo.gov/des/employers/tax-rates) |  |
| Montana | Not confirmed | Not confirmed | None | [Montana UI Division](https://uid.dli.mt.gov/) |  |
| Nebraska | Not confirmed | Not confirmed | None | [Nebraska Department of Labor](https://dol.nebraska.gov/) |  |
| Nevada | USD 43,700 | Not confirmed | None | [DETR, UI tax](https://detr.nv.gov/Page/UI_Tax) |  |
| New Hampshire | Not confirmed | Not confirmed | None (voluntary paid family leave plan) | [NH Employment Security](https://www.nhes.nh.gov/) |  |
| New Jersey | Not confirmed | Not confirmed | TDI and FLI: not confirmed | [NJ Department of Labor, rate information](https://www.nj.gov/labor/ea/employer-services/rate-info/) |  |
| New Mexico | Not confirmed | Not confirmed | None | [NM Department of Workforce Solutions](https://www.dws.state.nm.us/) |  |
| New York | USD 17,600 | 4.1% (3.4% normal, 0.625% subsidiary, 0.075% re-employment service fund) | PFL 0.432% employee, maximum USD 411.91; DBL: not confirmed | [NYS-45-I (1/26)](https://www.tax.ny.gov/pdf/current_forms/wt/nys45i.pdf); [DOL UI rates](https://dol.ny.gov/unemployment-insurance-rate-information); [WCB PFL 2026](https://www.wcb.ny.gov/content/main/PressRe/paid-family-leave-2026.jsp) | `ny-payroll` |
| North Carolina | USD 34,200 | 1% | None | [NC DES tax rate information](https://des.nc.gov/employers/tax-rate-information) | `nc-payroll` |
| North Dakota | Not confirmed | Not confirmed | None | [Job Service North Dakota](https://www.jobsnd.com/) |  |
| Ohio | USD 9,000 | 2.85% (construction 5.85%) | None | [ODJFS contribution rates](https://jfs.ohio.gov/page/CAJM.hl56rs7cilxWeGzd) | `oh-payroll` |
| Oklahoma | Not confirmed | Not confirmed | None | [OESC](https://oklahoma.gov/oesc.html) |  |
| Oregon | USD 56,700 | Not confirmed | Paid Leave Oregon: not confirmed | [Oregon Employment Department, 2026 rates](https://www.oregon.gov/employ/businesses/pages/current-tax-rate.aspx) |  |
| Pennsylvania | USD 10,000 (employer); employee 0.07% on all wages | 3.822% (construction 10.5924%) | None | [DLI UC yearly tax highlights](https://www.pa.gov/agencies/dli/resources/for-employers-and-educators/how-to-file/uc-tax/yearly-tax-highlights) | `pa-payroll` |
| Rhode Island | USD 30,800 | 1.00% UI plus 0.21% JDF (1.21%) | TDI 1.1% employee on the first USD 100,000 | [DLT 2026 quick reference](https://dlt.ri.gov/sites/g/files/xkgbur571/files/2025-12/FINAL%202026%20Quick%20Reference.pdf) | `ri-payroll` |
| South Carolina | Not confirmed | Not confirmed | None | [SC Department of Employment and Workforce](https://dew.sc.gov/) |  |
| South Dakota | Not confirmed | Not confirmed | None | [SD Department of Labor and Regulation](https://dlr.sd.gov/) |  |
| Tennessee | Not confirmed | Not confirmed | None | [Tennessee Department of Labor and Workforce Development](https://www.tn.gov/workforce.html) |  |
| Texas | USD 9,000 | 2.70% | None | [TWC UI tax rates](https://www.twc.texas.gov/programs/unemployment-tax/tax-rates) | `tx-payroll` |
| Utah | USD 50,700 | Not confirmed | None | [Utah DWS, tax rates](https://jobs.utah.gov/UI/Employer/Public/Questions/TaxRates.aspx) |  |
| Vermont | USD 15,400 | 1% (from 1 July 2026) | Not confirmed (child care contribution not re-read) | [Vermont Labor, UI reporting](https://labor.vermont.gov/unemployment-insurance/ui-employers/quarterly-reporting-taxable-wage-information); [UI rates](https://labor.vermont.gov/unemployment-insurance/ui-employers/unemployment-tax-rates) | `vt-payroll` |
| Virginia | USD 8,000 | Not confirmed | None | [VEC FAQ](https://vec.virginia.gov/frequently-asked-questions) |  |
| Washington | USD 78,200 (USD 82,000 for 2027) | 115% of the industry average, minimum 1% | PFML 1.13% to USD 184,500 (employee up to 71.43%); WA Cares 0.58% of all wages | [ESD wage base release](https://esd.wa.gov/); [Paid Leave employers](https://paidleave.wa.gov/employer-roles-responsibilities/); [WA Cares employers](https://wacaresfund.wa.gov/employers/) | `wa-payroll` |
| West Virginia | Not confirmed | Not confirmed | None | [WorkForce West Virginia](https://workforcewv.org/) |  |
| Wisconsin | USD 14,000 | Not confirmed | None | [DWD 2026 UI tax rates](https://dwd.wisconsin.gov/ui/employers/prior/taxrates-2026.htm) |  |
| Wyoming | Not confirmed | Not confirmed | None | [Wyoming DWS](https://dws.wyo.gov/) |  |

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Employee works from home in state B for an office in state A, all of the time | SUI to state B (localized there); withholding in B, plus A only under A's convenience rule if it has one |
| Employee splits time across states, none incidental | Base of operations, then direction and control, then residence |
| Washington employee earning USD 100,000 | UI stops at USD 78,200; PFML continues to USD 184,500; WA Cares on all wages |
| Rhode Island employee past the UI base | TDI continues to USD 100,000 |
| California employee earning USD 300,000 | SDI 1.3% on all wages: no wage limit |
| Massachusetts employer with fewer than 25 covered individuals | PFML 0.46%, all of which may be withheld; no employer medical share |
| Michigan employer with an unpaid balance of USD 25 or more | Not qualified for the USD 9,000 base: USD 9,500 applies |
| Rate notice not yet received | Use the new employer rate, then true up |

### Red flags to raise with the client

| Flag | Why it matters |
| --- | --- |
| Remote employees in states where no account is open | Unregistered SUI, withholding and paid leave liabilities |
| Paid leave state with no deduction on the payslip | Contributions owed for past quarters |
| Using a 2025 wage base in 2026 | Underpaid SUI (for example New York rose to USD 17,600, Washington to USD 78,200) |

## Worked cases

**Case 1, Washington, one employee earning USD 100,000.** SUI on USD 78,200 at the employer's rate. PFML: 1.13% x USD 100,000 = USD 1,130 (under the USD 184,500 cap), of which the employee may bear up to 71.43%, USD 807.16. WA Cares: 0.58% x USD 100,000 = USD 580, withheld from the employee.

```oa-check
name: Washington PFML and WA Cares on 100,000 of wages (2026)
inputs:
  wages: 100000
  pfml_cap: 184500
  sui_base: 78200
steps:
  - sui_wages: min(wages, sui_base)
  - pfml: min(wages, pfml_cap) * 0.0113
  - pfml_employee_max: round(pfml * 0.7143, 2)
  - wa_cares: wages * 0.0058
expected:
  sui_wages: 78200
  pfml: 1130.00
  pfml_employee_max: 807.16
  wa_cares: 580.00
```

**Case 2, a decision: where does the SUI go?** A New York employer hires an employee who works full time from home in New Jersey. Service is localized in New Jersey, so SUI is paid to New Jersey, not New York, whatever the office address. Had the employee worked three days a week in the New York office and two at home, neither state would be incidental: the base of operations (the New York office) decides, and New York SUI applies on the first USD 17,600 of wages. At the New York new employer rate of 4.1%, that is USD 721.60 for the year.

```oa-check
name: New York SUI at the new employer rate on 17,600 (2026)
inputs:
  wages: 95000
  ny_base: 17600
  ny_new_rate: 0.041
steps:
  - taxable: min(wages, ny_base)
  - sui: round(taxable * ny_new_rate, 2)
expected:
  taxable: 17600
  sui: 721.60
```

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-PAY-1 | Unregistered liabilities in past quarters | Refer: voluntary disclosure and back contributions |
| R-PAY-2 | Worker classification question | Refer |
| R-PAY-3 | Private disability or paid leave plan in place of the state plan | Refer to the state program rules |
| R-PAY-4 | A state marked "not confirmed" and the figure matters | Confirm on the agency's site first |

## Filing and payment

SUI returns and payments are quarterly in every state, filed with the state agency linked in the table; withholding returns follow each revenue department's deposit schedule. Paid leave contributions are reported and paid to the program's own portal in most states. The state payroll skills give forms and due dates.

## Completion checklist

- Each employee's SUI state fixed with the localization test.
- 2026 wage base and rate notice applied per state.
- Paid leave or disability deductions running where required, at the 2026 rate and cap.
- Withholding set for work state and resident state after reciprocity.
- New hire reports and local taxes handled.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| 26 U.S.C. 3306 (govinfo). Read for (c)(1) and the localization order of service. | https://www.govinfo.gov/content/pkg/USCODE-2023-title26/html/USCODE-2023-title26-subtitleC-chap23-sec3306.htm | 2026-11-13 |
| State payroll skills of 13 November 2026 (`ak-payroll`, `ar-payroll`, `az-payroll`, `ca-payroll`, `fl-payroll`, `ga-payroll`, `hi-payroll`, `ia-payroll`, `id-payroll`, `il-payroll`, `la-payroll`, `us-ma-payroll`, `mi-payroll`, `ms-payroll`, `nc-payroll`, `ny-payroll`, `oh-payroll`, `pa-payroll`, `ri-payroll`, `tx-payroll`, `vt-payroll`, `wa-payroll`) and `al-unemployment-contributions` on main. Read for each state's 2026 wage base, new employer rate and paid leave rate, with the agency links in the table. | https://edd.ca.gov/en/Payroll_Taxes/Rates_and_Withholding | 2026-11-13 |
| CT DOL, tax rates and taxable wage base. Read for 2026 "$27,000" and new employer rate "1.90%". | https://portal.ct.gov/dol/knowledge-base/articles/unemployment-taxes/tax-rates-and-taxable-wage-base | 2026-11-13 |
| CDLE premium rates. Read for the 2026 chargeable wage base of $30,600 and $32,100 for 2027. | https://cdle.colorado.gov/ui/employers/requirements/premiums/premium-rates | 2026-11-13 |
| Colorado FAMLI, 2026 premium rates. Read for 0.88% (10 or more employees) and 0.44% (nine or fewer). | https://famli.colorado.gov/news-article/update-your-employee-headcount-for-2026-premiums | 2026-11-13 |
| Maryland Labor, 2026 tax rates. Read for "the first $8,500 earned by each employee". | https://labor.maryland.gov/unemployment-insurance/employer-agent/tax-rate.shtml | 2026-11-13 |
| UI Minnesota, tax rates. Read for "The Taxable wage base for 2026 is $44,000". | https://www.uimn.org/employers/wages-taxes/tax-rates/index.jsp | 2026-11-13 |
| Missouri DES, tax rates. Read for 2026 taxable wage limitation $9,000. | https://labor.mo.gov/des/employers/tax-rates | 2026-11-13 |
| Nevada DETR, UI tax. Read for "The taxable wage base for calendar year 2026 is $43,700". | https://detr.nv.gov/Page/UI_Tax | 2026-11-13 |
| Oregon Employment Department, current rates. Read for "The UI taxable wage base for 2026 is $56,700 per employee". | https://www.oregon.gov/employ/businesses/pages/current-tax-rate.aspx | 2026-11-13 |
| Utah DWS, tax rates. Read for "During 2026, the taxable wage base is $50,700.00". | https://jobs.utah.gov/UI/Employer/Public/Questions/TaxRates.aspx | 2026-11-13 |
| VEC FAQ. Read for "the first $8,000 that each employee earns per year". | https://vec.virginia.gov/frequently-asked-questions | 2026-11-13 |
| Wisconsin DWD, 2026 UI tax rates. Read for "Taxable wage base $14,000". | https://dwd.wisconsin.gov/ui/employers/prior/taxrates-2026.htm | 2026-11-13 |

Not yet confirmed: 2026 wage bases and new employer rates for Delaware, DC, Indiana, Kansas, Kentucky, Maine, Montana, Nebraska, New Hampshire, New Jersey, New Mexico, North Dakota, Oklahoma, South Carolina, South Dakota, Tennessee, West Virginia and Wyoming; new employer rates for Arkansas, Colorado, Maryland, Mississippi, Missouri, Nevada, Oregon, Utah, Virginia and Wisconsin; 2026 paid leave and disability rates for Connecticut, Delaware, DC, Hawaii TDI, Maine, Maryland, Minnesota, New Jersey (TDI and FLI), New York DBL, Oregon and the Vermont child care contribution; state withholding forms and deposit schedules (old file's 2025 table withdrawn); state retirement savings mandates.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `us-state-payroll-matrix` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/us-state-payroll-matrix. If neither is available, confirm every figure against the official source pages cited above before relying on it.
