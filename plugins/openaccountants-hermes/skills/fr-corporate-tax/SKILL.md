---
name: fr-corporate-tax
description: "French corporate income tax (impôt sur les sociétés, IS) for companies resident in France and for foreign companies with an establishment in France, financial years closing in 2026. Covers the 25% standard rate and the 15% SME rate on the first EUR 42,500 (CGI art. 219), the 3.3% social contribution (art. 235 ter ZC), the exceptional contribution on large companies for the first two years closed from 31 December 2025, the taxable base, the parent-subsidiary regime, losses (EUR 1m plus 50% cap, one-year carry-back), tax consolidation at 95%, the interest cap (EUR 3m or 30%), form 2065, the four acomptes and the balance, penalties, and outbound withholding tax. Trigger on: IS France, impôt sur les sociétés, taux réduit PME, 2065, acompte IS, report en arrière, intégration fiscale, régime mère-fille, contribution exceptionnelle grandes entreprises. Out of scope: CFE and CVAE (fr-cfe), VAT (france-vat-return), transfer pricing (france-transfer-pricing), individual income tax (fr-personal-i"
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/fr-corporate-tax"
  jurisdiction: "FR"
  tax_year: "2026"
  last_updated: "2026-10-23"
  authored_by: "Ryan Duguid"
  trust_label: "Accountant-authored"
  review_status: "pending_review"
---

# France: corporate income tax (impôt sur les sociétés, IS) v0.1

> **General reference only.** This skill is general tax reference material for AI-assisted work. It has not been reviewed for any company's facts. Do not file, pay or take a tax position on it without review by a qualified professional in France.

**Tax year.** Figures are for financial years (exercices) closing in 2026. France taxes companies by financial year, not calendar year. The Code général des impôts (CGI) articles quoted were read on Légifrance on 22 October 2026, in the version in force on that day. Article 219, which sets the rates, was last amended by the 2026 finance law (loi n° 2026-103 du 19 février 2026, art. 15), with effect for years closed from 31 December 2025. Comparing the versions in force on 20 and 22 February 2026 shows that change touched only the accounting-entry condition for participation shares in art. 219-I-a quinquies (shares may now sit in a special subdivision of any securities account, whatever its accounting classification). The rates and the SME conditions were not changed.

**Sibling skills.** The local business taxes (CFE, CVAE and the CET cap) are in `fr-cfe`; do not compute them here. Bookkeeping, the annual closing and non-deductible charges in day-to-day practice are in `fr-business-accounting` and `france-bookkeeping`. Intercompany pricing is in `france-transfer-pricing`. Penalties procedure in an audit is in `fr-tax-audit`. Dividends received by individuals are in `fr-capital-gains`.

## Who this applies to

- **Companies liable by their form.** CGI art. 206-1 makes liable to IS, whatever their purpose, the sociétés anonymes (SA), sociétés en commandite par actions, sociétés à responsabilité limitée (SARL) that have not opted for partnership treatment, cooperatives, and other legal persons carrying on a profit-making activity. The SAS and SASU are joint-stock companies and are taxed the same way.
- **Territorial base.** Under CGI art. 209-I, profits liable to IS are computed "en tenant compte uniquement des bénéfices réalisés dans les entreprises exploitées en France", plus profits that a tax treaty gives France the right to tax. A French company's foreign branch profits are, as a rule, outside the French base. A foreign company is taxed in France on the profits of an enterprise it operates in France, typically through a branch or other establishment.
- **Out of scope here.** Partnerships (sociétés de personnes) and most SCIs are taxed in the hands of their partners unless they opt for IS (CGI art. 206-3 lists the entities that may opt, among them the SNC, the sociétés civiles of art. 8-1°, and the SARL whose single partner is an individual; the option itself is governed by art. 239); see `fr-rental-income` for the SCI. A sole trader (entreprise individuelle) is taxed under income tax: see `fr-income-tax`.
- **Pillar Two.** Groups with consolidated turnover of at least EUR 750 million in at least two of the four preceding years are subject to the minimum tax (CGI art. 223 VJ and 223 VL). This skill does not compute it.

## Rates, bands and thresholds

| Item | Rate or amount | Tax year | Source |
|---|---|---|---|
| Standard IS rate | 25% ("Le taux normal de l'impôt est fixé à 25 %") | Years closed from 31 Dec 2025 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000046868562 |
| SME reduced rate | 15% | Same | Same (art. 219-I-b) |
| Profit taxed at the reduced rate | First EUR 42,500 "de bénéfice imposable par période de douze mois" | Same | Same |
| SME condition 1: turnover of the year, restated to 12 months (summed across the group for a consolidation parent) | Not more than EUR 10 million | Same | Same |
| SME condition 2: capital fully paid up and held continuously at least this share by individuals, or by a company itself so held | 75% | Same | Same |
| Long-term net gains on participation shares (titres de participation) | 0%, with 12% of the gross gain added back as a share of costs (art. 219-I-a quinquies) | Same | Same |
| Social contribution on IS (contribution sociale sur l'IS) | 3.3% of IS after an abatement | 2026 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000031011715 |
| Annual abatement before the 3.3% | EUR 763,000 per 12 months, prorated for a short or long year | 2026 | Same |
| Exemption from the social contribution | Turnover below EUR 7,630,000 AND capital fully paid up and held continuously at least 75% by individuals, or by a company itself so held | 2026 | Same |
| Exceptional contribution on large companies, rate where turnover is below EUR 3 billion | 20.6% of the average IS of the year and the prior year | First two years closed from 31 Dec 2025 | https://www.legifrance.gouv.fr/loda/id/JORFARTI000051168626 |
| Exceptional contribution, rate where turnover is EUR 3 billion or more | 41.2% | Same | Same |
| Exceptional contribution, entry threshold, second year (the year closing in 2026 for a calendar-year company) | French turnover of EUR 1.5 billion or more | Same | Same |
| No quarterly instalments where IS is below | EUR 3,000 | 2026 | https://entreprendre.service-public.gouv.fr/vosdroits/F23575 |
| Late payment interest | 0.20% per month | 2026 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000051213330 |
| Local business taxes on companies (CFE, CVAE) | Not set out here | 2026 | See `fr-cfe` |
| Pillar Two minimum tax | In force (CGI art. 223 VJ, introduced by the 2024 finance law); groups at EUR 750m or more | 2026 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000048846056 |

**The exceptional contribution (contribution exceptionnelle sur les bénéfices des grandes entreprises).** It was created by article 48 of the 2025 finance law (loi n° 2025-127 du 14 février 2025) for the first year closed from 31 December 2025 only. Article 12 of the 2026 finance law extended it. The consolidated text read today says: "Il est institué, au titre des deux premiers exercices clos à compter du 31 décembre 2025, une contribution exceptionnelle". So it **does apply** to the second year, which for a calendar-year company is the year closing 31 December 2026. What the enacted text says for that second year:

- Liable: IS payers with French turnover of EUR 1 billion or more for the first year or the year before, "et à 1,5 milliard d'euros au titre du second exercice". The parent of a tax-consolidated group pays it, on the group's summed turnover.
- Base: the average of the IS due for the year and for the previous year, on all profits taxed at the art. 219 rates, before reductions, credits and tax receivables.
- Rates: 20.6% where turnover is below EUR 3 billion, 41.2% where it is EUR 3 billion or more. The text smooths the rate for turnover between EUR 1.5 billion and EUR 1.6 billion (second year) and between EUR 3 billion and EUR 3.1 billion. The rates in the text are the same for both years.
- No reduction or tax credit may be set against it (part V), and it is not deductible (part VI).
- Payment: an advance payment of 98% of the estimated contribution at the date of the last IS instalment, and the balance by the IS balance date (part VIII).

The BOFiP comment on the extension (ACTU-2026-00097) could not be opened today (see Sources). Rely on the statute above.

## The taxable base

Start from the accounting result and make the tax adjustments on the liasse fiscale.

1. **Add back taxes that are not deductible.** CGI art. 213: "L'impôt sur les sociétés, la contribution sociale mentionnée à l'article 235 ter ZC et l'impôt sur le revenu ne sont pas admis dans les charges déductibles". The exceptional contribution is also non-deductible (art. 48-VI of the 2025 finance law). Other common add-backs, such as luxury spending and excessive pay, are in `fr-business-accounting`.
2. **Interest limitation (CGI art. 212 bis).** For a company outside a tax-consolidated group, net financial charges are deductible up to the higher of "Trois millions d'euros" and "30 % de son résultat" (a tax EBITDA defined in part II of the article). The EUR 3 million is per year, prorated to 12 months. Disallowed charges can be carried forward under part VIII. Groups have their own version of the rule, which is not set out here.
3. **Depreciation.** Tax depreciation follows the accounts; the rules and the EUR 500 small-equipment tolerance are in `france-bookkeeping` and `fr-business-accounting`.
4. **Parent-subsidiary regime (régime mère-fille, CGI art. 145 and 216).** Dividends from a subsidiary are taken out of taxable profit, less a share of costs. Conditions (art. 145): the shares represent "au moins 5 % du capital" of the subsidiary, and are held for two years. A company controlled by non-profit bodies can instead qualify with 2.5% of the capital and 5% of the voting rights, held for five years. Share of costs (art. 216): "5 % du produit total des participations", reduced to 1% for dividends from another member of the same tax-consolidated group held for more than one financial year, and for dividends from an EU or EEA subsidiary that would have met the group conditions for more than one financial year. So 95% of a qualifying dividend is exempt, or 99% within a group.
5. **Gains on participation shares.** Net long-term gains on titres de participation are taxed at 0%, but 12% of the gross gain is added to the taxable result (art. 219-I-a quinquies). A gain is long-term only if the shares were held for at least two years: under CGI art. 39 duodecies-2-a, gains on assets "acquis ou créés depuis moins de deux ans" are short-term and taxed at the normal rate. Gains on property-rich company shares and shares in non-cooperative states are excluded.
6. **Losses carried forward (CGI art. 209-I).** A loss is deducted from the next year's profit "dans la limite d'un montant de 1 000 000 € majoré de 50 % du montant correspondant au bénéfice imposable dudit exercice excédant ce premier montant". The rest carries forward without time limit, under the same cap each year.
7. **Loss carried back (CGI art. 220 quinquies).** On option, a loss can be set against the profit of the year before only, limited to the lower of that year's profit (the undistributed part) and EUR 1,000,000. The tax overpaid becomes a non-taxable receivable on the State. It can be used to pay IS during the next five years and is refunded at the end of five years if unused.
8. **Tax consolidation (intégration fiscale, CGI art. 223 A).** A parent can elect to pay IS for the whole group formed with the companies it holds "95 % au moins du capital", directly or indirectly, continuously through the year. The election runs for five years. Profits and losses of members are pooled.

## Deadlines and filing

| Step | Rule | Source |
|---|---|---|
| Results return | Form 2065 with the liasse fiscale, filed electronically through the professional space. Due within 3 months of the year end; for a year closed on 31 December, by the second working day after 1 May (CGI art. 223) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000034387974 |
| Extra time for e-filing | The administration allows 15 more calendar days. For a year closed on 31 December 2025, the deadline was 20 May 2026 | https://entreprendre.service-public.gouv.fr/vosdroits/F23575 |
| Quarterly instalments (acomptes) | Four instalments on 15 March, 15 June, 15 September and 15 December, on form 2571, paid electronically. Together they equal the IS on the profit of the last closed year (CGI art. 1668-1) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000033836779 |
| Who pays no instalments | A company whose IS is below EUR 3,000, and a company in its first year of activity or first year under IS | F23575; art. 1668-1 |
| Large companies, last instalment | Turnover EUR 250 million to EUR 1 billion: the last instalment must bring the total to at least 95% of the estimated IS for the current year. Turnover above EUR 1 billion: at least 98%. Turnover is summed across a tax-consolidated group. There is no other band (point c of the article is repealed) | art. 1668-1 |
| Balance (solde) | Form 2572, by the 15th day of the 4th month after the year end; for a 31 December year end, 15 May of the next year. Any overpayment is refunded | art. 1668-2; F23575 |
| Year closing 31 December 2026 | By the rules above: instalments 15 March, 15 June, 15 September and 15 December 2026; return due the second working day after 1 May 2027 plus 15 days for e-filing (1 May 2027 is a Saturday, so by our count Tuesday 4 May 2027, or 19 May 2027 with the extra 15 days); balance by 15 May 2027. The administration had not published its 2027 calendar on the pages read today | As above |

## Penalties and interest

| What | Figure | Source |
|---|---|---|
| Late return, no formal notice, or filed within 30 days of a formal notice (mise en demeure) | 10% surcharge on the tax due | CGI art. 1728: https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053546784 |
| Return still not filed 30 days after a formal notice | 40% | Same |
| Hidden activity (activité occulte) | 80% | Same |
| Deliberate failure (manquement délibéré) | 40% of the extra tax | CGI art. 1729: https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000020051904 |
| Abuse of law (abus de droit) | 80%, reduced to 40% where the company was not the main initiator or beneficiary | Same |
| Fraudulent manoeuvres | 80% | Same |
| Late payment of IS | 5% surcharge on the amount paid late | CGI art. 1731: https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000033812315 |
| Late payment interest | 0.20% per month on top of the surcharges ("Le taux de l'intérêt de retard est de 0,20 % par mois") | CGI art. 1727: https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000051213330 |

For the audit procedure, reductions for good faith and the appeal steps, use `fr-tax-audit`.

## Cross-border points

- **Dividends paid abroad.** CGI art. 119 bis-2 levies withholding tax at the art. 187 rate where the beneficial owner has no tax domicile or seat in France. Art. 187-1 sets it at the art. 219 standard rate (25%) for companies, 12.8% for individuals, and 75% for payments into a non-cooperative state or territory (art. 187-2). Treaties usually reduce these rates.
- **EU parent-subsidiary exemption (CGI art. 119 ter).** No withholding on dividends paid to an EU or EEA parent company that has one of the forms listed in Directive 2011/96/EU and has held "10 % au moins du capital" directly for two years or more, or undertakes to do so. The threshold drops to 5% where the parent meets the art. 145 conditions and cannot credit the French tax. The exemption does not apply to a non-genuine arrangement set up mainly for the tax advantage (art. 119 ter-3).
- **Royalties and service fees.** Payments to a non-resident with no permanent installation in France, for intellectual property or for services supplied or used in France, bear withholding at the art. 219 standard rate (CGI art. 182 B-II), or 75% where paid into a non-cooperative state (art. 182 B-III). Royalties between associated EU companies are exempt under CGI art. 182 B bis. Companies are associated, by reference to CGI art. 119 quater, where one holds directly at least 25% of the other's capital, or a third company holds at least 25% of both, for two years without a break or with an undertaking to keep it for two years.
- **Interest.** Under CGI art. 125 A-III a compulsory levy applies to interest paid by a French debtor into a non-cooperative state or territory, whoever the beneficiary is, unless the debtor shows the main purpose and effect of the transactions was not to locate the income there. The rate is 75% (art. 125 A-III bis, 2°). Interest paid to non-residents outside that case is not subject to this levy.
- **Branch profits (CGI art. 115 quinquies).** Profits made in France by a foreign company are deemed distributed each year to shareholders outside France, on the total result after IS, and bear the art. 119 bis-2 withholding at the art. 187 rate. The company can ask for a refund to the extent the amounts exceed its actual distributions, or were paid to shareholders in France. The rule does not apply to a company with its seat in the EU or EEA that is liable there to corporate tax without option or exemption. Treaties often cancel or reduce it.
- **CFC rules (CGI art. 209 B).** A French IS payer that holds more than 50% of a foreign entity, or runs a foreign enterprise, subject to a privileged tax regime is taxed in France on that entity's profits. Under CGI art. 238 A, a regime is privileged if the foreign tax is at least 40% lower than the French tax would have been. The article has exceptions that this skill does not set out; read the article before applying it.
- **Exit tax on companies (CGI art. 221-2).** Moving the seat or an establishment to a State outside the EU or EEA (without the required recovery-assistance agreement) is treated as a cessation: latent gains are taxed at once. For a move within the EU or EEA, the tax on latent gains is paid within two months, either in full or, on the company's express request, one-fifth at once and the rest in equal parts over the next four years.
- **Exceptional contribution.** Treaty credits and other tax credits cannot be set against it (art. 48-V of the 2025 finance law).

## Worked examples

### Example 1: an SME on the reduced rate

A SAS closes its year on 31 December 2026. Turnover is EUR 4,000,000. Its capital is fully paid up and held 100% by two individuals. Taxable profit after all adjustments is EUR 200,000. Both art. 219-I-b conditions are met, so the first EUR 42,500 is taxed at 15% and the rest at 25%. Turnover is below EUR 7,630,000 and the capital test is met, so no social contribution is due. The four 2026 instalments were based on the 2025 tax of EUR 40,000, so the balance due by 15 May 2027 is the difference.

```oa-check
name: SAS, profit EUR 200,000, reduced rate, year closing 31 Dec 2026
inputs:
  profit: 200000
  sme_band: 42500
  instalments_paid: 40000
steps:
  - reduced_part: min(profit, sme_band) * 0.15
  - standard_part: max(profit - sme_band, 0) * 0.25
  - is_due: reduced_part + standard_part
  - balance: is_due - instalments_paid
expected:
  reduced_part: 6375.00
  standard_part: 39375.00
  is_due: 45750.00
  balance: 5750.00
```

### Example 2: losses brought forward and the social contribution

A SA closes its year on 31 December 2026. Turnover is EUR 60,000,000, so the reduced rate does not apply and the company is not exempt from the social contribution. Profit before losses is EUR 12,000,000. Losses brought forward are EUR 9,000,000. Art. 209-I caps the deduction at EUR 1,000,000 plus 50% of the profit above EUR 1,000,000, which is EUR 6,500,000. Taxable profit is EUR 5,500,000 and EUR 2,500,000 of losses carry forward. IS at 25% is EUR 1,375,000. The social contribution is 3.3% of the IS above the EUR 763,000 abatement. Turnover is far below EUR 1.5 billion, so the exceptional contribution does not apply.

```oa-check
name: SA, profit EUR 12m, losses EUR 9m brought forward, social contribution
inputs:
  profit_before_losses: 12000000
  losses_bf: 9000000
  abatement: 763000
steps:
  - loss_cap: 1000000 + max(profit_before_losses - 1000000, 0) * 0.5
  - loss_used: min(losses_bf, loss_cap)
  - taxable: profit_before_losses - loss_used
  - losses_cf: losses_bf - loss_used
  - is_due: taxable * 0.25
  - social_contribution: max(is_due - abatement, 0) * 0.033
  - total: is_due + social_contribution
expected:
  loss_cap: 6500000.00
  loss_used: 6500000.00
  taxable: 5500000.00
  losses_cf: 2500000.00
  is_due: 1375000.00
  social_contribution: 20196.00
  total: 1395196.00
```

## Ask the client first

1. Turnover for the year, restated to 12 months, and whether the company heads a tax-consolidated group (the turnover is then summed). This decides the reduced rate, the social contribution and the exceptional contribution.
2. Who holds the capital, whether it is fully paid up, and whether 75% has been held by individuals continuously through the year.
3. The year-end date and whether the year is shorter or longer than 12 months (the EUR 42,500 band, the EUR 763,000 abatement and the EUR 3 million interest floor are set per 12 months).
4. Losses brought forward by year, and whether a carry-back of this year's loss is wanted.
5. Shareholdings of 5% or more held for two years, intragroup dividends, and any 95% subsidiaries.
6. Payments to non-residents (dividends, royalties, service fees, interest), the recipient's country, and whether it is a non-cooperative state.

## Sources

| Source | URL | Read on |
|---|---|---|
| CGI art. 219 (rates, SME rate, participation gains) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000046868562 | 2026-10-22 |
| CGI art. 235 ter ZC (social contribution) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000031011715 | 2026-10-22 |
| Loi n° 2025-127, art. 48, consolidated as amended by loi n° 2026-103 art. 12 (exceptional contribution) | https://www.legifrance.gouv.fr/loda/id/JORFARTI000051168626 | 2026-10-22 |
| CGI art. 206 (companies liable; option for IS in 206-3) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000054373514 | 2026-10-22 |
| 2026 finance law, art. 15 (change to art. 219) | https://www.legifrance.gouv.fr/loda/id/LEGIARTI000053511649/2026-02-21 | 2026-10-22 |
| CGI art. 219, version in force on 20 February 2026 (compared with the current version) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000046868562/2026-02-20 | 2026-10-22 |
| CGI art. 39 duodecies (short-term and long-term gains, two-year holding) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006307676 | 2026-10-22 |
| CGI art. 209 (territoriality, loss carry-forward) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000048847486 | 2026-10-22 |
| CGI art. 220 quinquies (loss carry-back) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053560738 | 2026-10-22 |
| CGI art. 213 (IS not deductible) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000054373444 | 2026-10-22 |
| CGI art. 212 bis (interest limitation) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000049641637 | 2026-10-22 |
| CGI art. 145 (parent-subsidiary conditions) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000051203497 | 2026-10-22 |
| CGI art. 216 (share of costs) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000048831340 | 2026-10-22 |
| CGI art. 223 A (tax consolidation) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000048834056 | 2026-10-22 |
| CGI art. 223 (results return deadline) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000034387974 | 2026-10-22 |
| CGI art. 1668 (instalments and balance) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000033836779 | 2026-10-22 |
| CGI art. 1727 (late interest) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000051213330 | 2026-10-22 |
| CGI art. 1728 (late filing) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053546784 | 2026-10-22 |
| CGI art. 1729 (inaccuracy penalties) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000020051904 | 2026-10-22 |
| CGI art. 1731 (late payment surcharge) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000033812315 | 2026-10-22 |
| CGI art. 119 bis (withholding on distributions) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000051218411 | 2026-10-22 |
| CGI art. 187 (withholding rates) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000051218440 | 2026-10-22 |
| CGI art. 119 ter (EU parent-subsidiary exemption) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000031815505 | 2026-10-22 |
| CGI art. 182 B (royalties and services withholding) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000045765660 | 2026-10-22 |
| CGI art. 182 B bis (EU royalties exemption) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000039382322 | 2026-10-22 |
| CGI art. 125 A (levy on interest, 75% rate in III bis) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000037526745 | 2026-10-22 |
| CGI art. 119 quater (associated companies, 25%) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006302662 | 2026-10-22 |
| CGI art. 115 quinquies (branch profits) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000042159010 | 2026-10-22 |
| CGI art. 209 B (CFC rules) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000029355796 | 2026-10-22 |
| CGI art. 238 A (privileged tax regime) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000037526846 | 2026-10-22 |
| CGI art. 221 (cessation, exit tax) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000051765018 | 2026-10-22 |
| CGI art. 223 VJ and 223 VL (Pillar Two) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000048846056 and https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000048803788 | 2026-10-22 |
| Service-public.gouv.fr, IS rates, filing and payment (page last checked by its publisher on 17 February 2026) | https://entreprendre.service-public.gouv.fr/vosdroits/F23575 | 2026-10-22 |
| BOFiP, social contribution (BOI-IS-AUT-10-20) | https://bofip.impots.gouv.fr/bofip/3492-PGP.html | Could not be fetched on 2026-10-22 (connection refused, and timed out again on a second attempt); not relied on |
| BOFiP, extension of the exceptional contribution (ACTU-2026-00097) | https://bofip.impots.gouv.fr/bofip/15092-PGP.html/ACTU-2026-00097 | Could not be fetched on 2026-10-22 (timed out again on a second attempt); not relied on |
| impots.gouv.fr, professional IS pages and form 2065 | https://www.impots.gouv.fr/professionnel/impot-sur-les-societes | Site in maintenance on 2026-10-22 (still in maintenance on a second attempt); not relied on |

Not yet confirmed: the conditions of the option for IS under CGI art. 239 (not read today); the interest limitation rules for tax-consolidated groups; and the official 2027 filing calendar for years closed on 31 December 2026 (the dates given above are computed from the statute and the 15-day extension, not taken from a published calendar).

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

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-10-23. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `fr-corporate-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/fr-corporate-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
