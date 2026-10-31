---
name: netherlands-payroll
description: "Running Dutch payroll for tax year 2026: wage tax and national insurance withheld through the loonheffingen (Wet LB 1964), white and green tables, special-remuneration tables, the 2026 combined bands (35.75%, 37.56%, 49.50%) and the AOW-age bands, the payroll tax credits applied by one employer, the 52% anonymous rate, employer premiums (AWf, Aof, Wko, Whk, Ufo) and the Zvw levy on the EUR 79,409 cap, the director's customary wage of EUR 58,000, minimum wage, holiday pay and the transition payment, the monthly and four-weekly loonaangifte calendar, corrections, the EUR 83 and 3% penalties, payslips and the annual statement. Trigger phrases: loonheffing, loonaangifte, Dutch payroll, loonstrook, witte tabel, groene tabel, bijzondere beloningen, anoniementarief, minimumloon, vakantiegeld, nulaangifte, betaalverzuimboete. Out of scope: WKR detail (nl-payroll-tax), premium detail and self-employed (nl-social-contributions), company car (nl-company-car), expat scheme (nl-30-percent-ruling), cross-border (nl-cross-border)."
version: 1.2
jurisdiction: NL
tax_year: 2026
last_updated: 2026-10-27
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - payroll-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Netherlands: running payroll (loonheffingen) 2026

## Who this applies to

Every employer who pays wages to an employee and is a withholding agent (inhoudingsplichtige) under the Wet op de loonbelasting 1964 (Wet LB). That covers Dutch companies and foreign employers with a Dutch permanent establishment or that register voluntarily. The employer withholds wage tax and national insurance together, pays employer premiums for the employee insurances and the Zvw, files one loonaangifte per period, and pays it.

Use the Handboek Loonheffingen 2026 (version March 2026) with the rates appendix, edition 4 of 25 June 2026. Edition 4 corrects two figures from earlier editions: the general credit base runs "up to and including" EUR 29,736, and the employment credit ends at EUR 132,920 (not EUR 132,290). For a 2025 correction, use the 2025 tables.

Out of this skill: the work-cost scheme (WKR) in detail, see nl-payroll-tax; premium rules in depth and the self-employed, see nl-social-contributions; private use of a company car, see nl-company-car; the expat scheme, see nl-30-percent-ruling; who is insured where and treaty allocation, see nl-cross-border. Annual income tax for the employee: nl-income-tax.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source URL |
|---|---|---|---|
| Band 1, under AOW age: wage tax 8.10% + AOW 17.90% + Anw 0.10% + Wlz 9.65% | 35.75% up to EUR 38,883 | 2026 | https://download.belastingdienst.nl/belastingdienst/docs/bijlage-nieuwsbrief-loonheffingen-2026-lh2091b64fd.pdf |
| Band 2 | 37.56% from EUR 38,883 to EUR 78,426 | 2026 | same |
| Band 3 | 49.50% above EUR 78,426 | 2026 | same |
| Band 1, AOW age, born 1946 or later (no AOW premium) | 17.85% up to EUR 38,883 | 2026 | same |
| Band 1, born 1945 or earlier | 17.85% up to EUR 41,123 | 2026 | same |
| General credit (algemene heffingskorting), under AOW age | EUR 3,115; reduces 6.398% above EUR 29,736; nil at EUR 78,426 | 2026 | same |
| General credit, AOW age | EUR 1,556; reduces 3.195% | 2026 | same |
| Employment credit (arbeidskorting), under AOW age | max EUR 5,685 (reached at EUR 45,592); reduces 6.510% above EUR 45,592; nil at EUR 132,920 | 2026 | same |
| Employment credit, AOW age | max EUR 2,840; reduces 3.250% | 2026 | same |
| Elderly credit (ouderenkorting) | EUR 2,067; reduces above EUR 46,002; nil at EUR 59,782 | 2026 | same |
| Anonymous rate (no name, address or BSN given) | 52%, no credits | 2026 | https://wetten.overheid.nl/BWBR0002471/2026-01-01 (art. 26b) |
| AWf (unemployment fund), low / high | 2.74% / 7.74% | 2026 | https://download.belastingdienst.nl/belastingdienst/docs/bijlage-nieuwsbrief-loonheffingen-2026-lh2091b64fd.pdf |
| Aof (disability fund), small employer / medium and large | 6.27% / 7.63% | 2026 | same |
| Wko surcharge (childcare) | 0.50% | 2026 | same |
| Whk (return-to-work fund) | rate on the employer's own notice | 2026 | same (sector table 10) |
| Ufo (government employers only) | 0.68% | 2026 | https://download.belastingdienst.nl/belastingdienst/docs/handboek-loonheffingen-lh0221t61fd.pdf |
| Employer Zvw levy / withheld Zvw contribution | 6.10% / 4.85% | 2026 | https://download.belastingdienst.nl/belastingdienst/docs/bijlage-nieuwsbrief-loonheffingen-2026-lh2091b64fd.pdf |
| Maximum premium and contribution wage | EUR 79,409 a year; EUR 6,617.41 a month; EUR 6,108.38 per four weeks | 2026 | same (table 11) |
| Small employer (2024 premium wage sum) | up to and including EUR 1,082,500; medium up to EUR 4,330,000 | 2026 | same (table 9) |
| Customary wage, substantial-interest director | at least EUR 58,000 | 2026 | same (table 12) |
| WKR free space / final levy | 2.00% up to EUR 400,000 of fiscal wage, 1.18% above; 80% on the excess | 2026 | same (table 13) |
| Tax-free travel allowance | EUR 0.25 per km (from 1 January 2026, approved ahead of the Tax Plan 2027) | 2026 | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/berichten/nieuws/verhoging-onbelaste-kilometervergoeding-hoe-verwerkt-u-dit-in-de-loonaangifte |
| Home-working allowance / meal value / relocation | EUR 2.45 a day / EUR 4.05 a meal / EUR 7,750 | 2026 | https://download.belastingdienst.nl/belastingdienst/docs/bijlage-nieuwsbrief-loonheffingen-2026-lh2091b64fd.pdf |
| Expat scheme salary norm / under-30 master's / cap | more than EUR 48,013 / more than EUR 36,497 / WNT cap EUR 262,000 | 2026 | same (tables 12, 13) |
| Minimum wage, age 21 and over | EUR 14.71 an hour from 1 Jan; EUR 14.99 from 1 Jul | 2026 | https://www.rijksoverheid.nl/themas/werk/minimumloon/bedragen-minimumloon/bedragen-minimumloon-2026 |
| Holiday allowance (vakantiebijslag) | at least 8% of gross annual wage | 2026 | https://www.rijksoverheid.nl/vraag-en-antwoord/vakantiedagen-en-vakantiegeld/hoe-hoog-is-mijn-vakantiegeld |
| Transition payment cap | EUR 102,000, or one gross annual salary if higher | 2026 | https://www.rijksoverheid.nl/vraag-en-antwoord/ontslag/hoe-hoog-is-de-transitievergoeding-als-ik-word-ontslagen |

## The taxable base

1. **Wage.** Everything the employee gets from the employment: cash, benefits in kind, allowances. Employer Zvw levy is an employer cost; it is not wage and is not deducted from net pay. The wage-tax base, the premium base (employee insurances) and the Zvw base usually match but are recorded separately. Pension contributions follow the actual scheme; there is no standard percentage.
2. **Which table.** White tables for current employment. Green tables for income from former employment (pensions, many benefits). A one-off payment for current work stays white. Choose the period (day, week, four weeks, month, quarter), the age column (under or over AOW age), and whether the employee asked for the payroll tax credits. An employee asks for the credits with one employer or payer at a time.
3. **Special remuneration.** Bonuses, a once-a-year holiday allowance and similar payments use the special-remuneration table (white or green). The rate depends on the employee's annual wage, normally the previous year's wage; for a new starter, estimate the full current year. Holiday pay paid monthly joins the monthly wage.
4. **Do not shortcut the tables.** The bands and credits above are annual. The withholding for a period comes from the official period table or the software that implements it. A net-pay agreement needs a gross-up in the software. The annual figures are for checks and the employee's own return.
5. **Anonymous rate.** If the employee does not give name, address, place of residence or BSN, withhold 52% with no credits (Wet LB art. 26b). If the BSN is missing for reasons outside both parties' control (for example a municipal delay), the handbook allows normal withholding; record the reason.
6. **Employer premiums.** AWf low applies to a written indefinite contract that is not on-call, to young workers under 21 with at most 48 paid hours in four weeks (52 in a month), and to BBL trainees. Otherwise AWf high. Revise to high if the contract ends within two months of starting, or if paid hours exceed contracted hours by more than 30% in the year (this test does not apply where contracted hours average more than 30 a week). Aof low for small employers; size uses the 2024 premium wage sum. Even a small employer always pays the high Aof (7.63%) on UWV benefits it passes on to the employee (WW, ZW, WAO/WIA, paid through a werkgeversbetaling or as own-risk bearer), on WAZO benefits (such as pregnancy and maternity benefit), on Toeslagenwet supplements, and on old-scheme wachtgeld. Report these in the Aof uitkering boxes (Handboek §7.5). Whk is on the employer's notice. Premiums and the Zvw run on the capped base with cumulative period calculation (VCR, Handboek ch. 6). At each wage payment: (1) take the cumulative wage from 1 January; (2) take the cumulative maximum for all pay periods so far (EUR 6,617.41 a month, EUR 6,108.38 per four weeks, EUR 79,409 for the year); (3) take the lower of the two; (4) subtract the cumulative base already charged at earlier payments; (5) charge premiums on the difference; (6) round to 2 decimals. A period with no wage adds no room. So when wages vary month to month, unused room from a low month is used later in the year, and the annual cap is not a fresh allowance every month. The employer may recover up to half of the WGA part of Whk from net pay, never the ZW part.
7. **Benefits and the WKR.** Each benefit is either taxed as wage, exempt under a targeted exemption, valued at nil, or designated as final-levy wage under the WKR. The free space is 2.00% of fiscal wage up to EUR 400,000 and 1.18% above; the excess is taxed at 80% with the employer. The designation may not depart more than 30% from what is customary; up to EUR 2,400 per employee per year is accepted as customary. Detail and the settlement: nl-payroll-tax.
8. **Director-shareholder.** A working shareholder with a substantial interest takes a customary wage: the highest of the most comparable employment, the highest-paid other employee, and EUR 58,000 (Wet LB art. 12a). If the customary wage for all work is EUR 5,000 or less, no fictitious wage is added. Insurance and Zvw status are determined separately.
9. **Travel and mileage top-up.** EUR 0.25 per km applies back to 1 January 2026. If you paid EUR 0.23 or less, you may pay the EUR 0.02 difference tax-free with a later wage. If you taxed the excess over EUR 0.23 as wage, correct the earlier returns. If you paid 80% final levy on it, offset that levy in a later return.
10. **Employment-law inputs.** Pay at least the hourly minimum wage for the age band (youth rates for ages 15 to 20). Holiday allowance at least 8%; a CAO may remove it only if the wage is at least 108% of minimum wage. The transition payment is one third of a monthly salary per full year of service plus a pro rata part, capped as in the table.
11. **Sickness pay and statutory leave.** A sick employee keeps 70% of wage for 104 weeks, and for the first 52 weeks at least the statutory minimum wage; the wage counted is capped at the daily maximum premium wage (BW Book 7 art. 629(1)). Statutory leave is at least four times the agreed weekly working time per year (art. 634(1)). That statutory minimum expires six months after the end of the year in which it was earned, unless the employee could not reasonably take it (art. 640a).

## Deadlines and filing

- **Registration.** Register as employer before the first wage payment; the Belastingdienst assigns a loonheffingennummer and the return period (month or four weeks).
- **Return and payment** are due on the same day. Monthly 2026: one month after the period, for example September due 31 October 2026, December due 31 January 2027. Four-weekly: period 10 (7 September to 4 October) due 4 November 2026; period 13 due 31 January 2027. Use the official calendar. Payment must be received by the due date.
- **Nil returns.** A nihilaangifte when there were no employees in the period; a nulaangifte when there were employees but no wage was paid (for example an unpaid director). Keep filing until the Belastingdienst confirms deregistration.
- **Filing route.** Payroll software or an intermediary, or Mijn Belastingdienst Zakelijk for a small payroll. A rejected message is not a filed return.
- **Corrections.** Before the deadline, send the complete return again. After the deadline, correct in a later return; prior-year and specific cases use a separate correction. If you find the error yourself and a separate correction is needed, send it within 8 weeks of discovery.
- **Objection.** Disagreeing with the law as applied (not an error) is by objection within 6 weeks after payment.
- **Employee documents.** A payslip at the first payment and whenever it changes. An annual statement (jaaropgaaf) after the year end, reconciled to the final returns.
- **WKR final levy** is settled in the second return period of the next year (February 2027 for monthly filers).

## Penalties and interest

- **Late filing.** Grace period of 7 calendar days after the due date. Later or not at all: EUR 83. An incorrect or incomplete return can also attract EUR 83. Repeated or exceptional cases: up to EUR 6,709.
- **Late payment.** Grace period of 7 calendar days. Within it, no penalty if the previous return was paid on time and in full; otherwise 3%, minimum EUR 50, maximum EUR 6,709. After it: 3% of the late amount, minimum EUR 50, maximum EUR 6,709. Unpaid amounts found later are assessed (naheffingsaanslag) with the same 3% penalty.
- **Corrections** that lead to extra payment normally count as late payment too.
- **Interest.** On a negative correction, if the refund takes longer than 8 weeks, interest runs from 8 weeks after the correction is received.
- **Director liability.** Directors can be personally liable for unpaid wage tax; report an inability to pay promptly (Invorderingswet 1990).

## Cross-border points

- **Withholding versus insurance.** Decide separately whether Dutch wage tax applies (domestic law and the treaty) and whether the employee is insured for Dutch social security (EU Regulation 883/2004 or a bilateral agreement; an A1 or certificate of coverage). A worker can owe Dutch wage tax and be insured abroad, or the other way round. Use the table column that matches the tax and insurance position.
- **Foreign employers** without a permanent establishment can register voluntarily to run Dutch payroll.
- **Expat scheme (30% ruling).** Up to 30% tax-free in 2026 if the Belastingdienst has decided and the salary norm is met; detail and the fall to 27% from 2027 in nl-30-percent-ruling.
- **Residence, treaties and the 183-day test:** nl-cross-border.

## Worked examples

**Example 1. Annual check of wage tax for a full-year employee.** An employee under AOW age earns EUR 48,000 in 2026 from one employer, asked for the credits there, and has no other income. Band 1 is 38,883 at 35.75%; band 2 is the remaining 9,117 at 37.56%. The general credit falls by 6.398% of the wage above 29,736. The employment credit falls by 6.510% of the wage above 45,592. Over the year the period tables should withhold close to this total; small differences come from period rounding.

```oa-check
name: Employee EUR 48,000, under AOW age, credits with this employer (2026)
inputs:
  wage: 48000
steps:
  - band1: min(wage, 38883) * 0.3575
  - band2: max(min(wage, 78426) - 38883, 0) * 0.3756
  - band3: max(wage - 78426, 0) * 0.495
  - gross: band1 + band2 + band3
  - ahk: max(3115 - max(wage - 29736, 0) * 0.06398, 0)
  - ak: max(5685 - max(wage - 45592, 0) * 0.0651, 0)
  - withheld: max(gross - ahk - ak, 0)
expected:
  gross: 17325.02
  ahk: 1946.47
  ak: 5528.24
  withheld: 9850.31
```

**Example 2. Employer premiums on a wage above the monthly cap.** A small employer pays EUR 7,000 a month, every month, on a written indefinite contract (AWf low). The employer's Whk notice says 1.5% (an assumed figure for the example). The premium base is capped at EUR 6,617.41 a month. Because every month is over the cap, cumulative calculation gives the same base each month. Zvw uses the same cap.

```oa-check
name: Small employer, EUR 7,000 monthly wage, capped premiums (2026)
inputs:
  wage: 7000
  cap: 6617.41
  whk: 1.5
steps:
  - base: min(wage, cap)
  - awf: base * 0.0274
  - aof: base * 0.0627
  - wko: base * 0.005
  - whk_amt: base * whk / 100
  - zvw: base * 0.061
  - total: awf + aof + wko + whk_amt + zvw
expected:
  base: 6617.41
  awf: 181.32
  aof: 414.91
  wko: 33.09
  whk_amt: 99.26
  zvw: 403.66
  total: 1132.24
```

## Ask the client first

1. Is the employer registered, which return period does it have, and what does its current Whk notice say? Is it small, medium or large for Aof?
2. For each employee: identity and BSN, date of birth (AOW age, youth minimum wage), country of residence and where they work.
3. The contract: indefinite or fixed, on-call or not, contracted hours. This decides AWf low or high.
4. Has the employee asked for the payroll tax credits with this employer, and do they have another job or a benefit?
5. Is anyone a director with a substantial interest, an expat with a 30% decision, or working partly abroad?
6. What benefits and allowances are paid (car, travel, home working, meals, gifts), and which are designated under the WKR?

## Sources

| Source | URL | Read on |
|---|---|---|
| Belastingdienst, rates appendix loonheffingen 2026, edition 4 (25 June 2026) | https://download.belastingdienst.nl/belastingdienst/docs/bijlage-nieuwsbrief-loonheffingen-2026-lh2091b64fd.pdf | 2026-10-27 |
| Belastingdienst, Handboek Loonheffingen 2026 (March 2026), ch. 6, 7 (incl. §7.5), 9, 13, 14 | https://download.belastingdienst.nl/belastingdienst/docs/handboek-loonheffingen-lh0221t61fd.pdf | 2026-10-27 |
| Belastingdienst, period codes and filing and payment dates 2026 | https://download.belastingdienst.nl/belastingdienst/docs/tijdvakcodes-aangiftedatums-betaaldatums-lh2101t62fd.pdf | 2026-10-27 |
| Wet op de loonbelasting 1964, art. 12a, 20a, 22, 26b | https://wetten.overheid.nl/BWBR0002471/2026-01-01 | 2026-10-27 |
| Belastingdienst, mileage allowance EUR 0.25 (news of 25 June 2026) | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/berichten/nieuws/verhoging-onbelaste-kilometervergoeding-hoe-verwerkt-u-dit-in-de-loonaangifte | 2026-10-27 |
| Rijksoverheid, minimum wage 2026 | https://www.rijksoverheid.nl/themas/werk/minimumloon/bedragen-minimumloon/bedragen-minimumloon-2026 | 2026-10-27 |
| Rijksoverheid, holiday allowance | https://www.rijksoverheid.nl/vraag-en-antwoord/vakantiedagen-en-vakantiegeld/hoe-hoog-is-mijn-vakantiegeld | 2026-10-27 |
| Burgerlijk Wetboek Book 7, art. 629, 634, 640a | https://wetten.overheid.nl/BWBR0005290/2026-01-01 | 2026-10-27 |
| Rijksoverheid, transition payment | https://www.rijksoverheid.nl/vraag-en-antwoord/ontslag/hoe-hoog-is-de-transitievergoeding-als-ik-word-ontslagen | 2026-10-27 |

Not yet confirmed: the old version's employment-law points were not re-read today and are left out until checked (maternity and partner leave and their UWV benefits, working-time limits, payslip content list, third-party payments reporting); the exact customary-wage exceptions for start-ups and loss-making companies; the overtime revision method for multiple contracts and business transfers; the employee-count limit for filing in Mijn Belastingdienst Zakelijk; director-liability reporting deadlines in the Invorderingswet 1990.

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
