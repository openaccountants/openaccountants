---
name: lu-corporate-tax
description: "Use this skill for Luxembourg corporate income tax on resident companies (SA, SARL, SARL-S, SAS, SCA, SE, cooperatives) and on Luxembourg permanent establishments of foreign companies, for tax year 2026. Covers impôt sur le revenu des collectivités (IRC) at 14% / 16% with the EUR 175,000 to 200,000 band, the 7% contribution au fonds pour l'emploi, municipal business tax (impôt commercial communal, ICC) with the EUR 17,500 allowance and the Luxembourg City 225% multiplier, the combined 23.87% rate, net wealth tax and minimum net wealth tax, participation exemption (art. 166 LIR), 17-year loss carry-forward, fiscal unity (art. 164bis), interest limitation (art. 168bis), CFC rules, filing and quarterly advances, penalties, and dividend withholding tax. Trigger on: 'Luxembourg corporate tax', 'IRC Luxembourg', 'SARL tax', 'Soparfi', 'intégration fiscale'. Out of scope: individuals (luxembourg-income-tax), VAT (luxembourg-vat-return), payroll (luxembourg-payroll), social security (luxembourg-social-contributions), planning (luxembourg-tax-optimization), funds and securitisation vehicles."
jurisdiction: LU
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-22
version: 0.1
verified_by: pending
---

# Luxembourg corporate income tax (tax year 2026)

A Luxembourg company pays three taxes on its profit and one on its net assets:

- **IRC** (impôt sur le revenu des collectivités), the state corporate income tax, under the income tax law (LIR, loi modifiée du 4 décembre 1967).
- **The employment fund contribution** (contribution au fonds pour l'emploi), a 7% surcharge on the IRC.
- **ICC** (impôt commercial communal), the municipal business tax, set by each commune.
- **Net wealth tax** (impôt sur la fortune, IF) on net assets on 1 January, with a minimum amount set by balance sheet size.

All four are assessed and collected by the Administration des contributions directes (ACD). The tax year is the calendar year.

Related skills in this pack: [luxembourg-income-tax](luxembourg-income-tax.md) (individuals and sole traders), [luxembourg-vat-return](luxembourg-vat-return.md), [luxembourg-payroll](luxembourg-payroll.md), [luxembourg-social-contributions](luxembourg-social-contributions.md), [luxembourg-tax-optimization](luxembourg-tax-optimization.md) (self-employed versus SARL choice).

## Who this applies to

**Resident companies (art. 159 LIR).** A collective body is resident if its registered office (siège statutaire) **or** its central administration is in Luxembourg. Residents pay IRC on their worldwide income. Art. 159 lists the bodies in scope:

- capital companies: société anonyme (SA), société par actions simplifiée (SAS), société en commandite par actions (SCA), société à responsabilité limitée (SARL), SARL simplifiée (SARL-S), and the European company (SE);
- cooperatives and agricultural associations;
- mutual insurance associations, pension savings associations and pension funds;
- foundations, public-utility bodies and non-profit associations (ASBL);
- other private collective bodies whose income is not taxed directly in another taxpayer's hands;
- commercial, industrial or mining businesses of the State, communes and public bodies.

**Non-resident companies (art. 160 LIR).** A company with neither its registered office nor its central administration in Luxembourg pays IRC only on Luxembourg-source income as defined in art. 156, mainly the profit of a Luxembourg permanent establishment (PE). Income that has already suffered Luxembourg withholding tax and is not part of a Luxembourg business is not assessed again (art. 174(2)).

**Out of scope or taxed differently:**

- Partnerships (SNC, SCS, SCSp), GIE and sociétés civiles are transparent for IRC and net wealth tax (art. 175 LIR). Their partners are taxed. A commercial partnership still pays ICC.
- Investment funds (UCI/OPC, SICAV, RAIF meeting art. 48 of the 2016 law), SICARs, securitisation companies and the family wealth company (SPF) have their own regimes. This skill does not cover them.
- Religious congregations pay half the IRC; credit cooperatives pay one third (art. 174(3) and (4)).

## Rates, bands and thresholds

| Item | Rate or amount | Tax year | Source |
|---|---|---|---|
| IRC, taxable income up to EUR 175,000 | 14% | 2025 onwards | [LIR art. 174(1), consolidated text at 1 January 2026](https://impotsdirects.public.lu/dam-assets/fr/legislation/LIR/texte-coordonn-en-vigueur-au-1er-janvier-2026-ver-08052026.pdf); [ACD IRC tariff](https://impotsdirects.public.lu/fr/az/t/tarif-applicable-collectivites/tarif-collect.html) |
| IRC, taxable income from EUR 175,000 to EUR 200,000 | EUR 24,500 plus 30% of the income above EUR 175,000 | 2025 onwards | same |
| IRC, taxable income above EUR 200,000 | 16% | 2025 onwards | same |
| IRC for tax years 2019 to 2024 (for late returns) | 15% up to EUR 175,000; EUR 26,250 plus 31% above EUR 175,000; 17% above EUR 200,000 | 2019 to 2024 | [ACD IRC tariff](https://impotsdirects.public.lu/fr/az/t/tarif-applicable-collectivites/tarif-collect.html) |
| Employment fund contribution | 7% of IRC (1.12 points on the 16% rate) | 2025 onwards | [Guichet.lu, IRC](https://guichet.public.lu/fr/entreprises/fiscalite/impots-benefices/benefices-patrimoine/benefices-societes-capitaux/impot-revenu-collectivites.html); [ACD, overall tax burden](https://impotsdirects.public.lu/fr/az/c/charg_fisc.html) |
| ICC allowance for companies subject to IRC | EUR 17,500 deducted from the business profit | current | [ACD, ICC calculation](https://impotsdirects.public.lu/fr/az/c/calc_comm.html) |
| ICC base rate | 3% of the business profit after the allowance | current | same |
| ICC municipal multiplier, Luxembourg City | 225%, so 6.75% of profit | current | [ACD, overall tax burden](https://impotsdirects.public.lu/fr/az/c/charg_fisc.html); [Guichet.lu, ICC](https://guichet.public.lu/fr/entreprises/fiscalite/impots-benefices/benefices-patrimoine/impots-divers/impot-commercial-communal.html) |
| ICC multipliers elsewhere | set by each commune, generally 200% to 400% | current | [Guichet.lu, ICC](https://guichet.public.lu/fr/entreprises/fiscalite/impots-benefices/benefices-patrimoine/impots-divers/impot-commercial-communal.html) |
| Combined headline rate, Luxembourg City, income above EUR 200,000 | 23.87% (16% + 1.12% + 6.75%) | 2025 onwards | [ACD, overall tax burden](https://impotsdirects.public.lu/fr/az/c/charg_fisc.html) |
| Range of combined rates across communes and income levels | 21.73% to 27.62% | 2025 onwards | [Chamber of Deputies, answer to parliamentary question 3660, 12 March 2026](https://wdocs-pub.chd.lu/docs/exped/2026/03/QP_62533_1773327785492.pdf) |
| Net wealth tax, net wealth up to EUR 500m | 0.5% | 2016 onwards | [ACD, net wealth tax tariff](https://impotsdirects.public.lu/fr/az/t/tarif-applicable-collectivites/tarif-collect-if.html) |
| Net wealth tax, net wealth above EUR 500m | EUR 2,500,000 plus 0.05% of the excess | 2016 onwards | same |
| Minimum net wealth tax, balance sheet total up to EUR 350,000 | EUR 535 | 2025 onwards | same |
| Minimum net wealth tax, balance sheet total above EUR 350,000 up to EUR 2,000,000 | EUR 1,605 | 2025 onwards | same |
| Minimum net wealth tax, balance sheet total above EUR 2,000,000 | EUR 4,815 | 2025 onwards | same |
| Withholding tax on dividends | 15% (17.65% on the net amount if the payer bears the tax) | current | [LIR art. 148](https://impotsdirects.public.lu/dam-assets/fr/legislation/LIR/texte-coordonn-en-vigueur-au-1er-janvier-2026-ver-08052026.pdf) |
| Interest limitation | exceeding borrowing costs deductible up to the higher of 30% of EBITDA or EUR 3m | current | LIR art. 168bis(2) |
| Loss carry-forward | 17 years; no carry-back | losses from financial years closing after 31 Dec 2016 | LIR art. 114(2); [ACD, loss carry-forward](https://impotsdirects.public.lu/fr/az/r/report_perte.html) |
| Participation exemption on dividends | at least 10% or acquisition price at least EUR 1,200,000, held 12 months | current | LIR art. 166(1) |
| Pillar Two | In force for large multinational and domestic groups in scope of Directive (EU) 2022/2523, under the law of 22 December 2023 on minimum effective taxation | 2024 onwards | [ACD, laws passed in 2023](https://impotsdirects.public.lu/fr/legislation/legi23.html) |

**Change ahead.** The government told Parliament on 12 March 2026 that it plans a further one-point cut in the IRC rate from tax year **2027**. No law making that cut was listed by the ACD when this skill was written ([ACD, laws passed in 2026](https://impotsdirects.public.lu/fr/legislation/legi26.html)). For 2026, use 14% / 16%.

**A stale official page.** The Guichet.lu IRC page, last modified 7 April 2026, still shows 15% and 17%. Those are the 2019 to 2024 rates. The consolidated LIR and the ACD tariff page both give 14% and 16% from tax year 2025. Use the law.

## The taxable base

**Starting point.** Taxable profit starts from the commercial balance sheet profit, adjusted under the LIR. The return is filed with the balance sheet, profit and loss account, and fixed asset and depreciation table ([Guichet.lu, IRC](https://guichet.public.lu/fr/entreprises/fiscalite/impots-benefices/benefices-patrimoine/benefices-societes-capitaux/impot-revenu-collectivites.html)).

**Main add-backs:**

- IRC, the employment fund contribution and net wealth tax are not deductible.
- ICC is a non-deductible charge for companies subject to IRC ([ACD, ICC calculation](https://impotsdirects.public.lu/fr/az/c/calc_comm.html)).
- Expenses directly linked to exempt participation income, and write-downs on a participation caused by an exempt distribution, are not deductible (art. 166(5)).
- Exceeding borrowing costs above the art. 168bis cap (below).

**Depreciation.** Fixed assets are depreciated under arts. 29 to 34 LIR. This skill does not reproduce the asset-by-asset rules; read the articles for the asset in question.

**Interest limitation (art. 168bis).** "Exceeding borrowing costs" are borrowing costs less taxable interest income and economically equivalent income. They are deductible up to the higher of:

- 30% of tax EBITDA (net income plus exceeding borrowing costs, plus depreciation under arts. 29 to 34 and write-downs, with exempt income and its linked costs left out); or
- EUR 3 million.

Disallowed costs carry forward with no time limit. Unused interest capacity carries forward for five years, but only when exceeding borrowing costs are above EUR 3 million (art. 168bis(3)). Full deduction applies to financial undertakings and to standalone entities (no consolidated group, no associated enterprise, no foreign PE). A group-ratio escape (equity to total assets) is available on request. Loans taken out before 17 June 2016 and not modified since are grandfathered.

**Participation exemption on dividends (art. 166).** Dividends are exempt when:

- the recipient is a fully taxable resident company (or a Luxembourg PE of an EU parent-subsidiary directive company, a treaty-country company or an EEA company);
- the subsidiary is an EU directive company, a fully taxable resident capital company, or a non-resident capital company fully subject to a tax comparable to IRC; and
- on the date the income is made available, the recipient has held, or commits to hold, for an unbroken 12 months, at least **10%** of the capital or a stake with an acquisition price of at least **EUR 1,200,000**.

If the 12-month hold is not completed, the exemption is withdrawn by a corrective assessment (art. 166(8)). The exemption is refused for EU directive income that was deductible in the payer's state, and for income paid under a non-genuine arrangement (art. 166(2bis)). A company may waive the exemption where it rests only on the EUR 1.2m acquisition price (art. 166(1), last paragraph).

**Capital gains on participations.** Art. 166(9) lets a grand-ducal regulation extend the exemption to gains on disposal. That regulation was not read for this skill, so its thresholds are not stated here (see "Not yet confirmed").

**Losses (art. 114).** Losses from financial years closing after 31 December 2016 carry forward for **17 years**. The oldest losses are used first. Only the company that made the loss can use it, and it must have kept regular accounts in the loss year. Losses from financial years closed between 1 January 1991 and 31 December 2016 carry forward with no time limit. **No carry-back** ([ACD, loss carry-forward](https://impotsdirects.public.lu/fr/az/r/report_perte.html)). Carried-forward losses also reduce the ICC base ([ACD, ICC calculation](https://impotsdirects.public.lu/fr/az/c/calc_comm.html)).

**Fiscal unity (art. 164bis).** A resident fully taxable capital company (or a Luxembourg PE of a comparable foreign company) can form a tax group with subsidiaries it holds at least **95%**, directly or indirectly. A horizontal group (sister companies under a common parent in the EEA) is also allowed. Conditions:

- The holding must be in place without a break from the start of the first financial year of the group.
- All members must have the same financial year-end.
- The request must reach the ACD before the end of the first financial year of the group, and the group must run for at least **five** financial years (art. 164bis(20)).
- Each member still files its own return; the integrating company aggregates the results (art. 164bis(8) and (9)).
- The 30% / EUR 3m interest cap is applied at group level.
- The minister may allow a 75% holding in exceptional cases (art. 164bis(6)).

Securitisation companies, SICARs and art. 48 RAIFs cannot join a group.

**ICC base.** ICC is charged on the same business profit with ICC-specific adjustments ([ACD, ICC calculation](https://impotsdirects.public.lu/fr/az/c/calc_comm.html)). The main ones:

- add back profit shares and remuneration paid to a silent partner, and partnership losses;
- deduct partnership profit shares, the profit of a foreign PE, and dividends from a holding of at least 10% held at the start of the year;
- deduct carried-forward business losses.

Then deduct the EUR 17,500 allowance, apply 3%, and multiply by the commune's rate.

**Net wealth tax.** Net wealth tax is charged at 1 January each year on unit value (net assets). Real estate counts at historic 1941 unit values ([ACD, taxable wealth](https://impotsdirects.public.lu/fr/az/f/fort_impo.html)). The tax is 0.5% up to EUR 500m.

The **minimum** net wealth tax from tax year 2025 depends only on the total of the last closing balance sheet: EUR 535, EUR 1,605 or EUR 4,815. The minimum is reduced by the IRC plus employment fund contribution due for the year before. If the ordinary 0.5% tax is higher after that reduction, the ordinary tax applies ([ACD, net wealth tax tariff](https://impotsdirects.public.lu/fr/az/t/tarif-applicable-collectivites/tarif-collect-if.html)).

The ordinary net wealth tax can be cut by creating a special reserve of five times the reduction and keeping it for five years ([ACD, net wealth tax reduction](https://impotsdirects.public.lu/fr/az/r/reduc_fortun.html)). The reduction is capped at the previous year's IRC plus employment fund contribution. It cannot take the tax below the minimum.

Before 2025 the minimum was EUR 4,815 for holding-type companies (financial assets over 90% of the balance sheet and over EUR 350,000) and a seven-step scale up to EUR 32,100 for others. Use those figures only for tax years 2017 to 2024.

## Deadlines and filing

| What | Rule | Source |
|---|---|---|
| Return | One combined return for IRC, ICC and net wealth tax: "Déclaration pour l'impôt sur le revenu, l'impôt commercial et l'impôt sur la fortune des collectivités" (form 500). The 2025 return is on Guichet.lu. | [Guichet.lu, IRC](https://guichet.public.lu/fr/entreprises/fiscalite/impots-benefices/benefices-patrimoine/benefices-societes-capitaux/impot-revenu-collectivites.html) |
| Filing deadline | 31 December of the year after the tax year, from tax year 2022. The 2026 return is due by **31 December 2027**. The same deadline applies to the net wealth tax return. | [ACD, filing deadlines](https://impotsdirects.public.lu/fr/az/d/delais/depot.html) |
| Extension | A reasoned request to the tax office | same |
| E-filing | Mandatory electronic filing through MyGuichet.lu for SA, SARL, SARL-S, SAS, SCA and SE. Fields can be prefilled by XML import or API. Cooperatives, foreign-law companies and some others file on paper. | [Guichet.lu, IRC](https://guichet.public.lu/fr/entreprises/fiscalite/impots-benefices/benefices-patrimoine/benefices-societes-capitaux/impot-revenu-collectivites.html) |
| Advance payments | Quarterly, in March, June, September and December. The ACD fixes them from the last assessment and adjusts them automatically or on request. | same |
| Final payment | Within one month of receiving the assessment notice (bulletin). Receipt is presumed on the third working day after posting. | [ACD, payment deadlines](https://impotsdirects.public.lu/fr/az/d/delais/paiement.html) |
| Payment plan | A reasoned request to the tax office before the one month ends | same |

## Penalties and interest

| Item | Amount | Source |
|---|---|---|
| Late or missing return | A surcharge of up to **10%** of the tax due, set by the tax office | [ACD, additional charges](https://impotsdirects.public.lu/fr/az/p/prelev.html) |
| Persistent non-filing | A periodic penalty payment (astreinte) after a final formal deadline; the tax office then estimates the tax (taxation d'office) | same |
| Late payment of tax or an advance | **0.6% per month** on the tax and on any late filing surcharge | same |
| Agreed payment plan | No interest up to 4 months; 0.1% per month for 5 to 12 months; 0.2% per month for 13 months to 3 years; 0.6% per month above 3 years or if an instalment is missed | [ACD, payment deadlines](https://impotsdirects.public.lu/fr/az/d/delais/paiement.html) |

## Cross-border points

**Dividends paid abroad (arts. 146 to 148).** Withholding tax is **15%** on dividends and profit shares paid by a Luxembourg company. If the company bears the tax, the rate is **17.65%** on the net amount paid. No withholding applies (art. 147, number 2) when:

- the recipient is an EU parent-subsidiary directive company, a fully taxable treaty-country company, a Swiss capital company that is not exempt, an EEA company, or a PE of one of these; and
- it holds, or commits to hold, for 12 months at least **10%** or an acquisition price of at least **EUR 1,200,000**.

The exemption is refused for directive income paid under a non-genuine arrangement. SPFs, UCIs, SICARs and art. 48 RAIFs do not withhold (art. 147, number 3). Treaty rates can reduce the 15% where the domestic exemption does not apply.

**Interest and royalties.** Art. 146 lists only dividends, profit shares and profit-participating bond interest. Ordinary interest and royalties paid to a non-resident company bear **no Luxembourg withholding tax** under domestic law. Watch the arm's length test on related-party interest.

**EU directives.** The parent-subsidiary directive (2011/96/EU) is built into arts. 147 and 166. The anti-hybrid and CFC rules come from ATAD.

**CFC rules (art. 164ter).** A foreign company or PE is a CFC when both of these are true:

- the Luxembourg company, alone or with associated enterprises, holds more than 50% of the votes, capital or profit rights; and
- the actual foreign tax paid is less than half the IRC that would be due in Luxembourg.

Out of scope: a CFC with accounting profit of EUR 750,000 or less, or with profit of 10% or less of its operating costs. Only the income from non-genuine arrangements set up for a tax advantage is brought into the Luxembourg base.

**Exit tax.** When a resident company moves its registered office **and** central administration abroad, it is treated as liquidated. Its assets and liabilities are taxed at estimated realisation value (art. 172(1), applying art. 169). Assets that stay with a Luxembourg PE can keep their book values (art. 172(2)). Transfers of assets out of a Luxembourg business or PE, where Luxembourg loses the right to tax, are treated as disposals at estimated realisation value (art. 38).

**Non-resident PEs.** A Luxembourg PE files the same return and pays IRC, the employment fund contribution, ICC and net wealth tax on its Luxembourg assets ([ACD, companies subject to net wealth tax](https://impotsdirects.public.lu/fr/az/c/coll_fortune.html)). Non-resident companies file on paper.

## Worked examples

### Example 1: trading SARL in Luxembourg City

Moselle Trading SARL is resident in Luxembourg City and has a calendar financial year. Its 2026 taxable profit is EUR 500,000, with no losses brought forward, no exempt income and no ICC adjustments.

- IRC: income is above EUR 200,000, so 16% of 500,000 = EUR 80,000.
- Employment fund contribution: 7% of 80,000 = EUR 5,600.
- ICC: (500,000 - 17,500) x 3% x 225% = 482,500 x 6.75% = EUR 32,568.75.
- Total tax on profit: EUR 118,168.75, or 23.63% of profit. That is just below the 23.87% headline rate because of the ICC allowance.

```oa-check
name: Luxembourg City SARL, taxable profit EUR 500,000 (tax year 2026)
inputs:
  profit: 500000
  irc_rate: 0.16
  cfe_rate: 0.07
  icc_allowance: 17500
  icc_base_rate: 0.03
  icc_multiplier: 2.25
steps:
  - irc: profit * irc_rate
  - cfe: irc * cfe_rate
  - icc: (profit - icc_allowance) * icc_base_rate * icc_multiplier
  - total: irc + cfe + icc
  - effective_pct: total / profit * 100
expected:
  irc: 80000.00
  cfe: 5600.00
  icc: 32568.75
  total: 118168.75
  effective_pct: 23.63
```

The company also owes net wealth tax on 1 January and makes quarterly advances. The return for 2026 is due by 31 December 2027.

### Example 2: profit in the middle band, after a loss brought forward

Kirchberg Design SARL is in Luxembourg City. In 2026 its profit before losses is EUR 220,000. It has a EUR 30,000 tax loss from its 2022 financial year, well within the 17-year limit. Its net wealth (unit value) on 1 January 2026 is EUR 800,000.

- Taxable income after the loss: 220,000 - 30,000 = EUR 190,000. This falls between EUR 175,000 and EUR 200,000.
- IRC: 24,500 + 30% x (190,000 - 175,000) = 24,500 + 4,500 = EUR 29,000. That is 15.26% of income, between the 14% and 16% rates.
- Employment fund contribution: 7% of 29,000 = EUR 2,030.
- ICC: the loss also reduces the ICC base. (190,000 - 17,500) x 3% x 225% = EUR 11,643.75.
- Ordinary net wealth tax: 0.5% x 800,000 = EUR 4,000. Its balance sheet total is between EUR 350,000 and EUR 2,000,000, so the minimum is EUR 1,605. The minimum is reduced by the prior year's IRC plus contribution and so does not bite here: the ordinary EUR 4,000 is higher. A net wealth tax reduction reserve could cut the EUR 4,000. It is ignored here.

```oa-check
name: Luxembourg City SARL, EUR 220,000 profit less EUR 30,000 loss, middle IRC band (tax year 2026)
inputs:
  profit_before_losses: 220000
  loss_brought_forward: 30000
  band_start: 175000
  band_base_tax: 24500
  band_rate: 0.30
  cfe_rate: 0.07
  icc_allowance: 17500
  icc_base_rate: 0.03
  icc_multiplier: 2.25
  net_wealth: 800000
  nwt_rate: 0.005
  nwt_minimum: 1605
steps:
  - taxable: profit_before_losses - loss_brought_forward
  - irc: band_base_tax + (taxable - band_start) * band_rate
  - cfe: irc * cfe_rate
  - icc: (taxable - icc_allowance) * icc_base_rate * icc_multiplier
  - profit_taxes: irc + cfe + icc
  - nwt: max(net_wealth * nwt_rate, nwt_minimum)
  - total_with_nwt: profit_taxes + nwt
expected:
  taxable: 190000.00
  irc: 29000.00
  cfe: 2030.00
  icc: 11643.75
  profit_taxes: 42673.75
  nwt: 4000.00
  total_with_nwt: 46673.75
```

The `max` step is a simplification. It holds here because the ordinary tax exceeds the unreduced minimum. Where the minimum is higher, first reduce it by the prior year's IRC plus contribution.

## Ask the client first

1. **Where is the company managed, and in which commune is the business run?** Residence turns on the registered office or central administration. The commune sets the ICC multiplier (225% in Luxembourg City, other communes up to about 400%).
2. **What is the financial year-end, and what is taxable income before losses?** The band (up to EUR 175,000, EUR 175,000 to 200,000, above EUR 200,000) changes the IRC rate.
3. **What losses are carried forward, and from which financial years?** Losses from years closing after 2016 expire after 17 years. Older ones do not expire.
4. **Does the company hold participations or receive dividends?** You need the stake (10% or EUR 1.2m acquisition price), the holding period, and the payer's tax status.
5. **Is it in a group?** A 95% holding opens fiscal unity (five-year commitment). Large groups may be inside Pillar Two.
6. **What was the balance sheet total at the last closing, and how much interest does it pay or receive?** The total sets the minimum net wealth tax. Net interest above EUR 3m triggers the 30% EBITDA cap.

## Sources

| Source | URL | Read on |
|---|---|---|
| LIR, consolidated text in force at 1 January 2026 (ACD, updated 8 May 2026): arts. 38, 114, 146, 147, 148, 159, 160, 164bis, 164ter, 166, 168bis, 172, 174 | https://impotsdirects.public.lu/dam-assets/fr/legislation/LIR/texte-coordonn-en-vigueur-au-1er-janvier-2026-ver-08052026.pdf | 2026-10-22 |
| ACD, IRC tariff by tax year | https://impotsdirects.public.lu/fr/az/t/tarif-applicable-collectivites/tarif-collect.html | 2026-10-22 |
| ACD, net wealth tax and minimum net wealth tax tariff | https://impotsdirects.public.lu/fr/az/t/tarif-applicable-collectivites/tarif-collect-if.html | 2026-10-22 |
| ACD, overall tax burden of companies (charge fiscale globale) | https://impotsdirects.public.lu/fr/az/c/charg_fisc.html | 2026-10-22 |
| ACD, calculation of municipal business tax | https://impotsdirects.public.lu/fr/az/c/calc_comm.html | 2026-10-22 |
| ACD, loss carry-forward | https://impotsdirects.public.lu/fr/az/r/report_perte.html | 2026-10-22 |
| ACD, companies subject to net wealth tax | https://impotsdirects.public.lu/fr/az/c/coll_fortune.html | 2026-10-22 |
| ACD, taxable wealth | https://impotsdirects.public.lu/fr/az/f/fort_impo.html | 2026-10-22 |
| ACD, net wealth tax reduction | https://impotsdirects.public.lu/fr/az/r/reduc_fortun.html | 2026-10-22 |
| ACD, filing deadlines | https://impotsdirects.public.lu/fr/az/d/delais/depot.html | 2026-10-22 |
| ACD, payment deadlines | https://impotsdirects.public.lu/fr/az/d/delais/paiement.html | 2026-10-22 |
| ACD, late filing surcharge, penalty payment and late interest | https://impotsdirects.public.lu/fr/az/p/prelev.html | 2026-10-22 |
| ACD, laws passed in 2023 (minimum effective taxation law of 22 December 2023) | https://impotsdirects.public.lu/fr/legislation/legi23.html | 2026-10-22 |
| ACD, laws passed in 2025 | https://impotsdirects.public.lu/fr/legislation/legi25.html | 2026-10-22 |
| ACD, laws passed in 2026 | https://impotsdirects.public.lu/fr/legislation/legi26.html | 2026-10-22 |
| Guichet.lu, corporate income tax (rates shown are the pre-2025 rates; used for filing channel, advances and the 7% contribution only) | https://guichet.public.lu/fr/entreprises/fiscalite/impots-benefices/benefices-patrimoine/benefices-societes-capitaux/impot-revenu-collectivites.html | 2026-10-22 |
| Guichet.lu, municipal business tax | https://guichet.public.lu/fr/entreprises/fiscalite/impots-benefices/benefices-patrimoine/impots-divers/impot-commercial-communal.html | 2026-10-22 |
| Chamber of Deputies, answer to parliamentary question 3660 (12 March 2026) on the IRC rate and the planned 2027 cut | https://wdocs-pub.chd.lu/docs/exped/2026/03/QP_62533_1773327785492.pdf | 2026-10-22 |
| Legilux, law of 20 December 2024 (Mémorial A 2024 n° 589) that set the 14% / 16% rates | https://legilux.public.lu/eli/etat/leg/loi/2024/12/20/a589/jo | Not readable on 2026-10-22 (the page needs JavaScript); the rates were taken from the ACD consolidated LIR, which cites this law under art. 174 |

Not yet confirmed: the thresholds of the capital gains participation exemption (the grand-ducal regulation under art. 166(9) was not read); the maximum amount of the astreinte; the exact day of the month on which quarterly advances fall due; any rounding of the ICC base; payment deferral of exit tax in instalments; the 2027 IRC cut, which is a stated government plan, not yet law.
