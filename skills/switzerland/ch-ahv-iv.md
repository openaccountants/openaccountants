---
name: ch-ahv-iv
description: "Swiss AHV/IV/EO social contributions of the self-employed and of non-employed persons for 2026. Covers who counts as self-employed, the full rate of 10.0% (AHV 8.1%, IV 1.4%, EO 0.5%) from CHF 60,500, the full sliding scale from CHF 10,100 (5.371%) and the minimum contribution of CHF 530, how the contribution income is found (tax assessment, add-back of own contributions, interest on own capital, rounding), provisional (Akonto) and final contributions, the allowance past reference age, 5% late interest, non-employed contributions by wealth (CHF 530 to 26,500), voluntary BVG and the pillar 3a limits for 2026 (CHF 7,258 / 20% up to CHF 36,288). Trigger on: AHV Selbständige, AHV/IV/EO self-employed, sinkende Beitragsskala, Akontobeiträge, Beitragsverfügung, Nichterwerbstätige AHV, Säule 3a Selbständige. Out of scope: ch-payroll (employees), ch-federal-income-tax and ch-cantonal-tax (the tax return), ch-cross-border (which country insures)."
version: 2.2
jurisdiction: CH
tax_year: 2026
last_updated: 2026-10-31
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Switzerland: AHV/IV/EO contributions of the self-employed (2026)

This skill covers the old-age and survivors' insurance (AHV), disability insurance (IV) and income compensation (EO) contributions that self-employed people pay on their own earnings, and the contributions of people with no earned income. It links to the pack's other skills rather than repeating them:

- `ch-payroll`: contributions on wages (10.6%, split 5.3% each between employee and employer), ALV, BVG for employees, tax at source.
- `ch-federal-income-tax` and `ch-cantonal-tax`: the tax return, where own AHV/IV/EO and pillar 3a contributions are deducted.
- `ch-cross-border`: which country insures a person who works in Switzerland and abroad (EU coordination, A1 certificates).

## Who this applies to

**Self-employed.** A person is self-employed for AHV if they work in their own name and for their own account, independently, and carry their own economic risk. Signs are: trading under a business name, invoicing in their own name, financing their own equipment and premises, bearing bad-debt risk, organising their own work, and working for several clients ([AHV/IV sheet 2.02](https://www.ahv-iv.ch/p/2.02.d), no. 1). The compensation fund (Ausgleichskasse) decides, activity by activity, on the economic facts, not the contract. The same person can be self-employed for one activity and employed for another. Partners of a general or limited partnership pay on their share of the partnership's income (AHVV art. 20 para. 3).

A self-employed person is not insured against unemployment, is not compulsorily insured against accidents, and is not in compulsory BVG ([sheet 2.02](https://www.ahv-iv.ch/p/2.02.d), no. 2).

**When contributions start and end.** From 1 January after the 17th birthday, and until the activity ends. Contributions continue past reference age (65) on income above an allowance (see below). Someone who stops work before reference age pays as a non-employed person ([sheet 2.02](https://www.ahv-iv.ch/p/2.02.d), no. 3 and 4; AHVG art. 3).

**Non-employed.** People resident in Switzerland with no earned income pay from 1 January after their 20th birthday to the end of the month in which they reach reference age: early retirees, people living on wealth, students, the long-term unemployed and others (AHVG art. 3 para. 1bis; [sheet 2.03](https://www.ahv-iv.ch/p/2.03.d)). A non-employed spouse pays nothing if the working spouse pays at least CHF 1,060 (twice the minimum) in the year (AHVG art. 3 para. 3). People who are not fully employed all year (under nine months or under 50% of normal hours) pay as non-employed if their contributions on earnings, with the employer's share, are less than half of what they would owe as non-employed (AHVV art. 28bis).

**Not covered here:** employees (`ch-payroll`), owner-managers of an AG or GmbH (they are employees of their company for AHV, see `ch-payroll`), and the contribution rules of agriculture.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Full rate, self-employed | 10.0%: AHV 8.1%, IV 1.4%, EO 0.5%; no ceiling | 2026 | [sheet 2.02, no. 5](https://www.ahv-iv.ch/p/2.02.d); [AHVG art. 8](https://www.fedlex.admin.ch/eli/cc/63/837_843_843/de); [IVG art. 3](https://www.fedlex.admin.ch/eli/cc/1959/827_857_845/de); [EOG art. 27](https://www.fedlex.admin.ch/eli/cc/1952/1021_1046_1050/de) |
| Full rate applies from | Income of CHF 60,500 | 2026 | [sheet 2.02, no. 6](https://www.ahv-iv.ch/p/2.02.d); [AHVV art. 21](https://www.fedlex.admin.ch/eli/cc/63/1185_1183_1185/de) |
| Sliding scale (sinkende Beitragsskala) | CHF 10,100 to under 60,500, total rate 5.371% to 9.321% (full table below) | 2026 | [sheet 2.02, no. 6](https://www.ahv-iv.ch/p/2.02.d); [AHVV art. 21](https://www.fedlex.admin.ch/eli/cc/63/1185_1183_1185/de) |
| Minimum contribution | CHF 530 a year in total (AHV part CHF 435) on income under CHF 10,100 | 2026 | [sheet 2.02, no. 6](https://www.ahv-iv.ch/p/2.02.d); [AHVG art. 8 para. 2](https://www.fedlex.admin.ch/eli/cc/63/837_843_843/de) |
| Minimum already paid on wages | Then only the lowest scale rate, 5.371%, on self-employed income under CHF 10,100 (on request) | 2026 | [sheet 2.02, no. 6](https://www.ahv-iv.ch/p/2.02.d) |
| Small side income | Up to CHF 2,500 a year from a side activity: contributions only on request | 2026 | [AHVV art. 19](https://www.fedlex.admin.ch/eli/cc/63/1185_1183_1185/de) |
| Rounding | Income rounded down to the next CHF 100; own capital rounded up to the next CHF 1,000 | 2026 | [AHVG art. 8 para. 1](https://www.fedlex.admin.ch/eli/cc/63/837_843_843/de); [AHVV art. 18 para. 2](https://www.fedlex.admin.ch/eli/cc/63/1185_1183_1185/de) |
| Interest on own capital in the business, deducted from income | 1.0% for 2025; 1.5% for 2024; 2.0% for 2023; the 2026 rate is published in January 2027 | 2025 | [BSV Mitteilung Nr. 504, 19.1.2026](https://sozialversicherungen.admin.ch/de/d/21883/download); [sheet 2.02, no. 7](https://www.ahv-iv.ch/p/2.02.d) |
| Administration cost contribution | Up to 5% of the contributions, set by each fund | 2026 | [sheet 2.02, no. 6](https://www.ahv-iv.ch/p/2.02.d) |
| Allowance past reference age | CHF 16,800 a year (pro rata in the year reference age is reached); can be waived | 2026 | [AHVV art. 6quater para. 4 and 5](https://www.fedlex.admin.ch/eli/cc/63/1185_1183_1185/de) |
| Contributions on EO and IV daily allowances | 5.3%, deducted by the fund | 2026 | [sheet 2.02, no. 18](https://www.ahv-iv.ch/p/2.02.d) |
| Non-employed, wealth plus 20 x annual pension income under CHF 350,000 | CHF 530 a year | 2026 | [sheet 2.03, no. 8](https://www.ahv-iv.ch/p/2.03.d); [AHVV art. 28](https://www.fedlex.admin.ch/eli/cc/63/1185_1183_1185/de) |
| Non-employed, CHF 350,000 to 1,750,000 | CHF 636, plus CHF 106 for each further CHF 50,000 (CHF 3,604 at 1,750,000) | 2026 | [sheet 2.03, no. 8](https://www.ahv-iv.ch/p/2.03.d) |
| Non-employed, above CHF 1,750,000 | Plus CHF 159 for each further CHF 50,000; maximum CHF 26,500 from CHF 8,950,000 | 2026 | [sheet 2.03, no. 8](https://www.ahv-iv.ch/p/2.03.d) |
| Late payment interest | 5% a year, day by day (30-day month, 360-day year) | 2026 | [AHVV art. 41bis and 42](https://www.fedlex.admin.ch/eli/cc/63/1185_1183_1185/de) |
| Reminder fee | CHF 20 to 200 per reminder | 2026 | [AHVV art. 34a](https://www.fedlex.admin.ch/eli/cc/63/1185_1183_1185/de) |
| Pillar 3a limit, insured in a BVG pension fund | CHF 7,258 | 2026 | [BVV 3 art. 7 para. 1 let. a](https://www.fedlex.admin.ch/eli/cc/1985/1778_1778_1778/de); [BSV Masszahlen 2025/2026](https://www.bsv.admin.ch/dam/de/sd-web/GZplHByBJoFc/Internet_Masszahlenarticles_25_26_d.pdf), no. 9 |
| Pillar 3a limit, not in a BVG pension fund | 20% of earned income, at most CHF 36,288 | 2026 | [BVV 3 art. 7 para. 1 let. b](https://www.fedlex.admin.ch/eli/cc/1985/1778_1778_1778/de); [BSV Masszahlen](https://www.bsv.admin.ch/dam/de/sd-web/GZplHByBJoFc/Internet_Masszahlenarticles_25_26_d.pdf), no. 9 |
| BVG voluntary insurance, income limits | Same as compulsory: coordination deduction CHF 26,460, maximum insured CHF 90,720 | 2026 | [BVG art. 4 para. 2 and art. 8](https://www.fedlex.admin.ch/eli/cc/1983/797_797_797/de); [BSV Masszahlen](https://www.bsv.admin.ch/dam/de/sd-web/GZplHByBJoFc/Internet_Masszahlenarticles_25_26_d.pdf) |

**The 2026 sliding scale.** Total AHV/IV/EO rate on the year's income ([sheet 2.02, no. 6](https://www.ahv-iv.ch/p/2.02.d)). The AHV part alone is in AHVV art. 21 para. 1 (4.35% to 7.55%); IV and EO are scaled in the same proportion (IVG art. 3 para. 1, EOG art. 27 para. 2).

| Income from (CHF) | Under (CHF) | Total rate | AHV part (AHVV art. 21) |
|---|---|---|---|
| 0 | 10,100 | Minimum CHF 530 | |
| 10,100 | 17,600 | 5.371% | 4.35% |
| 17,600 | 23,000 | 5.494% | 4.45% |
| 23,000 | 25,500 | 5.617% | 4.55% |
| 25,500 | 28,000 | 5.741% | 4.65% |
| 28,000 | 30,500 | 5.864% | 4.75% |
| 30,500 | 33,000 | 5.987% | 4.85% |
| 33,000 | 35,500 | 6.235% | 5.05% |
| 35,500 | 38,000 | 6.481% | 5.25% |
| 38,000 | 40,500 | 6.728% | 5.45% |
| 40,500 | 43,000 | 6.976% | 5.65% |
| 43,000 | 45,500 | 7.222% | 5.85% |
| 45,500 | 48,000 | 7.469% | 6.05% |
| 48,000 | 50,500 | 7.840% | 6.35% |
| 50,500 | 53,000 | 8.209% | 6.65% |
| 53,000 | 55,500 | 8.580% | 6.95% |
| 55,500 | 58,000 | 8.951% | 7.25% |
| 58,000 | 60,500 | 9.321% | 7.55% |
| 60,500 | no limit | 10.000% | 8.1% |

The rate in a band applies to the whole income, not just the slice inside the band.

**13th AHV old-age pension.** From 2026 everyone receiving an AHV old-age pension in December gets a 13th pension, one twelfth of the year's pension, paid for the first time in December 2026 (AHVG art. 34ter). It does not change 2026 contributions: the 1 January 2026 editions of sheets 2.02 and 2.03 keep 10.0% and CHF 530, and the AHVG in force from 1 January 2027 still sets the AHV rate at 8.1%.

**From 2027.** The Federal Council moved the scale to CHF 10,300 to under 61,500 from 1 January 2027 (AHVV art. 21 as amended on 2 October 2026, AS 2026 541). Use the 2026 table above for contribution year 2026.

## The taxable base

**What is income.** All income earned independently from trade, industry, a craft, farming or a profession, including capital gains and transfer gains on business assets under DBG art. 18 para. 2. Income from shareholdings declared as business assets is excluded (AHVV art. 17).

**Who sets it.** The cantonal tax office reports the net income from self-employment, taken from the final federal tax assessment, and the own capital invested in the business, from the cantonal assessment. The fund is bound by these figures (AHVG art. 9 para. 3; AHVV art. 23). Deductions (costs, depreciation, provisions, business losses of the year and the year before, the owner's own BVG contributions up to the usual employer share) follow the federal tax rules (AHVG art. 9 para. 2; AHVV art. 18).

**Step by step, for one contribution year:**

1. Start from the net income from self-employment in the tax assessment for the business year that closed in the contribution year (AHVV art. 22 para. 2). No splitting between years if the business year differs from the calendar year, and no annualising of a short year (AHVV art. 22 para. 3 and 5).
2. Add back the own AHV/IV/EO contributions that were deducted for tax. The fund grosses the reported income up to 100% using the applicable rate (AHVG art. 9 para. 4; [sheet 2.02](https://www.ahv-iv.ch/p/2.02.d), no. 9).
3. Deduct interest on the own capital invested in the business at 31 December, rounded up to the next CHF 1,000, at the rate for that year (AHVG art. 9 para. 2 let. f; AHVV art. 18 para. 2). The rate is the yearly average yield of CHF bonds of private Swiss borrowers (SNB statistics), rounded to the nearest half percent. For 2025 it is 1% (BSV Mitteilung Nr. 504). The BSV announces the 2026 rate in January 2027.
4. Past reference age, deduct the CHF 16,800 allowance unless waived (AHVV art. 6quater).
5. Round down to the next CHF 100 (AHVG art. 8 para. 1).
6. Apply the rate for the band the income falls in, or the CHF 530 minimum below CHF 10,100. Past reference age, income under CHF 10,100 after the allowance is charged at the lowest rate (5.371%), but never more than the CHF 530 minimum (AHVV art. 21 para. 2; sheet 2.02, no. 17).

**Not part of the base for the fund:** EO maternity, paternity and service allowances and IV, ALV and military daily allowances. The fund deducts 5.3% from these directly, so they must be shown separately from business income in the tax return ([sheet 2.02](https://www.ahv-iv.ch/p/2.02.d), no. 18).

**Own contributions in the tax return.** Own AHV/IV/EO contributions reduce taxable income (see `ch-federal-income-tax`). Pillar 3a contributions are private costs and may not be booked in the profit and loss account ([ESTV circular 18a](https://www.estv.admin.ch/dam/de/sd-web/yQgKmvu80LEr/dbst-ks-2025-1-018a-dv-de.pdf), no. 5.1).

**Non-employed.** Net wealth at 31 December of the contribution year plus 20 times the year's pension income, rounded down to the CHF 50,000 step (AHVV art. 28 para. 1 to 3). Married people use half of the couple's wealth and pension income each. Pension income includes foreign pensions, the 13th AHV pension, alimony for the spouse, sickness and accident daily allowances and regular support from third parties. It excludes IV benefits, supplementary benefits and investment income. Second-pillar savings are not wealth ([sheet 2.03](https://www.ahv-iv.ch/p/2.03.d), no. 4 to 7).

**BVG and pillar 3a.** BVG is voluntary for the self-employed. They can join the pension fund of their profession or of their employees, or the substitute institution (Auffangeinrichtung), or insure only in the extra-mandatory part (BVG art. 4 and 44). A self-employed person without a pension fund may pay into pillar 3a up to 20% of earned income, capped at CHF 36,288 for 2026. Earned income here means the profit and loss balance after tax adjustments, after deducting own AHV/IV/EO contributions and before any pillar 3a contributions ([ESTV circular 18a](https://www.estv.admin.ch/dam/de/sd-web/yQgKmvu80LEr/dbst-ks-2025-1-018a-dv-de.pdf), no. 5.5). A loss means no 3a deduction. With a pension fund the limit is CHF 7,258. Payments must reach the 3a account by 31 December. Since 2025, missed contributions for 2025 onwards can be bought in later, up to CHF 7,258 a year, once the current year's maximum is paid (BVV 3 art. 7a; circular 18a, no. 5.6).

## Deadlines and filing

| What | When | Source |
|---|---|---|
| Register with the compensation fund | On starting the activity; the fund decides on status. Non-employed people register themselves with the fund of their canton of residence | [sheet 2.02](https://www.ahv-iv.ch/p/2.02.d), "Auf einen Blick"; [sheet 2.03](https://www.ahv-iv.ch/p/2.03.d), no. 2 |
| Provisional contributions (Akontobeiträge) | Set by the fund on the expected income of the year, usually the income of the last contribution decision | [AHVV art. 24](https://www.fedlex.admin.ch/eli/cc/63/1185_1183_1185/de) |
| Payment of Akontobeiträge | Quarterly, within 10 days after each quarter: 10 April, 10 July, 10 October, 10 January. Longer periods (up to a year) possible if annual contributions are CHF 3,000 or less | [AHVV art. 34](https://www.fedlex.admin.ch/eli/cc/63/1185_1183_1185/de); [sheet 2.02, no. 10](https://www.ahv-iv.ch/p/2.02.d) |
| Report a material change in income | Without delay, including when the closing shows the Akonto was too low | [AHVV art. 24 para. 4](https://www.fedlex.admin.ch/eli/cc/63/1185_1183_1185/de); [sheet 2.02, no. 8](https://www.ahv-iv.ch/p/2.02.d) |
| Final contributions (Beitragsverfügung) | After the final tax assessment; the fund nets them against the Akonto paid | [AHVV art. 25](https://www.fedlex.admin.ch/eli/cc/63/1185_1183_1185/de) |
| Balance due | Within 30 days of the invoice date (exactly 30 days, no extension) | [AHVV art. 25 para. 2](https://www.fedlex.admin.ch/eli/cc/63/1185_1183_1185/de); [sheet 2.02, no. 10](https://www.ahv-iv.ch/p/2.02.d) |
| Waive the allowance past reference age | By 31 December of the contribution year | [AHVV art. 6quater para. 5](https://www.fedlex.admin.ch/eli/cc/63/1185_1183_1185/de) |
| Report a liquidation gain after giving up the activity | By the end of the year after the gain | [sheet 2.02, no. 12](https://www.ahv-iv.ch/p/2.02.d) |
| Pillar 3a contribution for 2026 | Credited by 31 December 2026 | [ESTV circular 18a](https://www.estv.admin.ch/dam/de/sd-web/yQgKmvu80LEr/dbst-ks-2025-1-018a-dv-de.pdf), no. 5.1 |

Contributions count as paid when they reach the fund's account, not when the payment is ordered (AHVV art. 42 para. 1).

## Penalties and interest

- **Late interest of 5% a year**, regardless of fault or reminder, counted day by day with 30-day months and a 360-day year (AHVV art. 42 para. 2 and 3):
  - Akontobeiträge not received within 30 days after the quarter: interest from the day after the quarter ends (AHVV art. 41bis para. 1 let. a).
  - Balance after the final decision not paid within 30 days of the invoice: from the invoice date (let. e).
  - Akontobeiträge at least 25% below the final contributions: interest on the shortfall from 1 January after the year following the contribution year (let. f). For 2026, from 1 January 2028.
  - Contributions claimed for past years: from 1 January after the year they are owed for (let. b).
- **Credit interest of 5%** on contributions overpaid, from 1 January of the following year ([sheet 2.02](https://www.ahv-iv.ch/p/2.02.d), no. 13; AHVV art. 42).
- **Reminder fee** of CHF 20 to 200 (AHVV art. 34a). A payment deferral is possible in financial difficulty, but interest still runs (AHVV art. 34b).
- **Liquidation gain** reported late: interest runs back to the date the gain was made ([sheet 2.02](https://www.ahv-iv.ch/p/2.02.d), no. 12).
- **Unpaid contributions** are enforced by debt collection after a reminder (AHVG art. 15). The fund must claim them by decision within five years after the end of the year they are owed for; for the self-employed and non-employed this runs to at least one year after the year the tax assessment became final. A claim decided expires five years after the end of the year the decision became final (AHVG art. 16 para. 1 and 2).

## Cross-border points

- **Which country insures.** With EU and EFTA states, Switzerland applies Regulation (EC) 883/2004 through the Agreement on the Free Movement of Persons. A self-employed person is insured in one state only. Detail: `ch-cross-border`.
- **Posting.** A Swiss self-employed person working temporarily in an EU state, in the same line of work, stays insured in Switzerland for up to 24 months with an A1 certificate from their Swiss compensation fund. They must have had real business activity in Switzerland beforehand and normally at least two months of prior Swiss insurance ([BSV posting memo](https://www.bsv.admin.ch/dam/de/sd-web/nj5pRW599A3W/entsendungsmerkblatt-ch-eu.pdf)).
- **Non-treaty countries.** Income of a Swiss resident as owner or partner of a business or permanent establishment in a state without a social security agreement is exempt from Swiss contributions (AHVV art. 6ter let. a). The same applies to people taxed on expenditure (lump-sum taxation, see `ch-lump-sum`) for that income (let. c).
- **Double burden.** A person covered by a foreign state pension scheme can ask to be exempted where Swiss cover would be an unreasonable double burden (AHVV art. 3).

## Worked examples

### Example 1: designer with CHF 45,000 on the sliding scale

A self-employed graphic designer, aged 38, closes her 2026 accounts on 31 December. Her 2026 tax assessment shows net income from self-employment of CHF 41,800, after she deducted CHF 3,200 of own AHV/IV/EO contributions. She has no own capital in the business.

The fund adds back the CHF 3,200: 41,800 + 3,200 = CHF 45,000. Rounded down to the next CHF 100 it stays CHF 45,000. The law's method, grossing the reported income up to 100% at the band's rate (AHVG art. 9 para. 4), gives the same result here: 41,800 x 100 / (100 - 7.222) = CHF 45,053.79, rounded down to CHF 45,000. It falls in the band CHF 43,000 to under 45,500, so the total rate is 7.222%. Her 2026 contributions are 45,000 x 7.222% = CHF 3,249.90, plus the fund's administration cost of up to 5% of that.

Her Akontobeiträge for 2026 were set on the CHF 40,000 of her last decision: 40,000 x 6.728% = CHF 2,691.20 a year, CHF 672.80 a quarter, each paid by the 10th day after the quarter. The final decision bills the difference, CHF 558.70, payable within 30 days of the invoice. The Akonto reached about 83% of the final amount, so the 25% shortfall rule does not apply and no interest runs if she pays the invoice on time.

```oa-check
name: Self-employed CHF 45,000, 2026 sliding scale, Akonto and balance
inputs:
  assessed_net_income: 41800
  own_contributions_deducted: 3200
  own_capital: 0
  rate_43000_to_45500_pct: 7.222
  akonto_income: 40000
  rate_38000_to_40500_pct: 6.728
  shortfall_limit_pct: 75
steps:
  - income_before_contributions: assessed_net_income + own_contributions_deducted
  - contribution_income: floor(income_before_contributions / 100) * 100
  - grossed_up_at_band_rate: floor(assessed_net_income * 100 / (100 - rate_43000_to_45500_pct) / 100) * 100
  - final_contributions: contribution_income * rate_43000_to_45500_pct / 100
  - akonto_year: akonto_income * rate_38000_to_40500_pct / 100
  - akonto_quarter: akonto_year / 4
  - balance_due: final_contributions - akonto_year
  - akonto_share_pct: round(akonto_year / final_contributions * 100, 1)
  - above_shortfall_limit_by: akonto_share_pct - shortfall_limit_pct
expected:
  income_before_contributions: 45000.00
  contribution_income: 45000.00
  grossed_up_at_band_rate: 45000.00
  final_contributions: 3249.90
  akonto_year: 2691.20
  akonto_quarter: 672.80
  balance_due: 558.70
  akonto_share_pct: 82.8
  above_shortfall_limit_by: 7.8
```

### Example 2: consultant with CHF 120,000, full rate, own capital and pillar 3a

A self-employed consultant, aged 50, has no BVG pension fund. His 2026 profit before his own AHV/IV/EO contributions is CHF 120,000. He has CHF 150,000 of own capital in the business at 31 December 2026.

The edge case is the interest deduction. The 2026 rate is only published in January 2027, so this example assumes it equals the 2025 rate of 1%; replace it with the BSV figure when known. Interest: 150,000 x 1% = CHF 1,500. Contribution income: 120,000 - 1,500 = CHF 118,500, above CHF 60,500, so the full 10% applies: CHF 11,850 (AHV 8.1% = 9,598.50, IV 1.4% = 1,659, EO 0.5% = 592.50). The administration cost is up to 5% more, at most CHF 592.50.

Pillar 3a: we assume his Akonto deducted for tax in 2026 equals the final CHF 11,850. His earned income for 3a is the profit after own AHV contributions: 120,000 - 11,850 = CHF 108,150. Without a pension fund the limit is 20%: CHF 21,630, which is under the CHF 36,288 cap. He would need earned income of CHF 181,440 to reach the cap. The interest on own capital is an AHV-only deduction and does not change the 3a figure.

```oa-check
name: Self-employed CHF 120,000, full rate 2026, interest on own capital, pillar 3a without BVG
inputs:
  profit_before_own_contributions: 120000
  own_capital: 150000
  assumed_capital_interest_pct: 1
  full_rate_pct: 10
  ahv_pct: 8.1
  iv_pct: 1.4
  eo_pct: 0.5
  admin_cost_max_pct: 5
  pillar3a_share_pct: 20
  pillar3a_cap: 36288
steps:
  - capital_rounded: ceil(own_capital / 1000) * 1000
  - capital_interest: capital_rounded * assumed_capital_interest_pct / 100
  - contribution_income: floor((profit_before_own_contributions - capital_interest) / 100) * 100
  - contributions: contribution_income * full_rate_pct / 100
  - ahv: contribution_income * ahv_pct / 100
  - iv: contribution_income * iv_pct / 100
  - eo: contribution_income * eo_pct / 100
  - admin_cost_max: contributions * admin_cost_max_pct / 100
  - earned_income_for_3a: profit_before_own_contributions - contributions
  - pillar3a_limit: min(earned_income_for_3a * pillar3a_share_pct / 100, pillar3a_cap)
  - income_needed_for_cap: pillar3a_cap * 100 / pillar3a_share_pct
expected:
  capital_interest: 1500.00
  contribution_income: 118500.00
  contributions: 11850.00
  ahv: 9598.50
  iv: 1659.00
  eo: 592.50
  admin_cost_max: 592.50
  earned_income_for_3a: 108150.00
  pillar3a_limit: 21630.00
  income_needed_for_cap: 181440.00
```

## Ask the client first

1. Has the compensation fund accepted you as self-employed for this activity, and which fund (cantonal or professional)?
2. Your net income from self-employment for the year, the own AHV/IV/EO contributions you deducted, and the own capital in the business at 31 December.
3. Your Akonto for the year and whether the income has changed a lot since the last decision.
4. Your age, and whether you also have a salary from an employer.
5. Are you in a BVG pension fund (yours, your profession's or the substitute institution)? This sets the 3a limit.
6. Do you work in another country, or live abroad? This can move all contributions out of Switzerland.

## Sources

| Source | URL | Read on |
|---|---|---|
| Informationsstelle AHV/IV, Merkblatt 2.02 Beiträge der Selbstständigerwerbenden an die AHV, die IV und die EO, Stand 1. Januar 2026 | https://www.ahv-iv.ch/p/2.02.d | 2026-10-23 |
| Informationsstelle AHV/IV, Merkblatt 2.03 Beiträge der Nichterwerbstätigen an die AHV, die IV und die EO, Stand 1. Januar 2026 | https://www.ahv-iv.ch/p/2.03.d | 2026-10-23 |
| Informationsstelle AHV/IV, Merkblatt 2.01 Lohnbeiträge an die AHV, IV und EO, Stand 1. Januar 2026 | https://www.ahv-iv.ch/p/2.01.d | 2026-10-23 |
| Informationsstelle AHV/IV, Update Sozialversicherungen in der Schweiz, Änderungen 2026 | https://www.shop.ahv-iv.ch/data/docs/de/82816/Update-%C2%ABSozialversicherungen-in-der-Schweiz%C2%BB-Stand-1.-Januar-2026.pdf | 2026-10-23 |
| AHVG, SR 831.10, version of 1 January 2026, art. 3, 8, 9, 9bis, 10, 14, 15, 16, 34ter (and the version of 1 January 2027, art. 8) | https://www.fedlex.admin.ch/eli/cc/63/837_843_843/de | 2026-10-23 |
| AHVV, SR 831.101, version of 1 January 2026, art. 3, 6ter, 6quater, 17 to 25, 27, 28, 28bis, 34 to 34b, 41bis, 42 (and the version of 1 January 2027, art. 21) | https://www.fedlex.admin.ch/eli/cc/63/1185_1183_1185/de | 2026-10-23 |
| IVG, SR 831.20, version of 1 January 2026, art. 3 | https://www.fedlex.admin.ch/eli/cc/1959/827_857_845/de | 2026-10-23 |
| IVV, SR 831.201, version of 1 January 2025, art. 1bis (IV part of the sliding scale) | https://www.fedlex.admin.ch/eli/cc/1961/29_29_29/de | 2026-10-23 |
| EOG, SR 834.1, version of 1 June 2026, art. 27 | https://www.fedlex.admin.ch/eli/cc/1952/1021_1046_1050/de | 2026-10-23 |
| BVG, SR 831.40, version of 1 January 2025 (current), art. 4, 8, 44 | https://www.fedlex.admin.ch/eli/cc/1983/797_797_797/de | 2026-10-23 |
| BVV 3, SR 831.461.3, version of 1 January 2025 (current), art. 7, 7a | https://www.fedlex.admin.ch/eli/cc/1985/1778_1778_1778/de | 2026-10-23 |
| BSV, Mitteilungen an die AHV-Ausgleichskassen Nr. 504 (interest on own capital, 2025), 19 January 2026 | https://sozialversicherungen.admin.ch/de/d/21883/download | 2026-10-23 |
| BSV, Wichtige Masszahlen im Bereich der beruflichen Vorsorge 2025 und 2026 | https://www.bsv.admin.ch/dam/de/sd-web/GZplHByBJoFc/Internet_Masszahlenarticles_25_26_d.pdf | 2026-10-23 |
| BSV, Merkblatt Entsendung Schweiz-EU | https://www.bsv.admin.ch/dam/de/sd-web/nj5pRW599A3W/entsendungsmerkblatt-ch-eu.pdf | 2026-10-23 |
| ESTV, Kreisschreiben Nr. 18a, Steuerliche Behandlung von Vorsorgebeiträgen und -leistungen der Säule 3a, 22 December 2025 | https://www.estv.admin.ch/dam/de/sd-web/yQgKmvu80LEr/dbst-ks-2025-1-018a-dv-de.pdf | 2026-10-23 |

Not yet confirmed: the interest rate on own capital for contribution year 2026 (published by the BSV in January 2027; example 2 assumes the 2025 rate of 1%); the minimum contribution and non-employed table for 2027 (only the 2027 sliding-scale limits were read); how the 13th AHV pension will be financed after 2026; each fund's administration cost rate (up to 5%); the EO part of each sliding-scale band (the sheet gives only the total; the IV part is in IVV art. 1bis); the split of the CHF 530 minimum between IV and EO for the self-employed (AHVG art. 8 para. 2 sets only the AHV part, CHF 435).

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
