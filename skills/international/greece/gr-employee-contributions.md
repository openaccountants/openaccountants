---
name: gr-employee-contributions
description: "Greek social security contributions (e-EFKA) on employees' pay for 2026: what the employer withholds and what it pays on top. Covers the standard private-sector rates (code KPK 101: employee 13.37%, employer 21.79%, total 35.16%) by branch (main pension, health in kind and in cash, supplementary pension ETEAEP or TEKA, unemployment and other DYPA branches), the 2026 monthly insurable earnings ceiling of EUR 7,761.94, the heavy and unhealthy occupations (BAE) surcharge, occupational risk, bonuses and holiday allowance, the exempt overtime, night and Sunday premiums, the EUR 20 children's camps contribution, the monthly APD return and payment deadlines, and late payment. Trigger on: EFKA employer contributions, ασφαλιστικές εισφορές μισθωτών, ΑΠΔ, KPK 101, πλαφόν 2026, εργοδοτική εισφορά, Greek payroll social security. Out of scope: gr-efka (self-employed), gr-income-tax (employee income tax), gr-cross-border (residence, A1 postings, 5C)."
jurisdiction: GR
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-23
version: 0.1
verified_by: pending
---

# Greece: employee and employer social security contributions (e-EFKA), 2026

This skill covers the contributions a Greek employer withholds from an employee's pay and the contributions it pays on top, for pay periods in 2026. It links to the pack's other skills rather than repeating them:

- `gr-efka`: contributions of the self-employed, freelancers and farmers (the fixed monthly categories).
- `gr-income-tax`: income tax, including the deduction of employee contributions from taxable pay.
- `gr-cross-border`: tax residence, the 5C inbound regime and the EU social security rules (Regulation 883/2004, A1 postings).
- `gr-company-formation`: registering as an employer.

## Who this applies to

Every employer with staff in a private-law employment relationship in Greece. The employer deducts the employee's share from pay and pays both shares to e-EFKA, declaring them in the monthly APD return (Αναλυτική Περιοδική Δήλωση) ([Ministry of Labour, insurance contributions](https://ypergasias.gov.gr/en/social-security/insured-persons/insurance-contributions/)). The same rules cover company directors, general managers and paid board members of an AE when they are paid under a dependent employment relationship, and paid managers of companies other than the IKE (an IKE manager pays as self-employed, see `gr-efka`) (same page).

Which rates apply depends on the employee's coverage package code (Κωδικός Πακέτου Κάλυψης, KPK), which goes on the APD. The standard code for an ordinary private-sector employee is KPK 101. Other codes cover employees with an occupational risk charge, employees with no supplementary pension branch, BAE occupations and the former special funds of banks and utilities ([e-EFKA circular 38/2024 and its KPK table](https://www.efka.gov.gr/el/egkyklioi-kai-genika-eggrapha/egkyklios-38-24122024)).

Out of this skill:

- Public servants on public-law terms. Their main pension rate is the same 20% (6.67% employee, 13.33% employer), but health and other branches differ and the public sector files its own APD ([Ministry of Labour](https://ypergasias.gov.gr/en/social-security/insured-persons/insurance-contributions/)).
- Employed lawyers and engineers, whose supplementary and lump-sum contributions are fixed monthly categories (2026 amounts in [e-EFKA circular 4/2026](https://www.efka.gov.gr/el/egkyklioi-kai-genika-eggrapha/egkyklios-42026)).
- Construction works (Οικοδομοτεχνικά Έργα). They have their own APD and higher employer health rates (employer 6.312% health, against 4.05% for ordinary businesses) ([circular 38/2024](https://www.efka.gov.gr/el/egkyklioi-kai-genika-eggrapha/egkyklios-38-24122024)).
- Employees posted to or from Greece who hold an A1 from another state. See `gr-cross-border`.

## Rates, bands and thresholds

Standard rates for KPK 101 (ordinary private-sector employee), in force from 1 January 2025 and still the rates in e-EFKA's published package table for 2026 pay periods.

| Item | Employee | Employer | Total | Year | Source |
|---|---|---|---|---|---|
| Main pension (ΚΣΙ, former IKA-ETAM) | 6.67% | 13.33% | 20.00% | 2026 | [circular 38/2024, KPK table](https://www.efka.gov.gr/el/egkyklioi-kai-genika-eggrapha/egkyklios-38-24122024) |
| Health, benefits in kind (ΑΕΙ, to EOPYY) | 1.65% | 3.80% | 5.45% | from 1.1.2025 | [circular 38/2024](https://www.efka.gov.gr/el/egkyklioi-kai-genika-eggrapha/egkyklios-38-24122024) |
| Health, cash benefits (ΑΧΡ) | 0.40% | 0.25% | 0.65% | from 1.1.2025 | [circular 38/2024](https://www.efka.gov.gr/el/egkyklioi-kai-genika-eggrapha/egkyklios-38-24122024) |
| Supplementary pension (ETEAEP, or TEKA for people first insured from 1.1.2022) | 3.00% | 3.00% | 6.00% | from 1.6.2022 | [circular 38/2024](https://www.efka.gov.gr/el/egkyklioi-kai-genika-eggrapha/egkyklios-38-24122024); [Ministry of Labour, TEKA](https://ypergasias.gov.gr/xekinise-i-leitourgia-tou-neou-tameiou-epikourikis-kefalaiopoiitikis-asfalisis-teka/) |
| Unemployment (ΑΝΕ, DYPA, former OAED) | 1.20% | 1.20% | 2.40% | 2026 | [circular 38/2024](https://www.efka.gov.gr/el/egkyklioi-kai-genika-eggrapha/egkyklios-38-24122024) |
| Workers' housing fund (ΕΡΕ, Εργατική Εστία) | 0.35% | 0.00% | 0.35% | 2026 | [circular 38/2024](https://www.efka.gov.gr/el/egkyklioi-kai-genika-eggrapha/egkyklios-38-24122024) |
| LAEK (DYPA training fund) | 0.10% | 0.06% | 0.16% | 2026 | [circular 38/2024](https://www.efka.gov.gr/el/egkyklioi-kai-genika-eggrapha/egkyklios-38-24122024) |
| LPEAE (DYPA) | 0.00% | 0.15% | 0.15% | 2026 | [circular 38/2024](https://www.efka.gov.gr/el/egkyklioi-kai-genika-eggrapha/egkyklios-38-24122024) |
| **Total, KPK 101** | **13.37%** | **21.79%** | **35.16%** | 2026 | [circular 38/2024](https://www.efka.gov.gr/el/egkyklioi-kai-genika-eggrapha/egkyklios-38-24122024) |
| KPK 102: KPK 101 plus occupational risk (ΕΠΚ), employer only | 13.37% | 22.79% | 36.16% | 2026 | [circular 38/2024](https://www.efka.gov.gr/el/egkyklioi-kai-genika-eggrapha/egkyklios-38-24122024) |
| KPK 103: no supplementary branch | 10.37% | 18.79% | 29.16% | 2026 | [circular 38/2024](https://www.efka.gov.gr/el/egkyklioi-kai-genika-eggrapha/egkyklios-38-24122024) |
| KPK 105: BAE (heavy and unhealthy) occupation | 16.82% | 23.94% | 40.76% | 2026 | [circular 38/2024](https://www.efka.gov.gr/el/egkyklioi-kai-genika-eggrapha/egkyklios-38-24122024) |
| BAE surcharge inside KPK 105: main pension (ΚΣΒ) | 2.20% | 1.40% | 3.60% | 2026 | [circular 38/2024](https://www.efka.gov.gr/el/egkyklioi-kai-genika-eggrapha/egkyklios-38-24122024) |
| BAE surcharge inside KPK 105: supplementary (ΤΒΑ) | 1.25% | 0.75% | 2.00% | 2026 | [circular 38/2024](https://www.efka.gov.gr/el/egkyklioi-kai-genika-eggrapha/egkyklios-38-24122024) |
| Maximum monthly insurable earnings (πλαφόν), art. 38(2) ν. 4387/2016 | EUR 7,761.94 a month | | | from 1.1.2026 | [e-EFKA circular 4/2026](https://www.efka.gov.gr/el/egkyklioi-kai-genika-eggrapha/egkyklios-42026) |
| Children's camps account (ΕΛΠΚ), employer only | | EUR 20 per employee a year | | paid with August 2026 contributions | [e-EFKA general document 2338673/01.09.2026](https://www.efka.gov.gr/el/egkyklioi-kai-genika-eggrapha/geniko-eggrafo-233867301-09-2026) |

Notes on the table:

- **The 2025 cut.** The health in kind rate fell from 1 January 2025 under art. 12 of ν. 5162/2024, which amended art. 41(1) of ν. 4387/2016. Health in total is now 6.10% (employee 2.05%, employer 4.05%) ([circular 38/2024](https://www.efka.gov.gr/el/egkyklioi-kai-genika-eggrapha/egkyklios-38-24122024)). This is how KPK 101 reached 13.37% plus 21.79%.
- **No 2026 rate change.** e-EFKA's circulars and general documents published from January to 21 October 2026 contain no change to the KPK 101 rates ([e-EFKA circulars list](https://www.efka.gov.gr/el/egkyklioi-kai-genika-eggrapha)). The 2026 change was to the ceiling, which rose 2.5% (the 2025 consumer price index) to EUR 7,761.94 under ministerial decision Δ.15/Δ΄/1865/23.01.2026 (ΦΕΚ Β΄ 318/29.1.2026) ([circular 4/2026](https://www.efka.gov.gr/el/egkyklioi-kai-genika-eggrapha/egkyklios-42026)).
- **TEKA.** Anyone who first takes up insurable work from 1 January 2022 has their supplementary contribution paid to TEKA, the funded supplementary scheme of ν. 4826/2021, at the same 3% plus 3% ([Ministry of Labour, TEKA](https://ypergasias.gov.gr/xekinise-i-leitourgia-tou-neou-tameiou-epikourikis-kefalaiopoiitikis-asfalisis-teka/)). The employer's total cost does not change.
- **Lump-sum branch.** KPK 101 has no lump-sum (εφάπαξ, πρόνοια) branch. Employees whose sector has one (former welfare funds) are on a different KPK. For people insured from 1 January 1993 in a lump-sum branch, the contribution is 4% of insurable earnings ([Ministry of Labour](https://ypergasias.gov.gr/en/social-security/insured-persons/insurance-contributions/)). Check the employee's KPK before using the 101 rates.
- **BAE** occupations are those on the list of heavy and unhealthy occupations (ΚΒΑΕ). Whether a job is on the list is a separate question; this skill only gives the surcharge.

## The taxable base

- **What counts.** Contributions are due on all pay of any kind, except social benefits for marriage, childbirth, death and severe disability ([Ministry of Labour](https://ypergasias.gov.gr/en/social-security/insured-persons/insurance-contributions/)).
- **Ceiling.** Pay above EUR 7,761.94 in a month carries no contributions ([circular 4/2026](https://www.efka.gov.gr/el/egkyklioi-kai-genika-eggrapha/egkyklios-42026)). The same ceiling caps the base for the supplementary branch.
- **Christmas bonus, Easter bonus and holiday allowance.** All three are subject to contributions at the normal rates. The ceiling is applied to each of them on its own, separately from the month's salary ([Ministry of Labour](https://ypergasias.gov.gr/en/social-security/insured-persons/insurance-contributions/)). An employee paid monthly for a full year usually receives 14 payments: 12 salaries, the Christmas bonus (one salary), the Easter bonus and the holiday allowance (half a salary each). Those amounts come from labour law, not from EFKA rules; check them against the employment contract and collective agreement.
- **Exempt premiums.** For full-time employees, the premium part of pay for night work, extra hours (υπερεργασία), overtime and work on Sundays and public holidays is exempt from contributions. The base pay is not exempt. The exemption also covers a premium above the legal rate, whether paid voluntarily or under a collective agreement (art. 41 ν. 5184/2025 as amended by art. 73 ν. 5239/2025). The share of those premiums that flows into the Christmas and Easter bonuses is exempt too ([e-EFKA circular 21/2025](https://www.efka.gov.gr/el/egkyklioi-kai-genika-eggrapha/egkyklios-212025)). Only the subject amount goes on the APD.
- **Income tax.** Employee contributions are deducted from pay before income tax. See `gr-income-tax`.

## Deadlines and filing

**APD.** Ordinary businesses file the monthly APD online in the period e-EFKA sets for each pay month ([e-EFKA FAQ, ordinary businesses and construction works](https://www.e-efka.gov.gr/en/node/129)). For 2026 ([e-EFKA general document 2034418/04.12.2025](https://www.efka.gov.gr/el/egkyklioi-kai-genika-eggrapha/geniko-eggrafo-2034418-04122025)):

| Pay month 2026 | APD window opens | APD window closes |
|---|---|---|
| January | 1 Feb 2026 | 2 Mar 2026 |
| February | 1 Mar 2026 | 31 Mar 2026 |
| March | 1 Apr 2026 | 30 Apr 2026 |
| April | 1 May 2026 | 2 Jun 2026 |
| May | 1 Jun 2026 | 30 Jun 2026 |
| June | 1 Jul 2026 | 31 Jul 2026 |
| July | 1 Aug 2026 | 31 Aug 2026 |
| August | 1 Sep 2026 | 30 Sep 2026 |
| September | 1 Oct 2026 | 2 Nov 2026 |
| October | 1 Nov 2026 | 30 Nov 2026 |
| November | 1 Dec 2026 | 31 Dec 2026 |
| December | 1 Jan 2027 | 1 Feb 2027 |

The filing date is the date e-EFKA accepts and records the APD (same document). The Christmas and Easter bonuses have their own APD periods, set by former IKA-ETAM general document Ε40/535/28-07-2015 (same document).

**Payment.** Ordinary businesses and construction works pay current contributions by the last working day of the month after the pay month. Public sector employers pay by the last working day of the month after that. Payment goes through banks (e-banking, IRIS, DIAS) using only the employer's 23-digit RF code, which replaced the old payment ID on 7 April 2025 ([e-EFKA FAQ](https://www.e-efka.gov.gr/en/node/129)).

**ΕΛΠΚ.** The EUR 20 per employee goes with the August 2026 contributions. e-EFKA builds a separate APD for it centrally, so the employer files nothing extra ([general document 2338673/01.09.2026](https://www.efka.gov.gr/el/egkyklioi-kai-genika-eggrapha/geniko-eggrafo-233867301-09-2026)).

## Penalties and interest

- **Late payment.** Contributions paid after the deadline carry the statutory default interest and surcharges ([Ministry of Labour](https://ypergasias.gov.gr/en/social-security/insured-persons/insurance-contributions/)). This skill does not give the rate; see "Not yet confirmed".
- **Late APD.** A late or supplementary APD is still filed online ([e-EFKA FAQ](https://www.e-efka.gov.gr/en/node/129)).
- **Missed instalments on a settlement.** Under the ν. 4152/2013 settlement as amended by ν. 4997/2022, one late instalment in each twelve months of the plan costs a 15% surcharge on that instalment. Under the art. 54 ν. 4305/2014 settlement, a late instalment costs 2% a month. A late instalment can also cost the employer the whole settlement ([e-EFKA FAQ for debtors, KEAO](https://www.e-efka.gov.gr/el/sychnes-eroteseis/opheiletes-keao/themata-diakanonismoy-opheilon-sychn-erotapan-keao/genika)).
- **Natural disasters.** When a ministerial decision names a disaster area, contributions due before the event can be settled without surcharges for the suspension period (same FAQ).

## Cross-border points

- **One state at a time.** Under Regulation (EC) 883/2004 an employee is insured in one EU/EEA or Swiss system at a time, normally the state where they work. A worker posted to Greece who holds an A1 from the home state stays in that system and is left off the Greek APD. A worker posted from Greece needs an A1 from e-EFKA to stay in Greek insurance. See `gr-cross-border`.
- **Inbound workers on 5C.** The 5C regime is an income tax relief (see `gr-cross-border`). Contributions on a 5C employee's pay follow this skill.

## Worked examples

### Example 1: ordinary employee, EUR 2,000 a month with two Sundays worked

Maria works full time for a private Athens company under KPK 101. Her monthly salary in March 2026 is EUR 2,000. She also works two Sundays and gets the legal 75% premium on her daily wage. Her daily wage is 2,000 / 25 = EUR 80, so the premium is 80 x 2 x 75% = EUR 120. Under circular 21/2025 the premium is exempt, so only the EUR 2,000 goes on the APD.

Her pay is below the EUR 7,761.94 ceiling. Employee contributions are 2,000 x 13.37% = EUR 267.40. Employer contributions are 2,000 x 21.79% = EUR 435.80, so EUR 703.20 is paid to e-EFKA in total. The March APD is filed between 1 and 30 April 2026, and payment is due by 30 April 2026. Her pay before income tax is 2,000 + 120 - 267.40 = EUR 1,852.60. The employer's cost is 2,000 + 120 + 435.80 = EUR 2,555.80. In August the employer also pays EUR 20 to ΕΛΠΚ for her.

```oa-check
name: KPK 101, EUR 2,000 salary plus exempt Sunday premium, March 2026
inputs:
  salary: 2000
  working_days_divisor: 25
  sundays: 2
  sunday_premium_pct: 75
  employee_rate_pct: 13.37
  employer_rate_pct: 21.79
  ceiling: 7761.94
steps:
  - daily_wage: salary / working_days_divisor
  - exempt_premium: daily_wage * sundays * sunday_premium_pct / 100
  - base: min(salary, ceiling)
  - employee_contrib: round(base * employee_rate_pct / 100, 2)
  - employer_contrib: round(base * employer_rate_pct / 100, 2)
  - total_to_efka: employee_contrib + employer_contrib
  - pay_before_income_tax: salary + exempt_premium - employee_contrib
  - employer_cost: salary + exempt_premium + employer_contrib
expected:
  exempt_premium: 120.00
  employee_contrib: 267.40
  employer_contrib: 435.80
  total_to_efka: 703.20
  pay_before_income_tax: 1852.60
  employer_cost: 2555.80
```

### Example 2: high earner above the ceiling, December salary and Christmas bonus

Nikos is a KPK 101 employee on EUR 9,000 a month. In December 2026 he receives his December salary and a Christmas bonus, assumed under his contract to be one month's salary, EUR 9,000. The edge case is the ceiling. It applies to the salary and to the bonus separately, so each is capped at EUR 7,761.94. Contributions are not worked out on one combined EUR 18,000.

On each of the two amounts the employee pays 7,761.94 x 13.37% = EUR 1,037.77 and the employer pays 7,761.94 x 21.79% = EUR 1,691.33. For December that makes EUR 2,075.54 for the employee and EUR 3,382.66 for the employer. In total, 2 x (9,000 - 7,761.94) = EUR 2,476.12 of his December pay carries no contributions. The salary goes on the December APD (filed by 1 February 2027). The bonus goes on its own Christmas bonus APD.

```oa-check
name: KPK 101, EUR 9,000 salary and EUR 9,000 Christmas bonus, ceiling applied separately (2026)
inputs:
  salary: 9000
  christmas_bonus: 9000
  ceiling: 7761.94
  employee_rate_pct: 13.37
  employer_rate_pct: 21.79
steps:
  - salary_base: min(salary, ceiling)
  - bonus_base: min(christmas_bonus, ceiling)
  - employee_on_salary: round(salary_base * employee_rate_pct / 100, 2)
  - employer_on_salary: round(salary_base * employer_rate_pct / 100, 2)
  - employee_on_bonus: round(bonus_base * employee_rate_pct / 100, 2)
  - employer_on_bonus: round(bonus_base * employer_rate_pct / 100, 2)
  - employee_total: employee_on_salary + employee_on_bonus
  - employer_total: employer_on_salary + employer_on_bonus
  - pay_above_ceiling: (salary - salary_base) + (christmas_bonus - bonus_base)
expected:
  employee_on_salary: 1037.77
  employer_on_salary: 1691.33
  employee_total: 2075.54
  employer_total: 3382.66
  pay_above_ceiling: 2476.12
```

## Ask the client first

1. What is each employee's KPK? Is the job a BAE occupation, does it carry occupational risk, and does the sector have a supplementary or lump-sum branch?
2. When was the employee first insured anywhere (before 1993, 1993 to 2021, or from 2022 for TEKA)?
3. What are the monthly salary, the bonuses and holiday allowance actually paid, and does any month go above EUR 7,761.94?
4. Is the employee full time, and how much of their pay is night, overtime, extra-hours or Sunday and holiday premium?
5. Is anyone posted to or from Greece, and do they hold an A1?
6. Does the employer have unpaid contributions or a settlement plan with KEAO?

## Sources

| Source | URL | Read on |
|---|---|---|
| e-EFKA circular 38/2024 (health contribution cut from 1.1.2025) and the attached table of active KPK rates by branch | https://www.efka.gov.gr/el/egkyklioi-kai-genika-eggrapha/egkyklios-38-24122024 | 2026-10-23 |
| e-EFKA circular 4/2026 (ceiling EUR 7,761.94 from 1.1.2026; lawyers' and engineers' categories) | https://www.efka.gov.gr/el/egkyklioi-kai-genika-eggrapha/egkyklios-42026 | 2026-10-23 |
| e-EFKA circular 21/2025 (exempt overtime, night, Sunday and holiday premiums) | https://www.efka.gov.gr/el/egkyklioi-kai-genika-eggrapha/egkyklios-212025 | 2026-10-23 |
| e-EFKA general document 2034418/04.12.2025 (APD periods for 2026) | https://www.efka.gov.gr/el/egkyklioi-kai-genika-eggrapha/geniko-eggrafo-2034418-04122025 | 2026-10-23 |
| e-EFKA general document 2338673/01.09.2026 (EUR 20 ΕΛΠΚ contribution) | https://www.efka.gov.gr/el/egkyklioi-kai-genika-eggrapha/geniko-eggrafo-233867301-09-2026 | 2026-10-23 |
| e-EFKA circulars and general documents list (no 2026 KPK rate change to 21 Oct 2026) | https://www.efka.gov.gr/el/egkyklioi-kai-genika-eggrapha | 2026-10-23 |
| e-EFKA FAQ, ordinary businesses and construction works (APD filing, payment deadline, RF code) | https://www.e-efka.gov.gr/en/node/129 | 2026-10-23 |
| e-EFKA FAQ for debtors, KEAO (settlement surcharges) | https://www.e-efka.gov.gr/el/sychnes-eroteseis/opheiletes-keao/themata-diakanonismoy-opheilon-sychn-erotapan-keao/genika | 2026-10-23 |
| Ministry of Labour, insurance contributions (base, bonuses, scope, lump sum; its ceiling figure of EUR 6,500 is out of date) | https://ypergasias.gov.gr/en/social-security/insured-persons/insurance-contributions/ | 2026-10-23 |
| Ministry of Labour, TEKA start (first insured from 1.1.2022; 3% plus 3% from June 2022) | https://ypergasias.gov.gr/xekinise-i-leitourgia-tou-neou-tameiou-epikourikis-kefalaiopoiitikis-asfalisis-teka/ | 2026-10-23 |

Not yet confirmed: the monthly rate of default interest and surcharges on late-paid contributions and any fine for a late APD (the law was not fetched); the 2026 APD periods for the Christmas and Easter bonuses (general document Ε40/535/28-07-2015 was not fetched); the statutory size of the Christmas bonus, Easter bonus and holiday allowance (labour law, not fetched); whether any contribution rate cut is legislated for 2027.
