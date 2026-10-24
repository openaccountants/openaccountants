---
name: pl-zus-contributions
description: "Polish ZUS social contributions and the health contribution for the self-employed (jednoosobowa działalność gospodarcza) for 2026. Covers the standard base of PLN 5,652 (60% of the PLN 9,420 forecast wage), the rates (pension 19.52%, disability 8%, voluntary sickness 2.45%, accident 1.67%, Labour Fund 1.0% and Solidarity Fund 1.45%), the start relief (ulga na start), the 24-month preferential base of PLN 1,441.80, Mały ZUS Plus, the one-month contribution holiday, the annual cap of PLN 282,600, and the health contribution by tax form: 9% of income on the scale, 4.9% on the flat tax, both with a PLN 432.54 monthly minimum, and three fixed ryczałt bands (PLN 498.35, 830.58, 1,495.04). Also the DRA due on the 20th, the annual health reconciliation and 10.50% late interest. Trigger on: składki ZUS, ZUS przedsiębiorcy 2026, mały ZUS plus, ulga na start, preferencyjny ZUS, składka zdrowotna 2026. Out of scope: income tax in pl-income-tax; employees in pl-payroll; contract workers in pl-civil"
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/pl-zus-contributions"
  jurisdiction: "PL"
  tax_year: "2026"
  last_updated: "2026-10-23"
  trust_label: "Built by Michael Cutajar and the OpenAccountants team"
  review_status: "pending_review"
---

# Poland: ZUS and health contributions for the self-employed (2026)

Source-cited draft: not reviewed by an accountant, not for filing. Built by Michael Cutajar and the OpenAccountants team.

This skill covers what a sole trader in Poland pays to ZUS on themself in 2026: the social contributions (pension, disability, sickness, accident), the Labour Fund (Fundusz Pracy, FP) and Solidarity Fund (Fundusz Solidarnościowy, FS), and the health contribution (składka zdrowotna). It links to the other Poland skills and does not repeat them:

- [pl-income-tax](pl-income-tax.md): the income tax forms (scale, flat 19%, ryczałt) and how contributions reduce tax.
- [pl-payroll](pl-payroll.md): contributions an employer withholds and pays on employees.
- [pl-civil-law-contracts](pl-civil-law-contracts.md): ZUS on mandate contracts (umowa zlecenie), specific-task contracts and board fees.
- [pl-cross-border](pl-cross-border.md): residence, and which country insures a person who works in two states.

**Which text of the law.** Social Insurance System Act (ustawa o systemie ubezpieczeń społecznych, "ZUS Act"), consolidated text Dz.U. 2026 poz. 199; its later amendments (poz. 252, 426, 473, 734) were checked and do not change art. 17a-19, 22 or 47. Health Care Benefits Act ("Health Act"), consolidated text Dz.U. 2025 poz. 1461; its later amendments (2025 poz. 1537, 1739; 2026 poz. 26, 203, 791, 972, 986, 1007) do not change art. 79, 79a, 81 or 82. Entrepreneurs' Law (Prawo przedsiębiorców), Dz.U. 2025 poz. 1480, art. 18. Budget Act 2026, Dz.U. 2026 poz. 62, art. 24-26.

## Who this applies to

- **Sole traders.** A person running a registered business (pozarolnicza działalność gospodarcza) is compulsorily insured for pension, disability and accident from the day the business starts to the day it ends, except while it is suspended (ZUS Act art. 6 ust. 1 pkt 5, art. 12 ust. 1, art. 13 pkt 4). Sickness insurance is voluntary, on request (art. 11 ust. 2). The same rules reach partners of general, professional and limited partnerships, sole shareholders of a sp. z o.o. and people who help in the business (osoby współpracujące), but the reliefs below are for sole traders only.
- **Health contribution.** Every person in business pays it, including during the start relief (Health Act art. 66 ust. 1 pkt 1 lit. c, art. 79-81).
- **Someone who also has a job.** If the job pays at least the minimum wage (PLN 4,806 a month in 2026) the person is compulsorily insured only from the job; social contributions from the business become voluntary (ZUS Act art. 9 ust. 1 and 1a). The health contribution from the business is still due.
- **Pensioners.** A person with a set right to an old-age or disability pension pays pension and disability contributions from the business only voluntarily (ZUS Act art. 9 ust. 5). Accident and health stay compulsory.
- **Out of scope.** Farmers insured with KRUS, the tax card (karta podatkowa) and employees. See the sibling skills above.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Minimum wage (monthly) | PLN 4,806 | 2026 | https://www.zus.pl/baza-wiedzy/skladki-wskazniki-odsetki/skladki/wysokosc-skladek-na-ubezpieczenia-spoleczne |
| Forecast average wage | PLN 9,420 | 2026 | https://api.sejm.gov.pl/eli/acts/DU/2026/62/text.pdf (art. 24) |
| Standard minimum base: 60% of the forecast wage (ZUS Act art. 18 ust. 8) | PLN 5,652 a month | 2026 | https://www.zus.pl/baza-wiedzy/skladki-wskazniki-odsetki/skladki/wysokosc-skladek-na-ubezpieczenia-spoleczne |
| Pension (emerytalne) | 19.52% (PLN 1,103.27 on the standard base) | 2026 | https://api.sejm.gov.pl/eli/acts/DU/2026/199/text.pdf (art. 22) |
| Disability (rentowe) | 8.00% (PLN 452.16) | 2026 | same, art. 22 |
| Sickness (chorobowe), voluntary | 2.45% (PLN 138.47) | 2026 | same, art. 22 |
| Accident (wypadkowe), up to 9 insured persons | 1.67% (PLN 94.39) | 2026 | zus.pl page above |
| Labour Fund (FP) 1.0% + Solidarity Fund (FS) 1.45% | 2.45% (PLN 138.47), only if the base is at least the minimum wage | 2026 | https://api.sejm.gov.pl/eli/acts/DU/2026/62/text.pdf (art. 25, 26) |
| Total on the standard base, with sickness / without | PLN 1,926.76 / PLN 1,788.29 a month | 2026 | zus.pl page above |
| Preferential base: 30% of the minimum wage, first 24 months (art. 18a) | PLN 1,441.80 a month | 2026 | zus.pl page above |
| Total on the preferential base, with sickness / without (no FP or FS) | PLN 456.18 / PLN 420.86 a month | 2026 | zus.pl page above |
| Mały ZUS Plus: prior-year revenue limit | PLN 120,000 | 2026 | https://api.sejm.gov.pl/eli/acts/DU/2026/199/text.pdf (art. 18c) |
| Mały ZUS Plus base: floor and ceiling | PLN 1,441.80 to PLN 5,652 a month | 2026 | same, art. 18c ust. 2 |
| Annual cap on the pension and disability base (30 times the forecast wage) | PLN 282,600 | 2026 | https://api.sejm.gov.pl/eli/acts/MP/2025/1206/text.pdf |
| Monthly cap on the voluntary sickness base | PLN 23,550 | 2026 | zus.pl page above |
| Health, scale (art. 27 PIT): 9% of the prior month's income | minimum PLN 432.54 a month (Feb 2026 to Jan 2027) | 2026 | https://www.zus.pl/baza-wiedzy/skladki-wskazniki-odsetki/skladki/wysokosc-skladek-na-ubezpieczenia-spoleczne |
| Health, flat tax (art. 30c PIT): 4.9% of the prior month's income | minimum PLN 432.54 a month (9% of the minimum wage) | 2026 | https://api.sejm.gov.pl/eli/acts/DU/2025/1461/text.pdf (art. 79a) |
| Health, ryczałt, revenue to date up to PLN 60,000 | PLN 498.35 a month (9% of PLN 5,537.18) | 2026 | zus.pl page above |
| Health, ryczałt, revenue to date PLN 60,000 to 300,000 | PLN 830.58 a month (9% of PLN 9,228.64) | 2026 | zus.pl page above |
| Health, ryczałt, revenue to date over PLN 300,000 | PLN 1,495.04 a month (9% of PLN 16,611.55) | 2026 | zus.pl page above |
| Health, January 2026 (last month of the 2025 contribution year), scale and flat | minimum PLN 314.96 (9% of PLN 3,499.50) | 2025/26 | zus.pl page above |
| Late payment interest | 10.50% a year from 5 March 2026 | 2026 | https://api.sejm.gov.pl/eli/acts/MP/2026/269/text.pdf |

## The taxable base

**Social contributions.**
- **Standard.** The base is a declared amount of at least PLN 5,652 (ZUS Act art. 18 ust. 8). It is fixed for the year, not linked to profit.
- **Start relief (ulga na start).** A person starting a business for the first time, or again after at least 60 months, is not compulsorily insured for social contributions for 6 months from the start. The relief is not available to someone who works for a former employer doing what they did as an employee this year or last year (Entrepreneurs' Law art. 18 ust. 1). The person can opt out by registering for insurance (art. 18 ust. 2). Health is still due. During the relief the person has no pension, disability, sickness or accident cover.
- **Preferential base.** For the first 24 calendar months of the business (after the start relief, if used) the base is a declared amount of at least 30% of the minimum wage, PLN 1,441.80 (ZUS Act art. 18a ust. 1, 18aa ust. 3). It is not available to someone who ran a business in the 60 months before starting, or who works for a former employer as above (art. 18a ust. 2).
- **Mały ZUS Plus.** A sole trader whose business revenue last year was not over PLN 120,000 (pro rata if they traded part of the year) can use an income-linked base (art. 18c). The base is 0.5 times last year's average monthly income: annual income / days of activity x 30, then x 0.5 (art. 18c ust. 3-4). It is clamped between PLN 1,441.80 and PLN 5,652. For a ryczałt taxpayer, "income" is revenue x 0.5 (art. 18c ust. 12). Social contributions booked as costs are added back (art. 18c ust. 4a). Excluded: people who traded fewer than 60 days last year, people still entitled to the preferential base, people working for a former employer, people who last year also ran another non-farm activity such as a partnership (art. 8 ust. 6 pkt 2-5), and tax card users exempt from VAT (art. 18c ust. 11). From 1 January 2026 the limit is 36 months of use in each 60 months of business (art. 18c ust. 11a-11c, added by Dz.U. 2025 poz. 769).
- **FP and FS.** Due only when the monthly base is at least the minimum wage (Labour Market Act, Dz.U. 2025 poz. 620, art. 259 ust. 1), so not on the preferential base or a Mały ZUS Plus base under PLN 4,806. Not due for women aged 55 or over and men aged 60 or over (art. 261).
- **Contribution holiday.** Once a year a sole trader with no more than 10 insured persons, and revenue of no more than EUR 2 million in at least one of the last two years, can ask ZUS to waive one month of their own pension, disability and accident contributions (and sickness if they pay it). The request is made in the month before; the waiver is de minimis aid; health is not waived (ZUS Act art. 17a, 17b, 36d).
- **Annual cap.** Pension and disability contributions stop once the year's base reaches PLN 282,600 (art. 19 ust. 1). This matters only for someone who declares a high base.

**Health contribution (Health Act art. 79-81).** The base depends on the income tax form:
- **Scale and flat tax.** The monthly base is the business income of the previous month: revenue minus costs on PIT rules, less social contributions paid that month if they were not booked as costs (art. 81 ust. 2c). Scale: 9%. Flat tax: 4.9% (art. 79a). In both cases the monthly base is at least the minimum wage, so the contribution is at least PLN 432.54 from February 2026 to January 2027. Since 1 February 2025 revenue and costs from selling fixed assets are left out of the base unless the person chooses to include them (art. 81 ust. 2zd pkt 3 and 2ze, added by Dz.U. 2024 poz. 1915). The same act set a lower floor of 75% of the minimum wage only for the contribution year February 2025 to January 2026; from February 2026 the floor is 100% again.
- **Ryczałt.** A fixed monthly base by revenue earned since the start of the year: 60%, 100% or 180% of the Q4 2025 average wage of PLN 9,228.64 (art. 81 ust. 2f). Revenue is reduced by social contributions not already deducted (art. 81 ust. 2g).
- **Annual reconciliation.** For scale and flat tax the year's base is the year's business income (art. 81 ust. 2). The difference against monthly payments is shown in the DRA for April of the following year and paid by 20 May; an overpayment is refunded on a request filed through PUE ZUS within one month of the 30 April PIT return deadline; a late request is not considered (art. 81 ust. 2i, 2m-2o).
- **Tax relief for health.** Scale: none. Flat tax: deductible up to PLN 14,100 in 2026. Ryczałt: 50% of health paid reduces revenue. See [pl-income-tax](pl-income-tax.md).

## Deadlines and filing

| What | When | Rule |
|---|---|---|
| Register with ZUS (ZUA or ZZA for health only) | within 7 days of the start of insurance | ZUS Act art. 36 ust. 4 |
| Monthly DRA and payment of all contributions (sole trader without legal personality) | 20th of the following month | ZUS Act art. 47 ust. 1 pkt 4 |
| Mały ZUS Plus data (last year's tax form, revenue, income, base) | in the DRA for January, or for the first month of activity | ZUS Act art. 18c ust. 9 |
| Annual health reconciliation for 2026 (scale and flat tax) | in the DRA for April 2027, extra due by 20 May 2027 | Health Act art. 81 ust. 2k-2l |
| Contribution holiday request | in the month before the waived month | ZUS Act art. 36d |

A person who pays only for themself files only the DRA, not personal reports (ZUS Act art. 47 ust. 2). Payment goes to the individual contribution account (NRS) given by ZUS.

## Penalties and interest

- **Late payment interest.** Charged on the Tax Ordinance rules (ZUS Act art. 23 ust. 1): 200% of the NBP lombard rate plus 2 points, at least 8% (Tax Ordinance art. 56 § 1). With the lombard rate at 4.25% from 5 March 2026 that is 10.50% a year (M.P. 2026 poz. 269). The reduced 50% rate of art. 56a does not apply to contributions. Interest is not charged when it would be no more than 1% of the minimum wage, PLN 48.06 (ZUS Act art. 23 ust. 1a).
- **Additional fee.** For contributions not paid or paid too low, ZUS can charge an extra fee of up to 100% of the unpaid amount (ZUS Act art. 24 ust. 1a).
- **Health assessed by default.** If a scale or flat-tax payer does not report monthly income, ZUS sets the base at the minimum wage for that month; for ryczałt at 60% of the average wage (Health Act art. 81 ust. 2zc).

## Cross-border points

- **Which country insures.** Inside the EU, EEA and Switzerland, Regulation (EC) No 883/2004 decides. A person who is self-employed only in Poland is insured in Poland. A person who works in two states is usually insured where they live if they do a substantial part of their work there (art. 13). A Polish sole trader working temporarily abroad keeps Polish cover with an A1 certificate (art. 12(2)). If another state insures the person, no Polish ZUS or health contribution is due on the business.
- **Foreign contributions and tax.** Compulsory social contributions paid in another EU or EEA state or Switzerland can be deducted from Polish taxable income (PIT Act art. 26 ust. 1 pkt 2a). See [pl-income-tax](pl-income-tax.md).
- **Outside the EU.** Poland's bilateral social security agreements decide; check the agreement for the other country. Residence for income tax is in [pl-cross-border](pl-cross-border.md).

## Worked examples

### Example 1: established sole trader on the scale, standard base

Anna has run her business for six years. She pays tax on the scale (PIT-36), has no job and does not take voluntary sickness insurance. She is 40, so FP and FS are due. In September 2026 her business income for August (revenue minus costs) was PLN 12,000. She deducts social contributions from income, not as costs.

Social contributions on the PLN 5,652 base: pension PLN 1,103.27, disability PLN 452.16, accident PLN 94.39, together PLN 1,649.82. FP and FS add PLN 138.47, so she pays PLN 1,788.29 to ZUS for social and funds. The health base for September is August income less the social contributions paid (PLN 12,000 - 1,649.82 = PLN 10,350.18). Health at 9% is PLN 931.52, above the PLN 432.54 minimum. Total due by 20 October 2026: PLN 2,719.81.

```oa-check
name: PL ZUS 2026, standard base, scale, no sickness, prior-month income PLN 12,000
inputs:
  base: 5652
  prior_month_income: 12000
  health_minimum: 432.54
steps:
  - pension: round(base * 0.1952, 2)
  - disability: round(base * 0.08, 2)
  - accident: round(base * 0.0167, 2)
  - fp_fs: round(base * 0.0245, 2)
  - social: pension + disability + accident
  - health_base: prior_month_income - social
  - health: max(round(health_base * 0.09, 2), health_minimum)
  - total: social + fp_fs + health
expected:
  pension: 1103.27
  disability: 452.16
  accident: 94.39
  social: 1649.82
  fp_fs: 138.47
  health: 931.52
  total: 2719.81
```

### Example 2: Mały ZUS Plus on the flat tax, health at the minimum

Piotr traded for all of 2025 (365 days). His 2025 revenue was PLN 90,000, under the PLN 120,000 limit, and his income was PLN 54,000. He has never used Mały ZUS Plus and has no former-employer issue. He deducted social contributions from income, so there is no add-back. He chose the flat tax (PIT-36L) and does not take sickness insurance.

Average monthly income: 54,000 / 365 x 30 = PLN 4,438.36. The base is half of that, PLN 2,219.18, inside the PLN 1,441.80 to 5,652 range. Pension PLN 433.18, disability PLN 177.53, accident PLN 37.06: PLN 647.77 a month. The base is below the PLN 4,806 minimum wage, so no FP or FS. In a month after a prior month with income of PLN 6,000, the flat-tax health contribution would be 4.9% of (6,000 - 647.77) = PLN 262.26, but the minimum is PLN 432.54, so he pays the minimum. Total for that month: PLN 1,080.31.

```oa-check
name: PL ZUS 2026, Mały ZUS Plus, flat tax, health floor applies
inputs:
  income_2025: 54000
  days_active: 365
  floor_base: 1441.80
  cap_base: 5652
  prior_month_income: 6000
  health_minimum: 432.54
steps:
  - avg_month: round(income_2025 / days_active * 30, 2)
  - base: clamp(round(avg_month * 0.5, 2), floor_base, cap_base)
  - pension: round(base * 0.1952, 2)
  - disability: round(base * 0.08, 2)
  - accident: round(base * 0.0167, 2)
  - social: pension + disability + accident
  - health_calc: round((prior_month_income - social) * 0.049, 2)
  - health: max(health_calc, health_minimum)
  - total: social + health
expected:
  avg_month: 4438.36
  base: 2219.18
  social: 647.77
  health_calc: 262.26
  health: 432.54
  total: 1080.31
```

## Ask the client first

1. When did the business start, did they run a business in the 60 months before, and do they work for a former employer in the same line of work? (Start relief, preferential base and Mały ZUS Plus all turn on this.)
2. Which income tax form do they use in 2026: scale, flat 19% or ryczałt? (It sets the health rate and base.)
3. Last year's business revenue and income, and the days traded; months of Mały ZUS Plus already used.
4. Do they also have a job paying at least PLN 4,806 a month, or a pension?
5. Do they want voluntary sickness insurance, and what is their age (FP and FS)?
6. Do they work in another EU state, or hold an A1 from another state?

## Sources

| Source | URL | Read on |
|---|---|---|
| ZUS Act, consolidated text Dz.U. 2026 poz. 199 (art. 6, 9, 11-13, 17a, 17b, 18, 18a, 18aa, 18c, 19, 22-24, 36, 36d, 47) | https://api.sejm.gov.pl/eli/acts/DU/2026/199/text.pdf | 2026-10-23 |
| ZUS Act amendments after consolidation (poz. 252, 426, 473, 734; none touch the articles used) | https://api.sejm.gov.pl/eli/acts/DU/2026/199 | 2026-10-23 |
| Health Care Benefits Act, consolidated text Dz.U. 2025 poz. 1461 (art. 66, 79, 79a, 81, 82) | https://api.sejm.gov.pl/eli/acts/DU/2025/1461/text.pdf | 2026-10-23 |
| Act amending the Health Care Benefits Act, Dz.U. 2024 poz. 1915 (fixed assets left out of the base; 75% floor for 2025 only) | https://api.sejm.gov.pl/eli/acts/DU/2024/1915/text.pdf | 2026-10-23 |
| Entrepreneurs' Law, Dz.U. 2025 poz. 1480 (art. 18, start relief) | https://api.sejm.gov.pl/eli/acts/DU/2025/1480/text.pdf | 2026-10-23 |
| Budget Act 2026, Dz.U. 2026 poz. 62 (art. 24-26) | https://api.sejm.gov.pl/eli/acts/DU/2026/62/text.pdf | 2026-10-23 |
| Labour Market Act, Dz.U. 2025 poz. 620 (art. 259, 261) | https://api.sejm.gov.pl/eli/acts/DU/2025/620/text.pdf | 2026-10-23 |
| Minister of Family notice on the 2026 annual cap and forecast wage, M.P. 2025 poz. 1206 | https://api.sejm.gov.pl/eli/acts/MP/2025/1206/text.pdf | 2026-10-23 |
| ZUS, contributions of the self-employed in 2026 (bases, amounts, health bands and minimum) | https://www.zus.pl/baza-wiedzy/skladki-wskazniki-odsetki/skladki/wysokosc-skladek-na-ubezpieczenia-spoleczne | 2026-10-23 |
| Tax Ordinance, Dz.U. 2026 poz. 622 (art. 56, 56a) | https://api.sejm.gov.pl/eli/acts/DU/2026/622/text.pdf | 2026-10-23 |
| Minister of Finance notice on late payment interest, M.P. 2026 poz. 269 | https://api.sejm.gov.pl/eli/acts/MP/2026/269/text.pdf | 2026-10-23 |
| NBP base rates (lombard 4.25% from 5 March 2026) | https://static.nbp.pl/dane/stopy/stopy_procentowe.xml | 2026-10-23 |
| PIT Act, Dz.U. 2026 poz. 592 (art. 26 ust. 1 pkt 2a) | https://api.sejm.gov.pl/eli/acts/DU/2026/592/text.pdf | 2026-10-23 |
| Regulation (EC) No 883/2004 on social security coordination | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32004R0883 | 2026-10-23 |

Not yet confirmed: the minimum wage regulation (Dz.U. 2025 poz. 1242) is an image-only PDF, so PLN 4,806 is taken from zus.pl, not from the regulation text. The 1.67% accident rate applies to payers with up to 9 insured persons; others use their own rate from the Accident Insurance Act.

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

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-10-23. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `pl-zus-contributions` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/pl-zus-contributions. If neither is available, confirm every figure against the official source pages cited above before relying on it.
