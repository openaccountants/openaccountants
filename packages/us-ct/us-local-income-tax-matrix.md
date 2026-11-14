---
name: us-local-income-tax-matrix
description: >
  City and county income and wage taxes in the United States for 2026: Ohio
  municipal income tax under Revised Code 718.04, Pennsylvania local earned
  income tax under the Department of Community and Economic Development rules,
  Kentucky occupational license taxes in Lexington and Louisville, Michigan
  city income taxes with the 2026 Detroit rates, the St. Louis and Kansas City
  earnings taxes, Maryland county income tax rates for 2026, Indiana county
  withholding rates, the New York City and Yonkers pointer, and the Portland
  Metro supportive housing tax and the Multnomah County preschool tax. Each
  row uses the locality's or the state's own page. Pennsylvania return
  mechanics stay in pa-local-eit.
jurisdiction: US
category: state-tax
tax_year: 2026
last_updated: 2026-11-13
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: cross-country-method
version: "1.0"
---

# US local income and wage tax matrix, tax year 2026

> **Source-cited draft.** Built from the state and city pages named below, read on 2026-11-13. No accountant has reviewed it. It is not a Circular 230 written opinion. Do not withhold or file a local return from this skill without a qualified professional for that city or county.

**Answer first.** Local income and wage taxes are not one national tax. For 2026, the regimes opened for this skill are Ohio municipalities, Pennsylvania earned income tax (Philadelphia separate), Kentucky occupational license taxes in Lexington and Louisville, Michigan city income taxes, the St. Louis and Kansas City earnings taxes, Maryland county income tax, Indiana county income tax, New York City and Yonkers tax reported on the New York return, and two Portland-area personal income taxes (Metro supportive housing and Multnomah County preschool). A city that is not named here is not certified to be free of a local income tax.

Pennsylvania's return, PSD codes, and forms are in `pa-local-eit`. This skill states the withholding rule from the Department of Community and Economic Development page that was read, and does not restate that skill's rate tables. State income tax is the state's own skill. Federal wages are not recomputed here.

## Scope

In scope: the local income, wage, earnings, or occupational license tax for the places named in the brief for this skill, at the rate or statutory limit on the page that was opened.

Out of scope:

| Topic | Where it goes |
| --- | --- |
| Pennsylvania earned income tax returns, forms, and a particular PSD rate | `pa-local-eit` |
| State personal income tax | that state's income tax skill |
| State payroll withholding, unemployment, and new-hire reporting | `us-state-payroll-matrix` |
| Federal income tax withholding | `us-form-941-940-payroll` |
| A city or county not named in the tables | not covered; open that locality's own page |

## Ask the client first

1. **Street address of the home and of the work site**, not just the state. Ohio, Pennsylvania, Michigan, Missouri, Maryland, Indiana, New York City, Yonkers, Metro, and Multnomah County all turn on the city or county.
2. **For Pennsylvania,** the resident municipality and the work municipality. The Department's rule is the higher of the total resident earned income tax rate and the work-location nonresident rate. Philadelphia is not that comparison.
3. **For Ohio,** the municipal rate on the ordinance and whether the city of residence grants a credit for tax paid to another municipality. The statute allows the credit. It does not require one, and it does not print a city's rate.
4. **For Detroit,** city of residence, the percentage of work performed in Detroit, and the number of withholding exemptions on Form 5527. A nonresident is withheld only if Detroit is the predominant place of employment.
5. **For the Portland area,** Oregon taxable income, filing status, and whether the address is inside Metro, inside Multnomah County, or both. Both taxes can apply to the same person.
6. **For Maryland,** the county of residence. Anne Arundel and Frederick are graduated. The flat-rate counties are in the table.

## The method, step by step

1. **Name the residence and the work location** at city and county level. If either place is not in the tables, stop and open that locality's page.
2. **Pick the regime, not a blended rate.** These taxes do not stack across states. They can stack inside one place when two jurisdictions both tax (a Detroit resident working in another Michigan city that has a tax; a Multnomah County resident inside Metro).
3. **Apply that row's resident or nonresident rule.** Do not use the resident rate for a nonresident unless the row says the nonresident owes it.
4. **Use only the rate on that row.** A 1 percent statutory cap in Ohio is not Lexington's 2.25 percent, and Indiana's county decimal is not Maryland's county percent.
5. **Withhold or file on the form and date the row states.** Where no month is stated, the page that was read did not give one.
6. **Send the state return to the state skill and the Pennsylvania local return to `pa-local-eit`.**

### Ohio, Pennsylvania, and Kentucky

| Place | Tax | 2026 figure | Rate | Who and when | Source |
| --- | --- | --- | --- | --- | --- |
| Ohio municipalities | Municipal income tax and withholding, Revised Code 718.04 | A municipal corporation may levy a tax on the income of every person residing in, or earning or receiving income in, the municipal corporation, measured by municipal taxable income. The rate must be uniform. | Except for a rate already over 1 percent on or before 23 March 2015, which may continue at the rate in the original ordinance, a rate over 1 percent needs approval of a majority of the electors voting on the question. A city may grant residents a credit for all or part of the tax paid to another municipal corporation, in Ohio or elsewhere. It is not required to grant the credit, and it is not required to refund tax it did not receive. | This row is the statewide limit. It does not print Columbus, Cleveland, Cincinnati, or any other city's rate. Use the ordinance or the city's tax administrator for the rate and the credit factor. | https://codes.ohio.gov/ohio-revised-code/section-718.04 |
| Pennsylvania, other than Philadelphia | Local earned income tax | The Department of Community and Economic Development does not print one statewide rate. The rate owed is the higher of the employee's total resident earned income tax rate and the work-location nonresident rate. Withhold that higher rate. PSD codes are six-digit numbers for each municipality. The employee completes a residency certification form at hire. | Look up the two rates in the Department's address search. Do not use a rate from `pa-local-eit` unless that skill is loaded and its figure is still the one on the Department's search. Quarterly withholding returns are due within 30 days after the end of the calendar quarter. An employer with worksites in more than one district may remit earned income tax to one collector, monthly and electronically. That option does not cover the local services tax. | A resident who works outside Pennsylvania still owes the resident rate. An out-of-state employer is not required to withhold it, and may do so as a courtesy. If it does not, the resident pays the home collector. An employee who lives outside Pennsylvania and works in Pennsylvania owes the work-location nonresident rate (resident PSD code 880000 and resident rate 0 on the certification form). Philadelphia is under the Sterling Act, not this comparison: withhold the Philadelphia resident rate for a Philadelphia resident, and the Philadelphia nonresident rate for a nonresident who works in Philadelphia, and remit to the Philadelphia Department of Revenue. This page does not print those Philadelphia percents. | https://dced.pa.gov/local-government/local-income-tax-information/local-withholding-tax-faqs/ |
| Lexington-Fayette, Kentucky | Occupational license fee | The Urban County Government assesses 2.25 percent on an individual's compensation and on a business's net profits. | 2.25 percent. The page does not print a separate nonresident rate. | Withholding forms are mailed to registered businesses. The page lists 2026 quarterly estimated net profit Form 228 ENP and 2026 due dates. Net profit extensions may use a copy of federal Form 4868, 8736, or 7004 if the local account number is on it, it arrives by the original due date, and the estimated tax is paid with it. | https://www.lexingtonky.gov/working/business-licensing-taxes/occupational-license-fee-rates-current-forms |
| Louisville Metro, Kentucky | Occupational license tax, plus transit tax and school boards tax | Regulations adopted 16 December 2025, effective 1 January 2026. On wages for work in Louisville Metro: occupational license tax 1.25 percent, plus transit tax 0.20 percent. School boards tax is another 0.75 percent and is imposed on resident employees, not on nonresident individuals. | A resident employee working in Louisville Metro: 1.25 plus 0.20 plus 0.75, which is 2.20 percent. A nonresident individual working in Louisville Metro: 1.25 plus 0.20, which is 1.45 percent. A business entity's net profit from activity in Louisville Metro is measured by 1.25 percent plus 0.20 percent plus 0.75 percent. | Residents owe on work done in Louisville Metro. Nonresident individuals do not pay the school boards tax. An ordained minister's pay for regular ministerial duties is exempt from the occupational license tax under KRS 91.200(10); the regulations say that exemption does not extend to the school boards tax. Quarterly withholding is due by the end of the following month (30 April, 31 July, 31 October, 31 January). | https://louisvilleky.gov/sites/default/files/2026-01/Louisville%20Metro%20Revenue%20Commission%20Regulations%20%282026%29.1.pdf |

### Michigan, Missouri, Maryland, and Indiana

| Place | Tax | 2026 figure | Rate | Who and when | Source |
| --- | --- | --- | --- | --- | --- |
| Detroit, Michigan | City income tax | 2026 withholding guide: residents 2.4 percent (multiply by 0.024). Nonresidents 1.2 percent (multiply by 0.012). Each exemption is USD 600 a year (USD 11.54 a week, USD 23.08 biweekly, USD 25.00 semimonthly, USD 50.00 a month, USD 1.64 a day). | Withhold on all compensation of a resident, wherever the work is done. Withhold on a nonresident only for work in Detroit, and only if Detroit is the predominant place of employment: a greater share of compensation than in any other Michigan city with an income tax, except the city of residence, and at least 25 percent. If a resident works in another Michigan city that taxes income, withhold for both cities, and compute the Detroit rate by subtracting the other city's nonresident rate from 2.4 percent. | Monthly Form 5323 is due on the 15th of the following month. The 2026 annual reconciliation, Form 5321, is due 28 February 2027. Exemptions follow federal dependency rules, plus an extra exemption if the employee or spouse is 65 or older or blind. A person who can be claimed on someone else's return claims zero personal exemptions. If the employee does not complete Form 5527, withhold at the resident rate with no exemptions. | https://www.michigan.gov/taxes/-/media/Project/Websites/taxes/Forms/City-Withholding/TY2026/5469_ty2026.pdf |
| Other Michigan cities on the Grand Rapids list | City income tax | The City of Grand Rapids income tax page prints a resident rate, a nonresident rate, and an exemption for each city below. The page does not print a tax year. Detroit's 2.40 and 1.2 percent on that page match the 2026 Treasury guide. | Grand Rapids: 1.50 percent resident, 0.75 percent nonresident, exemption USD 600. Highland Park: 2.00 percent resident, 1.00 percent nonresident, exemption USD 600. The page prints 1.00 percent resident and 0.50 percent nonresident for Albion, Battle Creek, Big Rapids, Flint, Grayling, Hamtramck, Hudson, Ionia, Jackson, Lansing, Lapeer, Muskegon, Muskegon Heights, Pontiac (printed there as "Pontaic"), Port Huron, Portland, Saginaw, Springfield, Walker, Benton Harbor, and East Lansing. | Exemptions printed on that page, other than the USD 600 cities: Battle Creek, Springfield, and Benton Harbor USD 750; Grayling USD 3,000; Hudson, Portland, and Saginaw USD 1,000; Ionia USD 700. Ionia and Muskegon are marked as prorating the exemption for part-year residency. The others on the page are marked as not prorating it. | https://www.grandrapidsmi.gov/departments/fiscal-services/income-tax/other-michigan-cities-with-income-tax/ |
| St. Louis, Missouri | Earnings tax | 1 percent. The Collector of Revenue says the one percent tax is collected from residents regardless of where the employer is, and from employees of businesses located in, or performing work in, the city regardless of where they live. | 1 percent of earnings. A partial day worked in the city counts as a day worked in the city. A person who moves during the year is liable only for wages earned while living or working in the city. | Form E-1 for a calendar year is due 15 April. The city does not allow an individual extension. After the deadline, penalty is 5 percent of the tax per month or fraction, not over 25 percent, plus interest of 1 percent per month or fraction. The taxpayer remains liable if the employer did not withhold. | https://www.stlouis-mo.gov/government/departments/collector/earnings-tax/individual-earnings-tax-info.cfm |
| Kansas City, Missouri | Earnings tax | 1 percent of earned income: salaries, wages, commissions, tips, and other compensation. | 1 percent. Residents pay even if they work outside the city. Nonresidents pay on income earned inside the city limits. The tax also applies to net profits of businesses. | Not taxed: Social Security, pensions, retirement accounts, and other non-earned income of a retiree; active military in a combat zone; non-profits. The page does not print the return due date. | https://www.kcmo.gov/city-hall/departments/finance/earnings-tax |
| Maryland counties | County income tax | Calendar year 2026 local income tax rates published by the Department of Legislative Services, source noted as the Office of the Comptroller. Anne Arundel and Frederick print as "Varies" because they adopted graduated rates beginning in tax year 2023. The brackets are not in this table. | Flat 2026 rates: Allegany 3.20 percent; Baltimore City 3.20; Baltimore County 3.20; Calvert 3.20; Caroline 3.20; Carroll 3.03; Cecil 2.74; Charles 3.03; Dorchester 3.30; Garrett 2.65; Harford 3.06; Howard 3.20; Kent 3.30; Montgomery 3.20; Prince George's 3.20; Queen Anne's 3.20; St. Mary's 3.20; Somerset 3.20; Talbot 2.40; Washington 2.95; Wicomico 3.20; Worcester 2.25. | These are county income tax rates, not the Maryland state income tax and not the real property tax rates in the same publication. | https://dls.maryland.gov/pubs/prod/NoPblTabPDF/2026CountyLocalTaxRates.pdf |
| Indiana counties | County income tax, withholding | Departmental Notice 1, effective 1 October 2026 (R47 / 10-26), prints a county rate for withholding on or after that date. The county of residence, and the county of principal work, are fixed on 1 January of the year. If the person lives in an Indiana county on 1 January, withhold that county's rate. If the person lives outside Indiana on 1 January but the principal place of work is in an Indiana county on 1 January, withhold that work county's rate. | The notice prints the rate as a decimal. Adams County, code 01, is 0.016. The same notice says the 2026 state adjusted gross income tax rate for individuals is 2.95 percent. That state rate is not the county rate. An asterisk marks a county whose rate changed after the 1 January 2026 notice. Boone County, code 06, is marked 0.0171 with an asterisk. | The full list of 92 counties is in that notice. This skill does not copy every county. Withholding is not required for some employees who will work in Indiana for 30 days or less; the notice points to its nonresident section. The notice is a withholding schedule. It is not, by its own words, the annual return rate for the whole year. | https://www.in.gov/dA/92797e5a5f/dn01.pdf?language_id=1 |

### New York City, Yonkers, and the Portland area

| Place | Tax | 2026 figure | Rate | Who and when | Source |
| --- | --- | --- | --- | --- | --- |
| New York City | Resident income tax, reported on the New York return | A New York City resident, or a part-year resident, who must file a New York State return reports New York City resident income tax on Form IT-201. New York City is the Bronx, Brooklyn, Manhattan, Queens, and Staten Island. | The 2026 withholding methods are in publication NYS-50-T-NYC, effective 1 January 2026 through 31 December 2026. That publication is a wage table. It does not state a single resident percentage, and this skill does not invent the bracket rates. | Use the New York State income tax skill for the state tax. This row is only the city layer. | https://www.tax.ny.gov/pit/file/nyc_yonkers_residents.htm |
| Yonkers, New York | Resident income tax surcharge, and nonresident earnings tax | Publication NYS-50-T-Y, revised January 2026, is effective 1 January 2026 through 31 December 2026. The resident surcharge in the withholding methods is 16.75 percent (0.1675) of the New York State withholding tax computed in that method. | The same publication states that the Yonkers nonresident earnings tax rate has not changed, and that the rate is 0.50 percent (0.0050) after the allowed exclusion. Supplemental wages withheld separately: Yonkers resident 1.95975 percent, Yonkers nonresident 0.50 percent. | A Yonkers resident reports the resident surcharge on Form IT-201. A nonresident of Yonkers with Yonkers earnings reports the nonresident earnings tax. The Metropolitan Commuter Transportation Mobility Tax is a separate item on the same Department page and is not computed here. | https://www.tax.ny.gov/pdf/publications/withholding/nys50_t_y.pdf |
| Metro (Portland area) | Supportive housing services personal income tax | For tax year 2026 the income threshold is USD 128,000 single and USD 205,000 joint. Single includes married filing separately. Joint includes married filing jointly, head of household, and qualifying surviving spouse. The 2021 through 2025 thresholds were USD 125,000 and USD 200,000. | 1 percent of Metro taxable income over that threshold. | Owed by a person over the threshold who lives in Metro (including part of the year), works in Metro, or has Metro-source income. The City of Portland Revenue Division administers it. File a separate Metro return. Beginning in 2026, estimated payments are required if the current-year tax and the prior-year tax for the program are each USD 5,000 or more. For 2021 through 2025 that figure was USD 1,000. | https://www.portland.gov/revenue/personal-tax |
| Multnomah County, Oregon | Preschool for All personal income tax | 1.5 percent of Multnomah County taxable income over USD 125,000 single or USD 200,000 joint, plus another 1.5 percent over USD 250,000 single or USD 400,000 joint. The City of Portland page says the rate will increase by 0.8 percent in 2028. It does not print a 2026 inflation adjustment of these thresholds. | The two 1.5 percent layers. A person over the USD 125,000 or USD 200,000 threshold who lives in the county, works in the county, or has county-source income owes the tax, including a part-year resident. | Administered by the City of Portland Revenue Division on a separate county return. The same estimated-tax change to USD 5,000 in 2026 applies. A person inside both Metro and Multnomah County can owe both this tax and the Metro tax. | https://www.portland.gov/revenue/personal-tax |

New York City withholding tables, read so they are not treated as a single rate: https://www.tax.ny.gov/pdf/publications/withholding/nys50_t_nyc.pdf

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Pennsylvania local services tax | Not the earned income tax. On the same Department page: if the combined local services tax is more than USD 10, withhold it over the pay periods, and a person with earned income and net profits under USD 12,000 from that locality is exempt. If the combined rate is USD 10 or less, it may be taken from the first paycheck. Do not use an earned income tax rate for it. |
| Philadelphia | Sterling Act, not the Act 32 higher-of comparison. The Department page says which Philadelphia rate to withhold and does not print the percent. |
| Ohio resident working in another Ohio city | Tax may be owed to both. The credit exists only if the city of residence has granted it. Read the ordinance. |
| Detroit resident working in another taxing Michigan city | Withhold both. Detroit's rate for that withholding is 2.4 percent minus the other city's nonresident rate. |
| Detroit nonresident, under 25 percent of work in Detroit | No Detroit withholding. The person may still have to file if they earned Detroit income. |
| St. Louis nonresident refund | Form E-1R. The employer must verify days worked outside the city. Refund claims are limited to one year from the original due date. |
| Maryland Anne Arundel or Frederick | Graduated. Do not use a flat rate from an earlier year. |
| Indiana county rate of 0.016 | That is the decimal printed for Adams County withholding on or after 1 October 2026. It is not 0.016 percent, and it is not the 2.95 percent state rate. |
| Metro and Multnomah both | Compute each tax on its own base and threshold. Do not add the 1 percent to the 1.5 percent and apply one threshold. |
| A city not in this skill | Do not answer "no local tax" from the absence of a row. |

## Worked cases

**A decision: Detroit resident or Detroit nonresident, same weekly pay.** The 2026 City of Detroit withholding guide's example is a resident paid USD 200 a week with 3 exemptions. The weekly exemption is USD 11.54. Three exemptions are USD 34.62. Taxable wages are USD 200.00 minus USD 34.62, which is USD 165.38. The resident tax is 2.4 percent of that, USD 3.97 after rounding to the cent, which is the amount the guide says to withhold.

The same wages for a nonresident whose predominant place of employment is Detroit, and who works 100 percent of the time in Detroit, use 1.2 percent instead of 2.4 percent. That is USD 1.98 after rounding to the cent. If only 60 percent of the nonresident's work is in Detroit, the guide's own method first limits gross pay to 60 percent (USD 120.00 in the guide's illustration) and only then subtracts exemptions. Do not apply 1.2 percent to the full USD 200.

The fact that decides the two rates is residence. A nonresident who does not meet the 25 percent predominant-place test is not in this withholding computation at all.

```oa-check
name: Detroit 2026 weekly withholding, resident against nonresident
inputs:
  gross: 200
  exemptions: 3
  weekly_exemption: 11.54
  resident_rate: 0.024
  nonresident_rate: 0.012
steps:
  - adjustment: exemptions * weekly_exemption
  - taxable: gross - adjustment
  - resident_withholding: round(taxable * resident_rate, 2)
  - nonresident_withholding: round(taxable * nonresident_rate, 2)
expected:
  adjustment: 34.62
  taxable: 165.38
  resident_withholding: 3.97
  nonresident_withholding: 1.98
```

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-LOC-MISSING | The home or the work city is not in the tables | Stop. Open that city's page. Do not answer zero. |
| R-LOC-OH-RATE | The client needs a named Ohio city's rate or credit factor | Revised Code 718.04 does not print it. Read the ordinance. |
| R-LOC-PA-PSD | The client needs the earned income tax for a street address | Use the Department's address search, then `pa-local-eit` for the return. Do not invent the rate. |
| R-LOC-PHL | Philadelphia wage tax percent | The Department page does not print it. Open the Philadelphia Department of Revenue page. |
| R-LOC-MD-GRAD | Anne Arundel or Frederick County | The 2026 table says the rate varies. Do not use a single percent. |
| R-LOC-IN-DATE | Withholding before 1 October 2026, or the rate on the annual Indiana return | The notice that was read is the 1 October 2026 withholding schedule. |
| R-LOC-NYC-BRACKET | A New York City resident tax computed from brackets | The withholding publication is a wage table. Do not invent the bracket percentages. |
| R-LOC-MI-YEAR | A Michigan city other than Detroit, and the client needs a rate dated 2026 | The Grand Rapids page prints rates and does not print a year. Confirm with that city. |

## Filing and payment

Use the office and the date in the row. Detroit monthly withholding is due on the 15th, and the 2026 annual reconciliation is due 28 February 2027. St. Louis Form E-1 is due 15 April, with no individual extension. Pennsylvania earned income tax withholding is due within 30 days after the quarter, or monthly if the employer has elected one collector. Louisville quarterly withholding is due by the end of the next month. Lexington, Kansas City, Maryland, Indiana, New York City, Yonkers, Metro, and Multnomah County: file on the return the administering office names. This skill does not add a due date the opened page did not state.

## Completion checklist

- Residence and work location are both written down, at city or county level.
- Resident and nonresident rates were not swapped.
- Philadelphia was not run through the Act 32 higher-of rule.
- Ohio credit was not assumed.
- Detroit exemptions were subtracted before the 2.4 or 1.2 percent, except on a bonus, which the guide taxes with no exemption adjustment.
- Metro and Multnomah were computed separately if both apply.
- Indiana's printed decimal was multiplied as printed, and was not confused with the 2.95 percent state rate.
- Any figure on the "Not yet confirmed" line was left blank.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Ohio Revised Code section 718.04. Read for the authority to tax, the 1 percent limit, the pre-23 March 2015 exception, voter approval above 1 percent, and the optional resident credit. | https://codes.ohio.gov/ohio-revised-code/section-718.04 | 2026-11-13 |
| Pennsylvania DCED, local withholding tax FAQs. Read for the higher-of earned income tax rule, PSD codes, out-of-state employees, Philadelphia withholding without a printed percent, quarterly due dates, and the local services tax distinction. | https://dced.pa.gov/local-government/local-income-tax-information/local-withholding-tax-faqs/ | 2026-11-13 |
| Lexington-Fayette Urban County Government, occupational license fee rates. Read for the 2.25 percent fee on compensation and net profits, and for the 2026 net profit forms. | https://www.lexingtonky.gov/working/business-licensing-taxes/occupational-license-fee-rates-current-forms | 2026-11-13 |
| Louisville Metro Revenue Commission regulations, effective 1 January 2026. Read for section 1.02: 1.25 percent occupational license tax, 0.20 percent transit tax, and 0.75 percent school boards tax on resident employees. | https://louisvilleky.gov/sites/default/files/2026-01/Louisville%20Metro%20Revenue%20Commission%20Regulations%20%282026%29.1.pdf | 2026-11-13 |
| Michigan Department of Treasury, 2026 City of Detroit income tax withholding guide (Form 5469). Read for 2.4 percent, 1.2 percent, the USD 600 exemption, the weekly example, and the predominant-place test. | https://www.michigan.gov/taxes/-/media/Project/Websites/taxes/Forms/City-Withholding/TY2026/5469_ty2026.pdf | 2026-11-13 |
| City of Grand Rapids, other Michigan cities with an income tax. Read for the resident and nonresident rates and exemption amounts. The page does not state a tax year. | https://www.grandrapidsmi.gov/departments/fiscal-services/income-tax/other-michigan-cities-with-income-tax/ | 2026-11-13 |
| St. Louis Collector of Revenue, individual earnings tax. Read for the 1 percent tax, who pays, Form E-1 due 15 April, and the 5 percent and 1 percent penalty and interest. | https://www.stlouis-mo.gov/government/departments/collector/earnings-tax/individual-earnings-tax-info.cfm | 2026-11-13 |
| Kansas City, Missouri, earnings tax. Read for the 1 percent tax, residents, nonresidents, and the retirement and combat-zone exclusions. | https://www.kcmo.gov/city-hall/departments/finance/earnings-tax | 2026-11-13 |
| Maryland Department of Legislative Services, 2026 local tax rates. Read for the calendar year 2026 county income tax column, including "Varies" for Anne Arundel and Frederick. | https://dls.maryland.gov/pubs/prod/NoPblTabPDF/2026CountyLocalTaxRates.pdf | 2026-11-13 |
| Indiana Department of Revenue, Departmental Notice 1, effective 1 October 2026. Read for the 1 January county rule, Adams County 0.016, the 2.95 percent state rate, and the statement that the notice is for withholding. | https://www.in.gov/dA/92797e5a5f/dn01.pdf?language_id=1 | 2026-11-13 |
| New York Tax Department, New York City, Yonkers, and MCTMT. Read for who reports city tax on Form IT-201. | https://www.tax.ny.gov/pit/file/nyc_yonkers_residents.htm | 2026-11-13 |
| New York publication NYS-50-T-Y (1/26). Read for the 16.75 percent Yonkers resident withholding factor and the 0.50 percent nonresident earnings tax, effective through 31 December 2026. | https://www.tax.ny.gov/pdf/publications/withholding/nys50_t_y.pdf | 2026-11-13 |
| New York publication NYS-50-T-NYC (1/26). Read to confirm it is a 2026 withholding table and not a single resident rate. | https://www.tax.ny.gov/pdf/publications/withholding/nys50_t_nyc.pdf | 2026-11-13 |
| City of Portland Revenue Division, personal income tax. Read for the 2026 Metro thresholds of USD 128,000 and USD 205,000, the 1 percent Metro rate, the Multnomah 1.5 percent layers, and the 2026 estimated-tax figure of USD 5,000. | https://www.portland.gov/revenue/personal-tax | 2026-11-13 |

Not yet confirmed: any named Ohio city's 2026 rate and credit factor; the 2026 Philadelphia resident and nonresident wage tax percents; a tax year on the Grand Rapids list of other Michigan city rates; the Anne Arundel and Frederick County 2026 graduated brackets; Indiana county rates for withholding before 1 October 2026 and the rate to use on the 2026 annual county return; the New York City resident tax bracket percentages for 2026; Kansas City's earnings tax return due date; whether every Kentucky city other than Lexington and Louisville imposes an occupational license tax and at what rate; and any local income tax in a city or county this skill does not name.
