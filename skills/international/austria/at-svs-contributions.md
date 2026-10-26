---
name: at-svs-contributions
description: "Austrian social insurance for the self-employed, tax year 2026, collected by the SVS: pension (18.5% GSVG, 20% FSVG), health (6.8%), accident insurance (EUR 12.95 a month) and the Selbständigenvorsorge (1.53%), for trade licence holders (Gewerbetreibende), Neue Selbständige and FSVG freelancers. Covers the 2026 minimum base (EUR 551.10 a month) and maximum base (EUR 8,085 a month, EUR 97,020 a year), the provisional base for new businesses and from year four (factor 1.181), the Nachbemessung, quarterly due dates, the Versicherungsgrenze and the small business exemption (EUR 6,613.20 income, EUR 55,000 turnover), the health contribution credit, ASVG overlap and deductibility. Trigger on: SVS, GSVG, FSVG, Beitragsvorschreibung, Nachbemessung, Neue Selbständige, Kleinunternehmer SVS, Selbständigenvorsorge. Out of scope: employees and employers (at-payroll-and-social-insurance), income tax (at-income-tax), farmers under the BSVG, A1 cases (at-cross-border)."
version: 2.1
jurisdiction: AT
tax_year: 2026
last_updated: 2026-10-26
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
drafted_by: OpenAccountants
approved_by: pending
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# SVS social insurance for the self-employed in Austria (GSVG and FSVG, 2026)

> **Source-cited draft: not reviewed by an accountant.** This skill is general tax reference material for AI-assisted work. It has not been reviewed for any person's facts. Do not rely on it to file or pay without review by a Steuerberater or another licensed adviser in Austria.

**Sibling skills.** Income tax, including how SVS contributions reduce profit, is in [at-income-tax](at-income-tax.md). Employee and employer contributions (ASVG) are in [at-payroll-and-social-insurance](at-payroll-and-social-insurance.md). Work in more than one country is in [at-cross-border](at-cross-border.md). The VAT small business exemption is in [at-vat-return](at-vat-return.md).

## Who this applies to

- **Gewerbetreibende**: holders of a trade licence and the managing partners of trading companies (GSVG § 2 Abs 1 Z 1 to 3). Insurance starts with the licence.
- **Neue Selbständige**: self-employed people with business income under EStG § 22 Z 1 to 3 and 5 or § 23 and no trade licence, for example consultants, writers and IT contractors (GSVG § 2 Abs 1 Z 4). They are insured only when their yearly income from all GSVG activities is above the Versicherungsgrenze (EUR 6,613.20 in 2026). The test is the same whether or not they also have a job or a pension.
- **FSVG freelancers**: doctors, pharmacists, patent attorneys and civil engineers pay SVS pension insurance at 20% under the FSVG.
- **Not covered here**: farmers (BSVG, their own rates and the Einheitswert base), employees (ASVG), and people in more than one EU/EEA state or Switzerland (Regulation 883/2004; one state's law applies).
- **Stop rule**: if you do not know which group the client is in, stop. The group decides the rates, the start of insurance and the exemptions.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source URL |
|---|---|---|---|
| Pension insurance, GSVG (paid by the insured; the Bund adds 4.3%) | 18.5% of the base | 2026 | GSVG § 27 Abs 2, https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10008422 |
| Pension insurance, FSVG | 20% of the base | 2026 | https://www.svs.at/cdscontent/?contentid=10007.816638&portal=svsportal |
| Health insurance (paid by the insured; the Bund adds 0.85%) | 6.8% of the base | 2026 | GSVG § 27 Abs 1a, RIS link above |
| Accident insurance, fixed per month | EUR 12.95 | 2026 | ASVG § 74 Abs 1 Z 1 with BGBl. II Nr. 263/2025, https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10008147 |
| Selbständigenvorsorge, share of the provisional health base | 1.53% | 2026 | BMSVG § 52 Abs 1, https://www.ris.bka.gv.at/Dokumente/Bundesnormen/NOR40210216/NOR40210216.html |
| Minimum base per month (Mindestbeitragsgrundlage, GSVG § 25 Abs 4 links it to ASVG § 5 Abs 2) | EUR 551.10 | 2026 | https://www.svs.at/cdscontent/load?contentid=10008.763406&version=1672393252 |
| Maximum base per month (GSVG § 25 Abs 5) | EUR 8,085.00 | 2026 | same SVS contribution sheet |
| Maximum base per year | EUR 97,020.00 | 2026 | https://www.svs.at/cdscontent/?contentid=10007.816635&portal=svsportal |
| Minimum base per year of full insurance | EUR 6,613.20 | 2026 | same SVS page |
| Pension at the minimum and maximum base, GSVG | EUR 101.95 / EUR 1,495.73 a month | 2026 | SVS contribution sheet |
| Pension at the minimum and maximum base, FSVG | EUR 110.22 / EUR 1,617.00 a month | 2026 | SVS contribution sheet |
| Health at the minimum and maximum base | EUR 37.48 / EUR 549.79 a month | 2026 | SVS contribution sheet |
| Revaluation factor for 2023 income used for 2026 provisional bases (Aufwertungszahlen 2024 1.035 x 2025 1.063 x 2026 1.073) | 1.181 | 2026 | GSVG § 25a Abs 1 Z 2; ASVG § 108a with BGBl. II Nr. 263/2025; https://www.svs.at/cdscontent/?contentid=10007.816634&portal=svsportal |
| Versicherungsgrenze, Neue Selbständige, per year | EUR 6,613.20 | 2026 | https://www.svs.at/cdscontent/?contentid=10007.816855&portal=svsportal |
| Small business exemption: income limit per year (twelve times the minimum base) | EUR 6,613.20 | 2026 | GSVG § 4 Abs 1 Z 7; https://www.svs.at/cdscontent/?contentid=10007.816718&portal=svsportal |
| Small business exemption: turnover limit from all business (UStG § 6 Abs 1 Z 27 limit) | EUR 55,000.00 | 2026 | same |
| Surcharge when insurance is found later from the tax assessment | 9.3% of pension and health contributions | 2026 | GSVG § 35; https://www.svs.at/cdscontent/?contentid=10007.816855&portal=svsportal |
| Health contribution credit (Gutschrift): monthly health base on 31 May at most | EUR 2,900.00 | 2026 | GSVG § 27f |
| Zusatzversicherung (Krankengeld), share of the provisional health base | 2.5%, at least EUR 30.77, at most EUR 202.13 a month | 2026 | https://www.svs.at/cdscontent/?contentid=10007.816678&portal=svsportal |
| Krankengeld from the Zusatzversicherung | 60% of the daily base, at least EUR 11.02 a day | 2026 | https://www.svs.at/cdscontent/?contentid=10007.816735&portal=svsportal |
| Unterstützungsleistung (no opt-in needed), per day | EUR 40.04 | 2026 | https://www.svs.at/cdscontent/?contentid=10007.816734&portal=svsportal |

Accident insurance: the law and the SVS contribution sheet both give EUR 12.95. One SVS web page (contentid 10007.816638) prints EUR 12.96. Use EUR 12.95.

## The taxable base

**What the base is (GSVG § 25 Abs 1 and 2).** The monthly average of the year's income under the EStG from one or more activities insured under the GSVG, plus the pension, health and unemployment contributions the SVS charged (vorgeschrieben) for that year, as far as they are business expenses under EStG § 4 Abs 4 Z 1 lit a. Sale gains and restructuring gains (Sanierungsgewinne) are taken out. Several insured activities go into one base. Income as a managing director or as a shareholder-managing director of a GmbH counts as income from an insured activity. The base is clamped between the minimum and maximum base for each month.

**Provisional base (GSVG § 25a Abs 1).** The SVS charges each quarter on a provisional base until the income tax assessment for the year exists.
- No GSVG insurance in the third prior year (2023 for 2026): the minimum base, EUR 551.10 a month.
- Otherwise: the bases found for the third prior year, divided by that year's insured months, times the product of three years' Aufwertungszahlen (1.181 for 2026), rounded to the cent.
- The client may apply to lower or raise it (GSVG § 25a). A raised base avoids a large back-payment later; too high a guess creates a credit.

**New business health base (GSVG § 25a Abs 4).** For a Gewerbetreibender, the minimum base is the provisional and the final health base for the first two calendar years, if there was no GSVG insurance in the 120 months before. It is not re-assessed. Calendar years count, so a July start keeps the fixed health base for 18 months. Neue Selbständige do not get this; their health base is re-assessed.

**Final base and Nachbemessung (GSVG § 25 Abs 6, § 35 Abs 3).** Once the income tax assessment is in, the final base replaces the provisional one and the SVS recomputes pension and health. A back-payment is paid in the following year in four equal parts, each at the end of the second month of a quarter. For the first year of insurance and the next two, the client can apply (by 31 March) for twelve parts over three years. Accident insurance and the Selbständigenvorsorge follow the provisional base and are not re-assessed.

**Monthly charge.** pension = base x rate; health = base x 6.8%; accident = EUR 12.95; Selbständigenvorsorge = provisional health base x 1.53%. The full month is due for the month insurance starts (GSVG § 27 Abs 3).

**Selbständigenvorsorge.** Compulsory for everyone in compulsory GSVG health insurance, including Neue Selbständige. Not compulsory for opted-in health insurance or for freelancers insured under GSVG §§ 14a and 14b. Voluntary for freelancers insured only in pension insurance; they pay 1.53% of the provisional pension base. It stops the day before the client draws an own pension, unless the client agrees in writing within one month of the SVS notice to keep paying (BMSVG § 52 Abs 1a).

**Health contribution credit (GSVG § 27f, in force until 31 December 2027).** A person in GSVG health insurance on 31 May whose monthly health base on that day is EUR 2,900 or less gets a flat credit, tiered by base (EUR 90 for a base up to EUR 500, EUR 110 up to EUR 600, EUR 130 up to EUR 700, and so on in § 27f Abs 2). The last final base counts; without one, the provisional base. The SVS checks on 1 June and books the credit on the third quarter charge.

**ASVG job at the same time (GSVG § 35a).** Each base is set on its own, but all bases together cannot exceed the maximum base times the insured months. ASVG ranks first. The SVS cuts the GSVG pension and health base with a Differenzbeitragsvorschreibung and refunds any excess once all bases are final. Accident insurance stays a flat amount.

**Small business exemption (GSVG § 4 Abs 1 Z 7).** On application, a sole trader with a trade licence, or an FSVG doctor, is exempt from GSVG pension and health insurance (FSVG pension insurance for doctors) if yearly income from the activity is at most EUR 6,613.20 and turnover from all business is at most EUR 55,000. The applicant must also have been insured under the GSVG or FSVG for at most 12 of the last 60 months, or have reached the standard pension age, or be 57 or over and have met the limits in each of the last five years. Accident insurance stays. If the year's figures go over the limits, the SVS ends the exemption afterwards. The VAT small business exemption does not by itself change SVS obligations; only this application does.

**Versicherungsgrenze (Neue Selbständige).** Not an exemption. Income at or under EUR 6,613.20 means no insurance, with no application, no turnover test and no age test. Until an assessment exists, insurance starts only if the client declares that income will exceed the limit. If the tax office later shows the limit was passed, the client pays the contributions and a 9.3% surcharge on pension and health. Reporting the excess within eight weeks of the income tax assessment avoids the surcharge. A client below the limit has no pension or health cover; they can opt in.

**Tax deduction.** Compulsory contributions to statutory health, accident and pension insurance are business expenses (EStG § 4 Abs 4 Z 1 lit a), deductible on top of the Basispauschalierung. With cash-basis accounts they are deducted in the year paid (EStG § 19 Abs 2), so a Nachbemessung payment is deducted in the year it is paid. Zusatzversicherung contributions are deductible too. Krankengeld and the Unterstützungsleistung are taxable business income.

## Deadlines and filing

| Quarter | Covers | Due |
|---|---|---|
| Q1 | January to March | 28 February (29 in a leap year) |
| Q2 | April to June | 31 May |
| Q3 | July to September | 31 August |
| Q4 | October to December | 30 November |

The quarterly charge is due at the end of the second month of the quarter (GSVG § 35 Abs 2; SVS https://www.svs.at/cdscontent/?contentid=10007.816647&portal=svsportal). Contributions charged after the tax office reports income fall due at the end of the second month of the quarter in which they are charged. There is no return to file: the SVS takes income from the tax office's assessment. A Neuer Selbständiger who expects to pass the Versicherungsgrenze declares it to the SVS (GSVG § 2 Abs 1 Z 4).

## Penalties and interest

- **Late payment interest (GSVG § 35)**: due when contributions are not paid within 15 days of the due date (a payment within three days after that has no consequence). The rate is the base rate (Basiszinssatz) on 31 October of the prior year plus four percentage points. The base rate on 31 October 2025 was 1.53%, so the 2026 rate is 5.53% (OeNB, as in [at-income-tax](at-income-tax.md)).
- **9.3% surcharge (GSVG § 35)**: on pension and health contributions where insurance is found only after the tax assessment, unless the client declared or reported in time.
- **Enforcement (GSVG § 37)**: the SVS can collect arrears by administrative enforcement. It can also agree a payment plan or a deferral on request.

## Cross-border points

- Under Regulation (EC) 883/2004 only one state's social security law applies at a time. A person employed in another state and self-employed in Austria is insured in the state of employment; Austria is free. A person employed in Austria and self-employed abroad is insured in Austria, and the SVS asks for the foreign tax assessment.
- Work in two or more states needs an A1 determination. Refer to [at-cross-border](at-cross-border.md).
- Foreign pensions comparable to Austrian ones have their own health contribution rule (GSVG § 29a); not covered here.

## Worked examples

**Example 1. New trade licence holder, first year, minimum base.** A sole trader starts a trade in January 2026 with no GSVG insurance in the last 120 months. She has no 2023 base, so the provisional base is the minimum, EUR 551.10. The health base is fixed for 2026 and 2027. Each month she pays pension at 18.5%, health at 6.8%, accident EUR 12.95 and the Selbständigenvorsorge at 1.53%. The quarter is three months. Pension will be re-assessed when her 2026 assessment arrives; health will not.

```oa-check
name: Austria new Gewerbetreibender on the 2026 minimum base, monthly and quarterly SVS charge
inputs:
  min_base: 551.10
  accident: 12.95
steps:
  - pension: min_base * 0.185
  - health: min_base * 0.068
  - vorsorge: min_base * 0.0153
  - monthly_total: pension + health + accident + vorsorge
  - quarterly: monthly_total * 3
expected:
  pension: 101.95
  health: 37.47
  vorsorge: 8.43
  monthly_total: 160.81
  quarterly: 482.43
```

**Example 2. Established consultant, provisional base and Nachbemessung.** A Neuer Selbständiger was insured all of 2023 with bases (income plus contributions charged) of EUR 40,000. His 2026 provisional base is 40,000 x 1.181 / 12 = EUR 3,936.67 a month, under the maximum. His 2026 assessment shows profit of EUR 50,000. The final base adds the pension and health contributions charged in 2026, giving a monthly base under the maximum. The extra pension and health is paid in 2027 in four quarterly parts.

```oa-check
name: Austria Neuer Selbstaendiger, 2026 provisional base from 2023 and Nachbemessung
inputs:
  base_2023: 40000
  months_2023: 12
  profit_2026: 50000
  accident: 12.95
steps:
  - prov_base: round(base_2023 * 1.181 / months_2023, 2)
  - pension: prov_base * 0.185
  - health: prov_base * 0.068
  - vorsorge: prov_base * 0.0153
  - monthly_total: pension + health + accident + vorsorge
  - quarterly: monthly_total * 3
  - charged_ph_year: (pension + health) * 12
  - final_base_year: min(profit_2026 + charged_ph_year, 97020)
  - final_ph_year: final_base_year * 0.253
  - back_payment: final_ph_year - charged_ph_year
  - instalment_2027: back_payment / 4
expected:
  prov_base: 3936.67
  monthly_total: 1069.16
  quarterly: 3207.48
  charged_ph_year: 11951.73
  final_base_year: 61951.73
  back_payment: 3722.06
  instalment_2027: 930.51
```

## Ask the client first

- Do you hold a trade licence, are you a freelancer without one, or are you a doctor, pharmacist, patent attorney or civil engineer?
- When did your SVS insurance start, and were you insured under the GSVG in the 120 months before?
- What were your SVS bases in 2023, and what profit do you expect for 2026?
- Are you also employed, or do you draw a pension?
- If you have no trade licence: will your 2026 income stay at or under EUR 6,613.20?
- If you are a sole trader or an FSVG doctor: will income stay at or under EUR 6,613.20 and turnover from all business at or under EUR 55,000, and do you meet the prior insurance or age condition?
- Do you work in another EU/EEA state or Switzerland?
- Do you want Krankengeld cover (Zusatzversicherung)?

## Sources

| Source | URL | Read on |
|---|---|---|
| GSVG (§§ 2, 4, 25, 25a, 27, 27f, 35, 35a, 37), RIS | https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10008422 | 2026-10-26 |
| ASVG (§ 5 Abs 2, § 74 Abs 1 accident amount 2026, § 108a Aufwertungszahlen), RIS | https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10008147 | 2026-10-26 |
| BSVG (farmers, out of scope), RIS | https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10008431 | 2026-10-26 |
| EStG 1988 (§ 4 Abs 4 Z 1 lit a, § 19 Abs 2), RIS | https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004570 | 2026-10-24 |
| SVS, contribution sheet 2026 (VS-016) | https://www.svs.at/cdscontent/load?contentid=10008.763406&version=1672393252 | 2026-10-26 |
| SVS, provisional calculation in the first three years (rates) | https://www.svs.at/cdscontent/?contentid=10007.816638&portal=svsportal | 2026-10-26 |
| SVS, provisional calculation from year four (factor 1.181) | https://www.svs.at/cdscontent/?contentid=10007.816634&portal=svsportal | 2026-10-26 |
| SVS, final calculation (minimum and maximum per year) | https://www.svs.at/cdscontent/?contentid=10007.816635&portal=svsportal | 2026-10-26 |
| SVS, Versicherungsgrenze and 9.3% surcharge | https://www.svs.at/cdscontent/?contentid=10007.816855&portal=svsportal | 2026-10-26 |
| SVS, 2026 values and limits | https://www.svs.at/cdscontent/?contentid=10007.816718&portal=svsportal | 2026-10-26 |
| SVS, small business exemption conditions | https://www.svs.at/cdscontent/?contentid=10007.846813&portal=svsportal | 2026-10-26 |
| SVS, due dates | https://www.svs.at/cdscontent/?contentid=10007.816647&portal=svsportal | 2026-10-26 |
| SVS, Zusatzversicherung | https://www.svs.at/cdscontent/?contentid=10007.816678&portal=svsportal | 2026-10-26 |
| SVS, Krankengeld | https://www.svs.at/cdscontent/?contentid=10007.816735&portal=svsportal | 2026-10-26 |
| SVS, Unterstützungsleistung | https://www.svs.at/cdscontent/?contentid=10007.816734&portal=svsportal | 2026-10-26 |
| BMSVG § 52 (Selbständigenvorsorge rate, base, end on own pension), RIS | https://www.ris.bka.gv.at/Dokumente/Bundesnormen/NOR40210216/NOR40210216.html | 2026-10-26 |
| SVS, Selbständigenvorsorge | https://www.svs.at/selbstaendigenvorsorge | 2026-09-22 |
| OeNB, base rate (Basiszinssatz) | https://www.oenb.at/isawebstat/stabfrage/createReport?report=2.1&lang=DE | 2026-10-24 |
| USP, Basispauschalierung (SVS deductible on top) | https://www.usp.gv.at/themen/steuern-finanzen/steuerliche-gewinnermittlung/weitere-informationen-zur-steuerlichen-gewinnermittlung/pauschalierung-weitere-infos/basispauschalierung-einkommensteuer.html | 2026-10-24 |

Not yet confirmed: the Selbständigenvorsorge scope for opted-in and pension-only freelancers (BMSVG § 52a not read); the SVS worked example on contentid 10007.816634 prints 32,000 x 1.181 = 34,784, which is arithmetically wrong (it is 37,792), so this skill does not use it; whether the § 27f credit was booked in Q3 2026; the old version's Krankengeld terms (day 4, 26 weeks, six-month wait, start before 60) and the Unterstützungsleistung from day 43, kept out of the rates table and not re-read; the retirement rule (GSVG pension contributions continue alongside a pension); the registration deadline and the right to pay by monthly direct debit (in the old version, not re-read).

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
