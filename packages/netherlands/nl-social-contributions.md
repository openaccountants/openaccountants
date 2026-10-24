---
name: nl-social-contributions
description: "Dutch social contributions for tax year 2026, for employees, employers and the self-employed. Covers who is insured for the national insurances (AOW, Anw, Wlz) and the employee insurances (WW, WIA, ZW); the 2026 national insurance premiums of 27.65% in the first box 1 band (EUR 38,883) and the AOW-age variant; employer premiums AWf (2.74% / 7.74%), Aof (6.27% / 7.63%), Wko, Whk and the Zvw employer levy (6.10%) up to the maximum premium wage of EUR 79,409; the 4.85% Zvw contribution for the self-employed; the premium base, deadlines, fines and interest; and cross-border rules (Regulation 883/2004, A1, the 25% test, telework). Trigger on: premies volksverzekeringen, premies werknemersverzekeringen, bijdrage Zvw, werkgeversheffing Zvw, maximumpremieloon, AWf, Aof, Whk, social security Netherlands, zzp Zvw, A1 Netherlands. Out of scope: the payroll run itself (nl-payroll-tax, netherlands-payroll) and the income tax computation (nl-income-tax)."
version: 0.1
jurisdiction: NL
tax_year: 2026
last_updated: 2026-10-23
authored_by: Ryan Duguid
review_status: pending_review
trust_label: Accountant-authored
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Netherlands social contributions (2026)

This skill says which Dutch social contributions apply to a person or a business in 2026, at what rate, on what base, and when they are paid. It does not run a payroll. For the monthly payroll calculation (tables, cumulative calculation, WKR, corrections) use `nl-payroll-tax` or `netherlands-payroll`. For the income tax computation of a sole trader use `nl-income-tax`, with `nl-zzp-deductions` for taxable profit. For residence and the expat scheme use `nl-cross-border` and `nl-30-percent-ruling`.

The Netherlands has three layers of contributions:

- **National insurances (volksverzekeringen):** AOW (state pension), Anw (survivors) and Wlz (long-term care). Paid by the insured person, collected together with wage tax or income tax in the first box 1 band.
- **Employee insurances (werknemersverzekeringen):** WW (unemployment, financed by the AWf), WIA/WAO (disability, financed by the Aof and the Whk) and ZW (sickness, financed partly by the Whk). Paid by the employer only.
- **Health insurance contribution (inkomensafhankelijke bijdrage Zvw):** an employer levy on wages, or a contribution the self-employed pay themselves on profit. This is separate from the nominal premium every insured person pays to their own health insurer.

## Who this applies to

**National insurances.** A person is insured for the AOW if they are under AOW age and either live in the Netherlands, or do not live here but are subject to Dutch wage tax for work done here as an employee (AOW art. 6(1)). The Wlz uses the same two tests, without the age limit (Wlz art. 2.1.1(1)). Every insured person is liable for the premium (Wfsv art. 6(1)). The AOW age in 2026 is 67 (Belastingdienst, box 1 page).

**Employee insurances.** An employee for the WW is a natural person under AOW age in a private or public employment relationship (WW art. 3(1)). Someone working outside the Netherlands is not an employee for the WW unless they live here and the employer is here too (WW art. 3(2)). The premiums are owed by the employer and may not be recovered from the employee (Wfsv art. 20), with one exception: the employer may recover up to 50% of the WGA part of the Whk premium from net pay, but not the ZW part (Handboek Loonheffingen 2026, §7.6.9). No employee insurance premiums are due from the first day of the month in which the employee reaches AOW age (Wfsv art. 21).

**Self-employed (ondernemers, zzp'ers).** The self-employed pay national insurance premiums through their income tax assessment and the Zvw contribution through a separate assessment. They are not employees, so they are not insured for WW, WIA or ZW and pay no employee insurance premiums.

**Mandatory disability insurance for the self-employed (Wet baz): not in force.** The bill (Kamerstuk 36912, Wet basisverzekering arbeidsongeschiktheid zelfstandigen) was submitted to the Tweede Kamer on 24 March 2026. On 22 October 2026 the Tweede Kamer had not debated or voted on it. The government page says the premium would be 5.4% of income, capped at EUR 171 a month, that these figures may change, and that the insurance is at least several years away. Nothing is payable in 2026. Do not include it in any 2026 computation.

**Non-residents and cross-border workers.** Within the EU, EEA and Switzerland, Regulation (EC) 883/2004 decides which one country's social security applies. Elsewhere a bilateral social security treaty or Dutch national law decides. See "Cross-border points".

**Directors who are major shareholders (DGA).** Whether a DGA is insured for the employee insurances depends on the facts of the relationship, not on the title. Get a decision before computing. The national insurance and Zvw position follows the normal rules (see `nl-payroll-tax`, Directors and expatriates).

## Rates, bands and thresholds

| Item | Rate or amount | Tax year | Source |
|---|---|---|---|
| AOW premium (under AOW age) | 17.90% | 2026 | [Rates appendix, table 1](https://download.belastingdienst.nl/belastingdienst/docs/bijlage-nieuwsbrief-loonheffingen-2026-lh2091b64fd.pdf) |
| Anw premium | 0.10% | 2026 | same |
| Wlz premium | 9.65% | 2026 | same |
| National insurance total, under AOW age | 27.65% | 2026 | [Belastingdienst box 1](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/prive/inkomstenbelasting/heffingskortingen_boxen_tarieven/boxen_en_tarieven/box_1/) |
| National insurance total, at or over AOW age (no AOW premium) | 9.75% (Anw + Wlz); combined first-band rate with tax 17.85% | 2026 | [Rates appendix, table 1](https://download.belastingdienst.nl/belastingdienst/docs/bijlage-nieuwsbrief-loonheffingen-2026-lh2091b64fd.pdf) |
| Premium income ceiling (first band) | EUR 38,883 | 2026 | same |
| Premium income ceiling, born in 1945 or earlier | EUR 41,123 | 2026 | same |
| Tax part of the first band (not a contribution) | 8.10% | 2026 | same |
| AWf low (written permanent contract, not on-call, or a listed exception) | 2.74% | 2026 | [Rates appendix, table 9](https://download.belastingdienst.nl/belastingdienst/docs/bijlage-nieuwsbrief-loonheffingen-2026-lh2091b64fd.pdf) |
| AWf high (all other employment) | 7.74% | 2026 | same |
| Aof low (small employer) | 6.27% | 2026 | same |
| Aof high (medium and large employer) | 7.63% | 2026 | same |
| Wko surcharge (childcare) | 0.50% | 2026 | same |
| Ufo premium (government employers only) | 0.68% | 2026 | same |
| Whk | Small employers: sector rate from table 10 (WGA + ZW-flex; for example sector 44, Zakelijke Dienstverlening II, 0.94%). Medium and large: individual rate in the employer's Whk decision | 2026 | [Rates appendix, tables 9 and 10](https://download.belastingdienst.nl/belastingdienst/docs/bijlage-nieuwsbrief-loonheffingen-2026-lh2091b64fd.pdf) |
| Small employer: 2024 premium wage sum up to and including | EUR 1,082,500 (25 x average premium wage of EUR 43,300) | 2026 | same, table 9 |
| Medium employer: up to and including | EUR 4,330,000 | 2026 | same |
| Maximum premium wage (maximumpremieloon), employee insurances and Zvw | EUR 79,409 a year; EUR 6,617.41 a month; EUR 6,108.38 per four weeks | 2026 | [Rates appendix, table 11](https://download.belastingdienst.nl/belastingdienst/docs/bijlage-nieuwsbrief-loonheffingen-2026-lh2091b64fd.pdf) |
| Zvw employer levy (werkgeversheffing Zvw) | 6.10% | 2026 | [Rates appendix, table 12](https://download.belastingdienst.nl/belastingdienst/docs/bijlage-nieuwsbrief-loonheffingen-2026-lh2091b64fd.pdf) |
| Zvw contribution withheld (pensions, benefits, some DGAs) | 4.85% | 2026 | same |
| Zvw contribution for the self-employed and other income | 4.85%, maximum contribution income EUR 79,409 | 2026 | [Belastingdienst, Zvw 2026](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/inkomensafhankelijke_bijdrage_zorgverzekeringswet) |
| Premium part of the tax credits | 27.65 / 35.75 of each credit | 2026 | [Belastingdienst, heffingskortingen 2026, §21.9.1](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/heffingskortingen) |
| Mandatory self-employed disability insurance (Wet baz) | Not in force; bill 36912 pending | 2026 | [Tweede Kamer, 36912](https://www.tweedekamer.nl/kamerstukken/wetsvoorstellen/detail?qry=wetsvoorstel%3A36912&cfg=wetsvoorsteldetails) |

The AOW age variant: from the first day of the month in which a person reaches AOW age, the AOW premium is no longer part of the national insurance premium (Wfsv art. 10(2)) and no employee insurance premiums are due (Wfsv art. 21). Anw, Wlz and Zvw continue.

## The taxable base

**National insurances, employee (by withholding).** The premium income is the taxable wage under the Wage Tax Act, without the final-levy items in Wet LB art. 31(1)(d) to (g) (Wfsv art. 8(2)). It is capped at the first band ceiling of EUR 38,883 (Wfsv art. 8(3)). The employer withholds wage tax and national insurance premiums as one amount (loonbelasting/premie volksverzekeringen) using the official tables. Credits reduce the premium as well as the tax: 27.65/35.75 of each credit is the premium part (Wfsv art. 9(1); Belastingdienst heffingskortingen 2026, §21.9.1).

**National insurances, self-employed (by assessment).** The premium income is the taxable income from work and home (box 1) under chapter 3 of the Income Tax Act, after personal deductions, capped at EUR 38,883 (Wfsv art. 8(1) and (3)). The premium is assessed together with income tax. Income from box 2 and box 3 is not premium income.

**Employee insurances and Zvw employer levy.** The base is the wage under the Wage Tax Act (the "SV-loon"), without wages from former employment (other than employee insurance benefits) and without final-levy items in Wet LB art. 31(1)(b) to (h) (Wfsv art. 16). The base is capped at the maximum premium wage per employer (Wfsv art. 17(1)). Premiums are worked out per pay period on the cumulative base (voortschrijdend cumulatief rekenen, Wfsv art. 17(3)); the method is in `nl-payroll-tax`.

**What is outside the base.**
- WKR items designated as final-levy wage, and other final-levy items: outside the employee insurance and Zvw base (Wfsv art. 16(2)(b); Zvw art. 43(2)(a)).
- The expat scheme (30% ruling) allowance: it is a targeted exemption for extraterritorial costs (Wet LB art. 31a(2)(e)), which the employer designates as final-levy wage under Wet LB art. 31(1)(f) (Handboek Loonheffingen 2026, §22.1). The Handboek states that no employee insurance premiums are due on it (§19.4.8). For the national insurance premiums and the Zvw no Belastingdienst text says so in terms; the result follows from the statutes, which take art. 31(1)(f) items out of the national insurance premium income (Wfsv art. 8(2)) and out of the Zvw contribution income (Zvw art. 43(2)(a), 2°). So the allowance is outside all three bases.
- Employer Zvw levy: an employer cost, not taxable wage for the employee (Handboek Loonheffingen 2026, chapter 8).

**Zvw contribution, self-employed.** The contribution income includes taxable profit from a business under section 3.2 of the Income Tax Act and taxable results from other work (Zvw art. 43(2)(b) and (c)). Taxable profit is profit after the entrepreneur deductions and the MKB profit exemption (Wet IB art. 3.2). Personal deductions such as mortgage interest do not reduce it. If wages already carry the employer levy, the 4.85% applies only to the other income, up to what is left of the EUR 79,409 maximum (Belastingdienst, Zvw 2026, §28.2.4).

## Deadlines and filing

**Employers.** Wage tax, national insurance premiums, employee insurance premiums and the Zvw levy are reported and paid together in the payroll return (aangifte loonheffingen), per month or per four weeks. The return and the payment are due on the same date, about one month after the period ends. The 2026 calendar gives, for example: September 2026 due 31 October 2026; four-week period 10 (ending 4 October 2026) due 4 November 2026; December and period 13 due 31 January 2027 (Belastingdienst, tijdvakcodes aangifte- en betaaldatums 2026). The payment must be on the Belastingdienst account by that date; if the date falls on a weekend or public holiday, it must arrive before it (Handboek Loonheffingen 2026, §13.4.2). The period itself can only change from 1 January 2027 (§13.1).

**Self-employed.** National insurance premiums are assessed with income tax in the income tax return; the Zvw contribution is assessed separately but at the same time. For the 2025 return the deadline was 1 May 2026, with an online extension to 1 September 2026 if asked for before 1 May. The 2026 return follows the date in the invitation letter. A provisional assessment (voorlopige aanslag) can be asked for during the year for both income tax and the Zvw contribution, so the premiums are paid during the year rather than after the final assessment.

## Penalties and interest

**Payroll returns (Handboek Loonheffingen 2026, §13.5).**
- Late or no return: a fine of EUR 83, after a grace period of 7 calendar days.
- Late, short or no payment: 3% of the amount paid late, minimum EUR 50, maximum EUR 6,709. A payment within the 7-day grace period is not fined if the previous return was paid on time and in full.
- Late filing and late payment are separate defaults; one period can carry two fines.
- In exceptional cases (repeated defaults): up to EUR 1,675 per filing default, and up to 10% of the unpaid amount (maximum EUR 6,709) per payment default.
- Gross negligence or intent: a vergrijpboete instead of the default fine. Deliberate non-filing or non-payment is a criminal offence.
- Not registering as an employer in time: up to 10% of the amount paid late.

**Interest.**
- Collection interest (invorderingsrente) on late-paid tax debts: 4.3% from 1 January 2026.
- Tax interest (belastingrente) on assessments for past years, including payroll top-up assessments and income tax: 5% from 1 January 2026. Allowances (toeslagen) have their own rate.

## Cross-border points

**Which country.** Within the EU, EEA and Switzerland the person is insured in one country only, under Regulations 883/2004 and 987/2009 (Handboek Loonheffingen 2026, §20.1.1). The main rules for employees:
- Working only in the Netherlands: insured in the Netherlands, wherever they live. This covers most frontier workers living in Belgium or Germany and working here.
- Working in the Netherlands and in the country of residence: insured in the country of residence if they do at least 25% of their working time there, or earn at least 25% of their pay there. Below 25% and with one employer, insured where the employer is established.
- Secondment: an employee sent temporarily to another regulation country stays insured in the Netherlands for up to 24 months, with an A1 certificate from the SVB, if the conditions in §20.2.1 are met.
- Telework: under the multilateral framework agreement in force for the Netherlands since 1 July 2023, an employee can telework from the country of residence for up to 50% of total working time without a change of country, if the residence country has also signed the agreement, on application to the SVB (§20.4).

**Self-employed in more than one EU country.** Insured in the country of residence if they do at least 25% of their working time or services there, or earn 25% of their income there. Otherwise insured where the centre of interest of the business is (SVB, zelfstandige in meerdere EU-landen).

**Treaty countries.** The Netherlands has social security treaties with, among others, the United States, Canada, Australia, Japan, India, China, South Korea, Turkey and the United Kingdom (Trade and Cooperation Agreement). A person living in a treaty country and working here is usually insured here, with exceptions per treaty (§20.1.2, §20.2.2).

**Insured abroad.** If an employee is insured in another country, the Dutch employer pays that country's contributions there and registers with its institution (§20.2.2). An employee who pays income tax here but no Dutch national insurance premiums gets only the tax part of the credits (Belastingdienst heffingskortingen 2026, §21.9).

**Expat scheme.** The 30% allowance is outside the national insurance, employee insurance and Zvw bases (see "The taxable base"). It does not change the country of insurance.

## Worked examples

### Example 1: employee on EUR 60,000, small employer

A small employer in business services (Whk sector 44, small employer rate 0.94%) employs one person on a written permanent contract, not on-call, at EUR 60,000 a year. The employee is under AOW age, lives and works only in the Netherlands, and has no other income. All pay is ordinary wage.

Employer side. The wage is under the EUR 79,409 maximum, so the full wage is the base. AWf low 2.74% gives EUR 1,644.00. Aof low 6.27% gives EUR 3,762.00. Wko 0.50% gives EUR 300.00. Whk 0.94% gives EUR 564.00. The Zvw levy of 6.10% gives EUR 3,660.00. Total employer contributions: EUR 9,930.00 a year, on top of the wage.

Employee side. National insurance premiums apply only to the first EUR 38,883: AOW EUR 6,960.06, Anw EUR 38.88, Wlz EUR 3,752.21, total EUR 10,751.15 before credits. The general credit at EUR 60,000 is EUR 1,178.71 and the labour credit is EUR 4,747.04. Their premium part (27.65/35.75) is EUR 4,583.13, so the net annual national insurance premium is about EUR 6,168.02. In practice the employer withholds this through the payroll tables, not by this annual sum; the figure is an annual check. The employee pays no employee insurance premiums and no Zvw (unless the employer recovers part of the WGA premium).

```oa-check
name: Employee EUR 60,000, small employer, sector 44 (2026)
inputs:
  wage: 60000
  max_premium_wage: 79409
  band1: 38883
steps:
  - base: min(wage, max_premium_wage)
  - awf: base * 0.0274
  - aof: base * 0.0627
  - wko: base * 0.005
  - whk: base * 0.0094
  - zvw: base * 0.061
  - employer_total: awf + aof + wko + whk + zvw
  - ni_base: min(wage, band1)
  - aow: round(ni_base * 0.179, 2)
  - anw: round(ni_base * 0.001, 2)
  - wlz: round(ni_base * 0.0965, 2)
  - ni_gross: round(ni_base * 0.2765, 2)
  - general_credit: 3115 - 0.06398 * (wage - 29736)
  - labour_credit: 5685 - 0.0651 * (wage - 45592)
  - credit_share: 27.65 / 35.75
  - premium_part: round((general_credit + labour_credit) * credit_share, 2)
  - ni_net: ni_gross - premium_part
expected:
  awf: 1644.00
  aof: 3762.00
  wko: 300.00
  whk: 564.00
  zvw: 3660.00
  employer_total: 9930.00
  aow: 6960.06
  anw: 38.88
  wlz: 3752.21
  ni_gross: 10751.15
  premium_part: 4583.13
  ni_net: 6168.02
```

If the same employee were on a fixed-term or on-call contract and no exception applied, AWf high (7.74%) would apply: EUR 4,644.00 instead of EUR 1,644.00.

### Example 2: self-employed sole trader, premiums inside income tax

A sole trader under AOW age, resident and insured only in the Netherlands, has 2026 profit of EUR 50,000 before entrepreneur relief. After the self-employed deduction and the MKB exemption (worked out in `nl-zzp-deductions` and `nl-income-tax`), taxable profit is EUR 42,602.40. There are no wages, no other income and no personal deductions, so box 1 taxable income is also EUR 42,602.40.

National insurance. Premium income is box 1 income, capped at EUR 38,883. The gross premium is 27.65% of EUR 38,883 = EUR 10,751.15. The general credit (on EUR 42,602.40) is EUR 2,291.81 and the labour credit (on work income of EUR 50,000, before entrepreneur relief) is EUR 5,398.04. Their premium part is EUR 5,947.53, so about EUR 4,803.62 of national insurance premium is due, inside the income tax assessment.

Zvw. The contribution income is taxable profit, EUR 42,602.40, which is under the EUR 79,409 maximum. The contribution is 4.85% = EUR 2,066.22, assessed separately. There are no WW, WIA or ZW premiums, and no Wet baz premium in 2026.

The edge cases: the national insurance base is capped at the band 1 ceiling while the Zvw base is not (it uses the higher EUR 79,409 maximum), and the two credits use different incomes.

```oa-check
name: Sole trader, taxable profit EUR 42,602.40 (2026)
inputs:
  profit_before_relief: 50000
  taxable_profit: 42602.40
  band1: 38883
  zvw_max: 79409
steps:
  - ni_base: min(taxable_profit, band1)
  - ni_gross: round(ni_base * 0.2765, 2)
  - general_credit: 3115 - 0.06398 * (taxable_profit - 29736)
  - labour_credit: 5685 - 0.0651 * (profit_before_relief - 45592)
  - credit_share: 27.65 / 35.75
  - premium_part: round((general_credit + labour_credit) * credit_share, 2)
  - ni_net: ni_gross - premium_part
  - zvw_base: min(taxable_profit, zvw_max)
  - zvw: round(zvw_base * 0.0485, 2)
expected:
  ni_gross: 10751.15
  premium_part: 5947.53
  ni_net: 4803.62
  zvw: 2066.22
```

These are annual checks before the Belastingdienst's own rounding on the assessment.

## Ask the client first

1. Where does the person live, and in which countries do they work (days or hours in each)? Is there an A1 or other certificate of coverage?
2. Employee or self-employed? For an employee: written permanent contract or fixed-term or on-call, and is the person a director-major shareholder?
3. For an employer: the 2024 premium wage sum (small, medium or large), the sector code, and the current Whk notice or decision.
4. Date of birth: does the person reach AOW age (67) in 2026 or before?
5. For the self-employed: profit before and after entrepreneur relief, any wages that already carry the Zvw employer levy, and personal deductions.
6. Is the expat scheme (30% ruling) applied, and from when?

## Sources

| Source | URL | Read on |
|---|---|---|
| Wet financiering sociale verzekeringen, arts. 6, 8, 9, 10, 11, 16, 17, 20, 21 | https://wetten.overheid.nl/BWBR0017745/2026-01-01 | 2026-10-22 |
| Zorgverzekeringswet, arts. 43, 45 | https://wetten.overheid.nl/BWBR0018450/2026-01-01 | 2026-10-22 |
| Algemene Ouderdomswet, art. 6 | https://wetten.overheid.nl/BWBR0002221/ | 2026-10-22 |
| Wet langdurige zorg, art. 2.1.1 | https://wetten.overheid.nl/BWBR0035917/2026-01-01 | 2026-10-22 |
| Werkloosheidswet, art. 3 | https://wetten.overheid.nl/BWBR0004045/2026-01-01 | 2026-10-22 |
| Wet op de loonbelasting 1964, arts. 31(1)(f), 31a(2)(e) | https://wetten.overheid.nl/BWBR0002471/2026-01-01 | 2026-10-22 |
| Wet inkomstenbelasting 2001, art. 3.2 | https://wetten.overheid.nl/BWBR0011353/2026-01-01 | 2026-10-22 |
| Belastingdienst, Tarieven, bedragen en percentages loonheffingen 2026 (4th edition, 25 June 2026), tables 1, 9, 10, 11, 12 | https://download.belastingdienst.nl/belastingdienst/docs/bijlage-nieuwsbrief-loonheffingen-2026-lh2091b64fd.pdf | 2026-10-22 |
| Belastingdienst, Handboek Loonheffingen 2026 (March 2026), §§4.1, 7.5, 7.6.9, 13.1, 13.4, 13.5, 19.4.3, 19.4.8, 20.1, 20.2, 20.4, 22.1 | https://download.belastingdienst.nl/belastingdienst/docs/handboek-loonheffingen-lh0221t61fd.pdf | 2026-10-22 |
| Belastingdienst, Aangifte loonheffingen 2026: tijdvakcodes, aangifte- en betaaldatums | https://download.belastingdienst.nl/belastingdienst/docs/tijdvakcodes-aangiftedatums-betaaldatums-lh2101t62fd.pdf | 2026-10-22 |
| Belastingdienst, Inkomensafhankelijke bijdrage Zorgverzekeringswet 2026, §§28.2.3, 28.2.4 | https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/inkomensafhankelijke_bijdrage_zorgverzekeringswet | 2026-10-22 |
| Belastingdienst, Heffingskortingen 2026, §§21.2, 21.3, 21.9 | https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/heffingskortingen | 2026-10-22 |
| Belastingdienst, Box 1: uitleg en tarieven | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/prive/inkomstenbelasting/heffingskortingen_boxen_tarieven/boxen_en_tarieven/box_1/ | 2026-10-22 |
| Belastingdienst, Uitstel aanvragen voor de belastingaangifte 2025 | https://www.belastingdienst.nl/wps/wcm/connect/nl/belastingaangifte/content/ik-moet-aangifte-doen-maar-ik-wil-graag-uitstel-kan-dat | 2026-10-22 |
| Belastingdienst, Voorlopige aanslag aanvragen | https://www.belastingdienst.nl/wps/wcm/connect/nl/voorlopige-aanslag/content/waarom-zou-ik-een-voorlopige-aanslag-aanvragen | 2026-10-22 |
| Belastingdienst, Invorderingsrente | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/standaard_functies/prive/contact/rechten_en_plichten_bij_de_belastingdienst/invorderingsrente | 2026-10-22 |
| Belastingdienst, Overzicht percentages belastingrente | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/standaard_functies/prive/contact/rechten_en_plichten_bij_de_belastingdienst/belastingrente/overzicht_percentages_belastingrente | 2026-10-22 |
| SVB, U werkt als zelfstandige in meerdere EU-landen | https://www.svb.nl/nl/id/u-werkt-in-meerdere-landen/u-werkt-als-zelfstandige-in-meerdere-eu-landen | 2026-10-22 |
| Tweede Kamer, wetsvoorstel 36912 (Wet basisverzekering arbeidsongeschiktheid zelfstandigen) | https://www.tweedekamer.nl/kamerstukken/wetsvoorstellen/detail?qry=wetsvoorstel%3A36912&cfg=wetsvoorsteldetails | 2026-10-22 |
| Rijksoverheid, Plannen voor verplichte basisverzekering arbeidsongeschiktheid voor zelfstandigen | https://www.rijksoverheid.nl/themas/werk/hervormingen-arbeidsmarkt/meer-zekerheid-voor-werkenden/verplichte-arbeidsongeschiktheidsverzekering-voor-zelfstandigen | 2026-10-22 |

Not yet confirmed: the filing deadline for the 2026 income tax return (the page read covers the 2025 return); the fine for a late income tax return by a self-employed person (not on the pages read); the AOW-age band 1 rate split for a person who reaches AOW age during 2026 (month-by-month; use the official tables); the DGA employee insurance test (no source read for the criteria).

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
