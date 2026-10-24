---
name: luxembourg-tax-optimization
description: "Use this skill for lawful tax planning by a Luxembourg resident individual, sole trader or owner of a small company (SARL, SARL-S) for tax year 2026. It covers the sole trader versus company choice (14% / 16% IRC, 7% employment fund contribution, municipal business tax with the EUR 40,000 and EUR 17,500 allowances), paying out profit (15% withholding, 50% dividend exemption), and the reliefs individuals miss: the EUR 4,500 private pension (prévoyance-vieillesse) cap, the EUR 672 cap on interest and insurance premiums, home-savings contracts, employer and self-employed supplementary pensions, the EUR 4,500 extra-professional abatement and the start-up investment credit. It sets the red lines: hidden profit distributions and the anti-abuse rule. Trigger on: reduce tax Luxembourg, SARL or indépendant, SARL-S, third pillar Luxembourg, prévoyance-vieillesse, dépenses spéciales, save tax Luxembourg, tax planning Luxembourg. Out of scope: computing the full tax (luxembourg-income-tax, lu-corporate-tax), payroll (luxembourg-payroll), contributions (luxembourg-social-contributions), non-residents (lu-cross-border)."
version: 0.2
jurisdiction: LU
tax_year: 2026
last_updated: 2026-10-23
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Luxembourg Tax Optimization

## Luxembourg Tax Optimization Skill v0.2

> **Source-cited draft: not reviewed by an accountant.** Built by Michael Cutajar and the OpenAccountants team. Every figure below comes from the LIR text in force on 1 January 2026 (ACD), the ACD and CCSS websites, or Guichet.lu. Aggressive positions are never advised. A Luxembourg tax adviser should check any plan before the client acts on it. This skill is general reference material, not tax, legal or financial advice.

This skill picks the levers. It does not compute the full tax. For that, use the sibling skills:

- `luxembourg-income-tax`: the 2026 scale, tax classes, credits, Form 100.
- `lu-corporate-tax`: IRC, ICC, net wealth tax, participation exemption, interest limitation.
- `luxembourg-payroll`: monthly withholding on a salary paid by the client's company.
- `luxembourg-social-contributions`: CCSS rates and bases for employees and the self-employed.
- `lu-cross-border`: non-residents, frontier workers, treaties, the impatriate regime.

## Who this applies to

- **Resident individuals** (LIR art. 2) who want to lower their personal income tax through special expenses (dépenses spéciales) and abatements.
- **Sole traders and liberal professions** (indépendants: LIR arts. 14 and 91) deciding whether to stay as a sole trader or move the business into a company.
- **Owners of a small resident company** (SARL, SARL-S, SA) deciding how much profit to keep in the company and how to pay the rest out: salary, directors' fees or dividends.

Out of scope: investment funds, SPF, securitisation and holding structures for groups; Pillar Two; real estate and substantial-shareholding gains. Send those to a Luxembourg tax adviser.

**The main lever.** Personal income tax reaches 42% at the top of the scale, plus a 7% or 9% employment fund surcharge. A company in Luxembourg City pays 23.87% at the full rate (16% IRC, 1.12% employment fund, 6.75% ICC). Profit kept and reinvested in a company is taxed at the lower company rate. Profit paid out later as a dividend bears 15% withholding, but only half of it is taxed again in the shareholder's return (art. 115 no. 15a), and the withholding is credited. Below a certain profit, a sole trader who uses every personal relief keeps it simpler.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Personal income tax scale | 0% up to EUR 13,230, rising to 42% above EUR 234,870 (23 bands; see `luxembourg-income-tax`) | 2025 and 2026 | [LIR art. 118, consolidated text at 1 January 2026](https://impotsdirects.public.lu/dam-assets/fr/legislation/LIR/texte-coordonn-en-vigueur-au-1er-janvier-2026-ver-08052026.pdf) |
| Employment fund surcharge, individuals | 7% of the tax; 9% above EUR 150,000 (classes 1, 1a) or EUR 300,000 (class 2) of taxable income | 2026 | [ACD, fonds pour l'emploi](https://impotsdirects.public.lu/fr/az/f/fond_empl.html) |
| Flat minimum for special expenses | EUR 480, covering arts. 109 no. 1 and 1a, 110 no. 4, 111, 111bis and 111ter; replaced by the actual amount when higher | 2026 | LIR art. 113(1) (same URL) |
| Interest (not on the own home) plus life, death, accident, invalidity, sickness and liability insurance premiums | EUR 672 a year in total, plus EUR 672 for a spouse taxed jointly and for each child | 2026 | LIR art. 109(1) no. 1a (same URL) |
| Home-savings contract (épargne-logement) contributions | EUR 1,344 a year if the youngest adult subscriber is 18 to 40 at the start of the year; otherwise EUR 672 (increased for a spouse and each child) | 2026 | LIR art. 111(5) (same URL) |
| Private pension (prévoyance-vieillesse) contract or Luxembourg PEPP sub-account | EUR 4,500 a year per taxpayer, one cap for both kinds of contract | 2026 (law of 19 December 2025) | LIR arts. 111bis(7) and 111ter(7) (same URL) |
| Employee's own contributions to an employer supplementary pension scheme | EUR 1,200 a year | 2026 | LIR art. 110 no. 3 (same URL) |
| Self-employed contributions to an approved supplementary pension scheme | up to 20% of net business income (arts. 10 nos. 1 to 3), on an actuary's certificate | 2026 | LIR art. 110 no. 3a (same URL) |
| Gifts to approved bodies | up to 20% of total net income and EUR 1,000,000; the excess carries forward to the next two tax years | 2026 | LIR art. 109(1) no. 3 (same URL) |
| Extra-professional abatement | EUR 4,500 for spouses taxed jointly who both have professional income; EUR 2,250 each if taxed individually | 2026 | LIR art. 129b(1) (same URL) |
| Investment income taxed by assessment | First EUR 1,500 a year exempt (EUR 3,000 for spouses taxed jointly) | 2026 | LIR art. 115 no. 15 (same URL) |
| Dividends from a fully taxable resident company (or treaty or EU equivalent) | 50% exempt in the shareholder's hands | 2026 | LIR art. 115 no. 15a (same URL) |
| Withholding tax on dividends | 15% (17.65% on the net amount if the company bears it); credited against the shareholder's income tax | 2026 | LIR arts. 148(1) and 154(1) no. 2 (same URL) |
| Start-up investment credit | 20% of the eligible investment in new shares of an innovative start-up (under 5 years old, under 50 staff, balance sheet or turnover up to EUR 10m); at least EUR 10,000 invested in the entity in the year; the part that takes the investor above 30% of the capital is not eligible; credit capped at EUR 100,000 a year | from tax year 2026 (law of 19 December 2025, Mémorial A 2025 n° 617, art. 3) | LIR art. 154quaterdecies (same URL) |
| Abatement for staying in work after pension rights open | up to EUR 9,000 a year (EUR 750 a month) | from tax year 2026 (law of 19 December 2025, Mémorial A 2025 n° 623) | LIR art. 129g (same URL) |
| Interest on the owner's own home (deducted against the rental value, not as a special expense) | in full in the year the rental value is first fixed and the next year; then EUR 4,000 a year for four years, EUR 3,000 a year for five years, then EUR 2,000 a year; each cap is increased by its own amount for a spouse taxed jointly and for each child | from tax year 2024 | LIR art. 98(4); grand-ducal regulation of 12 July 1968 as amended, as stated by [ACD, habitation personnelle](https://impotsdirects.public.lu/fr/az/h/habit_pers.html) |
| IRC, taxable income up to EUR 175,000 | 14% | 2025 onwards | [ACD, IRC tariff](https://impotsdirects.public.lu/fr/az/t/tarif-applicable-collectivites/tarif-collect.html) |
| IRC, EUR 175,000 to 200,000 | EUR 24,500 plus 30% of the income above EUR 175,000 | 2025 onwards | same |
| IRC, above EUR 200,000 | 16% | 2025 onwards | same |
| Employment fund contribution, companies | 7% of the IRC | 2025 onwards | [ACD, charge fiscale](https://impotsdirects.public.lu/fr/az/c/charg_fisc.html) |
| ICC (municipal business tax) allowance | EUR 40,000 for sole traders and partnerships; EUR 17,500 for companies paying IRC | current | [ACD, calcul de l'impôt commercial](https://impotsdirects.public.lu/fr/az/c/calc_comm.html) |
| ICC rate | 3% of profit after the allowance, times the commune's multiplier (225% in Luxembourg City, so 6.75%) | current | same; [ACD, charge fiscale](https://impotsdirects.public.lu/fr/az/c/charg_fisc.html) |
| Combined company rate, Luxembourg City, above EUR 200,000 | 23.87% | 2025 onwards | [ACD, charge fiscale](https://impotsdirects.public.lu/fr/az/c/charg_fisc.html) |
| Minimum net wealth tax, company balance sheet up to EUR 350,000 | EUR 535 (EUR 1,605 up to EUR 2m; EUR 4,815 above) | 2025 onwards | [ACD, IF tariff](https://impotsdirects.public.lu/fr/az/t/tarif-applicable-collectivites/tarif-collect-if.html) |
| Self-employed CCSS rates | Pension 17%, health 5.60%, cash benefits 0.50%, dependency 1.40%, accident 0.65% times a factor | 2026 | [CCSS, paramètres sociaux](https://ccss.public.lu/fr/parametres-sociaux.html) |
| Contribution base, monthly minimum and maximum | EUR 2,703.74 and EUR 13,518.68 from 1 January 2026; EUR 2,771.33 and EUR 13,856.63 from 1 June 2026 | 2026 | same |

## The taxable base

**Sole trader.** Net profit is taxed on the personal scale with all other income of the household. Compulsory CCSS health, accident and pension contributions are deducted in full (art. 110 no. 2). Then come the special expenses in the table above and the abatements. A commercial sole trader also pays ICC, but only on profit above the EUR 40,000 allowance. Liberal professions and individual farming businesses do not pay ICC ([Guichet.lu, ICC](https://guichet.public.lu/fr/entreprises/fiscalite/impots-benefices/benefices-patrimoine/impots-divers/impot-commercial-communal.html)).

**Company.** Profit is taxed at 14% / 16% IRC plus 7% of that, and ICC above a EUR 17,500 allowance. A salary or directors' fee the company pays the owner is a cost for the company and income for the owner. Retained profit stays at the company rate. A dividend is not deductible; the owner pays tax on half of it (art. 115 no. 15a), after 15% withholding which is credited. The company also owes net wealth tax each year, with a minimum by balance sheet size (see `lu-corporate-tax` for how the minimum is reduced by IRC).

**Personal reliefs most clients miss.**

- **Private pension (art. 111bis).** Up to EUR 4,500 a year per person into an approved prévoyance-vieillesse contract, or a Luxembourg PEPP sub-account (art. 111ter). Spouses taxed jointly each get their own cap. The contract must run at least 10 years and pay out between ages 60 and 75. Payout as capital or annual withdrawals is taxed under art. 99 no. 4.
- **Interest and insurance (art. 109(1) no. 1a).** One EUR 672 cap per person covers consumer-loan interest and the listed insurance premiums. It does not cover the private pension, which has its own cap.
- **Home-savings contract (art. 111(1)(c) and (5)).** A separate cap of EUR 1,344 or EUR 672, if the money finances the client's own home.
- **Own-home mortgage interest.** Under art. 98(4) the limits are set by grand-ducal regulation (12 July 1968, as amended). From tax year 2024 interest is deductible in full in the year the home's rental value is first fixed and the year after, then up to EUR 4,000, EUR 3,000 and finally EUR 2,000 a year, each increased by its own amount for a spouse taxed jointly and for each child ([ACD](https://impotsdirects.public.lu/fr/az/h/habit_pers.html)). This is a deduction against the rental value, separate from the EUR 672 cap.
- **Staying in work after pension rights open (art. 129g).** From 2026 a person who meets the conditions for a Luxembourg personal pension but keeps working and does not draw it gets an abatement of up to EUR 9,000 a year (EUR 750 a month), on a certificate from the pension body.
- **Supplementary pensions.** An employee can deduct up to EUR 1,200 of own contributions to the employer's scheme (art. 110 no. 3). A self-employed person can deduct contributions to an approved scheme up to 20% of net business income (art. 110 no. 3a).
- **Couples.** Spouses taxed jointly who both work get a EUR 4,500 extra-professional abatement (art. 129b), capped at the lower earner's net income from work.
- **Start-up credit.** From 2026 a resident who subscribes at least EUR 10,000 in new, fully paid shares of a qualifying start-up gets a credit of 20% of the eligible amount, capped at EUR 100,000 a year (art. 154quaterdecies). The start-up must be innovative (at least two full-time staff and R&D of at least 15% of operating costs, certified). The client cannot claim it for the client's own company: a founder, or anyone employed by the start-up, is excluded, and so are shares held as business assets. The shares must be held three years. Credit above the tax due carries forward; it is not refunded.

**Red lines (do not cross).**

- **Hidden profit distributions.** Any advantage a shareholder gets from the company that an outsider would not get (pay above market, private costs, interest-free loans) is a hidden distribution. It is added back to the company's taxable income (art. 164(3)).
- **Anti-abuse rule.** The law of 21 December 2018 transposed the EU anti-tax-avoidance directive (2016/1164) and amended the Steueranpassungsgesetz ([ACD, laws of 2018](https://impotsdirects.public.lu/fr/legislation/legi18.html)). An arrangement put in place mainly for a tax advantage, without valid commercial reasons, can be set aside.
- **Substance.** A company is resident if its registered office or central administration is in Luxembourg (art. 159). A company with no real activity behind it is exposed to the anti-abuse rule.
- **Private pension surrender.** Taking the private pension savings back before age 60 or before 10 years (other than for invalidity or serious illness) makes the whole amount taxable (art. 111bis(6)).

**Prohibitions.**

- NEVER advise taking profit out as interest-free loans, private costs or above-market pay to a shareholder. Those are hidden distributions (art. 164(3)).
- NEVER present incorporation as a pure tax play without the substance and anti-abuse warning.
- NEVER contradict the rates in `luxembourg-income-tax`, `lu-corporate-tax` or `luxembourg-social-contributions`. If they differ, the LIR and the CCSS pages win.
- NEVER offer the start-up credit for the client's own company; founders and employees of the start-up are excluded (art. 154quaterdecies(3)).
- NEVER present a plan as final advice. Route it to a Luxembourg tax adviser.

## Deadlines and filing

| Item | Rule | Source |
|---|---|---|
| Individual return (Form 100) | 31 December of the following year; tax year 2026 is due 31 December 2027 | [ACD, délais de dépôt](https://impotsdirects.public.lu/fr/az/d/delais/depot.html) |
| Company return (IRC, ICC, net wealth tax) | 31 December of the following year | same |
| Individual advances | 10 March, 10 June, 10 September, 10 December | LIR art. 135 ([consolidated text](https://impotsdirects.public.lu/dam-assets/fr/legislation/LIR/texte-coordonn-en-vigueur-au-1er-janvier-2026-ver-08052026.pdf)) |
| PEPP sub-account | The provider gives the client a certificate of the year's payments for the return | LIR art. 111ter(8) (same URL) |
| Dividend withholding | Declared and paid by the company; see `lu-corporate-tax` | LIR art. 148 (same URL) |

Payment dates for companies, ICC advances and the dividend withholding return are in `lu-corporate-tax`.

## Penalties and interest

- **Late filing:** a supplement of up to 10% of the tax, and a periodic penalty (astreinte) after a final notice ([ACD, prélèvements supplémentaires](https://impotsdirects.public.lu/fr/az/p/prelev.html)).
- **Late payment:** 0.6% a month at the full rate (same source).
- **Reliefs claimed wrongly:** a surrendered insurance or a home-savings contract cancelled early leads to a corrective assessment of the years already deducted (art. 111(7)). Early surrender of a private pension is taxed in full (art. 111bis(6)).
- **Hidden distribution:** the payment is added back to the company's taxable income (art. 164(3)).

## Cross-border points

- **Non-residents** use the planning levers only through the rules in `lu-cross-border` (the 90% option for assimilation to residents, frontier-worker rules).
- **Foreign dividends** get the 50% exemption only from a company resident in a treaty country and taxed there like the IRC, or from an EU company covered by the parent-subsidiary directive (art. 115 no. 15a).
- **Moving abroad** while holding a company: see `lu-cross-border` for treaty residence and exit points.
- **Start-up credit:** a non-resident taxed in Luxembourg under art. 157ter can also claim it (art. 154quaterdecies(1)).

## Worked examples

Both are 2026 estimates for residents. They show the saving from one lever; they are not full returns.

### Example 1: single self-employed consultant uses the pension and insurance caps

A single consultant, class 1, net profit EUR 90,000. She paid EUR 21,000 of compulsory CCSS health, accident and pension contributions (deductible under art. 110 no. 2). Without planning she claims only the EUR 480 flat special expenses (art. 113).

She now pays EUR 4,500 into a private pension contract (art. 111bis) and has EUR 672 or more of liability and life insurance premiums (art. 109(1) no. 1a). Her special expenses become EUR 5,172, which replaces the EUR 480 flat amount.

**Without:** 90,000 - 21,000 - 480 = 68,520, rounded down to EUR 68,500 (art. 126(2)). Tax on the scale = 8,859.60 + (68,500 - 54,090) x 39% = 14,479.50.

**With:** 90,000 - 21,000 - 5,172 = 63,828, rounded down to EUR 63,800. Tax = 8,859.60 + (63,800 - 54,090) x 39% = 12,646.50.

**Saving:** 1,833.00 of tax, plus the 7% employment fund surcharge on it: **EUR 1,961.31**. Her CII and CI-CO2 credits depend on profit, so they do not change.

```oa-check
name: LU class 1, pension EUR 4,500 and premiums EUR 672 (2026)
inputs:
  profit: 90000
  contributions: 21000
  flat: 480
  pension: 4500
  premiums: 672
steps:
  - taxable_before: floor((profit - contributions - flat) / 50) * 50
  - tax_before: 8859.60 + (taxable_before - 54090) * 0.39
  - taxable_after: floor((profit - contributions - pension - premiums) / 50) * 50
  - tax_after: 8859.60 + (taxable_after - 54090) * 0.39
  - saving: tax_before - tax_after
  - saving_with_surcharge: saving * 1.07
expected:
  taxable_before: 68500
  tax_before: 14479.50
  taxable_after: 63800
  tax_after: 12646.50
  saving: 1833.00
  saving_with_surcharge: 1961.31
```

### Example 2: company in Luxembourg City with profit in the EUR 175,000 to 200,000 band

A SARL in Luxembourg City has taxable profit of EUR 190,000 and the same ICC base. The edge case: income between EUR 175,000 and 200,000 is taxed at a 30% marginal IRC rate, the "catch-up" band that brings the average rate to 16%.

- IRC = 24,500 + (190,000 - 175,000) x 30% = 29,000.
- Employment fund = 7% x 29,000 = 2,030.
- ICC = (190,000 - 17,500) x 3% x 225% = 11,643.75.
- Total company tax = **EUR 42,673.75**. After-tax profit = 147,326.25.
- Each extra euro in this band costs 30% x 1.07 + 6.75% = **38.85%**, about the same as the owner's 39% personal band before surcharge. Paying the owner a market salary that brings company profit down to EUR 175,000 can be neutral or better. Check CCSS contributions on the salary first (`luxembourg-social-contributions`).

If the company pays out the whole after-tax profit as a dividend, it withholds 15% (EUR 22,098.94), and half the dividend (EUR 73,663.13) goes into the owner's taxable income. The withholding is credited against the owner's tax.

```oa-check
name: LU SARL, Luxembourg City, profit EUR 190,000 (2026)
inputs:
  profit: 190000
steps:
  - irc: 24500 + (profit - 175000) * 0.30
  - fund: irc * 0.07
  - icc: (profit - 17500) * 0.03 * 2.25
  - company_tax: irc + fund + icc
  - after_tax: profit - company_tax
  - marginal_rate: 0.30 * 1.07 + 0.03 * 2.25
  - withholding: after_tax * 0.15
  - taxable_half: after_tax * 0.5
expected:
  irc: 29000.00
  fund: 2030.00
  icc: 11643.75
  company_tax: 42673.75
  after_tax: 147326.25
  marginal_rate: 0.3885
  withholding: 22098.94
  taxable_half: 73663.13
```

## Ask the client first

1. Sole trader or company today? If a company, what form (SARL, SARL-S, SA), which commune, and what share does the client hold?
2. Expected profit for 2026, and how much the client needs to live on each year (that is what must come out as salary or dividends).
3. Family situation and tax class; does a spouse work and are you taxed jointly?
4. What do you pay now into a private pension, a home-savings contract, an employer pension, and which insurance premiums and loan interest?
5. Is the business commercial (ICC applies) or a liberal profession (no ICC)?
6. Any plan to invest in a young company, to move abroad, or to sell the business in the next few years?

## Sources

| Source | URL | Read on |
|---|---|---|
| LIR, consolidated text in force on 1 January 2026 (arts. 98, 99, 109, 110, 111, 111bis, 111ter, 113, 115, 118, 126, 129b, 129g, 135, 148, 154, 154quaterdecies, 164) | https://impotsdirects.public.lu/dam-assets/fr/legislation/LIR/texte-coordonn-en-vigueur-au-1er-janvier-2026-ver-08052026.pdf | 2026-10-23 |
| ACD, IRC tariff from 2025 | https://impotsdirects.public.lu/fr/az/t/tarif-applicable-collectivites/tarif-collect.html | 2026-10-23 |
| ACD, net wealth tax tariff and minimum | https://impotsdirects.public.lu/fr/az/t/tarif-applicable-collectivites/tarif-collect-if.html | 2026-10-23 |
| ACD, overall tax burden of a company (23.87%) | https://impotsdirects.public.lu/fr/az/c/charg_fisc.html | 2026-10-23 |
| ACD, calculation of the municipal business tax (EUR 40,000 / 17,500) | https://impotsdirects.public.lu/fr/az/c/calc_comm.html | 2026-10-23 |
| Guichet.lu, impôt commercial communal (who is outside ICC) | https://guichet.public.lu/fr/entreprises/fiscalite/impots-benefices/benefices-patrimoine/impots-divers/impot-commercial-communal.html | 2026-10-23 |
| ACD, fonds pour l'emploi | https://impotsdirects.public.lu/fr/az/f/fond_empl.html | 2026-10-23 |
| ACD, filing deadlines | https://impotsdirects.public.lu/fr/az/d/delais/depot.html | 2026-10-23 |
| ACD, late filing and late payment | https://impotsdirects.public.lu/fr/az/p/prelev.html | 2026-10-23 |
| ACD, own home of the owner (interest limits from tax year 2024) | https://impotsdirects.public.lu/fr/az/h/habit_pers.html | 2026-10-23 |
| Legilux, law of 19 December 2025, Mémorial A 2025 n° 617 (start-up credit, from tax year 2026) | https://legilux.public.lu/eli/etat/leg/loi/2025/12/19/a617/jo | 2026-10-23 |
| Legilux, law of 19 December 2025, Mémorial A 2025 n° 623 (EUR 4,500 pension cap, art. 129g, from tax year 2026) | https://legilux.public.lu/eli/etat/leg/loi/2025/12/19/a623/jo | 2026-10-23 |
| ACD, laws of 2018 (ATAD transposition, law of 21 December 2018) | https://impotsdirects.public.lu/fr/legislation/legi18.html | 2026-10-23 |
| CCSS, social parameters (2026 rates, minimum and maximum base) | https://ccss.public.lu/fr/parametres-sociaux.html | 2026-10-23 |

Not yet confirmed: the own-home interest limits come from the ACD page; the text of the amended grand-ducal regulation of 12 July 1968 on Legilux was not read; the exact provision of the Steueranpassungsgesetz that holds the anti-abuse rule; when a shareholder-manager of a SARL is insured with the CCSS as self-employed rather than as an employee (see `luxembourg-social-contributions`).

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
