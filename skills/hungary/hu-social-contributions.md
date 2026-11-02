---
name: hu-social-contributions
description: "Hungarian social contributions for the self-employed, tax year 2026. Covers the 18.5% social security contribution (társadalombiztosítási járulék, TB), split 54% pension, 37.9% health and 8.1% labour market, and the 13% social contribution tax (szociális hozzájárulási adó, szocho) a sole trader (egyéni vállalkozó) pays on themself: the base for the real-cost regime (the draw) and for flat-rate taxation (the cumulative quarterly method), the monthly floor of the 2026 minimum wage HUF 322,800 or guaranteed minimum wage HUF 373,200, who escapes the floor (36-hour job, student, pensioner), the family contribution allowance, szocho on the business dividend base up to HUF 7,747,200, KATA, company members (társas vállalkozó), the HUF 12,300 health service contribution and the quarterly 2658 return. Trigger phrases: TB járulék egyéni vállalkozó, szocho egyéni vállalkozó, minimum járulékalap, göngyölítés, 58-as bevallás, Hungarian self-employed contributions. Out of scope: hu-payroll (employees), hu-income-tax (szja), hu-cross-border."
version: 2.2
jurisdiction: HU
tax_year: 2026
last_updated: 2026-10-31
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Hungary: social contributions for the self-employed (2026)

Source-cited draft: not reviewed by an accountant, not for filing. Built by the OpenAccountants team.

This skill covers what a Hungarian sole trader (egyéni vállalkozó) pays on themself to the social security system in 2026: the 18.5% social security contribution (TB) and the 13% social contribution tax (szocho). It also covers the minimum for working members of companies (társas vállalkozó). It links to the other Hungary skills and does not repeat them:

- [hu-income-tax](hu-income-tax.md): the sole trader's income tax and the three regimes (flat-rate, real-cost, KATA).
- [hu-payroll](hu-payroll.md): contributions an employer withholds and pays on employees.
- [hu-cross-border](hu-cross-border.md): residence, non-residents and which country insures a person.

Law used: the Tbj. (Act CXXII of 2019 on social security entitlements and contributions) and the Szocho tv. (Act LII of 2018 on the social contribution tax), read on njt.jog.gov.hu on 2026-10-23 in the version in force from 1 October 2026; NAV information sheets 3, 91, 99 and 100 for 2026. The short address njt.hu refused connections.

**What changed for 2026.**
- The floors moved with the minimum wage: HUF 322,800 a month, or HUF 373,200 (guaranteed minimum wage) where the sole trader's main personal activity needs at least secondary education or a secondary vocational qualification (Government Decree 426/2025. (XII. 23.), 2. §; Tbj. 4. § 14.; Szocho tv. 34. § 11.).
- The szocho floor for a sole trader is the minimum wage itself. The 112.5% multiplier no longer applies from 1 January 2026 (Szocho tv. 8. § (3) as amended by Act LXXXIV of 2025, 28. §, in force 1 January 2026 under 35. § (3) of that Act; NAV sheet 3, part III.2; NAV sheet 100, part 6.1).
- The tax-free part of flat-rate income, which is outside the TB and szocho base, is HUF 1,936,800.
- The health service contribution is HUF 12,300 a month (NAV sheet 91, part 5).

## Who this applies to

- **Sole traders** for social security purposes: people in the register of sole traders (egyéni vállalkozói nyilvántartás), practising vets and private pharmacists, lawyers, individual patent attorneys, and notaries and bailiffs working outside a firm (Tbj. 4. § 2.; NAV sheet 3, part II.2). Insurance runs from registration to deletion, whether or not the person works (Tbj. 10. §).
- **Three statuses** decide the contributions (NAV sheet 3, part II.3; NAV sheet 100, part 6):
  - **Full-time (főfoglalkozású):** the default. Pays on actual income, with a monthly floor.
  - **Second job (másodfoglalkozású):** also has a job of at least 36 hours a week (hours across jobs are added), or is a full-time student. Pays on actual income only, no floor (Tbj. 42. § (2)-(3)).
  - **Supplementary (kiegészítő tevékenységet folytató):** an own-right pensioner, or a widow's pensioner over pension age. Pays no TB, and no szocho on the draw or flat-rate income (Szocho tv. 5. § (1) a); NAV sheet 3, part II.4.5, III.1.2; NAV sheet 100, part 6.3). Szocho on the business dividend base is still due (Szocho tv. 19. § (1)).
- **KATA taxpayers** pay neither: the HUF 50,000 monthly fixed tax replaces them (Tbj. 38. § (2); Kata tv. 8. §). See [hu-income-tax](hu-income-tax.md).
- **Company members (társas vállalkozó)** who work personally in a Kft., Bt. or similar pay TB on what the company pays them for personal work, at least the minimum wage a month (Tbj. 39. § (1)); the company pays szocho on at least the minimum wage (Szocho tv. 8. § (1)). In both, the guaranteed minimum wage applies where the member's main activity needs at least secondary education (Tbj. 4. § 14.2.; Szocho tv. 34. § 11.). NAV sheet 12 has the details.
- **Employees** are in [hu-payroll](hu-payroll.md).

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Social security contribution (TB) | 18.5%, no ceiling | 2026 | [Tbj. 25. § (1)](https://njt.jog.gov.hu/jogszabaly/2019-122-00-00) |
| How NAV splits the TB it collects | 54% pension (Nyugdíjbiztosítási Alap), 37.9% health (Egészségbiztosítási Alap), 8.1% labour market | 2026 | [Tbj. 26. § (1)](https://njt.jog.gov.hu/jogszabaly/2019-122-00-00) |
| Pension contribution (nyugdíjjárulék), a separate charge only for certain benefit recipients and insured persons named in Tbj. 23. § (1) c), not the sole trader's TB | 10% | 2026 | [Tbj. 25. § (2), 23. § (1) c)](https://njt.jog.gov.hu/jogszabaly/2019-122-00-00) |
| Social contribution tax (szocho) | 13% | 2026 | [Szocho tv. 2. § (1)](https://njt.jog.gov.hu/jogszabaly/2018-52-00-00) |
| Monthly floor for TB and szocho, full-time sole trader | Minimum wage HUF 322,800; HUF 373,200 if the main personal activity needs at least secondary education or qualification | from 2026-01-01 | [Tbj. 40. § (3), 4. § 14.](https://njt.jog.gov.hu/jogszabaly/2019-122-00-00); [Szocho tv. 8. § (3), 34. § 11.](https://njt.jog.gov.hu/jogszabaly/2018-52-00-00); [426/2025. Korm. rendelet 2. §](https://njt.jog.gov.hu/jogszabaly/2025-426-20-22) |
| Tax-free flat-rate income, outside the TB and szocho base | HUF 1,936,800 a year | 2026 | [Tbj. 40. § (2)](https://njt.jog.gov.hu/jogszabaly/2019-122-00-00); [Szocho tv. 6. § (2)](https://njt.jog.gov.hu/jogszabaly/2018-52-00-00); [NAV sheet 100, part 6](https://nav.gov.hu/pfile/file?path=/ugyfeliranytu/nezzen-utana/inf_fuz/2026/100.-Az-egyeni-vallalkozok-atalanyadozasanak-alapveto-szabalyai-2026.-02.-20) |
| Szocho on the business dividend base (vállalkozói osztalékalap): stops when the year's income reaches 24 times the minimum wage | Cap HUF 7,747,200 | 2026 | [Szocho tv. 2. § (2)](https://njt.jog.gov.hu/jogszabaly/2018-52-00-00); [NAV sheet 3, part III.1.1](https://nav.gov.hu/pfile/file?path=/ugyfeliranytu/nezzen-utana/inf_fuz/2026/03.-Az-egyeni-vallalkozok-szja--es-jarulekkotelezettsege-2026.-08.-31.) |
| Family contribution allowance (családi járulékkedvezmény) | 15% of the family allowance the tax base could not absorb, up to the TB | 2026 | [Tbj. 34. § (3), (6)](https://njt.jog.gov.hu/jogszabaly/2019-122-00-00) |
| Szocho credit for a sole trader with health impairment of 60% or less, or on disability benefits | Up to 13% of twice the minimum wage a month | 2026 | [Szocho tv. 13. § (3)-(4)](https://njt.jog.gov.hu/jogszabaly/2018-52-00-00); [NAV sheet 3, part III.3](https://nav.gov.hu/pfile/file?path=/ugyfeliranytu/nezzen-utana/inf_fuz/2026/03.-Az-egyeni-vallalkozok-szja--es-jarulekkotelezettsege-2026.-08.-31.) |
| Pensioner using a mothers' allowance: szocho on flat-rate income above four times the annual average wage | Above HUF 34,356,720 | from 2026-01-01 | [Szocho tv. 5. § (1a) b)](https://njt.jog.gov.hu/jogszabaly/2018-52-00-00); [NAV sheet 100, part 6.3](https://nav.gov.hu/pfile/file?path=/ugyfeliranytu/nezzen-utana/inf_fuz/2026/100.-Az-egyeni-vallalkozok-atalanyadozasanak-alapveto-szabalyai-2026.-02.-20) |
| Health service contribution (egészségügyi szolgáltatási járulék), for an uninsured person, for example during suspension | HUF 12,300 a month (HUF 410 a day) | 2026 | [Tbj. 25. § (3)](https://njt.jog.gov.hu/jogszabaly/2019-122-00-00); [NAV sheet 91, part 5](https://nav.gov.hu/pfile/file?path=/ugyfeliranytu/nezzen-utana/inf_fuz/2026/91.-informacios-fuzet---az-egeszsegugyi-szolgaltatasi-jarulek-2026.01.09) |
| Late payment interest (késedelmi pótlék) | Central bank base rate plus 5 points, per day /365. Base rate 5.50% from 26 August 2026, held on 20 October 2026, so 10.50% a year | 2026 | [Art. 209. § (1)](https://njt.jog.gov.hu/jogszabaly/2017-150-00-00); [NAV, base rate notice of 25 August 2026](https://nav.gov.hu/ugyfeliranytu/jegybank); [MNB, 20 October 2026](https://www.mnb.hu/monetaris-politika/a-monetaris-tanacs/kozlemenyek/2026/kozlemeny-a-monetaris-tanacs-2026-oktober-20-i-uleserol) |

## The taxable base

### Real-cost regime: the draw

- **TB base = the draw (vállalkozói kivét)** for the month (Tbj. 40. § (1)). **Szocho base = the draw** (Szocho tv. 6. § (1)).
- **Floor.** Each month the base is at least the minimum wage, or the guaranteed minimum wage where the main activity needs secondary education (Tbj. 40. § (3); Szocho tv. 8. § (3)). A month with no draw still pays on the floor (NAV sheet 3, part II.4.2).
- **Dividend base.** Szocho at 13% is also due on the business dividend base until the person's income for the year (consolidated base, dividends, dividend base, capital gains and similar) reaches HUF 7,747,200. It is paid with the annual szja return (Szocho tv. 2. § (2), 19. § (1); NAV sheet 3, part III.1.1).
- The sole trader's own szocho is a deductible business cost; their own TB is not (NAV sheet 3, part I.1.2.1).

### Flat-rate taxation: the cumulative quarterly method (göngyölítés)

For each quarter (Tbj. 40. § (2); Szocho tv. 6. § (2)):

1. Take the taxable flat-rate income from 1 January to the end of the quarter (flat-rate income minus the HUF 1,936,800 tax-free part).
2. Subtract the base already used for the earlier quarters of the year. The base already used includes months charged at the floor (NAV sheet 100, part 6.1, worked table).
3. Divide by the number of months in the quarter in which the person was insured for at least one day.
4. That is the monthly base, but not less than the floor for a full-time sole trader.

While flat-rate income for the year stays under HUF 1,936,800, a full-time sole trader pays on the floor every month, including months with only tax-free income (NAV sheet 100, part 6.1). A second-job sole trader pays nothing until income passes HUF 1,936,800, but still files the quarterly return (NAV sheet 100, part 6.2).

### When the floor does not apply

- **Benefit months.** No TB or szocho on the floor for days on sick pay, maternity and childcare benefits (CSED, GYED, and GYES or nursing benefits unless the person keeps working), military reserve service or detention. For part months, the floor is cut by one thirtieth per day (Tbj. 40. § (4)-(5); Szocho tv. 9. §).
- **Suspension (szünetelés).** A whole month of suspension carries no TB or szocho. A part month is not pro-rated: the full monthly floor is due (NAV sheet 3, part II.4.3). During suspension the person is uninsured. If not insured or entitled to health care on another ground, they owe the HUF 12,300 monthly health service contribution (NAV sheet 3, part II.4.3).
- **36-hour job or full-time study:** no floor (Tbj. 42. § (2); NAV sheet 3, part III.2).
- **Sole trader and company member at once:** pays the floor only as a sole trader, unless a statement to the company by 31 January moves the floor to the company for the whole year (Tbj. 42. § (8); Szocho tv. 9. § (10); NAV sheet 3, part II.4.4.2).

### Family contribution allowance (Tbj. 34. §, 80. §)

A sole trader entitled to the family allowance can cut their TB by 15% of the family allowance the tax base could not use, up to the TB. Monthly, it is 15% of the gap between the month's family allowance and the month's draw or flat-rate income advance base. For a full-time flat-rate sole trader paying on the floor, the allowance works against the TB on the floor up to that month's flat-rate income, even if tax-free; in a month with no income it cannot be used (NAV sheet 100, part 6.1). It is reported on the quarterly 2658 return and settled in the annual return. Claiming it without entitlement means repaying it plus a 12% penalty if the repayment is above HUF 10,000 (Tbj. 81. § (3)).

## Deadlines and filing

| What | When | Where |
|---|---|---|
| Insurance registration | Done by NAV from the sole trader register; changes within 15 days on form 08E (T1041 in ÁNYK). Lawyers, notaries, bailiffs, patent attorneys, vets and private pharmacists still file 08E themselves | NAV (Art. 1. melléklet 3.10., 44. §; NAV sheet 3, part II.6) |
| TB and szocho return (2658, the '58 return) with the three months shown separately | By the 12th of the month after the quarter, even if nothing is due | NAV, electronically (Art. 50. § (1a); Tbj. 77. § (2); Szocho tv. 19. § (1)-(2)) |
| Pay the TB and szocho for the quarter | Same day | TB: NAV account 10032000-06055802; szocho: 10032000-06055912 (Tbj. 77. §; NAV sheet 3) |
| Szocho on the dividend base | With the annual szja return, 20 May 2027 for 2026 | NAV (Szocho tv. 19. § (1)) |
| Out-of-cycle return | When the sole trader stops trading, loses the right to trade, or claims an old-age pension (within 30 days of the claim) | NAV (Art. 52. §; NAV sheet 3, part II.5) |
| A sole trader who employs staff | Monthly 2608 return for the employees | See [hu-payroll](hu-payroll.md) |
| Health service contribution | Monthly, by the 12th of the next month | NAV (NAV sheet 91) |

## Penalties and interest

- **Late payment interest (Art. 209. § (1)).** Central bank base rate plus 5 points /365 per day: 10.50% a year at the 5.50% base rate in force from 26 August 2026 (held on 20 October 2026).
- **Tax penalty (Art. 215. § (3)-(4)).** 50% of a shortfall found on audit; 200% where income was hidden or records falsified.
- **Default fine (Art. 220. § (1)).** Up to HUF 400,000 for an individual for a late, missing or wrong return.
- **Missed quarterly return (Art. 221. §).** A 15-day notice first, then a fixed HUF 50,000 fine for an individual and a second notice; after that, HUF 200,000.
- **Self-correction (Art. 212. § (1)).** Base rate /365 per day; 1.5 times on a repeat correction.
- **Family contribution allowance claimed without entitlement.** Repay by the annual return deadline plus a 12% difference penalty when the repayment exceeds HUF 10,000 (NAV sheet 100, part 6.1).

## Cross-border points

- **Which country insures the person.** Within the EU, EEA and Switzerland, Regulation (EC) 883/2004 decides. A sole trader insured in another state and holding an A1 certificate pays no Hungarian TB on that activity, and cannot use KATA (NAV sheet 99, part 1). Szocho is not due on income of a person insured in another member state under the coordination rules, proven with the foreign authority's certificate (Szocho tv. 5. § (4)).
- **Full-time study abroad** in an EEA state or Switzerland counts as study for the second-job rule (Tbj. 42. § (2) b)).
- **Residence and treaty questions** are in [hu-cross-border](hu-cross-border.md).

## Worked examples

### Example 1: full-time flat-rate sole trader under the tax-free amount

Eszter is a full-time sole trader on flat-rate taxation delivering food, a job with no education requirement. Her 2026 flat-rate income is HUF 1,500,000, all inside the HUF 1,936,800 tax-free part, so she pays no szja. She still pays TB and szocho every month on the minimum wage floor of HUF 322,800: TB HUF 59,718 and szocho HUF 41,964, HUF 101,682 a month, HUF 1,220,184 for the year. She files the 2658 return and pays by the 12th of the month after each quarter. If she had a full-time job of 36 hours a week, she would pay nothing, because her taxable flat-rate income is nil.

```oa-check
name: HU 2026 full-time flat-rate sole trader on the minimum wage floor
inputs:
  monthly_floor: 322800
  flat_rate_income: 1500000
  tax_free: 1936800
  tb_rate_pct: 18.5
  szocho_rate_pct: 13
steps:
  - taxable_income: max(flat_rate_income - tax_free, 0)
  - tb_month: monthly_floor * tb_rate_pct / 100
  - szocho_month: monthly_floor * szocho_rate_pct / 100
  - total_month: tb_month + szocho_month
  - total_year: total_month * 12
  - second_job_total: taxable_income * (tb_rate_pct + szocho_rate_pct) / 100
expected:
  taxable_income: 0
  tb_month: 59718
  szocho_month: 41964
  total_month: 101682
  total_year: 1220184
  second_job_total: 0
```

### Example 2: the cumulative quarterly method, floor then actual income

Ferenc is a full-time flat-rate sole trader (web development, 45% cost ratio, no education requirement for the floor). In Q1 his revenue is HUF 3,000,000, so his flat-rate income is HUF 1,650,000, all tax-free. He pays on the floor for January to March: a Q1 base of HUF 968,400.

In Q2 his revenue is HUF 5,064,000, so his flat-rate income for the half year is HUF 4,435,200 and his taxable flat-rate income HUF 2,498,400. The base already used is the Q1 floor of HUF 968,400. The Q2 monthly base is (2,498,400 - 968,400) / 3 = HUF 510,000, above the floor, so it applies: TB HUF 94,350 and szocho HUF 66,300 a month. The edge: the Q1 floor months count as base already used, so they are not charged twice.

```oa-check
name: HU 2026 flat-rate cumulative quarterly base, Q1 floor then Q2 actual
inputs:
  q1_revenue: 3000000
  q2_revenue: 5064000
  cost_ratio_pct: 45
  tax_free: 1936800
  monthly_floor: 322800
steps:
  - q1_income: q1_revenue * (100 - cost_ratio_pct) / 100
  - q1_taxable: max(q1_income - tax_free, 0)
  - q1_monthly_base: max(q1_taxable / 3, monthly_floor)
  - q1_base_used: q1_monthly_base * 3
  - h1_income: (q1_revenue + q2_revenue) * (100 - cost_ratio_pct) / 100
  - h1_taxable: max(h1_income - tax_free, 0)
  - q2_monthly_base: max((h1_taxable - q1_base_used) / 3, monthly_floor)
  - q2_tb_month: q2_monthly_base * 18.5 / 100
  - q2_szocho_month: q2_monthly_base * 13 / 100
expected:
  q1_income: 1650000
  q1_taxable: 0
  q1_base_used: 968400
  h1_income: 4435200
  h1_taxable: 2498400
  q2_monthly_base: 510000
  q2_tb_month: 94350
  q2_szocho_month: 66300
```

## Ask the client first

1. Do you have a job of at least 36 hours a week, or are you a full-time student or a pensioner? This sets whether the monthly floor applies at all.
2. Does your main personal activity need at least secondary education or a secondary vocational qualification? That sets the floor at HUF 373,200 instead of HUF 322,800.
3. Which income tax regime are you in (flat-rate, real-cost, KATA), and what was your draw or flat-rate income each quarter?
4. Any months on sick pay, maternity or childcare benefits, or suspension, and their exact dates?
5. Are you also a working member of a company, and which one pays the floor?
6. Do you work in another country or hold an A1 certificate?

## Sources

| Source | URL | Read on |
|---|---|---|
| Tbj., Act CXXII of 2019 (social security), 4. §, 10. §, 23.-27. §, 34. §, 38.-40. §, 42. §, 77. §, 80.-81. §, version in force from 2026-10-01 | https://njt.jog.gov.hu/jogszabaly/2019-122-00-00 | 2026-10-23 |
| Szocho tv., Act LII of 2018 (social contribution tax), 1. §, 2. §, 5. §, 6. §, 8.-9. §, 13. §, 19. §, 34. §; 8. § (1) and (3) as amended by Act LXXXIV of 2025, 28. § (no 112.5% multiplier from 2026-01-01) | https://njt.jog.gov.hu/jogszabaly/2018-52-00-00 | 2026-10-23 |
| Szja tv., Act CXVII of 1995 (personal income tax), 1. számú melléklet 4.48. | https://njt.jog.gov.hu/jogszabaly/1995-117-00-00 | 2026-10-23 |
| Kata tv., Act XIII of 2022, 8. § | https://njt.jog.gov.hu/jogszabaly/2022-13-00-00 | 2026-10-23 |
| Art., Act CL of 2017 (tax procedure), 50. §, 52. §, 209. §, 212. §, 215. §, 220.-221. § | https://njt.jog.gov.hu/jogszabaly/2017-150-00-00 | 2026-10-23 |
| Government Decree 426/2025. (XII. 23.) on the 2026 minimum wage and guaranteed minimum wage | https://njt.jog.gov.hu/jogszabaly/2025-426-20-22 | 2026-10-23 |
| NAV information sheet 3, Egyéni vállalkozók szja- és járulékkötelezettsége (2026-08-31) | https://nav.gov.hu/pfile/file?path=/ugyfeliranytu/nezzen-utana/inf_fuz/2026/03.-Az-egyeni-vallalkozok-szja--es-jarulekkotelezettsege-2026.-08.-31. | 2026-10-23 |
| NAV information sheet 100, Az egyéni vállalkozók átalányadózásának alapvető szabályai (2026-02-20) | https://nav.gov.hu/pfile/file?path=/ugyfeliranytu/nezzen-utana/inf_fuz/2026/100.-Az-egyeni-vallalkozok-atalanyadozasanak-alapveto-szabalyai-2026.-02.-20 | 2026-10-23 |
| NAV information sheet 99, Kisadózó vállalkozók tételes adója (2026-02-20) | https://nav.gov.hu/pfile/file?path=/ugyfeliranytu/nezzen-utana/inf_fuz/2026/99.-Kisadozo-vallalkozok-teteles-adoja-kata-2026.-02.-20 | 2026-10-23 |
| NAV information sheet 91, Az egészségügyi szolgáltatási járulék (2026-01-09) | https://nav.gov.hu/pfile/file?path=/ugyfeliranytu/nezzen-utana/inf_fuz/2026/91.-informacios-fuzet---az-egeszsegugyi-szolgaltatasi-jarulek-2026.01.09 | 2026-10-23 |
| NAV, notice on the central bank base rate (25 August 2026: 5.50% from 26 August 2026) | https://nav.gov.hu/ugyfeliranytu/jegybank | 2026-10-23 |
| MNB, Monetary Council statement of 20 October 2026 (base rate held at 5.50%) | https://www.mnb.hu/monetaris-politika/a-monetaris-tanacs/kozlemenyek/2026/kozlemeny-a-monetaris-tanacs-2026-oktober-20-i-uleserol | 2026-10-23 |

Not yet confirmed: NAV information sheet 12 on company members (társas vállalkozó) was not read, so their part-month, multiple-company and suspension rules are left out; voluntary pension top-ups and agreements for extra insurance (megállapodás) are not covered.

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
