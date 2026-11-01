---
name: be-social-contributions
description: "Belgian social contributions for the self-employed (sociale bijdragen zelfstandigen / cotisations sociales des indépendants) for contribution year 2026, under Royal Decree No. 38 and the RSVZ / INASTI 2026 amounts. Covers the 20.50% rate up to EUR 75,024.54 and 14.16% up to EUR 110,562.42, the minimum quarterly contribution of EUR 890.42 and maximum of EUR 5,103.05, provisional contributions on income of three years earlier revalued by 1.07236269, regularisation, starters (primostarters), secondary activity, assisting spouses, student-entrepreneurs and pensioners, late payment increases, and VAPZ at 8.50% / 9.78% from 2026. Trigger on: sociale bijdragen, cotisations sociales indépendant, RSVZ, INASTI, socialeverzekeringsfonds, bijberoep, primostarter, VAPZ, PLCI. Out of scope: be-income-tax (income tax on self-employed profits), belgium-payroll (employees), be-corporate-tax (the annual company contribution), be-cross-border."
version: 2.2
jurisdiction: BE
tax_year: 2026
last_updated: 2026-10-31
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Belgium: social contributions for the self-employed (contribution year 2026) v2.1

> **General reference only.** This skill is general tax reference material for AI-assisted work. It has not been reviewed for any person's facts. Do not rely on it to pay, plan or take a position without review by a qualified professional in Belgium.

This skill computes the quarterly social contributions a self-employed person pays to a social insurance fund (socialeverzekeringsfonds) in 2026. Related skills:

- Income tax on the same profits, where these contributions are deductible: `be-income-tax`
- Employees and employer RSZ / ONSS: `belgium-payroll`
- Company directors working through a company, and the annual company contribution: `be-corporate-tax`
- Which country's social security applies to cross-border work: `be-cross-border`

## Who this applies to

- **Self-employed in main occupation (hoofdberoep)**: anyone working in Belgium as self-employed who is not in one of the categories below. This includes a company director (bestuurder, zaakvoerder) paid by the company.
- **Self-employed in secondary occupation (bijberoep)**: someone whose self-employed work sits beside another main occupation, usually employment; the fund checks the conditions. Lower thresholds apply.
- **Assisting spouses and legal cohabitants (meewerkende echtgenoot)**: maxi-statute (full cover) or mini-statute (sickness and invalidity only, on the helped person's income).
- **Student-entrepreneurs, pensioners and people above pension age**: their own thresholds and rates.

Out: employees (`belgium-payroll`), and people insured in another EU state under Regulation 883/2004 (`be-cross-border`).

## Rates, bands and thresholds

All amounts are from the RSVZ table "Bijdragen 2026" (January 2026), reference year 2023, revaluation coefficient 1.07236269.

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Main occupation, rate band 1 | 20.50% on professional income up to EUR 75,024.54, on a minimum income of EUR 17,374.08 | 2026 | [RSVZ, Bijdragen 2026, section 1](https://www.rsvz.be/sites/rsvz/files/2024-01/folder_sociale_bijdragen.pdf) |
| Main occupation, rate band 2 | 14.16% on income above EUR 75,024.54 up to EUR 110,562.42; nothing above | 2026 | [RSVZ, Bijdragen 2026, section 1](https://www.rsvz.be/sites/rsvz/files/2024-01/folder_sociale_bijdragen.pdf) |
| Main occupation, minimum and maximum | Minimum EUR 890.42 a quarter; maximum EUR 5,103.05 a quarter | 2026 | [RSVZ, Bijdragen 2026, section 1](https://www.rsvz.be/sites/rsvz/files/2024-01/folder_sociale_bijdragen.pdf) |
| Starter, provisional | EUR 890.42 a quarter until the end of the third full calendar year; EUR 771.90 for a primostarter's first quarter | 2026 | [RSVZ, Bijdragen 2026, section 1, A.1](https://www.rsvz.be/sites/rsvz/files/2024-01/folder_sociale_bijdragen.pdf) |
| Primostarter, reduced (first 4 quarters, on request) | EUR 459.82 a quarter if estimated income does not exceed EUR 8,972.07; above that, 20.50% / 14.16%. First-quarter discount EUR 118.52. Final minimum: EUR 341.30 first quarter, EUR 459.82 other quarters | 2026 | [RSVZ, Bijdragen 2026, section 1, A.3 and B.1](https://www.rsvz.be/sites/rsvz/files/2024-01/folder_sociale_bijdragen.pdf) |
| Secondary occupation | Nothing below EUR 1,922.16 income; from EUR 1,922.16, 20.50% / 14.16%; minimum EUR 98.51 a quarter, maximum EUR 5,103.05 | 2026 | [RSVZ, Bijdragen 2026, section 3](https://www.rsvz.be/sites/rsvz/files/2024-01/folder_sociale_bijdragen.pdf) |
| Equated with secondary occupation (art. 37 ARS) | Nothing below EUR 1,922.16; 20.50% up to EUR 9,101.26, maximum EUR 466.44 a quarter; main-occupation rules from EUR 9,101.26 | 2026 | [RSVZ, Bijdragen 2026, section 4](https://www.rsvz.be/sites/rsvz/files/2024-01/folder_sociale_bijdragen.pdf) |
| Student-entrepreneur | Nothing below EUR 8,687.04; 20.50% on the part from EUR 8,687.04, maximum EUR 445.21 a quarter; main-occupation rules from EUR 17,374.08 | 2026 | [RSVZ, Bijdragen 2026, section 5](https://www.rsvz.be/sites/rsvz/files/2024-01/folder_sociale_bijdragen.pdf) |
| Assisting spouse, maxi-statute | 20.50% / 14.16% on a minimum income of EUR 7,632.44; minimum EUR 391.16, maximum EUR 5,103.05 a quarter | 2026 | [RSVZ, Bijdragen 2026, section 2, §1](https://www.rsvz.be/sites/rsvz/files/2024-01/folder_sociale_bijdragen.pdf) |
| Assisting spouse, mini-statute | 0.79% / 0.51% of the helped person's income; minimum EUR 34.31, maximum EUR 193.48 a quarter | 2026 | [RSVZ, Bijdragen 2026, section 2, §2](https://www.rsvz.be/sites/rsvz/files/2024-01/folder_sociale_bijdragen.pdf) |
| Above pension age with a retirement pension | Nothing below EUR 3,844.32; 14.70% up to EUR 75,024.54 and 14.16% to EUR 110,562.42; minimum EUR 141.28, maximum EUR 4,015.19 a quarter | 2026 | [RSVZ, Bijdragen 2026, section 8, §1](https://www.rsvz.be/sites/rsvz/files/2024-01/folder_sociale_bijdragen.pdf) |
| Revaluation of reference income | Income of 2023 x 1.07236269 for provisional 2026 contributions | 2026 | [RSVZ, Bijdragen 2026, cover page](https://www.rsvz.be/sites/rsvz/files/2024-01/folder_sociale_bijdragen.pdf) |
| Late payment increases | 3% of the unpaid part at the end of each quarter it stays unpaid; plus a one-off 7% on 1 January of the next year on contributions first claimed in the year and still unpaid; never on increases | 2026 | [RSVZ, Wat als ik mijn bijdragen niet betaal?](https://www.rsvz.be/nl/faq/wat-als-ik-mijn-bijdragen-niet-betaal) |
| VAPZ maximum rate | Ordinary VAPZ 8.50% of the reference income (was 8.17%); social VAPZ 9.78% (was 9.40%); secondary occupation can join from EUR 1,922.16 income three years earlier | From 2026 | [RSVZ, Wijzigingen VAPZ, 13 October 2026](https://www.rsvz.be/nl/nieuws/wijzigingen-vapz) |
| Tax treatment | Personal social contributions, including VAPZ, are deductible professional expenses | Income 2026 | [Art. 52, 7° and 7°bis WIB 92](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/e2123748-b2c4-49ab-8b2d-5eacb94fbc34) |

On top of the contributions, the social insurance fund charges management costs (beheerskosten) to cover its expenses. The rate is set by each fund; ask the fund.

## The taxable base

- **What income counts.** Professional income from the self-employed activity: gross professional income less professional expenses and professional losses, as set by the tax administration (RSVZ). Social contributions paid are themselves professional expenses for income tax (art. 52, 7° WIB 92).
- **Final contributions use the income of the year itself.** The 2026 contributions are finally based on 2026 income. The fund learns that income only when the tax administration reports it, usually one or two years later.
- **Provisional contributions use income of three years earlier.** For 2026, the 2023 income revalued by 1.07236269. Someone who was not self-employed then pays the legal provisional amounts (EUR 890.42 a quarter in main occupation).
- **Regularisation.** When the 2026 income is known, the fund recomputes the final contributions and asks for more or refunds the difference.
- **Paying more or less in advance.** You can pay higher provisional contributions to avoid a large regularisation. Lower provisional contributions need the fund's agreement on objective evidence; if the real income turns out higher, the fund charges the supplement plus increases. The reduced amount never goes below the minimum.
- **Computation, main occupation.** Annual contributions = 20.50% x min(income, 75,024.54) + 14.16% x (min(income, 110,562.42) - 75,024.54) if positive, with the income taken as at least EUR 17,374.08. Quarterly = annual / 4.

## Deadlines and filing

| What | When | Source |
|---|---|---|
| Quarterly contributions | On the fund's account by the last day of each quarter (31 March, 30 June, 30 September, 31 December 2026) | [RSVZ, Wat als ik mijn bijdragen niet betaal?](https://www.rsvz.be/nl/faq/wat-als-ik-mijn-bijdragen-niet-betaal) |
| VAPZ for 2026 | Paid within 2026; those who already paid for 2026 can top up to the new 8.50% / 9.78% maximum | [RSVZ, Wijzigingen VAPZ](https://www.rsvz.be/nl/nieuws/wijzigingen-vapz) |
| Limitation period | The fund has 5 years from 1 January after the contribution year to claim; the starter supplement runs to 1 January of the 8th year after the start | [RSVZ, Wat als ik mijn bijdragen niet betaal?](https://www.rsvz.be/nl/faq/wat-als-ik-mijn-bijdragen-niet-betaal) |

## Penalties and interest

- **3% per quarter.** If the contribution is not fully on the fund's account by the last day of the quarter, the fund adds 3% of the unpaid part, and again at the end of every later quarter while it stays unpaid.
- **7% once.** Contributions first claimed in a year and still unpaid at year end get a one-off extra 7% on 1 January of the next year.
- **No increases on increases.** They apply only to the principal.
- **Waiver.** You can ask the fund to waive the increases once the principal for that quarter is paid, for force majeure, good faith on your status, or a hardship case. A first late payment in your career, for one quarter and paid within 8 days, can be waived on request without detailed reasons. A missed letter or an accountant's error is not a valid reason.
- **Underestimated provisional contributions.** A supplement plus increases at regularisation.

## Cross-border points

- **One country's social security.** Under EU Regulation 883/2004, a person working in more than one member state pays contributions in one state only; an A1 certificate shows which. See `be-cross-border`.
- **Self-employed in Belgium, employed abroad.** The person is generally insured in the state of employment; check the A1 before charging Belgian contributions.
- **Contributions paid abroad** are not Belgian social contributions for this skill; the income tax deduction then depends on art. 52, 7° and the treaty.

## Worked examples

### Example 1: established, main occupation, final contributions

Facts: a self-employed designer in main occupation since 2019. Final professional income for 2026: EUR 45,000.

1. Income is between the minimum income (EUR 17,374.08) and EUR 75,024.54, so only band 1 applies.
2. Annual contributions: 20.50% x 45,000 = EUR 9,225.00.
3. Quarterly: EUR 2,306.25, above the EUR 890.42 minimum and below the EUR 5,103.05 maximum.
4. The fund's management costs come on top.

```oa-check
name: Main occupation, final 2026 contributions on income EUR 45,000
inputs:
  income: 45000
  min_income: 17374.08
  band1_top: 75024.54
  ceiling: 110562.42
steps:
  - base: max(income, min_income)
  - band1: min(base, band1_top) * 0.205
  - band2: max(min(base, ceiling) - band1_top, 0) * 0.1416
  - annual: band1 + band2
  - quarterly: round(annual / 4, 2)
expected:
  base: 45000
  annual: 9225.00
  quarterly: 2306.25
```

### Example 2: provisional contributions on 2023 income, then a refund at regularisation

Facts: a self-employed consultant in main occupation. Professional income 2023: EUR 80,000. The fund sets 2026 provisional contributions on 2023 income revalued. Final income for 2026 turns out to be EUR 60,000. The client did not ask for a reduction.

1. Revalued 2023 income: 80,000 x 1.07236269 = EUR 85,789.02.
2. Band 1: 20.50% x 75,024.54 = 15,380.03. Band 2: 14.16% x (85,789.02 - 75,024.54) = 1,524.25. Annual provisional EUR 16,904.28.
3. Quarterly provisional: EUR 4,226.07, under the EUR 5,103.05 maximum.
4. Final 2026 contributions: 20.50% x 60,000 = EUR 12,300.00.
5. Regularisation: the fund refunds 16,904.28 - 12,300.00 = EUR 4,604.28, once the tax administration reports the 2026 income. Had the client expected this, a reduced provisional amount could have been requested from the fund with evidence.

```oa-check
name: Provisional 2026 contributions on revalued 2023 income, then regularisation
inputs:
  income_2023: 80000
  revaluation: 1.07236269
  income_2026: 60000
  band1_top: 75024.54
  ceiling: 110562.42
steps:
  - revalued: round(income_2023 * revaluation, 2)
  - prov_band1: round(min(revalued, band1_top) * 0.205, 2)
  - prov_band2: round(max(min(revalued, ceiling) - band1_top, 0) * 0.1416, 2)
  - provisional_annual: prov_band1 + prov_band2
  - provisional_quarterly: round(provisional_annual / 4, 2)
  - final_annual: min(income_2026, band1_top) * 0.205 + max(min(income_2026, ceiling) - band1_top, 0) * 0.1416
  - refund: provisional_quarterly * 4 - final_annual
expected:
  revalued: 85789.02
  prov_band1: 15380.03
  prov_band2: 1524.25
  provisional_annual: 16904.28
  provisional_quarterly: 4226.07
  final_annual: 12300.00
  refund: 4604.28
```

## Ask the client first

1. Main or secondary occupation? Any employment, and at what fraction of full-time?
2. When did the activity start (first three calendar years, primostarter)?
3. Professional income of 2023 and the expected income for 2026.
4. Which social insurance fund, and its management cost rate?
5. VAPZ: ordinary or social, and what was already paid for 2026?
6. Any work or insurance in another country (A1 certificate)?

## Sources

| Source | URL | Read on |
|---|---|---|
| RSVZ, Bijdragen 2026, main categories (January 2026) | https://www.rsvz.be/sites/rsvz/files/2024-01/folder_sociale_bijdragen.pdf | 2026-10-23 |
| RSVZ, publication page for the 2026 contribution amounts | https://www.rsvz.be/nl/publicaties/sociale-bijdragen | 2026-10-23 |
| RSVZ, Hoeveel sociale bijdragen moet ik betalen? | https://www.rsvz.be/nl/faq/hoeveel-sociale-bijdragen-moet-ik-betalen | 2026-10-23 |
| RSVZ, Wat als ik mijn bijdragen niet betaal? | https://www.rsvz.be/nl/faq/wat-als-ik-mijn-bijdragen-niet-betaal | 2026-10-23 |
| RSVZ, Wijzigingen VAPZ (13 October 2026) | https://www.rsvz.be/nl/nieuws/wijzigingen-vapz | 2026-10-23 |
| Fisconetplus, art. 52 WIB 92 (income 2026), deductibility | https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/e2123748-b2c4-49ab-8b2d-5eacb94fbc34 | 2026-10-23 |

Not yet confirmed: the management cost rates of the social insurance funds and their legal maximum; the VAPZ maximum in euro for 2026; the 2026 amounts for self-employed with an early retirement pension or a survivor's pension only (sections 6 and 7 of the RSVZ table were not worked into this skill); the annual company contribution (vennootschapsbijdrage) for 2026.

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
