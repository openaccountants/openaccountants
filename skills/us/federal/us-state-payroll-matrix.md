---
name: us-state-payroll-matrix
description: "State payroll for US employers in 2026: UI wage bases and new-employer rates for all 50 states and DC, state paid leave and disability contributions, multi-state localization, rate-notice boundaries and worked cases. Trigger on state payroll, SUI wage base, SUTA rate, new employer rate, state disability insurance, paid family leave deduction or multi-state payroll. Federal payroll is in us-form-941-940-payroll; withholding and local taxes use the companion Guides."
version: "3.3"
jurisdiction: US
tax_year: 2026
last_updated: 2026-11-28
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: payroll
type: cross-country-method
---


# US state payroll: unemployment insurance and paid leave by state, 2026

**Answer first.** Determine the employee’s unemployment-insurance state before applying that state’s wage base and the employer’s assigned rate. Withholding, paid leave, disability, new-hire reports and local taxes need their own decisions; a UI assignment alone does not settle them.

## Scope and who this is for

This matrix covers ordinary contributing private employers and wages already established as covered employment for 2026. It separates UI bases, new-employer UI rates and the additional contributions expressly described below. It is not a determination that an employer or payment is covered or exempt. Household, agricultural, governmental, reimbursable nonprofit, railroad, owner/officer, successor, shared-work and approved private-plan cases can have different rules: use R-PAY-2 or R-PAY-3 before applying an ordinary row.

A dash in the additional-contribution column is **not a zero rate or a finding that no program exists**. This matrix makes no deduction determination from a dash. An unresolved rate, coverage question or deduction is a **NON-USABLE HOLD**: do not enter a zero or estimate in payroll. **Check this point with one of our partner accountants.**

| Topic | Destination |
| --- | --- |
| Federal Forms 941, 940, W-2, FUTA and Social Security | `us-form-941-940-payroll` |
| New-hire deadlines, contractor reports and multistate reporting elections | `us-state-new-hire-reporting-matrix` |
| Resident/work-state withholding, reciprocity and convenience rules | `us-multi-state-residency-and-allocation` |
| State withholding tables, registration forms, deposit frequencies and reconciliations | State payroll companion in the matrix; otherwise the linked state agency |
| Local wage taxes, including Pennsylvania EIT/LST, Ohio municipal, NYC/Yonkers and Detroit | `us-local-income-tax-matrix` and the relevant state payroll Guide |
| State retirement mandates, paid-sick-leave accrual and voluntary insurance | Historical-topic destinations below; no payroll setting inferred here |

## Information to establish

Record each employee’s residence, actual work locations and travel; the employee’s base of operations; direction and control; state accounts and rate notices; prior subject wages with this employer; program-specific headcount; exemption letters; and any private plan or acquisition. Headcount tests differ by program. Do not substitute the number working in one state for the required program count.

## The method, step by step

1. **Allocate UI services in order.** Apply localization, then base of operations, then direction and control, then residence. Stop when a test allocates all services. Work entirely in one state is localized there; incidental temporary/transitional/outlying services do not necessarily break localization. For a base-of-operations allocation, some services must be performed in that state, and there must be a single base. If that fails, direction and control must be in a state where some services occur. Residence works only after the previous tests fail and some services occur in the residence state. These are state employment-law tests, not the agricultural/American-employer definitions previously cited in 26 USC 3306(c)(1)/(j). See [NY DOL’s sequential tests](https://dol.ny.gov/system/files/documents/2024/03/ia116.3.pdf).
2. **If no test allocates all services**, stop the ordinary one-state answer. Split coverage, special agreements and extraterritorial coverage require the relevant states’ law and an agency determination. **Check this point with one of our partner accountants.**
3. **Calculate UI on subject wages.** Use the actual period’s employer rate notice and annual base. Keep reportable wages separate from taxable wages. Do not treat every gross payment as subject wages. Another-state or predecessor wage credit is not automatic: establish the receiving state’s conditions and supporting records before reducing its base.
4. **Decide withholding separately.** Use the resident/work-state, reciprocity, convenience-rule and local-tax companions above. The employer’s postal address or a UI row is insufficient to establish income-tax withholding.
5. **Apply each additional program separately.** Use its subject-wage definition, cap, employee/employer split, headcount and exemption rules. UI bases do not cap disability or paid-leave contributions.
6. **Complete new-hire and filing duties** through the relevant companion and agency account. Do not assume that every multistate employer reports new hires in every work state, or that every employer class has the same quarterly filing schedule.

## Rates, bands and thresholds

Amounts below are annual USD bases per employee for the covered employer, except the expressly weekly Hawaii/NY limits. “New” means the relevant agency’s new-employer category; it is not a replacement for an experienced, successor, delinquent or otherwise assigned rate. Named additions are separated from pure UI rates. No unlisted assessment is represented as zero. State source reads are dated 28 November 2026, except California’s applicable completed primary-source reads from 27 November; the unchanged federal cap read is dated 26 November.

| State | 2026 UI taxable wage base | New-employer UI rate / named additions | Additional contribution established here | Official source / state companion |
| --- | --- | --- | --- | --- |


| Alabama | USD 8,000 | 2.70% for newly liable employers | Not established here | [source 1](https://adol.alabama.gov/faq/what-is-the-taxable-wage-base/); [source 2](https://adol.alabama.gov/faq/what-is-the-new-account-rate/) · `al-unemployment-contributions` |
| Alaska | USD 54,200, both UI shares | Employer maximum 1.00% plus employee 0.50% pending assigned new rate; 1.50% total | Employee UI: 0.50% to the same base; covered employees only, not unelected corporate-officer wages | [source 1](https://dol.alaska.gov/estax/forms/2026_First_Time_Filers.pdf); [source 2](https://www.labor.alaska.gov/estax/faq/WagesDeductions.htm) · `ak-payroll` |
| Arizona | USD 8,000 | 2.00% | Not established here | [source 1](https://des.az.gov/sites/default/files/dl/UIT-0603A_FY26.pdf) · `az-payroll` |
| Arkansas | USD 7,000 | 2.0% total: 1.8% base + 0.2% administrative assessment | Not established here | [source 1](https://reemployment.arkansas.gov/calculating-taxable-wages/) · `ar-payroll` |
| California | USD 7,000 UI/ETT | Ordinary new UI 3.4% for 2–3 years; ETT generally 0.1%, with statutory exemptions | State-plan SDI/PFL: 1.3% of SDI-subject wages, uncapped; do not equate every gross payment with subject wages | [source 1](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de44.pdf#page=16); [source 2](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de44.pdf#page=85); [source 3](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=976.6.&lawCode=UIC); [source 4](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de3395.pdf) · `ca-payroll` |
| Colorado | USD 30,600 | Industry-based introductory rate; use 2026 agency assignment | FAMLI 0.88% for 10+ employees, 0.44% for ≤9; employee at most 0.44%, to Social Security base (USD 184,500) | [source 1](https://cdle.nxt-dev.colorado.gov/employers/unemployment-insurance-premiums/premium-rates); [source 2](https://famli.colorado.gov/news-article/update-your-employee-headcount-for-2026-premiums); [source 3](https://content.govdelivery.com/accounts/CODLE/bulletins/40a6215); [source 4](https://content.govdelivery.com/accounts/CODLE/bulletins/3c9e0c5); [source 5](https://www.irs.gov/publications/p15) |
| Connecticut | USD 27,000 | 1.90% | CT Paid Leave employee 0.5% of program total wages (exclude FICA-excluded benefits), to the Social Security base (USD 184,500 in 2026) | [source 1](https://portal.ct.gov/dol/knowledge-base/articles/unemployment-taxes/tax-rates-and-taxable-wage-base); [source 2](https://www.ctpaidleave.org/remit-contributions); [source 3](https://www.irs.gov/publications/p15) |
| Delaware | USD 14,500 | 1.0% (including new construction) | State-plan Paid Leave: 0.32% parental only (10–24 eligible Delaware employees); 0.80% full coverage (25+), employee at most half; Delaware FICA wages capped at USD 184,500 | [source 1](https://labor.delaware.gov/divisions/unemployment-insurance/employer-services/); [source 2](https://delcode.delaware.gov/title19/c037/index.html#3701); [source 3](https://laborfiles.delaware.gov/main/pfl/Employer_and_TPAs_Guide_to_DPL.pdf); [source 4](https://delcode.delaware.gov/title19/c037/index.html#3705); [source 5](https://labor.delaware.gov/delaware-paid-leave/employers/); [source 6](https://www.irs.gov/publications/p15) |
| District of Columbia | USD 9,000 | 2.7% UI plus 0.2% administrative assessment | PFL employer 0.75% of covered wages; employee deduction not authorized by this row | [source 1](https://essp.does.dc.gov/DOES%20ESSP%20Employer%20Landing%20Page.html); [source 2](https://code.dccouncil.gov/us/dc/council/code/sections/32-541.03); [source 3](https://dcpaidfamilyleave.dc.gov/employer-information/) |
| Florida | USD 7,000 | 2.7% until ten reported quarters; successor election is separate | Not established here | [source 1](https://floridarevenue.com/taxes/taxesfees/Pages/rt_rate.aspx) · `fl-payroll` |
| Georgia | USD 9,500 | 2.70% until experience-rated | Not established here | [source 1](https://dol.georgia.gov/faqs-employers/employers-faqs-unemployment-insurance) · `ga-payroll` |
| Hawaii | USD 64,500 | 2.40% UI; separate 0.01% E&T charge | TDI: up to half premium, 0.5% of weekly wages and USD 7.50 weekly; preceding-payroll-period eligibility test below | [source 1](https://labor.hawaii.gov/ui/tax-rate-schedule-and-weekly-benefit-amount/); [source 2](https://labor.hawaii.gov/dcd/files/2025/12/2026-Maximum-Weekly-Wage-Base.pdf); [source 3](https://data.capitol.hawaii.gov/hrscurrent/Vol07_Ch0346-0398/HRS0392/HRS_0392-0043.htm); [source 4](https://labor.hawaii.gov/wp-content/uploads/2026/08/Disability-Compensation-Labor-Law-Notice_2026-1.pdf) · `hi-payroll` |
| Idaho | USD 58,300 | Standard new-employer 1.000%, at least first six calendar quarters; excludes reimbursable employers | Not established here | [source 1](https://www.labor.idaho.gov/wp-content/uploads/2024/12/AO.682.pdf); [source 2](https://www.labor.idaho.gov/Businesses/Unemployment-Tax-Rates/) · `id-payroll` |
| Illinois | USD 14,250 | Standard ineligible 3.350%; administrative support/waste management 3.450%; agency chart lists 5.4% small-employer rule for gross wages < USD 50,000 - use assigned notice to resolve applicability | Not established here | [source 1](https://ides.illinois.gov/content/dam/soi/en/web/ides/ides_forms_and_publications/UI_tax_rates_2026.pdf) · `il-payroll` |
| Indiana | USD 9,500 | Most new employers 2.5%; construction/government/successors follow separate agency rules | Not established here | [source 1](https://www.in.gov/dwd/indiana-unemployment/employers/FAQs/ess-enhancement-faq/); [source 2](https://www.in.gov/dwd/indiana-unemployment/employers/employer-guide/rate-computation/new-employer-premium-rate) |
| Iowa | USD 20,400 | 1.000% non-construction; 5.400% construction | Not established here | [source 1](https://workforce.iowa.gov/employers/unemployment-insurance/unemployment-insurance-employer-handbook/unemployment-insurance-taxes); [source 2](https://www.legis.iowa.gov/docs/code/2026/96.pdf) · `ia-payroll` |
| Kansas | USD 15,100 | New ordinary 1.75%; construction 5.55%; qualifying imported experience is separate | Not established here | [source 1](https://content.govdelivery.com/accounts/KSDOL/bulletins/40b913a); [source 2](https://www.kslegislature.gov/b2025_26/laws/044_000_0000_chapter/044_007_0000_article/044_007_0010a_section/044_007_0010a_k/) |
| Kentucky | USD 12,000 | Ordinary entry rate 2.7%; construction/successor exceptions require assigned notice | Not established here | [source 1](https://ui.ky.gov/Redesign/ResourcePages/TaxableWageBase.aspx); [source 2](https://apps.legislature.ky.gov/law/acts/22RS/documents/0029.pdf) |
| Louisiana | USD 7,000 | Assigned industry-average rate (NAICS); no single statewide new-employer percentage | Not established here | [source 1](https://www.laworks.net/Downloads/UI/WTS/2026RateTable.pdf); [source 2](https://www.laworks.net/FAQs/FAQ_UI_EmployerTaxes.asp) · `la-payroll` |
| Maine | USD 12,000 | 2.23% UI + 0.14% CSSF + 0.17% UPAF = 2.54% combined | PFML 1.0% if 15+ Maine employees meet counting test; otherwise 0.5%; employee up to 0.5%; capped at USD 184,500 | [source 1](https://legislature.maine.gov/statutes/26/title26sec1043.html); [source 2](https://www.maine.gov/unemployment/docs/2026/employers/2026.pdf); [source 3](https://www.maine.gov/paidleave/docs/2026/employers/WhatEmployersNeedtoKnowPremiumsandCountingEmployees.pdf); [source 4](https://www1.maine.gov/paidleave/docs/2026/employees/pfmlpremiumbenefitchart.pdf) |
| Maryland | USD 8,500 | Assigned new-employer rate 1.0%–2.6%; out-of-state construction uses industry rule | No 2026 FAMLI deduction: contributions begin 1 January 2027 | [source 1](https://labor.maryland.gov/unemployment-insurance/employer-agent/tax-rate.shtml); [source 2](https://paidleave.maryland.gov/about-the-program/frequently-asked-questions/contributions/) |
| Massachusetts | USD 15,000 | New registered <3 years UI 2.42%; new construction 6.08%; other assessments follow notice | PFML 25+ covered individuals 0.88%: EE max 0.46%, ER 0.42%; <25 effective 0.46%, all may be withheld; eligible wages capped at USD 184,500 | [source 1](https://malegislature.gov/Laws/GeneralLaws/PartI/TitleXXI/Chapter151A/Section14); [source 2](https://www.mass.gov/info-details/employer-contributions-to-unemployment); [source 3](https://www.mass.gov/info-details/paid-family-and-medical-leave-employer-contribution-rates-and-calculator); [source 4](https://malegislature.gov/Laws/GeneralLaws/PartI/TitleXXII/Chapter175M/Section6); [source 5](https://www.irs.gov/publications/p15) · `us-ma-payroll` |
| Michigan | USD 9,000 if qualified; otherwise USD 9,500 | First two liability years 2.7%; construction 5.0% in 2026 | Not established here | [source 1](https://www.michigan.gov/leo/bureaus-agencies/uia/employers/michigan-employer-advisor/2025/11/26/michigan-employer-advisor-november-2025); [source 2](https://www.michigan.gov/leo/bureaus-agencies/uia/employers/about-taxes-and-ui/unemployment-insurance-taxes) · `mi-payroll` |
| Minnesota | USD 44,000 | Assigned by industry | Paid Leave ordinary 0.88% to USD 185,000 (rounded Social Security limit); employee up to 0.44%; designated small employer 0.66% with employee still up to 0.44% | [source 1](https://uimn.org/employers/wages-taxes/tax-rates/index.jsp); [source 2](https://mn.gov/deed/assets/paid-leave-small-employer-premium-rate-designation-acc_tcm1045-716947.pdf) |
| Mississippi | USD 14,000 | Startup UI 1.0% first liability year, 1.1% second, 1.2% third+ until modified rate; excludes applicable WIT contribution | Not established here | [source 1](https://www.mdes.ms.gov/employer-faqs/) · `ms-payroll` |
| Missouri | USD 9,000 | 2.376% ordinary new employers; special nonprofit/shared-work rules excluded | Not established here | [source 1](https://labor.mo.gov/des/employers/tax-rates) |
| Montana | USD 47,300 | Positive-reserve new employers: industry UI 1.00%–2.00% plus 0.18% AFT; less than three full federal fiscal years | Not established here | [source 1](https://uid.dli.mt.gov/_docs/contributions-bureau/Rate-Explanation.pdf) |
| Nebraska | USD 9,000; category 20 USD 24,000 | New non-construction 1.25%; construction 5.40% | Not established here | [source 1](https://dol.nebraska.gov/webdocs/Resources/Items/2026%20UI%20guide%20to%20understanding.pdf) |
| Nevada | USD 43,700 | New UI 2.95% plus CEP 0.05% | Not established here | [source 1](https://detr.nv.gov/Page/UI_Tax); [source 2](https://ui.nv.gov/ESSHTML/Handbook/Employer_Handbook%28Published%29.pdf) |
| New Hampshire | USD 14,000 | Statutory initial 2.7% before quarterly fund adjustments; final 2026 quarter rate held | Voluntary paid-leave settings not established here | [source 1](https://www.nhes.nh.gov/forms/documents/emp-handbook.pdf); [source 2](https://gc.nh.gov/rsa/html/XXIII/282-A/282-A-81.htm); [source 3](https://gc.nh.gov/rsa/html/XXIII/282-A/282-A-82.htm) |
| New Jersey | USD 44,800 UI and WF/SWF; employer TDI uses this base | UI 2.6825% + WF/SWF 0.1175% = 2.80% (derived), both fiscal halves of 2026; employer state TDI 0.5% separate | Employee UI/WF 0.425% (derived) to USD 44,800; TDI 0.19% and FLI 0.23% to USD 171,100; covered state-plan wages | [source 1](https://www.nj.gov/labor/ea/employer-services/rate-info/) |
| New Mexico | NON-USABLE HOLD: 2026 wage base not proven | NON-USABLE HOLD: 2026 new-employer rate not proven | Not established here | [source 1](https://www.dws.state.nm.us/UI-Tax-Information) |
| New York | USD 17,600 | 4.1% new employer total, not successor rate | PFL employee 0.432% of gross wages, annual maximum USD 411.91; ordinary DBL employee up to 0.5% of wages, maximum USD 0.60 weekly; agreed enhanced plans held | [source 1](https://dol.ny.gov/unemployment-insurance-rate-information); [source 2](https://www.wcb.ny.gov/content/main/PressRe/paid-family-leave-2026.jsp); [source 3](https://www.tax.ny.gov/pdf/current_forms/wt/nys45i.pdf); [source 4](https://www.wcb.ny.gov/content/main/DisabilityBenefits/employee-disability-benefits.jsp); [source 5](https://ww3.nysif.com/Home/Employer/DBpolicyholder/AboutYourPolicy/DBPremiumRates) · `ny-payroll` |
| North Carolina | USD 34,200 | 1.000% beginning employer rate | Not established here | [source 1](https://des.nc.gov/employers/tax-rate-information) · `nc-payroll` |
| North Dakota | USD 46,600 | New non-construction: 1.00% positive / 6.07% negative balance; construction 9.67% either balance | Not established here | [source 1](https://www.jobsnd.com/sites/www/files/documents/jsnd-documents/uitaxrateschedules2026.pdf) |
| Ohio | USD 9,000 | 2.85%; construction 5.85% | Not established here | [source 1](https://jfs.ohio.gov/unemployment-services/for-employers/file-unemployment-taxes/tax-resources/contribution-rates) · `oh-payroll` |
| Oklahoma | USD 25,000 | 1.5% | Not established here | [source 1](https://oklahoma.gov/content/dam/ok/en/oesc/images/misc/Employer-Improtant-Numbers-2026.pdf) |
| Oregon | USD 56,700 | 2.4% new-employer UI | Paid Leave: 1% of subject wages to USD 184,500; employee 60% of premium, large employer 40%; <25 average employees exempt employer share unless assistance grant | [source 1](https://www.oregon.gov/employ/businesses/pages/current-tax-rate.aspx); [source 2](https://paidleave.oregon.gov/resources/); [source 3](https://paidleave.oregon.gov/employees/overview.html) |
| Pennsylvania | USD 10,000 employer; employee UC 0.07% uncapped | New non-construction 3.822%; construction 10.5924% (derived: printed decimals × 100); ordinary new rates include surcharge, not delinquency additions | Not established here | [source 1](https://www.pa.gov/agencies/dli/resources/for-employers-and-educators/how-to-file/uc-tax/yearly-tax-highlights) · `pa-payroll` |
| Rhode Island | USD 30,800; highest-tax-rate employers USD 32,300 | 1.00% UI plus 0.21% JDA = 1.21% (derived sum) | TDI/TCI employee 1.1% of first USD 100,000 | [source 1](https://dlt.ri.gov/sites/g/files/xkgbur571/files/2025-12/FINAL%202026%20Quick%20Reference.pdf) · `ri-payroll` |
| South Carolina | USD 14,000 | New non-successor: higher of class 12 or 1%, plus applicable assessment; numerical 2026 total requires notice | Not established here | [source 1](https://www.scstatehouse.gov/code/t41c027); [source 2](https://dew.sc.gov/employers/tax-rate-information) |
| South Dakota | USD 15,000 | First year: non-construction 1.20%, construction 6.00%, each plus 0.55% investment fee; do not use first-year rate for later liability years | Not established here | [source 1](https://dlr.sd.gov/ra/businesses/default.aspx); [source 2](https://dlr.sd.gov/ra/businesses/faq.aspx) |
| Tennessee | USD 7,000 | New-employer industry rate currently 2.7%; use assigned notice until experience eligible | Not established here | [source 1](https://www.tn.gov/workforce/employers/tax-and-insurance-redirect/unemployment-insurance-tax/ui-tax-rates.html); [source 2](https://lwdsupport.tn.gov/hc/en-us/articles/20035311746579-Instructions-for-Report-to-Determine-Status-Applications-for-Employer-Number) |
| Texas | USD 9,000 | Generally 2.70% during first six calendar quarters; use actual assigned 2026 rate; no universal all-industry conclusion | Not established here | [source 1](https://efte.twc.texas.gov/how_ui_claims_affect_employers.html); [source 2](https://efte.twc.texas.gov/estimate_cbs_and_tax_rates.html) · `tx-payroll` |
| Utah | USD 50,700 | Industry-based assigned rate; special out-of-state contractor rate requires notice | Not established here | [source 1](https://jobs.utah.gov/ui/Employer/Public/Empadv/Summer_2026.pdf); [source 2](https://jobs.utah.gov/UI/Employer/Public/Questions/TaxRates.aspx) |
| Vermont | USD 15,400 | From 1 July 2026: ordinary 1%; foreign construction NAICS 236: 1.9%, 237: 4.0%, 238: 2.7%; January–June rate requires period notice | CCC 0.44% on Vermont-withholding-subject wages; employee withholding at most 0.11%; courtesy withholding on out-of-state work does not create CCC | [source 1](https://labor.vermont.gov/unemployment-insurance/ui-employers/unemployment-tax-rates); [source 2](https://tax.vermont.gov/sites/tax/files/documents/GB-1326.pdf) · `vt-payroll` |
| Virginia | USD 8,000 | Initial base rate 2.5% plus applicable add-ons; foreign contractors use separate rule, not this ordinary base rate | Not established here | [source 1](https://vec.virginia.gov/faqs) |
| Washington | USD 78,200 (USD 82,000 for 2027) | 2026: 115% of industry average, minimum 1%; use assigned total notice | PFML 1.13% of gross wages excluding tips to USD 184,500; employee up to 71.43%; employer 28.57% subject to small-employer rule. WA Cares 0.58% uncapped gross wages; approved exemptions excluded | [source 1](https://esd.wa.gov/employer-requirements/unemployment-taxes/how-we-determine-tax-rates); [source 2](https://esd.wa.gov/about-us/news-release/2026/new-average-annual-wage-estimates-adjust-unemployment-insurance-and-paid-leave-benefits); [source 3](https://paidleave.wa.gov/employer-roles-responsibilities/); [source 4](https://wacaresfund.wa.gov/employers/) · `wa-payroll` |
| West Virginia | USD 9,500 | Assigned after application; use annual rate statement | Not established here | [source 1](https://code.wvlegislature.gov/21A-1A-28/); [source 2](https://workforcewv.org/businesses/unemployment-tax-information/frequently-asked-questions/) |
| Wisconsin | USD 14,000 | Payroll < USD 500,000: ordinary 3.05%, construction 2.50%; payroll ≥ USD 500,000: ordinary 3.25%, construction 2.70% | Not established here | [source 1](https://dwd.wisconsin.gov/ui/employer/prior/taxrates-2026) |
| Wyoming | USD 33,800 | New employers with <3 years experience: industry base plus four factors; use assigned total | Not established here | [source 1](https://dws.wyo.gov/dws-division/unemployment-insurance/wyui/unemployment-taxable-wage-base/); [source 2](https://dws.wyo.gov/dws-division/unemployment-insurance/employers/unemployment-tax-rates/) |


## Program conditions and boundaries

- **Colorado FAMLI:** count nationwide payroll employees who worked 20 or more calendar workweeks in 2025. Premiums are for Colorado-based employees. Failure to refresh the 2026 headcount by 28 February 2026 causes the full 0.88% rate to be applied. The original parenthetical 2027 UI base of USD 32,100 is retained as a future-year **NON-USABLE HOLD** pending the actual 2027 notice; do not use it for 2026.
- **Delaware Paid Leave:** the state-plan figures distinguish parental-only coverage from full coverage. Count the eligible Delaware employees under the previous-12-month statutory test, including those reasonably expected to meet its service requirements. Establish the worksite, employer exemptions and any approved employee waiver before deductions. Nine-or-fewer employers may participate voluntarily; federal employers and qualifying seasonal closures are exempt. The cap follows FICA: the official employer guide’s projected USD 183,600 for 2026 conflicts with the actual USD 184,500 Social Security base; use USD 184,500 for 2026 Delaware FICA wages. Private plans, waivers and reclassified out-of-state employees need their specific determination.
- **Hawaii TDI:** the withholding test is HRS 392-43(b)(1): in the 52 weeks immediately before the payroll period, at least USD 400 earned and at least 14 weeks in employment, each with remuneration for 20 or more hours. The 2026 published weekly wage base is USD 1,500.21 and the employee deduction is at most half the premium, 0.5% of weekly wages and USD 7.50 weekly. Benefit eligibility has a different reference date; do not substitute it for the payroll-period test.
- **Maine PFML:** the 1% test is at least 15 covered Maine employees on the employer’s established payroll in 20 or more calendar workweeks in the 12 months before 30 September, per FEIN. Count paid full-time, part-time, temporary and intermittent employees, including pay for only part of a pay period; do not import Colorado’s individual 20-week counting rule. The employee maximum is 0.5% whether the employer owes 1% or 0.5%. This is not a 60/40 split.
- **Massachusetts PFML:** use covered individuals, including covered contract workers where the law requires, rather than a raw nationwide headcount. For 2026 the family component is 0.18%; medical is 0.70%, with employee medical at most 0.28% and employer medical 0.42% for the larger category. Do not use 2027’s changed component allocation for 2026.
- **Minnesota Paid Leave:** the 2026 cap is USD 185,000, not USD 184,500: the statutory Social Security limit is rounded to the nearest thousand. A small-employer designation requires no more than 30 employees in each quarter of the basis period, average employee wage no greater than 150% of the statewide average, and compliant wage-detail reports. For 2026 that basis period is 1 October 2024–30 September 2025. Use the program’s maximum quarterly employee-record count and wage assessment; a one-day headcount does not establish the 0.66% rate.
- **Oregon Paid Leave:** the 25-employee test uses average total employees wherever they work or live. Below that size, the employer share is not compulsory unless an assistance grant applies; the employee portion must still be collected and paid. Do not apply the UI base to Paid Leave.
- **Washington:** agency-classified employers with fewer than 50 employees need not pay the PFML employer portion unless a small-business assistance grant applies. The employee portion must still be withheld or paid on the employee’s behalf. Do not recover missed premiums from later pay periods. WA Cares is separate; retain the approved exemption letter and stop deductions for an exempt worker.
- **Michigan:** the USD 9,000 base requires all quarterly reports, no missing or estimated reports and no delinquent balance of USD 25 or more in tax, penalty or interest. A nonqualifying employer uses USD 9,500, subject to the agency’s notice and correction procedure.
- **Vermont:** the UI new rates shown are effective from 1 July 2026. January–June’s actual rate is a **NON-USABLE HOLD** without the period notice. The child-care contribution is based on Vermont-withholding-subject wages, not every wage paid to a Vermont resident.

For every limited or held outcome above: **Check this point with one of our partner accountants.**

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Home in state B, office in A, all services physically in B | UI services localized in B. Resolve withholding independently; do not infer an A convenience-rule result from UI. [Localization source](https://dol.ny.gov/system/files/documents/2024/03/ia116.3.pdf) |
| Regular non-incidental services in several states | Apply the sequential tests, including service in the state used by the base/control/residence test; no automatic “office address wins.” [Localization source](https://dol.ny.gov/system/files/documents/2024/03/ia116.3.pdf) |
| Washington 2026 derived example wages USD 100,000 | UI taxable wages USD 78,200; PFML uses its own USD 184,500 cap and small-employer rule; WA Cares is uncapped unless exempt. [UI base](https://esd.wa.gov/employer-requirements/unemployment-taxes/how-we-determine-tax-rates); [program source](https://paidleave.wa.gov/employer-roles-responsibilities/) |
| Rhode Island employee past the UI base | Employee TDI/TCI continues to its separate USD 100,000 base. Highest-rate UI employers have the separate USD 32,300 base. [2026 table](https://dlt.ri.gov/sites/g/files/xkgbur571/files/2025-12/FINAL%202026%20Quick%20Reference.pdf) |
| California 2026 derived example: wages USD 300,000, all SDI-subject | 1.3% × USD 300,000 = USD 3,900 employee SDI; there is no annual SDI wage limit. [EDD historical rates](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de3395.pdf) |
| Massachusetts fewer than 25 covered individuals | Effective PFML 0.46%; all may be withheld; no mandatory employer medical share. [DFML 2026 split](https://www.mass.gov/info-details/paid-family-and-medical-leave-employer-contribution-rates-and-calculator) |
| Michigan unpaid tax/penalty/interest USD 25 or more, or missing reports | Do not assume qualification for the reduced USD 9,000 base. [2026 eligibility notice](https://www.michigan.gov/leo/bureaus-agencies/uia/employers/michigan-employer-advisor/2025/11/26/michigan-employer-advisor-november-2025) |
| Rate notice absent, or successor/acquisition | Obtain the agency determination. Alaska’s expressly documented temporary maximum is a specific exception, not a general authority to guess and true up. |
| New Mexico 2026 UI figures | **NON-USABLE HOLD.** The cited agency page did not provide readable operative figures in this proof; do not use secondary estimates. **Check this point with one of our partner accountants.** |

## Worked cases

**Case 1, Washington, one employee earning USD 100,000 in 2026.** Assume all USD 100,000 is subject gross wages, none is tips, the employee has no WA Cares exemption, and state-plan coverage applies. UI taxable wages are USD 78,200 at the assigned employer rate. The full PFML premium reference is 1.13% × USD 100,000 = USD 1,130. Employee maximum is 71.43%, USD 807.16; the employer portion is USD 322.84. A business classified below 50 employees with no assistance grant ordinarily remits the employee USD 807.16 portion (withheld or paid for the employee), without the compulsory employer portion. A business subject to the employer share pays both portions. “One employee” alone does not establish the employer’s size category. WA Cares is 0.58% × USD 100,000 = USD 580. [Washington program rules](https://paidleave.wa.gov/employer-roles-responsibilities/)

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
  - pfml_employer: round(pfml * 0.2857, 2)
  - wa_cares: wages * 0.0058
expected:
  sui_wages: 78200
  pfml: 1130.00
  pfml_employee_max: 807.16
  pfml_employer: 322.84
  wa_cares: 580.00
```

**Case 2, a decision: where does the UI go?** A New York employer hires an employee working full time from home in New Jersey. Services are localized in New Jersey, irrespective of the New York office address. In the original alternative - three days in the New York office and two days at home - assume neither state’s services are incidental **and the employee actually has a single base of operations at the New York office**, with services performed there. Then the base test allocates UI to New York. If that base assumption is not established, continue to direction/control and residence rather than infer it from the employer’s address. Retaining the original USD 95,000 wages, USD 17,600 2026 base and nonsuccessor new-employer rate of 4.1%, New York UI is USD 721.60. This is a UI calculation, not a withholding or paid-leave calculation. [Sequential tests](https://dol.ny.gov/system/files/documents/2024/03/ia116.3.pdf); [2026 rates](https://dol.ny.gov/unemployment-insurance-rate-information)

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

**Historical case retained, California 2025 executive earning USD 500,000 annually.** Assume all wages are SDI-subject under the state plan. The 2025 SDI rate was 1.2% with no wage limit: USD 500,000 × 1.2% = **USD 6,000**, not an unspecified “USD 6,000+”. This is a 2025 illustration; it does not use the 2026 1.3% rate. The current California USD 300,000 boundary above remains separate. [EDD year-by-year rates and uncapped-base footnote](https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de3395.pdf)

```oa-check
name: Historical California SDI executive (2025)
inputs:
  wages: 500000
  sdi_rate: 0.012
steps:
  - sdi: wages * sdi_rate
expected:
  sdi: 6000
```

```oa-check
name: California SDI on original boundary wages (2026)
inputs:
  wages: 300000
  sdi_rate: 0.013
steps:
  - sdi: wages * sdi_rate
expected:
  sdi: 3900
```



## Historical topics and destinations

The original 2025 matrix and later revisions remain in Git history. This 2026 matrix does not turn their unproved 2025 values into current payroll settings. The historical California executive case above retains its original year and USD 500,000 input.

| Original topic / year | Destination and usable boundary |
| --- | --- |
| Complete 2025 50-state/DC PIT types, brackets, no-wage-tax list, registration forms, withholding returns/deadlines, annual reconciliations and SUI bases/new/experience-rate ranges; original Ohio 2026 PIT projection and Mississippi 2030 rate / 2040 repeal-trigger projections | All 51 state rows remain above for 2026 UI. Historical 2025 amounts, PIT brackets, form mappings and schedules are **NON-USABLE HOLD** for any 2025 calculation until the applicable state payroll Guide and original-year official notice establish them. Do not use 2026 UI figures to amend a 2025 return. |
| 2025/new-hire portals, original federal “20-day” deadline and contractor reporting | `us-state-new-hire-reporting-matrix`; original universal deadline and per-work-state reporting instruction are not usable without the jurisdiction/election conditions. |
| 2024–2025 remote-work and convenience rules: NY, limited NJ, CT, PA, NE, AR and DE; reciprocity; nonresident/resident allocation | `us-multi-state-residency-and-allocation`. Historical blanket “never sets foot in NY” treatment and unproved revenue/litigation statistics are withdrawn. These are income-tax questions, separate from the UI cases. |
| Pennsylvania Act 32 EIT, resident/work PSD codes, Residency Certification, TCD registration and original USD 52 LST cap; Ohio RITA/CCA, principal workplace, original 20-day direction and separate SDIT | `us-local-income-tax-matrix`, `pa-payroll`, `oh-payroll`. Original local rates, deadlines, counts and universal cap/day-rule outcomes are **NON-USABLE HOLD**. Do not reverse an Ohio work-location rule from the old prose. |
| NYC/Yonkers, NY MCTMT, Kentucky occupational fees, Alabama/Missouri/Michigan/Maryland/Indiana/Delaware local/county taxes; Oregon TriMet/Lane and statewide transit tax | Relevant state payroll Guide and local-tax matrix. Historical 2025 locality lists, rates, coverage, PSD/county codes and transit rates are **NON-USABLE HOLD**; absence from the current UI matrix is not an exemption. |
| 2025 SDI/DBL/PFL/PFML in CA, NY, NJ, RI, MA, WA, OR, CT, CO, DC and ME; planned MN/DE/MD commencement | Current program rows and conditions above are for 2026 only. CA 2025 SDI 1.2% is proved for the retained case; other unproved 2025 program rates/caps/splits are **NON-USABLE HOLD**. The old Maryland contribution/benefit dates in 2025/2026 are superseded: contributions begin January 2027 and benefits January 2028. The old statement that WA Cares exemptions are effectively unavailable is withdrawn; approved letters control deductions. |
| CalSavers; Illinois Secure Choice; OregonSaves; CT MyCTSavings; MarylandSaves; Virginia RetirePath; Colorado SecureSavings; NJ and NY Secure Choice; employer retirement-plan exclusions | State payroll/formation Guide and the program’s official original-year rules. Historical enrollment headcounts/deadlines and contribution defaults - including the old CalSavers December 2023 claim - are **NON-USABLE HOLD** here. Do not infer a mandate or exemption from this list of topics. Employer-sponsored federal retirement plans remain with `us-self-employed-retirement`. |
| State/municipal paid-sick-leave accrual (AZ, CA, CO, CT, IL, MD, MA, MI, MN, NV, NJ, NM, NY, OR, RI, VT, WA, DC); workers’ compensation; private disability/paid-leave plans | Relevant state Guide and official program rules. These are separate from payroll contribution rates; original blanket compliance/absence statements are **NON-USABLE HOLD**. Commercial insurance prices are not set by this matrix. |

For all historical holds: **Check this point with one of our partner accountants.**

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-PAY-1 | Unregistered past-quarter liabilities, missed withholding or back contributions | **NON-USABLE HOLD** on a filing/payment or recovery-from-pay answer until disclosure, penalty and deduction rules are established. **Check this point with one of our partner accountants.** |
| R-PAY-2 | Worker/officer classification, unusual employer class, disputed localization, no allocating state or missing rate determination | **NON-USABLE HOLD** on the affected output. **Check this point with one of our partner accountants.** |
| R-PAY-3 | Private plan, voluntary coverage, waiver, assistance grant, succession or exemption outside the proved ordinary condition | **NON-USABLE HOLD** on applying the ordinary state-plan result. **Check this point with one of our partner accountants.** |
| R-PAY-4 | A held current or historical figure, period or operative condition matters | Do not estimate, set zero, or borrow another year’s value. **Check this point with one of our partner accountants.** |

## Filing and payment

Use the employer’s actual agency account and employer class. The former claim that UI filings/payments are quarterly in every state for every employer is withdrawn: Oregon, for example, expressly provides annual domestic reporting as well as ordinary quarterly reporting. Forms, deposit frequencies, weekend adjustments, notices and penalty calculations belong with the relevant state Guide and original-period agency instructions. This matrix provides no universal due date or authority to collect an earlier missed employee deduction in a later payroll.

Before completing payroll, record the UI allocation, subject-wage calculation, applicable annual base, assigned period rate, each additional program’s cap/split and headcount, withholding decision, new-hire reporting decision and filing schedule. An unpaid or missing registration is a red flag, not permission to choose the ordinary new-employer rate.

## Sources

Each state row links the official authority for its retained 2026 figures and conditions. Dates of completed primary-source reads: 28 November 2026, except reused California law/EDD reads of 27 November and the unchanged IRS Social Security base read of 26 November. The [IRS 2026 base](https://www.irs.gov/publications/p15) is USD 184,500; Minnesota’s own rule rounds its Paid Leave cap to USD 185,000. State Guides are destinations, not proof substitutes. The original blanket claim of a completed 13 November read for every linked row is not carried forward.

Not yet confirmed: New Mexico 2026 UI base/rate; New Hampshire final quarterly rate; Vermont January–June 2026 rate; Colorado original 2027 USD 32,100 base; historical 2025 tax/form/deadline outcomes and retirement/accrual settings held above; deduction outcomes marked not established here. These outputs are NON-USABLE HOLD. Check this point with one of our partner accountants.
