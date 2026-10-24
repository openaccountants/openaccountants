---
name: se-cross-border
description: "Use when a person or company crosses the Swedish border for tax. Covers unlimited tax liability for individuals (living in Sweden, a stay of six months in a row, or an essential connection after leaving, presumed for five years for citizens and people who lived here ten years), company residence by registration, the expert tax relief (25% of pay tax-free for up to seven years, 2026 pay floor SEK 88,801 a month, apply within three months), SINK at 22.5% for non-residents in 2026 (20% from 2027) and the option to be taxed as a resident, the ten-year rule on shares for people who leave, company exit taxation and the EEA payment deferral, kupongskatt at 30% on dividends, and EU social security. Tax year 2026. Trigger on: moving to Sweden, leaving Sweden, non-resident, expat, expertskatt, SINK, kupongskatt, exit tax Sweden, väsentlig anknytning, A1. Out of scope: se-income-tax, se-capital-gains, sweden-payroll, se-social-contributions."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/se-cross-border"
  jurisdiction: "SE"
  tax_year: "2026"
  last_updated: "2026-10-23"
  authored_by: "Ryan Duguid"
  trust_label: "Accountant-authored"
  review_status: "pending_review"
---

# Sweden: cross-border tax for people and companies (2026)

This skill is the hub for what changes when a person or a company comes into or leaves Sweden. It summarises the rules and points to the detailed skills in this pack. The Swedish income year is the calendar year. The authority is Skatteverket (the Swedish Tax Agency). The main laws are the Income Tax Act (inkomstskattelagen 1999:1229, IL), the Act on Special Income Tax for Non-Residents (lag 1991:586 om särskild inkomstskatt för utomlands bosatta, SINK), the Withholding Tax on Dividends Act (kupongskattelagen 1970:624) and the Tax Procedure Act (skatteförfarandelagen 2011:1244, SFL).

Detail lives elsewhere. Read [se-income-tax](se-income-tax.md) for income tax on a sole trader, [se-capital-gains](se-capital-gains.md) for gains, [sweden-payroll](sweden-payroll.md) for withholding on pay, [se-social-contributions](se-social-contributions.md) for self-employed contributions, and [se-corporate-tax](se-corporate-tax.md) for corporate income tax.

## Who this applies to

### Individuals: unlimited and limited tax liability

Sweden does not use a day count. A person is unlimited taxable (obegränsat skattskyldig) if they (3 kap. 3 § IL):

1. are resident (bosatt) in Sweden: Skatteverket reads this as having their real home here, and such a person should be registered in the population register;
2. stay in Sweden on a lasting basis (stadigvarande vistelse): Skatteverket's rule is a stay of at least six months in a row, and short trips home do not break it; or
3. have an essential connection (väsentlig anknytning) to Sweden and lived here before.

([Skatteverket: skattskyldighet](https://www.skatteverket.se/privat/skatter/arbeteochinkomst/sabeskattasdinlon/skattskyldighet.4.65fc817e1077c25b8328000206.html))

**Essential connection after leaving (3 kap. 7 § IL).** Skatteverket weighs: Swedish citizenship, how long the person lived here, whether they are settled in one place abroad, whether they are abroad to study or for health, a year-round home in Sweden, family in Sweden (spouse and children under 18), a business here, holdings that give significant influence over a business here, and real property here. One factor alone can be enough. For five years from the day of departure, a Swedish citizen, or anyone who lived or stayed in Sweden for at least ten years, is presumed to have an essential connection unless they show they do not. After five years the burden moves to Skatteverket. ([Skatteverket: har du flyttat från Sverige?](https://www.skatteverket.se/privat/internationellt/bosattutomlands/harduflyttatfransverige.4.7459477810df5bccdd4800030036.html))

Everyone else is limited taxable (begränsat skattskyldig, 3 kap. 17 § IL).

**No split-year rule in the statute.** Liability runs from the day a person becomes resident or starts a lasting stay, and ends when they are no longer resident and have no essential connection. Income before arrival or after departure is taxed only if it is Swedish-source income caught by the limited liability rules. A resident who works abroad can be exempt on that pay under the six-month rule (taxed in the work country) or the one-year rule (3 kap. 9 § IL).

### Companies

A legal person is unlimited taxable if it counts as Swedish by registration or, without registration, by the seat of its board or a similar fact (6 kap. 3 § IL). Sweden has no place-of-management test in its domestic law. Foreign legal persons are limited taxable (6 kap. 7 § IL).

## Rates, bands and thresholds

| Item | Amount | Tax year | Source |
|---|---|---|---|
| SINK on pay, pensions and board fees of non-residents | 22.5% of gross taxable income (Lag 2025:1355) | 2026 (income received after 31 Dec 2025) | [SINK 7 §](https://data.riksdagen.se/dokument/sfs-1991-586.text); [Skatteverket: SINK](https://www.skatteverket.se/privat/internationellt/bosattutomlands/sinksarskildinkomstskattforutomlandsbosatta.4.6fdde64a12cc4eee23080002583.html) |
| SINK from 2027 | 20% (Lag 2025:1356, in force 1 Jan 2027, for income received after 31 Dec 2026) | 2027 | [SINK 7 §](https://data.riksdagen.se/dokument/sfs-1991-586.text) |
| SINK on seamen's income | 15% | 2026 | [SINK 7 §](https://data.riksdagen.se/dokument/sfs-1991-586.text) |
| SINK monthly allowance on social insurance pensions | SEK 3,799 a month (1/12 of 0.77 price base amount) | 2026 | [Skatteverket: belopp och procent 2026](https://www.skatteverket.se/privat/skatter/beloppochprocent/2026.4.1522bf3f19aea8075ba21.html) |
| Non-resident opting to be taxed under IL: municipal tax | 32.38% (average municipal rate) | 2026 | [Skatteverket: belopp och procent 2026](https://www.skatteverket.se/privat/skatter/beloppochprocent/2026.4.1522bf3f19aea8075ba21.html) |
| State income tax on earned income | 20% above taxable earned income of SEK 643,000 (skiktgräns) | 2026 | [Skatteverket: belopp och procent 2026](https://www.skatteverket.se/privat/skatter/beloppochprocent/2026.4.1522bf3f19aea8075ba21.html) |
| Basic deduction (under 66) | SEK 17,400 at high incomes, up to SEK 45,600 | 2026 | [Skatteverket: belopp och procent 2026](https://www.skatteverket.se/privat/skatter/beloppochprocent/2026.4.1522bf3f19aea8075ba21.html) |
| Tax on capital income (incl. ten-year rule gains and Swedish rental income of individuals) | 30% | 2026 | [Skatteverket: belopp och procent 2026](https://www.skatteverket.se/privat/skatter/beloppochprocent/2026.4.1522bf3f19aea8075ba21.html) |
| Expert tax relief | 25% of pay tax-free, for up to 7 years | 2026 | [11 kap. 22-23 §§ IL](https://data.riksdagen.se/dokument/sfs-1999-1229.text); [Forskarskattenämnden](https://forskarskattenamnden.se/andra-sprak/taxation-of-research-workers-board/about-tax-relief) |
| Expert relief pay floor | more than 1.5 x price base amount a month: at least SEK 88,801 for work starting in 2026 (price base amount SEK 59,200); SEK 89,401 for 2027 starts | 2026 | [Forskarskattenämnden: remuneration rate](https://forskarskattenamnden.se/andra-sprak/taxation-of-research-workers-board/conditions-for-tax-relief/remuneration-rate) |
| Company income tax (also the rate on company exit gains) | 20.6% | 2026 | [65 kap. 10 § IL](https://data.riksdagen.se/dokument/sfs-1999-1229.text); [Skatteverket: belopp och procent 2026](https://www.skatteverket.se/privat/skatter/beloppochprocent/2026.4.1522bf3f19aea8075ba21.html) |
| Kupongskatt on dividends from Swedish shares to non-residents | 30% (treaty may reduce) | 2026 | [Kupongskattelagen 5 §](https://data.riksdagen.se/dokument/sfs-1970-624.text) |
| Interest paid to non-residents | No Swedish tax: interest is not on the list of income a limited taxpayer is taxed on | 2026 | [3 kap. 18 § and 6 kap. 11 § IL](https://data.riksdagen.se/dokument/sfs-1999-1229.text) |
| Royalties paid to non-residents | No withholding. Taxed by assessment as income of a Swedish permanent establishment if paid from a Swedish business; exempt for qualifying associated EU companies (6 a kap. IL) | 2026 | [6 kap. 11 § and 6 a kap. IL](https://data.riksdagen.se/dokument/sfs-1999-1229.text) |

Sweden has no separate exit tax on individuals. The departure rule for individuals is the ten-year rule on shares (see the base).

## The taxable base

**Unlimited taxpayers** are taxed on worldwide income (3 kap. 8 § IL). There is no remittance basis.

**Limited taxpayers (individuals)** are taxed in Sweden on, among others (3 kap. 18 § IL and SINK 5 §):

- pay for work done in Sweden, board fees from Swedish companies wherever the work is done, Swedish public pay and pensions, and Swedish pensions: under SINK at 22.5%, unless they ask to be taxed under IL;
- income of a Swedish permanent establishment or Swedish real property (business income);
- current income from, and gains on, Swedish private housing and tenant-owner flats (capital income);
- dividends from Swedish companies: through kupongskatt, not SINK.

**SINK exemptions (SINK 6 and 6 a §§).** Pay from an employer other than the Swedish state, a municipality or a region is exempt where the person is in Sweden no more than 183 days in a 12-month period, the employer is not resident here, and the pay is not borne by a Swedish permanent establishment. This does not apply to hired-out labour, except work of up to 15 days in a row and 45 days a year. On a temporary employment in Sweden, employer reimbursement of travel to Sweden at the start and home at the end, and of lodging while working here, is also exempt, as is income a treaty exempts.

**Choosing IL instead of SINK (SINK 4 §).** A non-resident can ask to be taxed under IL for the year. They then pay the average municipal rate (32.38% for 2026) and state tax. If at least 90% of their earned income for the year comes from Sweden, they get the basic deduction and the job tax credit. ([Skatteverket: belopp och procent 2026](https://www.skatteverket.se/privat/skatter/beloppochprocent/2026.4.1522bf3f19aea8075ba21.html)) How those are computed is in [se-employee-income-tax](se-employee-income-tax.md).

**The ten-year rule (3 kap. 19 § IL).** A limited taxpayer is taxed on a gain on shares and similar rights (delägarrätter, 48 kap. 2 § IL) and on interests in Swedish partnerships, if they lived in Sweden or stayed here on a lasting basis at any time in the calendar year of the sale or the ten calendar years before. Units in investment funds and special funds are outside the rule, and so are shares held in an investment savings account (ISK), with narrow exceptions set out in 3 kap. 19 §. Foreign company shares are caught only if acquired while the person was unlimited taxable. A tax treaty can limit or remove the right to tax.

**Expert tax relief (11 kap. 22-23 a §§ IL).** For work that is specialist, qualified research and development, or a key management role that is hard to recruit for in Sweden, the person does not take up:

- 25% of pay, fees and benefits from the work; and
- employer reimbursement of moving to and from Sweden, up to two trips a year per person between Sweden and the former home country, and children's school fees (compulsory and upper secondary).

Conditions: the employer is Swedish or a foreign company with a permanent establishment here; the employee is not a Swedish citizen; they were not resident or on a lasting stay in Sweden in the five calendar years before the year work starts; and the stay is meant to last at most seven years. If pay for the work in Sweden is more than 1.5 times the price base amount a month (2026: at least SEK 88,801), the conditions on the work are treated as met. Bonuses and other pay not set as a monthly amount do not count towards the floor. The relief runs for at most seven years from the start of the stay. Forskarskattenämnden (the Taxation of Research Workers Board) decides eligibility. Employer social contributions are also charged on 75% of pay only. ([Forskarskattenämnden: about tax relief](https://forskarskattenamnden.se/andra-sprak/taxation-of-research-workers-board/about-tax-relief); [conditions](https://forskarskattenamnden.se/andra-sprak/taxation-of-research-workers-board/conditions-for-tax-relief))

**Company exit taxation (22 kap. 5 and 7 §§ IL).** Withdrawal taxation (uttagsbeskattning) treats assets as sold at market value when, among other cases, tax liability for the income of a business stops in full or in part (5 § 2), or a treaty means the income is no longer taxed in Sweden (5 § 4), or assets move to a part of the business a treaty exempts (5 § 5). This catches a company that moves its registered seat abroad, and a permanent establishment that moves assets or its business abroad. The gain is taxed at 20.6%.

**Foreign companies' dividends (kupongskattelagen 4 §).** Kupongskatt does not apply to an EU company holding 10% or more under the Parent-Subsidiary Directive, or to a foreign company equivalent to a Swedish company receiving dividends on business-related shares (näringsbetingade andelar, held at least one year at the time of payment). It also does not apply to dividends that belong to a Swedish permanent establishment.

## Deadlines and filing

- **Arrival, population register:** a person who can be expected to spend their daily rest in Sweden regularly for at least one year must be registered (folkbokföringslagen 1991:481, 3 §).
- **Arrival, work of six months or more without registration:** the person files a notification for preliminary A tax instead of a SINK application. ([Skatteverket: SINK](https://www.skatteverket.se/privat/internationellt/bosattutomlands/sinksarskildinkomstskattforutomlandsbosatta.4.6fdde64a12cc4eee23080002583.html))
- **SINK:** apply through Skatteverket's e-service (an email address is enough) or form SKV 4350, or the employer applies. A new application is needed for each income year and each new employer or period; Skatteverket handles applications for the next year from December at the earliest. A person with a SINK decision does not file an income tax return for that income. Without a decision, the payer withholds ordinary preliminary tax.
- **Expert tax relief:** the application (forms FSN 1220 or FSN 1226) must reach Forskarskattenämnden within three months after work in Sweden starts. A late application is rejected, even by one day. Either the employee or the employer may apply. A change of employer needs a new application. ([Forskarskattenämnden: apply](https://forskarskattenamnden.se/andra-sprak/taxation-of-research-workers-board/apply-for-tax-relief))
- **Departure, population register:** a registered person who will live abroad for a year or more notifies Skatteverket of the move, at least one week before, through the e-service or form SKV 7665. ([Skatteverket: moving away from Sweden](https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/individualsandemployees/movingfromsweden/movingawayfromsweden.4.6bef7d451695d90def41857.html)) Leaving the register does not end tax liability by itself.
- **Income tax return (individuals, including limited taxpayers with Swedish income outside SINK):** by 2 May the year after the income year (SFL 32 kap. 1 §). When 2 May is a Saturday, Sunday or public holiday the return can be filed on the next weekday (Lag 1930:173, 2 §), so for income year 2026 the date is Monday 3 May 2027. An unlimited taxpayer reports all income, Swedish and foreign.
- **Company exit tax:** the gain is reported in the company's income return for the year of the exit. That return is due by 1 July after a financial year ending 31 December, 1 November after one ending 30 April, 15 December after one ending 30 June, and 1 March after one ending 31 August; a return filed electronically may come in one month later (SFL 32 kap. 2 §). See [se-corporate-tax](se-corporate-tax.md). The payment deferral (anstånd) is granted only on application (SFL 63 kap. 2 §); see Penalties and interest and Cross-border points for how it runs.

## Penalties and interest

([Skatteverket: belopp och procent 2026](https://www.skatteverket.se/privat/skatter/beloppochprocent/2026.4.1522bf3f19aea8075ba21.html))

- **Late income tax return (förseningsavgift):** each fee is SEK 1,250 for individuals and others, and SEK 6,250 for aktiebolag and economic associations (SFL 48 kap. 6 §). A second fee of the same amount is charged if the return is still missing three months after the deadline, and a third after two more months (SFL 48 kap. 7 §). So an individual pays SEK 1,250, then SEK 2,500 in total, then SEK 3,750 in total; a company SEK 6,250, SEK 12,500 and SEK 18,750 in total.
- **Tax surcharge (skattetillägg) for an incorrect statement:** 40% of the tax that would have been withheld on final tax; 20% on other taxes (for example VAT and employer contributions); 10% for a timing error on final tax (5% or 2% on other taxes). The same 40% and 20% apply on a discretionary assessment. Where tax should have been withheld and was not, the surcharge is 5% of the amount that should have been withheld.
- **Interest on the tax account (kostnadsränta):** both rates follow the base rate (basränta), which is 125% of the six-month Treasury bill rate with a floor of 1.25% (SFL 65 kap. 3 §). The low rate equals the base rate (65 kap. 4 §); the high rate is the base rate plus 15 percentage points (65 kap. 13 §). The base rate has been 2.5% since 1 December 2024, so the low rate is 2.5% and the high rate 17.5%; Skatteverket still showed these as current on 22 October 2026. The low rate applies to deferred tax (anstånd) and to final tax up to the due date; the high rate to amounts unpaid after the due date. The interest is not deductible. ([Skatteverket: ränta på skattekontot](https://www.skatteverket.se/privat/skatter/skattekontobetalaochfatillbaka/rantapaskattekontot.4.18e1b10334ebe8bc80002582.html))
- **Deferred company exit tax:** carries the low cost interest while deferred; on a renewed deferral, interest runs from the day after it is granted (SFL 65 kap. 7 §). Skatteverket may withdraw or reduce the deferral if circumstances change materially (SFL 63 kap. 22 §).

## Cross-border points

**Treaty tie-breaker.** Where a person is unlimited taxable in Sweden and resident in a treaty state, the treaty decides which state is the residence state, and Skatteverket says residence under the treaty decides where most income is taxed. An unlimited taxpayer still reports all income to Skatteverket, even income a treaty exempts. ([Skatteverket: har du flyttat från Sverige?](https://www.skatteverket.se/privat/internationellt/bosattutomlands/harduflyttatfransverige.4.7459477810df5bccdd4800030036.html))

**Double tax relief.** Sweden gives a credit for foreign tax against Swedish state and municipal tax under the Act on Credit for Foreign Tax (lag 1986:468 om avräkning av utländsk skatt). Treaties can also exempt income outright. Pay for work abroad of six months or more can be exempt under the six-month rule or the one-year rule (3 kap. 9-10 §§ IL).

**Company exit deferral (SFL 63 kap. 14 and 17 §§).** Where the exit taxation arises only under 22 kap. 5 § 2, 4 or 5 IL, and the assets or business move to an EEA state that is in the EU or has a debt-recovery assistance agreement with Sweden, Skatteverket grants deferral of the tax on application. Each deferral runs for one year and can be renewed. The maximum deferred amount falls by one fifth each year, so the tax is paid over five years. The deferral cannot exceed the tax on the assets still in the business, so a sale of an asset brings its share of the tax forward.

**Kupongskatt and treaties.** Kupongskatt at 30% is withheld at payment. For a company whose shares are registered with a central securities depository (avstämningsbolag), the depository withholds unless the information it holds shows the recipient is not liable (7 §). For other companies, the payer withholds unless the recipient's declaration shows plainly that they are not liable. Where more was withheld than a treaty allows, or from someone not liable, Skatteverket refunds the excess on application (27 §). The rules are in [kupongskattelagen](https://data.riksdagen.se/dokument/sfs-1970-624.text).

**EU social security.** Under Regulation (EC) 883/2004, a person is covered by one country's social security at a time. An employee posted from Sweden to another EU or EEA state, Switzerland or the UK stays in Swedish social insurance for up to 24 months if they were covered in Sweden at least one month before, do not replace another posted worker, and the employer keeps its business in Sweden. The employer and employee notify Försäkringskassan before the work starts, and Försäkringskassan issues certificate A1 (forms 6220 and 6221). An extension to 24 months must be applied for before the first period ends; after a posting ends, a new posting to the same country needs a two-month gap. Someone living in Sweden and working in two or more states is covered where they live if they do at least 25% of their work (or earn 25% of pay) there. ([Försäkringskassan: employee who will work abroad](https://www.forsakringskassan.se/english/for-employers/employee-who-will-work-abroad); [Försäkringskassan: jobba i flera länder](https://www.forsakringskassan.se/privatperson/flytta-jobba-studera-eller-fa-vard-utomlands/jobba-utomlands/jobba-i-flera-lander-inom-eu-ees-eller-i-schweiz-och-storbritannien))

**Other skills.** Withholding on pay, SINK decisions in payroll and A1 records are in [sweden-payroll](sweden-payroll.md). Gains on Swedish property and shares are in [se-capital-gains](se-capital-gains.md). Self-employed contributions are in [se-social-contributions](se-social-contributions.md). Company exit and the corporate return are in [se-corporate-tax](se-corporate-tax.md).

## Worked examples

### Example 1: an expert moves to Stockholm in 2026

Lena is a German software architect with no earlier link to Sweden. A Swedish company hires her from 1 February 2026 for four years at SEK 100,000 a month. She had no job in January. Her pay is above the SEK 88,801 floor, so Forskarskattenämnden grants the expert relief on an application made within three months of her start. She becomes resident in February. She earns SEK 1,100,000 from the Swedish job in 2026 and has no other income. She is under 66.

- Exempt part: 25% of 1,100,000 = SEK 275,000.
- Taxable pay: SEK 825,000. She is unlimited taxable for only part of 2026, but all her earned income is Swedish, so the full-year basic deduction applies (63 kap. 4 § second paragraph IL): SEK 17,400 at this level. Taxable earned income: SEK 807,600.
- State income tax: 20% of (807,600 minus 643,000) = SEK 32,920.
- Municipal tax at the 2026 average rate of 32.38%: SEK 261,500.88. Her actual municipality's rate applies, and the job tax credit and other credits come off; see [se-employee-income-tax](se-employee-income-tax.md).
- Without the relief, taxable earned income would be SEK 1,082,600 and state tax SEK 87,920. The relief cuts state tax by SEK 55,000 and the municipal tax base by SEK 275,000.
- Had she earned substantial pay abroad in January, her basic deduction would instead be one twelfth of 0.293 price base amount for each month of unlimited liability (63 kap. 4 § first paragraph IL), and the foreign pay itself would be outside Swedish tax.

```oa-check
name: Expert relief, SEK 100,000 a month from 1 February 2026
inputs:
  pay: 1100000
  relief_rate: 0.25
  basic_deduction: 17400
  skiktgrans: 643000
  municipal_rate: 0.3238
steps:
  - exempt: pay * relief_rate
  - taxable_pay: pay - exempt
  - taxable_earned: taxable_pay - basic_deduction
  - state_tax: max(taxable_earned - skiktgrans, 0) * 0.20
  - municipal_tax: taxable_earned * municipal_rate
  - state_tax_without_relief: max(pay - basic_deduction - skiktgrans, 0) * 0.20
  - state_tax_saved: state_tax_without_relief - state_tax
expected:
  exempt: 275000.00
  taxable_earned: 807600.00
  state_tax: 32920.00
  municipal_tax: 261500.88
  state_tax_without_relief: 87920.00
  state_tax_saved: 55000.00
```

### Example 2: a non-resident works four months in Sweden under SINK

Tomasz lives in Poland and keeps his home and family there. A Swedish company employs him on a project in Gothenburg from March to June 2026 at SEK 60,000 a month. He stays in Sweden for four months, so he has no lasting stay and is limited taxable. The employer is Swedish, so the 183-day exemption does not apply. Skatteverket issues a SINK decision. The employer also pays his flight to Sweden in March, his flight home in June and his lodging, which are exempt under SINK 6 § 1.

- Taxable pay: 4 x 60,000 = SEK 240,000.
- SINK at 22.5%: SEK 54,000, withheld by the employer. He files no Swedish return for this pay.
- The same pay received in 2027 would bear SINK at 20%: SEK 48,000.
- Whether Poland also taxes the pay, and gives a credit, follows the Sweden-Poland treaty and Polish law.

```oa-check
name: SINK 2026, four months at SEK 60,000
inputs:
  monthly_pay: 60000
  months: 4
  sink_2026: 0.225
  sink_2027: 0.20
steps:
  - pay: monthly_pay * months
  - sink_tax: pay * sink_2026
  - sink_tax_if_2027: pay * sink_2027
expected:
  pay: 240000.00
  sink_tax: 54000.00
  sink_tax_if_2027: 48000.00
```

## Ask the client first

1. Dates in and out of Sweden, where they sleep, and whether any stay in Sweden lasts six months in a row.
2. Citizenship, and how long they lived in Sweden before leaving (ten years or citizenship triggers the five-year presumption).
3. What ties remain in Sweden after leaving: a year-round home, spouse or children under 18, a business, significant shareholdings, real property.
4. For an arrival: who employs them, the contracted monthly pay, the start date (the three-month expert relief deadline runs from it), and whether they lived in Sweden in the five calendar years before.
5. For someone leaving: shares or partnership interests they hold and may sell within ten years, and the treaty with the new country.
6. For a company: where it is registered, and whether it will move its seat, a branch, or assets out of Sweden, and to which state.

## Sources

Read on 2026-10-22:

- Inkomstskattelag (1999:1229), as amended to SFS 2026:1393 (3 kap. 3-23 §§, 6 kap. 3-18 §§, 6 a kap., 11 kap. 22-23 a §§, 22 kap. 5 and 7 §§, 63 kap. 3-4 §§, 65 kap. 10 §): https://data.riksdagen.se/dokument/sfs-1999-1229.text
- Lag (1991:586) om särskild inkomstskatt för utomlands bosatta, as amended to SFS 2025:1356 (4, 5, 6, 6 a, 6 b and 7 §§, and the transitional rules of 2025:1355 and 2025:1356): https://data.riksdagen.se/dokument/sfs-1991-586.text
- Kupongskattelag (1970:624): https://data.riksdagen.se/dokument/sfs-1970-624.text
- Skatteförfarandelag (2011:1244), as amended to SFS 2026:1305 (32 kap. 1-2 §§, 48 kap. 6-7 §§ (read 2026-10-23), 63 kap. 2, 14, 17 and 22 §§, 65 kap. 3, 4, 7 and 13 §§): https://data.riksdagen.se/dokument/sfs-2011-1244.text
- Lag (1986:468) om avräkning av utländsk skatt: https://data.riksdagen.se/dokument/sfs-1986-468.text
- Folkbokföringslag (1991:481), 3 §: https://data.riksdagen.se/dokument/sfs-1991-481.text
- Lag (1930:173) om beräkning av lagstadgad tid, 2 § (read 2026-10-23): https://data.riksdagen.se/dokument/sfs-1930-173.text
- Skatteverket, belopp och procent inkomstår 2026: https://www.skatteverket.se/privat/skatter/beloppochprocent/2026.4.1522bf3f19aea8075ba21.html
- Skatteverket, skattskyldighet: https://www.skatteverket.se/privat/skatter/arbeteochinkomst/sabeskattasdinlon/skattskyldighet.4.65fc817e1077c25b8328000206.html
- Skatteverket, har du flyttat från Sverige?: https://www.skatteverket.se/privat/internationellt/bosattutomlands/harduflyttatfransverige.4.7459477810df5bccdd4800030036.html
- Skatteverket, moving away from Sweden: https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/individualsandemployees/movingfromsweden/movingawayfromsweden.4.6bef7d451695d90def41857.html
- Skatteverket, SINK: https://www.skatteverket.se/privat/internationellt/bosattutomlands/sinksarskildinkomstskattforutomlandsbosatta.4.6fdde64a12cc4eee23080002583.html
- Skatteverket, ränta på skattekontot: https://www.skatteverket.se/privat/skatter/skattekontobetalaochfatillbaka/rantapaskattekontot.4.18e1b10334ebe8bc80002582.html
- Forskarskattenämnden, about tax relief: https://forskarskattenamnden.se/andra-sprak/taxation-of-research-workers-board/about-tax-relief
- Forskarskattenämnden, conditions for tax relief: https://forskarskattenamnden.se/andra-sprak/taxation-of-research-workers-board/conditions-for-tax-relief
- Forskarskattenämnden, remuneration rate: https://forskarskattenamnden.se/andra-sprak/taxation-of-research-workers-board/conditions-for-tax-relief/remuneration-rate
- Forskarskattenämnden, apply for tax relief: https://forskarskattenamnden.se/andra-sprak/taxation-of-research-workers-board/apply-for-tax-relief
- Försäkringskassan, employee who will work abroad: https://www.forsakringskassan.se/english/for-employers/employee-who-will-work-abroad
- Försäkringskassan, jobba i flera länder inom EU/EES eller i Schweiz och Storbritannien: https://www.forsakringskassan.se/privatperson/flytta-jobba-studera-eller-fa-vard-utomlands/jobba-utomlands/jobba-i-flera-lander-inom-eu-ees-eller-i-schweiz-och-storbritannien

Not yet confirmed: treaty rates on dividends for specific countries (read the treaty); the treaty tie-breaker order, which is the OECD model wording and must be read in each treaty; the events that end a company exit deferral beyond SFL 63 kap. 17 and 22 §§.

> Contributed by Ryan Duguid.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-10-23. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `se-cross-border` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/se-cross-border. If neither is available, confirm every figure against the official source pages cited above before relying on it.
