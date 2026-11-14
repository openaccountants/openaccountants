---
name: sri-lanka-betting-gaming-excise
description: "Sri Lanka Betting and Gaming Levy for 2026 and the year of assessment 2026/27, under the Betting and Gaming Levy Act No. 40 of 1988 as amended by Act No. 11 of 2023 and Act No. 25 of 2025. Covers who is liable (bookmakers and gaming businesses, each place separately), the annual levy amounts, the gross collection levy (18% from 1 January 2026, 15% before), the casino entrance levy on Sri Lankan citizens (USD 100), payment and quarterly return dates, the 45% income tax rate on betting, gaming, liquor and tobacco profits, and how VAT and SSCL interact. Excise duty and customs duty are flagged, not computed."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/sri-lanka-betting-gaming-excise"
  jurisdiction: "LK"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Sri Lanka Betting and Gaming Levy, with excise and customs flags (2026)

Built from the law: not yet approved by an accountant. Not tax advice.

## Scope and who this is for

- **Law:** Betting and Gaming Levy Act No. 40 of 1988, as amended, most recently by the Betting and Gaming Levy (Amendment) Act No. 11 of 2023 (certified 21 August 2023) and No. 25 of 2025 (certified 17 December 2025). Administered by the Inland Revenue Department (IRD).
- **Who is liable:** every person carrying on the business of a bookmaker or the business of gaming within Sri Lanka, lawfully or unlawfully. If the business is carried on in different places by the same person, the levy is payable for each place: each place is a separate business.
- **Bookmaker:** a person who receives or negotiates bets, directly or indirectly, in cash or on credit, or via internet, on horse races or any sport event in or outside Sri Lanka.
- **Gaming:** playing any game for a stake, including baccarat, punto banco, big six, black jack, chemin de fer, faro, poker dice, pontoon, roulette, rudjino or wheel of fortune, in premises to which individuals have access.
- **Also covered here:** the income tax rate on these businesses, and the VAT and SSCL interaction.
- **Flagged only:** excise duty on liquor, tobacco, fuel and motor vehicles (Department of Excise), customs import duty (Sri Lanka Customs), and the Gambling Regulatory Authority licensing regime. None of their figures was confirmed on an official page for this rewrite; see Not yet confirmed.

## Ask the client first

1. Bookmaker or gaming (casino or rudjino)? Through an agent or internet, with or without live telecast?
2. How many places of business?
3. Monthly gross collection for each place.
4. Number of Sri Lankan citizens entering the casino each instalment period.
5. Company or individual (income tax at 45% on these profits either way)?

## The method, step by step

### Rates, bands and thresholds

| Item | Amount | Conditions | Source |
| --- | --- | --- | --- |
| Gross collection levy, from 1 January 2026 | eighteen per centum of gross collection | Section 2(1A)(d) inserted by Act No. 25 of 2025 | https://www.ird.gov.lk/en/publications/Acts_Betting%20and%20Gaming%20Levy/BNG_Act_No._25_2025_E.pdf |
| Gross collection levy, 1 April 2023 to 31 December 2025 | fifteen per centum of gross collection | Section 2(1A)(c) as amended by Act No. 25 of 2025 | same |
| Casino entrance levy | USD 100, or the equivalent in another convertible currency or in Sri Lanka currency | From each Sri Lankan citizen entering the place of gaming; section 2(1AA)(b), amount substituted by Act No. 25 of 2025 (was USD 50) | same |
| Casino entrance levy applies to | Citizens of Sri Lanka only, from 1 April 2023 | Section 2(1AA)(b) as substituted by Act No. 11 of 2023 | https://www.ird.gov.lk/en/publications/Acts_Betting%20and%20Gaming%20Levy/BNG_Act_No._11_2023_E.pdf |
| Annual levy, bookmaker through an agent or via internet, with or without live telecast | Five million rupees a year | Every year from 1 April 2023; Schedule Part I item 8 | same |
| Annual levy, bookmaker with live telecast | One million rupees a year | Same | https://www.ird.gov.lk/en/Type%20of%20Taxes/SitePages/Betting%20and%20Gaming%20Levy.aspx?menuid=1210 |
| Annual levy, bookmaker without live telecast | Seventy-five thousand rupees a year | Same | same |
| Annual levy, business of gaming including rudjino | Five hundred million rupees a year | Every year from 1 April 2023 | same |
| Gross collection levy floor | No levy where gross collection does not exceed one million rupees per month | IRD guidance | same |
| Income tax on betting and gaming, and on domestic liquor or tobacco profits | 45% | From 1 April 2025, companies and individuals; exports of liquor or tobacco excluded | https://www.ird.gov.lk/en/publications/Acts_Income%20Tax_2017/IRA_Cons_Act_-_2025_Changes.pdf |

### Steps

1. Register each place of business separately.
2. Pay the annual levy in four equal instalments before the start of each quarter.
3. Each month, compute the gross collection levy at 18% (months from January 2026) on the gross collection of each place, unless gross collection does not exceed Rs. 1,000,000 for the month. Pay by the first week of the following month.
4. For a casino, collect the casino entrance levy from every Sri Lankan citizen entering and pay it with the instalments under section 2(1B)(b).
5. File the quarterly return: quarter to 31 March before 20 April; to 30 June before 20 July; to 30 September before 20 October; to 31 December before 20 January.
6. Income tax: the business profits are taxed at 45% (`sri-lanka-corporate-tax`, `sri-lanka-income-tax`).

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Business subject to the gross collection levy | Not liable to VAT, SSCL or the Nation Building Tax on that business (first proviso to section 2(1A), as amended by Act No. 11 of 2023) |
| Same operator, two casinos | Two businesses: two annual levies and two gross collection computations |
| Foreign visitor entering a casino | No casino entrance levy (citizens only since 1 April 2023) |
| Gross collection Rs. 1,000,000 or less in a month | No gross collection levy that month (IRD guidance) |
| Month in 2025 | 15% gross collection levy; 18% applies from January 2026 |
| Income tax rate quoted as 40% | Wrong from 1 April 2025; 45% now |
| Export of liquor or tobacco | Not at 45% income tax; normal rate |
| Online betting licences (Gambling Regulatory Authority Act No. 16 of 2025) | Not confirmed; refer |

## Worked cases

### Case 1: casino, one month in 2026

A casino has gross collection of Rs. 200,000,000 in March 2026 and 3,000 Sri Lankan citizen entrants. Gross collection levy at 18%; quarterly instalment of the annual levy is one quarter of Rs. 500,000,000; entrance levy USD 100 each.

```oa-check
name: Casino levies, one month and one quarter instalment, 2026
inputs:
  gross_collection: 200000000
  annual_levy: 500000000
  citizen_entrants: 3000
steps:
  - gcl: gross_collection * 0.18
  - quarter_instalment: annual_levy / 4
  - entrance_usd: citizen_entrants * 100
expected:
  gcl: 36000000
  quarter_instalment: 125000000
  entrance_usd: 300000
```

### Case 2: small bookmaker around the Rs. 1,000,000 monthly floor

A bookmaker without live telecast collects Rs. 900,000 in one month and Rs. 1,200,000 the next. The first month is below the floor; the second is not, and the levy runs on the whole collection. The 2026 rate costs Rs. 36,000 more than the 2025 rate on that month.

```oa-check
name: Gross collection levy below and above the floor
inputs:
  month_low: 900000
  month_high: 1200000
steps:
  - levy_low: min(month_low, 0)
  - levy_high: month_high * 0.18
  - levy_high_2025_rate: month_high * 0.15
  - rate_change_cost: levy_high - levy_high_2025_rate
expected:
  levy_low: 0
  levy_high: 216000
  levy_high_2025_rate: 180000
  rate_change_cost: 36000
```

## When to refuse or refer

- Excise duty, customs duty, para-tariffs, anti-dumping duties, BOI or strategic development project exemptions: refer to the Department of Excise or Sri Lanka Customs and a Sri Lankan professional; no figure here is confirmed.
- Gambling Regulatory Authority licensing and penalties: refer.
- Disputes, assessments or arrears under the levy Act: refer.

## Filing and payment

| Obligation | Due |
| --- | --- |
| Annual levy | In 4 equal instalments, before the start of each quarter |
| Gross collection levy | Monthly, by the first week of the following month |
| Casino entrance levy | With each instalment (section 2(1B)(b)) |
| Quarterly return | Before 20 April, 20 July, 20 October, 20 January |

## Completion checklist

- [ ] Each place registered and levied separately
- [ ] 18% applied to months from January 2026
- [ ] Monthly floor of Rs. 1,000,000 checked
- [ ] Entrance levy collected from citizens only, at USD 100
- [ ] VAT and SSCL not charged on the levied business
- [ ] Income tax at 45% passed to the income tax skills

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Read for section 2 (gross collection levy rate of 18% and casino entrance levy of USD 100) of the Betting and Gaming Levy (Amendment) Act No. 25 of 2025 | https://www.ird.gov.lk/en/publications/Acts_Betting%20and%20Gaming%20Levy/BNG_Act_No._25_2025_E.pdf | 2026-11-14 |
| Read for section 2 (15% rate, citizens-only entrance levy, the VAT, NBT and SSCL proviso) and Schedule Part I (annual bookmaker levies) of Act No. 11 of 2023 | https://www.ird.gov.lk/en/publications/Acts_Betting%20and%20Gaming%20Levy/BNG_Act_No._11_2023_E.pdf | 2026-11-14 |
| Read for persons liable, definitions, annual levy amounts, the Rs. 1,000,000 monthly floor, payment and return dates on the IRD Betting and Gaming Levy page (the page still shows the older 15% and USD 50) | https://www.ird.gov.lk/en/Type%20of%20Taxes/SitePages/Betting%20and%20Gaming%20Levy.aspx?menuid=1210 | 2026-11-14 |
| Read for First Schedule paragraphs 1(2)(c) and 4(2C) (45% income tax rate) in the IRD consolidated Act | https://www.ird.gov.lk/en/publications/Acts_Income%20Tax_2017/IRA_Cons_Act_-_2025_Changes.pdf | 2026-11-14 |

Not yet confirmed: whether the Rs. 1,000,000 monthly floor is still in the Act after the 2023 and 2025 amendments (the IRD page states it); excise duty rates and rules on liquor, tobacco, petroleum products and motor vehicles; customs import duty bands (the earlier version cited 0%, 10%, 20% and 30% from April 2026 under a National Tariff Policy) and the phasing out of PAL and CESS; anti-dumping and countervailing duties; BOI and SDP exemptions; the Gambling Regulatory Authority Act No. 16 of 2025 (licensing, penalty of up to LKR 10 million or 2 years, self-exclusion duties, 30 June 2026 operational target); SSCL on vehicle sales from April 2026; how VAT and SSCL are collected at import by Sri Lanka Customs.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `sri-lanka-betting-gaming-excise` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/sri-lanka-betting-gaming-excise. If neither is available, confirm every figure against the official source pages cited above before relying on it.
