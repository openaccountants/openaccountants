---
name: pl-income-tax
description: "Polish personal income tax (PIT) for individuals and the self-employed for tax year 2026. Covers residence, the three tax forms for a sole trader (the 12% and 32% scale with the PLN 30,000 tax-free amount and PLN 120,000 threshold; the 19% flat tax with the PLN 14,100 health deduction limit; ryczałt on revenue at 2% to 17% with the 2026 eligibility limit of EUR 2 million, PLN 8,517,200), the 4% solidarity levy above PLN 1 million, IP Box at 5%, joint filing for spouses and single parents, the main reliefs (child relief, the PLN 85,528 reliefs, losses), the PIT-36, PIT-36L, PIT-28 and PIT-37 returns due 30 April 2027, and monthly or quarterly advances. Trigger on: PIT 2026, skala podatkowa, podatek liniowy, ryczałt, danina solidarnościowa, wspólne rozliczenie, zaliczki PIT, PIT-36. Out of scope: ZUS in pl-zus-contributions; employee withholding in pl-payroll; mandate contracts in pl-civil-law-contracts; non-residents and foreign income in pl-cross-border; shares, crypto and property gains in pl-capital-gains."
version: 2.2
jurisdiction: PL
tax_year: 2026
last_updated: 2026-10-31
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Poland: personal income tax for individuals and the self-employed (2026)

Source-cited draft: not reviewed by an accountant, not for filing. Built by Michael Cutajar and the OpenAccountants team.

This skill covers the annual PIT for an individual resident in Poland, and the choice of tax form for a sole trader (jednoosobowa działalność gospodarcza). It links to the other Poland skills and does not repeat them:

- [pl-zus-contributions](pl-zus-contributions.md): social and health contributions of the self-employed.
- [pl-payroll](pl-payroll.md): monthly withholding on employees, PIT-2, PIT-11.
- [pl-civil-law-contracts](pl-civil-law-contracts.md): mandate and specific-task contracts and board fees.
- [pl-cross-border](pl-cross-border.md): residence tests in detail, non-residents, foreign income and the return relief.
- [pl-capital-gains](pl-capital-gains.md): 19% tax on shares, dividends, interest, crypto and property (PIT-38, PIT-39).

**Which text of the law.** PIT Act (ustawa o podatku dochodowym od osób fizycznych), consolidated text Dz.U. 2026 poz. 592. Later amendments (poz. 203, 424, 779, 846, 1079, 1098, 1123, 1287, 1347, 1354, 1371) were checked and do not change art. 3, 6, 9, 9a, 26, 27, 27f, 30c, 30ca, 30h, 44 or 45. Ryczałt Act (ustawa o zryczałtowanym podatku dochodowym od niektórych przychodów osiąganych przez osoby fizyczne), consolidated text Dz.U. 2025 poz. 843; its only later amendment (Dz.U. 2026 poz. 779) adds a rule on e-signing. Tax Ordinance, Dz.U. 2026 poz. 622.

## Who this applies to

- **Residents.** A person who has their centre of personal or economic interests in Poland, or stays in Poland more than 183 days in the tax year, is taxed on worldwide income (PIT Act art. 3 ust. 1 and 1a). The tax year is the calendar year.
- **Non-residents.** They are taxed only on Polish-source income (art. 3 ust. 2a-2b). See [pl-cross-border](pl-cross-border.md).
- **Sole traders.** Business income (art. 10 ust. 1 pkt 3, art. 14) is taxed on the scale unless the person elects the flat tax or ryczałt (art. 9a). Partners in civil, general and similar partnerships are taxed the same way on their share.
- **Employees and pensioners.** Their income is on the scale. The employer or pension body withholds monthly ([pl-payroll](pl-payroll.md)); they file PIT-37 or accept the tax office's pre-filled return.
- **Out of scope.** Companies (pl-cit-corporate-tax), capital gains (pl-capital-gains), tonnage tax and the tax card.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Scale, income up to PLN 120,000 | 12% minus a tax-reducing amount of PLN 3,600 (so PLN 30,000 is tax-free) | 2026 | https://api.sejm.gov.pl/eli/acts/DU/2026/592/text.pdf (art. 27 ust. 1) |
| Scale, income over PLN 120,000 | PLN 10,800 + 32% of the excess | 2026 | same, art. 27 ust. 1 |
| Flat tax on business income (podatek liniowy) | 19%, no tax-free amount | 2026 | same, art. 30c ust. 1 |
| Flat tax: health contribution deductible from income or as a cost | up to PLN 14,100 | 2026 | https://api.sejm.gov.pl/eli/acts/MP/2025/1274/text.pdf |
| IP Box: qualified income from qualified IP rights | 5% | 2026 | PIT Act art. 30ca ust. 1 |
| Solidarity levy (danina solidarnościowa) | 4% of income above PLN 1,000,000 | 2026 | PIT Act art. 30h |
| Ryczałt rates on revenue (main ones) | 17% liberal professions; 15% listed services (for example legal, accounting, advertising, management consulting); 14% health care, architecture and engineering services; 12% IT services; 10% buying and selling real estate on own account; 8.5% other services, and private rental up to PLN 100,000 (12.5% above); 5.5% production and construction; 3% trade and catering; 2% own processed farm produce | 2026 | https://api.sejm.gov.pl/eli/acts/DU/2025/843/text.pdf (art. 12 ust. 1) |
| Ryczałt eligibility: prior-year revenue not over EUR 2,000,000 | PLN 8,517,200 (EUR rate 4.2586 of 1 October 2025) | 2026 | Ryczałt Act art. 4 ust. 2, art. 6 ust. 4; https://api.nbp.pl/api/exchangerates/rates/a/eur/2025-10-01/?format=json |
| Ryczałt: quarterly payment allowed if prior-year revenue not over EUR 200,000 | PLN 851,720 | 2026 | https://www.podatki.gov.pl/podatki-osobiste/pit/stawki-i-limity |
| Small taxpayer (quarterly advances): prior-year sales not over EUR 2,000,000 | EUR 2,000,000 | 2026 | PIT Act art. 5a pkt 20 |
| Child relief (scale only), per month | PLN 92.67 each for the first and second child; PLN 166.67 for the third; PLN 225 for the fourth and each next | 2026 | PIT Act art. 27f ust. 2 |
| Child relief, one child only: income limit | PLN 112,000 (married couple or single parent); PLN 56,000 (other) | 2026 | PIT Act art. 27f ust. 2 pkt 1 |
| Reliefs for under-26s, returners, parents of four or more, working seniors | exempt up to PLN 85,528 a year | 2026 | PIT Act art. 21 ust. 1 pkt 148, 152-154 |
| Internet deduction | up to PLN 760 | 2026 | PIT Act art. 26 ust. 1 pkt 6a |
| Late payment interest | 10.50% a year from 5 March 2026 | 2026 | https://api.sejm.gov.pl/eli/acts/MP/2026/269/text.pdf |

## The taxable base

**Scale and flat tax.** Income is revenue minus costs of earning it, for each source (art. 9). Business income is booked in the tax ledger (KPiR) or full accounts. Then:
- **Social contributions** (pension, disability, sickness, accident) paid in the year are deducted from income (art. 26 ust. 1 pkt 2) or, for the flat tax, from income under art. 30c ust. 2 pkt 1. The business may instead book them as costs. Contributions paid in another EU or EEA state or Switzerland are deductible too (art. 26 ust. 1 pkt 2a). FP and FS are business costs.
- **Health contribution.** On the scale it is not deductible at all. On the flat tax it is deductible up to PLN 14,100 in 2026, from income or as a cost (art. 30c ust. 2 pkt 2, art. 23 ust. 1 pkt 58).
- **Losses** from a source can be carried forward five years: up to 50% of the loss a year, or one deduction of up to PLN 5,000,000 with the rest under the 50% rule (art. 9 ust. 3).
- **Scale-only reliefs.** Child relief (art. 27f), the internet deduction, rehabilitation spending, donations and the thermal-modernisation relief apply on the scale. The flat tax allows only social contributions, health up to the limit, IKZE payments and certain donations (art. 30c ust. 2).
- **Rounding.** The base and the tax are rounded to whole złoty, with 50 grosze and above rounded up (Tax Ordinance art. 63 § 1).

**Ryczałt.** Tax is on revenue, with no costs (Ryczałt Act art. 12 ust. 2). Revenue can be reduced by social contributions, losses and some scale reliefs (art. 11 ust. 1), and by 50% of the health contribution paid in the year (art. 11 ust. 1a). The rate depends on the activity classification (PKWiU), so check it against art. 12 and the annexes.

**Choosing the form.** The flat tax or ryczałt is chosen by written notice to the tax office by the 20th of the month after the month of the first revenue in the year, or by the end of the year if that revenue comes in December (PIT Act art. 9a ust. 2; Ryczałt Act art. 9 ust. 1). The choice carries over to later years unless it is changed by the same deadline. Without a choice the scale applies.

**Joint filing.** Married couples in community of property for the whole year (or from the wedding) can be taxed jointly: tax is twice the tax on half their combined income (art. 6 ust. 2). A single parent bringing up a child alone pays twice the tax on half of their own income (art. 6 ust. 4c-4d). Joint filing is not allowed if either spouse uses the flat tax or ryczałt in the year, except ryczałt on private rental (art. 6 ust. 8). It needs scale income only.

**Solidarity levy.** The base is the excess over PLN 1,000,000 of income taxed on the scale, the flat tax, capital income (art. 30b) and CFC income (art. 30f), after deducting social contributions and the flat-tax health deduction (art. 30h ust. 2). Ryczałt revenue is not in the base.

## Deadlines and filing

| What | When | Rule |
|---|---|---|
| Choice of flat tax or ryczałt | by the 20th of the month after the first revenue of the year | PIT Act art. 9a ust. 2; Ryczałt Act art. 9 ust. 1 |
| Monthly advance (scale, flat tax) or ryczałt | by the 20th of the following month | PIT Act art. 44 ust. 6; Ryczałt Act art. 21 ust. 1 |
| Quarterly advance (small taxpayers and new businesses) | by the 20th of the month after the quarter | PIT Act art. 44 ust. 3g, 3h, 6; Ryczałt Act art. 21 ust. 1a |
| Advance for December 2026 or Q4 2026 | 20 January 2027 | PIT Act art. 44 ust. 6 |
| Annual return for 2026: PIT-36 (scale with business), PIT-36L (flat tax), PIT-28 (ryczałt), PIT-37 (income only through payers) | 15 February to 30 April 2027; tax due by the same date | PIT Act art. 45 ust. 1 and 1a; Ryczałt Act art. 21 ust. 2 |
| Solidarity levy return (DSF-1) and payment | 30 April 2027 | PIT Act art. 30h ust. 4 |

Under monthly or quarterly advances on the scale, each advance is the tax on income from the start of the year minus advances already due (art. 44 ust. 3). A first-time business owner is exempt from advances in the year after the start year if conditions are met (art. 44 ust. 7a). Returns are filed through e-Urząd Skarbowy (Twój e-PIT).

## Penalties and interest

- **Late payment interest.** 200% of the NBP lombard rate plus 2 points, at least 8% (Tax Ordinance art. 56 § 1): 10.50% a year from 5 March 2026 (M.P. 2026 poz. 269). The reduced rate of 5.25% applies if a correction is filed within 6 months of the return deadline and the tax is paid within 7 days of filing the correction (Tax Ordinance art. 56a § 1).
- **Fiscal Penal Code.** Not filing a return and so understating tax, or filing a false return, is a fiscal offence or petty offence depending on the amount (Fiscal Penal Code art. 54, 56). Persistent late payment is a petty offence (art. 57). A petty-offence fine is 1/10 to 20 times the minimum wage (art. 48 § 1). Filing a valid correction (art. 16a) or a voluntary disclosure (czynny żal, art. 16) and paying the tax removes liability if done before the authority acts.

## Cross-border points

- **Foreign income of a resident.** Under most of Poland's treaties a credit applies: foreign tax is deducted up to the Polish tax on that income (art. 27 ust. 9). Where a treaty exempts the income, it still sets the rate on the rest on the scale (progression, art. 27 ust. 8). The flat tax has its own credit rule (art. 30c ust. 4). Details, the abolition relief and the return relief are in [pl-cross-border](pl-cross-border.md).
- **Non-residents.** They file on Polish-source income only. Withholding on payments to non-residents is in [pl-cross-border](pl-cross-border.md).
- **Social contributions abroad** reduce Polish income (art. 26 ust. 1 pkt 2a). See [pl-zus-contributions](pl-zus-contributions.md) for which country insures.

## Worked examples

### Example 1: sole trader on the scale

Marek pays tax on the scale (PIT-36) and files alone. In 2026 his business revenue is PLN 300,000 and his costs are PLN 100,000, including FP and FS. He paid social contributions of PLN 19,797.84 (12 months of pension, disability and accident on the standard base, PLN 1,649.82 a month) and deducts them from income. His health contribution is not deductible on the scale. He has no children or other reliefs.

Income is PLN 200,000. Less social contributions the base is PLN 180,202.16, rounded to PLN 180,202. Tax is PLN 10,800 plus 32% of the PLN 60,202 above PLN 120,000: PLN 30,064.64, rounded to PLN 30,065. His advances during the year count against this.

```oa-check
name: PL PIT 2026, scale, sole trader, income PLN 200,000
inputs:
  revenue: 300000
  costs: 100000
  social: 19797.84
steps:
  - income: revenue - costs
  - base: round(income - social, 0)
  - tax: round(10800 + (base - 120000) * 0.32, 0)
expected:
  income: 200000
  base: 180202
  tax: 30065
```

### Example 2: flat tax with the health cap and the solidarity levy

Ewa uses the flat tax (PIT-36L). Her 2026 business income is PLN 1,300,000. She paid the same social contributions, PLN 19,797.84, and health contributions far above the cap. Only PLN 14,100 of health is deductible.

The flat-tax base is 1,300,000 - 19,797.84 - 14,100 = PLN 1,266,102.16, rounded to PLN 1,266,102. Tax at 19% is PLN 240,559.38, rounded to PLN 240,559. The solidarity levy base is the same income after those deductions, minus PLN 1,000,000: PLN 266,102.16, rounded to PLN 266,102. The levy at 4% is PLN 10,644, due with DSF-1 by 30 April 2027. She cannot file jointly with her husband because she uses the flat tax.

```oa-check
name: PL PIT 2026, flat 19%, health capped at PLN 14,100, solidarity levy
inputs:
  income: 1300000
  social: 19797.84
  health_cap: 14100
steps:
  - base_exact: income - social - health_cap
  - base: round(base_exact, 0)
  - tax: round(base * 0.19, 0)
  - levy_base: round(base_exact - 1000000, 0)
  - levy: round(levy_base * 0.04, 0)
expected:
  base: 1266102
  tax: 240559
  levy_base: 266102
  levy: 10644
```

## Ask the client first

1. Were they resident in Poland in 2026 (home, family, business, days in Poland)? Did they earn anything abroad?
2. Which tax form did they choose for the business in 2026, and when? What did the business earn in 2025 (ryczałt limit, quarterly advances)?
3. What is the business activity (PKWiU), for the ryczałt rate?
4. Are they married with community of property, or a single parent? Does the spouse use the flat tax or ryczałt?
5. How many children, and the family income, for the child relief? Age under 26, a recent move to Poland, four or more children, or past retirement age?
6. Social and health contributions paid in 2026, losses from 2021-2025, and advances paid.

## Sources

| Source | URL | Read on |
|---|---|---|
| PIT Act, consolidated text Dz.U. 2026 poz. 592 (art. 3, 5a, 6, 9, 9a, 21, 23, 24a, 26, 27, 27f, 30c, 30ca, 30h, 44, 45) | https://api.sejm.gov.pl/eli/acts/DU/2026/592/text.pdf | 2026-10-23 |
| PIT Act amendments after consolidation (none change the articles used; poz. 779 rewords art. 24a ust. 1e on sending books electronically) | https://api.sejm.gov.pl/eli/acts/DU/2026/779/text.pdf | 2026-10-23 |
| Ryczałt Act, consolidated text Dz.U. 2025 poz. 843 (art. 4, 6, 9, 11, 12, 21) | https://api.sejm.gov.pl/eli/acts/DU/2025/843/text.pdf | 2026-10-23 |
| Minister of Finance notice: flat-tax health deduction limit for 2026, M.P. 2025 poz. 1274 | https://api.sejm.gov.pl/eli/acts/MP/2025/1274/text.pdf | 2026-10-23 |
| NBP EUR mid rate, table 190/A/NBP/2025 of 1 October 2025 (4.2586) | https://api.nbp.pl/api/exchangerates/rates/a/eur/2025-10-01/?format=json | 2026-10-23 |
| Ministry of Finance, PIT rates and limits (scale, ryczałt quarterly limit 2026) | https://www.podatki.gov.pl/podatki-osobiste/pit/stawki-i-limity | 2026-10-23 |
| Ministry of Finance, PIT forms (PIT-28, PIT-36, PIT-36L, PIT-37) | https://www.podatki.gov.pl/podatki-osobiste/pit/formularze-pit | 2026-10-23 |
| Tax Ordinance, Dz.U. 2026 poz. 622 (art. 56, 56a, 63) | https://api.sejm.gov.pl/eli/acts/DU/2026/622/text.pdf | 2026-10-23 |
| Minister of Finance notice on late payment interest, M.P. 2026 poz. 269 | https://api.sejm.gov.pl/eli/acts/MP/2026/269/text.pdf | 2026-10-23 |
| Fiscal Penal Code, Dz.U. 2025 poz. 633 (art. 16, 16a, 48, 54, 56, 57) | https://api.sejm.gov.pl/eli/acts/DU/2025/633/text.pdf | 2026-10-23 |

Not yet confirmed: the podatki.gov.pl limits page prints the 1 October 2025 EUR rate as 4.2846 (the 2024 rate) while its PLN 851,720 figure uses 4.2586, the NBP rate; the PLN 8,517,200 ryczałt limit is computed here from the NBP rate, not published by the Ministry. PIT Act art. 24a ust. 1e (as reworded by Dz.U. 2026 poz. 779 from 1 July 2026) requires the KPiR and fixed-asset register to be kept with software and sent to the tax office by the return deadline; the first tax year it applies to was not found in the transitional provisions, so it is left out of the deadlines table. The ryczałt rate list above names the main groups only; the full lists in Ryczałt Act art. 12 decide each activity. The art. 27 ust. 8 and 9 treaty methods and art. 44 ust. 7a conditions were taken from the article headings and not worked through in an example.

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
