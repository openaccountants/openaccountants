---
name: no-individual-residence
description: >
  Norwegian tax residence of individuals for income year 2026: arrival,
  emigration and the cross-border consequences. Covers the 183 days in 12 months
  and 270 days in 36 months presence tests in skatteloven § 2-1, when residence
  starts, emigration under the 61-day and no-home conditions, the three-year
  tail for people resident ten years or more, the home and family definitions
  and the five-year holiday-home exception, wealth tax liability on 31 December,
  global versus limited liability (§ 2-3), the one-year foreign work relief, the
  foreign tax credit, the exit tax on shares above NOK 3 million with 12-year
  deferral, treaty residence, return deadlines and additional tax. Trigger on:
  Norway tax residence, skattemessig bosatt, emigrate from Norway, 183 days
  Norway, 61 days rule, ten-year rule, exit tax Norway, utflyttingsskatt,
  ettårsregelen. Out of scope: income tax bands (no-income-tax), payroll
  withholding (no-employer-payroll), the Switzerland corridor
  (norway-to-switzerland-wealth-tax-exit).
jurisdiction: "NO"
category: cross-border
tax_year: 2026
tier: 2
last_updated: 2026-10-30
version: 0.2
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Norway individual tax residence (2026) v0.2

Income year 2026. Currency: Norwegian kroner (NOK). Authority: Skatteetaten. Statutes: Skatteloven (Taxation Act, lov 26 March 1999 nr. 14, "sktl.") §§ 2-1, 2-3, 10-70, 16-20 and chapter 20; Skatteforvaltningsloven (lov 27 May 2016 nr. 14, "sktfvl.") and its regulation (forskrift 23 November 2016 nr. 1360). See Sources.

**What changed for 2026.** Sktl. § 2-1 was amended by lov 22 December 2025 nr. 119 with effect from income year 2026. The seventh paragraph now ties wealth tax liability to living in Norway at the end of 31 December of the year before the assessment year; Skatteetaten describes this as putting existing practice into law (Forskuddsutskrivingen 2026).

See also: [norway-to-switzerland-wealth-tax-exit](norway-to-switzerland-wealth-tax-exit.md) (one exit corridor in depth), [no-income-tax](no-income-tax.md), [no-employer-payroll](no-employer-payroll.md) (PAYE source tax for short-stay workers).

## Who this applies to

- **Arrivals and frequent visitors.** A person is resident if, in one or more periods, they stay in Norway more than 183 days in any 12-month period, or more than 270 days in any 36-month period (sktl. § 2-1 second paragraph). The 270-day test does not apply to a person resident on Svalbard.
- **Leavers.** A resident who takes up permanent residence abroad stays resident until the § 2-1 third paragraph conditions are met.
- **Diplomats and NATO staff.** Norwegian foreign-service staff posted abroad, and employees serving in NATO with a fixed post abroad, are treated as resident (§ 2-1 eighth paragraph).
- **Non-residents with Norwegian income.** Taxed only on the sources in § 2-3 (limited liability).
- **Out of scope.** Companies' residence (§ 2-2), Svalbard tax, seafarers, treaty tie-breaker analysis for a specific treaty.

## Rates, bands and thresholds

| Item | Amount | Year | Source |
|---|---|---|---|
| Arrival: 12-month test | More than 183 days in any 12-month period | 2026 | sktl. § 2-1 second paragraph letter a; https://lovdata.no/lov/1999-03-26-14/§2-1 |
| Arrival: 36-month test | More than 270 days in any 36-month period | 2026 | sktl. § 2-1 second paragraph letter b |
| Emigration: presence limit | Not in Norway for periods exceeding 61 days in the income year | 2026 | sktl. § 2-1 third paragraph letters a and b |
| Long-resident rule | Resident at least 10 years before the year of moving: residence ends only after the 3rd income year after the moving year | 2026 | sktl. § 2-1 third paragraph letter b |
| Holiday-home exception | A unit acquired at least 5 years before the moving year, not used as a home by the person or close relatives in that period, is not a "home" | 2026 | sktl. § 2-1 sixth paragraph |
| Wealth tax liability | Living in Norway at the end of 31 December of the year before the assessment year | From income year 2026 | sktl. § 2-1 seventh paragraph (lov 2025-12-22-119) |
| Foreign work relief | Work stay abroad of at least 12 continuous months; Norway visits average at most 6 days per full month (9 days where unforeseeable) | 2026 | sktl. § 2-1 tenth paragraph letters a and b |
| Foreign work relief, state employees | Several stays of at least 6 months each, together at least 12 months within 30 months | 2026 | sktl. § 2-1 tenth paragraph letter a, second sentence |
| Exit tax threshold on emigration | Net gain on shares etc. above NOK 3,000,000 | 2026 | sktl. § 10-70 fourth paragraph; https://lovdata.no/lov/1999-03-26-14/§10-70 |
| Exit tax on transfer to a non-resident | Net gain or loss above NOK 100,000 in the income year | 2026 | sktl. § 10-70 fourth paragraph, second sentence |
| Exit tax payment deferral | Up to 12 years from the end of the year the tax is timed to | 2026 | sktl. § 10-70 seventh paragraph |
| Upward adjustment factor for share gains | 1.72 (gain after unused shielding, times 1.72, taxed as ordinary income at 22%) | 2026 | Forskuddsutskrivingen 2026; sktl. § 10-31 first paragraph; https://www.skatteetaten.no/rettskilder/type/uttalelser/uttalelser/forskuddsutskrivingen-2026/ |
| Dividends to shareholders resident abroad | 25% unless a treaty reduces it | 2026 | Forskuddsutskrivingen 2026; sktl. §§ 2-3 first paragraph letter c, 10-13 |
| PAYE source tax on wages (short-stay non-residents) | 25%; cap NOK 725,050 | 2026 | Forskuddsutskrivingen 2026; sktl. chapter 20 |
| Change window where exit tax was not assessed | 15 years after the end of the tax period | 2026 | sktfvl. § 12-6 first paragraph |

## The base

1. **Count days.** Every whole or part day in Norway counts; days need not be in a row and the reason for the stay does not matter (Skatteetaten, global tax liability). Test every rolling 12-month and 36-month window.
2. **When residence starts.** Residence begins in the income year in which the stay first exceeds 183 or 270 days (§ 2-1 second paragraph). Skatteetaten applies this as follows: more than 183 days in the arrival year means resident from the arrival date; if the days are split over two years, resident from 1 January of the second year; under the 270-day test, resident from 1 January of the year the total passes 270 (global tax liability page). An average of 90 days a year for three years (270 days in total) does not exceed 270.
3. **Global liability.** A resident is taxed on all income and wealth in Norway and abroad (§ 2-1 ninth paragraph) and files a full return.
4. **Emigration, under ten years' residence (§ 2-1 third paragraph letter a).** Residence ends for the income year in which the person shows that they (a) have taken up permanent residence abroad, (b) did not stay in Norway for periods exceeding 61 days in that year, and (c) did not, with their close relatives, have a home available in Norway. It never ends before the date the person and close relatives stop having a home available in Norway.
5. **Emigration, ten years or more (letter b).** Residence ends only after the third income year after the moving year, and only if for each of those three years the person shows the 61-day and no-home conditions were met.
6. **Definitions.** Close relatives: spouse, cohabitant or minor children (fourth paragraph). Having a home available: owning, renting or having any other right to use a home, directly or indirectly (fifth paragraph). Home: a unit with year-round water and drainage unless planning rules bar its use as a home, and any unit actually used as a home; the five-year holiday-home exception in the sixth paragraph applies.
7. **Foreign work relief (§ 2-1 tenth paragraph).** A resident working abroad for at least 12 continuous months can claim a reduction of the total tax equal to the part that falls on salary for the work abroad. It does not apply to income only Norway may tax under a treaty, or to work mainly outside any state's territory. For salary from the Norwegian state (not for business services) the relief covers only municipal and county tax.
8. **Foreign tax credit (§ 16-20).** A resident taxed on foreign-source income or foreign wealth can deduct the final foreign income or wealth tax paid on it. A person who is resident in another state under a treaty cannot claim this credit.
9. **Exit tax (§ 10-70).** On ceasing residence under § 2-1 third paragraph, or on becoming resident in another state under a treaty, a gain on Norwegian and equivalent foreign shares, share savings accounts, partnership interests, options and certain life policies is taxed as if realised on the last day before. Only the part of total net gain above NOK 3,000,000 is taxable on emigration. Losses are deductible on a move to another EEA state (third paragraph). Market value at the move is the exit value; for assets held on arrival, the entry value is market value at arrival (fifth and sixth paragraphs).

## Deadlines and filing

| What | Deadline | Source |
|---|---|---|
| Tax return, individuals | End of April after the income year (30 April 2027 for 2026) | sktfvf. § 8-2-3 first paragraph letter b |
| Tax return, owners of a sole proprietorship | End of May after the income year | sktfvf. § 8-2-3 first paragraph letter a |
| Proof of emigration conditions | For each year the person relies on: the 61-day and no-home conditions must be shown ("godtgjøres") | sktl. § 2-1 third paragraph |
| Exit tax information | Without being asked and without undue delay, any information relevant to the exit tax; a breach ends the deferral | sktl. § 10-70 eleventh paragraph |

A person taxed only under the chapter 20 PAYE scheme does not file a return (sktfvl. § 8-2 fifth paragraph). Spouses with different deadlines may both use the later one (sktfvf. § 8-2-3 second paragraph).

## Penalties and interest

- **Additional tax (sktfvl. §§ 14-3, 14-5).** 20% of the tax advantage for wrong or incomplete information, such as an unreported foreign income or a wrongly claimed emigration. Plus 20% or 40% where wilful or grossly negligent (§ 14-6).
- **Coercive fine (§ 14-1; sktfvf. § 14-1-1).** For a missing return, normally half a court fee a day (NOK 672.50 with the 2026 court fee of NOK 1,345), at most 50 court fees (NOK 67,250).
- **Change window (§ 12-6).** Five years after the end of the income year, ten years with aggravated additional tax, and 15 years where exit tax under § 10-70 first paragraph was never assessed.
- **Deferral lost (§ 10-70 eighth and eleventh paragraphs).** The exit tax deferral ends on realisation, death (unless heirs take over the duties), a transfer to a non-resident, and any breach of the duty to inform.

## Cross-border points

- **Treaty residence.** Domestic residence under § 2-1 can continue while a treaty makes the person resident in the other state. The treaty then limits Norway's taxing rights; the § 16-20 credit is no longer available (§ 16-20 first paragraph, last sentence). Becoming treaty-resident abroad also triggers the exit tax (§ 10-70 first paragraph).
- **Limited liability (§ 2-3).** A non-resident is taxed on, among others, Norwegian real estate and business, dividends from Norwegian companies, pay for work done during a temporary stay in Norway, and board fees from Norwegian companies (§ 2-3 first paragraph letters a to f). An employee hired out to work in Norway is also taxed (§ 2-3 second paragraph).
- **Exit tax deferral.** Up to 12 years with security; on a move within the EEA, security is required only where there is a real risk the tax cannot be collected. The person pays one twelfth a year, or everything at the end with interest (§ 10-70 seventh paragraph). If the person becomes resident in Norway again within 12 years, the exit tax falls away for the assets still held (ninth paragraph).
- **Returning residents.** For assets owned on arrival, the entry value is market value at arrival, less gains built up in an earlier period of Norwegian residence that were not taxed here (§ 10-70 sixth paragraph).

## Worked examples

### Example 1: repeated visits exceed the 36-month test

A consultant spends 80 days in Norway in 2024, 90 days in 2025 and 110 days in 2026, all in one 36-month window, and never more than 183 days in any 12 months. The total is 280 days, 10 days over 270. The 270-day limit is passed during 2026, so she is resident from 1 January 2026 and must report her worldwide income and wealth for 2026.

```oa-check
name: Norway 36-month presence test, 80 + 90 + 110 days
inputs:
  days_2024: 80
  days_2025: 90
  days_2026: 110
  limit_36_months: 270
steps:
  - total_days: days_2024 + days_2025 + days_2026
  - excess_days: total_days - limit_36_months
expected:
  total_days: 280
  excess_days: 10
```

### Example 2: long-resident leaver with a share portfolio

A person resident in Norway since 2012 moves permanently to Spain on 1 July 2026 and is resident in Spain under the treaty from that date. On 30 June 2026 his shares have a market value of NOK 9,000,000 and a cost of NOK 4,000,000.

1. Residence history: 14 years, more than ten, so letter b applies. Norwegian residence continues until the end of the third income year after 2026: 2029. It ends then only if he shows, for each of 2027, 2028 and 2029, at most 61 days in Norway and no home available to him or his close relatives.
2. Exit tax is triggered on 1 July 2026, when he becomes treaty-resident in Spain (§ 10-70 first paragraph), not in 2030.
3. Gain: 9,000,000 - 4,000,000 = NOK 5,000,000. The part above NOK 3,000,000 is taxable: NOK 2,000,000.
4. Spain is in the EEA, so he can ask for 12 years' deferral, with security only if there is a real risk the tax cannot be collected. The tax rate on the taxable gain follows the share rules (no-capital-gains); see Not yet confirmed for how the 1.72 adjustment combines with the threshold.

```oa-check
name: Norway exit tax, gain NOK 5m, NOK 3m threshold, 10-year resident leaving in 2026
inputs:
  moving_year: 2026
  tail_years: 3
  market_value: 9000000
  cost: 4000000
  exit_threshold: 3000000
steps:
  - last_resident_year: moving_year + tail_years
  - gain: market_value - cost
  - taxable_gain: max(gain - exit_threshold, 0)
expected:
  last_resident_year: 2029
  gain: 5000000
  taxable_gain: 2000000
```

## Ask the client first

1. Exact days in Norway in each of the last three years, with travel evidence.
2. How long has the person been resident in Norway, and has an earlier emigration been accepted?
3. Which homes in Norway can the person, spouse, cohabitant or minor children use, by ownership, lease or otherwise, and when were they acquired and last lived in?
4. Where will the person live permanently, and is a treaty residence certificate available?
5. What shares, funds, share savings accounts and partnership interests does the person hold, at what cost and market value?
6. Is the person working abroad for 12 months or more, and for whom?

## Sources

| Source | URL | Read on |
|---|---|---|
| Skatteloven (lov 1999-03-26-14) § 2-1, as amended by lov 2025-12-22-119 | https://lovdata.no/lov/1999-03-26-14/§2-1 | 2026-10-30 |
| Skatteloven §§ 2-3, 10-70, 16-20, 20-1 to 20-3 | https://lovdata.no/lov/1999-03-26-14/§10-70 | 2026-10-30 |
| Skatteforvaltningsloven (lov 2016-05-27-14) §§ 8-2, 12-6, 14-1, 14-3 to 14-6 | https://lovdata.no/dokument/NL/lov/2016-05-27-14 | 2026-10-30 |
| Skatteforvaltningsforskriften (forskrift 2016-11-23-1360) §§ 8-2-3, 14-1-1 | https://lovdata.no/forskrift/2016-11-23-1360/§8-2-3 | 2026-10-30 |
| Rettsgebyrloven (lov 1982-12-17-86) § 1 and note 1 (court fee NOK 1,345 from 1 January 2026) | https://lovdata.no/lov/1982-12-17-86/§1 | 2026-10-30 |
| Skatteetaten, Forskuddsutskrivingen 2026 (15 December 2025) | https://www.skatteetaten.no/rettskilder/type/uttalelser/uttalelser/forskuddsutskrivingen-2026/ | 2026-10-30 |
| Skatteetaten, global tax liability (counting days, when residence starts) | https://www.skatteetaten.no/en/person/to-from-norway/from/tax-when-you-move-abroad/global-tax-liability/ | 2026-10-30 |

Not yet confirmed: how the NOK 3,000,000 exit threshold combines with the 1.72 upward adjustment and shielding deduction in the exit tax computation; the interest on deferred exit tax; the form or return section used to claim emigration (Skatteetaten's emigration and treaty-residence pages cited in v0.1 now redirect to a general page); the treatment of wealth in each treaty; Svalbard residence.
