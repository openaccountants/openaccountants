---
name: se-benefits-and-allowances
description: "Swedish taxable employee benefits (förmåner) and tax-free travel allowances, income year 2026. Covers valuation under Inkomstskattelagen 61 kap.: car benefit (0.29 price base amount + interest part + 13% of new-car price + vehicle tax, environmental-car reductions, 3,000-mil and part-year rules), fuel benefit (market value x 1.2; market value for contributions), meal benefit (SEK 62 / 124 / 310), housing; tax-free items (friskvårdsbidrag up to SEK 5,000, gifts SEK 600 / 1,800 / 15,000, bicycle, workplace charging); per diem (traktamente SEK 300 a day, meal reductions) and mileage (SEK 25 / 12 / 9.50 a mil); reporting in the arbetsgivardeklaration and employer contributions. Trigger on: förmånsvärde, bilförmån, kostförmån, traktamente, milersättning, friskvårdsbidrag, julgåva, company car Sweden. Out of scope: the payroll run and withholding tables (sweden-payroll), the employee's annual return (se-employee-income-tax), self-employed (se-income-tax)."
version: 0.1
jurisdiction: SE
tax_year: 2026
last_updated: 2026-10-23
authored_by: Ryan Duguid
review_status: pending_review
trust_label: Accountant-authored
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Sweden: taxable benefits and tax-free travel allowances, income year 2026

> **General reference only.** A source-cited draft, not reviewed by an accountant. Do not rely on it to file, pay or take a tax position without review by a qualified professional in Sweden.

This skill values non-cash benefits and travel allowances that an employer gives an employee in Sweden. It picks up where `sweden-payroll` stops: that skill runs the monthly payroll and the arbetsgivardeklaration (AGI) but does not put a value on a benefit. The law is Inkomstskattelagen (1999:1229), "IL" below (11 kap. what is taxed, 12 kap. travel deductions, 61 kap. valuation), Socialavgiftslagen (2000:980), "SAL" below, and Skatteförfarandelagen (2011:1244), "SFL" below. All three were read on 2026-10-23 in the consolidated text on data.riksdagen.se (IL to SFS 2026:1393, SAL to SFS 2026:493, SFL to SFS 2026:1305). The 2026 figures come from Skatteverket's "Belopp och procent inkomstår 2026". Amounts are in Swedish kronor (SEK). One Swedish mil is 10 km.

See also, in this pack: `sweden-payroll` (registration, withholding tables, the 31.42% rate and its reduced rates, AGI deadlines, late-filing fees, corrections), `se-employee-income-tax` (how the employee's earned income, including benefits, is taxed in the annual return), `se-income-tax` (sole traders), `se-cross-border` (non-residents, SINK, treaties). This skill does not repeat them.

## Who this applies to

- Any employer, Swedish or foreign, that pays remuneration for work taxed in Sweden and gives the employee something other than cash, or pays a per diem or mileage allowance. The rules apply equally to company directors and to owners of a closely held company who take benefits from it.
- A benefit received "på grund av tjänst" is employment income, valued at market value unless 61 kap. sets a standard value (IL 11 kap. 1 §, 61 kap. 2 §).
- The employer values the benefit, withholds tax on it from cash pay, reports it in the AGI and pays employer contributions on it. The employee is then taxed on it in the annual return as earned income.
- Out: benefits to a self-employed person from their own business (see `se-income-tax`), and the person's own deduction claims for travel the employer did not pay (see `se-employee-income-tax`).

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Price base amount (prisbasbelopp, PBB) | SEK 59,200 | 2026 | https://www.skatteverket.se/privat/skatter/beloppochprocent/2026.4.1522bf3f19aea8075ba21.html |
| Raised price base amount | SEK 60,500 | 2026 | same |
| Car benefit, fixed part | 0.29 x PBB = SEK 17,168 a year | 2026 | IL 61 kap. 5 §; Skatteverket 2026 page |
| Car benefit, interest part | new-car price x (70% of statslåneränta + 0.01); floor on the rate 0.5% | 2026 | IL 61 kap. 5 § |
| Statslåneränta at 30 November 2025 | 2.55%, so the interest factor is 2.785% | 2026 | https://www.riksgalden.se/press-och-publicerat/pressmeddelanden-och-nyheter/nyheter/20252/statslanerantan-per-den-30-november-2025/ |
| Car benefit, price part | 13% of the new-car price | 2026 | IL 61 kap. 5 § |
| Car benefit, vehicle tax | the car's annual fordonsskatt is added | 2026 | IL 61 kap. 5 § |
| Environmental-car price reduction | electric or hydrogen SEK 350,000; plug-in hybrid SEK 140,000; gas (not LPG) SEK 100,000; never more than 50% of the new-car price | 2026 | IL 61 kap. 8 a § |
| Car six years old or more | new-car price is at least 4 x PBB | 2026 | IL 61 kap. 7 § |
| High business mileage | 75% of the value if at least 3,000 mil driven in service in the year | 2026 | IL 61 kap. 9 § |
| Fuel benefit | market value x 1.2 for tax; market value for employer contributions | 2026 | IL 61 kap. 10 §; SAL 2 kap. 10 a § |
| Meal benefit (kostförmån) | breakfast SEK 62; lunch or dinner SEK 124; full day (at least three meals) SEK 310 | 2026 | IL 61 kap. 3 §; Skatteverket 2026 page |
| Housing benefit | market value for tax; for contributions, Skatteverket's per-m² table (Storstockholm SEK 1,744 a year; outside urban areas SEK 1,189 a year) | 2026 | IL 61 kap. 2 §; SAL 2 kap. 10 a §; Skatteverket 2026 page |
| Wellness allowance (friskvårdsbidrag) | tax-free up to SEK 5,000 a year, same terms for all staff; above that, all of it is taxable | 2026 | IL 11 kap. 11-12 §§; https://www.skatteverket.se/foretag/arbetsgivare/lonochersattning/formaner/personalvardsformanmotionochfriskvard.4.3016b5d91791bf546791431.html |
| Christmas gift / jubilee gift / memorial gift | SEK 600 / SEK 1,800 / SEK 15,000, including VAT; above the limit, all of it is taxable; never cash | 2026 | IL 11 kap. 14 §; Skatteverket 2026 page |
| Bicycle for private use | taxable only above SEK 3,000 a year, offer must go to all permanent staff | 2026 | IL 11 kap. 12 a § |
| Charging at the workplace | tax-free (not if the workplace is the employee's home) | 2026 | IL 11 kap. 12 b § |
| Per diem, domestic (maximibelopp) | SEK 300 full day; SEK 150 half day; SEK 150 night allowance | 2026 | IL 12 kap. 10-11 §§; Skatteverket 2026 page |
| Per diem after three months at the same place | SEK 210 a full day (70%); after two years SEK 150 (50%) | 2026 | IL 12 kap. 6 § second paragraph and 21 §; https://www.skatteverket.se/foretag/arbetsgivare/lonochersattning/traktamenteochbilersattning.4.361dc8c15312eff6fd1703e.html |
| Meal reduction of a SEK 300 full day | all three meals SEK 270; lunch and dinner SEK 210; lunch or dinner SEK 105; breakfast SEK 60 | 2026 | IL 12 kap. 17 §; Skatteverket traktamente page |
| Mileage, own car | SEK 25 a mil (SEK 2.50 a km) | 2026 | IL 12 kap. 5 § |
| Mileage, benefit car, employee pays all fuel | SEK 12 a mil; fully electric SEK 9.50 a mil | 2026 | IL 12 kap. 5 § |
| Employer contributions on benefits | 31.42% ordinary full rate: 18.80% arbetsgivaravgifter plus 12.62% allmän löneavgift (reduced rates in `sweden-payroll`) | 2026 | SAL 2 kap. 10 and 26 §§; Lag (1994:1920) om allmän löneavgift 3 §; Skatteverket 2026 page |

## The taxable base

**General rule.** Everything received because of the job is taxable unless 11 kap. exempts it (IL 11 kap. 1 §). A benefit is valued at market value: what the employee would have paid locally in cash for the same thing (IL 61 kap. 2 §). Any amount the employee pays for the benefit out of taxed pay reduces the value (61 kap. 4 and 11 §§). For employer contributions the same values apply, except housing (table value) and fuel (market value without the 1.2 uplift) (SAL 2 kap. 10 a §).

**Car benefit (bilförmån).** The yearly value of a car the employee may use privately is the sum of four parts (IL 61 kap. 5 §):

1. 0.29 x PBB, SEK 17,168 for 2026;
2. the interest part: new-car price x (0.70 x statslåneränta at the end of November 2025 + 0.01). With 2.55%, the factor is 0.02785;
3. the price part: 13% of the new-car price;
4. the car's annual vehicle tax.

The new-car price is the price of that model when it came onto the Swedish market, plus any extra equipment (alcolocks excluded) (6 and 8 §§). For an electric, hydrogen, plug-in hybrid or gas car, cut the price by the 8 a § amount before parts 2 and 3, capped at half the price. For a car six or more years old, use at least 4 x PBB (7 §). Take 75% of the value if the employee drove at least 3,000 mil in service in the year (9 §). Reduce by one twelfth for each whole calendar month without the car (9 §). Use only "ringa omfattning" (very occasional private use) gives a value of nil (11 §). Road, bridge and ferry charges and congestion tax are outside the car benefit (5 a §), so an employer that pays them for private trips gives a separate benefit. Skatteverket can adjust a value only on "synnerliga skäl" (18-19 §§); for contributions the employer must apply for that decision (SAL 2 kap. 10 b §). **Which cars this formula covers.** The four-part formula applies to a car that first became liable to Swedish vehicle tax on or after 1 July 2021, and to a car registered abroad (SFS 2021:479, transitional point 2). It has no extra charge on the price above 7.5 PBB. A car first liable to vehicle tax before 1 July 2021 keeps the older rules (SFS 2021:479, transitional point 3), which this skill does not reproduce. The 8 a § reductions in the amounts above apply to cars first liable to vehicle tax after 30 June 2022 (SFS 2022:479, transitional points 2 and 3); a car first taxed between 1 July 2021 and 30 June 2022 keeps the 8 a § wording in force before then, which is not reproduced here. Skatteverket's 2026 car benefit example states the same scope.

**Fuel benefit (drivmedelsförmån).** If the employer pays fuel for private driving in a benefit car, the benefit is market value x 1.2 of the fuel used. The statute starts from the fuel for the car's total distance and reduces it when the employee shows that private use was lower (IL 61 kap. 10 §); in practice Skatteverket splits the fuel bill by private and total mil from the driving log. Employer contributions are on market value only (SAL 2 kap. 10 a §). In the AGI, enter the x 1.2 amount in box 018, and anything the employee paid for the fuel by net pay deduction in box 098; Skatteverket works out the contribution base. A fuel benefit is reported for the month after the month the car was filled or charged. Fuel paid for an employee's own private car is not uplifted: it is market value, in box 012.

**Meals (kostförmån).** A free meal is a benefit at the standard values above: a full day is 0.52% of PBB rounded to the nearest five kronor (SEK 310), lunch or dinner 40% of that (SEK 124), breakfast 20% (SEK 62) (IL 61 kap. 3 §). If the employee pays part, the benefit is the difference. Not taxed: meals included by obligation in a travel ticket, hotel breakfast included in the room price, external representation, and short internal events such as a staff party (11 kap. 2 §).

**Housing (bostadsförmån).** Market value for income tax (61 kap. 2 §). For employer contributions on a home in Sweden (not a holiday home), Skatteverket's area table per m² applies (SAL 2 kap. 10 a §). In the AGI the value goes in box 012, with a tick in box 041 (one- or two-family house) or 043 (other housing).

**Tax-free items.** Simple exercise and wellness offered to all staff (11 kap. 11-12 §§), with Skatteverket's limit of SEK 5,000 a year for a cash friskvårdsbidrag paid against a receipt; a bicycle up to SEK 3,000 (12 a §); workplace charging (12 b §); occupational health care and work-related vaccinations (18 §); group life cover on state terms (19 §); Christmas, jubilee and memorial gifts within the limits (14 §); staff discounts within the normal range (13 §). A cash gift is always taxable. A benefit the employee can swap for cash is not a tax-free personnel benefit (11 §).

**Per diem (traktamente).** A per diem is tax-free, and free of employer contributions, up to the standard amounts only if the trip involves an overnight stay more than 50 km from both the usual workplace and home (IL 12 kap. 6-7 §§). The departure day is a full day if the trip starts before 12:00 and a half day if it starts at 12:00 or later; the return day is a full day if the trip ends after 19:00 and a half day if it ends at 19:00 or earlier; days in between are full days (10 §). Free meals during the trip reduce the tax-free amount by the reduction amounts in the table (17 §). Hotel breakfast and representation reduce the per diem but are not a taxable benefit; meals in a transport ticket do neither; other free meals both reduce the per diem and are taxed as kostförmån. After three months at the same place the full-day amount falls to 70%, after two years to 50% (12 kap. 6 § second paragraph and 21 §). Lodging is reimbursed tax-free at actual cost; without a receipt the night allowance is SEK 150.

**Mileage (bilersättning).** Reimbursement for business driving is tax-free up to SEK 25 a mil in the employee's own car. In a benefit car it is tax-free up to SEK 12 a mil (SEK 9.50 for a fully electric car) only if the employee paid all the fuel (IL 12 kap. 5 §). From 1 July 2026 a plug-in hybrid still qualifies when it was charged at the workplace (SFS 2026:464).

**The excess.** The part of a per diem or mileage payment above the standard amount is pay: withhold tax on it and charge employer contributions (SFL 10 kap. 3 § second paragraph points 8-9; SAL 2 kap. 11 § 1). The tax-free part is never taxed and never carries contributions (SAL 2 kap. 12 §).

## Deadlines and filing

- **When to report.** A benefit is reported in the AGI for the month the employee could use it. A January benefit goes in the January return. If the employer does not know the value when pay is run (for example, it learns of the benefit only from a travel expense claim), reporting may be put back one, at most two, months; Skatteverket says this is for particular cases and not a general practice.
- **Where.** Individual statement (individuppgift): box 012 other taxable benefits (meals, housing, phone and so on); box 013 car benefit excluding fuel, one twelfth a month (a part month counts as a whole month); box 018 fuel benefit at x 1.2; box 098 what the employee paid for fuel by net deduction; box 048 if Skatteverket has adjusted a value. Tax-free per diem and mileage are reported only by a tick in box 051 (per diem) and box 050 (mileage). Any excess goes in box 011 as cash pay.
- **Withholding.** Tax on a benefit is withheld from the same month's cash pay, using the table on cash pay plus benefit value. Box 001 shows the tax withheld.
- **Filing and payment dates, corrections.** As for every AGI: see `sweden-payroll` (12th of the following month for most employers, 17 August and 17 January for July and December; an employer whose VAT taxable base for the year is expected to exceed SEK 40 million files by the 26th but still pays by the 12th, 17th in January) (SFL 26 kap. 26 and 30 §§; 62 kap. 3 §).
- **Records.** Keep the travel expense report (dates, times, destination, purpose, meals received) for every tax-free per diem and the driving log for every tax-free mileage payment. These records are the evidence that the conditions in IL 12 kap. were met.

## Penalties and interest

- **Late AGI.** Late-filing fee SEK 625, or SEK 1,250 after an order: see `sweden-payroll`.
- **Wrong or missing benefit value.** Skattetillägg is 20% of the employer contributions that would have gone unpaid because of an incorrect AGI (SFL 49 kap. 11 §, "annan skatt"). It is not charged if the employer corrects the error on its own initiative, or if the amount is insignificant (SFL 49 kap. 10 §). A correction linked to a general check that Skatteverket has announced does not count as on the employer's own initiative if it is made more than two months after the end of the month of that announcement.
- **Tax not withheld.** Skatteverket can make the employer pay the tax that should have been withheld on a benefit or a taxable excess allowance (SFL 59 kap. 2 §). The employee is also taxed in the annual return.
- **Interest.** Unpaid amounts on the tax account carry kostnadsränta; the rate is set from the base rate (see `se-corporate-tax` and `sweden-payroll`).
- **Over-the-limit gifts and wellness money.** Not a penalty, but a cliff: a Christmas gift of SEK 601 or a friskvårdsbidrag of SEK 5,001 is taxable in full, with employer contributions on the whole amount.

## Cross-border points

- **Trips abroad.** The tax-free per diem is the normalbelopp for each country, published by Skatteverket each year; free meals reduce it by percentages (85% for all meals, 70% lunch and dinner, 35% lunch or dinner, 15% breakfast). Where the employee is in more than one country in a day, the country where most of 06:00-24:00 was spent decides (IL 12 kap. 12 §). The country amounts are not reproduced here.
- **Non-resident employees.** SINK covers "lön eller därmed jämförlig förmån", so a non-resident taxed under SINK is taxed on benefits too (SINK 5 §). Rates and the SINK decision: see `se-cross-border`.
- **Foreign employer without a Swedish establishment.** Benefits are still part of the contribution base; the rates and the no-establishment route are in `sweden-payroll`.
- **Social security coverage.** If an A1 or convention certificate puts the employee in another country's system, no Swedish employer contributions are due on the benefit, but Swedish income tax still applies if Sweden has the taxing right.
- **Foreign registered car.** The car benefit uses the Swedish new-car price of the model; if the model was never sold in Sweden, use the price it would have had (IL 61 kap. 6 §).

## Worked examples

**Example 1: car benefit on a SEK 450,000 petrol car, 2026.** Ekdal AB gives its sales manager, born 1985, a new petrol car for the whole of 2026 with free private use. The model's new-car price including extra equipment is SEK 450,000. The registration certificate shows vehicle tax of SEK 5,000 a year (an assumed figure for this example; take the real one from Transportstyrelsen's register). She drives fewer than 3,000 mil in service and pays her own fuel. The yearly benefit is 17,168 (0.29 x 59,200) + 12,532.50 (450,000 x 2.785%) + 58,500 (13% of 450,000) + 5,000 = SEK 93,200.50. Each month Ekdal reports one twelfth, SEK 7,766.71, in box 013, adds it to cash pay for the withholding table, and pays employer contributions of 31.42%: SEK 29,283.60 for the year (SEK 2,440.30 a month). If the same car were fully electric, the new-car price would be cut by SEK 350,000, capped at half the price, so by SEK 225,000. The interest and price parts would then be 6,266.25 and 29,250, and the value before vehicle tax SEK 52,684.25.

```oa-check
name: SE car benefit, SEK 450,000 petrol car, full year 2026
inputs:
  pbb: 59200
  new_car_price: 450000
  statslaneranta_pct: 2.55
  vehicle_tax: 5000
  contribution_rate_pct: 31.42
  ev_reduction_cap: 350000
steps:
  - fixed_part: 0.29 * pbb
  - interest_factor_pct: 0.70 * statslaneranta_pct + 1
  - interest_part: pct(new_car_price, interest_factor_pct)
  - price_part: pct(new_car_price, 13)
  - benefit_year: fixed_part + interest_part + price_part + vehicle_tax
  - benefit_month: round(benefit_year / 12, 2)
  - contributions_year: round(pct(benefit_year, contribution_rate_pct), 2)
  - contributions_month: round(pct(benefit_month, contribution_rate_pct), 2)
  - ev_price: new_car_price - min(ev_reduction_cap, new_car_price / 2)
  - ev_interest_part: pct(ev_price, interest_factor_pct)
  - ev_price_part: pct(ev_price, 13)
  - ev_benefit_before_vehicle_tax: fixed_part + ev_interest_part + ev_price_part
expected:
  fixed_part: 17168
  interest_factor_pct: 2.785
  interest_part: 12532.50
  price_part: 58500
  benefit_year: 93200.50
  benefit_month: 7766.71
  contributions_year: 29283.60
  contributions_month: 2440.30
  ev_price: 225000
  ev_benefit_before_vehicle_tax: 52684.25
```

**Example 2: three-day domestic trip with some meals provided.** An engineer based in Malmö travels to a client in Stockholm (more than 50 km from her workplace and her home). She leaves on Monday at 07:00 and comes home on Wednesday at 20:30, with two nights in a hotel that the employer books and pays. All three days are full days: the trip starts before 12:00 and ends after 19:00. Breakfast is included in the room price on Tuesday and Wednesday. On Tuesday the client's project lunch is paid by her employer; it is not representation. The employer pays a flat SEK 300 a day without making any reduction, SEK 900 in all.

The tax-free maximum is 3 x 300 = 900, less 60 for each hotel breakfast and 105 for the lunch: SEK 675. The other SEK 225 is pay: it goes in box 011, tax is withheld on it, and it carries employer contributions. The hotel breakfasts are not a benefit. The lunch is also a taxable kostförmån of SEK 124 in box 012. Taxable total SEK 349; employer contributions at 31.42% are SEK 109.66. Box 051 is ticked for the tax-free part. Had the employer paid only SEK 675, nothing would be taxable except the SEK 124 lunch benefit.

```oa-check
name: SE domestic per diem, three full days, hotel breakfasts and one paid lunch, 2026
inputs:
  full_days: 3
  per_diem_full_day: 300
  per_diem_paid: 900
  hotel_breakfasts: 2
  reduction_breakfast: 60
  paid_lunches: 1
  reduction_lunch: 105
  meal_benefit_lunch: 124
  contribution_rate_pct: 31.42
steps:
  - max_before_meals: full_days * per_diem_full_day
  - meal_reductions: hotel_breakfasts * reduction_breakfast + paid_lunches * reduction_lunch
  - tax_free: max_before_meals - meal_reductions
  - taxable_excess: max(per_diem_paid - tax_free, 0)
  - kostforman: paid_lunches * meal_benefit_lunch
  - taxable_total: taxable_excess + kostforman
  - contributions: round(pct(taxable_total, contribution_rate_pct), 2)
expected:
  max_before_meals: 900
  meal_reductions: 225
  tax_free: 675
  taxable_excess: 225
  kostforman: 124
  taxable_total: 349
  contributions: 109.66
```

## Ask the client first

1. For a car: the model, year, Swedish new-car price, extra equipment, fuel type, vehicle tax, the months it was available, and the expected service mileage (3,000 mil test).
2. Who pays fuel or charging for private driving, and where the car is charged (workplace, home on the employer's card, public).
3. For each trip: departure and return times, distance from workplace and home, overnight stay, which meals were provided and by whom, and how long the employee has worked at that place.
4. Whether the wellness allowance, gifts and other perks go to all staff on the same terms, and their amounts including VAT.
5. Anything the employee pays towards a benefit, and whether it comes from net pay.
6. Whether the employee is covered by Swedish social security (A1 or convention certificate) and is resident in Sweden.

## Sources

| Source | URL | Read on |
|---|---|---|
| Inkomstskattelag (1999:1229), consolidated to SFS 2026:1393 (11 kap. 1-2, 8, 11-14, 18-19 §§; 12 kap. 5-17 and 21 §§; 61 kap. 2-11, 18-19 §§; transitional provisions SFS 2021:479, 2022:479, 2026:464) | https://data.riksdagen.se/dokument/sfs-1999-1229.text | 2026-10-23 |
| Socialavgiftslag (2000:980), consolidated to SFS 2026:493 (2 kap. 10-12 and 26 §§) | https://data.riksdagen.se/dokument/sfs-2000-980.text | 2026-10-23 |
| Lag (1994:1920) om allmän löneavgift, consolidated to SFS 2025:1360 (3 §, 12.62%) | https://data.riksdagen.se/dokument/sfs-1994-1920.text | 2026-10-23 |
| Skatteförfarandelag (2011:1244), consolidated to SFS 2026:1305 (10 kap. 3 §; 26 kap. 26 and 30 §§; 49 kap. 10-11 §§; 59 kap. 2 §; 62 kap. 3 §) | https://data.riksdagen.se/dokument/sfs-2011-1244.text | 2026-10-23 |
| Lag (1991:586) om särskild inkomstskatt för utomlands bosatta (5 §) | https://data.riksdagen.se/dokument/sfs-1991-586.text | 2026-10-23 |
| Skatteverket: Belopp och procent inkomstår 2026 (PBB, car benefit example, meal values, per diem, reductions, mileage, gifts, housing table, employer contributions) | https://www.skatteverket.se/privat/skatter/beloppochprocent/2026.4.1522bf3f19aea8075ba21.html | 2026-10-23 |
| Riksgälden: Statslåneräntan per den 30 november 2025 (2.55%) | https://www.riksgalden.se/press-och-publicerat/pressmeddelanden-och-nyheter/nyheter/20252/statslanerantan-per-den-30-november-2025/ | 2026-10-23 |
| Skatteverket: Traktamente och bilersättning (for employers) | https://www.skatteverket.se/foretag/arbetsgivare/lonochersattning/traktamenteochbilersattning.4.361dc8c15312eff6fd1703e.html | 2026-10-23 |
| Skatteverket: Personalvårdsförmån, motion och friskvård | https://www.skatteverket.se/foretag/arbetsgivare/lonochersattning/formaner/personalvardsformanmotionochfriskvard.4.3016b5d91791bf546791431.html | 2026-10-23 |
| Skatteverket: Drivmedel vid bilförmån | https://www.skatteverket.se/foretag/arbetsgivare/lonochersattning/formaner/bilforman/drivmedelsforman.4.3016b5d91791bf546791a89.html | 2026-10-23 |
| Skatteverket: Så här fyller du i arbetsgivardeklarationen (reporting period for benefits, deferral of one or two months) | https://www.skatteverket.se/foretag/arbetsgivare/lamnaarbetsgivardeklaration/safyllerduiarbetsgivardeklarationen.4.2cf1b5cd163796a5c8b66a8.html | 2026-10-23 |
| Skatteverket: How to fill in the PAYE tax return, box by box | https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/startingandrunningaswedishbusiness/declaringtaxesbusinesses/filingapayereturn/howtofillinthepayetaxreturnboxbybox.4.309a41aa1672ad0c8379f84.html | 2026-10-23 |

Not yet confirmed: the 2026 normalbelopp per country for trips abroad (not reproduced); Skatteverket's practical test for "ringa omfattning" private use of a car; the car benefit rules for a car first liable to vehicle tax before 1 July 2021, and the 8 a § wording for a car first taxed between 1 July 2021 and 30 June 2022 (only the current consolidated text was read); the vehicle tax in example 1 is an assumed input.

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
