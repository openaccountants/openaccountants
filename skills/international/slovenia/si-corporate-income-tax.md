---
name: si-corporate-income-tax
description: "Slovenian corporate income tax (davek od dohodkov pravnih oseb, DDPO) for tax year 2026. Covers who pays (resident companies on worldwide profit, non-residents through a Slovenian PE), the 22% rate for 2024 to 2028 under ZORZFS art. 64 (the ZDDPO-2 art. 60 rate is 19%), the taxable base and non-deductible items, the 50% rules for entertainment and provisions, maximum depreciation rates, the R&D (100%), investment (40%) and digital and green (40%) reliefs, losses (five years, 50% of the base) and the 63% overall cap in art. 59.a, the interest limitation rule (30% of EBITDA or EUR 3 million), advance payments, the return three months after year end, and fines and interest. Trigger phrases: DDPO, davek od dohodkov pravnih oseb, Slovenia corporate tax, d.o.o. tax, akontacija davka, davčna izguba. Out of scope: si-cross-border, si-transfer-pricing, slovenia-income-tax, slovenia-vat-return, slovenia-payroll."
jurisdiction: SI
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-24
version: 0.2
verified_by: pending
trust_label: Built by Michael Cutajar and the OpenAccountants team
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Slovenia corporate income tax (DDPO), tax year 2026

This skill computes the Slovenian corporate income tax of a company for a tax period in 2026. The tax is "davek od dohodkov pravnih oseb" (DDPO). The law is the Corporate Income Tax Act (ZDDPO-2). The return, advance payments and fines are in the Tax Procedure Act (ZDavP-2). The Financial Administration (FURS) runs the tax through eDavki.

## Who this applies to

- **Taxpayers.** Every legal person under Slovenian or foreign law (ZDDPO-2 art. 3(1)). A foreign partnership or association without legal personality is also a taxpayer if it is not taxed under the personal income tax act (art. 3(2)). The state and municipalities are not taxpayers (art. 3(3)).
- **Residents.** A company is resident if its seat or its place of effective management is in Slovenia (art. 5(1)). Residents pay tax on worldwide income (art. 4(1)).
- **Non-residents.** They pay tax only on Slovenian-source income (art. 4(2)). Their business profit is taxed through the return only when earned in or through a Slovenian permanent establishment (arts. 11 and 12(4)). Other Slovenian-source income is reached by withholding under art. 70. Both are covered in si-cross-border.
- **Non-profit bodies.** Institutes, societies, foundations, religious communities, political parties, chambers and unions set up for non-profit work pay no tax on that work, but pay on profit-making activity (art. 9).
- **Tax period.** The calendar year. A company may choose a business year that differs from the calendar year, of no more than 12 months, and must keep it for at least three years (art. 10).
- **Out of this skill.** Sole traders (s.p.) pay personal income tax: see slovenia-income-tax. Pricing between related parties: see si-transfer-pricing.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| General rate | 22% of the tax base | 2024 to 2028 (so 2026) | ZORZFS art. 64(1), https://pisrs.si/pregledPredpisa?id=ZAKO8910 |
| Rate in ZDDPO-2 itself | 19% (displaced for 2024 to 2028) | from 2029 unless changed | ZDDPO-2 art. 60, https://pisrs.si/pregledPredpisa?id=ZAKO4687 |
| Qualifying investment funds | 0% if at least 75% of prior-year realised profit is distributed by 30 November | 2026 | ZDDPO-2 art. 61(1), https://pisrs.si/pregledPredpisa?id=ZAKO4687 |
| Pension funds; pension plans of insurers | 0% | 2026 | ZDDPO-2 art. 61(2) and (3), https://pisrs.si/pregledPredpisa?id=ZAKO4687 |
| Entertainment (reprezentanca); supervisory board costs | 50% deductible | 2026 | ZDDPO-2 art. 31, https://pisrs.si/pregledPredpisa?id=ZAKO4687 |
| Provisions for warranties, restructuring, onerous contracts, pensions, jubilee awards, retirement pay | 50% deductible when set up | 2026 | ZDDPO-2 art. 20(2), https://pisrs.si/pregledPredpisa?id=ZAKO4687 |
| Impairment of trade receivables | deductible up to the lower of the 3-year average of actual write-offs and 1% of taxable revenue | 2026 | ZDDPO-2 art. 21(1), https://pisrs.si/pregledPredpisa?id=ZAKO4687 |
| Depreciation, buildings incl. investment property | max 3% a year, straight line | 2026 | ZDDPO-2 art. 33(5), https://pisrs.si/pregledPredpisa?id=ZAKO4687 |
| Depreciation, parts of buildings | max 6% | 2026 | ZDDPO-2 art. 33(5), https://pisrs.si/pregledPredpisa?id=ZAKO4687 |
| Depreciation, equipment, vehicles, machinery | max 20% | 2026 | ZDDPO-2 art. 33(5), https://pisrs.si/pregledPredpisa?id=ZAKO4687 |
| Depreciation, parts of equipment and research equipment | max 33.3% | 2026 | ZDDPO-2 art. 33(5), https://pisrs.si/pregledPredpisa?id=ZAKO4687 |
| Depreciation, computers, hardware and software | max 50% | 2026 | ZDDPO-2 art. 33(5), https://pisrs.si/pregledPredpisa?id=ZAKO4687 |
| Depreciation, perennial plantations; other investments | max 10% | 2026 | ZDDPO-2 art. 33(5), https://pisrs.si/pregledPredpisa?id=ZAKO4687 |
| Depreciation, breeding herd | max 20% | 2026 | ZDDPO-2 art. 33(5), https://pisrs.si/pregledPredpisa?id=ZAKO4687 |
| Small asset write-off | full cost if unit cost is no more than EUR 500 | 2026 | ZDDPO-2 art. 33(6), https://pisrs.si/pregledPredpisa?id=ZAKO4687 |
| Goodwill amortisation | not deductible | 2026 | ZDDPO-2 art. 33(8), https://pisrs.si/pregledPredpisa?id=ZAKO4687 |
| R&D relief | 100% of R&D spend, unused part carried 5 periods | 2026 | ZDDPO-2 art. 55, https://pisrs.si/pregledPredpisa?id=ZAKO4687 |
| Investment relief | 40% of investment in equipment and intangibles, unused part carried 5 periods | 2026 | ZDDPO-2 art. 55.a, https://pisrs.si/pregledPredpisa?id=ZAKO4687 |
| Digital and green transition relief | 40% of qualifying spend, unused part carried 5 periods | 2026 | ZDDPO-2 art. 55.c, https://pisrs.si/pregledPredpisa?id=ZAKO4687 |
| Employment relief | 45% of salary (55% for a first job under age 25), first 24 months | 2026 | ZDDPO-2 art. 55.b, https://pisrs.si/pregledPredpisa?id=ZAKO4687 |
| Donations relief | up to 1% of taxable revenue, plus 0.2% and 3.8% for listed purposes | 2026 | ZDDPO-2 art. 59, https://pisrs.si/pregledPredpisa?id=ZAKO4687 |
| Tax losses | carried forward 5 periods; use limited to 50% of the period's base | losses from periods starting on or after 1 Jan 2025 | ZDDPO-2 art. 36(2) and (4), https://pisrs.si/pregledPredpisa?id=ZAKO4687 |
| Losses from periods before 2025 | usable up to and including the tax period starting in 2029 | transitional | FURS, Pokrivanje davčne izgube (Feb 2025), https://www.fu.gov.si/fileadmin/Internet/Davki_in_druge_dajatve/Podrocja/Davek_od_dohodkov_pravnih_oseb/Opis/Pokrivanje_davcne_izgube.doc |
| Overall cap on reductions | losses plus reliefs in arts. 55 to 59 may cut the base by at most 63% | 2026 | ZDDPO-2 art. 59.a, https://pisrs.si/pregledPredpisa?id=ZAKO4687 |
| Interest limitation | net borrowing costs deductible up to the higher of 30% of tax EBITDA or EUR 3,000,000 | 2026 | ZDDPO-2 art. 54.c(1), https://pisrs.si/pregledPredpisa?id=ZAKO4687 |
| Participation exemption, dividends | 100% exempt, less 5% of the exempt amount added back as costs | 2026 | ZDDPO-2 arts. 24 and 26, https://pisrs.si/pregledPredpisa?id=ZAKO4687 |
| Participation exemption, share gains | 50% exempt (holding of 8% for 6 months, one full-time employee) | 2026 | ZDDPO-2 art. 25(1), https://pisrs.si/pregledPredpisa?id=ZAKO4687 |
| Advance payments | monthly if the advance exceeds EUR 400, quarterly if not; due within 20 days after each period ends | 2026 | ZDavP-2 art. 371(2) and (3), https://pisrs.si/pregledPredpisa?id=ZAKO4703 |
| Annual return | within 3 months after the end of the tax period | 2026 | ZDavP-2 art. 358(2) and (3), https://pisrs.si/pregledPredpisa?id=ZAKO4703 |
| Balance of tax | within 30 days of the return deadline | 2026 | ZDavP-2 art. 370(2), https://pisrs.si/pregledPredpisa?id=ZAKO4703 |
| Fine, legal person, return not filed or late | EUR 1,200 to 15,000; medium or large company EUR 3,200 to 30,000 | 2026 | ZDavP-2 art. 397(1), https://pisrs.si/pregledPredpisa?id=ZAKO4703 |
| Interest on tax found in an audit | 7% a year | 2026 | ZDavP-2 art. 95, https://pisrs.si/pregledPredpisa?id=ZAKO4703 |

## The taxable base

**Starting point.** The base is profit: taxable revenue minus deductible expenses as set by the act (ZDDPO-2 art. 12(1) and (2)). Revenue and expenses come from the income statement under the accounting standards, unless the act says otherwise (art. 12(3)).

**Deductible expenses.** An expense is deductible only if needed to earn taxable revenue (art. 29(1)). It fails that test if it is not a condition or result of the business, is private in nature, or is not normal business practice (art. 29(2)).

**Not deductible at all** (art. 30(1)):
- distributions similar to dividends, including hidden profit distributions;
- covering losses of earlier years;
- private costs of owners and related persons, such as entertainment, holidays, sport and recreation, with the VAT on them (art. 30(2));
- enforcement costs of taxes, fines imposed by an authority, and taxes paid by a shareholder as an individual;
- input VAT that could have been deducted but was not;
- interest on late taxes, and interest on loans from persons in jurisdictions on the art. 8.a list;
- donations (relief instead under art. 59);
- bribes.

**Half deductible.** Entertainment of business partners (meals, entertainment, gifts) and supervisory board costs: 50% (art. 31). Listed provisions: 50% when created, the rest recognised when used or released (art. 20(2) and (3)).

**Write-downs.** Impairment of financial investments is not deductible until disposal, except for instruments at fair value through profit or loss (art. 22). Impairment of receivables is capped as in the table (art. 21(1)). Write-offs in insolvency or after failed enforcement are deductible (art. 21(6)).

**Depreciation.** Straight line, asset by asset, at no more than the rates in art. 33(5). Book depreciation above the cap is carried to later years (art. 33(2)). Assets of up to EUR 500 may be expensed at once (art. 33(6)). Goodwill amortisation is never deductible (art. 33(8)). A right-of-use asset is depreciated over the lease term (art. 33(9)).

**Salaries and staff costs.** Deductible as accrued, including benefits taxed under the personal income tax act (art. 35).

**Interest.**
- Loans from or to related parties are tested against the recognised interest rate (art. 19). See si-transfer-pricing.
- The old thin capitalisation rule in art. 32 is deleted. The limit now is art. 54.c: a company with a related person deducts net borrowing costs only up to the higher of 30% of tax EBITDA or EUR 3,000,000 (art. 54.c(1)). A related person here means a 25% link by votes, capital or profit (art. 54.c(2)).
- The rule does not apply to banks, insurers, or standalone companies that are not in a consolidated group and have no associated enterprise or PE (art. 54.c(9)). Loans concluded before 17 June 2016 and not later changed are outside it (art. 54.c(7)).

**Exempt income.**
- Dividends from a Slovenian taxpayer, an EU parent-subsidiary company, or a company paying a comparable profit tax outside the art. 8.a list are excluded from the base (art. 24(1)). 5% of the exempt dividends is added back as costs (art. 26).
- 50% of a gain on shares is exempt if the company held at least 8% for at least 6 months and employed at least one full-time person in that time (art. 25(1)). 50% of a loss on such shares is not deductible (art. 25(2)).

**Losses.**
- A tax loss is the excess of expenses over revenue under the act (art. 36(1)).
- Losses from tax periods starting on or after 1 January 2025 can be used in the next five tax periods (art. 36(2); FURS guidance on ZDDPO-2U).
- Losses from periods before 2025 ("old losses") can be used up to and including the tax period that starts in 2029 (FURS guidance, transitional rule of ZDDPO-2U).
- The oldest loss is used first (art. 36(3)).
- Loss relief in a period is limited to 50% of that period's base (art. 36(4)).
- Losses are forfeited if ownership changes by more than 50% in a period and the company either had no activity for two years before, or substantially changes its activity within two years before or after (art. 36(5)). Changes made to keep jobs or to restructure are excluded (art. 36(7)).

**Reliefs** (each is limited to the tax base of the period):
- **R&D (art. 55).** 100% of spending on in-house R&D (including dedicated R&D equipment) and bought-in R&D services. The work must be in a business plan or a separate development project. Spending funded by non-repayable public or EU grants is excluded.
- **Investment (art. 55.a).** 40% of investment in equipment and intangibles. Excluded: furniture and office equipment (computers are allowed), most motor vehicles (hybrid or electric cars and buses, and buses and trucks meeting at least EURO VI, are allowed), goodwill and real property rights. If the asset is sold within three years, the relief is clawed back (art. 55.a(6)).
- **Digital and green transition (art. 55.c).** 40% of spending on cloud computing, AI and big data, and on green technologies and energy efficiency.
- **One relief per spend.** Arts. 55, 55.a and 55.c cannot be claimed together for the same spend (arts. 55(7) and 55.c(2)).
- **Other reliefs.** Employment of young, older or shortage-occupation workers (art. 55.b), employment of disabled persons (art. 56), apprentices (art. 57), voluntary pension premiums (art. 58) and donations (art. 59).

**The 63% cap.** All reductions from losses (art. 36), from the reliefs in arts. 55 to 59, and from reliefs in other laws, together with unused reliefs brought forward, may reduce the base by at most 63% (art. 59.a). At least 37% of the base is therefore always taxed. The 50% loss limit in art. 36(4) applies inside this cap.

**Rate.** 22% of the base after reductions, for 2024 to 2028 (ZORZFS art. 64(1)). FURS confirms the 22% rate on its DDPO page.

**Foreign tax credit.** Foreign tax on foreign income in the base is credited, capped per country at the Slovenian tax on that income (arts. 62 and 63). Excess credit is not carried (arts. 66 and 67). See si-cross-border.

## Deadlines and filing

- **Annual return.** The DDPO return goes to FURS through eDavki within three months after the end of the tax period: by 31 March 2027 for calendar year 2026 (ZDavP-2 art. 358(2)). A company with a different business year files within three months after that year ends (art. 358(3)).
- **Payment of the balance.** The difference between advances paid and tax due is payable within 30 days of the return deadline (art. 370(2)). For calendar 2026 that is 30 April 2027. Overpaid tax is refunded within 30 days of the deadline.
- **Advance payments.**
  - The annual advance equals the base in the last return times the rate for the current period (art. 371(4)).
  - It is paid monthly if it is above EUR 400 and quarterly if not (art. 371(2)).
  - Each instalment falls due on the last day of its month or quarter and must be paid within 20 days after that (art. 371(3)).
  - A new company estimates its own advance and files the calculation within 8 days of registration (art. 371(7)).
  - A company whose base has changed may ask FURS to change the advance at least 30 days before an instalment is due (art. 371(9)).
- **Changing the tax period.** Tell FURS at least 45 days before the new period starts (art. 372(1)).
- **Liquidation, bankruptcy, mergers.** Special returns apply, for example within 30 days of a merger being entered in the register (art. 361(2)) or 20 days after a liquidation starts (art. 368.a(2)).
- **Withholding on outbound payments.** Paid and reported within five days of payment (art. 374). See si-cross-border.

## Penalties and interest

- **Late or missing return.** A legal person is fined EUR 1,200 to 15,000. A medium or large company is fined EUR 3,200 to 30,000. The responsible person is fined EUR 600 to 4,000, or EUR 800 to 4,000 in a medium or large company (ZDavP-2 art. 397(1) and (3)). A new company that does not calculate or file its advance is fined under the same article (art. 397(1) point 24).
- **Particularly serious offences.** If the tax at stake exceeds EUR 10,000 for a legal person, or EUR 25,000 for a medium or large company, or the act was intentional, the fine is EUR 4,500 to 100,000. For a medium or large company it is EUR 10,500 to 150,000 (art. 398(1) and (4)).
- **Late payment.** Tax not paid on time carries late interest at the rate set by the act on statutory default interest (ZDavP-2 art. 96(1)). A return or correction filed late also carries this interest, from the payment deadline to payment (art. 95.a).
- **Tax found in an audit.** Interest at 7% a year runs from the payment deadline to the date of the decision (art. 95).

## Cross-border points

- **Residence.** A company is resident if its seat or place of effective management is in Slovenia (ZDDPO-2 art. 5). A move of effective management abroad can trigger exit tax (arts. 54.a and 54.b).
- **PE profit.** A non-resident's PE is taxed on the profit it would earn as a separate taxpayer (art. 12(4)). It files the same DDPO return.
- **Withholding.** Dividends, interest, royalties and certain service fees paid abroad bear 15% withholding unless a directive or treaty applies (arts. 70 to 72).
- **Listed jurisdictions.** Interest paid to lenders in art. 8.a list jurisdictions is not deductible (art. 30(1) point 8(b)). Dividends and share gains from those jurisdictions get no exemption (arts. 24(1) point 3 and 25(3)).
- **Controlled foreign companies.** Arts. 67.h to 67.n.
- **Transfer pricing and recognised interest rate.** Arts. 16 to 19.

For withholding rates, treaty claims (KIDO forms), residence tests, CFC and exit tax, use **si-cross-border**. For related-party pricing and loans, use **si-transfer-pricing**. This skill does not repeat them.

## Worked examples

### Example 1: a profitable d.o.o. with an investment relief (calendar 2026)

A Ljubljana d.o.o. has accounting profit before tax of EUR 300,000 for 2026. In the books it has EUR 20,000 of business entertainment and EUR 2,000 of fines from a labour inspector. It bought production equipment for EUR 100,000 in 2026, with no grant. It has no losses brought forward. Its 2025 return showed a base of EUR 250,000.

1. Add back half the entertainment: EUR 10,000 (ZDDPO-2 art. 31).
2. Add back the fines in full: EUR 2,000 (art. 30(1) point 5).
3. Base before reliefs: 300,000 + 10,000 + 2,000 = EUR 312,000.
4. Investment relief: 40% of EUR 100,000 = EUR 40,000 (art. 55.a).
5. Check the 63% cap: 63% of EUR 312,000 = EUR 196,560. The relief is below the cap (art. 59.a).
6. Taxable base: 312,000 - 40,000 = EUR 272,000.
7. Tax at 22%: EUR 59,840 (ZORZFS art. 64).
8. Advances paid in 2026: 2025 base EUR 250,000 x 22% = EUR 55,000. That is above EUR 400, so it is paid in 12 monthly instalments of EUR 4,583.33 (ZDavP-2 art. 371).
9. Balance due by 30 April 2027: 59,840 - 55,000 = EUR 4,840.

```oa-check
name: d.o.o. with investment relief, calendar 2026
inputs:
  profit: 300000
  entertainment: 20000
  fines: 2000
  investment: 100000
  base_2025: 250000
steps:
  - base: profit + entertainment * 0.5 + fines
  - relief: investment * 0.40
  - cap: base * 0.63
  - allowed: min(relief, cap)
  - taxable: base - allowed
  - tax: taxable * 0.22
  - advances: base_2025 * 0.22
  - monthly: advances / 12
  - balance: tax - advances
expected:
  base: 312000
  relief: 40000
  cap: 196560
  taxable: 272000
  tax: 59840
  advances: 55000
  monthly: 4583.33
  balance: 4840
```

### Example 2: an old loss and R&D relief hit the 50% and 63% caps

A tech company has a 2026 base, before losses and reliefs, of EUR 500,000. It carries an unused tax loss of EUR 400,000 from 2023 and has EUR 150,000 of qualifying R&D spending in 2026, all self-funded.

1. Loss relief is limited to 50% of the base: EUR 250,000 (ZDDPO-2 art. 36(4)). The 2023 loss is an old loss and can be used up to the tax period starting in 2029.
2. Total reductions from losses and reliefs are limited to 63% of the base: EUR 315,000 (art. 59.a).
3. Room left for R&D relief after the loss: 315,000 - 250,000 = EUR 65,000.
4. R&D relief used: EUR 65,000. Unused R&D relief of EUR 85,000 is carried to the next five tax periods (art. 55(2)).
5. Loss carried forward: 400,000 - 250,000 = EUR 150,000.
6. Taxable base: 500,000 - 315,000 = EUR 185,000.
7. Tax at 22%: EUR 40,700.

The law caps the total but does not set an order between losses and reliefs. Here the loss is used first because it expires sooner. The tax is the same either way. Only the amounts carried forward differ.

```oa-check
name: Loss and R&D relief under the 50% and 63% caps (2026)
inputs:
  base: 500000
  loss_bf: 400000
  rnd: 150000
steps:
  - loss_cap: base * 0.50
  - loss_used: min(loss_bf, loss_cap)
  - total_cap: base * 0.63
  - rnd_used: min(rnd, total_cap - loss_used)
  - rnd_cf: rnd - rnd_used
  - loss_cf: loss_bf - loss_used
  - taxable: base - loss_used - rnd_used
  - tax: taxable * 0.22
expected:
  loss_cap: 250000
  loss_used: 250000
  total_cap: 315000
  rnd_used: 65000
  rnd_cf: 85000
  loss_cf: 150000
  taxable: 185000
  tax: 40700
```

## Ask the client first

1. Is the company's seat or effective management in Slovenia, and does it use the calendar year or a different business year?
2. What tax losses are brought forward, and from which years (before 2025 or from 2025)? Has ownership changed by more than 50% in the period?
3. Which investments, R&D projects or green and digital spending happened in the year, and was any of it grant funded?
4. Does the company have related-party loans, or net interest costs above EUR 3 million? Is it part of a consolidated group?
5. What advances were paid in 2026, and what base did the last return show?
6. Is it a medium or large company under the Companies Act (this changes the fine bands)?

## Sources

| Source | URL | Read on |
|---|---|---|
| Corporate Income Tax Act (ZDDPO-2), consolidated text to ZDDPO-2V (UL RS 85/25), arts. 3 to 5, 9 to 12, 19 to 26, 29 to 31, 33, 35, 36, 54.c, 55 to 67, 68, 69 | https://pisrs.si/pregledPredpisa?id=ZAKO4687 | 2026-10-24 |
| Act on Recovery, Development and Provision of Funds (ZORZFS), consolidated to ZORZFS-C (UL RS 57/25), art. 64 | https://pisrs.si/pregledPredpisa?id=ZAKO8910 | 2026-10-24 |
| Tax Procedure Act (ZDavP-2), consolidated, arts. 95, 95.a, 96, 358, 361, 368.a, 370, 371, 372, 374, 397, 398 | https://pisrs.si/pregledPredpisa?id=ZAKO4703 | 2026-10-24 |
| FURS, corporate income tax (DDPO) page, 22% rate for 2024 to 2028 | https://www.fu.gov.si/davki_in_druge_dajatve/podrocja/davek_od_dohodkov_pravnih_oseb_ddpo/ | 2026-10-24 |
| FURS, Pokrivanje davčne izgube (2nd edition, February 2025), five-year rule and old losses | https://www.fu.gov.si/fileadmin/Internet/Davki_in_druge_dajatve/Podrocja/Davek_od_dohodkov_pravnih_oseb/Opis/Pokrivanje_davcne_izgube.doc | 2026-10-24 |

Not yet confirmed: the 2026 late-payment interest rate (ZDavP-2 art. 96 points to the act on statutory default interest, which was not read); whether FURS requires a particular order between loss relief and other reliefs inside the 63% cap; the Pillar Two minimum tax act, which was not read and is not covered here.
