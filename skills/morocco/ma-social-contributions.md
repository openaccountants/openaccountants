---
name: ma-social-contributions
description: "Morocco social contributions for tax year 2026: CNSS, AMO and pension cover for self-employed workers (TNS), auto-entrepreneurs, CPU payers and those who hire. Covers the flat income base set by category decree, the multiples for traders, artisans and accounts-keeping individuals, registration, payment, refunds of over-paid contributions, and the employer and employee split. Use for CNSS auto-entrepreneur, AMO Maroc, cotisation CNSS indépendant, TNS, retraite TNS, couverture sociale. CNSS rates are the latest we could read and are marked unverified for 2026. Out of scope: payslips and IR on salaries (morocco-payroll), auto-entrepreneur tax (ma-auto-entrepreneur), CPU (ma-cpu)."
version: 1.1
jurisdiction: MA
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - social-contributions-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Morocco social contributions, tax year 2026

Keep Moroccan terms (CNSS, AMO, TNS, retraite, SMIG, DGI) and reply in the user's language: English, French or Darija.

## Who this applies to

Morocco is extending cover to all workers under framework Law 09-21. Three groups, three mechanics. Place the user first.

- **TNS:** self-employed people who are neither employees nor auto-entrepreneurs, brought in category by category. Law 98-15 sets the AMO scheme, Law 99-15 the pension scheme, and a decree for each category sets its flat income. Decrees read: traders and artisans keeping accounts (2-21-751, amended by 2-22-338), individuals keeping accounts (the decree in BO 7376 of 6 Feb 2025, amended by 2-22-859), owners of artisanal fishing boats (2-22-337), plus further category decrees in the same issue. Reported also covered: CPU payers (see `ma-cpu`), health, legal and other regulated professions. Confirm a named profession against its decree. Never move one category's base to another. If the category decree is not found, ask; do not assume a base. Treat affiliation as mandatory until the decree says otherwise.
- **Auto-entrepreneurs:** cover under decree 2-21-928, amended by 2-22-208. See `ma-auto-entrepreneur`.
- **Anyone who hires:** ordinary CNSS on real salary, separate from the owner's own cover. Payslip mechanics are in `morocco-payroll`. An owner who hires has two CNSS relationships.

## Rates, bands and thresholds

| Item | Rate or amount | Conditions | Year | Source URL |
|---|---|---|---|---|
| TNS AMO, active | unverified for 2026: 6.37% | On flat income | 2024 | https://www.cleiss.fr/docs/cotisations/maroc.html |
| TNS pension | unverified for 2026: 10% | On flat income | 2024 | same |
| TNS AMO, pensioners | unverified for 2026: 4.52% of base pensions | Taken by the payer. Reported by a search result for cnss.ma; page not read | not read | unverified |
| Flat income, general band | unverified for 2026: 1.75 to 2.75 times SMIG | CLEISS summary. The decrees below show other multiples for some categories, so use the decree | 2024 | https://www.cleiss.fr/docs/cotisations/maroc.html |
| Traders, artisans keeping accounts, simplified net result | 1 times the value | Value = SMIG times normal annual non-agricultural hours. Decree 2-21-751 art. 4 as amended; text elided in the BO, confirm the original | 2026 | https://www.sgg.gov.ma/BulletinOfficiel.aspx |
| Same, real net result, profit up to MAD 100,000 | 3.2 times the value | Same | 2026 | same |
| Same, real net result, profit above MAD 100,000 | 6 times the value | Same | 2026 | same |
| Individuals keeping accounts, simplified net result | 1 times the value | Art. 4 of the decree in BO 7376 | 2026 | same |
| Same, real net result, profit to MAD 50,000 | 2 times | Same | 2026 | same |
| Same, profit 50,001 to 100,000 | 3 times | Same | 2026 | same |
| Same, profit 100,001 to 150,000 | 4 times | Same | 2026 | same |
| Same, profit 150,001 to 200,000 | 5 times | Same | 2026 | same |
| Same, profit above 200,000 | 6 times | Same | 2026 | same |
| Artisanal fishing-boat owners | 0.75 times the value | Decree 2-22-337 art. 4; not those under the employee scheme | 2026 | same |
| Pension base opt-up | Higher base at registration; change once a year; ask 60 days before it takes effect | Pension only (CLEISS); return to the category base is also allowed in the yearly change | 2024 | https://www.cleiss.fr/docs/cotisations/maroc.html |
| Refund after over-estimate | Within 3 months of CNSS receiving the tax return from the DGI | Where 6 times was charged and the return shows less | 2026 | https://www.sgg.gov.ma/BulletinOfficiel.aspx |
| Auto-entrepreneur start | First day of the month after the month the first turnover return is due | Decree 2-21-928 art. 2 as amended. Registered by 31 Dec 2021: 1 Feb 2022 | 2026 | same |
| Short-term benefits, sickness, maternity, death, job loss, employer | unverified for 2026: 1.05% (of which job-loss indemnity 0.38%) | Capped at MAD 6,000 a month | 2024 | https://www.cleiss.fr/docs/cotisations/maroc.html |
| Same branch, employee | unverified for 2026: 0.52% (of which job-loss indemnity 0.19%) | Capped at MAD 6,000 | 2024 | same |
| Pension, employer | unverified for 2026: 7.93% | Capped at MAD 6,000 | 2024 | same |
| Pension, employee | unverified for 2026: 3.96% | Capped at MAD 6,000 | 2024 | same |
| Family benefits, employer only | unverified for 2026: 6.40% | No cap | 2024 | same |
| AMO base, employer | unverified for 2026: 2.26% | No cap. Employers with group medical cover from before 1 March 2006 pay only the solidarity rate, on a yearly application | 2024 | same |
| AMO solidarity, employer | unverified for 2026: 1.85% | No cap | 2024 | same |
| AMO, employee | unverified for 2026: 2.26% | No cap | 2024 | same |
| Vocational training tax (TFP), employer only | unverified for 2026: 1.60% | No cap | 2024 | same |
| Total | unverified for 2026: employer 21.09%, employee 6.74%, together 27.83% | | 2024 | same |
| Employee ceiling | unverified for 2026: MAD 6,000 a month | Capped branches only | 2024 | https://www.cleiss.fr/docs/cotisations/maroc.html |

The old table figures for auto-entrepreneurs (base 50% of services turnover, 20% of commercial turnover, MAD 300 a quarter minimum, range 1,200 to 14,400, T1 to T8 brackets, 3-month AMO waiting period) could not be read at source. They are on the last line of Sources. Do not quote them as settled and never invent a bracket amount.

## The base

**TNS.** Contribution = flat income from the category decree times the AMO rate, plus the same base times the pension rate. Contributions rest on flat income, not on real profit (art. 5 of the decrees). "No income" does not mean no contribution.

For traders, artisans and individuals keeping accounts on the real net result, the base is first set on the provisional multiple (3.2, or 2) from the month after accounts begin until the end of the month the first tax return is due. After that, if there is no update, it is 6 times, then updated from the tax return for the year. If the return shows a lower band, CNSS refunds the difference on its own initiative and informs the person.

AMO and pension are separate schemes with separate decrees. Confirm the category is in both.

**Auto-entrepreneurs.** The contribution is collected with the turnover declaration through the auto-entrepreneur portal. Default for unknown mix: ask whether services or commercial. Do not compute a bracket.

**CPU.** Bundled in the CPU; see `ma-cpu`.

**Employees.** Percentages on real salary. The ceiling applies only to short-term and pension branches. AMO, family benefits and TFP run on full salary. This is the key contrast with TNS.

## Deadlines and filing

**TNS.** 1. Ask for registration on the CNSS electronic platform, at an agency, or through a partner network listed on the CNSS site, by the last day of the month in which registration takes effect (art. 2 of the fishing-boat decree; check the category's own decree). 2. Registration takes effect on the first of the month after conditions are met (art. 3, same). 3. Attach the documents the regulations require and keep the receipt. 4. Pay monthly from the first day of the month in which the contribution falls due (art. 6 of the category decrees read). The old skill said quarterly; the decrees read say monthly, so follow the decree and confirm the category. Portal steps are not confirmed.

**Auto-entrepreneurs.** 1. Registration in the national register brings CNSS affiliation. 2. Contributions go with the turnover return, including nil returns; dates in `ma-auto-entrepreneur`.

**Employers.** 1. Register the business with CNSS, get the affiliation number. 2. Each month, file on Damancom and pay, taking the employee share from pay. Steps and the unverified deadline are in `morocco-payroll`.

## Penalties and interest

No official text on CNSS surcharges for TNS or auto-entrepreneurs was read, so no figure is given here. For employers see the unverified row in `morocco-payroll`. Arrears and loss of benefit rights go to a Moroccan expert-comptable.

## Cross-border points

Work abroad, foreign self-employed people in Morocco, detachment and social security agreements are not covered here: refer them, and ask which country's cover applies now.

## Two worked examples that recompute

Rates are those marked unverified above. Bases are inputs, not 2026 SMIG figures.

**Example 1: TNS with a monthly flat income of MAD 6,000 from the category decree.** AMO 382.20, pension 600, monthly 982.20, or 2,946.60 a quarter.

```oa-check
name: TNS on flat income 6000
inputs:
  base: 6000
steps:
  - amo: base * 0.0637
  - pension: base * 0.10
  - monthly: amo + pension
  - quarter: monthly * 3
expected:
  monthly: 982.20
  quarter: 2946.60
```

**Example 2, a decision: an individual on real net result, charged at 6 times, whose return shows profit of MAD 120,000. Should they chase CNSS or wait?** With a monthly value of 3,000 as a stand-in, 6 times costs 2,946.60 a month and 4 times costs 1,964.40. The gap is 982.20 a month. CNSS refunds without a request within 3 months of getting the return from the DGI, so file the return first. If the refund has not arrived after that, follow up.

```oa-check
name: Six times against four times
inputs:
  value: 3000
  rate: 0.1637
steps:
  - charged: value * 6 * rate
  - due: value * 4 * rate
  - refund_month: charged - due
expected:
  charged: 2946.60
  due: 1964.40
  refund_month: 982.20
```

**Case 3: owner hires an assistant at MAD 8,000.** Employee: capped 268.80 plus AMO 180.80. Employer: capped 8.98% of 6,000 is 538.80, family 512, AMO 328.80, TFP 128: 1,507.60. Filed monthly. The owner's own cover stays on its own track.

Rules for every answer in this skill:

- Do not apply the MAD 6,000 ceiling to AMO, family benefits or TFP.
- Do not mix TNS or auto-entrepreneur self-cover with the employer and employee computation. A person who hires has both, computed separately.
- Do not assume that no income means no contribution.
- Do not advise on payroll mechanics, IR withholding, VAT or company forms here. Route to `morocco-payroll`, `morocco-professional-income-tax` or `morocco-vat`.
- Do not confirm a profession's start date without its decree.
- If the activity mix of an auto-entrepreneur is unknown, ask. Do not choose a base.
- If the category or flat income is unknown, give the formula and ask for the decree. Do not guess the band.
- If the person has any staff, assume employer CNSS registration and the monthly Damancom filing are due, separately from the owner's own cover.
- Whether a category is in AMO only or in both AMO and pension decides the rate: AMO alone is 6.37%, both are 16.37%, on the unverified rates above. Check which applies before quoting a total.
- Present every computation with its assumptions and open items, so the reader can see what still rests on an unverified rate.

**Case 4: test answers.** Employee on MAD 10,000: only the capped branches stop at 6,000. CPU payer who hires: own CPU cover plus employer CNSS. Auto-entrepreneur at nil turnover: still files; amount from the portal.

## Ask the client first

1. Which group: TNS (which profession), auto-entrepreneur, CPU, employee?
2. Tax regime: simplified or real net result, and last year's net profit.
3. When did accounts or activity start?
4. Services or commercial activity, and turnover, if auto-entrepreneur.
5. Any staff?
6. For pension planning: does the person want a base above the category flat income?

Escalate to a Moroccan expert-comptable: unclear roll-out or start date, opting up, leaving the auto-entrepreneur regime, arrears, pension vesting (the old skill's 3,240 days is not confirmed), cross-border cases.

## Sources

| Source | URL | Read on |
|---|---|---|
| Bulletin officiel 7376, 6 Feb 2025 (French translation), decrees 2-22-208, 2-22-337, 2-22-338, 2-22-858, 2-22-859 read in part; found from the listing page, PDF held locally | https://www.sgg.gov.ma/BulletinOfficiel.aspx | 2026-11-01 |
| CLEISS, Les cotisations au Maroc, table at 1 January 2024 (French public body, not a Moroccan source) | https://www.cleiss.fr/docs/cotisations/maroc.html | 2026-11-01 |
| cnss.ma, failed: no connection from script or browser | https://www.cnss.ma | not read, connection failed 2026-11-01 |

Not yet confirmed: every rate and the ceiling for 2026; SMIG for 2026 (reported at MAD 17.92 an hour by press, decree text not read) and the annual hours; whether Finance Law 2026 or later decrees changed any multiple; decree list per profession and each profession's start date (doctors, pharmacists, dentists, midwives, physiotherapists, nurses, opticians, notaries, adouls, lawyers, bailiffs, accountants, architects, engineers); TNS pensioner rate; TNS portal steps and penalty; auto-entrepreneur 50% and 20% bases, MAD 300 minimum, 1,200 to 14,400 range, T1 to T8 brackets, 3-month AMO waiting period, decree 2.21.477 reference; pension vesting at 3,240 days; decree numbers 2-18-622 and 2-18-623 as the rate source.

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
