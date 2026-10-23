---
name: nl-company-car
description: "Dutch company car benefit (bijtelling privegebruik auto) in payroll for tax year 2026. Covers when an employer adds private use of a car or van to wage (Wet LB 1964 art. 13bis): the 22% addition on the catalogue value including VAT and BPM, 25% for cars first admitted before 2017, the 2026 zero-emission discount (18% up to EUR 30,000, 22% above), the 60-month rule that fixes the rate in force at first admission, 35% of market value for cars older than 16 years, vans, the 500 km private-use proof (rittenregistratie, Verklaring geen privegebruik), the employee's own contribution (eigen bijdrage), Zvw and employee-insurance effects, and why the werkkostenregeling cannot absorb it. Trigger on: bijtelling, auto van de zaak, company car Netherlands, lease car tax, eigen bijdrage auto, rittenregistratie, bestelauto. Out of scope: general payroll (nl-payroll-tax, netherlands-payroll), entrepreneurs' own cars in box 1 profit (nl-zzp-deductions), VAT on private use (nl-vat-return)."
jurisdiction: NL
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-23
version: 0.1
verified_by: pending
---

# Netherlands: company car benefit (bijtelling) in payroll, 2026 v0.1

This skill is the car method that `nl-payroll-tax` and `netherlands-payroll` refer to. It covers the private-use benefit an employer adds to wages. General payroll steps (tables, credits, the return itself) stay in those two skills.

## Who this applies to

- **Employers (inhoudingsplichtigen) that make a car available to an employee** who may or can use it privately. This includes owned, leased or rented cars, and an employee's own lease car when the employer pays all of its costs. It does not include an employee's own car with only a EUR 0.23 per km business allowance. (Handboek Loonheffingen 2026, par. 23.3)
- **Directors who are employees for wage tax**, including a director-shareholder (DGA) on the BV's payroll. The benefit also feeds the customary-wage test (par. 23.3.22).
- **Cars and vans.** "Auto" means a passenger car or van as defined in the BPM Act art. 3. A van is out of the rule if it is (almost) only fit to carry goods, cannot be used outside working hours, or has a written, supervised and sanctioned ban on private use (Wet LB art. 13bis(5)(a)).
- **Private use is presumed.** The car counts as made available for private use unless it is shown that private use is not more than 500 km in the calendar year (art. 13bis(1)). Commuting (woon-werkverkeer) counts as business use (art. 13bis(3)).
- **Out:** self-employed people and partners with a business car. They use the parallel profit rule in Wet IB 2001 art. 3.20, not this skill. Note that Wet IB 2001 art. 3.145 ("Privé-gebruik auto") was repealed from 1 January 2006; the employee rule sits in Wet LB art. 13bis.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source URL |
|---|---|---|---|
| General addition, first admission on or after 1 Jan 2017 | 22% of catalogue value | 2026 | https://wetten.overheid.nl/BWBR0002471/2026-01-01 (art. 13bis(1)(a)) |
| General addition, first admission before 1 Jan 2017 | 25% of catalogue value | 2026 | https://wetten.overheid.nl/BWBR0002471/2026-01-01 (art. 36c) |
| Car more than 16 years since first use (youngtimer) | 35% of market value | 2026 | https://wetten.overheid.nl/BWBR0002471/2026-01-01 (art. 13bis(1)(b)); https://download.belastingdienst.nl/belastingdienst/docs/handboek-loonheffingen-lh0221t61fd.pdf (par. 23.3.20) |
| Zero-emission discount, first admission 2026 | minus 4% of value, at most EUR 1,200 (so 18% on the first EUR 30,000, 22% above) | 2026 | https://wetten.overheid.nl/BWBR0002471/2026-01-01 (art. 13bis(2)) |
| Zero-emission discount, first admission 2025 | 17% up to EUR 30,000, 22% above | 2026 (60-month lock) | https://download.belastingdienst.nl/belastingdienst/docs/bijlage-nieuwsbrief-loonheffingen-2026-lh2091b64fd.pdf |
| Zero-emission discount, first admission 2023 and 2024 | 16% up to EUR 30,000, 22% above | 2026 (60-month lock) | https://download.belastingdienst.nl/belastingdienst/docs/bijlage-nieuwsbrief-loonheffingen-2026-lh2091b64fd.pdf |
| Zero-emission discount, first admission 2022 | 16% up to EUR 35,000, 22% above | 2026 (60-month lock) | https://download.belastingdienst.nl/belastingdienst/docs/bijlage-nieuwsbrief-loonheffingen-2026-lh2091b64fd.pdf |
| Zero-emission, first admission 2021, inside 60 months | 12% up to EUR 40,000, 22% above; after the 60 months 18% up to EUR 30,000 | 2026 | https://download.belastingdienst.nl/belastingdienst/docs/handboek-loonheffingen-lh0221t61fd.pdf (par. 23.3.4) |
| Zero-emission, first admission 2017 to 2020 (60 months expired) | 18% up to EUR 30,000, 22% above | 2026 | https://download.belastingdienst.nl/belastingdienst/docs/handboek-loonheffingen-lh0221t61fd.pdf (par. 23.3.4) |
| Zero-emission, first admission 2010 to 2016 (rate set by date of first Dutch registration, general rate 25%) | first registration 2026: 21% up to EUR 30,000; 2025: 20% up to EUR 30,000; 2023 and 2024: 19% up to EUR 30,000; 2022: 19% up to EUR 35,000; 2021 inside 60 months: 15% up to EUR 40,000, after: 21% up to EUR 30,000; 2010 to 2020: 21% up to EUR 30,000; 25% above the cap | 2026 | https://download.belastingdienst.nl/belastingdienst/docs/bijlage-nieuwsbrief-loonheffingen-2026-lh2091b64fd.pdf; https://download.belastingdienst.nl/belastingdienst/docs/handboek-loonheffingen-lh0221t61fd.pdf (par. 23.3.4) |
| Zero-emission youngtimer (more than 16 years old) | 35% of market value less the discount for its date of first Dutch registration, for example 31% up to EUR 30,000 for registration in 2026 or before 2020 | 2026 | https://download.belastingdienst.nl/belastingdienst/docs/handboek-loonheffingen-lh0221t61fd.pdf (par. 23.3.4) |
| Hydrogen and qualifying solar-cell cars | discount on the whole value, no EUR 30,000 cap (18% for 2026 admissions) | 2026 | https://wetten.overheid.nl/BWBR0002471/2026-01-01 (art. 13bis(2)) |
| Private-use threshold | 500 km a calendar year | 2026 | https://wetten.overheid.nl/BWBR0002471/2026-01-01 (art. 13bis(1), (3)) |
| Final levy for continuous alternating use of a van | EUR 451 a van a year (EUR 37.58 a month) | 2026 | https://download.belastingdienst.nl/belastingdienst/docs/bijlage-nieuwsbrief-loonheffingen-2026-lh2091b64fd.pdf |
| Employer Zvw levy on the benefit | 6.10% | 2026 | https://download.belastingdienst.nl/belastingdienst/docs/bijlage-nieuwsbrief-loonheffingen-2026-lh2091b64fd.pdf |
| Withheld Zvw contribution (where it applies instead) | 4.85% | 2026 | https://download.belastingdienst.nl/belastingdienst/docs/bijlage-nieuwsbrief-loonheffingen-2026-lh2091b64fd.pdf |
| Maximum premium and Zvw wage | EUR 79,409 a year (EUR 6,617.41 a month) | 2026 | https://download.belastingdienst.nl/belastingdienst/docs/bijlage-nieuwsbrief-loonheffingen-2026-lh2091b64fd.pdf |

## The taxable base

**Step 1. Is there a benefit at all?** No benefit if any of these holds:
- The employee has a closing trip log (rittenregistratie) showing not more than 500 private km in the year (art. 13bis(3); Handboek par. 23.3.18). A trip log records the car (make, type, plate, period available) and each trip (date, number, odometer start and end, departure address, any different route, the business address visited, and whether the trip was private).
- Other evidence under the free-proof rule shows not more than 500 private km (par. 23.3.19).
- The employee gives the employer a copy of a **Verklaring geen privégebruik auto** (art. 13bis(7)). The employer stops the addition from the next pay period. It may not correct periods already paid (par. 23.3.16). If the employer knows the statement is wrong, it must ignore it.
- A van falls outside the rule (goods-only, no use possible outside working hours, or a valid written private-use ban), or the employer files a **Verklaring uitsluitend zakelijk gebruik bestelauto** on the employee's behalf (art. 13bis(13); par. 23.4.7).

A car made available for part of the year: scale private km to a full year before testing the 500 km limit (par. 23.3.10). 200 km in three months is 800 km a year, so the addition applies.

**Step 2. The value (grondslag).** The Dutch catalogue price at the date of first admission, including VAT and BPM, plus factory or dealer accessories fitted before registration (art. 13bis(5)(b); par. 23.3.2). Use the RDW licence-plate check for cars registered from 2005. An imported used car uses the Dutch catalogue price at its first admission anywhere. For a car more than 16 years since first use, the value is the market value (par. 23.3.20). The law text in force still says market value from 15 years (art. 13bis(5)(b)), while the 35% rate starts after 16 years (art. 13bis(1)(b)). The State Secretary told the Senate on 15 January 2026 that this is an omission and will be repaired with retroactive effect from 1 January 2026 (letter ref. 2026-0000011922). The repair was not yet in the law text on 23 October 2026. Follow the Belastingdienst: a car aged 15 to 16 uses its catalogue value.

**Step 3. The percentage.** 22% for first admission on or after 1 January 2017, 25% before that (art. 36c). For a zero-emission car first admitted before 2017, the discount follows the date of first Dutch registration (tenaamstelling), not first admission (par. 23.3.3, 23.3.4). For a zero-emission car, apply the discount for its year of first admission (table above). The 2026 discount is 4% of the value, capped at EUR 1,200. That equals 18% on the first EUR 30,000 and 22% on the rest.

**Step 4. The 60-month rule.** The discount in force at first admission stays fixed for 60 months. The 60 months start on the first day of the month after the month of first admission (art. 13bis(18)). A car first admitted on 7 March 2026 keeps 18% up to EUR 30,000 until 31 March 2031. After that the rules then in force apply. When the period ends during the year, make two calculations: the old rate up to the end month, the new rate after (Handboek par. 23.3.3, example 1).

**Step 5. Annual amount, then per pay period.** Work out the annual value first. Add a time-proportional share to each pay period (1/12 for a monthly period, 1/13 for a four-week period). A car made available mid-month is pro-rated by calendar days (par. 23.3.3, 23.3.10).

**Step 6. Deduct the own contribution (eigen bijdrage).** The benefit counts only to the extent it exceeds what the employee owes for private use (art. 13bis(4)). The contribution must be agreed in advance, be for private use, and be withheld from net pay or paid to the employer (par. 23.3.7). Payments to third parties (car wash) do not count unless agreed as paid on the employer's behalf. A fine for breaking a private-use ban is not a contribution. The yearly net addition may not be negative; a single period may be. The employee cannot deduct the contribution in his income tax return.

**Step 7. Which levies apply.** The net addition is wage in kind. The employer withholds wage tax and national insurance contributions, pays employee-insurance premiums, and pays the employer Zvw levy (or withholds the Zvw contribution where that branch applies) (par. 23.3.1). No pension may be built up on the benefit (par. 23.3.22).

**Step 8. The werkkostenregeling does not apply.** The private-use benefit is always the employee's wage. The employer cannot designate it as final-levy wage in the free space (vrije ruimte). The one exception is the part of the value for extraordinary security measures (Wet LB art. 31(5)(a); Handboek par. 23.3.1). A home charging point paid by the employer and charging at work are covered by the addition and are not extra wage (par. 23.3.9).

**Excessive private use.** If the real value of private use is clearly higher than the percentage result, the higher real value applies, less any zero-emission discount (par. 23.3.3).

**Vans used in rotation.** If two or more employees use a van in continuous rotation because of the work, the employer pays a final levy of EUR 451 a van a year instead of individual additions (par. 23.4.5).

**Youngtimer transition.** A car already made available to the same employee in 2025 that was at least 15 years old on 31 December 2025 and turns 16 during 2026 may use 35% of market value for all of 2026. This is an elective approval by policy decision ahead of legislation (Kamerstukken II 2025-26, 36812, nr. 116); the employer may instead use the catalogue value if that gives a lower addition. A car that turns 15 on or after 1 January 2026 uses 25% of catalogue value until it is more than 16 years old (par. 23.3.20). From 2027 the youngtimer age is 25 years and the discount for zero-emission cars first admitted in 2027 is 2% of the value, capped at EUR 600 (art. 13bis(1) and (2) as they read from 1 January 2027; par. 23.3.20, Let op 2).

## Deadlines and filing

- The addition runs through the ordinary payroll tax return (aangifte loonheffingen) for each period. File and pay by the date in the employer's Aangiftebrief loonheffingen (Handboek par. 13.2.2, 13.4.2). The period calendar is in `nl-payroll-tax`.
- In the return, report per employee the **value of private use before the contribution** and the **employee contribution** separately. On the payroll record (loonstaat) both go in column 4, the contribution as a negative amount (par. 23.3.23).
- Where a car is made available but nothing is added, enter the reason code: 1 (agreement with the Belastingdienst, also a van private-use ban), 2 (Verklaring geen privégebruik auto), 3 (other evidence, goods-only van, van not usable after hours), 5 (van final levy), 7 (Verklaring uitsluitend zakelijk gebruik bestelauto) (par. 23.3.23).
- Keep a copy of the Verklaring geen privégebruik auto, the van statement signed by the employee, and the written private-use ban with records of supervision, in the payroll records.
- The employee applies for the Verklaring geen privégebruik auto online with DigiD (par. 23.3.16). The employer files the van statement through "Inloggen voor ondernemers" (par. 23.4.7).

## Penalties and interest

- **Missed addition.** The Belastingdienst raises a supplementary assessment (naheffingsaanslag) on the employer for the wage tax, premiums and Zvw it should have paid. The payment-default penalty is 3% of the unpaid amount, minimum EUR 50, maximum EUR 6,709 (Handboek par. 13.5.1). Gross negligence or intent can lead to a vergrijpboete instead (par. 13.5.5).
- **Late or wrong return.** EUR 83 a return after the seven-day grace period; up to EUR 1,675 in exceptional repeat cases (par. 13.5.2, 13.5.4, 13.5.5).
- **Employee statement that turns out wrong.** If an employee with a Verklaring geen privégebruik auto drives more than 500 private km, the assessment for past periods goes to the **employee**, for wage tax, employee-insurance premiums and the Zvw contribution, with possible interest and a fine. The employer pays no employer Zvw or premiums for those periods. The assessment can be raised up to five years after the calendar year. If the employer knew the statement was wrong, the assessment goes to the employer (art. 13bis(11); par. 23.3.16).
- **Van statement and a private trip.** If the inspector suspects a private trip and the business purpose cannot be shown, the van is treated as used for more than 500 private km and the tax is assessed on the employee, or on the employer if it knew (art. 13bis(15)).
- Interest (belastingrente) is charged on a supplementary assessment for a past year (par. 14.5.1).

## Cross-border points

- **Imported cars.** The base is the Dutch catalogue price at first admission anywhere, or that of a comparable Dutch model (par. 23.3.2). A foreign-plated car does not escape the rule.
- **30% ruling.** The car benefit is wage and counts in the salary test for the expat scheme (par. 23.3.22). The ruling method is in `nl-30-percent-ruling`.
- **Employees working partly abroad.** Whether Dutch wage tax applies to the benefit follows the employee's tax liability and any treaty split of wages; social security follows the EU or bilateral coordination rules. Use `nl-cross-border` for the wage split, then apply this skill to the Dutch share.
- **VAT on private use** by the employer is a separate charge. See `nl-vat-return`.

## Worked examples

### Example 1: petrol car, list price EUR 45,000

A petrol car first admitted in 2025 is made available all of 2026 to an employee on a monthly payroll. The catalogue value including VAT and BPM is EUR 45,000. There is no trip log and no own contribution. The employee's total wage stays below the EUR 79,409 Zvw maximum.

The rate is 22% because the car has CO2 emissions and was first admitted after 2016. The annual addition is 22% of EUR 45,000, which is EUR 9,900. Each month EUR 825 is added to wage. Wage tax is withheld on it through the normal table. The employer pays employer Zvw of 6.10% on the addition, EUR 603.90 for the year, plus employee-insurance premiums. None of it can go into the WKR free space.

```oa-check
name: Petrol car, catalogue value EUR 45,000, full year 2026
inputs:
  catalogue_value: 45000
  rate_pct: 22
  zvw_pct: 6.10
  months: 12
steps:
  - annual_addition: catalogue_value * rate_pct / 100
  - monthly_addition: annual_addition / months
  - employer_zvw_year: annual_addition * zvw_pct / 100
expected:
  annual_addition: 9900.00
  monthly_addition: 825.00
  employer_zvw_year: 603.90
```

### Example 2: electric car, list price EUR 50,000, first admitted 2026, EUR 100 a month own contribution

A fully electric car (no hydrogen, no solar cells) is first admitted on 1 January 2026 and made available from that date. The catalogue value is EUR 50,000. The employee pays EUR 100 a month for private use, agreed in advance and withheld from net pay. Monthly payroll.

The 2026 discount is 4% of the value, capped at EUR 1,200. 4% of EUR 50,000 is EUR 2,000, so the cap applies. The value of private use is 22% of EUR 50,000 (EUR 11,000) less EUR 1,200, which is EUR 9,800. The same result follows from 18% of EUR 30,000 (EUR 5,400) plus 22% of EUR 20,000 (EUR 4,400). The own contribution of EUR 1,200 a year brings the addition to EUR 8,600, or EUR 716.67 a month. In the return the employer reports EUR 816.67 value of private use and EUR 100 contribution each month. The 60-month period runs from 1 February 2026 to 31 January 2031, so this rate holds for the whole of 2026. If the wage stays under the Zvw maximum, employer Zvw on the addition is EUR 524.60 for the year.

```oa-check
name: Electric car, catalogue value EUR 50,000, first admission 2026, EUR 100 a month contribution
inputs:
  catalogue_value: 50000
  general_pct: 22
  discount_pct: 4
  discount_cap: 1200
  low_band_cap: 30000
  low_pct: 18
  monthly_contribution: 100
  months: 12
  zvw_pct: 6.10
steps:
  - gross_value: catalogue_value * general_pct / 100
  - discount: min(catalogue_value * discount_pct / 100, discount_cap)
  - private_use_value: gross_value - discount
  - check_by_bands: low_band_cap * low_pct / 100 + (catalogue_value - low_band_cap) * general_pct / 100
  - annual_contribution: monthly_contribution * months
  - annual_addition: max(private_use_value - annual_contribution, 0)
  - monthly_value: private_use_value / months
  - monthly_addition: annual_addition / months
  - employer_zvw_year: annual_addition * zvw_pct / 100
expected:
  discount: 1200.00
  private_use_value: 9800.00
  check_by_bands: 9800.00
  annual_addition: 8600.00
  monthly_value: 816.67
  monthly_addition: 716.67
  employer_zvw_year: 524.60
```

## Ask the client first

1. The licence plate. From it: catalogue value incl. VAT and BPM, date of first admission, date of first Dutch registration (for pre-2017 cars) and CO2 emission.
2. Is the car a passenger car or a van, and if a van: goods-only, parked at the business after hours, a written private-use ban, or shared in rotation?
3. Does the employee have a Verklaring geen privégebruik auto, a closing trip log, or other evidence of 500 private km or less? From which date?
4. Is there a written agreement on an own contribution, how much, and is it withheld from net pay or paid to a third party?
5. Dates the car was made available, and any change of car during the year.
6. Is the employee a DGA, on the 30% ruling, or working partly abroad?

## Sources

| Source | URL | Read on |
|---|---|---|
| Wet op de loonbelasting 1964, art. 13bis, 31 and 36c (version 1 Jan 2026, and current version from 8 Oct 2026) | https://wetten.overheid.nl/BWBR0002471/2026-01-01 | 2026-10-23 |
| Wet op de loonbelasting 1964, current version | https://wetten.overheid.nl/BWBR0002471/ | 2026-10-23 |
| Wet op de loonbelasting 1964, version from 1 Jan 2027 (art. 13bis) | https://wetten.overheid.nl/BWBR0002471/2027-01-01 | 2026-10-23 |
| Staatssecretaris van Financiën, letter to the Eerste Kamer, Herstel omissie versobering youngtimerregeling, 15 Jan 2026 | https://apiback.eerstekamer.nl/9370000/1/j9vvkfvj6b325az/vmu8e84v2svn/f=/vmu8e84n1bqh.pdf | 2026-10-23 |
| Kamerstukken II 2025-26, 36812, nr. 116 (transition for cars that turned 15 in 2025) | https://zoek.officielebekendmakingen.nl/kst-36812-116.html | 2026-10-23 |
| Wet inkomstenbelasting 2001, art. 3.145 (repealed 1 Jan 2006) | https://wetten.overheid.nl/BWBR0011353/2026-01-01 | 2026-10-23 |
| Belastingdienst, Handboek Loonheffingen 2026 (March 2026), par. 13.2, 13.4, 13.5, 14.5, 23.3, 23.4 | https://download.belastingdienst.nl/belastingdienst/docs/handboek-loonheffingen-lh0221t61fd.pdf | 2026-10-23 |
| Belastingdienst, Tarieven, bedragen en percentages loonheffingen 2026 | https://download.belastingdienst.nl/belastingdienst/docs/bijlage-nieuwsbrief-loonheffingen-2026-lh2091b64fd.pdf | 2026-10-23 |
| Belastingdienst, Bijtelling privégebruik auto 2026 | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/veranderingen-inkomstenbelasting-2026/bijtelling-privegebruik-auto-2026 | 2026-10-23 |
| Belastingdienst, Werknemer: wat is mijn bijtelling? | https://www.belastingdienst.nl/wps/wcm/connect/nl/personeel-en-loon/content/reizen-werk-privegebruik-werknemer-wat-is-mijn-bijtelling | 2026-10-23 |
| Kennisgroep Belastingdienst KG:213:2026:1 (youngtimer age 25 from 2027) | https://kennisgroepen.belastingdienst.nl/publicaties/kg21320261-heretikettering-bij-wetswijziging-privegebruik-auto/ | 2026-10-23 |

Not yet confirmed: (1) the retroactive repair of art. 13bis(5)(b) (market value from 16 instead of 15 years) is announced but was not in the law text on 23 October 2026; (2) no October 2026 edition of the Handboek Loonheffingen 2026 was found, so the March 2026 edition is used.
