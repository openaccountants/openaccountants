---
name: pa-local-eit
description: "Use this skill for Pennsylvania local earned income tax (EIT) for tax year 2026 under the Local Tax Enabling Act (Act 511 of 1965) as rewritten by Act 32 of 2008, for residents, nonresidents, employees and the self-employed. It covers what is taxed (earned income and net profits, no offset of business losses against wages, military pay excluded), the higher-of withholding rule, PSD codes and the Residency Certification Form, the 1% statutory cap and the half-rate split between municipality and school district, credits for tax paid to other Pennsylvania localities and to other states, part-year domicile, quarterly estimates on net profits (15 April, 15 July, 15 October, 15 January) with the 100% and 90% safe harbours, the annual final return, and a triage of the Philadelphia wage, earnings and net profits taxes at the 2026 rates of 3.74% then 3.735% (residents) and 3.43% then 3.425% (nonresidents). Trigger on \"Pennsylvania local tax\", \"PA local earned income tax\", \"Act 32\", \"PSD code\", "
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/pa-local-eit"
  jurisdiction: "US-PA"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Pennsylvania local earned income tax (Act 32) and the Philadelphia wage and net profits taxes, tax year 2026

> **Built from the law, not yet approved by an accountant.** Written from the Local Tax Enabling Act as published by the Pennsylvania General Assembly, the DCED local income tax pages and the City of Philadelphia Department of Revenue pages, read on 13 November 2026. Review by a qualified professional before filing.

**Quick reference, tax year 2026**

| Item | Amount or rule, 2026 | Source |
| --- | --- | --- |
| Who levies it | Municipalities and school districts (not Philadelphia, which taxes under the Sterling Act) | [Local Tax Enabling Act](https://www.palegis.us/statutes/unconsolidated/law-information/view-statute?txtType=PDF&SessYr=1965&ActNum=0511.&SessInd=0) |
| Rate | Set locally by address; look it up with DCED's Address Search for both home and worksite | [DCED Local Withholding Tax FAQs](https://dced.pa.gov/local-government/local-income-tax-information/local-withholding-tax-faqs/) |
| Withholding rule | The higher of the home Total Resident EIT Rate and the worksite Work Location Non-Resident EIT Rate | same |
| Out-of-state resident working in PA | Resident PSD code 880000, resident rate 0%; owes the worksite nonresident rate | same |
| Philadelphia wage tax, 1 January to 30 June 2026 | 3.74% residents, 3.43% nonresidents | [Philadelphia Wage Tax (employers)](https://www.phila.gov/services/payments-assistance-taxes/taxes/business-taxes/business-taxes-by-type/wage-tax-employers/) |
| Philadelphia wage tax, from 1 July 2026 | 3.735% residents, 3.425% nonresidents | same |
| Philadelphia net profits tax, tax year 2026 | 3.735% residents, 3.425% nonresidents | [Philadelphia tax changes, June 2026](https://www.phila.gov/2026-06-11-what-you-need-to-know-about-changes-to-phillys-use-and-occupancy-tax/) |
| Estimates on net profits | 15 April, 15 July, 15 October 2026, 15 January 2027 | [LTEA section 502(c)(2)](https://www.palegis.us/statutes/unconsolidated/law-information/view-statute?txtType=PDF&SessYr=1965&ActNum=0511.&SessInd=0) |
| Annual final return | Same deadline as the PA-40 (15 April for a calendar year) | [LTEA section 502(c)(4)](https://www.palegis.us/statutes/unconsolidated/law-information/view-statute?txtType=PDF&SessYr=1965&ActNum=0511.&SessInd=0) |

## Scope and who this is for

- **In:** individuals who live or work in a Pennsylvania municipality or school district that levies an earned income and net profits tax: employees, sole proprietors, single-member LLC owners and partners with net profits, full-year and part-year residents, and nonresidents working in Pennsylvania.
- **Legal basis:** the Local Tax Enabling Act, Act 511 of 1965 (53 P.S. 6924.101 and following), whose Chapter 5 (added by Act 32 of 2008) sets the definitions, declaration and payment rules, tax collection districts, employer withholding and distribution. The text read is the General Assembly's consolidated Act 511 ([LTEA](https://www.palegis.us/statutes/unconsolidated/law-information/view-statute?txtType=PDF&SessYr=1965&ActNum=0511.&SessInd=0)).
- **Philadelphia** is triaged only: who owes what and at which 2026 rate, and where to file. Philadelphia returns, the Business Income and Receipts Tax (BIRT) and the School Income Tax are referred.
- **Out:** employer registration, deposit and W2-R mechanics and the Local Services Tax (`pa-payroll`); the state PA-40 (`pa-income-tax`); per capita, occupation, mercantile and business privilege taxes; Pittsburgh's payroll expense tax (an employer tax); corporations, which do not owe EIT on their profits ("net profits" means income from a business "other than a corporation", LTEA section 501).

## Ask the client first

1. **Home address and dates:** the full street address of every home in 2026, and the dates of any move (the PSD code and rate follow the exact address; a part-year domicile changes the base).
2. **Work addresses:** every worksite, including a home office, and for travelling employees how long each assignment lasted (90 consecutive days is the line).
3. **Income by type:** W-2 wages (PA wages, Box 16, not federal Box 1), net profits from PA Schedule C or partnership K-1s, and any business losses.
4. **What was withheld, and where:** local wages and tax in W-2 Boxes 18 to 20, and whether an out-of-state employer withheld local tax at all.
5. **Tax paid elsewhere:** Philadelphia wage or net profits tax, other states' income tax on the same income, and how much of that was already used as a credit on the PA-40 Schedule G-L.
6. **Estimates and last year:** 2026 estimated payments with dates, and the 2025 local tax (for the 100% safe harbour).

## The method, step by step

1. **Find the jurisdictions.** Run DCED's Address Search for the home and each worksite. It returns the PSD codes (six digits identifying each municipality), the Total Resident EIT Rate, the Work Location Non-Resident EIT Rate, and the tax collector ([DCED FAQs](https://dced.pa.gov/local-government/local-income-tax-information/local-withholding-tax-faqs/)). Employees complete a Residency Certification Form at hire and report any name or address change. If the home or the work is in Philadelphia, go to step 8 for that part.
2. **Build the base.** Earned income is the compensation reported under section 303 of the Tax Reform Code (the PA-40 compensation figure), less allowable employee business expenses. It does not include pay for active military service, "Offsets for business losses", or a clergy housing allowance. Net profits are the net income from a business other than a corporation as determined for the PA-40, excluding investment-type income and gains on farm machinery, draft and breeding livestock and other farm capital assets (LTEA section 501). Use PA wages: elective 401(k) deferrals are in PA compensation (see `pa-payroll`), so they are in the local base.
3. **Do not net a business loss against wages.** A Schedule C loss cannot reduce W-2 earned income (section 501, "Offsets for business losses").
4. **Part-year domicile.** Multiply taxable income by the months domiciled in the subdivision over 12. A month counts if domiciled there more than half the month; the day of the move counts in the new home; an equal split goes to the new home (section 502(b)).
5. **Apply the rate.** Resident tax is the base times the Total Resident EIT Rate. A nonresident owes a municipality's nonresident tax on pay for work there ("nonresident" in section 501 means performing services there for 90 or more consecutive days). Employers withhold the higher of the two rates (DCED FAQs).
6. **Credits, in this order.**
   - Resident tax paid to the home subdivision is credited against another Pennsylvania subdivision's like tax (section 317(b)). In practice the home collects its resident rate and the work location keeps only any excess of its nonresident rate.
   - Income tax paid to another state, or to a locality outside Pennsylvania, on the same earned income or net profits is credited against the local tax (section 317(e)), in proportion to the concurrent periods and not more than the amount paid (section 317(f)), and only to the extent the same credit was not taken on the PA-40 against state income tax (section 317(g)). Use the other state's tax against the 3.07% state tax on Schedule G-L first; only the part left over can reach the local return.
   - For crediting under section 317, "Income tax" includes all taxes on earned income or net profits authorised by any Pennsylvania law (section 501, paragraph (3)), which reaches Philadelphia's taxes; the Sterling Act governs Philadelphia's side, so refer any Philadelphia credit computation.
7. **Payments and return.** Subtract withholding and estimates. File the annual final return with the resident tax officer; amounts are rounded to whole dollars (section 502(c)(1)). Self-employed: declare and pay estimates (see the table below).
8. **Philadelphia part.** A Philadelphia resident owes the resident rate on all earned income wherever earned; a nonresident owes the nonresident rate on pay for work in Philadelphia. Employers withhold and pay the City, not an Act 32 collector; Act 32 does not apply to a Philadelphia resident working elsewhere in Pennsylvania (DCED FAQs). Net profits go on the City's Net Profits Tax return.

### Rates, bands and thresholds

| Item | Amount or rule | Condition | Source |
| --- | --- | --- | --- |
| Statutory cap on a tax on wages and other earned income | 1% | Where the municipality and the school district both levy the same tax, each is limited to one-half of the capped rate unless they agree otherwise (the usual 0.5% and 0.5%) (in words on the page). Higher rates exist under other laws; read the actual rate from DCED | [LTEA section 311(3) and the half-rate paragraph](https://www.palegis.us/statutes/unconsolidated/law-information/view-statute?txtType=PDF&SessYr=1965&ActNum=0511.&SessInd=0) |
| Cap on a payroll tax | 0.55% | Employer tax on payrolls | same, section 311(12) |
| Local Services Tax cap | See `pa-payroll` | Owned by the payroll skill | [DCED LST](https://dced.pa.gov/local-government/local-income-tax-information/local-services-tax/) |
| Resident PSD code and rate for someone living outside Pennsylvania | 880000 and 0% | Owes the worksite nonresident rate | [DCED FAQs](https://dced.pa.gov/local-government/local-income-tax-information/local-withholding-tax-faqs/) |
| Temporary job site | Under 90 consecutive days: the employer's permanent home office is the worksite; 90 or more: the job location | Philadelphia work is under the Sterling Act | same |
| Estimated tax on net profits, 2026 | Declaration and first quarter by 15 April 2026; then 15 July 2026, 15 October 2026, 15 January 2027 (equal installments) | First expected after 15 April: declare by the next of those dates; the fourth installment can be replaced by filing the final return by 31 January 2027 | [LTEA section 502(c)(2)](https://www.palegis.us/statutes/unconsolidated/law-information/view-statute?txtType=PDF&SessYr=1965&ActNum=0511.&SessInd=0) |
| Other income not subject to withholding (for example wages from an out-of-state employer that does not withhold) | Quarterly return and payment by 15 April, 15 July, 15 October and 15 January for the quarters ending 31 March, 30 June, 30 September and 31 December | The tax officer may waive quarterly returns under DCED criteria | same, section 502(c)(3) |
| Safe harbour against the estimate penalty | Four equal, timely payments of 100% of the prior year's tax, or of 90% of the current year's tax, in each case less local tax withheld for the current year | Either one | same, section 502(c)(5) |
| Annual final return | Same deadline as the PA-40 under Tax Reform Code section 330(a); weekend or holiday moves to the next business day | Calendar year | same, section 502(c)(4) |
| Business discontinued in the year | Final return and payment within 30 days | Net profits | same, section 502(c)(2)(v) |
| Employer quarterly return and payment | By the last day of the month after each calendar quarter, to the collector for each place of employment | Monthly and electronic if the employer elects one collector for several districts | same, section 512(4) and (5) |
| Employer annual return | By 28 February of the next year | With individual withholding statements | same, section 512(7) |
| Assessment limit | Five years after the due date, including extensions | Except a fraudulent return | same, section 319 |
| Philadelphia wage and earnings tax, wages paid 1 January to 30 June 2026 | 3.74% resident; 3.43% nonresident | Effective 1 July 2025 | [Philadelphia Wage Tax (employers)](https://www.phila.gov/services/payments-assistance-taxes/taxes/business-taxes/business-taxes-by-type/wage-tax-employers/) |
| Philadelphia wage and earnings tax, from 1 July 2026 | 3.735% resident; 3.425% nonresident | Effective 1 July 2026 | same |
| Philadelphia net profits tax, tax year 2026 (returns due 15 April 2027) | 3.735% resident; 3.425% nonresident | Residents on all net profits; nonresidents on Philadelphia business | [Philadelphia tax changes, June 2026](https://www.phila.gov/2026-06-11-what-you-need-to-know-about-changes-to-phillys-use-and-occupancy-tax/) |
| Philadelphia net profits tax, tax year 2025 (due 15 April 2026) | 3.74% resident; 3.43% nonresident | Returns for 2025 | [Philadelphia Net Profits Tax](https://www.phila.gov/services/payments-assistance-taxes/taxes/business-taxes/business-taxes-by-type/net-profits-tax/) |
| Philadelphia net profits tax estimates | 15 April and 15 June, each 25% of the prior year's net profits tax | Current-year estimates | same |

DCED's Address Search is a live tool; this skill gives no municipal rate. The worked cases below use assumed local rates for arithmetic only.

## Boundary and exception table

| Situation | Rule | Source |
| --- | --- | --- |
| Home rate 1.7%, worksite nonresident rate 1.0% | Withhold 1.7%; all of it goes to the home | DCED FAQs; LTEA 317(b) |
| Home rate 1.0%, worksite nonresident rate 2.0% | Withhold 2.0%; the home keeps 1.0%, the work location the excess | same |
| PA resident works only outside Pennsylvania for an out-of-state employer | The employer is not required to withhold local EIT (it may as a courtesy). The employee still owes the resident rate and pays quarterly to the home collector | DCED FAQs |
| Lives in another state, works in Pennsylvania | PSD 880000, rate 0%; owes the worksite nonresident rate, plus the LST | DCED FAQs |
| Lives in Philadelphia, works elsewhere in Pennsylvania | Act 32 does not apply; the employer withholds the Philadelphia resident rate and pays the City | DCED FAQs |
| Works in Philadelphia, lives elsewhere | The employer withholds the Philadelphia nonresident rate and pays the City | DCED FAQs |
| Wage period straddles 1 July 2026 in Philadelphia | Use the rate in force for the period paid: 3.74% or 3.43% before, 3.735% or 3.425% from 1 July | Philadelphia Wage Tax page |
| Schedule C loss and W-2 wages | No offset; local tax on the full wages | LTEA 501 |
| Active duty military pay | Not earned income, wherever earned | LTEA 501 |
| Clergy housing allowance | Not earned income | LTEA 501 |
| Interest, dividends and other investment-type income | Not net profits | LTEA 501 |
| Moved on 10 August | August counts in the new home (more than half the month there) | LTEA 502(b) |
| Other state taxed the wages and the credit was fully used on Schedule G-L | No local credit for that amount | LTEA 317(g) |
| Net profits first expected in August | Declare by 15 October and pay in equal installments on the remaining dates | LTEA 502(c)(2)(ii) |
| Paid 100% of 2025 local tax in four equal timely installments | No estimate penalty, even if 2026 tax is higher | LTEA 502(c)(5) |
| Fiscal-year taxpayer | The tax officer sets equivalent deadlines | LTEA 502(a)(2) |

### Defaults when a fact is missing

| Missing fact | Default |
| --- | --- |
| The exact address | Ask; do not infer a PSD code from a town name or ZIP code |
| Whether the employer withheld local tax | Check W-2 Boxes 18 to 20; if blank, assume nothing was withheld and plan quarterly payments |
| Which wage figure to use | PA wages (Box 16), which include 401(k) deferrals |
| A Philadelphia leg | Refer the Philadelphia return; note the rate for the period |

### Red flags

- Local wages equal to federal Box 1 when the employee made 401(k) deferrals: the local base is probably understated.
- A remote PA resident whose out-of-state employer withheld nothing: quarterly payments to the home collector are needed.
- Estimates scheduled on 30 April, 31 July and 31 October: those are employer quarterly dates, not the statutory estimate dates for net profits.

## Worked cases

Local EIT rates in these cases are assumed for illustration; look up the real rate by address with DCED. The Philadelphia rates and the statutory rules are the 2026 figures above.

**Case 1: resident commuting within Pennsylvania, and where the money goes.** PA wages $82,500 (including a $2,500 401(k) deferral). Assumed home rate 1.7%; assumed worksite nonresident rate 1.0%. Withhold the higher rate: $82,500 x 1.7% = $1,402.50, all to the home. If instead the home rate were 1.0% and the worksite 2.0%, the employer would withhold 2.0% ($1,650.00); the home would keep $825.00 and the work location $825.00.

```oa-check
name: PA local EIT 2026, higher-of rule and the split
inputs:
  wages: 82500
  home: 0.017
  work: 0.010
  home_b: 0.010
  work_b: 0.020
steps:
  - withheld_a: wages * max(home, work)
  - withheld_b: wages * max(home_b, work_b)
  - home_share_b: wages * home_b
  - work_share_b: withheld_b - home_share_b
expected:
  withheld_a: 1402.50
  withheld_b: 1650.00
  home_share_b: 825.00
  work_share_b: 825.00
```

**Case 2: self-employed resident, estimates and which safe harbour to use (a decision).** 2026 PA Schedule C net profit $74,500; assumed resident rate 1.0%; no wages. 2026 local tax $745.00. The 2025 local tax was $640.00. The 100% prior-year harbour needs four equal payments of $160.00 ($640.00 in total); the 90% current-year harbour needs $167.63 a quarter ($670.50 in total). The prior-year harbour is cheaper, so it decides; the balance of $105.00 is paid with the final return by 15 April 2027. Payment dates: 15 April, 15 July, 15 October 2026 and 15 January 2027.

```oa-check
name: PA local EIT 2026 estimates, prior-year vs current-year harbour
inputs:
  net_profit: 74500
  rate: 0.010
  prior_tax: 640
steps:
  - tax_2026: net_profit * rate
  - harbour_prior: prior_tax
  - harbour_current: tax_2026 * 0.90
  - required: min(harbour_prior, harbour_current)
  - quarterly: required / 4
  - balance_with_return: tax_2026 - required
expected:
  tax_2026: 745.00
  harbour_current: 670.50
  required: 640.00
  quarterly: 160.00
  balance_with_return: 105.00
```

**Case 3: Philadelphia nonresident wage tax across 1 July 2026.** A suburban resident earns $97,500 evenly through 2026, all for work in Philadelphia. January to June: $48,750 x 3.43% = $1,672.13. July to December: $48,750 x 3.425% = $1,669.69. Philadelphia wage tax withheld about $3,341.81 (rounded by pay period in practice). Whether and how the home municipality's EIT is credited is referred (see "When to refuse or refer").

**Case 4: remote employee of an out-of-state company.** A Lehigh County resident works from home for a California employer that does not withhold local tax (DCED treats a home-based employee's home as a worksite, so whether this employer should have registered and withheld is a question for its payroll adviser; see `pa-payroll`). PA wages $148,000; assumed resident rate 1.0%; local tax $1,480. The employee files quarterly returns and pays $370 by 15 April, 15 July, 15 October 2026 and 15 January 2027 (section 502(c)(3)), then the final return.

**Case 5: moved mid-year.** A taxpayer moves on 10 August 2026 from municipality A (assumed 1.0%) to municipality B (assumed 1.5%), with taxable income of $60,000. August counts in B. A: 7 months, $60,000 x 7/12 x 1.0% = $350. B: 5 months, $60,000 x 5/12 x 1.5% = $375.

## When to refuse or refer

- Philadelphia wage, earnings, net profits, BIRT and School Income Tax returns, refund petitions, and any credit between Philadelphia tax and another municipality's EIT.
- Pittsburgh's payroll expense tax and other employer-side city taxes.
- Credits for other states' tax where the PA-40 Schedule G-L credit and the local credit interact (section 317(g)), and dual residents.
- Part-year residents with income in more than one Pennsylvania locality and more than one tax officer.
- Collector notices, assessments, appeals and penalty disputes.
- Any request to use a remembered or prior-year local rate: refuse and look it up by address.
- S corporation owners' reasonable compensation questions and stock compensation timing.

## Filing and payment

1. **Find the collector.** DCED's Address Search names the tax collector (tax officer) for the home and for each worksite.
2. **Employees:** check that the employer withheld the higher rate and that Boxes 18 to 20 of the W-2 show it. File the annual final return with the resident tax officer even when withholding covers the tax; use the collector's form or the Annual Local Earned Income Tax Return from DCED (section 502(c)(1)), and attach W-2s.
3. **Self-employed:** file the declaration of estimated net profits with the resident tax officer and pay the first quarter by 15 April 2026; then pay on 15 July, 15 October 2026 and 15 January 2027, or file the final return by 31 January 2027 instead of the last installment. File the final return by the PA-40 deadline.
4. **Other unwithheld income:** quarterly return and payment on the same four dates (section 502(c)(3)).
5. **Payment:** to the resident tax officer, by its online portal, check or card; keep the confirmation.
6. **After filing:** the tax officer distributes the tax to the municipality and school district by PSD code, and may issue a notice or assessment within five years (section 319).
7. **Philadelphia:** wage tax is withheld and paid by employers through the Philadelphia Tax Center (quarterly returns, no separate annual reconciliation); net profits tax return by 15 April with estimates on 15 April and 15 June ([Philadelphia Net Profits Tax](https://www.phila.gov/services/payments-assistance-taxes/taxes/business-taxes/business-taxes-by-type/net-profits-tax/)).

## Completion checklist

- [ ] Exact home and work addresses run through DCED's Address Search for 2026.
- [ ] Base built from PA wages and PA net profits; no business loss offset; military pay excluded.
- [ ] Higher-of rule applied; out-of-state and Philadelphia cases identified.
- [ ] Part-year months counted under section 502(b).
- [ ] Other-state credit only for what was not used on the PA-40.
- [ ] Estimates on 15 April, 15 July, 15 October and 15 January, sized to a safe harbour.
- [ ] Annual final return filed with the resident tax officer by the PA-40 deadline.
- [ ] Philadelphia legs referred, with the right rate for each half of 2026.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Local Tax Enabling Act, Act 511 of 1965, consolidated text (General Assembly, PDF). Read for sections 311 (rate caps, half-rate rule), 317 (credits (b), (e), (f), (g)), 319 (five-year limit), 501 (definitions of earned income, net profits, nonresident), 502 (declaration, estimates, safe harbours, final return) and 512 (employer quarterly and annual returns). | https://www.palegis.us/statutes/unconsolidated/law-information/view-statute?txtType=PDF&SessYr=1965&ActNum=0511.&SessInd=0 | 2026-11-13 |
| DCED, Local Withholding Tax FAQs. Read for the higher-of rule, PSD codes, out-of-state employers, PSD 880000, temporary job sites, single collector and Philadelphia. | https://dced.pa.gov/local-government/local-income-tax-information/local-withholding-tax-faqs/ | 2026-11-13 |
| DCED, Local Services Tax. Read only to point to the LST rules kept in pa-payroll. | https://dced.pa.gov/local-government/local-income-tax-information/local-services-tax/ | 2026-11-13 |
| City of Philadelphia, Wage Tax (employers). Read for the rate history (3.735% and 3.425% from 1 July 2026; 3.74% and 3.43% from 1 July 2025), quarterly filing and no annual reconciliation. | https://www.phila.gov/services/payments-assistance-taxes/taxes/business-taxes/business-taxes-by-type/wage-tax-employers/ | 2026-11-13 |
| City of Philadelphia, Net Profits Tax. Read for who pays, the 2025 rates (3.74% and 3.43%), due date and the 15 April and 15 June estimates at 25% of the prior year's tax. | https://www.phila.gov/services/payments-assistance-taxes/taxes/business-taxes/business-taxes-by-type/net-profits-tax/ | 2026-11-13 |
| City of Philadelphia, "What you need to know about changes to Philly's Use and Occupancy Tax" (11 June 2026). Read for the 2026 wage, earnings, net profits and school income tax rates (3.735% and 3.425%). | https://www.phila.gov/2026-06-11-what-you-need-to-know-about-changes-to-phillys-use-and-occupancy-tax/ | 2026-11-13 |

Not yet confirmed: any municipal or school district rate (DCED's Address Search is interactive and was not run; the rates in the worked cases are assumed); how Philadelphia wage or net profits tax is credited against a suburban resident's home EIT under the Sterling Act (53 P.S. 15971, not read); the penalty and interest a tax officer charges on late local tax (LTEA section 509 not read in full); whether an out-of-state employer must withhold for a PA resident whose home is a worksite (DCED's FAQ answer covers only employees who physically work outside Pennsylvania); collectors' own forms, portals and extension practice.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `pa-local-eit` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/pa-local-eit. If neither is available, confirm every figure against the official source pages cited above before relying on it.
