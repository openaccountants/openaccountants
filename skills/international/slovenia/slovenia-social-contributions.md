---
name: slovenia-social-contributions
description: "Slovenian social security contributions (prispevki za socialno varnost) for tax year 2026. Covers the rates for employees (22.1%) and employers (16.1%), the long-term care contribution in force since 1 July 2025 (1% + 1% on wages, 2% for the self-employed), the flat compulsory health contribution (EUR 39.36 a month from 1 March 2026), the minimum base for employees (EUR 1,521.62), and the self-employed (s.p.) and owner-manager bases: profit less 25%, at least 60% (90% for owner-managers) and at most 3.5 times the 2025 average wage of EUR 2,536.03, the relief for new s.p., the monthly OPSV return and payment by the 20th, and fines. Trigger phrases: Slovenia social security, prispevki s.p. 2026, zavarovalna osnova, OPSV, POPSV, prispevek za dolgotrajno oskrbo, OZP, minimalna osnova samozaposleni. Out of scope: the monthly gross-to-net and REK-O (slovenia-payroll), income tax on the s.p. profit and normed expenses (slovenia-income-tax), postings and A1 (si-cross-border)."
version: 0.4
jurisdiction: SI
tax_year: 2026
last_updated: 2026-10-30
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Slovenia social security contributions (2026)

> **Source-cited draft.** Drafted from the Social Security Contributions Act (ZPSV), the Pension and Disability Insurance Act (ZPIZ-2), the Health Care and Health Insurance Act (ZZVZZ), the Long-Term Care Act (ZDOsk-1) and the Tax Procedure Act (ZDavP-2), as consolidated on pisrs.si, with the 2026 bases and amounts from the Financial Administration (FURS) and the Health Insurance Institute (ZZZS), read on 2026-10-24. No accountant has reviewed it. Do not file or pay from it without review by a qualified Slovenian professional.

Contribution period: the calendar month. Authority: the Financial Administration (FURS) assesses and collects all contributions through eDavki. The ZPIZ (pensions) and the ZZZS (health and long-term care) receive them. Currency: euro. The employee's monthly gross-to-net, the REK-O and withholding tax are in `slovenia-payroll`. The income tax on an s.p. profit and the normed-expense regime are in `slovenia-income-tax`.

## Who this applies to

- **Employees and employers.** Everyone in an employment relationship in Slovenia, and their employers (ZPIZ-2 art. 14; ZZVZZ art. 15(1)(1)). The employer calculates and pays both shares in the REK-O (ZDavP-2 art. 352(2) and (3)). See `slovenia-payroll`.
- **Self-employed (samozaposleni).** Sole proprietors (s.p.) and other persons carrying on an independent business or profession in Slovenia, insured full time (ZPIZ-2 art. 15). Also people registered as self-employed abroad if EU rules make Slovenian law apply (art. 15(2)). They file and pay their own contributions monthly.
- **Owner-managers.** Partners and shareholders who manage their company and are not insured on another basis (ZPIZ-2 art. 16). Same rates as the self-employed, on a higher minimum base.
- **Farmers** (ZPIZ-2 art. 17) and **pensioners** (1% long-term care on the net pension, ZZZS table) are only touched on here.
- **Not covered here:** voluntary insurance, part-time self-employment alongside a job (dopolnilna dejavnost), contract and student work, and the extra contribution for insurance periods counted with an increase (ZPSV art. 10).

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Pension and disability, insured person / employer | 15.50% / 8.85% | 2026 | ZPSV art. 8, [pisrs.si](https://pisrs.si/pregledPredpisa?id=ZAKO984) |
| Health, insured person / employer | 6.36% / 6.56% | 2026 | ZPSV art. 11(1) |
| Injury at work, employer (the self-employed pay it too) | 0.53% | 2026 | ZPSV art. 12(1) |
| Parental care, insured person / employer | 0.10% / 0.10% | 2026 | ZPSV art. 13 |
| Employment, insured person / employer | 0.14% / 0.06% | 2026 | ZPSV art. 14 |
| Total, employee / employer | 22.10% / 16.10% | 2026 | ZPSV arts. 8, 11 to 14 |
| Total paid by a self-employed person or owner-manager (both shares) | 38.20% of the base, plus long-term care and the OZP | 2026 | ZPSV arts. 8, 11 to 14; FURS SZ tables |
| Long-term care, employee / employer | 1% / 1% | from 1 July 2025 | ZDOsk-1 arts. 56(1) and 137, [pisrs.si](https://pisrs.si/pregledPredpisa?id=ZAKO8819) |
| Long-term care, self-employed, owner-manager, farmer | 2% | from 1 July 2025 | ZDOsk-1 art. 56(2) |
| Long-term care, pensioners | 1% of the net pension | from 1 July 2025 | ZDOsk-1 arts. 56(1) and (10); ZZZS table, [zzzs.si](https://zavezanec.zzzs.si/fileadmin/user_upload/dokumenti/zavezanec/do/preglednica_zavarovanci__do_furs__v2.pdf) |
| Compulsory health contribution (OZP) | EUR 39.36 a month from 1 March 2026; EUR 37.17 before | 2026 | ZZVZZ art. 48; Uradni list RS 16/26 as cited by FURS, [fu.gov.si](https://www.fu.gov.si/fileadmin/Internet/Davki_in_druge_dajatve/Podrocja/Prispevki_za_socialno_varnost/Samozaposleni/SZ_10_2026.xlsx) |
| Average monthly gross wage, 2025 (used from the February 2026 contributions) | EUR 2,536.03 | 2026 | FURS SZ tables, [fu.gov.si](https://www.fu.gov.si/davki_in_druge_dajatve/podrocja/prispevki_za_socialno_varnost/osnove_za_placilo_ter_zneski_prispevkov_za_socialno_varnost/) |
| Average monthly gross wage, 2024 (used for January 2026) | EUR 2,394.92 | 2026 | FURS table SZ 1/2026 |
| Minimum base, employees (60%) | EUR 1,521.62 | 2026 | ZPIZ-2 art. 144(4), [pisrs.si](https://pisrs.si/pregledPredpisa?id=ZAKO6280) |
| Minimum base, self-employed and farmers (60%) | EUR 1,521.62 (January 2026: EUR 1,436.95) | 2026 | ZPIZ-2 art. 145(4); FURS SZ tables |
| Minimum base, owner-managers (90%) | EUR 2,282.43 | 2026 | ZPIZ-2 art. 145(4); FURS table LZP 10/2026 |
| Maximum base, self-employed and owner-managers (3.5 times) | EUR 8,876.11 (January 2026: EUR 8,382.22) | 2026 | ZPIZ-2 art. 145(5); FURS SZ tables |
| Maximum base, employees | none | 2026 | ZPIZ-2 art. 144(1) |
| Monthly total for an s.p. on the minimum base / maximum base | EUR 651.04 / 3,607.57 (from March 2026) | 2026 | FURS table SZ 10/2026 |
| Monthly total for an owner-manager on the minimum base | EUR 956.91 (from March 2026) | 2026 | FURS table LZP 10/2026 |
| New s.p. relief | 50% of the pension contributions in the first 12 months, 30% in the next 12; the state pays the relieved part | 2026 | ZPIZ-2 art. 145(14) and (15) |
| Late payment interest | 10.15% a year from 1 January 2026; 10.40% from 1 July 2026 | 2026 | ZDavP-2 art. 96; ZPOMZO-1 art. 2; [Uradni list RS 2/2026](https://www.uradni-list.si/glasilo-uradni-list-rs/vsebina/2026-01-0011); [Uradni list RS 1124/2026](https://pisrs.si/api/uradni-list/objava/u20261124.pdf) |

## The taxable base

**Employees.** Gross pay and all other pay from employment, with no ceiling (ZPSV art. 3; ZPIZ-2 art. 144(1) and (2)). If the pay is below EUR 1,521.62 the employer pays the employee's share on the difference (ZPIZ-2 arts. 144(4) and 152(2); ZZVZZ art. 50). Worked through in `slovenia-payroll`.

**Self-employed (s.p.): the insurance base.** Take the profit for the previous year as set under the income tax rules, before the contributions charged and before tax-base increases and reductions. Divide by 12. Reduce it by 25% (ZPIZ-2 art. 145(2)). The result is the insurance base (zavarovalna osnova), but never less than 60% of the average annual wage (EUR 1,521.62) and never more than 3.5 times it (EUR 8,876.11) (art. 145(4) and (5)).

- **When the base changes.** FURS sets the new base from the prior-year tax return, at the latest for April (art. 145(6)). It applies until the next one (art. 145(8)).
- **New s.p.** pays on the minimum base from the start, unless insured on the same basis in the six months before (art. 145(9)).
- **Lower base on request.** If the s.p. expects a lower profit this year, they can pay on a base up to 20% lower, but never below the minimum. If the actual profit then shows a base more than 20% above the reduced one, the next base is the actual one plus 20% (art. 145(10) and (11)).
- **Higher base on request.** Any s.p. can choose a base above their own, up to the maximum (art. 145(16)).
- **New s.p. relief.** In the first 12 months after first registration, 50% of the pension contributions is relieved; in the next 12 months, 30%. The state pays the relieved part to the ZPIZ (art. 145(14) and (15)).

**Normed-expense s.p. (normiranec).** The profit for the base is the profit set under the income tax rules (ZPIZ-2 art. 145(2)), so for an s.p. on normed expenses it is revenue less the normed expenses. From tax year 2026 ZPZR (Uradni list RS 91/25, amended by ZPZR-A 32/26) sets the normed-expense entry and exit tests (two-year average revenue of EUR 120,000, 85,000 or 50,000) and the final income tax (20% up to a base of EUR 72,000, or EUR 33,000 if not full-time self-insured, and 35% above) (ZPZR arts. 6 and 7). ZPZR does not change the contribution base: its only contribution rule is for the employees' winter allowance (ZPZR art. 5). The normed expenses themselves still come from ZDoh-2 art. 59 (ZPZR art. 6(3)). The full rules are in `slovenia-income-tax`.

**Owner-managers.** All pay received for managing and working counts as the profit. The minimum base is 90% of the average wage (EUR 2,282.43) and the maximum is the same EUR 8,876.11 (ZPIZ-2 art. 145(3) to (5)).

**Long-term care.** Due on the same base as the health contribution (ZDOsk-1 art. 56(4)). An s.p. or owner-manager pays 2% alone (art. 56(2)).

**OZP.** A flat EUR 39.36 a month from 1 March 2026, for every insured person, whatever their income (ZZVZZ art. 48). An s.p. pays it in the monthly contributions.

**Income tax.** Contributions paid by the self-employed are expenses in computing profit (ZPSV art. 7). Employee contributions, including the 1% long-term care contribution and the OZP, reduce the employee's tax base: they are compulsory social security contributions the employee must pay (ZDoh-2 art. 41(1); ZPSV art. 1; ZZVZZ art. 48; ZDOsk-1 arts. 51(2) and 56.a(1)). See `slovenia-payroll`.

## Deadlines and filing

| Obligation | Deadline | Source |
|---|---|---|
| Employees: contributions calculated in the REK-O | the REK-O on the pay date; payment within 5 days of it | ZDavP-2 arts. 283(1), 284(1), 353(2) |
| Self-employed and owner-managers: FURS posts a prefilled contributions return (POPSV) in eDavki | by the 10th of the month for the previous month | ZDavP-2 art. 353.a(4) |
| Self-employed: file the contributions return (OPSV) if the POPSV is wrong, incomplete or missing | by the 15th of the month for the previous month | ZDavP-2 arts. 353(1) and 353.a(5) and (6) |
| Self-employed: pay the contributions | by the 20th of the month for the previous month | ZDavP-2 art. 353(1) |
| If the s.p. does not file an OPSV, the POPSV counts as the return | at the 15th | ZDavP-2 art. 353.a(5) |

A POPSV that is right needs no action except payment by the 20th. The October 2026 contributions are filed by 15 November 2026 and paid by 20 November 2026.

## Penalties and interest

- **Employer does not file the REK-O properly.** Fine EUR 1,200 to 15,000 for a company, EUR 3,200 to 30,000 for a medium or large company, EUR 800 to 10,000 for an s.p. employer (ZDavP-2 art. 397(1) point 2).
- **Self-employed person does not file the OPSV properly.** Fine EUR 800 to 10,000 for an s.p. (ZDavP-2 art. 397(1) point 36). The fine for an individual who gives untrue or incomplete data in a contributions return is EUR 400 to 5,000 (art. 395 point 4).
- **Responsible persons.** The responsible person of a company is fined EUR 600 to 4,000, or EUR 800 to 4,000 in a medium or large company (art. 397(3)); of an s.p., EUR 400 to 4,000 (art. 397(2)).
- **Late payment.** Late interest at 10.15% a year from 1 January 2026 and 10.40% from 1 July 2026 (ZDavP-2 art. 96(1); ZPOMZO-1 art. 2). ZPSV art. 15 applies ZDavP-2 to contributions.
- **No relief on request.** The OZP and the long-term care contribution cannot be written off, deferred or paid in instalments on request (ZZVZZ art. 48; ZDOsk-1 art. 56(8)).
- **Wrong base.** If the base was wrong, FURS sets the right one by decision and recalculates past contributions (ZPIZ-2 art. 145(12)).

## Cross-border points

- **Which country insures.** Within the EU, EEA and Switzerland, Regulation (EC) 883/2004 decides. A person registered as self-employed abroad is insured in Slovenia if EU rules make Slovenian law apply (ZPIZ-2 art. 15(2)). ZZZS issues the A1 certificate for postings from Slovenia.
- **Posted employees.** A Slovenian employer that posts a worker abroad keeps paying contributions on the pay for equal work in Slovenia, unless a treaty says otherwise (ZPSV art. 3(2)).
- **Insured abroad, living in Slovenia.** People insured with a foreign insurer who cannot use Slovenian long-term care benefits are outside long-term care insurance (ZDOsk-1 art. 54(5)).
- Residence, treaties and the A1 procedure are in `si-cross-border`.

## Worked examples

### Example 1: s.p. on the minimum base, October 2026

A sole proprietor in their fourth year of business had a small profit in 2025, so FURS put them on the minimum base of EUR 1,521.62. For October 2026 they owe both shares of every contribution, the 2% long-term care contribution and the OZP. FURS posts the POPSV by 10 November 2026. If it is right, the s.p. only pays, by 20 November 2026.

Pension 15.5% + 8.85%: EUR 235.85 + 134.66. Health 6.36% + 6.56%: EUR 96.78 + 99.82. Injury at work 0.53%: EUR 8.06. OZP: EUR 39.36. Long-term care 2%: EUR 30.43. Parental care 0.1% + 0.1%: EUR 1.52 + 1.52. Employment 0.14% + 0.06%: EUR 2.13 + 0.91. Total: EUR 651.04, the same as the FURS table for October 2026.

```oa-check
name: Slovenia s.p. on the minimum base EUR 1,521.62, October 2026
inputs:
  base: 1521.62
  ozp: 39.36
steps:
  - pension: round(base * 0.155, 2) + round(base * 0.0885, 2)
  - health: round(base * 0.0636, 2) + round(base * 0.0656, 2) + round(base * 0.0053, 2) + ozp
  - ltc: round(base * 0.02, 2)
  - parental: round(base * 0.001, 2) * 2
  - employment: round(base * 0.0014, 2) + round(base * 0.0006, 2)
  - total: pension + health + ltc + parental + employment
expected:
  pension: 370.51
  health: 244.02
  ltc: 30.43
  total: 651.04
```

### Example 2: high-earning s.p. capped at the maximum base

A sole proprietor on actual expenses had a 2025 profit of EUR 150,000 before contributions. FURS sets the new base from the 2025 return, at the latest for April 2026. Monthly profit is EUR 12,500. Less 25% it is EUR 9,375. That is above 3.5 times the 2025 average wage (EUR 8,876.11), so the base is capped at EUR 8,876.11.

On the capped base the October 2026 contributions are: pension EUR 2,161.34, health EUR 1,233.19 (with the OZP), long-term care EUR 177.52, parental care EUR 17.76 and employment EUR 17.76. Total: EUR 3,607.57, the same as the FURS table for the maximum base. Without the cap the s.p. would pay on EUR 9,375.

```oa-check
name: Slovenia s.p. with 2025 profit EUR 150,000, base capped at EUR 8,876.11, October 2026
inputs:
  profit: 150000
  avg_wage: 2536.03
  ozp: 39.36
steps:
  - reduced: profit / 12 * 0.75
  - min_base: round(avg_wage * 0.6, 2)
  - max_base: round(avg_wage * 3.5, 2)
  - base: min(max(reduced, min_base), max_base)
  - pension: round(base * 0.155, 2) + round(base * 0.0885, 2)
  - health: round(base * 0.0636, 2) + round(base * 0.0656, 2) + round(base * 0.0053, 2) + ozp
  - ltc: round(base * 0.02, 2)
  - parental: round(base * 0.001, 2) * 2
  - employment: round(base * 0.0014, 2) + round(base * 0.0006, 2)
  - total: pension + health + ltc + parental + employment
expected:
  reduced: 9375.00
  base: 8876.11
  pension: 2161.34
  health: 1233.19
  ltc: 177.52
  total: 3607.57
```

## Ask the client first

1. Employee, self-employed (s.p.), owner-manager, or more than one? The base and who pays differ.
2. For an s.p.: the date of first registration (the 24-month relief) and whether they were insured on the same basis in the six months before.
3. For an s.p.: last year's profit, and whether it was on actual or normed expenses. This sets the base from April.
4. Does the s.p. want to pay on a lower base (up to 20% less) or a higher one?
5. Is the person insured in another EU or EEA country (A1 certificate), or posted from Slovenia?
6. Which month does each amount relate to? The OZP and the average wage changed during 2026.

## Sources

| Source | URL | Read on |
|---|---|---|
| Social Security Contributions Act (ZPSV), consolidated NPB 14: arts. 1, 3, 6, 7, 8, 10 to 15 | https://pisrs.si/pregledPredpisa?id=ZAKO984 | 2026-10-24 |
| Pension and Disability Insurance Act (ZPIZ-2), consolidated NPB 27 to Uradni list RS 90/25: arts. 14 to 17, 144, 145, 152 | https://pisrs.si/pregledPredpisa?id=ZAKO6280 | 2026-10-24 |
| Act on the Right to a Winter Allowance and the Reform of Normed Expenses (ZPZR), Uradni list RS 91/25 as amended by ZPZR-A 32/26, unofficial consolidated text NPB 1: arts. 5, 6, 7 and 21 | https://pisrs.si/pregledPredpisa?id=ZAKO9359 | 2026-10-30 |
| Health Care and Health Insurance Act (ZZVZZ), consolidated NPB 42: arts. 48, 50 | https://pisrs.si/pregledPredpisa?id=ZAKO213 | 2026-10-24 |
| Long-Term Care Act (ZDOsk-1), consolidated NPB 2: arts. 51, 54, 55, 56, 56.a, 137 | https://pisrs.si/pregledPredpisa?id=ZAKO8819 | 2026-10-24 |
| Personal Income Tax Act (ZDoh-2): art. 41 | https://pisrs.si/pregledPredpisa?id=ZAKO4697 | 2026-10-24 |
| Tax Procedure Act (ZDavP-2), consolidated to Uradni list RS 100/25: arts. 96, 283, 284, 352, 353, 353.a, 395, 397 | https://pisrs.si/pregledPredpisa?id=ZAKO4703 | 2026-10-24 |
| Act on the Prescribed Default Interest Rate (ZPOMZO-1): art. 2 | https://pisrs.si/pregledPredpisa?id=ZAKO3695 | 2026-10-24 |
| Minister of Finance, default interest rate from 1 January 2026, Uradni list RS 2/2026 | https://www.uradni-list.si/glasilo-uradni-list-rs/vsebina/2026-01-0011 | 2026-10-24 |
| Minister of Finance, default interest rate from 1 July 2026, Uradni list RS 1124/2026 | https://pisrs.si/api/uradni-list/objava/u20261124.pdf | 2026-10-24 |
| FURS, contribution bases and amounts 2026 (index page) | https://www.fu.gov.si/davki_in_druge_dajatve/podrocja/prispevki_za_socialno_varnost/osnove_za_placilo_ter_zneski_prispevkov_za_socialno_varnost/ | 2026-10-24 |
| FURS, self-employed table October 2026 (SZ 10/2026); also January, February and March 2026 | https://www.fu.gov.si/fileadmin/Internet/Davki_in_druge_dajatve/Podrocja/Prispevki_za_socialno_varnost/Samozaposleni/SZ_10_2026.xlsx | 2026-10-24 |
| FURS, owner-manager table October 2026 (LZP 10/2026) | https://www.fu.gov.si/fileadmin/Internet/Davki_in_druge_dajatve/Podrocja/Prispevki_za_socialno_varnost/Druzbeniki-lastniki_zasebnih_podjetij/LZP_10_2026.xlsx | 2026-10-24 |
| ZZZS, long-term care contribution table for insured persons supervised by FURS | https://zavezanec.zzzs.si/fileadmin/user_upload/dokumenti/zavezanec/do/preglednica_zavarovanci__do_furs__v2.pdf | 2026-10-24 |

Not yet confirmed: the Uradni list RS 16/26 order setting the OZP at EUR 39.36 was not read (the figure is from the FURS 2026 tables, which cite it); how FURS computes the new s.p. relief in practice (ZPIZ-2 art. 145(14) applies it to contributions on the art. 145(2) base; no FURS worked figure was read); the rules for part-time self-employment alongside a job (dopolnilna dejavnost) and for farmers; the parental care and employment acts (ZSDP-1, ZUTD) were not read for their own base rules, so this skill relies on the ZPSV rates and the FURS tables.

> Contributed by Michael Cutajar.

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
